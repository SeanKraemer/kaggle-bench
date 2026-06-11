#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "${ROOT_DIR}"

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  cat <<'EOF'
Usage: data/collector/scripts/collect_competitions.sh

Environment variables:
  COMPETITION_LIMIT         Number of competitions to select (default: 50)
  INSPECT_LIMIT             Number of prefiltered competitions to inspect files for (default: 250)
  COMPETITIONS_PAGE_SIZE    Kaggle competitions list page size (default: 500)
  MIN_TEAMS                 Minimum team count filter (default: 300)
  MAX_DATASET_GB            Maximum dataset size in GB (default: 50)
  MIN_TABULAR_SHARE         Minimum tabular-bytes share [0,1] (default: 0.60)
  CATEGORY_ALLOWLIST        Comma-separated categories (default: Featured,Research,Analytics,Getting Started,Playground)
  ONLY_CLOSED               true/false, only include competitions past deadline (default: true)
  REFRESH_FILES_METADATA    true/false, force refresh of competition files metadata (default: false)
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

COMPETITION_LIMIT="${COMPETITION_LIMIT:-50}"
INSPECT_LIMIT="${INSPECT_LIMIT:-250}"
COMPETITIONS_PAGE_SIZE="${COMPETITIONS_PAGE_SIZE:-500}"
MIN_TEAMS="${MIN_TEAMS:-300}"
MAX_DATASET_GB="${MAX_DATASET_GB:-50}"
MIN_TABULAR_SHARE="${MIN_TABULAR_SHARE:-0.60}"
CATEGORY_ALLOWLIST="${CATEGORY_ALLOWLIST:-Featured,Research,Analytics,Getting Started,Playground}"
ONLY_CLOSED="${ONLY_CLOSED:-true}"
REFRESH_FILES_METADATA="${REFRESH_FILES_METADATA:-false}"

RAW_PATH="data/collector/data/kaggle/competitions_raw.csv"
TABLE_PATH="data/reports/competitions_table.csv"
OVERVIEW_PATH="data/reports/competitions_overview.md"
SELECTED_PATH="data/reports/selected_competitions.txt"

mkdir -p "data/collector/data/kaggle" "data/reports"
kaggle competitions list --csv --page-size "${COMPETITIONS_PAGE_SIZE}" > "${RAW_PATH}"

"${PYTHON_BIN}" "data/collector/scripts/select_competitions.py" \
  --input "${RAW_PATH}" \
  --output-csv "${TABLE_PATH}" \
  --output-overview "${OVERVIEW_PATH}" \
  --output-selected "${SELECTED_PATH}" \
  --competition-limit "${COMPETITION_LIMIT}" \
  --inspect-limit "${INSPECT_LIMIT}" \
  --min-teams "${MIN_TEAMS}" \
  --max-dataset-gb "${MAX_DATASET_GB}" \
  --min-tabular-share "${MIN_TABULAR_SHARE}" \
  --category-allowlist "${CATEGORY_ALLOWLIST}" \
  --only-closed "${ONLY_CLOSED}" \
  --refresh-files-metadata "${REFRESH_FILES_METADATA}"

echo "Done. Raw list: ${RAW_PATH}"
echo "Done. Competition table: ${TABLE_PATH}"
echo "Done. Selected slugs: ${SELECTED_PATH}"
