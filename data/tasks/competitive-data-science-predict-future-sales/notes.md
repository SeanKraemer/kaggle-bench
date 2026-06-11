# competitive-data-science-predict-future-sales Benchmark Notes

This task root defines the canonical action-bank benchmark task for Predict Future Sales.

## Benchmark Shape

- Task artifacts live under `data/tasks/competitive-data-science-predict-future-sales/`.
- Machine-checked schemas live under `data/schema/`.
- Evaluator code and reports live under `eval/`.

## Task Contract

- This benchmark uses a single task-level action bank in `candidate_actions.json`.
- Every testcase uses the same full bank.
- Each testcase stores only `input.context_action_ids`.
- The evaluator derives:
  - add-side targets from the active good portion of the bank that is still missing from context
  - remove-side targets from the active bad portion of the context
- Outputs are unordered unique bank-id sets:
  - `predicted_add_action_ids`
  - `predicted_remove_action_ids`

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

## Predict Future Sales Scope

- Official competition files only:
  - `sales_train.csv`
  - `test.csv`
  - `items.csv`
  - `item_categories.csv`
  - `shops.csv`
  - `sample_submission.csv`
- Benchmark slice:
  - raw daily sales
  - monthly shop-item aggregation
  - official-only lagged forecasting features
- External data is excluded from benchmark-defining good actions.

## Benchmark Assumptions

- The benchmark assumes the standard competition workflow converts daily sales into a month-level `shop_id x item_id x date_block_num` representation before lag features are built.
- Full shop-item-month grid completion is treated as a workflow assumption documented here rather than as a standalone scored canonical action row, because the current ontology does not expose a first-class cartesian-grid construction action.
- The primary score therefore focuses on actions that can be expressed cleanly and scored deterministically inside the existing evaluator contract.

## Current Bank Snapshot

- Current draft bank size: 42 actions
- Good actions: 13
- Bad actions: 29
- Primary effective good units after equivalence-group collapse: 8
- The validator hard gate is `bad >= 3 * primary effective good units`.
- The bank keeps the headline score anchored to the conservative monthly forecasting spine while pushing text-derived shop/category parsing, richer recency features, and encoding branches into `model_specific_preprocessing`.
- Bank ids were interleaved and renumbered to avoid front-loaded label leakage, following the same rationale used in the Spaceship task renumbering pass.

## Predict Future Sales Primary Spine

The current primary benchmark is built around these effective units:

- parse raw `date`
- filter gross transaction anomalies
- aggregate `item_cnt_day` to monthly `item_cnt_month`
- join `items.csv` to recover `item_category_id`
- clip monthly target to `[0, 20]`
- build shop-item target lags
- zero-fill lag gaps
- drop the first 12 months after introducing 12-step lags

## Model-Specific Branches

The bank keeps these branches outside the primary headline score:

- month/day calendar features from `date_block_num`
- shop-city and category-type text decomposition
- categorical encoding for city/type/subtype features
- first-sale / last-sale style recency features
- raw name-column cleanup after text-derived features are materialized

## Authoring Reminders

- Treat this benchmark as a standalone action-bank contract rather than a direct transcription of any one notebook.
- Keep notebook-backed evidence explicit for good actions.
- Preserve a strong `bad >> good` imbalance and prefer hard distractors over weak noise.
- Keep official-only provenance as the benchmark source of truth even when external-data notebooks are reviewed as background.
