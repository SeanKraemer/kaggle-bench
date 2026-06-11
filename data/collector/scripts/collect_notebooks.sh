#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "${ROOT_DIR}"

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  cat <<'EOF'
Usage: data/collector/scripts/collect_notebooks.sh

Environment variables:
  COMPETITIONS_TABLE        Path to competition table CSV (default: data/reports/competitions_table.csv)
  SELECTED_SLUGS_PATH       Path to selected slug list (default: data/reports/selected_competitions.txt)
  EXPLICIT_SLUGS            Comma-separated slugs to override table/selected list
  COMPETITION_LIMIT         Number of competitions to process (default: 50)
  MIN_COUNT                 Minimum FE notebooks per competition (default: 30)
  VOTES_RANK_CUTOFF         Vote rank cutoff for threshold selection (default: 100)
  VOTES_RANK_RELAX_STEP     Relaxation step for vote rank cutoff (default: 1)
  VOTES_RANK_RELAX_MAX      Max vote rank cutoff after relaxation (default: 120)
  VOTES_METADATA_PAGE_SIZE  Page size for metadata votes csv (default: max(100, VOTES_RANK_RELAX_MAX))
  SCORE_PAGE_SIZE           Score-scan page size (default: 20)
  SCORE_MAX_PAGES           Score-scan max pages (default: 40)
  UPDATE_COMPETITIONS_TABLE true/false, update high_quality_fe_notebooks_count (default: true)
EOF
  exit 0
fi

if [[ -f ".venv/bin/activate" ]]; then
  # Keep Kaggle CLI/python dependencies consistent with project environment.
  source ".venv/bin/activate"
fi

if ! command -v kaggle >/dev/null 2>&1; then
  echo "ERROR: kaggle CLI not found." >&2
  exit 1
fi

PYTHON_BIN="python3"
if [[ -x "${ROOT_DIR}/.venv/bin/python3" ]]; then
  PYTHON_BIN="${ROOT_DIR}/.venv/bin/python3"
fi

COMPETITIONS_TABLE="${COMPETITIONS_TABLE:-data/reports/competitions_table.csv}"
SELECTED_SLUGS_PATH="${SELECTED_SLUGS_PATH:-data/reports/selected_competitions.txt}"
EXPLICIT_SLUGS="${EXPLICIT_SLUGS:-}"
COMPETITION_LIMIT="${COMPETITION_LIMIT:-50}"
MIN_COUNT="${MIN_COUNT:-30}"
VOTES_RANK_CUTOFF="${VOTES_RANK_CUTOFF:-100}"
VOTES_RANK_RELAX_STEP="${VOTES_RANK_RELAX_STEP:-1}"
VOTES_RANK_RELAX_MAX="${VOTES_RANK_RELAX_MAX:-120}"
VOTES_METADATA_PAGE_SIZE="${VOTES_METADATA_PAGE_SIZE:-${VOTES_RANK_RELAX_MAX}}"
if (( VOTES_METADATA_PAGE_SIZE < 100 )); then
  VOTES_METADATA_PAGE_SIZE=100
fi
SCORE_PAGE_SIZE="${SCORE_PAGE_SIZE:-20}"
SCORE_MAX_PAGES="${SCORE_MAX_PAGES:-40}"
UPDATE_COMPETITIONS_TABLE="${UPDATE_COMPETITIONS_TABLE:-true}"

STATUS_PATH="data/reports/competition_collection_status.tsv"
RUN_SLUGS_PATH="data/reports/notebook_collection_slugs.txt"

resolve_slugs() {
  if [[ -n "${EXPLICIT_SLUGS}" ]]; then
    EXPLICIT_SLUGS="${EXPLICIT_SLUGS}" "${PYTHON_BIN}" -c '
import os
values = [item.strip() for item in os.environ["EXPLICIT_SLUGS"].split(",")]
for value in values:
    if value:
        print(value)
'
    return
  fi

  if [[ -s "${SELECTED_SLUGS_PATH}" ]]; then
    head -n "${COMPETITION_LIMIT}" "${SELECTED_SLUGS_PATH}" | sed "/^$/d"
    return
  fi

  COMPETITIONS_TABLE="${COMPETITIONS_TABLE}" COMPETITION_LIMIT="${COMPETITION_LIMIT}" "${PYTHON_BIN}" -c '
import csv
import os
from pathlib import Path

path = Path(os.environ["COMPETITIONS_TABLE"])
limit = max(1, int(os.environ["COMPETITION_LIMIT"]))
if not path.exists():
    raise SystemExit(f"ERROR: competitions table not found: {path}")

rows = list(csv.DictReader(path.open("r", encoding="utf-8", newline="")))
slugs = []
for row in rows:
    slug = (row.get("competition_slug") or "").strip()
    if not slug:
        continue
    status = (row.get("selection_status") or "").strip().lower()
    if status and status != "selected":
        continue
    slugs.append(slug)
    if len(slugs) >= limit:
        break

for slug in slugs:
    print(slug)
'
}

