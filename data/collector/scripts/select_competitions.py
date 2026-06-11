#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

TABULAR_MARKERS = (
    ".csv",
    ".tsv",
    ".parquet",
    ".feather",
    ".pq",
    ".arrow",
    ".jsonl",
    ".json",
    ".txt",
)
NON_TABULAR_MARKERS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tif",
    ".tiff",
    ".mp4",
    ".avi",
    ".mov",
    ".wav",
    ".flac",
    ".mp3",
    ".dcm",
    ".nii",
    ".zip",
    ".tar",
    ".7z",
)
REQUIRED_COLUMNS = [
    "competition_slug",
    "url",
    "year",
    "summary",
    "teams/participants",
    "reward",
    "difficulty(1-5)",
    "high_quality_fe_notebooks_count",
    "fe_complexity(1-5)",
    "domain",
]
EXTRA_COLUMNS = [
    "category",
    "deadline",
    "dataset_total_gb",
    "tabular_share",
    "is_tabular",
    "size_under_50gb",
    "selection_status",
    "selection_reason",
]


@dataclass(frozen=True)
class CompetitionRow:
    slug: str
    url: str
    deadline: datetime | None
    category: str
    reward: str
    reward_usd: float
    team_count: int


def parse_bool(text: str) -> bool:
    return text.strip().lower() in {"1", "true", "yes", "y"}


def parse_number(text: str | None) -> float:
    if not text:
        return 0.0
    cleaned = "".join(ch for ch in text if ch.isdigit() or ch == ".")
    if not cleaned:
        return 0.0
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


def parse_int(text: str | None) -> int:
    return int(parse_number(text))


