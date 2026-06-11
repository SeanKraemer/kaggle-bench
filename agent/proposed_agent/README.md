# Proposed Agent Method

`proposed_agent` is the benchmark-aware, specific-tool agent design for
preprocessing diagnosis and repair.

Status: this directory contains the v1 two-phase implementation: request
context, curated benchmark tools, controller, reconciliation, runner, and
tests. Shared model/tool loop behavior lives in `agent/agentic_core/`.

Plain-English task framing:

- the benchmark gives a current preprocessing pipeline state and a fixed
  candidate action bank
- the method must return two lists of action IDs:
  - actions to add
  - active context actions to remove
- `proposed_agent` runs a fixed controller around the same underlying agent
  loop twice:
  - add mode identifies missing beneficial actions
  - remove mode identifies harmful active actions
- the controller reconciles both phase outputs into one benchmark-compatible
  prediction JSON

## What It Is

`proposed_agent` is a specialized repair agent.

It is not:

- a free-form coding agent
- an end-to-end AutoML generator
- a notebook-writing agent
- a generic data-cleaning assistant that invents arbitrary transformations

It does:

- use the shared benchmark task/testcase/action-bank contract
- reason only over the visible candidate action bank
- use benchmark-specific tools for selective evidence gathering
- keep add-side recovery separate from remove-side rollback
- persist intermediate judgments in a scratchpad
- reconcile phase outputs conservatively
- validate final output through the shared benchmark validator

The core distinction from `generic_agent` is tool access. `generic_agent` must
discover evidence with broad tools such as shell, Python, and scratchpad.
`proposed_agent` gets curated benchmark-specific tools that expose known useful
views of the task, dataset, action bank, and current context.

## Intended Layout

Method files:

```text
agent/proposed_agent/
  README.md
  __init__.py
  runner.py
  controller.py
  request_context.py
  tools.py
  reconciliation.py
```

Shared loop support should live in `agent/agentic_core/` rather than being
copied into this directory:

```text
agent/agentic_core/
  execution.py
  tool_runtime.py
  scratchpad.py
  parsing.py
  trace.py
  types.py
```

Prompt file:

```text
agent/prompts/proposed_agent.py
```

Existing shared modules this method should reuse:

- `agent/task_bundle.py`
- `agent/action_bank.py`
- `agent/context_builder.py`
- `agent/tool_registry.py`
- `agent/prediction_validation.py`
- `agent/output_artifacts.py`
- `agent/prompts/shared.py`
- `agent/llm/`

## Execution Environment

`proposed_agent` should run through an explicit tool runtime rather than a
general filesystem workspace by default. The method is meant to test whether
curated benchmark-specific tools improve repair decisions, so the model-visible
environment should be the tool allowlist, not arbitrary repo access.

The tool runtime is part of the method definition:

- it exposes selected benchmark-specific tools with stable schemas
- it hides private repo internals and gold/evaluation data
- it records every tool call for provenance
- it keeps add-mode and remove-mode evidence gathering bounded
- it makes the specific-tool advantage explicit and auditable

Unlike `generic_agent`, `proposed_agent` does not need a packaged shell/Python
workspace for the cleanest comparison. If a future ablation allows generic
bash/Python in addition to specific tools, that variant should add a controlled
workspace section or config flag rather than silently changing this method's
default environment.

## Execution Flow

The `run_proposed_agent(...)` entry point:

1. Build a shared benchmark context for the task, testcase, visible action
   bank, dataset paths, and output contract.
2. Build a proposed-agent request context with method prompts, phase prompts,
   tool descriptions, model settings, and budget settings.
3. Register benchmark-specific tools through the shared agentic tool runtime.
4. Initialize a scratchpad shared across both phases.
5. Run the agent loop in add mode.
6. Parse and validate the add-mode output.
7. Run the agent loop in remove mode.
8. Parse and validate the remove-mode output.
9. Reconcile both phase outputs into one final add/remove prediction.
10. Run final shared validation and write output/provenance artifacts.

High-level flow:

```text
benchmark context
        |
        v
proposed-agent controller
        |
        +--> shared agentic loop, add mode
        |       +--> benchmark-specific tools
        |       +--> scratchpad
        |
        +--> shared agentic loop, remove mode
        |       +--> benchmark-specific tools
        |       +--> scratchpad
        |
        v
conservative reconciliation
        |
        v
benchmark prediction JSON
```

## Tool Boundary

`proposed_agent` should expose specific benchmark tools, not arbitrary private
access to every repo function.

Existing tools in `agent/tool_registry.py` are the first layer:

- `load_task_bundle`
- `build_agent_visible_action_bank`
- `resolve_dataset_paths`
- `load_csv_rows`
- `load_joined_training_view`
- `profile_table_schema`
- `profile_missingness`
- `profile_numeric_columns`
- `profile_boolean_like_columns`
- `profile_join_key`
- `profile_target_distribution`

Implemented proposed-agent tools:

- `lookup_actions`
- `summarize_context_actions`
- `inspect_dataset_tables`
- `inspect_columns`
- `profile_join_key`
- `profile_target_distribution`
- `preview_rows`
- `scratchpad_read`
- `scratchpad_write`

These wrappers should be thin, deterministic, and backed by shared modules such
as `agent/data_access.py`, `agent/profiles/`, `agent/action_bank.py`, and
`agent/context_builder.py`.

The intended evidence strategy is selective inspection. The agent should not
load every raw column into the prompt. It should call tools only when the
current prompt evidence is insufficient to judge a specific action family,
column, join, target, or active context action.

