# Method Implementation Review

This document summarizes how each baseline method is actually implemented today in this worktree.

Scope:
- branch: `codex/zillow-agent-baselines`
- task bundle source of truth: current `data/tasks/zillow-prize-1`
- focus: implementation behavior, not intended paper description

## Shared Contract

All three methods share the same broad benchmark contract:

- they read `task.json`, `testcases/<testcase_id>.json`, and `candidate_actions.json` through `load_task_bundle(...)` in `agent/task_bundle.py`
- they write benchmark-compatible output JSON plus provenance artifacts through `write_output_bundle(...)` in `agent/output_artifacts.py`
- they use the same agent-visible action policy from `agent/action_bank.py`

### Agent-Visible Action Policy

Only these fields are exposed to any method as candidate-action content:

- `action_id`
- `action_type`
- `canonical_params`

This is enforced by:
- `ALLOWED_AGENT_ACTION_FIELDS` in `agent/action_bank.py`
- `build_agent_visible_actions(...)`
- `build_agent_visible_action_bank(...)`

Important caveat:
- `build_agent_visible_action_bank(..., stage_scope=...)` currently ignores `stage_scope`
- this means methods see the full action bank, just reduced to the three visible fields
- `eval_stage`, `role`, `difficulty`, `reasoning`, provenance fields, and hidden scoring metadata are not exposed

### Dataset Access

Dataset access is resolved by `resolve_dataset_paths(data_root, task)` in `agent/data_access.py`.

Current behavior:
- expected train and lookup files come from `task["dataset"]["train_files"]` and `task["dataset"]["lookup_files"]`
- missing files raise `FileNotFoundError`
- `load_csv_rows(...)` loads full CSVs into memory and also supports `.csv.zip`
- `inspect_csv_table(...)` scans row/column shape before loading
- large tables switch to deterministic uniform sampling before profile construction
- `load_joined_training_view(...)` still exists as a helper for explicit join materialization, but shared context building no longer depends on it
- resolved join columns may come from visible `JOIN_LOOKUP` metadata and can use distinct left/right keys or composite keys

### Prompt Scaffold For LLM-Based Methods

`single_llm` and `claude_code` both use the shared scaffold from `agent/prompts/shared.py`:

1. `[TASK]`
2. `[Method-specific instruction]`
3. `[Dataset summary]`
4. `[Current context (testcase)]`
5. `[Candidate actions]`
6. `[Output format]`

The shared task block now explicitly says:
- this is a constrained action-selection repair task
- not an open-ended pipeline design task
- `predicted_add_action_ids` means actions not currently active but should be added
- `predicted_remove_action_ids` means actions currently active and harmful
- actions should not be added just because they are generally useful
- if `context_action_ids` is empty, remove should normally be empty

## Rule-Based

### Entry Point

- `run_rule_based(...)` in `agent/rule_based/runner.py`

There is no separate CLI wrapper. Batch execution is handled externally by `agent/run_matrix.py`.

### Inputs It Reads

`rule_based` reads:
- task bundle via `load_task_bundle(...)`
- visible actions via `build_agent_visible_action_bank(...)`
- all referenced train/lookup CSVs via `load_csv_rows(...)`
- an optional join summary via visible `JOIN_LOOKUP` metadata and `profile_join_key(...)`

### Profilers Actually Used

The runner builds `dataset_insights` with:

- `profile_table_schema(...)`
- `profile_missingness(...)`
- `profile_numeric_columns(...)`
- `profile_boolean_like_columns(...)`
- `profile_join_key(...)`
- `profile_target_distribution(...)`

Not currently wired into `rule_based` even though present in repo:
- categorical profiler
- datetime profiler
- inferred column roles helper

### Decision Flow

`predict_actions(...)` in `agent/rule_based/policy.py` does one pass over the visible action list.

Logic:
- if `action_id` is not in `context_action_ids`, treat as add candidate
- if `action_id` is in `context_action_ids`, treat as remove candidate
- no search, ranking, beam, or retries
- every action produces a `decision_log` record

### Add Heuristics

Implemented in `agent/rule_based/scorers.py`.

