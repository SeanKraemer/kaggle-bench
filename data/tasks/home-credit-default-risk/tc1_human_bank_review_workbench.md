# TC1 Human Output Bank Review Workbench

This file is a review index for manually selecting the `tc1_human` output for Home Credit.

It is intentionally a categorization layer only.
It does not recommend which actions to choose.

## TC1 Constraint

- [tc1_from_scratch.json](./testcases/tc1_from_scratch.json) has empty context.
- So the final `tc1_human.json` can only add actions.
- `predicted_remove_action_ids` should stay empty for TC1.
- This workbench still indexes the full bank so the add-side choices can be made after reviewing nearby alternatives and negatives.

## Coverage

- Total bank size: `137`
- Good actions: `21`
- Bad actions: `116`

Every `CA-*` in [candidate_actions.json](./candidate_actions.json) is covered exactly once below.

## 1. Main Application Good Path

Purpose:
main-table cleanup, ratio features, anomaly handling, and the preferred categorical-encoding choices that live on or very near the main application table.

- `APPLY_EXPRESSION`: `CA-000082`, `CA-000102`
- `ENCODE_CATEGORICAL`: `CA-000010`, `CA-000023`, `CA-000076`
- `FILTER_ROWS`: `CA-000017`
- `INTERACTION_FEATURE`: `CA-000036`
- `RATIO_FEATURE`: `CA-000030`, `CA-000134`

## 2. Relational Good Path

Purpose:
customer-level aggregates and aggregate join-backs for the auxiliary history tables.

- `GROUP_AGG`: `CA-000004`, `CA-000056`, `CA-000062`, `CA-000089`, `CA-000095`, `CA-000108`, `CA-000115`
- `JOIN_LOOKUP`: `CA-000043`, `CA-000049`, `CA-000069`, `CA-000121`, `CA-000128`

## 3. Destructive Main-Table Errors

Purpose:
bad actions that directly drop rows, drop columns, or overwrite core application fields before useful features can be built.

- `DROP_COLUMNS`: `CA-000011`, `CA-000039`, `CA-000042`, `CA-000045`, `CA-000116`
- `DROP_ROWS_WITH_MISSING`: `CA-000038`, `CA-000105`, `CA-000112`, `CA-000130`
- `FILTER_ROWS`: `CA-000005`, `CA-000044`
- `IMPUTE_MISSING`: `CA-000001`, `CA-000032`, `CA-000090`, `CA-000091`, `CA-000092`

## 4. Core Semantic Near-Miss Features

Purpose:
actions that are close to the preferred main path but encode the wrong feature definition or the wrong categorical strategy.

- `APPLY_EXPRESSION`: `CA-000014`, `CA-000015`, `CA-000132`
- `ENCODE_CATEGORICAL`: `CA-000022`, `CA-000055`, `CA-000073`, `CA-000075`
- `INTERACTION_FEATURE`: `CA-000007`
- `RATIO_FEATURE`: `CA-000029`, `CA-000123`

## 5. Relational Aggregate Mistakes

Purpose:
aggregates with the wrong grain, too-narrow summaries, or notebook-local derived summaries that diverge from the preferred backbone.

- `GROUP_AGG`: `CA-000009`, `CA-000016`, `CA-000024`, `CA-000034`, `CA-000035`, `CA-000046`, `CA-000058`, `CA-000061`, `CA-000067`, `CA-000079`, `CA-000093`, `CA-000101`, `CA-000122`, `CA-000125`, `CA-000137`

## 6. Relational Join Mistakes

Purpose:
join-level failure modes, especially row explosion and wrong join type.

- `JOIN_LOOKUP`: `CA-000008`, `CA-000018`, `CA-000025`, `CA-000054`, `CA-000057`, `CA-000080`, `CA-000081`, `CA-000088`, `CA-000097`, `CA-000110`, `CA-000118`, `CA-000119`, `CA-000124`, `CA-000127`, `CA-000136`

