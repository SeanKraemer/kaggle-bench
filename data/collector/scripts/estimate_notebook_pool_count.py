#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[3]
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from kaggle_benchmark_builder.collect_notebooks import (  # noqa: E402
    _cache_subdir_for_ref,
    _extract_ref,
    _extract_votes,
    _pull_kernel_source_text,
    _run_kaggle_kernels_csv,
    has_feature_engineering_signal,
)
from kaggle_benchmark_builder.config import load_dotenv_file  # noqa: E402


def _scan_score_rows(competition: str, page_size: int, max_pages: int) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for page in range(1, max_pages + 1):
        page_rows = _run_kaggle_kernels_csv(
            competition=competition,
            sort_by="scoreDescending",
            page_size=page_size,
            page=page,
        )
        if not page_rows:
            break
        rows.extend(page_rows)

    unique_rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in rows:
        ref = _extract_ref(row)
        if not ref or ref in seen:
            continue
        seen.add(ref)
        unique_rows.append(row)
    return unique_rows


def _read_ranked_votes_single_page(competition: str, max_rank: int) -> tuple[list[float], int]:
    vote_rows = _run_kaggle_kernels_csv(
        competition=competition,
        sort_by="voteCount",
        page_size=max_rank,
        page=1,
    )
    ranked_votes = sorted((_extract_votes(row) for row in vote_rows), reverse=True)
    return ranked_votes, len(vote_rows)


def _votes_cutoff(ranked_votes: list[float], rank: int) -> float:
    if not ranked_votes:
        return 0.0
    idx = min(max(1, rank), len(ranked_votes)) - 1
    return ranked_votes[idx]


def _dir_has_files(path: Path) -> bool:
    if not path.exists():
        return False
    for p in path.rglob("*"):
        if p.is_file():
            return True
    return False


def estimate_pool(
    competition: str,
    min_count: int,
    votes_rank_cutoff: int,
    score_scan_page_size: int,
    score_scan_max_pages: int,
    votes_rank_relax_step: int,
    votes_rank_relax_max: int,
    kernel_cache_dir: Path,
    skip_fe_eval: bool,
) -> dict[str, Any]:
    score_rows = _scan_score_rows(competition, score_scan_page_size, score_scan_max_pages)
    cutoff_rank = max(1, votes_rank_cutoff)
    max_rank = max(cutoff_rank, votes_rank_relax_max)
    relax_step = max(1, votes_rank_relax_step)

    ranked_votes, vote_rows_retrieved = _read_ranked_votes_single_page(competition, max_rank)
    vote_sorted_rows = sorted(
        [(_extract_votes(row), idx, row) for idx, row in enumerate(score_rows)],
        key=lambda item: item[0],
        reverse=True,
    )

    kernel_cache_dir.mkdir(parents=True, exist_ok=True)
    eligible_refs: set[str] = set()
    fe_pass_refs_in_score_order: list[str] = []
    fe_pass_set: set[str] = set()
    cutoff_trace: list[dict[str, Any]] = []
    eval_cache: dict[str, bool] = {}
    cache_hit_count = 0
    pull_success_count = 0
    pull_failed_count = 0
    eligible_idx = 0

    for rank in range(cutoff_rank, max_rank + 1, relax_step):
        cutoff = _votes_cutoff(ranked_votes, rank)
        newly_eligible: list[tuple[int, dict[str, str], float]] = []
        while eligible_idx < len(vote_sorted_rows):
            vote, score_idx, row = vote_sorted_rows[eligible_idx]
            if vote < cutoff:
                break
            newly_eligible.append((score_idx, row, vote))
            eligible_idx += 1

        newly_eligible_sorted = sorted(newly_eligible, key=lambda item: item[0])
        added_refs = 0
        for _, row, _vote in newly_eligible_sorted:
            ref = _extract_ref(row)
            if not ref or ref in eligible_refs:
                continue
            eligible_refs.add(ref)
            added_refs += 1

            if skip_fe_eval:
                if ref not in fe_pass_set:
                    fe_pass_set.add(ref)
                    fe_pass_refs_in_score_order.append(ref)
                continue

            cached = eval_cache.get(ref)
            if cached is not None:
                has_fe = cached
            else:
                kernel_dir = kernel_cache_dir / _cache_subdir_for_ref(ref)
                had_cache = _dir_has_files(kernel_dir)
                content_text, code_only_text = _pull_kernel_source_text(ref, cache_root=kernel_cache_dir)
                has_fe = bool(code_only_text) and has_feature_engineering_signal(code_only_text)
                eval_cache[ref] = has_fe

                if had_cache:
                    cache_hit_count += 1
                elif content_text or code_only_text:
                    pull_success_count += 1
                else:
                    pull_failed_count += 1

            if has_fe and ref not in fe_pass_set:
                fe_pass_set.add(ref)
                fe_pass_refs_in_score_order.append(ref)

        cutoff_trace.append(
            {
                "rank": rank,
                "votes_cutoff": cutoff,
                "newly_eligible_count": added_refs,
                "eligible_total": len(eligible_refs),
                "fe_pass_total": len(fe_pass_refs_in_score_order),
            }
        )
        if eligible_idx >= len(vote_sorted_rows):
            break

    selected_refs = fe_pass_refs_in_score_order[: max(0, min_count)]
    return {
        "competition": competition,
        "mode": "single_page_votes",
        "settings": {
            "min_count": min_count,
            "votes_rank_cutoff": votes_rank_cutoff,
            "votes_rank_relax_step": votes_rank_relax_step,
            "votes_rank_relax_max": votes_rank_relax_max,
            "score_scan_page_size": score_scan_page_size,
            "score_scan_max_pages": score_scan_max_pages,
            "kernel_cache_dir": str(kernel_cache_dir),
            "skip_fe_eval": skip_fe_eval,
        },
        "score_scan": {
            "unique_rows": len(score_rows),
        },
        "vote_scan": {
            "vote_rows_retrieved": vote_rows_retrieved,
            "max_rank_available": len(ranked_votes),
            "initial_cutoff": _votes_cutoff(ranked_votes, cutoff_rank),
            "final_cutoff": _votes_cutoff(ranked_votes, max_rank),
        },
        "pool": {
            "eligible_by_vote_count": len(eligible_refs),
            "fe_signal_pass_count": len(fe_pass_refs_in_score_order),
            "selected_count_if_run_collect_notebooks": len(selected_refs),
            "would_meet_min_count": len(selected_refs) >= min_count,
        },
        "fe_eval": {
            "evaluated_refs": len(eval_cache) if not skip_fe_eval else len(eligible_refs),
            "cache_hits": cache_hit_count if not skip_fe_eval else 0,
            "pull_successes": pull_success_count if not skip_fe_eval else 0,
            "pull_failures": pull_failed_count if not skip_fe_eval else 0,
        },
        "selected_refs_preview": selected_refs[:20],
        "cutoff_trace": cutoff_trace,
    }


