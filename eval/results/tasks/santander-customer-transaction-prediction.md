# Task Report: Santander Customer Transaction Prediction

## Status

- Migrated to the action-bank benchmark contract on current `main`.
- Shared evaluator, validator, and schemas come from the canonical benchmark implementation on `main`.
- The human baseline was intentionally rebuilt as a narrow, evidence-backed baseline rather than a fresh local Kaggle rerun.
- Raw benchmark outputs are complete for `human`, `rule_based`, `single_llm`, `generic_agent`, `proposed_agent`, and `claude_code`.
- Aggregate benchmark markdown was regenerated on the `sean/results-consolidated-santander` branch after the full Santander campaign completed.

## Candidate Bank

- Total candidates: `14`
- Good candidates: `3`
- Bad candidates: `11`
- Primary effective good units: `3`

## Benchmark Files

- Task bundle: `data/tasks/santander-customer-transaction-prediction`
- Primary aggregate report: `eval/results/benchmarks/santander-customer-transaction-prediction-primary.md`
- All-scope aggregate report: `eval/results/benchmarks/santander-customer-transaction-prediction-all.md`

## Benchmark Coverage

- Single-run artifacts: `85`
- Grouped agent/testcase units: `21`
- Agent/run coverage: `human` x1, `rule_based` x4, `single_llm` x20, `generic_agent` x20, `proposed_agent` x20, `claude_code` x20

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task santander-customer-transaction-prediction --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/santander-customer-transaction-prediction-primary.md
uv run python eval/aggregate.py --task santander-customer-transaction-prediction --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/santander-customer-transaction-prediction-all.md
```

## Notes

This report is a lightweight branch-local summary. The aggregate benchmark reports are the source of truth for current metrics and should be regenerated after any benchmark artifact changes.