SLUGS=()
while IFS= read -r slug; do
  [[ -n "${slug}" ]] || continue
  SLUGS+=("${slug}")
done < <(resolve_slugs)
if [[ "${#SLUGS[@]}" -eq 0 ]]; then
  echo "ERROR: no competition slugs resolved." >&2
  exit 1
fi

mkdir -p "data/collector/data/kaggle" "data/reports"
printf "%s\n" "${SLUGS[@]}" > "${RUN_SLUGS_PATH}"
printf "competition_slug\tselected_notebooks_count\tmin_count_target\tvotes_rank_cutoff\tstatus\n" > "${STATUS_PATH}"

for slug in "${SLUGS[@]}"; do
  echo "==> ${slug}"
  comp_dir="data/collector/data/kaggle/${slug}"
  meta_dir="${comp_dir}/metadata"
  kernel_dir="${comp_dir}/notebooks"
  notebooks_json="${comp_dir}/notebooks.json"

  mkdir -p "${meta_dir}" "${kernel_dir}"

  kaggle kernels list \
    --competition "${slug}" \
    --sort-by voteCount \
    --page-size "${VOTES_METADATA_PAGE_SIZE}" \
    --page 1 \
    --csv > "${meta_dir}/votes_metadata.csv"

  PYTHONPATH="${ROOT_DIR}/src" "${PYTHON_BIN}" -m kaggle_benchmark_builder.collect_notebooks \
    --competition "${slug}" \
    --output "${notebooks_json}" \
    --min-count "${MIN_COUNT}" \
    --votes-rank-cutoff "${VOTES_RANK_CUTOFF}" \
    --score-scan-page-size "${SCORE_PAGE_SIZE}" \
    --score-scan-max-pages "${SCORE_MAX_PAGES}" \
    --votes-rank-relax-step "${VOTES_RANK_RELAX_STEP}" \
    --votes-rank-relax-max "${VOTES_RANK_RELAX_MAX}" \
    --kernel-cache-dir "${kernel_dir}"

  count="$(
    "${PYTHON_BIN}" -c 'import json,sys; print(len(json.load(open(sys.argv[1], "r", encoding="utf-8"))))' "${notebooks_json}"
  )"

  status="ok"
  if [[ "${count}" -lt "${MIN_COUNT}" ]]; then
    status="below_min_count"
  fi

  printf "%s\t%s\t%s\t%s\t%s\n" "${slug}" "${count}" "${MIN_COUNT}" "${VOTES_RANK_CUTOFF}" "${status}" >> "${STATUS_PATH}"
done

if [[ "${UPDATE_COMPETITIONS_TABLE}" == "true" && -f "${COMPETITIONS_TABLE}" ]]; then
  COMPETITIONS_TABLE="${COMPETITIONS_TABLE}" STATUS_PATH="${STATUS_PATH}" "${PYTHON_BIN}" -c '
import csv
import os
from pathlib import Path

table_path = Path(os.environ["COMPETITIONS_TABLE"])
status_path = Path(os.environ["STATUS_PATH"])
status_rows = list(csv.DictReader(status_path.open("r", encoding="utf-8", newline=""), delimiter="\t"))
status_map = {
    (row.get("competition_slug") or "").strip(): row
    for row in status_rows
    if (row.get("competition_slug") or "").strip()
}

rows = list(csv.DictReader(table_path.open("r", encoding="utf-8", newline="")))
for row in rows:
    slug = (row.get("competition_slug") or "").strip()
    status = status_map.get(slug)
    if not status:
        continue
    row["high_quality_fe_notebooks_count"] = status.get("selected_notebooks_count", "0")

if rows:
    tmp_path = table_path.with_suffix(table_path.suffix + ".tmp")
    with tmp_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp_path, table_path)
'
fi

echo "Done. Status: ${STATUS_PATH}"
echo "Done. Slugs: ${RUN_SLUGS_PATH}"
