# Task Report: ASHRAE Energy Prediction

## Status

- Migrated to the action-bank benchmark contract.
- Shared evaluator, validator, and schemas come from `origin/main`'s canonical benchmark implementation.
- Human baseline is finalized and notebook-backed (`human_baseline/work.ipynb`).

## Candidate Bank

- Total candidates: `35`
- Good candidates: `11` (6 core, 5 model-specific)
- Bad candidates: `24` (11 core, 9 model-specific, 4 validation)
- Primary effective good units: `6`
- Represented action types: `14`
- Bad-to-primary ratio: `4.0x` (exceeds minimum `3x` gate)

## Benchmark Files

- Task bundle: `data/tasks/ashrae-energy-prediction`
- Primary aggregate report: `eval/results/benchmarks/ashrae-energy-prediction-primary.md`
- All-scope aggregate report: `eval/results/benchmarks/ashrae-energy-prediction-all.md`

## Notes

This report is a lightweight branch-local summary. The aggregate benchmark reports are the source of truth for current metrics. Reports should be regenerated after any bank or testcase changes.
