# lish-moa Benchmark Notes

This task root defines the action-bank benchmark task for the Kaggle LISH MoA competition.

## Benchmark Shape

- Task artifacts live under `data/tasks/lish-moa/`.
- Machine-checked schemas live under `data/schema/`.
- Evaluator code and reports live under `eval/`.
- `task.json` is shared competition metadata.
- `candidate_actions.json` is the current single action bank.
- `testcases/` contains four standard scenario contexts.
- `human_baseline/` contains the TC1 human baseline.
- `outputs/` is intentionally absent at this rebuild stage.

## Task Contract

- The benchmark uses the full LISH MoA feature set described in `task.json`.
- Every testcase will use the same full `candidate_actions.json` bank.
- Testcase files reference action IDs only through `input.context_action_ids`.
- The evaluator derives:
  - `candidate_action_ids = full_bank_action_ids - context_action_ids`
  - add targets from active `role = good` actions on the candidate side
  - remove targets from active `role = bad` actions on the context side
- `primary` scope scores only `eval_stage = core_preprocessing`.
- `all` scope scores every active stage.

## Task Metadata Review

`task.json` was reviewed during Stage 4 and left unchanged.

- `dataset_size_bucket` is `small`.
- `dataset_size_raw` is `23814`, the training row count.
- `feature_dimensionality_raw` is `876`, matching the input feature columns in `train_features.csv`.
- `preprocessing_complexity_raw` remains `11` as inherited task metadata. It is not required to equal the evaluator-derived `primary_effective_good_unit_count`.
- Benchmark-specific action-bank and testcase assumptions are kept in this file and `candidate_actions.json`, not in `task.json`.

## Current Bank Snapshot

- Current bank size: 52 actions
- Good actions: 11
- Bad actions: 41
- Primary good actions: 9
- Primary effective good units after equivalence-group collapse: 8
- Validator hard gate: `bad >= 3 * primary_effective_good_units`
- Required bad-action minimum: 24
- Current bad-action count: 41
- Canonical action types represented: 14
- No represented canonical action type is singleton.
- Separate retired action-bank files have been removed; the current bank is `candidate_actions.json`.

## Primary Good Scope

The primary good scope is intentionally conservative. A missing primary action should reasonably reduce add-side recall.

| Action | Type | Intent |
| --- | --- | --- |
| `CA-000034` | `FILTER_ROWS` | Remove `ctl_vehicle` training rows from the labeled training distribution. |
| `CA-000008` | `DROP_COLUMNS` | Remove the unique `sig_id` identifier from model features. |
| `CA-000012` | `DROP_COLUMNS` | Drop `cp_type` after the control-row filter, when it is constant for treated training rows. |
| `CA-000020` | `ENCODE_CATEGORICAL` | One-hot encode treatment duration and dose. |
| `CA-000031` | `ORDINAL_ENCODE` | Ordinally encode treatment duration and dose. |
| `CA-000003` | `APPLY_EXPRESSION` | Apply RankGauss normalization to gene and cell features. |
| `CA-000043` | `PCA_REDUCTION` | Add separate PCA features over gene-expression columns. |
| `CA-000047` | `PCA_REDUCTION` | Add separate PCA features over cell-viability columns. |
| `CA-000026` | `FEATURE_SELECTION` | Apply variance-based feature selection to numeric features. |

`CA-000020` and `CA-000031` are alternatives for the same treatment-metadata encoding need. They share the `lish_moa_categorical_encoding_strategy` equivalence group, so they count as one effective primary add unit.

## Non-Primary Good Scope

Two observed notebook-backed feature-engineering patterns are retained for all-scope evaluation only:

- `CA-000005`: KMeans cluster features over gene and cell groups.
- `CA-000039`: row-level summary statistics over gene and cell groups.

These are uncommon and model-specific. They should not enlarge the primary add-side denominator, and a reasonable primary-only human baseline may omit them.

## Good-Action Evidence Summary

Manual close reading covered 30 selected public notebooks.

| Action | Stage | Type | Equivalence group | Evidence summary |
| --- | --- | --- | --- | --- |
| `CA-000003` | `core_preprocessing` | `APPLY_EXPRESSION` | - | Observed in 11 of 30 notebooks and repeatedly used in strong PCA/NN pipelines. |
| `CA-000005` | `model_specific_preprocessing` | `APPLY_EXPRESSION` | - | Observed in 4 of 30 notebooks. Kept for all-scope evaluation only because it is uncommon and model/pipeline-specific. |
| `CA-000008` | `core_preprocessing` | `DROP_COLUMNS` | - | All 30 reviewed notebooks exclude `sig_id` before constructing the feature matrix. |
| `CA-000012` | `core_preprocessing` | `DROP_COLUMNS` | - | Observed in 15 of 30 notebooks. Must happen after the control-row filter if `cp_type` is needed to identify controls. |
| `CA-000020` | `core_preprocessing` | `ENCODE_CATEGORICAL` | `lish_moa_categorical_encoding_strategy` | One-hot encoding is the most common treatment-metadata strategy, observed in 19 of 30 reviewed notebooks. |
| `CA-000026` | `core_preprocessing` | `FEATURE_SELECTION` | - | Observed in 15 of 30 notebooks. The canonical threshold 0.8 follows strong Kushal/VBMokin/Riad-style pipelines. |
| `CA-000031` | `core_preprocessing` | `ORDINAL_ENCODE` | `lish_moa_categorical_encoding_strategy` | Observed in 12 of 30 notebooks. It satisfies the same preprocessing need as one-hot encoding. |
| `CA-000034` | `core_preprocessing` | `FILTER_ROWS` | - | Observed in 24 of 30 reviewed notebooks. Applied to training rows; test controls are usually retained for submission and assigned near-zero predictions. |
| `CA-000039` | `model_specific_preprocessing` | `APPLY_EXPRESSION` | - | Observed in 6 of 30 notebooks. Kept for all-scope evaluation but not primary core because it is optional extended feature engineering. |
| `CA-000043` | `core_preprocessing` | `PCA_REDUCTION` | - | Observed in 13 of 30 notebooks. Component counts vary, but the canonical high-capacity variant follows strong Kushal/VBMokin-style notebooks. |
| `CA-000047` | `core_preprocessing` | `PCA_REDUCTION` | - | Observed in 13 of 30 notebooks, usually paired with gene PCA while keeping the two feature groups separate. |

