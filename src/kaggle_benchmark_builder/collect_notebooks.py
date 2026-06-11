from __future__ import annotations

import argparse
import csv
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import load_dotenv_file

FEATURE_ENGINEERING_PATTERNS = [
    r"feature engineering",
    r"feature_engineering",
    r"groupby\(",
    r"\.agg\(",
    r"rolling\(",
    r"shift\(",
    r"diff\(",
    r"cum(sum|max|min|prod)",
    r"rank\(",
    r"interaction",
    r"polynomialfeatures\(",
    r"targetencoder\(",
    r"woe",
    r"onehotencoder\(",
    r"get_dummies\(",
    r"labelencoder\(",
    r"qcut\(",
    r"cut\(",
]


def _run_kaggle_kernels_csv(competition: str, sort_by: str, page_size: int, page: int) -> list[dict[str, str]]:
    cmd = [
        "kaggle",
        "kernels",
        "list",
        "--competition",
        competition,
        "--sort-by",
        sort_by,
        "--page-size",
        str(page_size),
        "--page",
        str(page),
        "--csv",
    ]
    try:
        proc = subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as exc:
        if exc.stderr:
            print(exc.stderr.strip(), file=sys.stderr)
        raise
    return list(csv.DictReader(proc.stdout.splitlines()))


def _extract_ref(row: dict[str, str]) -> str:
    return (row.get("ref") or row.get("kernelRef") or "").strip()


def _extract_votes(row: dict[str, str]) -> float:
    return float(row.get("totalVotes") or 0.0)


