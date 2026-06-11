# Elo TC1 Manual Selection Worksheet

- Task: `elo-merchant-category-recommendation`
- Testcase: `tc1_from_scratch`
- Context: empty, so this artifact only selects `predicted_add_action_ids`
- Workflow: plain-English shortlist first, bank-id alignment second

## Manual Shortlist Before Bank Mapping

This shortlist was frozen before translating anything into `CA-*` ids.

1. Turn `first_active_month` into a compact card-age block.
2. One-hot encode the three low-cardinality base-card features.
3. Compute the recurring `month_diff` recency feature inside the transaction tables.
4. Aggregate the strongest numeric transaction summaries back to `card_id` for historical transactions.
5. Mirror the same numeric aggregation path for new-merchant transactions.
6. Stop there rather than forcing the transaction-flag cleanup branch or the heavier category-dummy and categorical-aggregation branch into the baseline.

## Final Bank Mapping

After the plain-English shortlist was fixed, the current bank was consulted only to align the selected behaviors to the current benchmark ids.

- `CA-000004`: extract year and month from `first_active_month`
- `CA-000047`: compute elapsed time from the reference date
- `CA-000035`: one-hot encode `feature_1`
- `CA-000011`: one-hot encode `feature_2`
- `CA-000062`: one-hot encode `feature_3`
- `CA-000051`: compute `month_diff`
- `CA-000060`: aggregate historical numeric transaction summaries to `card_id`
- `CA-000049`: aggregate new-merchant numeric transaction summaries to `card_id`

## Final Predicted Add IDs

```text
CA-000004
CA-000047
CA-000035
CA-000011
CA-000062
CA-000051
CA-000060
CA-000049
```

## Intentionally Omitted

- `CA-000019`, `CA-000058`: the two transaction-flag encodes are reasonable, but they felt like the first obvious second-wave Elo cleanup once the base-card block and numeric transaction summaries were already present.
- `CA-000042`, `CA-000031`: category_2 and category_3 dummy expansion were left out because this baseline stops before the heavier categorical aggregation branch.
- `CA-000040`, `CA-000072`: historical and new categorical aggregate blocks were intentionally omitted for the same reason.
- `CA-000050`, `CA-000065`: diversity-count aggregates remain out of scope for this TC1 baseline.
