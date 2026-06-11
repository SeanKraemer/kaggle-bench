# spaceship-titanic Benchmark Notes

This task root defines the canonical action-bank benchmark task for Spaceship Titanic.

## Benchmark Shape

- Task artifacts live under `data/tasks/spaceship-titanic/`.
- Machine-checked schemas live under `data/schema/`.
- Evaluator code and reports live under `eval/`.

## Task Contract

- This benchmark uses a single task-level action bank in `candidate_actions.json`.
- Every testcase uses the same full bank.
- Each testcase stores only `input.context_action_ids`.
- The evaluator derives:
  - add-side targets from the active good portion of the bank that is still missing from context
  - remove-side targets from the active bad portion of the context
- Outputs are unordered unique bank-id sets:
  - `predicted_add_action_ids`
  - `predicted_remove_action_ids`

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

## Spaceship Benchmark Scope

- Testcases in scope:
  - `tc1_from_scratch`
  - `tc2_partial_good`
  - `tc3_fault_injected`
  - `tc4_mixed_history`
- Human baseline scope:
  - `tc1_human`

## Current Bank Snapshot

- Current draft bank size: 51 actions
- Good actions: 15
- Bad actions: 36
- Primary good rows: 13
- Primary effective good units after equivalence-group collapse: 11
- The bank order was reshuffled with seed `20260413`, then all Spaceship `CA-*` ids were renumbered to remove front-loaded label leakage.
- The validator hard gate is `bad >= 3 * primary effective good units`.
- The current bank keeps the core preprocessing spine conservative while concentrating hard negative coverage around destructive drops, malformed spend features, weak imputations, and identifier encodings.

## Spaceship Primary Spine

The current primary benchmark is built around these effective units:

- cabin split
- passenger-group split
- total-spend feature
- no-spending feature
- CryoSleep zero-spend rule
- group-size aggregation
- one age-imputation strategy via the shared equivalence group
- categorical/boolean mode imputation
- spending zero-fill
- one categorical-encoding strategy via the shared equivalence group
- raw-column drop

Numeric scaling remains in the bank as `model_specific_preprocessing`, but it does not affect the primary headline score.

## Authoring Reminders

- Treat this benchmark as a standalone action-bank contract rather than an extension of the old exact-match evaluator.
- Keep notebook-backed evidence explicit for good actions.
- Preserve a strong `bad >> good` imbalance and prefer hard negatives over evaluator heuristics.
- Task-specific benchmark assumptions should live in this file and the bank, not in `task.json`.
