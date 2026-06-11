# Elo Merchant Category Recommendation Action-Bank Benchmark Notes

This task uses the action-bank evaluator now defined under `eval/` and `data/schema/`.
Shared competition metadata stays in `task.json`; benchmark-local curation lives in `candidate_actions.json` and testcase contexts.

## Benchmark Focus

- card-age features derived from `first_active_month`
- repeated transaction flag/category encodings plus shared `month_diff` recency features
- card-level aggregation over historical and new-merchant transaction tables


## Candidate Bank Summary

- Total candidates: `66`
- Good candidates: `16`
- Bad candidates: `50`
- Primary effective good units: `14`
- Model-specific good units: `2` (`CA-000050`, `CA-000065`)
- Candidate ids use the label-neutral `CA-*` namespace.
- Hidden evaluator semantics such as `equivalence_group` and `invalidates_action_ids` live in the bank rather than in testcase files.
- Former prerequisite chains for card-age, recency, and categorical aggregation blocks were collapsed into self-contained benchmark units during review cleanup.
- Standalone `PARSE_DATETIME` rows were removed from the scored slice once those downstream units became self-contained.

## Testcase Semantics

- `tc1_from_scratch`: empty context, pure add-side recovery from the task-level bank.
- `tc2_partial_good`: some correct actions are already present, so the agent only needs the missing additions.
- `tc3_fault_injected`: harmful actions are already in context and should be removed while missing good actions are recovered.
- `tc4_mixed_history`: valid context and harmful context coexist, so the agent must preserve, add, and roll back in one pass.

## Outputs And Human Baseline

- Outputs now predict `predicted_add_action_ids` and `predicted_remove_action_ids`, not inline canonical actions.
- Example output artifacts are intentionally minimal prediction records; benchmark semantics live in the candidate bank, testcase contexts, and regenerated aggregate reports.
- `human_baseline/tc1_human.json` is a manually rebuilt TC1 baseline. `human_baseline/work.ipynb` is an evidence-only inspection notebook, while `human_baseline/manual_selection_worksheet.md` is the authoritative shortlist-to-bank mapping.

## Validation

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task elo-merchant-category-recommendation --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/elo-merchant-category-recommendation-primary.md
uv run python eval/aggregate.py --task elo-merchant-category-recommendation --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/elo-merchant-category-recommendation-all.md
```
