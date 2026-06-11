# Human Baseline Notes

- This directory holds the canonical human baseline artifacts for `restaurant-revenue-prediction`.
- Initial scope is only `tc1_human`.
- The human baseline follows the output contract in `data/schema/output.schema.json`.
- This baseline is `true bank-id authoring`, not a legacy migration or a re-authored carry-over from an older evaluator format.
- The notebook stays `official-only` and uses only the repo-local competition files under `../data/`.
- The selected actions intentionally choose one conservative date branch (`OpenDays`) and one compact low-cardinality encoding branch (`label` for `City Group` and `Type`) instead of trying to combine mutually alternative rows from the bank.
- The notebook does not attempt to mirror every plausible notebook branch in the corpus; it only implements the specific bank rows selected in `tc1_human.json`.
