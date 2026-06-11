# home-credit-default-risk Benchmark Notes

This task root defines the action-bank benchmark task for Home Credit.

## Benchmark Shape

- Task artifacts live under `data/tasks/home-credit-default-risk/`.
- Machine-checked schemas live under `data/schema/`.
- Evaluator code and reports live under `eval/`.

## Task Contract

- The benchmark uses the Home Credit competition tables named in [task.json](./task.json).
- The main supervised entity is one row per applicant / current loan application keyed by `SK_ID_CURR`.
- The benchmark is therefore a state-editing problem over an applicant-level multi-table preprocessing pipeline.
- The task-level bank lives in [candidate_actions.json](./candidate_actions.json).
- Every testcase uses the same full bank.
- Each testcase stores only `input.context_action_ids`.
- The evaluator derives:
  - `candidate_action_ids = full_bank_action_ids - context_action_ids`
  - expected add units from the active good portion of the derived candidate side
  - expected remove units from the active bad portion of the context side

## Home Credit-Specific Assumptions

- This task rewards applicant-level aggregation over the auxiliary history tables and penalizes raw one-to-many joins that duplicate `SK_ID_CURR`.
- The strongest good path remains:
  - application-table cleanup and ratio features
  - one application categorical encoding strategy
  - customer-level aggregates from `bureau`, `previous_application`, `POS_CASH_balance`, `installments_payments`, and `credit_card_balance`
  - left joins of those aggregate tables back onto the main application table
- High-value bad behavior remains:
  - harmful `DAYS_EMPLOYED` sentinel filtering or destructive replacement
  - raw joins from history tables directly onto the main application table
  - wrong-grain aggregates such as `SK_ID_PREV` / `SK_ID_BUREAU` rollups where `SK_ID_CURR` is required
  - sparse-feature row dropping and destructive key drops

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

## Current Bank Snapshot

- Current draft bank size: `137` actions
- Good actions: `21`
- Bad actions: `116`
- Primary effective good units after equivalence-group collapse: `15`
- The validator hard gate is `bad >= 3 * primary effective good units`.
- Canonical action-type coverage is currently `40 / 40` against `data/schema/canonical_actions.json`.
- No represented canonical action type is singleton; every represented family currently has at least two rows.

## Bank Curation Notes

- Good rows were seeded from the earlier Home Credit gold set, then rewritten into the benchmark-native `CA-*` namespace.
- Bad rows combine migrated legacy faults with synthetic hard negatives aimed at relational failure modes that matter in Home Credit.
- The bank intentionally over-indexes on:
  - wrong join type
  - raw one-to-many joins
  - wrong-grain aggregation
  - destructive drops
  - harmful missing-value handling
- The broad coverage tail is larger than the old exact-match task because the new benchmark needs nearby distractors, not just one gold path plus a small fault library.

## Testcase Semantics

The four standard testcase roles are:

- [tc1_from_scratch.json](./testcases/tc1_from_scratch.json)
  - empty context
  - checks full add-side planning from scratch
- [tc2_partial_good.json](./testcases/tc2_partial_good.json)
  - context already contains part of the good path
  - checks continuation without redoing already-good work
- [tc3_fault_injected.json](./testcases/tc3_fault_injected.json)
  - context contains only bad actions
  - checks rollback of harmful filtering and raw one-to-many joins
- [tc4_mixed_history.json](./testcases/tc4_mixed_history.json)
  - context contains both good and bad history
  - checks selective editing under mixed state

Current Home Credit testcase shape:

- `tc1`
  - empty state
- `tc2`
  - application cleanup plus one application encoding strategy and previous-application aggregate/join already present
- `tc3`
  - bad-only state built from a harmful `DAYS_EMPLOYED` filter plus raw `bureau`, `previous_application`, and `POS_CASH_balance` joins
- `tc4`
  - coherent bureau and POS good history already present, mixed with sparse-score row dropping and a raw installments join fault

## Provenance Basis

- The current bank reuses the notebook evidence gathered during the earlier Home Credit authoring pass.
- Important evidence inputs remain:
  - `data/collector/data/kaggle/home-credit-default-risk/notebooks.json`
  - `data/collector/data/golden/home-credit-default-risk/action_candidates.jsonl`
  - `data/collector/data/golden/home-credit-default-risk/manual_close_reading_snippets.md`
  - raw notebook files under `data/collector/data/kaggle/home-credit-default-risk/notebooks/`
- The strongest backbone evidence still comes from winner-style Home Credit notebooks centered on applicant-level aggregate-table construction and join-back.

## Current Migration Status

- [x] `candidate_actions.json` authored
- [x] candidate-bank review and cleanup completed
- [x] testcase files migrated to `context_action_ids`
- [x] testcase semantics reviewed after migration
- [x] `human_baseline/tc1_human.json` re-authored to bank ids
- [x] `outputs/*.json` rewritten to `predicted_add_action_ids` / `predicted_remove_action_ids`
- [x] task-level reports regenerated after output and human-baseline migration

## Authoring Reminders

- Treat this as a standalone benchmark contract even when reusing legacy Home Credit evidence.
- Keep notebook-backed provenance explicit for good actions.
- Maintain the imbalanced bank with `bad >> good`.
- Keep testcase difficulty in the contexts, not in custom per-testcase candidate subsets.
- Re-check testcase coherence whenever the bank changes; do not assume old contexts stay valid after bank edits.
