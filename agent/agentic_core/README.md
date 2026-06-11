# Agentic Core

`agentic_core` is the shared runtime for method-specific agent loops.

Status: this directory contains the shared model/tool loop used by
`generic_agent` and `proposed_agent`, plus small helper modules for common
request controls and scratchpad tools.

## Purpose

`agentic_core` should own generic execution mechanics:

- bounded model turns
- tool-call dispatch
- scratchpad persistence
- parse/retry flow
- trace event collection
- token and cost accounting hooks
- timeout and budget enforcement

Method directories should own method policy:

- which tools are exposed
- what prompts are sent
- whether the agent runs once or in phases
- how phase outputs are reconciled
- what extra provenance files are written

This split keeps `generic_agent` and `proposed_agent` comparable while still
allowing them to share the expensive, failure-prone orchestration code.

## Intended Layout

Implemented files:

```text
agent/agentic_core/
  README.md
  __init__.py
  types.py
  execution.py
  tool_runtime.py
  scratchpad.py
  scratchpad_tools.py
  request_controls.py
  parsing.py
  trace.py
```

Suggested responsibilities:

- `types.py`: shared dataclasses for requests, turns, tool calls, budgets,
  parsed outputs, and execution results
- `execution.py`: bounded model/tool loop used by both agent methods
- `tool_runtime.py`: method-supplied tool registry, schema exposure, tool-call
  execution, and tool-result normalization
- `scratchpad.py`: run-local read/write store with size limits
- `scratchpad_tools.py`: shared read/write tool specs backed by `scratchpad.py`
- `request_controls.py`: shared model reasoning/temperature request controls
- `parsing.py`: extraction of final JSON from model responses or files
- `trace.py`: human-readable and JSONL trace rendering helpers

## Runtime Contract

The shared execution function should receive:

- model caller or provider client
- static prompt blocks
- dynamic prompt blocks
- optional phase instruction
- method-owned tool catalog
- scratchpad instance
- budget settings
- parse/validation callback supplied by the method

It should return:

- raw model attempts
- normalized tool-call records
- scratchpad snapshot
- parsed model output when available
- validation warnings or errors
- token/cost metadata when available
- a final success/failure status

`agentic_core` should not know whether a run is "generic" or "proposed" except
through the method name and supplied tool catalog.

## Boundaries

`agentic_core` should not:

- load task bundles directly
- decide which preprocessing actions are good
- know gold labels or evaluation results
- decide the add/remove reconciliation policy
- expose benchmark-specific tools by default
- write final benchmark output files directly

Those responsibilities belong in method directories or existing shared
benchmark modules:

- `agent/task_bundle.py`
- `agent/action_bank.py`
- `agent/context_builder.py`
- `agent/tool_registry.py`
- `agent/prediction_validation.py`
- `agent/output_artifacts.py`

## Tool Runtime Expectations

Tools should be supplied by the method as an explicit allowlist.

`generic_agent` should pass only generic tools:

- bash
- Python
- scratchpad read/write

`proposed_agent` should pass benchmark-specific tools:

- existing profiling/data-access tools from `agent/tool_registry.py`
- proposed action lookup wrappers
- context summarization wrappers
- scratchpad read/write

The runtime should record every tool call with:

- method name
- phase name when present
- tool name
- sanitized input
- compact output or error
- elapsed time
- retry status when relevant

## Failure Policy

The core loop should be strict about bounded execution:

- stop at max turns
- stop at max tool calls
- stop at timeout
- stop when cost cap is exceeded
- retry parse/validation failures only within the method-supplied retry budget
- return a structured failure instead of fabricating predictions

Method code can decide whether a structured failure should raise, write failure
metadata, or preserve a workspace for debugging.

## Test Plan

Tests cover:

- tool allowlist dispatch
- unknown tool rejection
- scratchpad size limits
- max-turn and max-tool-call limits
- parse retry behavior
- validation callback failures
- trace event rendering
- successful mocked execution for a single-pass generic run
- successful mocked execution for add/remove proposed phases
