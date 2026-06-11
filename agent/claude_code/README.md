# Claude Code Method

This directory contains the Claude Code CLI baseline.

Plain-English task framing:
- the benchmark gives a current preprocessing pipeline state and a fixed candidate action bank
- the method must output which candidate action IDs should be added and which active IDs should be removed
- unlike `single_llm`, this baseline does not receive a precomputed dataset summary; it is expected to inspect raw files and form its own judgment

Entry point:
- [runner.py](./runner.py)

Main support files:
- [command.py](./command.py)
- [workspace.py](./workspace.py)
- [stream.py](./stream.py)
- [trace.py](./trace.py)
- [run_claude_code_campaign.py](./run_claude_code_campaign.py)
- [run_claude_code.sh](./run_claude_code.sh)

## What It Is

`claude_code` is a wrapper around the Claude Code CLI.

It is the most agentic of the current baselines because the model may:
- inspect workspace files
- inspect raw dataset files
- use Claude Code tools during the run
- write the final `prediction.json` itself

It is still bounded by the benchmark contract because the wrapper controls:
- what files are staged into the workspace
- what prompt is provided
- how final output is parsed and validated

## Campaign Runner

`run_claude_code_campaign.py` is an operational batch driver for large rerun campaigns.

Its role is different from `runner.py`:
- `runner.py`
  - executes one `claude_code` benchmark run
- `run_claude_code_campaign.py`
  - executes many runs in fixed order
  - resumes from prior campaign state using a JSONL progress log
  - prioritizes previously failed targets on resume
  - launches up to 4 workers in parallel with 10-second staggering
  - verifies each successful run's output/provenance bundle and `eval.py`
  - runs `validate_artifacts.py` after each completed 4-testcase block
  - stops after the first failed run, but lets already-started peer workers drain before exiting

This file is meant for campaign operations, not for changing the public baseline contract.

Current implementation assumptions:
- `KAGGLE_BENCH_DOWNLOAD_ROOT` points to the directory containing the benchmark task datasets
- `KAGGLE_BENCH_RECRUIT_ZIP_ROOT` may override the Recruit zip directory when it is stored elsewhere
- Sberbank uses a compatibility extraction step from `.csv.zip` files
- `KAGGLE_BENCH_SBERBANK_COMPAT_ROOT` may override the extracted Sberbank compatibility directory
- `KAGGLE_BENCH_CLAUDE_CODE_CAMPAIGN_LOG` may override the JSONL campaign log path
- by default, extracted Sberbank files are staged under `.cache/` and the campaign log is written under `.logs/`

At a glance compared with the other methods:
- evidence source: raw workspace files and raw dataset files
- model use: Claude Code CLI orchestration
- tool use: yes, through Claude Code
- decision style: agentic inspection followed by a final `prediction.json`

## Execution Flow

`run_claude_code(...)` in [runner.py](./runner.py) does the following:

1. Builds a lightweight `BenchmarkContext`.
2. Builds a Claude-Code-specific prompt.
3. Prepares a temporary workspace.
4. Builds the Claude CLI command and environment.
5. Runs the CLI and captures stream-json output.
6. Requires `prediction.json` to exist and requires a zero exit code.
7. Parses and validates the prediction through the shared validator.
8. Writes output, metadata, trace, prompt, and raw stream artifacts.

## What Information It Gets Up Front

Unlike `single_llm`, this method does not receive a precomputed dataset summary.

The prompt explicitly says:
- no precomputed dataset summary is provided
- inspect the raw dataset files under `dataset/`
- use workspace files as needed

So the method starts from:
- task goal
- testcase context summary
- visible candidate action bank
- output schema / prediction target
- raw dataset access

## Temporary Workspace Layout

`prepare_claude_workspace(...)` in [workspace.py](./workspace.py) creates a temp directory containing:
- `dataset/` symlink to the actual dataset root
- `TASK.md`
- `testcase.json`
- `candidate_actions_visible.json`
- `output_schema.json`
- `PROMPT.md`

This means Claude Code can inspect:
- the raw dataset files
- the testcase state
- the visible action bank
- the expected output shape

Minimal expected final output:

```json
{
  "predicted_add_action_ids": ["CA-000107"],
  "predicted_remove_action_ids": ["CA-000108"]
}
```

## Command Construction

`build_claude_command(...)` in [command.py](./command.py) currently runs Claude Code with:
- `--print`
- `--verbose`
- `--output-format stream-json`
- `--include-partial-messages`
- `--model <model_name>`
- `--permission-mode bypassPermissions`
- `--add-dir=<workdir>`
- `--add-dir=<dataset_root>`

Optional:
- `--max-thinking-tokens <n>` when a fixed override is explicitly provided

The raw prompt text is passed as the final argument.

This runner uses `bypassPermissions` because headless `--print` runs with `auto`
were observed to initialize as effective `default` permission mode instead.

## Authentication Modes

This wrapper supports two auth modes:
- `subscription`
- `api_key`

Current default:
- `subscription`

Baseline contract:
- `claude_code` baseline runs must use `subscription`
- `api_key` is blocked unless the caller explicitly sets both `allow_api_key_override=True` and `CLAUDE_CODE_ALLOW_API_KEY=1`

Behavior in [command.py](./command.py):
- `subscription`
  - removes `ANTHROPIC_API_KEY` from the subprocess env
  - preserves the existing logged-in Claude session
- `api_key`
  - uses a temp `HOME`
  - injects `ANTHROPIC_API_KEY`

This keeps subscription-first runs from accidentally falling back to API-key billing.

## Output And Validation

Claude Code itself is expected to create `prediction.json`.

The wrapper does not trust that file blindly.

After the run, it:
- requires a zero exit code
- requires `prediction.json` to exist
- parses the file with [prediction_validation.py](../prediction_validation.py)
- restricts remove predictions to the currently active `context_action_ids`

So even if the model writes malformed or overbroad content, the shared validator still normalizes the final payload.

## Stream Capture And Trace

The CLI is run in `stream-json` mode.

The wrapper stores:
- normalized execution metadata
- raw stream-json output
- tool call counts
- usage details
- model usage
- permission denials

Trace rendering is handled in [trace.py](./trace.py).

Current provenance artifacts include:
- output JSON
- metadata JSON
- markdown trace
- prompt artifact
- raw `.stream.jsonl` event log

This makes Claude Code the most inspectable method in terms of raw execution telemetry.

## How It Differs From Single LLM

`single_llm`:
- gets structured evidence precomputed and summarized
- makes a direct API call
- has no tool use

`claude_code`:
- gets no precomputed dataset summary
- is expected to inspect raw files itself
- runs through the Claude Code CLI
- may use tools internally
- emits raw event streams

So the intended comparison is:
- one-shot reasoning over prepared evidence
vs.
- agentic reasoning that gathers its own evidence from the provided workspace

## Strengths

- closest current baseline to a real coding/data agent
- can inspect raw files instead of relying on pre-rendered summaries
- records richer telemetry than the other methods
- now supports both subscription and API-key auth

## Limitations

- more expensive and slower than the other baselines
- behavior can depend on internal Claude Code orchestration
- the CLI may internally use multiple model variants
- still bounded by the workspace and prompt the wrapper provides
- local accounting fields may not perfectly match billing-page totals

## Tests

Primary tests:
- [test_claude_code_runner.py](../tests/test_claude_code_runner.py)
- [test_prompts.py](../tests/test_prompts.py)
- [test_prediction_validation.py](../tests/test_prediction_validation.py)

These cover:
- workspace preparation
- command/env construction
- auth-mode handling
- prompt construction
- output validation
- runner artifact behavior
