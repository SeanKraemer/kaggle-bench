# Optiver Trading At The Close Human Baseline Notes

This directory contains Sean's `tc1_from_scratch` human baseline for the Optiver action-bank benchmark.
It records a manual pass over the Optiver data, a plain-English shortlist, and the final bank-id alignment used for evaluation.

Use the artifacts in this directory as follows:

- `work.ipynb`: evidence-only inspection notebook with dataset checks and plain-language reasoning; it does not contain bank ids or a final answer list
- `manual_selection_worksheet.md`: authoritative mapping document for the manual baseline; this is where the plain-English shortlist is translated into `CA-*` ids
- `tc1_human.json`: the canonical benchmark output for the TC1 human baseline
- `provenance/action_trace.json`: action-by-action mapping from the selected ids back to notebook sections or worksheet sections
- `provenance/metadata.json`: authorship, timing, and provenance notes for the manual pass

Selection philosophy:

- keep the simple Optiver far/near default fills
- keep the first-order microstructure block, one lag family, one stock-prior strategy, and compact clock features
- stop before memory downcasting, grouped-median repair, higher-order interactions, and the broader rolling-window branch

Validation commands:

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task optiver-trading-at-the-close --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/optiver-trading-at-the-close-primary.md
uv run python eval/aggregate.py --task optiver-trading-at-the-close --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/optiver-trading-at-the-close-all.md
```
