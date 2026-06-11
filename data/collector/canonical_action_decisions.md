# Canonical Action Decisions Log

This document records canonical action schema change history (`add/update/deprecate`).

## [2026-03-09] amex-default-prediction / multiple notebooks

- Change type: `update`

- Schema before change:
  - `GROUP_AGG.validation_rules.agg_functions`: `["mean","sum","min","max","std","median","count","nunique"]`
  - `golden_action.schema.json` GROUP_AGG agg_functions enum: same (no `last`, `first`)

- Schema after change:
  - `GROUP_AGG.validation_rules.agg_functions`: `["mean","sum","min","max","std","median","count","nunique","last","first"]`
  - `golden_action.schema.json` GROUP_AGG (and GROUP_AGG_FEATURE, GROUP_AGG_JOIN) agg_functions enum: added `"last"`, `"first"`

- Reason for change:
  - `last` and `first` are standard pandas `.agg()` functions essential for time-series competitions where the most recent / earliest value per group carries strong signal. They appear in the majority of top AMEX notebooks. The omission was a schema gap not a deliberate exclusion.

- Impact scope:
  - No existing datasets need reprocessing (zillow-prize-1 does not use `last`/`first` in GROUP_AGG)

- Related evidence:
  - `train.groupby('customer_ID')[num_features].agg(['mean', 'std', 'min', 'max', 'last'])`
  - `cdeotte/xgboost-starter-0-793`, `ragnar123/amex-lgbm-dart-cv-0-7977`

## Log Template

### [YYYY-MM-DD] <competition_slug> / <notebook_ref>

- Change type: `add|update|deprecate`
- Schema before change:
  - `<action_type and schema>`
- Schema after change:
  - `<action_type and schema>`
- Reason for change:
  - Specify applicable rationale among need for generalization / leakage prevention / ambiguity resolution
- Impact scope:
  - Whether existing datasets need reprocessing, and target scope
- Related evidence:
  - Notebook code snippet or link
