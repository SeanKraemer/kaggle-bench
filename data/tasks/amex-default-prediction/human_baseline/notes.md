# AMEX Default Prediction Human Baseline Notes

This directory contains the TC1 human baseline bundle for the AMEX action-bank benchmark.

Key points:

- `tc1_human.json` contains the final selected `CA-*` ids for the AMEX human baseline.
- `manual_selection_worksheet.md` records the plain-English shortlist first, then the final bank-id mapping and the intentionally omitted alternatives.
- `provenance/action_trace.json` maps each selected action to concrete worksheet sections or scratch-notebook sections.
- `provenance/metadata.json` records authorship, timing, and the late-bank-mapping provenance mode for the final manual selection.
- `work.ipynb` and `work.py` are consulted scratch artifacts that capture the reasoning pass; they are supporting evidence for the final selection.

Selection philosophy:

- emphasize customer aggregation and restrained missingness cleanup
- keep one representative from each equivalence group instead of rewarding parallel alternatives as separate baseline needs
- leave recency-delta families, final cleanup, and other second-pass embellishments out of the final baseline
- leave model-specific or exploratory all-scope families out of the final baseline
- keep `predicted_remove_action_ids` empty because TC1 starts from an empty context

Validation commands:

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task amex-default-prediction --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/amex-default-prediction-primary.md
uv run python eval/aggregate.py --task amex-default-prediction --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/amex-default-prediction-all.md
```