def _to_iso8601(value: str | None) -> str:
    if not value:
        return ""
    text = value.strip()
    if not text:
        return ""
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"

    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        try:
            parsed = datetime.strptime(text, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return ""

    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.isoformat()


def _cache_subdir_for_ref(kernel_ref: str) -> str:
    return kernel_ref.replace("/", "__")


def _read_kernel_source_from_dir(directory: Path) -> tuple[str, str]:
    if not directory.exists():
        return "", ""
    def _file_order_key(path: Path) -> tuple[int, str]:
        suffix = path.suffix.lower()
        if suffix == ".ipynb":
            return (0, path.name.lower())
        if suffix == ".py":
            return (1, path.name.lower())
        return (2, path.name.lower())

    files = sorted([path for path in directory.iterdir() if path.is_file()], key=_file_order_key)
    if not files:
        return "", ""

    merged_parts: list[str] = []
    code_parts: list[str] = []
    for file in files:
        suffix = file.suffix.lower()
        if suffix == ".py":
            text = file.read_text(encoding="utf-8", errors="ignore")
            merged_parts.append(f"[CODE]\n{text}")
            code_parts.append(text)
            continue
        if suffix != ".ipynb":
            continue

        try:
            notebook = json.loads(file.read_text(encoding="utf-8", errors="ignore"))
        except json.JSONDecodeError:
            continue

        for cell in notebook.get("cells", []):
            source = cell.get("source", [])
            if isinstance(source, list):
                text = "".join(source)
            else:
                text = str(source)
            if cell.get("cell_type") == "code":
                merged_parts.append(f"[CODE]\n{text}")
                code_parts.append(text)
            elif cell.get("cell_type") == "markdown":
                merged_parts.append(f"[MARKDOWN]\n{text}")
    return "\n\n".join(merged_parts), "\n".join(code_parts)


def _pull_kernel_source_text(kernel_ref: str, cache_root: Path) -> tuple[str, str]:
    kernel_dir = cache_root / _cache_subdir_for_ref(kernel_ref)
    cached_content, cached_code = _read_kernel_source_from_dir(kernel_dir)
    if cached_content:
        return cached_content, cached_code

    kernel_dir.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(["kaggle", "kernels", "pull", kernel_ref, "--path", str(kernel_dir)], check=True, capture_output=True, text=True)
        return _read_kernel_source_from_dir(kernel_dir)
    except subprocess.CalledProcessError:
        return "", ""


def has_feature_engineering_signal(code_text: str) -> bool:
    lowered = code_text.lower()
    return any(re.search(pattern, lowered) for pattern in FEATURE_ENGINEERING_PATTERNS)


def get_votes_cutoff(competition: str, top_votes_rank: int, ranked_votes: list[float] | None = None) -> float:
    if ranked_votes is None:
        rows = _run_kaggle_kernels_csv(
            competition=competition,
            sort_by="voteCount",
            page_size=max(1, top_votes_rank),
            page=1,
        )
        ranked_votes = sorted((_extract_votes(row) for row in rows), reverse=True)

    if not ranked_votes:
        return 0.0
    idx = min(top_votes_rank, len(ranked_votes)) - 1
    return ranked_votes[idx]


def collect_competition_notebooks(
    competition: str,
    min_count: int,
    votes_rank_cutoff: int,
    score_scan_page_size: int,
    score_scan_max_pages: int,
    votes_rank_relax_step: int,
    votes_rank_relax_max: int,
    kernel_cache_dir: str,
) -> list[dict[str, Any]]:
    score_rows: list[dict[str, str]] = []
    for page in range(1, score_scan_max_pages + 1):
        page_rows = _run_kaggle_kernels_csv(
            competition=competition,
            sort_by="scoreDescending",
            page_size=score_scan_page_size,
            page=page,
        )
        if not page_rows:
            break
        score_rows.extend(page_rows)

    unique_score_rows: list[dict[str, str]] = []
    seen_in_score: set[str] = set()
    for row in score_rows:
        ref = _extract_ref(row)
        if not ref or ref in seen_in_score:
            continue
        seen_in_score.add(ref)
        unique_score_rows.append(row)

    selected: list[dict[str, Any]] = []
    selected_refs: set[str] = set()
    fe_cache: dict[str, tuple[bool, str, str]] = {}
    cache_root = Path(kernel_cache_dir)
    cache_root.mkdir(parents=True, exist_ok=True)

    def _get_fe_eval(ref: str) -> tuple[bool, str, str]:
        cached = fe_cache.get(ref)
        if cached is not None:
            return cached
        content_text, code_only_text = _pull_kernel_source_text(ref, cache_root=cache_root)
        has_fe = bool(code_only_text) and has_feature_engineering_signal(code_only_text)
        fe_cache[ref] = (has_fe, content_text, code_only_text)
        return fe_cache[ref]

    cutoff_rank = max(1, votes_rank_cutoff)
    max_rank = max(cutoff_rank, votes_rank_relax_max)
    relax_step = max(1, votes_rank_relax_step)
    vote_rows = _run_kaggle_kernels_csv(
        competition=competition,
        sort_by="voteCount",
        page_size=max_rank,
        page=1,
    )
    ranked_votes = sorted((_extract_votes(row) for row in vote_rows), reverse=True)
    vote_sorted_rows = sorted(
        [(_extract_votes(row), idx, row) for idx, row in enumerate(unique_score_rows)],
        key=lambda item: item[0],
        reverse=True,
    )
    eligible_idx = 0

    while len(selected) < min_count and cutoff_rank <= max_rank:
        votes_cutoff = get_votes_cutoff(
            competition=competition,
            top_votes_rank=cutoff_rank,
            ranked_votes=ranked_votes,
        )
        newly_eligible: list[tuple[int, dict[str, str]]] = []
        while eligible_idx < len(vote_sorted_rows):
            vote, score_idx, row = vote_sorted_rows[eligible_idx]
            if vote < votes_cutoff:
                break
            newly_eligible.append((score_idx, row))
            eligible_idx += 1

        for _score_idx, row in sorted(newly_eligible, key=lambda item: item[0]):
            if len(selected) >= min_count:
                break
            ref = _extract_ref(row)
            if not ref or ref in selected_refs:
                continue

            has_fe, content_text, _code_only_text = _get_fe_eval(ref)
            if not has_fe:
                continue

            selected_refs.add(ref)
            selected.append(
                {
                    "notebook_ref": ref,
                    "title": (row.get("title") or ref).strip(),
                    "content": content_text,
                    "popularity": _extract_votes(row),
                    "last_run_at": _to_iso8601(row.get("lastRunTime")),
                }
            )
        if eligible_idx >= len(vote_sorted_rows):
            break
        cutoff_rank += relax_step

    if len(selected) < min_count:
        print(
            (
                f"warning: selected notebooks below target for {competition}: "
                f"{len(selected)}/{min_count} (votes_rank_cutoff={votes_rank_cutoff}, relax_max={max_rank})"
            ),
            file=sys.stderr,
        )

    return selected


def main() -> None:
    load_dotenv_file(".env")
    parser = argparse.ArgumentParser(description="Collect Kaggle notebook candidates for a competition")
    parser.add_argument("--competition", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--min-count", type=int, default=30)
    parser.add_argument("--votes-rank-cutoff", type=int, default=30)
    parser.add_argument("--score-scan-page-size", type=int, default=20)
    parser.add_argument("--score-scan-max-pages", type=int, default=20)
    parser.add_argument("--votes-rank-relax-step", type=int, default=10)
    parser.add_argument("--votes-rank-relax-max", type=int, default=120)
    parser.add_argument("--kernel-cache-dir", required=True)
    args = parser.parse_args()

    notebooks = collect_competition_notebooks(
        competition=args.competition,
        min_count=args.min_count,
        votes_rank_cutoff=args.votes_rank_cutoff,
        score_scan_page_size=args.score_scan_page_size,
        score_scan_max_pages=args.score_scan_max_pages,
        votes_rank_relax_step=args.votes_rank_relax_step,
        votes_rank_relax_max=args.votes_rank_relax_max,
        kernel_cache_dir=args.kernel_cache_dir,
    )

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = out_path.with_suffix(out_path.suffix + ".tmp")
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(notebooks, f, ensure_ascii=True, indent=2)
    os.replace(tmp_path, out_path)

    print(
        json.dumps(
            {
                "competition": args.competition,
                "votes_cutoff_rank": args.votes_rank_cutoff,
                "selected_count": len(notebooks),
                "min_count_target": args.min_count,
                "output": str(out_path),
            },
            ensure_ascii=True,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
