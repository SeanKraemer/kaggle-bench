#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

ROOT_DIR = Path(__file__).resolve().parents[3]
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


def parse_int_list(value: str) -> list[int]:
    parsed = []
    for item in value.split(","):
        text = item.strip()
        if not text:
            continue
        parsed.append(max(1, int(text)))
    if not parsed:
        raise ValueError("list must not be empty")
    return sorted(set(parsed))


def load_slugs(competitions_csv: Path, selected_only: bool, limit: int) -> list[str]:
    if not competitions_csv.exists():
        raise FileNotFoundError(f"competitions csv not found: {competitions_csv}")

    rows = list(csv.DictReader(competitions_csv.open("r", encoding="utf-8", newline="")))
    slugs: list[str] = []
    for row in rows:
        slug = (row.get("competition_slug") or "").strip()
        if not slug:
            continue
        if selected_only:
            status = (row.get("selection_status") or "").strip().lower()
            if status != "selected":
                continue
        slugs.append(slug)
        if len(slugs) >= limit:
            break
    return slugs


@dataclass(frozen=True)
class SweepRow:
    competition_slug: str
    votes_rank_cutoff: int
    selected_notebooks_count: int


def write_csv(path: Path, rows: list[SweepRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["competition_slug", "votes_rank_cutoff", "selected_notebooks_count"],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "competition_slug": row.competition_slug,
                    "votes_rank_cutoff": row.votes_rank_cutoff,
                    "selected_notebooks_count": row.selected_notebooks_count,
                }
            )


def write_report(
    path: Path,
    rows: list[SweepRow],
    cutoffs: list[int],
    min_fe_notebooks: list[int],
    target_pass_rate: float,
) -> dict[str, object]:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Notebook Cutoff Calibration",
        "",
        f"- Generated at (UTC): {datetime.now(timezone.utc).isoformat()}",
        f"- Evaluated cutoffs: {', '.join(map(str, cutoffs))}",
        f"- Evaluated min FE notebook thresholds: {', '.join(map(str, min_fe_notebooks))}",
        "",
        "## Sweep Summary",
        "",
        "| votes_rank_cutoff | min_fe_notebooks | pass_count | total | pass_rate |",
        "|---:|---:|---:|---:|---:|",
    ]

    by_cutoff: dict[int, list[int]] = {cutoff: [] for cutoff in cutoffs}
    for row in rows:
        by_cutoff[row.votes_rank_cutoff].append(row.selected_notebooks_count)

    target_min = max(min_fe_notebooks)
    recommendation: dict[str, object] = {
        "recommended_votes_rank_cutoff": None,
        "target_min_fe_notebooks": target_min,
        "target_pass_rate": target_pass_rate,
    }

    for cutoff in cutoffs:
        counts = by_cutoff.get(cutoff, [])
        total = len(counts)
        for threshold in min_fe_notebooks:
            passes = sum(1 for count in counts if count >= threshold)
            rate = (passes / total) if total else 0.0
            lines.append(f"| {cutoff} | {threshold} | {passes} | {total} | {rate:.3f} |")
            if (
                threshold == target_min
                and recommendation["recommended_votes_rank_cutoff"] is None
                and rate >= target_pass_rate
            ):
                recommendation["recommended_votes_rank_cutoff"] = cutoff

    lines.extend(
        [
            "",
            "## Recommendation",
            "",
            "```json",
            json.dumps(recommendation, ensure_ascii=True, indent=2, sort_keys=True),
            "```",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return recommendation


def main() -> None:
    parser = argparse.ArgumentParser(description="Calibrate votes rank cutoff for FE notebook collection")
    parser.add_argument("--competitions-csv", default="data/reports/competitions_table.csv")
    parser.add_argument("--selected-only", action="store_true")
    parser.add_argument("--competition-limit", type=int, default=10)
    parser.add_argument("--votes-rank-cutoffs", default="50,75,100,125")
    parser.add_argument("--min-fe-notebooks", default="30")
    parser.add_argument("--target-pass-rate", type=float, default=0.8)
    parser.add_argument("--score-scan-page-size", type=int, default=20)
    parser.add_argument("--score-scan-max-pages", type=int, default=40)
    parser.add_argument("--kernel-cache-root", default="data/collector/data/kaggle")
    parser.add_argument("--output-csv", default="data/reports/notebook_cutoff_calibration.csv")
    parser.add_argument("--output-report", default="data/reports/notebook_cutoff_calibration.md")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    collect_fn: Callable[..., list[dict[str, object]]] | None = None
    if not args.dry_run:
        try:
            from kaggle_benchmark_builder.collect_notebooks import collect_competition_notebooks
        except ModuleNotFoundError as exc:
            raise SystemExit(
                "kaggle_benchmark_builder module not found. Run with --dry-run or set PYTHONPATH to include src/."
            ) from exc
        collect_fn = collect_competition_notebooks

    cutoffs = parse_int_list(args.votes_rank_cutoffs)
    min_targets = parse_int_list(args.min_fe_notebooks)
    competition_limit = max(1, args.competition_limit)

    slugs = load_slugs(Path(args.competitions_csv), selected_only=args.selected_only, limit=competition_limit)
    if not slugs:
        raise SystemExit("no competitions to evaluate")

    rows: list[SweepRow] = []
    max_target = max(min_targets)
    for slug in slugs:
        for cutoff in cutoffs:
            if args.dry_run:
                count = 0
            else:
                assert collect_fn is not None
                selected = collect_fn(
                    competition=slug,
                    min_count=max_target,
                    votes_rank_cutoff=cutoff,
                    score_scan_page_size=max(1, args.score_scan_page_size),
                    score_scan_max_pages=max(1, args.score_scan_max_pages),
                    votes_rank_relax_step=1,
                    votes_rank_relax_max=cutoff,
                    kernel_cache_dir=str(Path(args.kernel_cache_root) / slug / "notebooks"),
                )
                count = len(selected)
            rows.append(SweepRow(competition_slug=slug, votes_rank_cutoff=cutoff, selected_notebooks_count=count))

    write_csv(Path(args.output_csv), rows)
    recommendation = write_report(
        path=Path(args.output_report),
        rows=rows,
        cutoffs=cutoffs,
        min_fe_notebooks=min_targets,
        target_pass_rate=max(0.0, min(1.0, args.target_pass_rate)),
    )
    print(
        json.dumps(
            {
                "competitions": len(slugs),
                "rows": len(rows),
                "output_csv": args.output_csv,
                "output_report": args.output_report,
                "recommended_votes_rank_cutoff": recommendation.get("recommended_votes_rank_cutoff"),
            },
            ensure_ascii=True,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
