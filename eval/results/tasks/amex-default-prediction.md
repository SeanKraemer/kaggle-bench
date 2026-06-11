# Task Report: AMEX Default Prediction

## Status

- Migrated to the action-bank benchmark contract.
- Shared evaluator, validator, and schemas come from `origin/main`'s canonical benchmark implementation.
- The human baseline was manually rebuilt to be narrower and more defensible; `human_baseline/work.ipynb` is evidence-only and `human_baseline/manual_selection_worksheet.md` is the authoritative bank mapping.
- Raw benchmark outputs are complete for `human`, `rule_based`, `single_llm`, `generic_agent`, `proposed_agent`, and `claude_code`.
- Aggregate benchmark markdown was regenerated on the `sean/results-consolidated-all5` branch after the full AMEX campaign completed.

## Candidate Bank

- Total candidates: `70`
- Good candidates: `20`
- Bad candidates: `50`
- Primary effective good units: `14`

## Benchmark Files

- Task bundle: `data/tasks/amex-default-prediction`
- Primary aggregate report: `eval/results/benchmarks/amex-default-prediction-primary.md`
- All-scope aggregate report: `eval/results/benchmarks/amex-default-prediction-all.md`

## Benchmark Coverage

- Single-run artifacts: `85`
- Grouped agent/testcase units: `21`
- Agent/run coverage: `human` x1, `rule_based` x4, `single_llm` x20, `generic_agent` x20, `proposed_agent` x20, `claude_code` x20

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task amex-default-prediction --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/amex-default-prediction-primary.md
uv run python eval/aggregate.py --task amex-default-prediction --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/amex-default-prediction-all.md
```

## Notes

This report is a lightweight branch-local summary. The aggregate benchmark reports are the source of truth for current metrics and should be regenerated after any benchmark artifact changes.
