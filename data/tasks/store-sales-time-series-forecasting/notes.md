# store-sales-time-series-forecasting Benchmark Notes

This task root defines the canonical action-bank benchmark task for the Store Sales - Time Series Forecasting competition.

## Benchmark Shape

- Task artifacts live under `data/tasks/store-sales-time-series-forecasting/`.
- Machine-checked schemas live under `data/schema/`.
- Evaluator code and reports live under `eval/`.

## Task Contract

- This benchmark slice uses the official `train.csv`, `test.csv`, `stores.csv`, `oil.csv`, `holidays_events.csv`, and `transactions.csv` files.
- The task-level bank lives in `candidate_actions.json`.
- Every testcase uses the same full bank.
- Each testcase stores only `input.context_action_ids`.
- The evaluator derives:
  - `candidate_action_ids = full_bank_action_ids - context_action_ids`
  - expected add units from the active good portion of the derived candidate side
  - expected remove units from the active bad portion of the context side

## Scoring Metadata

The bank may include hidden scoring metadata that should stay out of agent-facing benchmark renderings:

- `equivalence_group`
- `must_follow_action_ids`
- `invalidates_action_ids`
- `conflicts_with_action_ids`

These fields are for evaluator logic only.

## Scope

- `primary` scores only `eval_stage = core_preprocessing`
- `all` scores every active stage

## Primary Good Spine

The 16 core preprocessing steps are:

1. **CA-000002** — PARSE_DATETIME on `date`
2. **CA-000004** — JOIN_LOOKUP stores (left, on store_nbr)
3. **CA-000007** — JOIN_LOOKUP oil (left, on date)
4. **CA-000011** — JOIN_LOOKUP holidays_events (left, on date)
5. **CA-000014** — JOIN_LOOKUP transactions (left, on [date, store_nbr])
6. **CA-000018** — APPLY_EXPRESSION linear interpolation of dcoilwtico
7. **CA-000021** — ROLLING_WINDOW_FEATURE 7-day mean of dcoilwtico
8. **CA-000024** — FILTER_ROWS transferred missing or False
9. **CA-000027** — FILTER_ROWS type != 'Work Day'
10. **CA-000031** / **CA-000034** — DATE_PART_FEATURE calendar decomposition (equivalence group: date_calendar_decomposition)
11. **CA-000038** / **CA-000041** — LAG_FEATURE sales grouped by (store_nbr, family) (equivalence group: sales_lag_feature)
12. **CA-000044** / **CA-000048** — ENCODE_CATEGORICAL family (equivalence group: family_encoding)
13. **CA-000052** — DROP_COLUMNS id

After equivalence-group collapse, primary effective good unit count = 13.

## Ordering Constraints

Key `must_follow_action_ids` chains:

- CA-000004/007/011/014 must follow CA-000002 (PARSE_DATETIME is prerequisite for date-keyed joins)
- CA-000018 must follow CA-000007 (oil join required before oil interpolation)
- CA-000021 must follow CA-000018 (interpolation required before rolling window)
- CA-000024/027 must follow CA-000011 when applied as post-join holiday cleanup. CA-000024 is null-safe so ordinary non-holiday rows with missing `transferred` values are preserved.

## Bank Snapshot

- Good actions: 16
- Bad actions: 40
- Primary effective good units: 13 after 3 equivalence-group units
- Bank satisfies `bad_count (40) >= 3 * primary_effective_good_unit_count (13) = 39`

## Authoring Reminders

- The oil series has systematic gaps on weekends and holidays; interpolation (CA-000018) is required after joining, not imputation or row deletion.
- The holidays_events join requires cleanup for transferred holidays and Work Day rows to avoid phantom holiday signals; after a left join, transferred-holiday cleanup must keep rows where `transferred` is missing or False.
- Lag features must be grouped by (store_nbr, family) to avoid cross-series leakage.
- The RMSLE metric means the target (sales) should NOT be log-transformed before training.
