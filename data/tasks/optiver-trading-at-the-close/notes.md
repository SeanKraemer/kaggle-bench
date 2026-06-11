# Optiver Trading At The Close Action-Bank Benchmark Notes

This task uses the action-bank evaluator now defined under `eval/` and `data/schema/`.
Shared competition metadata stays in `task.json`; benchmark-local curation lives in `candidate_actions.json` and testcase contexts.

## Benchmark Focus

- auction imbalance features over stock/time buckets
- lag, diff, and rolling-window signals within stock trajectories
- price and size cleanup before grouped temporal feature construction


## Candidate Bank Summary

- Total candidates: `73`
- Good candidates: `20`
- Bad candidates: `53`
- Primary effective good units: `14` (core_preprocessing, after equivalence-group collapse)
- Model-specific good units: `4`
- Represented action types: `14`
- Equivalence groups: `optiver_remaining_nan_strategy` and `optiver_stock_prior_strategy`
- Bad-to-primary ratio: `53 / 14 = 3.8x` (exceeds the minimum `3x` gate)
- No singleton families: every represented action type has at least 2 rows.
- Candidate ids use the label-neutral `CA-*` namespace.
- Hidden evaluator semantics such as `equivalence_group`, `must_follow_action_ids`, and `invalidates_action_ids` live in the bank rather than in testcase files.

## Testcase Semantics

- `tc1_from_scratch`: empty context, pure add-side recovery from the task-level bank.
- `tc2_partial_good`: the main imbalance block, both Optiver-specific auction-price defaults, and one lag family are already present; the agent only needs the missing additions.
- `tc3_fault_injected`: harmful actions are already in context and should be removed while missing good actions are recovered.
- `tc4_mixed_history`: stock-prior, lag, and clock features are already present while three harmful actions remain in context; the agent must preserve, add, and roll back in one pass.

## Outputs And Human Baseline

- Outputs now predict `predicted_add_action_ids` and `predicted_remove_action_ids`, not inline canonical actions.
- `human_baseline/tc1_human.json` is a manually rebuilt TC1 baseline. `human_baseline/work.ipynb` is an evidence-only inspection notebook, while `human_baseline/manual_selection_worksheet.md` is the authoritative shortlist-to-bank mapping.

## Validation

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task optiver-trading-at-the-close --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/optiver-trading-at-the-close-primary.md
uv run python eval/aggregate.py --task optiver-trading-at-the-close --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/optiver-trading-at-the-close-all.md
```
