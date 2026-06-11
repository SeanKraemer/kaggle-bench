# Task Report: Store Sales Time Series Forecasting

## Status

- Migrated to the action-bank benchmark contract.
- Shared evaluator, validator, and schemas come from `origin/main`'s canonical benchmark implementation.
- Raw benchmark outputs are complete for `human`, `rule_based`, `single_llm`, `generic_agent`, `proposed_agent`, and `claude_code`.
- Aggregate benchmark markdown was regenerated on the `results/store-sales-time-series-forecasting/reports` branch after the full single-task evaluation run completed.

## Candidate Bank

- Total candidates: `56`
- Good candidates: `16`
- Bad candidates: `40`
- Primary effective good units: `13`

## Benchmark Files

- Task bundle: `data/tasks/store-sales-time-series-forecasting`
- Primary aggregate report: `eval/results/benchmarks/store-sales-time-series-forecasting-primary.md`
- All-scope aggregate report: `eval/results/benchmarks/store-sales-time-series-forecasting-all.md`

## Benchmark Coverage

- Single-run artifacts: `85`
- Grouped agent/testcase units: `21`
- Agent/run coverage: `human` x1, `rule_based` x4, `single_llm` x20, `generic_agent` x20, `proposed_agent` x20, `claude_code` x20

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task store-sales-time-series-forecasting --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/store-sales-time-series-forecasting-primary.md
uv run python eval/aggregate.py --task store-sales-time-series-forecasting --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/store-sales-time-series-forecasting-all.md
```

## Notes

This report is a lightweight branch-local summary. The aggregate benchmark reports are the source of truth for current metrics and should be regenerated after any benchmark artifact changes.
