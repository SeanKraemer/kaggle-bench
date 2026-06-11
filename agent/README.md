# Agent Directory

This directory contains the benchmark runners, shared infrastructure, and tests for the preprocessing-repair baselines.

In plain English, the code here does one job:
- read a benchmark task, a testcase, and a candidate action bank
- decide which candidate preprocessing actions should be added and which active actions should be removed
- write a standardized prediction JSON plus provenance artifacts

The important split is:
- shared benchmark plumbing in `agent/`
- method-specific runners in:
  - `agent/rule_based/`
  - `agent/single_llm/`
  - `agent/claude_code/`

For a longer implementation review, see [METHOD_IMPLEMENTATION_REVIEW.md](/agent/METHOD_IMPLEMENTATION_REVIEW.md).

## What This Directory Does

Each method in this directory solves the same benchmark problem:
- the benchmark gives a `task`
- each `testcase` gives a current pipeline state through `context_action_ids`
- the method must predict:
  - which action IDs should be added
  - which already-active action IDs should be removed

Every method is constrained to choose only from the provided candidate action bank. No method is allowed to invent new preprocessing steps outside that bank.

## Tiny End-To-End Example

Minimal shapes look like this:

`task.json`-side information:

```json
{
  "goal": "Repair the preprocessing pipeline for this tabular task.",
  "dataset": {
    "primary_key": "parcelid",
    "target_column": "logerror",
    "train_files": ["train_2016_v2.csv"],
    "lookup_files": ["properties_2016.csv"]
  }
}
```

`testcase.json`-side information:

```json
{
  "input": {
    "context_action_ids": ["CA-000108"]
  }
}
```

One visible candidate action:

```json
{
  "action_id": "CA-000107",
  "action_type": "JOIN_LOOKUP",
  "canonical_params": {
    "how": "left",
    "right_table_id": "properties_2016"
  }
}
```

Final prediction shape:

```json
{
  "predicted_add_action_ids": ["CA-000107"],
  "predicted_remove_action_ids": ["CA-000108"]
}
```

Interpretation:
- `CA-000107` is not active yet, so the method proposes adding it
- `CA-000108` is already active in the testcase context, so the method proposes removing it

This example is only one valid task shape.
- some tasks have no `lookup_files`
- some tasks omit `primary_key`
- some tasks expose multiple train or lookup tables

## Start Here: Method Summary

- [rule_based/README.md](/agent/rule_based/README.md)
  - deterministic heuristic baseline
  - evidence source: locally materialized structured profiles
  - model/tool use: none
  - expected profile: cheapest and most inspectable
- [single_llm/README.md](/agent/single_llm/README.md)
  - one-shot Anthropic API baseline
  - evidence source: precomputed structured summary rendered into the prompt
  - model/tool use: single model call, no tools
  - expected profile: semantically richer than `rule_based`, but no iterative evidence gathering
- [claude_code/README.md](/agent/claude_code/README.md)
  - Claude Code CLI baseline
  - evidence source: raw workspace files and raw dataset files
  - model/tool use: tool-using CLI agent
  - expected profile: most agentic, most expensive, richest telemetry

## Shared Terms

- `task`
  - the benchmark-level problem definition, including dataset metadata such as target column, train/lookup table paths, and optional primary key
- `testcase`
  - one repair scenario for the task; it mainly differs by which actions are already active in `context_action_ids`
- `candidate action bank`
  - the full benchmark action list from `candidate_actions.json`
- `visible action bank`
  - the reduced action view exposed to methods: only `action_id`, `action_type`, `canonical_params`
- `context_action_ids`
  - the action IDs that are already active in the current testcase and may need to be preserved or rolled back
- `provenance`
  - side artifacts that explain a run, such as metadata, prompt text, traces, or raw event streams
- `trace`
  - the human-readable per-run log used for debugging and qualitative analysis

## What Every Method Shares

All methods are built around the same benchmark contract.