Current add families:
- `JOIN_LOOKUP`
  - add if `how in {"left", "inner"}` and left key coverage >= threshold
- `PARSE_DATETIME`
  - add if at least one referenced column is `datetime_like`
- `IMPUTE_MISSING(strategy="median")`
  - add if any referenced column has missing rate >= threshold
- `IMPUTE_MISSING(strategy="constant")`
  - add for boolean-like `FALSE` fills or sparse nonnegative numeric `0` fills
- `CREATE_MISSING_INDICATOR`
  - add when missingness is in a midrange band
- `DROP_HIGH_NULL_COLUMNS`
  - add when all listed columns exceed the null threshold
- `DATE_PART_FEATURE`, `CYCLICAL_ENCODE`, `TIME_SINCE_REFERENCE`
  - add when the referenced columns are datetime-like
- `ENCODE_CATEGORICAL`
  - add using cardinality bands for `onehot`, `label`, or `count`
- `CLIP_OUTLIERS`
  - add when min/max exceed IQR-based bounds
- `DROP_COLUMNS`
  - add if any listed column is target, primary key, identifier-like, or datetime-like

### Remove Heuristics

Current remove families:
- `JOIN_LOOKUP`
  - remove if `how` is not `left` or `inner`
  - also remove `inner` joins when join coverage falls below the generic join threshold
- `PARSE_DATETIME`
  - remove if referenced columns are not actually `datetime_like`
- `DATE_PART_FEATURE`, `CYCLICAL_ENCODE`, `TIME_SINCE_REFERENCE`
  - remove if their referenced source columns are not `datetime_like`
- `IMPUTE_MISSING(strategy="median")`
  - remove if applied to non-numeric, identifier-like, or datetime-like columns
- `IMPUTE_MISSING(strategy="constant")`
  - remove `FALSE` fills on non-boolean-like columns
  - remove `0` fills on columns that are not sparse nonnegative numeric columns with meaningful missingness
- `CREATE_MISSING_INDICATOR`
  - remove if missingness is too low or so high that the indicator is nearly constant
- `DROP_HIGH_NULL_COLUMNS`
  - remove if listed columns do not actually exceed the configured null threshold
- `ENCODE_CATEGORICAL`
  - remove if encoding is applied to identifier-like or datetime-like columns
  - also remove if the selected method does not match the columns' cardinality band
- `CLIP_OUTLIERS`
  - remove if columns are not numeric-like
  - also remove when the current numeric profile does not show IQR-based outlier evidence
- `DROP_COLUMNS`
  - remove if it targets the target, primary key, identifier-like, or datetime-like columns
- `FILTER_ROWS`
  - remove if the predicate contains a numeric range narrower than half the IQR of a referenced numeric column

Important caveat:
- `FILTER_ROWS` removal is based on regex-parsed numeric literals, not a real predicate parser
- most remove rules are still local consistency checks against the current dataset profile, not higher-order semantic reasoning about action interactions

### Outputs And Trace

Artifacts:
- output JSON
- metadata JSON
- trace markdown

Metadata is hardcoded to:
- `status=success`
- `api_call_count=0`
- `tool_call_count=0`
- `cost_usd=0.0`

Trace content:
- join coverage / target / primary key summary, with `primary_key` potentially `None`
- final add/remove predictions
- per-action decision records with:
  - action type
  - add/remove side
  - selected/skipped
  - triggered rule
  - rule-specific details

### Practical Caveats

- deterministic, cheap, and easy to inspect
- add coverage is broader than remove coverage, but remove now covers more obvious type/threshold/cardinality mismatches than before
- threshold-driven and hand-tuned
- larger tables now use deterministic uniform sampling, so some profile evidence is approximate
- ignores `stage_scope`
- no internal self-evaluation

## Single LLM

### Entry Point

- `run_single_llm(...)` in `agent/single_llm/runner.py`

This is a one-shot Python runner, not a CLI wrapper.

### What The Model Sees

The model sees:
- shared task framing from `agent/prompts/shared.py`
- method-specific instruction from `agent/prompts/single_llm.py`
- rendered dataset summary from `agent/summaries.py`
- testcase summary with `context_action_ids`
- full visible action bank rendered as JSON
- strict output-format instruction

