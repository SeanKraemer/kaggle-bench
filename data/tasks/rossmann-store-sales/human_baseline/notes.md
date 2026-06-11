# Rossmann Store Sales Human Baseline Notes

This directory contains Sean's `tc1_from_scratch` human baseline for `rossmann-store-sales`.
It records a manual pass over the Rossmann data, a plain-English shortlist, and the final bank-id alignment used for evaluation.

Use the artifacts in this directory as follows:

- `work.ipynb`: evidence-only inspection notebook with dataset checks and plain-language reasoning; it does not contain bank ids or a final answer list
- `manual_selection_worksheet.md`: authoritative mapping document for the manual baseline; this is where the plain-English shortlist is translated into `CA-*` ids
- `tc1_human.json`: the canonical benchmark output for the TC1 human baseline
- `provenance/action_trace.json`: action-by-action mapping from the selected ids back to notebook sections or worksheet sections
- `provenance/metadata.json`: authorship, timing, and provenance notes for the manual pass

Selection philosophy:

- keep the store join and basic calendar scaffold
- choose one simple closed-store rule and one simple categorical encoding path
- keep only the clearest competition-distance repair
- keep the train-only leakage drop
- stop before competition-timing derivations, promo-heavy feature work, and optional all-scope cleanup

For `tc1_from_scratch`, `predicted_remove_action_ids` remain empty because the testcase starts with no prior context.

Validation commands:

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task rossmann-store-sales --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/rossmann-store-sales-primary.md
uv run python eval/aggregate.py --task rossmann-store-sales --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/rossmann-store-sales-all.md
```
