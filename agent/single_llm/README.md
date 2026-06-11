# Single LLM Method

This directory contains the one-shot Anthropic baseline.

Plain-English task framing:
- the benchmark gives a current preprocessing pipeline state and a fixed candidate action bank
- the method must return two lists of action IDs:
  - actions to add
  - actions to remove from the currently active context
- `single_llm` does this in one model call after the runner has already prepared a structured summary of the dataset

Entry point:
- [runner.py](/agent/single_llm/runner.py)

Main supporting files:
- [request_context.py](/agent/single_llm/request_context.py)
- [execution.py](/agent/single_llm/execution.py)
- [parsing.py](/agent/single_llm/parsing.py)
- [output.py](/agent/single_llm/output.py)

Shared LLM support:
- [agent/llm/client.py](/agent/llm/client.py)
- [agent/llm/anthropic_client.py](/agent/llm/anthropic_client.py)
- [agent/llm/telemetry.py](/agent/llm/telemetry.py)

## What It Is

`single_llm` is a one-shot prompt baseline.

It does not:
- call tools interactively
- inspect raw files during the model run
- iterate over candidate actions with multiple internal turns

It does:
- locally materialize benchmark evidence before the call
- render that evidence into a prompt
- make one model call per attempt
- parse and validate the returned add/remove prediction

At a glance compared with the other methods:
- evidence source: precomputed structured summary
- model use: one Anthropic call per attempt
- tool use: none
- decision style: semantic one-shot prediction over visible candidate actions

## Execution Flow

`run_single_llm(...)` in [runner.py](/agent/single_llm/runner.py) does the following:

1. Builds a request context with prompt parts and model settings.
2. Loads an API key and builds an Anthropic caller if a custom call function was not injected.
3. Executes one-shot inference through `run_single_llm_execution(...)`.
4. Parses and validates the model output.
5. Writes output, metadata, trace, and prompt artifacts.

## What Information The Model Gets

The model sees:
- the shared task framing from [agent/prompts/shared.py](/agent/prompts/shared.py)
- the single-LLM method instruction from [agent/prompts/single_llm.py](/agent/prompts/single_llm.py)
- a rendered dataset summary
- the testcase context summary
- the full visible action bank
- an explicit JSON-only output contract

Like the other methods, candidate actions are restricted to:
- `action_id`
- `action_type`
- `canonical_params`

## How Its Dataset Evidence Is Prepared

This method intentionally gets precomputed structured evidence.

`build_single_llm_request_context(...)`:
- builds `BenchmarkContext`
- materializes structured table profiles from the referenced train and lookup tables
- reuses the shared on-disk profile cache when the dataset files and visible actions match
- computes per-table structured profiles and a `primary_train_profile`
- attempts one optional join profile using visible `JOIN_LOOKUP` metadata, with `primary_key` fallback when a lookup table is available
- renders a compact textual summary from the cached structured profiles

The dataset summary currently includes:
- primary train schema/missingness/numeric/boolean-like profiles for action-referenced columns
- per-table schema/missingness/numeric/boolean-like profiles when those tables are referenced by visible actions
- optional join profile
- target profile
- target column
- primary key when present
- sampling metadata when a large table was summarized from a deterministic uniform sample

The underlying structured profiles are shared with `rule_based` through the same cache. `single_llm` reads those cached profiles and renders them into prompt text instead of recomputing CSV summaries on every attempt.

## Prompt Construction

Prompt construction happens in [request_context.py](/agent/single_llm/request_context.py).

The prompt is split into:
- `static_prompt`
- `dynamic_prompt`
- `full_prompt`

Plain-English mapping:
- `static_prompt` = the stable part of the request: task framing, method instruction, dataset summary, candidate actions, and output contract
- `dynamic_prompt` = the testcase-specific part: the current active context for this testcase
- `full_prompt` = the combined version preserved in provenance for inspection

Current Anthropic usage:
- `static_prompt` is sent in `system_blocks`
- `dynamic_prompt` is sent as the user message content
- `full_prompt` is preserved in provenance for inspection

If caching is enabled, the static prompt block gets cache-control metadata.

## Recommended Parallel Execution

For repeated runs on the same task, the cheapest and fastest operating mode is:
- keep dataset/profile caching enabled so the first run materializes structured profiles once and later runs reuse the on-disk cache instead of rescanning CSVs
- keep prompt caching enabled so the stable `static_prompt` block is reused across attempts for the same task
- start parallel lanes with a 2-minute stagger measured from the previous lane's first LLM API call, not from process start
- keep execution task-major so one task finishes before moving to the next task

Why this is the recommended pattern:
- the shared profile cache removes most local dataset-loading latency after the first run for a task
- prompt caching only applies to the stable `static_prompt` prefix, and that prefix is identical across tries and testcases for the same task
- a 2-minute stagger is short enough to stay inside the default 5-minute prompt-cache TTL while still reducing token-per-minute spikes that can trigger rate limits
- task-major ordering maximizes prompt-cache reuse; switching tasks too often replaces the cached prefix with a different one

Operationally, this means:
- warm the dataset/profile cache with the first run of a task
- once the first lane has reached its first model call, start the next lane 2 minutes later even if the earlier lane is still running
- continue using the same 2-minute first-call stagger for later lanes of that task
- move to the next task only after the current task's scheduled runs are done

## Reasoning And Generation Controls

Current defaults come from [agent/llm/config.py](/agent/llm/config.py).

The runner supports:
- reasoning-enabled requests
- thinking type and display controls
- effort level
- temperature
- timeout
- max tokens
- prompt caching
- cost cap enforcement

When reasoning is enabled, request temperature is forced to `1.0` in the current implementation.

## Call And Retry Behavior

`run_single_llm_execution(...)` in [execution.py](/agent/single_llm/execution.py):
- calls the provider once per attempt
- estimates cost from token usage and cache usage
- parses the returned text
- validates the resulting payload against visible action ids
- records a trace entry for each attempt

Failure modes handled here:
- JSON parse failure
- payload validation failure
- cost-cap exceeded after a successful parse

If all attempts fail to parse/validate, the method raises an error instead of silently fabricating a prediction.

## Output Validation

Validation is shared with the rest of the agent stack through [agent/prediction_validation.py](/agent/prediction_validation.py).

That layer handles:
- extraction of the JSON object from wrapped output
- unknown ID removal
- duplicate cleanup
- add/remove conflict cleanup
- optional notes/action-rationales normalization

## Provenance

This method writes:
- output JSON
- metadata JSON
- markdown trace
- prompt artifact

Trace content includes:
- prompt/response attempt records
- token usage
- estimated cost
- parsed prediction
- validation warnings
- optional thinking summaries when exposed by the provider

## Strengths

- simple baseline with minimal orchestration
- shares the same structured evidence families as `rule_based`
- easy to compare against tool-using methods
- predictable artifact shape and parsing path

## Limitations

- no tool use
- no incremental evidence gathering
- no selective follow-up on ambiguous columns
- can still overpredict because all decisions happen in one response
- depends on local precomputation quality of the materialized dataset summary

## Tests

Primary tests:
- [test_single_llm_runner.py](/agent/tests/test_single_llm_runner.py)
- [test_llm_client.py](/agent/tests/test_llm_client.py)
- [test_llm_core.py](/agent/tests/test_llm_core.py)
- [test_prompts.py](/agent/tests/test_prompts.py)
- [test_context_builder.py](/agent/tests/test_context_builder.py)
- [test_prediction_validation.py](/agent/tests/test_prediction_validation.py)

These cover:
- prompt construction
- request context shape
- validation behavior
- runner output contract
- LLM caller integration seams