Shared inputs:
- `task.json`
- `testcases/<testcase_id>.json`
- `candidate_actions.json`
- dataset files resolved from `task["dataset"]`

Shared output contract:
- benchmark-compatible output JSON in `data/tasks/<competition>/outputs/`
- provenance metadata and trace in `data/tasks/<competition>/outputs/provenance/`

Shared action visibility policy:
- methods only see:
  - `action_id`
  - `action_type`
  - `canonical_params`
- this is enforced in [action_bank.py](/agent/action_bank.py)

Shared core files:
- [task_bundle.py](/agent/task_bundle.py): loads task/testcase/action-bank bundle
- [action_bank.py](/agent/action_bank.py): builds the agent-visible action bank
- [data_access.py](/agent/data_access.py): resolves dataset paths and loads CSV rows
- [context_builder.py](/agent/context_builder.py): builds shared benchmark context
- [prediction_validation.py](/agent/prediction_validation.py): normalizes and validates add/remove predictions
- [output_artifacts.py](/agent/output_artifacts.py): writes output, metadata, trace, and extra provenance artifacts
- [summaries.py](/agent/summaries.py): renders dataset/context/action summaries for prompts and traces

## Shared Context Model

[context_builder.py](/agent/context_builder.py) exposes two levels of context:

- `BenchmarkContext`
  - lightweight
  - contains the task bundle, visible action bank, rendered testcase summary, candidate action JSON, and dataset file paths
  - does not materialize CSV contents
- `MaterializedBenchmarkContext`
  - heavier
  - inspects all referenced train and lookup tables first
  - loads each table sequentially, using full rows for smaller tables and deterministic uniform samples for larger ones
  - computes per-table structured profiles
  - exposes `primary_train_profile` for `task["dataset"]["train_files"][0]`
  - may compute one optional join profile when a visible `JOIN_LOOKUP` can be resolved to raw tables
  - renders a dataset summary string

Current implementation detail:
- the first train file is treated as the primary evidence surface for `rule_based`
- target profiling uses the first train file that actually contains the target column, which covers label-sidecar layouts
- join resolution prefers visible `JOIN_LOOKUP` metadata (`left_on`, `right_on`, `right_table_id`) that maps to raw dataset files
- if no visible raw-table join can be resolved, the current fallback is a same-name join on `task["dataset"]["primary_key"]` when present and a lookup table exists
- if neither path works, the materialized context keeps the per-table profiles and leaves join coverage at zero
- `.csv.zip` inputs are loaded transparently through `data_access.py`
- large tables switch to deterministic uniform sampling for profile generation, and the summaries record that sampling metadata

Current method usage:
- `rule_based`: uses `BenchmarkContext` plus `MaterializedBenchmarkContext`
- `single_llm`: uses `BenchmarkContext` plus `MaterializedBenchmarkContext`
- `claude_code`: uses only `BenchmarkContext`; it is expected to inspect raw files itself

This split is intentional:
- one-shot methods get precomputed structured evidence
- tool-using methods are expected to gather their own evidence from raw files

## Shared Profiles And Structured Evidence

Structured profiles live in `agent/profiles/`.

Current profilers include:
- schema
- missingness
- numeric
- boolean-like
- categorical
- join quality
- target distribution
- datetime helpers
- inferred roles

Current shared summary shape:
- primary train profile
- one section per train/lookup table
- optional join coverage summary
- target distribution summary

The methods do not all consume the same profiler outputs in the same way:
- `rule_based` uses structured profile dicts directly
- `single_llm` gets a rendered textual summary of the structured profiles
- `claude_code` does not get a precomputed summary by default

## Shared Prompt Framing

LLM-based methods share the common scaffold from [prompts/shared.py](/agent/prompts/shared.py).

The shared framing explicitly says:
- this is a constrained action-selection task
- not an open-ended pipeline design task
- `predicted_add_action_ids` means add actions not already active
- `predicted_remove_action_ids` means remove actions that are already active and harmful
- methods should prefer a small, high-confidence repair set