## Bad-Action Bank Design

Bad actions are synthetic remove targets and near-miss distractors. They are designed to be clear faults with task-specific failure modes.

The current bad bank includes:

- inverted or over-broad row filters
- identifier leakage
- dropping predictive feature groups or treatment metadata
- split-inconsistent PCA, RankGauss, and feature-selection steps
- overly destructive dimensionality reduction or feature pruning
- invalid numeric transforms for signed assay values
- destructive clipping and binning of continuous assay features
- generic numeric scaling substitutes for the observed RankGauss path
- target leakage through supervised encodings or unavailable labels
- high-dimensional interaction explosions
- destructive row sampling

Synthetic rows are traceable through `derived_from_action_ids` or `base_refs` plus `derivation_reasoning`.

## Canonical Action-Type Coverage

The bank is domain-scoped to LISH MoA rather than Zillow-style full canonical coverage.

| Action type | Total | Good | Bad |
| --- | ---: | ---: | ---: |
| `APPLY_EXPRESSION` | 11 | 3 | 8 |
| `BIN_NUMERIC` | 2 | 0 | 2 |
| `CLIP_OUTLIERS` | 2 | 0 | 2 |
| `DROP_COLUMNS` | 6 | 2 | 4 |
| `ENCODE_CATEGORICAL` | 4 | 1 | 3 |
| `FEATURE_SELECTION` | 4 | 1 | 3 |
| `FILTER_ROWS` | 5 | 1 | 4 |
| `INTERACTION_FEATURE` | 2 | 0 | 2 |
| `LOG_TRANSFORM` | 2 | 0 | 2 |
| `ORDINAL_ENCODE` | 2 | 1 | 1 |
| `PCA_REDUCTION` | 6 | 2 | 4 |
| `POWER_TRANSFORM` | 2 | 0 | 2 |
| `SAMPLE_ROWS` | 2 | 0 | 2 |
| `SCALE_NUMERIC` | 2 | 0 | 2 |

This is not a Zillow-style 40-family coverage bank. Some absent families are clearly inapplicable to the available single-table, non-temporal, non-text LISH MoA feature matrix, including datetime parsing, time-window features, text vectorization, lookup joins, and rolling or lag features. Other mechanically possible families remain future expansion candidates if the task later targets broader canonical-family coverage.

## Testcase Suite

The current testcase suite follows the four standard scenario roles. Expected add/remove targets are derived by the evaluator from the full bank, the context, and active stage scope; they are not stored in testcase files.

| Testcase | Scenario | Context actions | Primary add units | Primary remove actions | All-scope add units | All-scope remove actions |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `tc1_from_scratch` | `from_scratch` | none | 8 | 0 | 10 | 0 |
| `tc2_partial_good` | `partial_good` | `CA-000003`, `CA-000008`, `CA-000034` | 5 | 0 | 7 | 0 |
| `tc3_fault_injected` | `fault_injected` | `CA-000001`, `CA-000014`, `CA-000022`, `CA-000033` | 8 | 4 | 10 | 4 |
| `tc4_mixed_history` | `mixed` | `CA-000008`, `CA-000014`, `CA-000020`, `CA-000030`, `CA-000049` | 6 | 3 | 8 | 3 |

`tc4_mixed_history` includes `CA-000020`, so the `lish_moa_categorical_encoding_strategy` equivalence unit is already satisfied in that context and `CA-000031` is not expected as an additional primary action.

## Current Artifact Status

- `candidate_actions.json`: rebuilt and validates.
- `task.json`: reviewed and retained as shared competition metadata.
- `notes.md`: rewritten for the current action-bank contract.
- `testcases/`: authored with four standard scenario files.
- `human_baseline/`: TC1 human baseline authored as a true bank-ID selection against the current candidate bank.
- `outputs/`: intentionally absent; previous draft outputs were deleted.

## Authoring Reminders

- Keep hidden scoring metadata out of agent-facing testcase prompts.
- Re-check every testcase after any bank ID, role, equivalence, or order change.
- Future output artifacts must include required `artifact_refs` when sidecar provenance exists.
- Human baseline revisions should remain true bank-ID authoring against the current `candidate_actions.json`, not migrations from older action formats.