## 7. Numeric Handling And Hygiene Tail

Purpose:
generic numeric-preprocessing branches that are mechanically possible but not part of the Home Credit preferred path.

- `BIN_NUMERIC`: `CA-000051`, `CA-000074`
- `CAST_DTYPE`: `CA-000019`, `CA-000117`
- `CLIP_OUTLIERS`: `CA-000078`, `CA-000104`
- `CREATE_MISSING_INDICATOR`: `CA-000072`, `CA-000135`
- `REPLACE_INF`: `CA-000013`, `CA-000106`
- `SCALE_NUMERIC`: `CA-000037`, `CA-000094`

## 8. Temporal And Sequence-Like Tail

Purpose:
calendar-style or ordered-history feature families that are broad enough to be task-applicable but are not part of the benchmark-preferred backbone.

- `CYCLICAL_ENCODE`: `CA-000033`, `CA-000107`
- `DATE_PART_FEATURE`: `CA-000002`, `CA-000068`
- `DIFF_FEATURE`: `CA-000040`, `CA-000085`
- `EXPANDING_WINDOW_FEATURE`: `CA-000027`, `CA-000048`
- `LAG_FEATURE`: `CA-000050`, `CA-000059`
- `PARSE_DATETIME`: `CA-000020`, `CA-000021`
- `ROLLING_WINDOW_FEATURE`: `CA-000063`, `CA-000066`
- `TIME_SINCE_REFERENCE`: `CA-000077`, `CA-000096`

## 9. Pruning, Selection, And Sampling Tail

Purpose:
branches that prune rows or columns, deduplicate, reduce the active feature set, or alter evaluation protocol via sampling.

- `DROP_CONSTANT_COLUMNS`: `CA-000103`, `CA-000131`
- `DROP_DUPLICATES`: `CA-000087`, `CA-000126`
- `DROP_HIGH_NULL_COLUMNS`: `CA-000006`, `CA-000047`
- `FEATURE_SELECTION`: `CA-000003`, `CA-000129`
- `SAMPLE_ROWS`: `CA-000031`, `CA-000071`

## 10. Interaction And Transform Tail

Purpose:
generic nonlinear interaction or numeric-transform families that are plausible but not part of the retained core path.

- `HASH_CROSS`: `CA-000026`, `CA-000109`
- `LOG_TRANSFORM`: `CA-000012`, `CA-000113`
- `PCA_REDUCTION`: `CA-000041`, `CA-000065`
- `POLYNOMIAL_FEATURE`: `CA-000083`, `CA-000111`
- `POWER_TRANSFORM`: `CA-000028`, `CA-000052`

## 11. Category And Text-Like Tail

Purpose:
broader categorical normalization / encoding families and text-like branches that are mechanically possible under the current schema.

- `MAP_CATEGORIES`: `CA-000086`, `CA-000114`
- `NORMALIZE_STRING`: `CA-000064`, `CA-000099`
- `ORDINAL_ENCODE`: `CA-000084`, `CA-000100`
- `RARE_CATEGORY_BUCKETIZE`: `CA-000098`, `CA-000133`
- `TARGET_ENCODE_OOF`: `CA-000070`, `CA-000120`
- `TEXT_VECTORIZATION`: `CA-000053`, `CA-000060`

## Suggested Review Order

If the goal is to decide `tc1_human` fairly but efficiently, use this order:

1. Main Application Good Path
2. Relational Good Path
3. Core Semantic Near-Miss Features
4. Relational Aggregate Mistakes
5. Relational Join Mistakes
6. Destructive Main-Table Errors
7. The broad generic tail sections only after the task-native sections are settled

## Working Rule For TC1 Human Selection

- Review everything.
- Select only add-side actions that the human notebook actually supports.
- Do not force broader current-bank coverage if the notebook did not really do it.
- Use the bad and near-miss categories as comparison context, not as default selection candidates.
