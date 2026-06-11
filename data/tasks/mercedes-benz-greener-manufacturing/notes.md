# `mercedes-benz-greener-manufacturing` Benchmark Notes

This task root defines the canonical action-bank benchmark task for `mercedes-benz-greener-manufacturing`.

## Task Contract

- Task artifacts live under `data/tasks/mercedes-benz-greener-manufacturing/`.
- The benchmark is `official-only`.
- The fixed official scope is:
  - `train.csv`
  - `test.csv`
  - `sample_submission.csv`
- The task-level candidate bank lives in `candidate_actions.json`.
- Every testcase will use the same full bank.
- Testcases store only `input.context_action_ids`.
- Hidden scoring metadata stays in the bank, not in testcase files.

## Scope Boundary

Excluded from the benchmark contract:

- public-kernel side inputs
- leak-style metadata inferred from leaderboard probing
- external Mercedes manufacturing metadata
- manually curated duplicate-column maps that are not directly recoverable from the official files

These patterns may appear in notebooks, but they are outside the rewarded benchmark spine.

## Primary Spine

The conservative primary `core_preprocessing` spine is:

1. drop `ID`
2. choose one categorical encoding strategy for `X0`, `X1`, `X2`, `X3`, `X4`, `X5`, `X6`, `X8`
3. remove the deterministic constant columns from the official train table

The primary denominator intentionally excludes:

- model-specific feature selection
- low-rank projection branches such as PCA / ICA / SVD
- numeric scaling branches
- target-based outlier removal
- duplicate-row pruning

## Model-Specific Good Rows

The bank also keeps non-primary good rows in `model_specific_preprocessing`:

- one feature-selection branch via tree importance or RFECV
- one low-rank projection branch via PCA / ICA / SVD
- one numeric scaling branch via robust or min-max scaling

These remain rewarded in `all` scoring but do not enlarge the primary headline denominator.

## Task-Local Workflow Assumptions

### `X0-X8` notebook shorthand vs official columns

Many notebooks describe the categorical block as `X0-X8`.
The released official files do not contain `X7`.
The benchmark therefore binds categorical actions to the actual official object columns only:

- `X0`
- `X1`
- `X2`
- `X3`
- `X4`
- `X5`
- `X6`
- `X8`

### Downstream branch matrix assumption

Projection, feature-selection, and scaling rows are authored against the compact repaired feature matrix:

- `ID` already removed
- constant columns already removed
- one categorical encoding branch already chosen

The current hidden-order metadata can express hard prerequisites, but it does not express clean OR-dependencies between alternative encoding strategies.
So this benchmark records that matrix assumption here rather than forcing brittle pairwise conflicts into the bank.

## Bank Snapshot

- Draft bank size: `30`
- Good actions: `11`
- Bad actions: `19`
- Primary good rows: `4`
- Primary effective good units: `3`
- Canonical family coverage: `8`

Covered families:

- `DROP_COLUMNS`
- `DROP_CONSTANT_COLUMNS`
- `ENCODE_CATEGORICAL`
- `FEATURE_SELECTION`
- `PCA_REDUCTION`
- `SCALE_NUMERIC`
- `FILTER_ROWS`
- `DROP_DUPLICATES`

The bank is intentionally broader than the primary spine. It includes hard negatives around identifier misuse, destructive sparse-block pruning, aggressive row filtering, and lossy projection settings so the benchmark tests diagnosis rather than rote recovery of one baseline.

## Hidden-Order Assumptions

- constant-column pruning should happen before model-specific projection, scaling, or selection branches
- dropping the categorical block invalidates the rewarded encoding rows
- dropping the sparse binary block invalidates the rewarded downstream wide-matrix branches
- categorical encoding alternatives are label-neutral and share one equivalence group so the primary denominator does not reward both at once

## Metric And Raw-Field Notes

- `task.json` keeps the official competition metric as `R2`.
- Kaggle competition text describes this as the coefficient of determination (`R^2`).
- `task_characteristics.preprocessing_complexity_raw = 11` is authored as retained good-row count before equivalence collapse, not as the primary effective-good denominator.

## Notebook Evidence Summary

Phase 1 rerun produced a valid notebook corpus through the repo collector:

- `725` score-ranked unique refs scanned
- `104` refs survived the score plus vote cutoff gate
- `59` eligible notebooks matched the current FE-signal rules
- the collector selected `30` notebook artifacts for authoring

Observed notebook themes in that selected corpus:

- very strong preference for label encoding over the released object columns
- recurring alternative one-hot branch for the same low-cardinality block
- recurring 12-component PCA / ICA / SVD stack features
- smaller but real feature-selection and scaling branches
- repeated discussion of target outliers and duplicate / redundant feature handling
