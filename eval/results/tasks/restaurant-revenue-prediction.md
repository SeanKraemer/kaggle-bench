# Task Report: Restaurant Revenue Prediction

## Status

- Migrated to the action-bank benchmark contract.
- Shared evaluator, validator, and schemas come from `origin/main`'s canonical benchmark implementation.
- Human baseline is finalized and notebook-backed (`human_baseline/work.ipynb`).

## Candidate Bank

- Total candidates: `26`
- Good candidates: `11` (8 core, 3 model-specific)
- Bad candidates: `15` (13 core, 2 model-specific)
- Primary effective good units: `5`
- Represented action types: `10`
- Equivalence groups: `restaurant_date_signal_strategy`, `restaurant_low_card_encoding_strategy`, `restaurant_open_date_cleanup`
- Bad-to-primary ratio: `3.0x` (meets minimum `3x` gate)

## Benchmark Files

- Task bundle: `data/tasks/restaurant-revenue-prediction`
- Primary aggregate report: `eval/results/benchmarks/restaurant-revenue-prediction-primary.md`
- All-scope aggregate report: `eval/results/benchmarks/restaurant-revenue-prediction-all.md`

## Notes

This report is a lightweight branch-local summary. The aggregate benchmark reports are the source of truth for current metrics. Reports should be regenerated after any bank or testcase changes.
