# Human Baseline Notes

- This directory holds the canonical human baseline artifacts for `icr-identify-age-related-conditions`.
- Initial scope is only `tc1_human`.
- The human baseline uses the output schema in `data/schema/output.schema.json`.
- `tc1_human.json` is a `true bank-id authoring`, not a legacy migration and not a mock output.
- The notebook contains real working code for loading official files, inspecting missingness, encoding `EJ`, scalar imputation, the optional `greeks` / `Epsilon` branch, and one scaling-plus-log model-family branch.
- Trailing-whitespace header cleanup for `BD ` / `CD ` / `CW ` / `FD ` is shown in the notebook as a workflow assumption, but it is intentionally not mapped to a bank row because the current ontology has no rename-columns action.
- Frequent notebook patterns that were intentionally left out of the baseline selection:
  - `KNNImputer`, because the current canonical schema does not express it directly
  - label-aware over/under-sampling, because the current benchmark contract treats those branches as too ambiguous for add-side reward
