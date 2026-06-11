# Task Authoring Guide

This guide documents how to add and maintain one action-bank benchmark task under `data/tasks/<competition_slug>/`.

Use this document for authoring conventions.
Use `notes.md` in each task directory for task-local benchmark rationale and testcase semantics.
Use `data/schema/*.json` as the machine-checked source of truth for benchmark artifacts.
Use `eval/README.md` for evaluator semantics.
Use `task_review_rules.md` for review-time judgment rules.

## 1. Directory Layout

Each task lives under:

```text
data/tasks/<competition_slug>/
  task.json
  candidate_actions.json
  notes.md
  testcases/
    tc1_from_scratch.json
    tc2_partial_good.json
    tc3_fault_injected.json
    tc4_mixed_history.json
  outputs/
    <testcase>_<agent>_<run>.json
    provenance/
      ...
  human_baseline/
    tc1_human.json
    notes.md
    provenance/
      ...
```

`outputs/` is optional while a task is still being authored, but the bank, testcases, and at least one human baseline should exist before the task is treated as review-ready.

`<competition_slug>` should match the Kaggle competition slug, for example `zillow-prize-1`.

## 2. File Roles

### `task.json`

Shared task context for all testcases in the competition.

Keep this file for information that should not vary by testcase:

- competition slug
- dataset file layout
- goal
- task characteristics for analysis
- competition overview
- dataset description
- evaluation metric

Schema:

- `data/schema/task.schema.json`

Migration default:

- if the competition already exists under `data/tasks/<competition_slug>/task.json`, copy that file unchanged by default
- keep benchmark-specific bank/testcase assumptions in `notes.md`, `candidate_actions.json`, and testcase contexts rather than rewriting shared competition metadata

`task_characteristics` is still the standardized place for task-level analysis labels used in cross-task comparisons.

Current required raw fields:

- `dataset_size_raw`
- `feature_dimensionality_raw`
- `preprocessing_complexity_raw`

Current convention for raw values:

- `dataset_size_raw`
  - recommended metric: largest relevant table row count
- `feature_dimensionality_raw`
  - recommended metric: benchmark-relevant case-insensitive column union count
- `preprocessing_complexity_raw`
  - for migrated tasks, preserve the inherited legacy task metadata value from `data/tasks/<competition_slug>/task.json`
  - do not force this field to equal the evaluator's derived `primary_effective_good_unit_count`
  - if authoring a task from scratch, document the chosen metric in `notes.md`

Important distinction:

- `primary_effective_good_unit_count` is a reviewer/evaluator concept derived from the bank
- it is not required to equal `task_characteristics.preprocessing_complexity_raw`

Shared bucket thresholds live in:

- `data/schema/task_characteristic_bucket_criteria.json`

### `candidate_actions.json`

The task-level candidate bank.

This is the core artifact of the benchmark.
Every testcase uses the same full bank.

Each row should represent one candidate action with:

- stable `action_id`
- canonical `action_type`
- canonical `canonical_params`
- `eval_stage`
- `role`
- `difficulty`
- `reasoning`
- `provenance_type`

Schema:

- `data/schema/candidate_actions.schema.json`

Authoring requirements:

- use canonical action vocabulary from `data/schema/canonical_actions.json`
- keep `action_id` stable once a task is in active use
- use `role = good` only for actions you want the evaluator to derive as add targets
- use `role = bad` for actions you want the evaluator to derive as remove targets when present in context
- keep hidden scoring metadata in the bank, not in testcase files

Hidden scoring metadata may include:

- `equivalence_group`
- `must_follow_action_ids`
- `invalidates_action_ids`
- `conflicts_with_action_ids`

Hidden-order authoring rule:

- if the benchmark expects a set of selected actions to coexist, author hidden metadata so that at least one valid execution order exists for that set
- do not use `conflicts_with_action_ids` for cases that are actually salvageable by ordering

Evidence rules:

- `good` candidates must use `observed_notebook` provenance
- `good` candidates must include:
  - `notebook_refs`
  - `source_profile`
  - `context_notes`
  - `evidence_snippets`
  - `rareness`
  - `confidence`
- `synthetic` candidates must include:
  - `derivation_reasoning`
  - and at least one of:
    - `base_refs`
    - `derived_from_action_ids`

Bank composition rules:

- `bad_count >= 3 * primary_effective_good_unit_count`
- every represented canonical action family should have at least `2` bank rows
- high-salience or benchmark-target families should usually have at least `3` nearby rows
- do not use singleton family rows as pure coverage hints
- the bank should cover as many task-applicable canonical action families as reasonably possible
- exclude a canonical family only when it is clearly inapplicable to the task inputs, table structure, or available columns

### `testcases/*.json`

Scenario definitions.

Each testcase stores only:

- shared task reference
- `input.scenario`
- `input.context_action_ids`

Schema:

- `data/schema/testcase.schema.json`

Important:

- testcase files do not store `expected_add_action_ids`
- testcase files do not store `expected_remove_action_ids`
- expected add/remove targets are derived by the evaluator from:
  - `candidate_actions.json`
  - `context_action_ids`
  - active stage scope

Current scenario values:

- `from_scratch`
- `partial_good`
- `fault_injected`
- `mixed`

