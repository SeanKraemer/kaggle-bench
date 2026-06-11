# `restaurant-revenue-prediction` Benchmark Notes

This task root defines the canonical action-bank benchmark task for `restaurant-revenue-prediction`.

## Task-Local Contract

- Task artifacts live under `data/tasks/restaurant-revenue-prediction/`.
- The benchmark is single-table and `official-only`.
- The full action bank lives in `candidate_actions.json`.
- Every testcase will reuse the same bank and will store only:
  - `task_ref`
  - `input.scenario`
  - `input.context_action_ids`

## Scope

- Primary scoring stays on `eval_stage = core_preprocessing`.
- `all` scoring includes additional `model_specific_preprocessing` rows.
- The benchmark uses only the official Kaggle competition tables:
  - `data/train.csv`
  - `data/test.csv`
  - official sample file `sampleSubmission.csv`

Current local mirror note:

- The official competition files are part of the benchmark scope, but they are not mirrored into this task directory in the repository snapshot.
- `data/train.csv`, `data/test.csv`, and `sampleSubmission.csv` should be obtained from the official Kaggle competition source when needed.
- That omission is non-blocking for the benchmark because the bank, testcases, and human baseline depend only on the train/test feature layout.

## Primary Spine

The conservative primary good spine is:

1. Drop `Id`.
2. Parse `Open Date`.
3. Recover one stable date-signal strategy from `Open Date`:
   - derive `OpenDays` from a fixed benchmark reference date, or
   - extract explicit year / month / day parts.
4. Encode low-cardinality categoricals:
   - `City Group`
   - `Type`
5. Drop raw `Open Date` after date-signal derivation.

This keeps the add-side denominator narrow and avoids rewarding more volatile branches such as:

- aggressive `City` handling variants
- outlier filtering
- clipping
- numeric binning
- target-side row filtering
- external city priors

## Model-Specific Good Rows

The bank also keeps a few non-primary good rows in `model_specific_preprocessing`:

- binary `City == Istanbul` indicator
- standard scaling over numeric predictor columns
- `log1p` transform of `revenue`

These remain rewarded in `all` scoring but do not enlarge the primary denominator.

## Workflow Assumptions

Some repeated notebook behaviors are represented as task-local assumptions rather than new evaluator rules:

- `OpenDays` uses a fixed anchor date such as `2015-01-01`.
  - This is encoded as a normal `APPLY_EXPRESSION` row.
  - The fixed-date choice is a task-local workflow assumption, not a new evaluator primitive.
- `City` often contains Unicode spellings such as `Istanbul` / `İstanbul`.
  - The bank keeps one explicit binary-city branch but does not require a standalone normalization row.

## Inapplicable / Excluded Families

The task does not reward or even represent families that are not materially applicable to the official inputs:

- joins or relational lookup actions
- lag / rolling / diff time-series families
- missing-value imputation or missingness indicators
  - the official train/test tables are complete in the local mirror used for authoring
- text featurization
- external geocoding, holiday calendars, or city-level side data

## Hidden-Order Assumptions

The bank relies on standard hidden scoring metadata:

- `equivalence_group`
- `must_follow_action_ids`
- `invalidates_action_ids`
- `conflicts_with_action_ids`

Task-local ordering assumptions:

- `Open Date` parsing must happen before any date-derived branch.
- raw `Open Date` cleanup is represented with two separate good rows so each cleanup action can depend on the specific upstream date-signal strategy it follows.
- low-cardinality categorical encoding uses label and one-hot rows as label-neutral alternatives inside one equivalence group.

## Bank Snapshot

- Draft bank size: `26`
- Good actions: `11`
- Bad actions: `15`
- Primary effective good units after equivalence collapse: `5`
- Represented canonical families: `10`

## Metric / Raw Complexity Notes

- Competition metric: `RMSE`
- `task_characteristics.preprocessing_complexity_raw = 11`
  - Chosen metric: total rewarded good rows across all stages in the authored bank
  - This is intentionally not forced to equal the evaluator's primary effective good-unit count
