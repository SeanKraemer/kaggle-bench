# Human Baseline Notes

- This directory holds the Home Credit human baseline artifacts.
- Initial scope is only `tc1_human`.
- The human baseline uses the same output schema as ordinary run artifacts.
- Supporting notebook and provenance artifacts are referenced through `artifact_refs`.
- `tc1_human.json` now reflects an observed human bank-selection run after a full-bank review, not just the earlier notebook-faithful re-authoring pass.
- The selected add-side list should be read as one human run under the same action-bank constraints used for agents, not as an oracle answer key.
- [tc1_human_bank_review_workbench.md](../tc1_human_bank_review_workbench.md) records the category-level review surface that was used during the final selection pass.