def parse_deadline(text: str | None) -> datetime | None:
    if not text:
        return None
    value = text.strip()
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            parsed = datetime.strptime(value, fmt)
            return parsed.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def extract_slug(ref: str) -> str:
    value = (ref or "").strip()
    if not value:
        return ""
    if "kaggle.com/competitions/" not in value:
        return value.rstrip("/").split("/")[-1]
    path = urlparse(value).path.strip("/")
    parts = path.split("/")
    if len(parts) >= 2 and parts[0] == "competitions":
        return parts[1]
    return value.rstrip("/").split("/")[-1]


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv_rows(path: Path, fieldnames: list[str], rows: Iterable[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def load_competitions(path: Path) -> list[CompetitionRow]:
    rows = read_csv_rows(path)
    loaded: list[CompetitionRow] = []
    for row in rows:
        slug = extract_slug(row.get("ref", ""))
        if not slug:
            continue
        loaded.append(
            CompetitionRow(
                slug=slug,
                url=f"https://www.kaggle.com/competitions/{slug}",
                deadline=parse_deadline(row.get("deadline")),
                category=(row.get("category") or "").strip(),
                reward=(row.get("reward") or "").strip(),
                reward_usd=parse_number(row.get("reward")),
                team_count=parse_int(row.get("teamCount")),
            )
        )
    return loaded


def classify_dataset(files_rows: list[dict[str, str]], min_tabular_share: float) -> tuple[bool, float, float]:
    total_bytes = 0
    tabular_bytes = 0
    non_tabular_bytes = 0

    for row in files_rows:
        name = (row.get("name") or "").strip().lower()
        size = parse_int(row.get("size"))
        total_bytes += size
        suffixes = [suffix.lower() for suffix in Path(name).suffixes]
        is_tabular = any(suffix in TABULAR_MARKERS for suffix in suffixes)
        is_non_tabular = any(suffix in NON_TABULAR_MARKERS for suffix in suffixes)
        if is_tabular:
            tabular_bytes += size
        elif is_non_tabular:
            non_tabular_bytes += size

    if total_bytes <= 0:
        return False, 0.0, 0.0

    tabular_share = tabular_bytes / float(total_bytes)
    # Extra guard: avoid selecting mostly non-tabular files unless clear tabular dominance exists.
    is_tabular = tabular_bytes > 0 and tabular_share >= min_tabular_share and tabular_bytes >= non_tabular_bytes
    total_gb = total_bytes / float(1024**3)
    return is_tabular, total_gb, tabular_share


def fetch_or_load_files_csv(slug: str, refresh: bool) -> tuple[list[dict[str, str]], str]:
    cache_path = Path(f"data/collector/data/kaggle/{slug}/metadata/competition_files.csv")
    if cache_path.exists() and not refresh:
        return read_csv_rows(cache_path), "cache"

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["kaggle", "competitions", "files", slug, "--csv", "--page-size", "200"]
    try:
        proc = subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError:
        return [], "kaggle_error"

    lines = [line for line in proc.stdout.splitlines() if line.strip()]
    if not lines:
        return [], "empty"

    cache_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return list(csv.DictReader(lines)), "live"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Select Kaggle competitions for FE dataset collection")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output-csv", required=True)
    parser.add_argument("--output-overview", required=True)
    parser.add_argument("--output-selected", required=True)
    parser.add_argument("--competition-limit", type=int, default=50)
    parser.add_argument("--inspect-limit", type=int, default=250)
    parser.add_argument("--min-teams", type=int, default=300)
    parser.add_argument("--max-dataset-gb", type=float, default=50.0)
    parser.add_argument("--min-tabular-share", type=float, default=0.60)
    parser.add_argument("--category-allowlist", default="Featured,Research,Analytics,Getting Started,Playground")
    parser.add_argument("--only-closed", default="true")
    parser.add_argument("--refresh-files-metadata", default="false")
    return parser


def write_overview(
    output_path: Path,
    rows: list[dict[str, object]],
    selected_slugs: list[str],
    competition_limit: int,
    inspect_limit: int,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    selected_rows = [row for row in rows if row["selection_status"] == "selected"]
    lines = [
        "# Competition Collection Overview",
        "",
        f"- Generated at (UTC): {datetime.now(timezone.utc).isoformat()}",
        f"- Inspected competitions: {len(rows)} (limit={inspect_limit})",
        f"- Selected competitions: {len(selected_slugs)} (target={competition_limit})",
        "",
        "## Selected",
        "",
        "| competition_slug | teams/participants | reward | dataset_total_gb | tabular_share |",
        "|---|---:|---|---:|---:|",
    ]
    for row in selected_rows:
        lines.append(
            "| {slug} | {teams} | {reward} | {gb} | {share} |".format(
                slug=row["competition_slug"],
                teams=row["teams/participants"],
                reward=row["reward"],
                gb=row["dataset_total_gb"],
                share=row["tabular_share"],
            )
        )
    lines.append("")
    lines.append("## Selection Notes")
    lines.append("")
    lines.append(
        "- `summary`, `difficulty(1-5)`, `fe_complexity(1-5)`, `domain` columns are left blank for manual curation."
    )
    lines.append("- `high_quality_fe_notebooks_count` is initialized to `0` and updated after notebook collection.")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = build_parser().parse_args()
    competition_limit = max(1, args.competition_limit)
    inspect_limit = max(1, args.inspect_limit)
    min_teams = max(0, args.min_teams)
    max_dataset_gb = max(0.01, args.max_dataset_gb)
    min_tabular_share = max(0.0, min(1.0, args.min_tabular_share))
    only_closed = parse_bool(args.only_closed)
    refresh_files = parse_bool(args.refresh_files_metadata)

    allowlist = {item.strip().lower() for item in args.category_allowlist.split(",") if item.strip()}
    now_utc = datetime.now(timezone.utc)

    all_competitions = load_competitions(Path(args.input))
    prefiltered: list[CompetitionRow] = []
    for row in all_competitions:
        if row.team_count < min_teams:
            continue
        if allowlist and row.category.lower() not in allowlist:
            continue
        if only_closed and row.deadline and row.deadline > now_utc:
            continue
        prefiltered.append(row)

    prefiltered.sort(
        key=lambda x: (x.team_count, x.reward_usd, x.deadline or datetime.min.replace(tzinfo=timezone.utc)),
        reverse=True,
    )

    output_rows: list[dict[str, object]] = []
    selected_slugs: list[str] = []
    for row in prefiltered[:inspect_limit]:
        selection_status = "rejected"
        selection_reason = "unclassified"
        files_rows, source = fetch_or_load_files_csv(row.slug, refresh=refresh_files)
        if not files_rows:
            selection_status = "rejected"
            selection_reason = f"competition_files_unavailable:{source}"
            is_tabular = False
            total_gb = 0.0
            tabular_share = 0.0
            size_ok = False
        else:
            is_tabular, total_gb, tabular_share = classify_dataset(files_rows, min_tabular_share=min_tabular_share)
            size_ok = total_gb <= max_dataset_gb

            if not is_tabular:
                selection_status = "rejected"
                selection_reason = "non_tabular_or_low_tabular_share"
            elif not size_ok:
                selection_status = "rejected"
                selection_reason = "dataset_too_large"
            elif len(selected_slugs) >= competition_limit:
                selection_status = "overflow"
                selection_reason = "selection_limit_reached"
            else:
                selection_status = "selected"
                selection_reason = "passes_tabular_size_and_popularity_filters"
                selected_slugs.append(row.slug)

        output_row: dict[str, object] = {
            "competition_slug": row.slug,
            "url": row.url,
            "year": row.deadline.year if row.deadline else "",
            "summary": "",
            "teams/participants": row.team_count,
            "reward": row.reward,
            "difficulty(1-5)": "",
            "high_quality_fe_notebooks_count": 0,
            "fe_complexity(1-5)": "",
            "domain": "",
            "category": row.category,
            "deadline": row.deadline.strftime("%Y-%m-%d %H:%M:%S") if row.deadline else "",
            "dataset_total_gb": f"{total_gb:.2f}",
            "tabular_share": f"{tabular_share:.3f}",
            "is_tabular": str(is_tabular).lower(),
            "size_under_50gb": str(size_ok).lower(),
            "selection_status": selection_status,
            "selection_reason": selection_reason,
        }
        output_rows.append(output_row)

    fields = REQUIRED_COLUMNS + EXTRA_COLUMNS
    write_csv_rows(Path(args.output_csv), fieldnames=fields, rows=output_rows)

    selected_path = Path(args.output_selected)
    selected_path.parent.mkdir(parents=True, exist_ok=True)
    selected_path.write_text("\n".join(selected_slugs) + ("\n" if selected_slugs else ""), encoding="utf-8")

    write_overview(
        output_path=Path(args.output_overview),
        rows=output_rows,
        selected_slugs=selected_slugs,
        competition_limit=competition_limit,
        inspect_limit=inspect_limit,
    )

    print(
        "selected={selected} inspected={inspected} prefiltered={prefiltered} raw={raw}".format(
            selected=len(selected_slugs),
            inspected=len(output_rows),
            prefiltered=len(prefiltered),
            raw=len(all_competitions),
        )
    )


if __name__ == "__main__":
    main()
