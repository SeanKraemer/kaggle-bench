# recruit-restaurant-visitor-forecasting Notes

## 2026-03-31

### Close reading status
- Close reading completed for all 30 collected notebooks.
- Evidence source files:
  - `data/collector/data/golden/recruit-restaurant-visitor-forecasting/manual_close_reading_snippets.md`
  - `data/collector/data/golden/recruit-restaurant-visitor-forecasting/action_candidates.jsonl`

### Bank snapshot
- `candidate_actions.json` rows: 90
- `good`: 19
- `bad`: 71
- `core_preprocessing good`: 12
- `bad >= 3 * primary_effective_good_unit_count`: satisfied
- canonical family coverage: `40 / 40`
- minimum rows per canonical family: `2`

### Core good scope
- Recruit primary good is intentionally the shared tabular reservation/date/store spine:
  - parse reservation datetimes
  - reservation lead-time (`reserve_datetime_diff`)
  - reservation `sum` / `mean` by `(air_store_id, visit_date)`
  - parse `visit_date`
  - `visit_date -> dow/year/month`
  - visitors grouped by `(air_store_id, dow)`
  - join back reservation aggregates
  - join holiday calendar
  - join store metadata
  - label encode store genre/area
  - `log1p(visitors)`
- Weighted-mean holiday lookup, aggressive neural branches, and custom one-hot/scaling/fill policies are kept in `model_specific_preprocessing`.
- Weak single-notebook or two-notebook observed branches were pruned from `good` and left only in close-reading notes.
  - examples: custom one-hot weekday encoding, single-branch scaling, single-branch weekend/off-day flags, narrow recency filters

### Coverage decisions
- No canonical family was excluded.
- Some families are not benchmark-preferred for Recruit, but are still mechanically task-applicable and therefore represented as synthetic bank rows:
  - `TARGET_ENCODE_OOF`
  - `TEXT_VECTORIZATION`
  - `PCA_REDUCTION`
  - `POLYNOMIAL_FEATURE`
  - `ROLLING_WINDOW_FEATURE`
  - `LAG_FEATURE`
  - `EXPANDING_WINDOW_FEATURE`
- High-salience families were given thicker local decision boundaries than the minimum:
  - `JOIN_LOOKUP`
  - `GROUP_AGG`
  - `IMPUTE_MISSING`
  - `APPLY_EXPRESSION`
  - `DATE_PART_FEATURE`
  - `DROP_COLUMNS`

### Important bank semantics
- `TIME_SINCE_REFERENCE` is used for `reserve_datetime_diff`.
  - This is a better canonical fit than treating reservation lead-time as a generic free-form expression.
- `FILTER_ROWS` is represented only as non-primary alternatives and negatives.
  - harmful global row filters and near-miss reservation/recency filters are kept in the bank
  - narrow notebook-local filter choices are not treated as shared add-side targets
- `SCALE_NUMERIC` is kept as synthetic bad-only coverage.
  - observed scaling evidence was too thin to justify keeping weak good rows after pruning
  - two neural-style scaling negatives remain so the canonical family is still review-complete
- `IMPUTE_MISSING` keeps only one model-specific good fill policy.
  - the repeated `-1` wide-table fill remains as the representative good row
  - the observed zero-fill neural branch was left in close-reading evidence but removed from the bank to avoid all-scope double-counting of branch-specific fill alternatives
  - `CA-000086` now declares explicit prerequisites for the modeled reservation/date/store synthesis branch

### Task metadata choices
- `task.json` uses the current primary-effective core good count (`12`) as `preprocessing_complexity_raw`.
  - This aligns the raw complexity value to the core-preprocessing denominator-like quantity used in the primary benchmark slice.
- `dataset_size_raw` is the largest relevant table row count (`hpg_reserve.csv`: `2,000,320` rows).
- `feature_dimensionality_raw` is the benchmark-relevant case-insensitive raw column union count (`17`).
- `overview` metadata is mostly filled from historical public references plus local dataset inspection.
  - `enabled_date` is normalized to the earliest observed public notebook run timestamp in the local Kaggle metadata cache because the exact official launch timestamp was not preserved.
  - `new_entrant_deadline` and `deadline` are normalized to ISO-style timestamp strings.

### Residual review targets
- The weighted-mean family and the reservation-heavy tabular family are both represented, but they should not both be treated as primary add-side denominators.
- Some synthetic families are intentionally distractor-style rather than historically observed. That is deliberate and follows the new action-bank benchmark contract.

### Testcase semantics
- `tc1_from_scratch`
  - empty context; recover the full Recruit add-side target set from the bank
- `tc2_partial_good`
  - early parsing and date-part core actions are already present
  - remaining work is mainly reservation aggregation, joins, encoding, and target scaling
- `tc3_fault_injected`
  - pure harmful history with destructive date dropping, wrong-grain joins, and a harmful holiday-only filter
  - primary scope still has clear remove targets because the context includes core bad actions
- `tc4_mixed_history`
  - early reservation/date core preparation is present, but the history also contains a wrong holiday join and a wrong-grain reservation join
  - this keeps mixed-state remove targets non-empty and meaningfully harmful in both `primary` and `all` scopes without smuggling in ambiguous overlapping good alternatives
