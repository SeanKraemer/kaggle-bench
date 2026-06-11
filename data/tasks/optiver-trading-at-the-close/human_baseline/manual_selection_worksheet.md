# Optiver TC1 Manual Selection Worksheet

- Task: `optiver-trading-at-the-close`
- Testcase: `tc1_from_scratch`
- Context: empty, so this artifact only selects `predicted_add_action_ids`
- Workflow: plain-English shortlist first, bank-id alignment second

## Manual Shortlist Before Bank Mapping

This shortlist was frozen before translating anything into `CA-*` ids.

1. Keep the simple default fills for the two key auction-price fields rather than dropping them outright.
2. Keep the first-order imbalance and pairwise price-dislocation block.
3. Keep one simple imbalance-ratio style feature.
4. Keep one lag family over the stock-time sequence.
5. Keep one stock-prior strategy rather than multiple overlapping grouped summaries.
6. Keep simple clock features from the integer time columns.
7. Stop there rather than include memory downcasting, grouped-median repair, or the heavier higher-order interaction branch in the baseline.

## Final Bank Mapping

After the plain-English shortlist was fixed, the current bank was consulted only to align the selected behaviors to the current benchmark ids.

- `CA-000061`: zero-fill `far_price`
- `CA-000020`: default-fill `near_price` with `1`
- `CA-000001`: keep the main order-book imbalance block
- `CA-000043`: keep the pairwise price-difference block
- `CA-000065`: keep the simpler imbalance-ratio feature
- `CA-000031`: keep one stock-level lag family
- `CA-000049`: keep one stock-prior strategy
- `CA-000051`: derive compact clock features from `date_id` and `seconds_in_bucket`

## Final Predicted Add IDs

```text
CA-000001
CA-000020
CA-000031
CA-000043
CA-000049
CA-000051
CA-000061
CA-000065
```

## Intentionally Omitted

- `CA-000054`: memory downcasting is practical engineering hygiene, but it did not feel essential enough to keep in the manual baseline.
- `CA-000059`: grouped-median repair across auction seconds was intentionally left out of the first-pass baseline.
- `CA-000063`: the higher-order interaction block was also left out as a second-wave expansion.
- `CA-000011`, `CA-000012`: these remain valid alternatives for stock-prior and missing-value strategy, but I kept only one representative from each family.
- `CA-000008`, `CA-000045`, `CA-000046`: broader feature-expansion branches were intentionally omitted.
- `CA-000016`, `CA-000018`, `CA-000024`, `CA-000050`: model-specific scaling, extra imputation, and rolling-window steps remain out of scope for this TC1 baseline.
