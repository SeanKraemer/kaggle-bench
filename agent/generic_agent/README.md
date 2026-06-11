# Generic Agent Method

`generic_agent` is the tool-generic agent baseline for preprocessing diagnosis
and repair.

Status: this directory contains the Step 1 vertical-slice implementation:
request context, workspace packaging, generic tools, runner, and tests. Shared
model/tool loop behavior lives in `agent/agentic_core/`.

Plain-English task framing:

- the benchmark gives a current preprocessing pipeline state and a fixed
  candidate action bank
- the method must return two lists of action IDs:
  - actions to add
  - active context actions to remove
- `generic_agent` must make that decision with generic tools only
- it should inspect raw workspace files and maintain its own scratchpad, but it
  should not call benchmark-specific profiling or action-lookup APIs

## What It Is

`generic_agent` is a benchmark-aware but tool-generic repair agent.

It is benchmark-aware because the runner still controls:

- task/testcase/action-bank loading
- visible action-bank restriction
- workspace packaging
- final prediction validation
- output and provenance writing

It is tool-generic because the model should only receive broad tools such as:

- shell command execution
- Python execution
- scratchpad read/write

It should not receive curated benchmark tools such as:

- action-family lookup
- action-column lookup
- schema/missingness/numeric/join/target profilers
- context-action summarization helpers
- direct access to `agent/tool_registry.py`

This makes `generic_agent` the main comparison point for measuring whether the
specific tools in `proposed_agent` improve accuracy, cost, or trace quality.

## Intended Layout

Method files:

```text
agent/generic_agent/
  README.md
  __init__.py
  runner.py
  request_context.py
  workspace.py
  tools.py
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
agent/prompts/generic_agent.py
```

Existing shared modules this method should reuse:

- `agent/task_bundle.py`
- `agent/action_bank.py`
- `agent/context_builder.py`
- `agent/prediction_validation.py`
- `agent/output_artifacts.py`
- `agent/prompts/shared.py`
- `agent/llm/`

## Tool Boundary

The key invariant is that `generic_agent` has no benchmark-specific tool
advantage over a normal general-purpose data agent.

Allowed model-visible tools:

- `bash`: inspect files, run simple commands, and execute local scripts inside
  the prepared workspace
- `python`: analyze CSV files and candidate-action JSON using standard Python
  and installed libraries
- `scratchpad.read`: retrieve durable notes from the current run
- `scratchpad.write`: store intermediate observations and candidate decisions

Disallowed model-visible tools:

- `load_task_bundle`
- `build_agent_visible_action_bank`
- `load_joined_training_view`
- `profile_table_schema`
- `profile_missingness`
- `profile_numeric_columns`
- `profile_boolean_like_columns`
- `profile_join_key`
- `profile_target_distribution`
- proposed-agent action lookup wrappers

The runner may use shared benchmark code before and after the model run. That is
not a model-visible advantage; it is how every method gets the same benchmark
contract and final validation.

To preserve the boundary, the generic workspace should avoid exposing the full
repo as an importable Python package. The model should inspect packaged task
files and raw dataset files, not import `agent.profiles` or
`agent.tool_registry` from inside the tool loop.

## Execution Environment

`generic_agent` should run inside a prepared workspace because its model-visible
tools are broad. Bash and Python can inspect many things if the current working
directory is not controlled, so the runner should package only the benchmark
materials the generic baseline is allowed to see.

The workspace is part of the method definition:

- it exposes raw task files and raw dataset files
- it provides a writable place for scratchpad and final prediction artifacts
- it prevents accidental access to benchmark-specific helper modules
- it makes generic exploration reproducible across runs

### Workspace Layout

The `prepare_generic_workspace(...)` helper creates a temporary workspace
containing:

```text
dataset/
TASK.md
testcase.json
candidate_actions_visible.json
output_schema.json
PROMPT.md
scratchpad.json
prediction.json
```

The workspace should expose enough information for a general agent to solve the
benchmark task:

- raw dataset files under `dataset/`
- rendered task guidance
- testcase context
- visible candidate action bank
- required output schema
- writable final `prediction.json`
- writable scratchpad

The visible candidate action bank must contain only:

- `action_id`
- `action_type`
- `canonical_params`

The generic agent must never see hidden labels, gold actions, or private action
metadata.

### Runtime Access

Inside this workspace, the shared `agentic_core` loop should expose only the
generic tool allowlist:

