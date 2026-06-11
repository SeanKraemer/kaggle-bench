# Porto TC1 Manual Selection Worksheet

- Task: `porto-seguro-safe-driver-prediction`
- Testcase: `tc1_from_scratch`
- Context: empty, so this artifact only selects `predicted_add_action_ids`
- Workflow: plain-English shortlist first, bank-id alignment second

## Manual Shortlist Before Bank Mapping

This shortlist was frozen before translating anything into `CA-*` ids.

1. Replace the `-1` sentinel with standard missing values.
2. Drop the two very sparse categorical columns rather than try to rescue them.
3. Drop the weak `ps_calc_*` feature family.
4. Drop the row identifier.
5. Stop there rather than add typed imputation, missing indicators, or model-specific encoding choices to the baseline.

## Final Bank Mapping

After the plain-English shortlist was fixed, the current bank was consulted only to align the selected behaviors to the current benchmark ids.

- `CA-000019`: replace the `-1` sentinel with `NaN`
- `CA-000029`: drop `ps_car_03_cat` and `ps_car_05_cat`
- `CA-000008`: drop the `ps_calc_*` block
- `CA-000040`: drop `id`

## Final Predicted Add IDs

```text
CA-000019
CA-000029
CA-000008
CA-000040
```

## Intentionally Omitted

- `CA-000003`, `CA-000024`: typed imputation is practical, but it felt like the first clearly second-wave cleanup after the structural pruning steps were already in place.
- `CA-000035`: missing indicators were left out because the manual baseline stops after the structural cleanup steps.
- `CA-000013`, `CA-000045`, `CA-000051`, `CA-000056`, `CA-000061`, `CA-000067`: model-specific encoding, scaling, feature-selection, binning, and interaction steps remain out of scope for this TC1 baseline.
- `CA-000075`: deduplication is also left out of the manual baseline.
