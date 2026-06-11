# AMEX Default Prediction Action-Bank Benchmark Notes

This task uses the action-bank evaluator now defined under `eval/` and `data/schema/`.
Shared competition metadata stays in `task.json`; benchmark-local curation lives in `candidate_actions.json` and testcase contexts.

## Benchmark Focus

- customer-level aggregation from monthly statement history
- missingness handling, missing indicators, and cautious pruning
- recency, delta, and post-aggregation feature blocks

## Candidate Bank Summary

- Total candidates: `70`
- Good candidates: `20`
- Bad candidates: `50`
- Primary effective good units: `14`
- Model-specific good units: `3` (`CA-000015`, `CA-000017`, `CA-000060`)
- Equivalence groups: `2`
- Candidate ids use the label-neutral `CA-*` namespace.
- Hidden evaluator semantics such as `equivalence_group`, `must_follow_action_ids`, and `invalidates_action_ids` live in the bank rather than in testcase files.
- `preprocessing_complexity_raw` in `task.json` tracks primary effective good units after equivalence-group collapse and excludes `model_specific_preprocessing` rows.
- Placeholder `legacy_near_miss_variant_*` formulas and stale `#suggested_actions[...]` refs have been removed.
- Represented action families no longer contain singletons.

## Testcase Semantics

- `tc1_from_scratch`: empty context, pure add-side recovery from the task-level bank.
- `tc2_partial_good`: the richer numeric/categorical aggregation variants are already present, so the agent only needs the missing cleanup and recency actions.
- `tc3_fault_injected`: harmful actions are already in context and should be removed while missing good actions are recovered.
- `tc4_mixed_history`: valid context and harmful context coexist, so the agent must preserve the upstream good scaffold, add the missing aggregation/cleanup steps, and roll back harmful history in one pass.

## Outputs And Human Baseline

- Outputs now predict `predicted_add_action_ids` and `predicted_remove_action_ids`, not inline canonical actions.
- The human bundle now reads notebook-first and bank-second: the worksheet records the plain-English shortlist, while the trace and metadata document the late bank-id alignment.

## Benchmark Contract

- The evaluator scores action ids only; testcase files contain scenario input and context ids, not inline expected canonical actions.
- Expected model and human predictions live in output artifacts via `predicted_add_action_ids` and `predicted_remove_action_ids`.
- Schema validity and review completeness are tracked separately: this branch now satisfies both the structural contract and the substantive review pass for the AMEX task.

## Validation

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task amex-default-prediction --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/amex-default-prediction-primary.md
uv run python eval/aggregate.py --task amex-default-prediction --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/amex-default-prediction-all.md
```