def main() -> None:
    load_dotenv_file(".env")
    parser = argparse.ArgumentParser(
        description="Estimate FE-notebook pool size with current single-page voteCount behavior."
    )
    parser.add_argument("--competition", required=True)
    parser.add_argument("--min-count", type=int, default=30)
    parser.add_argument("--votes-rank-cutoff", type=int, default=100)
    parser.add_argument("--votes-rank-relax-step", type=int, default=1)
    parser.add_argument("--votes-rank-relax-max", type=int, default=120)
    parser.add_argument("--score-scan-page-size", type=int, default=20)
    parser.add_argument("--score-scan-max-pages", type=int, default=40)
    parser.add_argument("--kernel-cache-dir", default=None)
    parser.add_argument("--skip-fe-eval", action="store_true")
    parser.add_argument("--output-json", default=None)
    args = parser.parse_args()

    cache_dir = Path(
        args.kernel_cache_dir
        or f"data/collector/data/kaggle/{args.competition}/notebooks"
    )
    result = estimate_pool(
        competition=args.competition.strip(),
        min_count=max(1, args.min_count),
        votes_rank_cutoff=max(1, args.votes_rank_cutoff),
        score_scan_page_size=max(1, args.score_scan_page_size),
        score_scan_max_pages=max(1, args.score_scan_max_pages),
        votes_rank_relax_step=max(1, args.votes_rank_relax_step),
        votes_rank_relax_max=max(1, args.votes_rank_relax_max),
        kernel_cache_dir=cache_dir,
        skip_fe_eval=args.skip_fe_eval,
    )

    payload = json.dumps(result, ensure_ascii=True, indent=2)
    if args.output_json:
        out_path = Path(args.output_json)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(payload + "\n", encoding="utf-8")
    print(payload)

# Usage example:
# python3 data/collector/scripts/estimate_notebook_pool_count.py \
#   --competition spaceship-titanic \
#   --output-json data/collector/data/kaggle/spaceship-titanic/notebook_pool_estimate.json

if __name__ == "__main__":
    main()