- bash commands scoped to the prepared workspace and dataset directory
- Python execution scoped to the prepared workspace and dataset directory
- scratchpad read/write

The runner may still use shared benchmark code outside the model-visible loop to
package inputs and validate outputs. That code path should not be callable by
the model through bash or Python.

## Execution Flow

The `run_generic_agent(...)` entry point:

1. Build a lightweight `BenchmarkContext` through `agent/context_builder.py`.
2. Prepare a temporary generic workspace.
3. Build the generic-agent prompt from shared benchmark guidance and generic
   method instructions.
4. Register only generic tools through `agentic_core`.
5. Run the bounded agent loop.
6. Require a final JSON prediction from the model response or `prediction.json`.
7. Parse and validate the prediction through `agent/prediction_validation.py`.
8. Write standardized output and provenance artifacts through
   `agent/output_artifacts.py`.

High-level flow:

```text
benchmark context
        |
        v
generic workspace
        |
        v
shared agentic loop
        |
        +--> bash / python
        +--> scratchpad
        |
        v
prediction JSON
        |
        v
shared validation and artifacts
```

## Small Runner Usage

The runner entry point is `run_generic_agent(...)` in `agent/generic_agent/runner.py`.

Minimal usage with a mocked model response:

```python
from pathlib import Path

from agent.generic_agent.runner import run_generic_agent


result = run_generic_agent(
    task_dir=Path("data/tasks/zillow-prize-1"),
    testcase_id="tc1_from_scratch",
    run_id="try1",
    data_root=Path("/path/to/raw/zillow-prize-1"),
    llm_call=lambda **_: {
        "raw_text": (
            '{"predicted_add_action_ids":["CA-000107"],'
            '"predicted_remove_action_ids":[]}'
        ),
        "input_tokens": 10,
        "output_tokens": 5,
    },
    reasoning_enabled=False,
)

print(result["output_path"])
```

In this mocked form, no Claude or Anthropic API key is needed because the caller
injects `llm_call` and returns the same response shape that the Anthropic client
would normally return.

Usage with the real Anthropic client:

```python
from pathlib import Path

from agent.generic_agent.runner import run_generic_agent


result = run_generic_agent(
    task_dir=Path("data/tasks/zillow-prize-1"),
    testcase_id="tc1_from_scratch",
    run_id="try1",
    data_root=Path("/path/to/raw/zillow-prize-1"),
    api_key_path=Path("agent/api_key.txt"),
)

print(result["output_path"])
```

For a real run, `api_key_path` must point to a readable Anthropic API key file
unless the caller passes a custom `llm_call`. Unit tests use injected mock calls
so they can validate runner behavior without network access or credentials.

## Prompt Contract

The prompt should make the benchmark constraints explicit:

- this is constrained action selection, not open-ended pipeline design
- the agent must choose only visible candidate action IDs
- add IDs must be inactive actions
- remove IDs must be active context actions
- generally useful preprocessing is not enough; actions need evidence for this
  testcase
- the final response must be valid JSON or write valid `prediction.json`

The final output contract is:

```json
{
  "predicted_add_action_ids": [],
  "predicted_remove_action_ids": []
}
```

Optional rationales may be stored in trace/provenance, but the benchmark
prediction should keep the same top-level shape as existing methods.

## Provenance

Recommended artifacts:

- output JSON
- metadata JSON
- prompt artifact
- markdown trace
- raw tool-call trace when available
- scratchpad artifact
- copied or preserved workspace path on failure

Trace entries should make generic exploration inspectable:

- commands run
- Python snippets or script names
- compact stdout/stderr summaries
- scratchpad updates
- final prediction source
- validation warnings
- token and cost metadata

## Strengths

- closest to a general-purpose data agent baseline
- useful comparison against `proposed_agent`
- can discover evidence not covered by curated tools
- simple conceptual boundary: generic tools only

## Limitations

- may spend turns rediscovering evidence that specific tools expose directly
- may overpredict if it treats the task like full pipeline design
- less controlled than `proposed_agent`
- harder to compare if the workspace accidentally exposes benchmark-specific
  helper code
- shell/Python behavior can vary by local environment

## Test Plan

Tests cover:

- generic workspace packaging
- generic tool allowlist excludes benchmark-specific tools
- prompt construction mentions generic-only tool access
- mocked model/tool execution through `agentic_core`
- final output parsing and validation
- remove predictions restricted to active context IDs
- provenance artifact generation
- workspace preservation on failed prediction creation
- budget handling for max turns, max tool calls, and timeouts
