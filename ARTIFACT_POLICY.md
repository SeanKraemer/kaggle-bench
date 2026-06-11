# Artifact Policy

This repository keeps source code, schemas, task definitions, small fixtures, human baselines,
and compact result summaries in Git. High-volume generated artifacts and anything covered by
third-party data licenses are excluded, so the repository stays reviewable and never
redistributes Kaggle data or raw model traces.

## Keep in Git

- `agent/` source code and tests.
- `data/schema/` JSON schemas and the canonical action vocabulary.
- `data/tasks/*/task.json`, `candidate_actions.json`, `notes.md`, `testcases/`, and
  `human_baseline/` fixtures (notebooks stored with outputs stripped).
- `data/reports/` registry and collection summaries.
- `eval/` evaluator code, tests, scripts, and the generated summaries under `eval/results/`
  (per-task benchmark reports, benchmark-wide CSVs, SVG figures, HTML dashboard).

## Keep out of Git

- Kaggle and Anthropic API credentials, in any form.
- Downloaded Kaggle competition datasets (`make data` puts them under `.data/`, and
  `data/tasks/*/data/` is ignored). Competition data is licensed by Kaggle per competition;
  this repository ships download tooling and derived metadata only.
- Notebook collection caches under `data/collector/data/`.
- High-volume generated agent outputs under `data/tasks/*/outputs/` — per-run JSON plus
  provenance (prompts, streams, traces, API call logs). These can embed dataset excerpts and
  local-environment details, so they stay local.

## Regenerating results

The committed reports and figures under `eval/results/` were generated from a complete local
set of raw outputs (1,680 runs). `make aggregate` and `make figures` rebuild them, and refuse
to run when `data/tasks/*/outputs/` is absent so a fresh clone cannot overwrite the committed
results with partial data. To reproduce outputs from scratch: download the competition data
(`make data TASK=<slug>`), then run the relevant agent runner against the task bundle, then:

```bash
uv run python eval/scripts/validate_artifacts.py
make aggregate
```