The model does not see:
- raw CSV rows
- hidden action-bank metadata
- any field beyond `action_id`, `action_type`, `canonical_params`

### Local Preprocessing Before The Call

Before calling the model, the runner locally loads:
- all referenced train/lookup CSVs
- one optional joined training view when a raw-table join can be resolved

It computes:
- per-table schema/missingness/numeric/boolean-like profiles
- combined schema/missingness/numeric/boolean-like profiles
- join profile
- target profile

These become text inside the dataset summary.

### Prompt Construction

The prompt is split into:
- `static_prompt`
- `dynamic_prompt`
- `full_prompt`

Current use:
- `static_prompt` goes into Anthropic `system` blocks
- `dynamic_prompt` goes into the user message content
- `full_prompt` is also preserved in provenance for inspection

### Anthropic / LLM Layer

`single_llm` uses the shared HTTP client in `agent/llm/anthropic_client.py`.

Current default config:
- model: `claude-sonnet-4-6`
- reasoning enabled: yes
- thinking type: `adaptive`
- thinking display: `summarized`
- reasoning effort: `medium`
- cache enabled: yes
- cache type: `ephemeral`
- cache TTL: `5m`
- request timeout: `120s`
- run cost cap: `$1.00`

Important runtime behavior:
- when reasoning is enabled, request temperature is forced to `1.0`
- the static prompt block gets `cache_control`
- token usage includes cache read/write fields when Anthropic returns them

### Parsing And Validation

The raw response is parsed by:
- exact `json.loads(...)`
- if that fails, fallback to the substring from first `{` to last `}`

Validation then:
- requires both add and remove lists
- drops unknown IDs
- drops non-string entries
- deduplicates IDs
- removes add/remove conflicts from both sides
- keeps optional `notes`
- keeps optional `action_rationales` if structurally valid

Retries:
- only on parse or validation failure
- default `max_attempts=1`

### Outputs And Trace

Artifacts:
- output JSON
- metadata JSON
- trace markdown
- prompt markdown

Trace includes per attempt:
- status
- cost
- token counts
- parsed prediction summary
- validation warnings
- thinking summary
- cache usage
- full prompt text
- raw response text

Metadata includes:
- `model_name`
- `api_provider="anthropic"`
- `api_call_count`
- `tool_call_count=0`
- cumulative `cost_usd`
- cache usage from the last response
- reasoning settings
- error message if any

### Practical Caveats

- model never sees raw rows, only summaries
- `token_usage` in output JSON is from the last successful response, not cumulative retries
- `cost_usd` in metadata is cumulative across attempts
- still ignores `stage_scope` because the visible action bank helper ignores it
- one-shot baseline despite local profiling and rich telemetry

## Claude Code

### Entry Point

- `run_claude_code(...)` in `agent/claude_code/runner.py`

This is a CLI wrapper around the installed `claude` binary, not a Python Messages API call.

### Workspace Packaging

Before launch, the runner creates a temp workspace and writes:
- `TASK.md`
- `dataset_summary.json`
- `testcase.json`
- `candidate_actions_visible.json`
- `output_schema.json`
- `PROMPT.md`

It also creates:
- `dataset -> <actual data root>` symlink

And passes both:
- `--add-dir=<workdir>`
- `--add-dir=<dataset_root>`

to the Claude CLI.

### Prompt Construction

Method-specific prompt builder:
- `agent/prompts/claude_code.py`

Current instruction says Claude Code may:
- inspect workspace files
- inspect raw dataset files exposed in `dataset/`
- write final benchmark JSON to `prediction.json`

The prompt still uses the same shared benchmark framing as `single_llm`.

### Auth, Model, And Thinking

Current default behavior:
- model requested: `claude-sonnet-4-6`
- adaptive thinking requested via env `CLAUDE_CODE_EFFORT_LEVEL=auto`
- no fixed `--max-thinking-tokens` unless explicitly overridden
- `MAX_THINKING_TOKENS` and `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` are removed from env

