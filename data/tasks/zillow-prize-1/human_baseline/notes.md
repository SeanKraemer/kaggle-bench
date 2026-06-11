# Human Baseline Notes

- This directory holds the canonical human baseline artifacts for Zillow.
- Initial scope is only `tc1_human`.
- The human baseline should use the output schema in `data/schema/output.schema.json`.
- Supporting notebook or notes artifacts should be referenced through `artifact_refs`.
- `tc1_human.json` is a bank-id re-authoring of the legacy notebook baseline rather than a strict canonical-action migration.
- The new artifact only includes bank actions with clear notebook support and a defensible mapping into the current candidate bank.
- Some legacy notebook steps remain intentionally unmapped when the current bank does not provide a clean non-overlapping candidate.