## Dataset Evidence

`proposed_agent` may receive compact structured evidence up front and then use
tools for follow-up inspection.

The initial context should include:

- task framing and scenario description
- target column and primary key
- current `context_action_ids`
- visible candidate action summary
- compact schema profile
- compact missingness profile
- compact numeric profile
- compact boolean-like profile
- compact join profile when lookup files exist
- compact target profile when the target is available

Current shared context behavior is intentionally limited: materialization uses
the first train file and first lookup file from the task dataset metadata. If a
future task needs multi-file materialization, that should be expanded in shared
context/data-access code rather than inside `proposed_agent`.

## Prompt And Phase Contracts

Prompt construction should combine:

- shared benchmark guidance from `agent/prompts/shared.py`
- proposed-agent method instruction from `agent/prompts/proposed_agent.py`
- testcase-specific dynamic context
- available tool descriptions
- phase-specific instruction
- explicit JSON-only output contract

Add-mode instruction should require:

- only inactive candidate actions may be added
- remove decisions are not allowed in this phase
- action IDs must come from the visible action bank
- the add set should be compact and evidence-backed

Expected add-mode intermediate output:

```json
{
  "phase": "add",
  "predicted_add_action_ids": [],
  "predicted_remove_action_ids": [],
  "action_rationales": []
}
```

Remove-mode instruction should require:

- only currently active `context_action_ids` may be removed
- add decisions are not allowed in this phase
- empty active context normally means empty remove output
- rollback should be precise rather than broad

Expected remove-mode intermediate output:

```json
{
  "phase": "remove",
  "predicted_add_action_ids": [],
  "predicted_remove_action_ids": [],
  "action_rationales": []
}
```

Final reconciled output:

```json
{
  "predicted_add_action_ids": [],
  "predicted_remove_action_ids": []
}
```

## Small Runner Usage

The runner entry point is `run_proposed_agent(...)` in
`agent/proposed_agent/runner.py`.

Minimal usage with mocked add/remove phase responses:

```python
from pathlib import Path

from agent.proposed_agent.runner import run_proposed_agent


responses = iter(
    [
        {
            "raw_text": (
                '{"phase":"add","predicted_add_action_ids":["CA-000107"],'
                '"predicted_remove_action_ids":[]}'
            ),
            "input_tokens": 10,
            "output_tokens": 5,
        },
        {
            "raw_text": (
                '{"phase":"remove","predicted_add_action_ids":[],'
                '"predicted_remove_action_ids":[]}'
            ),
            "input_tokens": 8,
            "output_tokens": 4,
        },
    ]
)

result = run_proposed_agent(
    task_dir=Path("data/tasks/zillow-prize-1"),
    testcase_id="tc1_from_scratch",
    run_id="try1",
    data_root=Path("/path/to/raw/zillow-prize-1"),
    llm_call=lambda **_: next(responses),
    reasoning_enabled=False,
)

print(result["output_path"])
```

In this mocked form, no Claude or Anthropic API key is needed because the caller
injects `llm_call`. Real runs omit `llm_call`, load the configured Anthropic API
key, and use the same `agentic_core` tool loop with the proposed-agent tool
allowlist.

## Validation And Reconciliation

`proposed_agent` should use phase-aware validation before final shared
validation.

Add-mode validation:

- predicted add IDs exist in the visible action bank
- predicted add IDs are not already active
- no remove decisions appear in the add phase
- duplicate IDs are removed

Remove-mode validation:

- predicted remove IDs exist in the visible action bank
- predicted remove IDs are present in `context_action_ids`
- no add decisions appear in the remove phase
- duplicate IDs are removed

Reconciliation rules:

- final add IDs must be inactive candidate actions
- final remove IDs must be active context actions
- no action ID may appear in both final lists
- if an ID appears in both phase outputs, reconciliation keeps the remove
  decision and drops the add decision
- final output must pass `agent/prediction_validation.py`

The controller should fail loudly on malformed output after retries rather than
fabricating a prediction.

## Provenance

The method should write the same top-level benchmark output shape as the other
methods, plus richer agent artifacts.

Recommended artifacts:

- output JSON
- metadata JSON
- markdown trace
- full prompt
- add-mode prompt
- remove-mode prompt
- tool-call JSONL
- scratchpad JSON
- reconciliation notes
- validation warnings
- token and cost metadata

Trace entries should include:

- phase name
- model attempt records
- tool calls and compact tool results
- scratchpad updates
- parsed phase predictions
- reconciliation decisions
- final parsed prediction
- validation warnings

## Strengths

- aligned with the benchmark add/remove repair contract
- separates missing-action recovery from harmful-action rollback
- gives the model targeted evidence APIs instead of broad raw-file wandering
- improves interpretability through phase-level traces
- supports ablations on decomposition, tool access, scratchpad use, and
  reconciliation

## Limitations

- more expensive than `single_llm`
- less general than `generic_agent`
- depends on the quality and coverage of benchmark-specific tools
- can still overpredict if phase prompts are too broad
- final performance may depend heavily on reconciliation policy
- tool failures can cause otherwise valid reasoning to fail

## Test Plan

Tests cover:

- request context construction
- specific tool allowlist construction
- add-mode and remove-mode prompt construction
- mocked model/tool execution through `agentic_core`
- phase-aware validation
- reconciliation behavior
- final output validation against visible and active action IDs
- provenance artifact generation
- retry behavior for malformed phase output
- budget handling for max turns, max tool calls, and cost caps
