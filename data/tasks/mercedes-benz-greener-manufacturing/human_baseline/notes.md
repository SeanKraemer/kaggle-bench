# Human Baseline Notes

- This directory holds the canonical human baseline artifacts for `mercedes-benz-greener-manufacturing`.
- Initial scope is only `tc1_human`.
- The human baseline follows the output contract in `data/schema/output.schema.json`.
- This baseline is `true bank-id authoring`, not a legacy migration or a re-authored carry-over from an older evaluator format.
- The notebook stays `official-only` and uses only the repo-local competition files under `../data/`.
- The selected actions intentionally choose one conservative categorical branch (`label` encoding) instead of mixing it with the bank's one-hot alternative.
- The notebook also implements one scaling branch, one PCA branch, and one RFECV-style selection branch that are explicitly represented in the current candidate bank.
- The notebook does not attempt to mirror target-side outlier removal, destructive sparse-block pruning, or the alternative ICA / SVD projection rows.
