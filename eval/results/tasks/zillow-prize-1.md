# Task Report: Zillow Prize 1

## Status

- Migrated to the action-bank benchmark contract on current `main`.
- Shared evaluator, validator, and schemas come from the canonical benchmark implementation on `main`.
- Raw benchmark outputs are complete for `human`, `rule_based`, `single_llm`, `generic_agent`, `proposed_agent`, and `claude_code`.
- Aggregate benchmark markdown is checked in for both `primary` and `all` scoring scopes.

## Candidate Bank

- Total candidates: `115`
- Good candidates: `15`
- Bad candidates: `100`
- Primary effective good units: `9`

## Benchmark Files

- Task bundle: `data/tasks/zillow-prize-1`
- Primary aggregate report: `eval/results/benchmarks/zillow-prize-1-primary.md`
- All-scope aggregate report: `eval/results/benchmarks/zillow-prize-1-all.md`

## Benchmark Coverage

- Single-run artifacts: `85`
- Grouped agent/testcase units: `21`
- Agent/run coverage: `human` x1, `rule_based` x4, `single_llm` x20, `generic_agent` x20, `proposed_agent` x20, `claude_code` x20

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task zillow-prize-1 --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/zillow-prize-1-primary.md
uv run python eval/aggregate.py --task zillow-prize-1 --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/zillow-prize-1-all.md
```

## Notes

This report is a lightweight branch-local summary. The aggregate benchmark reports are the source of truth for current metrics and should be regenerated after any benchmark artifact changes.
