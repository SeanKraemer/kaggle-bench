# Eval Migration Log

This file is the working memory for the Zillow action-bank benchmark migration.

The benchmark should be authored as a standalone system, not as an extension of the old evaluator. This log exists only to preserve context about what changed and why.

## Status

- [x] Planning doc created
- [x] Benchmark README created
- [x] Initial schema scaffolding created
- [x] Zillow task skeleton created
- [x] Initial candidate action bank authored
- [x] Zillow testcase contexts migrated
- [x] Zillow human baseline re-authored to bank ids
- [x] Canonical validator implemented
- [x] Canonical evaluator implemented
- [x] Canonical aggregate report generator implemented
- [x] Evaluator and validator tests added
- [x] Zillow example outputs authored under the new schema
- [x] Zillow benchmark reports generated
- [ ] Old/new comparison report generated

## Contract Diff

The right-hand column below records the historical staging contract used during the POC before canonicalization.
The live benchmark contract now uses canonical paths under `eval/`, `data/schema/`, and `data/tasks/`.

| Area | Legacy exact-match eval | Historical POC staging contract |
| --- | --- | --- |
| Task artifacts | `data/tasks/<slug>/` | `data/new_tasks/<slug>/` |
| Schema root | `data/schema/` | `data/new_schema/` |
| Good actions | `golden_actions.json` | `candidate_actions.json` with `role = good` |
| Bad actions | `fault_actions.json` | `candidate_actions.json` with `role = bad` |
| Testcase state | `input.pre_actions` | `input.context_action_ids` |
| Testcase source of truth | explicit `expected.*` | derived from bank metadata + context + scope |
| Output contract | canonical action objects | action-id `add/remove` sets |
| Suggested-side semantics | exact match over canonical actions | add-side bank-id retrieval over derived candidate set |
| Rollback-side semantics | discouraged canonical actions | remove-side bank-id retrieval over context set |
| Alternative good actions | testcase expected OR units | hidden bank-level `equivalence_group` |
| Dependencies/conflicts | ordered output rules | hidden bank-level precedence-graph rules |
| Stage scope | `primary` / `all` | preserved |
| Binary success | threshold on task score | preserved |

## Current Decisions

### 2026-03-30

- Initial benchmark staging roots:
  - `new_eval/`
  - `data/new_schema/`
  - `data/new_tasks/`
- Zillow is the only POC task for now.
- Every testcase uses the full task-level bank.
- Testcases store only `context_action_ids`.
- The evaluator derives `candidate_action_ids = full_bank_action_ids - context_action_ids`.
- `predicted_add_action_ids` must come from the derived candidate set.
- `predicted_remove_action_ids` must come from the context set.
- `context_action_ids` and derived `candidate_action_ids` are disjoint and their union is the full bank.
- Expected add/remove sets are not stored in testcase files.
- Expected sets are derived from bank metadata, testcase context, and active stage scope.
- The bank is intentionally imbalanced:
  - validator hard gate: `bad >= 3 * primary effective good units`
  - hard bad coverage is important
- `role` is only `good` or `bad`.
- `difficulty` is `easy`, `medium`, or `hard`.
- `role` is not a metric axis in v1; it is bank curation and target-derivation metadata.
- Good candidates should preserve gold-style metadata:
  - `source_profile`
  - `context_notes`
  - `evidence_snippets`
  - `rareness`
  - `confidence`
- Good candidates should use notebook-backed provenance.
- Bad candidates may be notebook-observed or synthetic.
- Synthetic bad candidates are scored the same way as observed bad candidates.
- Hidden scoring metadata should stay out of agent-facing benchmark renderings:
  - `equivalence_group`
  - `must_follow_action_ids`
  - `invalidates_action_ids`
  - `conflicts_with_action_ids`
- Equivalent good actions should score as one add-side unit.
- Dependency and invalidation checks should be applied by asking whether the selected final action set admits at least one valid execution order.
- `must_follow_action_ids` and `invalidates_action_ids` should be interpreted as precedence edges in that execution-order check.
- `conflicts_with_action_ids` should be reserved for truly incompatible combinations that no ordering can salvage.
- Output arrays are unordered unique sets.
- Duplicate predictions should be schema-invalid; if they still reach scoring, they count as false positives.
- Invalid ids or invalid membership should not crash scoring; they count as false positives.
- Stage scope should stay aligned with the old benchmark:
  - `primary`
  - `all`
- `eval_stage` stays on candidate rows.
- Headline metrics:
  - `add_precision`
  - `add_recall`
  - `add_f1`
  - `remove_precision`
  - `remove_recall`
  - `remove_f1`
  - `rollback_accuracy = remove_recall` (legacy alias)
  - `task_completion_score = 0.5 * add_f1 + 0.5 * remove_recall`
  - `strict_task_completion_score = 0.5 * add_f1 + 0.5 * remove_f1`