Method-specific prompt files:
- [prompts/single_llm.py](/agent/prompts/single_llm.py)
- [prompts/claude_code.py](/agent/prompts/claude_code.py)

## Shared Validation And Provenance

[prediction_validation.py](/agent/prediction_validation.py) handles:
- JSON parsing with a fallback that extracts the outermost object
- unknown ID removal
- duplicate removal
- add/remove conflict cleanup
- optional restriction that remove actions must come from the active testcase context

[output_artifacts.py](/agent/output_artifacts.py) writes:
- output JSON
- metadata JSON
- markdown trace
- optional prompt/raw-stream artifacts

This means all methods emit the same top-level benchmark output shape even if their internal execution differs.

## Running Multiple Experiments

[run_matrix.py](/agent/run_matrix.py) provides a simple experiment-plan helper:
- `build_run_plan(...)`
- `execute_run_plan(...)`

[build_paper_tables.py](/agent/build_paper_tables.py) is the current paper-table helper on top of aggregated results.

## Tests

All agent-side tests live in `agent/tests/`.

Main test groups:
- shared infrastructure:
  - task bundle
  - action bank
  - data access
  - context builder
  - summaries
  - prediction validation
  - output artifacts
  - tool registry
- method runners:
  - rule-based
  - single-LLM
  - Claude Code
- LLM-specific support:
  - auth
  - client
  - prompt construction
  - telemetry-related behavior

Common test command:

```bash
python3 -m unittest discover -s agent/tests -p 'test_*.py'
```

## Extending This Directory

If a future method is added, the current intended layering is:

1. Reuse `task_bundle.py`, `action_bank.py`, and `context_builder.py`.
2. Reuse `prediction_validation.py` and `output_artifacts.py`.
3. Add a new method directory under `agent/`.
4. Keep method-specific logic inside that directory.
5. Add dedicated tests under `agent/tests/`.

The important invariant is that method behavior may differ, but the visible action contract and final benchmark output contract should remain the same.

## For Future Agent Implementers

If a future contributor is implementing a new agent loop, the expected split is:

- keep the agent loop itself method-specific
- reuse the shared benchmark plumbing from `agent/`
- keep final prediction validation and artifact writing on the shared path

In practice, a new agent should usually reuse:
- [task_bundle.py](/agent/task_bundle.py)
- [action_bank.py](/agent/action_bank.py)
- [context_builder.py](/agent/context_builder.py)
- [prediction_validation.py](/agent/prediction_validation.py)
- [output_artifacts.py](/agent/output_artifacts.py)

Rules of thumb:
- use `build_benchmark_context(...)` for any method that should see the benchmark/task/testcase/action-bank contract
- use `materialize_benchmark_context(...)` only for methods that are intentionally given precomputed structured evidence
- do not use `materialize_benchmark_context(...)` for methods that are supposed to inspect raw dataset files themselves
- always run final model output through `parse_and_validate_prediction_text(...)` before writing artifacts

Benchmark-specific tool guidance:
- if a future benchmark-aware agent needs benchmark-specific tools, implement them on top of the same shared backend used by `rule_based`
- in practice, that means reusing or extending the shared profile/data-access/context modules rather than reimplementing dataset statistics or action interpretation inside a new agent loop
- the goal is that benchmark-specific evidence helpers live in shared code and can be consumed by multiple methods, instead of each agent maintaining its own private version

Concretely:
- shared benchmark-specific logic should usually live near:
  - [data_access.py](/agent/data_access.py)
  - [profiles/](/agent/profiles)
  - [context_builder.py](/agent/context_builder.py)
  - [rule_based/predicates.py](/agent/rule_based/predicates.py)
- method-specific orchestration should stay inside the new method directory

The intended boundary is:
- shared code provides benchmark interpretation, dataset evidence, validation, and artifact writing
- each method provides its own reasoning loop, prompting strategy, and tool-calling behavior
