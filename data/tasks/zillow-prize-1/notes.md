# zillow-prize-1 Benchmark Notes

This task root defines the canonical action-bank benchmark task for Zillow.

## Benchmark Shape

- Task artifacts live under `data/tasks/zillow-prize-1/`.
- Machine-checked schemas live under `data/schema/`.
- Evaluator code and reports live under `eval/`.

## Task Contract

- This benchmark slice is fixed to `train_2016_v2.csv` with `properties_2016.csv`.
- The task-level bank will live in `candidate_actions.json`.
- Every testcase uses the same full bank.
- Each testcase stores only `input.context_action_ids`.
- The evaluator derives:
  - `candidate_action_ids = full_bank_action_ids - context_action_ids`
  - expected add units from the active good portion of the derived candidate side
  - expected remove units from the active bad portion of the context side

## Scoring Metadata

The bank may include hidden scoring metadata that should stay out of agent-facing benchmark renderings:

- `equivalence_group`
- `must_follow_action_ids`
- `invalidates_action_ids`
- `conflicts_with_action_ids`

These fields are for evaluator logic only.

## Scope

- `primary` scores only `eval_stage = core_preprocessing`
- `all` scores every active stage

## Zillow POC Scope

- Testcases to migrate:
  - `tc1_from_scratch`
  - `tc2_partial_good`
  - `tc3_fault_injected`
  - `tc4_mixed_history`
- Human baseline scope:
  - `tc1_human`

## Current Bank Snapshot

- Current draft bank size: 115 actions
- Good actions: 15
- Bad actions: 100
- Primary effective good units after equivalence-group collapse: 9
- The validator hard gate is `bad >= 3 * primary effective good units`.
- The current draft intentionally over-indexes on hard bad actions, synthetic near-miss negatives, and broad canonical-family coverage.
- Canonical action-type coverage is now `40 / 40` against `data/schema/canonical_actions.json`.
- No represented canonical action type is singleton; the bank now keeps at least two rows per represented type.

## Authoring Reminders

- Treat this as a standalone benchmark contract even when reusing Zillow notebook evidence.
- Keep notebook-backed evidence explicit for good actions.
- Maintain a strongly imbalanced bank with `bad >> good`.
- Preserve migration rationale separately in `eval/migration_log.md`.