Auth mode today:
- file-based API key
- `ANTHROPIC_API_KEY` injected into env
- private `.claude-home` under temp workdir

So this is:
- API-key mode
- not subscription-login mode

### Actual Command Invocation

The runner calls `claude` with:
- `--print`
- `--verbose`
- `--output-format stream-json`
- `--include-partial-messages`
- `--model claude-sonnet-4-6`
- `--permission-mode bypassPermissions`
- `--add-dir=<workdir>`
- `--add-dir=<dataset_root>`
- optional `--max-thinking-tokens ...`
- final positional prompt text

This uses `bypassPermissions` because headless `--print` runs with `auto`
were observed to initialize as effective `default` permission mode instead.

Baseline auth contract:
- `claude_code` baseline runs are expected to use `subscription`
- `api_key` mode is blocked by default and requires an explicit code-level override plus `CLAUDE_CODE_ALLOW_API_KEY=1`

### Stream Parsing And Provenance

The runner captures raw `stream-json` stdout and parses it line-by-line.

It extracts:
- raw event counts
- tool calls
- thinking text
- assistant text messages
- final `result` payload
- usage detail
- model usage
- permission denials

Artifacts:
- output JSON
- metadata JSON
- trace markdown
- prompt markdown
- raw stream JSONL

Trace includes:
- command
- raw event counts
- tool calls
- thinking
- assistant messages
- final result
- stderr

### Dataset Use In Practice

Unlike `single_llm`, Claude Code may actually inspect the raw dataset at runtime because:
- the prompt allows it
- the dataset root is exposed in the workspace and via `--add-dir`

Observed behavior in live runs:
- it may use `Task`/Explore subagents
- those subagents may call `Bash`, `Glob`, `Read`, etc. on the local dataset directory (e.g. `<download-root>/zillow-prize-1`)
- it has read file lists, sample rows, headers, row counts, and date values in recent `tc1` runs

So Claude Code is:
- summary-driven by default from the prompt
- but additionally capable of raw dataset inspection if it decides that helps

### Output Validation Behavior

Important caveat:
- once `prediction.json` exists and parses, the runner trusts it
- it does not semantically validate IDs or enforce remove ⊆ context itself

That means benchmark correctness is mostly enforced downstream by the evaluator, not by the runner.

### Practical Caveats

- internal model routing may include other Claude submodels even when `--model claude-sonnet-4-6` is requested
- `token_usage` in the output JSON only stores input/output/total, while cache/model-routing detail lives in metadata
- `tool_call_count` counts top-level tool-use events seen in the stream, not necessarily every nested subagent step in a human-friendly way
- if `prediction.json` is missing, the temp workspace is preserved for debugging
- because dataset inspection is allowed, prompt wording matters a lot: weak benchmark framing led to severe overprediction in earlier runs

## Cross-Method Differences

### Rule-Based vs Single LLM

- both build local dataset profiles first
- `rule_based` uses those profiles directly in heuristics
- `single_llm` converts those profiles into text and lets the model choose

### Single LLM vs Claude Code

- both use the shared prompt scaffold
- `single_llm` is strictly one-shot and tool-free from the model’s perspective
- `claude_code` is agentic and may inspect files or raw dataset contents before writing `prediction.json`

### Why Claude Code Behaves Differently

Because it can:
- inspect workspace files
- inspect raw dataset files
- spawn `Task` subagents
- run shell commands through the Claude Code tool layer

it is much more sensitive to prompt framing than `single_llm`. If the prompt sounds like “design a good pipeline,” it tends to expand; if the prompt emphasizes constrained repair semantics, it behaves more conservatively.

## Main Review Risks To Keep In Mind

- `stage_scope` is effectively ignored by all methods at candidate-bank construction time
- `rule_based` and `single_llm` now inspect tables first and fall back to sampled summaries on larger tables
- `claude_code` trusts `prediction.json` structurally rather than semantically
- `single_llm` and `claude_code` use different execution substrates even though they share much of the prompt scaffold
- prompt wording strongly affects whether `claude_code` behaves like a conservative repair agent or an open-ended feature engineer