Scenario conventions:

- `tc1_from_scratch`
  - empty context
- `tc2_partial_good`
  - context already contains some good actions
- `tc3_fault_injected`
  - context contains bad actions that should be removed
- `tc4_mixed_history`
  - context contains both good and bad history

### `outputs/*.json`

Agent submission artifacts.

Each output file represents one run for one testcase.
Repeated attempts for Pass@k should be stored as multiple sibling output files rather than as an array of runs inside one JSON artifact.

Schema:

- `data/schema/output.schema.json`

Current required fields:

- `competition_slug`
- `testcase_id`
- `agent_name`
- `run_by`
- `run_id`
- `artifact_refs`
- `predicted_add_action_ids`
- `predicted_remove_action_ids`
- `time_spent_seconds`
- `token_usage`
- `notes`

Important:

- outputs must predict bank IDs, not inline canonical action objects
- output arrays are unordered unique sets
- `predicted_add_action_ids` must refer to actions outside the testcase context
- `predicted_remove_action_ids` must refer only to actions already in the testcase context
- the same action id must not appear in both `predicted_add_action_ids` and `predicted_remove_action_ids`
- keep one run per JSON file
- every `artifact_refs[].path` must point to a real file
- supported `artifact_refs[].kind` values are:
  - `trace` for human-readable execution traces
  - `log` for plain log files
  - `metadata` for structured run telemetry consumed by the evaluator
  - `notebook` for scratch or authored notebooks
  - `notes` for supporting markdown notes
  - `prompt` for captured final prompt text sent to an agent or model
  - `stream` for raw streamed event logs such as jsonl traces
  - `scratchpad` for run-local agent scratchpad state
  - `tool_calls` for normalized tool-call jsonl records
  - `api_calls` for sanitized model request/response jsonl records
  - `other` for real sidecars that do not fit the standard buckets

Recommended sidecars:

- trace markdown or logs
- metadata JSON
- prompt markdown when prompt provenance matters
- stream logs when the agent exposes raw streamed events
- scratchpad, tool-call, and sanitized API-call logs for agentic methods
- scratch notebook or notes

### `human_baseline/`

Human baseline for TC1.

- `tc1_human.json` uses the same schema as normal output files
- the human baseline acts like one more baseline agent in evaluation
- initial scope is only `tc1_human` unless the task explicitly expands human coverage

Recommended contents:

- `notes.md`
- `provenance/metadata.json`
- `provenance/action_trace.json`
- optional scratch notebook or markdown work artifacts referenced through `artifact_refs`

Human-baseline provenance rule:

- explicitly state whether the human baseline is:
  - a true bank-id authoring under the current benchmark contract, or
  - a lossy migration from a legacy canonical-action output
- keep that distinction visible in notes or provenance metadata

## 3. Authoring Rules

### Task-Level Rules

- `competition_slug` should match the directory name
- `task.json` is shared context, not a dump of every artifact
- if the benchmark is intended to score a fixed slice of the competition data, state that slice explicitly in `notes.md`

### Candidate-Bank Rules

- do not author the bank as a thin wrapper around legacy golden/fault artifacts
- do not author only winner-style actions
- include awkward, weak, and non-preferred but still task-applicable canonical families
- keep `good` conservative enough that missing a truly important action should reduce add-side recall
- when two good rows are true alternatives, use:
  - `equivalence_group`, or
  - narrower definitions so they no longer overlap
- if a represented family only has one row, keep authoring until it has at least one additional nearby row

### Testcase Rules

- testcase files should reference action IDs only
- every testcase sees the same full bank
- testcase difficulty should come from `context_action_ids`, not from custom candidate subsets
- when the bank changes, re-check all testcase contexts; do not assume old contexts still induce clean targets

### Output Rules

- output files should look like agent predictions, not answer keys
- `run_by` is the human operator, not the system name
- keep traces, notes, and telemetry in sidecar files referenced by `artifact_refs`
- every nontrivial output should include at least one `metadata` ref when structured telemetry exists

## 4. Validation

Run:

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
```

What is checked by the validator:

- schema validity against `data/schema/*.json`
- unknown action IDs
- invalid context membership
- invalid add/remove membership
- invalid duplicate IDs
- hidden metadata reference consistency
- same-stage `equivalence_group` membership
- bank-level execution-order coherence
- testcase-context execution-order coherence
- output final-state execution-order coherence
- artifact reference existence

Important evaluator behavior:

- invalid add/remove IDs should not crash scoring
- they should be recorded and counted as false positives

## 5. Suggested Workflow

1. Create `data/tasks/<competition_slug>/`.
2. Add `task.json`.
3. Build and manually review `candidate_actions.json`.
4. Add scenario files under `testcases/`.
5. Add at least `human_baseline/tc1_human.json` plus provenance artifacts.
6. Add agent outputs under `outputs/` when comparison runs are available.
7. Run validator and tests.
8. Open PR only after manual review of bank coverage, hidden-order coherence, and testcase semantics.

## 6. Zillow Example

Use `data/tasks/zillow-prize-1/` as the current reference example for:

- `task.json`
- `candidate_actions.json`
- testcase layout
- human baseline layout
- bank-level hidden scoring metadata
- broad canonical-family coverage under one fixed task slice
