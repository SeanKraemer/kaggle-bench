# Santander Customer Transaction Prediction - Human Baseline Notes


## TC1 selection rationale from scratch

I treated the Santander task as a small but competition-specific preprocessing problem. The complete core path covers:

- DROP_COLUMNS ID_code (CA-000002)
- APPLY_EXPRESSION identify real test rows via per-feature value uniqueness (CA-000005)
- APPLY_EXPRESSION value-count features from train + real test (CA-000009)

For the human baseline, I kept the obvious identifier drop and the value-count feature idea, but I missed the separate real-test-row isolation step. That is a plausible mistake here because the synthetic-row discovery is the hidden competition trick; a quick notebook pass can find value counts without fully separating real and synthetic test rows first.

- DROP_COLUMNS ID_code (CA-000002)
- APPLY_EXPRESSION value-count features from train + real test (CA-000009)
