# `ashrae-energy-prediction` Benchmark Notes

This task root defines the canonical action-bank benchmark task for `ashrae-energy-prediction`.

## Task Contract

- Task artifacts live under `data/tasks/ashrae-energy-prediction/`.
- The benchmark is `official-only`.
- The fixed official scope is:
  - `train.csv`
  - `test.csv`
  - `building_metadata.csv`
  - `weather_train.csv`
  - `weather_test.csv`
  - `sample_submission.csv`
- The task-level candidate bank lives in `candidate_actions.json`.
- Every testcase will use the same full bank.
- Testcases store only `input.context_action_ids`.
- Hidden scoring metadata stays in the bank, not in testcase files.

## Scope Boundary

Excluded from the benchmark contract:

- leak-oriented corrections
- site-0 leak tables
- holiday calendars
- public-kernel side inputs such as feather/pickle/minified mirrors
- memory-only implementation tricks such as aggressive dtype downcasting

These may appear in notebooks, but they are outside the benchmark's rewarded `official-only` spine.

## Primary Spine

The conservative primary `core_preprocessing` spine is:

1. join `building_metadata.csv` onto train/test by `building_id`
2. join split-matched weather tables by `site_id, timestamp`
3. parse `timestamp`
4. derive stable date parts from `timestamp`
5. encode `primary_use`
6. handle missing building/weather values with scalar imputation

The primary denominator intentionally excludes:

- leak-style row filtering
- heavy lag/rolling pipelines
- grouped weather interpolation branches
- holiday features
- target transformations
- memory optimization steps

## Task-Local Workflow Assumptions

- The weather join is represented as one conceptual `JOIN_LOOKUP` row with `right_table_id = weather_by_split`.
  - On train rows this means `weather_train.csv`.
  - On test rows this means `weather_test.csv`.
- `LOG_TRANSFORM` on `meter_reading` is kept as a `model_specific_preprocessing` row even though it touches the training target.
  - This mirrors common Kaggle training pipelines and is intentionally kept out of the primary denominator.
- The raw local workspace currently stores official CSVs directly in the task root.
  - The benchmark contract still refers to official Kaggle filenames only.

## Bank Snapshot

- Draft bank size: `35`
- Good actions: `11`
- Bad actions: `24`
- Primary effective good units: `6`
- Canonical family coverage: `14`

Covered families:

- `JOIN_LOOKUP`
- `PARSE_DATETIME`
- `DATE_PART_FEATURE`
- `ENCODE_CATEGORICAL`
- `IMPUTE_MISSING`
- `DROP_COLUMNS`
- `LOG_TRANSFORM`
- `FILTER_ROWS`
- `SCALE_NUMERIC`
- `GROUP_AGG`
- `LAG_FEATURE`
- `ROLLING_WINDOW_FEATURE`
- `CYCLICAL_ENCODE`
- `CREATE_MISSING_INDICATOR`

The bank is intentionally broader than the primary spine. Several represented families are included as distractor or near-miss branches so the benchmark tests diagnosis quality rather than rote recovery of one baseline.

## Hidden-Order Assumptions

- Building metadata join should happen before:
  - weather join
  - `primary_use` encoding
  - `square_feet` log transforms
- Timestamp parsing should happen before:
  - date-part extraction
  - dropping the raw `timestamp` column
- Missing-value handling should happen after the relevant official joins.
- Some destructive drop candidates explicitly invalidate downstream good actions.

## Metric And Raw-Field Notes

- `task.json` keeps the official competition metric as `RMSLE`.
- `task_characteristics.preprocessing_complexity_raw = 11` is the count of rewarded good rows across all eval stages in this authored bank.
  - It is intentionally not forced to equal the evaluator's `primary_effective_good_unit_count`.