- Empty-case convention should stay aligned with the old evaluator.
- Binary success should stay aligned with the old evaluator threshold style.
- Human baseline is required, but initial scope is only `tc1_human`.
- The benchmark validator should be a separate implementation:
  - `eval/scripts/validate_artifacts.py`
- New bank action ids use the benchmark-native `CA-*` namespace rather than reusing legacy `GA-*` or `FA-*` ids.
- The current Zillow candidate bank draft contains:
  - 115 total candidates
  - 15 `good`
  - 100 `bad`
  - 9 primary effective good units after equivalence-group collapse
  - strong `hard bad` coverage
  - full `40 / 40` action-type coverage against the current canonical action vocabulary in `data/schema/canonical_actions.json`
  - no singleton represented action types; every represented canonical type now has at least two bank rows
- The four Zillow testcase files have been migrated into the new testcase contract using only `context_action_ids`.
- `tc1_human` has been re-authored directly against the new bank rather than strictly migrated from old canonical-action outputs.
- The re-authored human baseline currently keeps only the bank actions with clear notebook support and defensible mappings.
- The Zillow POC task is now fixed to the 2016 slice:
  - `train_2016_v2.csv`
  - `properties_2016.csv`
- This slice-specific benchmark assumption now lives in:
  - `data/tasks/zillow-prize-1/notes.md`
  - `candidate_actions.json`
  - testcase contexts
  rather than in `task.json`, which is inherited unchanged from the legacy task root.
- The overlapping blanket `fillna(-1)` good action was removed from the bank to keep missing-value scoring deterministic.
- The remaining missing-value family is curated as:
  - broad numeric median imputation
  - sparse count zero-fill
  - sparse flag FALSE fill
- Several higher-variance feature-engineering actions were moved out of `core_preprocessing` to reduce primary-scope ambiguity.
- Validation-split negatives now share `validation_protocol` stage semantics with their source good action.
- The validator now checks:
  - crash-safe testcase parsing
  - same-stage `equivalence_group` membership
  - representative good-set execution-order coherence
  - testcase-context execution-order coherence
  - output final-state execution-order coherence
- `eval/eval.py` is now implemented with:
  - derived add/remove targets from bank + context + scope
  - stage-filtered non-core predictions in `primary` scope
  - equivalence-group collapse on the add side
  - final-state validity checks over selected actions
  - old-aligned headline metrics plus `strict_task_completion_score`
- Unit coverage now includes:
  - equivalence-group satisfaction from context
  - stage-filtered predictions in `primary`
  - invalid add predictions from final-state conflicts
  - empty-side scoring semantics
  - validator regression checks for ratio, cross-stage groups, crash safety, and invalid final states
- `eval/aggregate.py` is now implemented with:
  - discovery of `outputs/`, `adapted_outputs/`, and `human_baseline/`
  - grouped agent/testcase summaries
  - benchmark-level markdown/json reports under `eval/results/benchmarks/`
- `data/tasks/<slug>/task.json` should inherit the shared competition metadata unchanged by default.
- Benchmark-specific assumptions that differ from legacy task metadata should live in:
  - `data/tasks/<slug>/notes.md`

### 2026-03-30 Canonicalization

- The benchmark now lives at canonical repo paths:
  - `eval/`
  - `data/schema/`
  - `data/tasks/`
- The temporary staging roots remain in this log only as migration history and should not be treated as live contract paths.
  - `candidate_actions.json`
  - testcase contexts

## Open Items

- Review and refine the initial synthetic negative bank for realism and diversity.
- Tighten documentation so README, authoring guide, and generated reports reflect the current implementation state without stale references.
- Generate a clearer old/new comparison write-up once the narrative comparison is ready.

## Explicitly Deferred Or Rejected

- Do not build an automatic legacy-output adapter for now.
  - Mechanical conversion from old canonical-action objects to new bank-id add/remove outputs is too lossy to treat as reliable comparison evidence.

## Resolved Semantic Issue

### Ordered invalidation vs unordered add/remove

This was resolved on 2026-03-30.

- The scorer should not use naive final-state conflicts for destructive-order cases.
- Instead, it should validate the implied selected final action set by checking whether at least one valid execution order exists.
- Old `must_follow_action_ids` and `invalidates_action_ids` metadata should therefore carry over into the new bank as hidden precedence metadata.

## Notes For Future Updates

- Append dated entries rather than rewriting old decisions away.
- If the benchmark contract changes, update both this file and `eval/README.md`.
- If a choice is only for migration convenience and should not affect the benchmark itself, say that explicitly here.
