# ieee-fraud-detection Benchmark Notes

This task root defines the canonical action-bank benchmark task for IEEE Fraud Detection.

## Benchmark Shape

- Task artifacts live under `data/tasks/ieee-fraud-detection/`.
- Machine-checked schemas live under `data/schema/`.
- Evaluator code and reports live under `eval/`.

## Task Contract

- This benchmark is defined over the IEEE transaction and identity tables keyed by `TransactionID`.
- The rewarded relational setup assumes a non-destructive identity lookup join:
  - transaction table on the left
  - identity table on the right
  - `how = left`
- The rewarded time-engineering path assumes `TransactionDT` is a relative second offset anchored to a task-local reference date, not a literal Unix timestamp.
- The task-level bank lives in `candidate_actions.json`.
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

IEEE-specific hidden-order use:

- UID construction alternatives collapse by equivalence rather than scoring as separate add units.
- UID aggregation rows depend on the corresponding UID-construction branch.
- interaction-key encoding depends on the upstream interaction-key construction row.

## Scope

- `primary` scores only `eval_stage = core_preprocessing`
- `all` scores every active stage

## IEEE Task Scope

- Testcases migrated to the new contract:
  - `tc1_from_scratch`
  - `tc2_partial_good`
  - `tc3_fault_injected`
  - `tc4_mixed_history`
- Human baseline target scope:
  - `tc1_human`

Core-preprocessing emphasis for IEEE:

- identity left join
- UID construction
- anchored time conversion and derived time parts
- email-domain grouping and match-style features
- device / browser / OS parsing
- broad categorical frequency encoding
- ratio-to-group-stat features
- UID-centered aggregations

Model-specific families intentionally kept out of primary:

- amount-fraction variants
- direct log transform
- interaction-key construction
- label encoding of interaction keys

## Current Bank Snapshot

- Current draft bank size: 90 actions
- Good actions: 17
- Bad actions: 73
- Primary effective good units after equivalence-group collapse: 10
- The validator hard gate is `bad >= 3 * primary effective good units`.
- Canonical action-type coverage is `40 / 40` against `data/schema/canonical_actions.json`.
- No represented canonical action type is singleton; every represented type currently has at least two rows.
- The current draft intentionally keeps primary good conservative and pushes most action-space coverage into synthetic bad or near-miss rows.

Current bank shape is deliberately stronger on:

- join / UID / time / email / device / aggregation families
- destructive rollback faults
- broad canonical action coverage

Current bank shape is still weaker than Zillow on:

- good-side provenance density
- hard negative density around local IEEE decision boundaries

## Authoring Reminders

- Treat this as a standalone benchmark contract even when reusing IEEE notebook evidence from the legacy task.
- Keep notebook-backed evidence explicit for good actions.
- Prefer IEEE-local harmful negatives over generic canonical coverage filler whenever possible.
- Preserve benchmark-specific assumptions here rather than rewriting `task.json`.
- Preserve migration rationale separately in `eval/migration_log.md`.
