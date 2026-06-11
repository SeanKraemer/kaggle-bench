# icr-identify-age-related-conditions Benchmark Notes

This task root defines the canonical action-bank benchmark task for `icr-identify-age-related-conditions`.

## Benchmark Shape

- Task artifacts live under `data/tasks/icr-identify-age-related-conditions/`.
- Machine-checked schemas live under `data/schema/`.
- The bank is competition-level and shared by every testcase.

## Task Contract

- Scope is `official-only`.
- Allowed files are:
  - `train.csv`
  - `test.csv`
  - `greeks.csv`
  - `sample_submission.csv`
- No external data, synthetic lookup tables, or off-platform enrichments belong in this benchmark contract.
- Every testcase stores only:
  - `task_ref`
  - `input.scenario`
  - `input.context_action_ids`
- Hidden scoring metadata stays in `candidate_actions.json`, not in testcase files.

## Scoring Scope

- `primary` scores only `eval_stage = core_preprocessing`.
- `all` scores every active stage.

Current authored intent:

- Primary good denominator should stay conservative.
- Validation-side `greeks` / `Epsilon` usage and model-family-specific scaling / log branches are real bank rows, but they should not enlarge the primary denominator.

## Primary Good Spine

The deterministic official-only primary spine is intentionally small:

- drop `Id` before modeling
- convert `EJ` from `A/B` into a numeric binary code
- handle sparse numeric missingness with a scalar imputation strategy

Important curation choice:

- both median-fill and mean-fill are notebook-backed and remain in the bank as `good`
- they share one `equivalence_group`, so they do not count as independent primary add units

Current primary effective good units after equivalence collapse:

- `3`

## Workflow Assumptions Kept Out Of The Bank

### Trailing-space header normalization

Many notebooks normalize the four official headers with trailing spaces:

- `BD `
- `CD `
- `CW `
- `FD `

The current canonical ontology does not have a first-class rename-columns action.
So this benchmark treats header trimming as a task-local workflow assumption recorded here rather than as a standalone candidate row.

### KNN imputation

Selected notebooks frequently use `KNNImputer`.
The current `IMPUTE_MISSING` schema does not support a `knn` strategy.
Because of that mismatch, the bank keeps scalar imputation branches that are expressible in the current ontology and records the KNN pattern only as supporting authoring context.

### Label-aware over/under-sampling

The notebook corpus contains target-aware oversampling / undersampling branches.
The current `SAMPLE_ROWS` action can express generic row sampling, but not the richer label-aware resampling semantics without benchmark ambiguity.
For this reason:

- the bank does not reward resampling as `good`
- the bank only includes clearly harmful random downsampling variants as `bad`

## Validation / Greeks Branch

The official `greeks.csv` file is in-scope.
It is treated as a validation-side branch rather than a primary submission-side requirement.

Allowed bank semantics for this branch:

- join `greeks` onto training rows by `Id`
- parse `Epsilon` with coercion because `Unknown` values occur

This branch is useful for fold design and train-side diagnostics, but it should not be treated as part of the deterministic primary good spine.

## Bank Coverage

The current Phase 2 bank is authored to cover a broad slice of task-applicable canonical families while staying deterministic:

- `DROP_COLUMNS`
- `MAP_CATEGORIES`
- `IMPUTE_MISSING`
- `SCALE_NUMERIC`
- `JOIN_LOOKUP`
- `PARSE_DATETIME`
- `LOG_TRANSFORM`
- `DROP_HIGH_NULL_COLUMNS`
- `DROP_ROWS_WITH_MISSING`
- `FILTER_ROWS`
- `SAMPLE_ROWS`
- `CLIP_OUTLIERS`
- `FEATURE_SELECTION`

Coverage policy:

- good rows stay conservative and notebook-backed
- bad rows intentionally over-index on destructive pruning, low-quality missing-data handling, and harmful small-data row loss
- families like KNN imputation and label-aware resampling are discussed here but not rewarded as standalone `good` rows because the current ontology cannot represent them faithfully enough

## Hidden-Order Assumptions

- `PARSE_DATETIME(Epsilon)` must follow the `greeks` join row.
- Scaling and log-transform rows are intentionally non-primary and are not used to create extra hidden-order constraints.
- The benchmark assumes there exists at least one valid execution order for the selected good set without needing additional evaluator rules.

## Raw Metric Choice For `preprocessing_complexity_raw`

This task is authored from scratch.
`task.json.task_characteristics.preprocessing_complexity_raw = 9` is defined as:

- retained `good` candidate rows before equivalence-group collapse
- excluding notes-only workflow assumptions
- excluding notebook patterns that are not representable in the current canonical schema

That choice is intentionally distinct from:

- primary effective good units, and
- total bank size

## Current Bank Snapshot

- Current draft bank size: `33`
- Good actions: `9`
- Bad actions: `24`
- Primary effective good units after equivalence-group collapse: `3`
- Bad-to-primary ratio: `24 / 3 = 8.0`
