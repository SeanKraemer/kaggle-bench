# AMEX TC1 Human Baseline Worksheet

- Task: `amex-default-prediction`
- Testcase: `tc1_from_scratch`
- Context: empty, so you are only choosing `predicted_add_action_ids`
- Goal: record a believable first-pass AMEX baseline, then map that shortlist to the current bank ids at the end

## Plain-English Shortlist Before Bank Mapping

- Separate the raw table into known categorical columns, numeric statement columns, and obvious non-predictors.
- Round the wide numeric statement block to reduce noise and make the matrix easier to handle.
- Cast the 11 known categorical columns into integer-like form and use simple label-ready encoding.
- Treat missingness as signal: inspect null patterns, add binary missing flags, and use a simple fill fallback for numeric columns with decent coverage.
- Collapse the monthly statements to one row per customer with standard numeric and categorical aggregations.
- Flatten the grouped feature names back into a single modeling table.
- Stop there rather than force the recency-delta layer or final matrix cleanup into the baseline.

## Final Bank Mapping

Final selected ids, in worksheet order:

- `CA-000014`
- `CA-000009`
- `CA-000049`
- `CA-000020`
- `CA-000056`
- `CA-000001`
- `CA-000029`
- `CA-000043`

## Schema And Basic Typing

- `CA-000014` `APPLY_EXPRESSION`: keep the AMEX-specific rounding trick on raw numeric features.
- `CA-000009` `CAST_DTYPE`: cast the 11 categorical columns to compact integer-like codes.

## Categorical Handling

- `CA-000049` `ENCODE_CATEGORICAL`: keep simple label encoding for the known AMEX categorical columns.

Notes:

- I used the notebook to inspect rare-level concentration, but I did not treat category collapsing as a committed baseline step because the current AMEX bank does not expose a clean dedicated action for that idea.

## Customer-Level Aggregations

- `CA-000020` `GROUP_AGG`: categorical customer-level aggregation with `count`, `first`, `last`, and `nunique`.
- `CA-000056` `GROUP_AGG`: numeric customer-level aggregation with the standard AMEX summary stats.
- `CA-000001` `APPLY_EXPRESSION`: flatten the grouped customer summaries into a usable `feature_stat` schema.

Why these representatives:

- `CA-000020` is the selected representative for the categorical aggregation equivalence group instead of `CA-000010`.
- `CA-000056` is the selected representative for the numeric aggregation equivalence group instead of `CA-000045` or `CA-000054`.

## Missingness

- `CA-000029` `IMPUTE_MISSING`: keep the simple numeric imputation fallback for the better-covered continuous-style subset.
- `CA-000043` `CREATE_MISSING_INDICATOR`: keep explicit missingness flags.

## Intentionally Omitted Alternatives

- `CA-000010`: valid categorical aggregation alternative, but not selected because `CA-000020` already covers that need.
- `CA-000045`: valid numeric aggregation alternative, but not selected because `CA-000056` already covers that need.
- `CA-000054`: valid percentile-style numeric aggregation alternative, now treated as the same aggregation need rather than a separate baseline requirement.
- `CA-000030`: narrow high-null raw-column cleanup is plausible, but it felt more bank-specific than mandatory in a first manual pass.
- `CA-000004`: the last-versus-mean delta family is useful, but it reads like a second-pass embellishment once lag-1 deltas already exist.
- `CA-000022`: numeric downcasting is practical engineering hygiene, but I did not keep it as part of the core human baseline story.
- `CA-000055`: lag-1 deltas are useful, but they felt like the first clearly second-wave AMEX feature family once the aggregation scaffold was already in place.
- `CA-000023`: dropping `customer_ID` and `S_2` is clean final hygiene, but it is not necessary to justify the manual baseline.
- `CA-000016`: plausible robustness step, but not omission-critical enough for the conservative baseline.
- `CA-000015`, `CA-000017`, `CA-000060`: all-scope/model-specific families kept out of the final manual baseline.

## Provenance Reminder

- `provenance/action_trace.json` carries the action-by-action rationale.
- `provenance/metadata.json` records timing and provenance mode.
- `work.ipynb` and `work.py` are consulted scratch artifacts used before late bank-id mapping, not the final selection record.
