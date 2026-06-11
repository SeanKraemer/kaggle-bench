# Human Baseline Notes

- This directory holds the canonical human baseline artifacts for Predict Future Sales.
- Initial scope is only `tc1_human`.
- The human baseline uses the output schema in `data/schema/output.schema.json`.
- Supporting notebook and provenance artifacts are referenced through `artifact_refs`.
- `tc1_human.json` is a bank-id re-authoring from the collected Kaggle notebook corpus rather than a one-to-one migration from any single legacy output file.
- `work.ipynb` is intended to be a real working notebook, not just a prose summary, and its section headings are aligned with `provenance/action_trace.json`.
- The baseline selects all current `good` bank rows because each one has direct notebook support and fits the official-only benchmark contract.
- Common notebook behaviors that are intentionally omitted from the bank remain omitted here as well, especially full shop-item-month grid completion, richer grouped-history lag families, and price-trend branches.
