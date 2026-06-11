# Porto Seguro Safe Driver Prediction Action-Bank Benchmark Notes

This task uses the action-bank evaluator defined under `eval/` and `data/schema/`.
Shared competition metadata stays in `task.json`; benchmark-local curation lives in `candidate_actions.json` and testcase contexts.

## Benchmark Focus

- sentinel-aware missingness cleanup for the `-1` encoded missing values
- dropping calc/high-null noise columns before encoding
- categorical imputation (mode) and numeric imputation (mean) after sentinel replacement
- missing indicator creation to preserve missingness signal
- id column removal for single-table classification (no joins/groups needed)
- categorical encoding strategy selection (one-hot vs target encoding)
- model-specific scaling, binning, interaction features, and feature selection
- validation-level deduplication

## Candidate Bank Summary

- Total candidates: `75`
- Good candidates: `14`
- Bad candidates: `61`
- Primary effective good units: `7` (core_preprocessing, after equivalence group collapse)
- Model-specific good units: `6` (includes one equivalence group: `porto_categorical_encoding`)
- Validation-protocol good units: `1`
- Represented action types: `28` (11 good types, 27 bad types)
- Equivalence groups: `porto_categorical_encoding` (CA-000013 onehot OR CA-000045 target-encode)
- Candidate ids use the label-neutral `CA-*` namespace.
- Hidden evaluator semantics (`equivalence_group`, `must_follow_action_ids`, `invalidates_action_ids`) live in the bank, not in testcase files.
- Bad-to-primary ratio: `61 / 7 = 8.7x` (exceeds the minimum `3x` gate)
- No singleton families: every represented action type has at least 2 rows.

## Testcase Semantics

- `tc1_from_scratch`: empty context, pure add-side recovery from the task-level bank.
- `tc2_partial_good`: sentinel replacement + high-null drop + categorical imputation already present. Agent must recover remaining core good actions (id drop, calc drop, numeric imputation, missing indicators) plus model-specific actions.
- `tc3_fault_injected`: two harmful actions in context (scale-categorical-codes + replace-sentinel-with-zero). Agent must remove both faults and recover all missing good actions.
- `tc4_mixed_history`: mixed state with sentinel replacement + calc drop preserved, plus three faults (replace-sentinel-with-zero, over-aggressive high-null threshold, mean-impute-categoricals). Agent must preserve the good actions, remove all three faults, and add the remaining good actions.

## Outputs And Human Baseline

- Outputs predict `predicted_add_action_ids` and `predicted_remove_action_ids`, not inline canonical actions.
- `human_baseline/tc1_human.json` is a manually rebuilt TC1 baseline. `human_baseline/work.ipynb` is an evidence-only inspection notebook, while `human_baseline/manual_selection_worksheet.md` is the authoritative shortlist-to-bank mapping.
- The rebuilt human baseline was authored from competition reasoning first and aligned to the current bank only after the shortlist was frozen.

## Validation

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task porto-seguro-safe-driver-prediction --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/porto-seguro-safe-driver-prediction-primary.md
uv run python eval/aggregate.py --task porto-seguro-safe-driver-prediction --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/porto-seguro-safe-driver-prediction-all.md
```
