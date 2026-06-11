#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "${ROOT_DIR}"

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  cat <<'EOF'
Usage: data/collector/scripts/collect_competitions_and_notebooks.sh

Wrapper for:
  1) data/collector/scripts/collect_competitions.sh
  2) data/collector/scripts/collect_notebooks.sh

Environment variables:
  COMPETITION_LIMIT  Number of competitions to collect (default: 50)
EOF
  exit 0
fi

echo "INFO: Running competition selection and notebook collection in sequence."

COMPETITION_LIMIT="${COMPETITION_LIMIT:-50}"

COMPETITION_LIMIT="${COMPETITION_LIMIT}" bash "${ROOT_DIR}/data/collector/scripts/collect_competitions.sh"
COMPETITION_LIMIT="${COMPETITION_LIMIT}" bash "${ROOT_DIR}/data/collector/scripts/collect_notebooks.sh"
