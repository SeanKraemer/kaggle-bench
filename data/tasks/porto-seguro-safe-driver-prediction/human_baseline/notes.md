# Porto Seguro Safe Driver Prediction Human Baseline Notes

This directory contains Sean's `tc1_from_scratch` human baseline for the Porto action-bank benchmark.
It records a manual pass over the Porto data, a plain-English shortlist, and the final bank-id alignment used for evaluation.

Use the artifacts in this directory as follows:

- `work.ipynb`: evidence-only inspection notebook with dataset checks and plain-language reasoning; it does not contain bank ids or a final answer list
- `manual_selection_worksheet.md`: authoritative mapping document for the manual baseline; this is where the plain-English shortlist is translated into `CA-*` ids
- `tc1_human.json`: the canonical benchmark output for the TC1 human baseline
- `provenance/action_trace.json`: action-by-action mapping from the selected ids back to notebook sections or worksheet sections
- `provenance/metadata.json`: authorship, timing, and provenance notes for the manual pass

Selection philosophy:

- keep the sentinel cleanup, sparse-column drops, calc-family pruning, and id drop
- stop before typed imputation, missing indicators, model-specific encoding strategy, scaling, and other higher-variance branches

Validation commands:

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task porto-seguro-safe-driver-prediction --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/porto-seguro-safe-driver-prediction-primary.md
uv run python eval/aggregate.py --task porto-seguro-safe-driver-prediction --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/porto-seguro-safe-driver-prediction-all.md
```
