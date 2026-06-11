# Rossmann TC1 Manual Selection Worksheet

- Task: `rossmann-store-sales`
- Testcase: `tc1_from_scratch`
- Context: empty, so this artifact only selects `predicted_add_action_ids`
- Workflow: plain-English shortlist first, bank-id alignment second

## Manual Shortlist Before Bank Mapping

This shortlist was frozen before translating anything into `CA-*` ids.

1. Join the daily sales rows with the static `store.csv` metadata.
2. Parse `Date` and extract the basic calendar parts needed for a forecasting baseline.
3. Keep one simple closed-store filtering rule in the training data.
4. Impute `CompetitionDistance`, because it is a central numeric store feature with moderate missingness.
5. Encode the small low-cardinality categorical block (`StateHoliday`, `StoreType`, `Assortment`) with one simple strategy.
6. Drop `Customers`, because it is present in train only and would leak unavailable future information.
7. Stop there rather than force competition-timing derivations, the full promo-repair branch, or extra all-scope cleanup into the baseline.

## Final Bank Mapping

After the plain-English shortlist was fixed, the current bank was consulted only to align the selected behaviors to the current benchmark ids.

- `CA-000044`: join `train` and `test` with `store.csv` on `Store`
- `CA-000036`: parse `Date`
- `CA-000021`: derive `year`, `month`, and `day` from `Date`
- `CA-000048`: use the `Open == 1` closed-store filtering branch
- `CA-000006`: median-impute `CompetitionDistance`
- `CA-000004`: use the label-encoding branch for `StateHoliday`, `StoreType`, and `Assortment`
- `CA-000042`: drop `Customers`

## Final Predicted Add IDs

```text
CA-000044
CA-000036
CA-000021
CA-000048
CA-000006
CA-000004
CA-000042
```

## Intentionally Omitted

- `CA-000031`, `CA-000020`: competitor opening date repair and the derived competition-age feature are plausible, but they felt like the first clear second-wave Rossmann branch once the basic store/calendar scaffold was already in place.
- `CA-000017`: filling the small number of missing `Open` values in test is practical, but I did not keep this all-scope step in the manual first-pass baseline.
- `CA-000018`, `CA-000052`, `CA-000035`: the promo-specific repair and promo-month feature block felt like a second-wave refinement rather than the minimum believable manual baseline.
- `CA-000045`: dropping raw `Date` after feature derivation is a reasonable cleanup step, but it is not essential to this TC1 manual baseline.
- `CA-000057`: valid one-hot alternative, but I kept a single simple encoding strategy.
- `CA-000058`: valid closed-store alternative, but I kept only one closure rule and used the simpler `Open == 1` branch.
