# Rule-Based Method

This directory contains the deterministic heuristic baseline.

Plain-English task framing:
- the benchmark gives a current preprocessing pipeline state
- some candidate actions are already active
- the method must decide which candidate action IDs should be added and which active ones should be removed
- `rule_based` makes that decision using locally computed dataset statistics and hard-coded heuristics, not an LLM

Entry point:
- [runner.py](/agent/rule_based/runner.py)

Core decision files:
- [policy.py](/agent/rule_based/policy.py)
- [scorers.py](/agent/rule_based/scorers.py)
- [predicates.py](/agent/rule_based/predicates.py)
- [decision_records.py](/agent/rule_based/decision_records.py)
- [thresholds.py](/agent/rule_based/thresholds.py)

## What It Is

`rule_based` is a non-agentic baseline.

It does not:
- call an LLM
- use tools interactively
- search over action sequences
- execute the preprocessing pipeline

It does:
- load the benchmark instance
- materialize local dataset profiles
- scan every visible candidate action once
- decide add/remove/skipped using hard-coded heuristics

At a glance compared with the other methods:
- evidence source: precomputed local profiles
- model use: none
- tool use: none
- decision style: deterministic rules over visible candidate actions

## Execution Flow

`run_rule_based(...)` in [runner.py](/agent/rule_based/runner.py) does the following:

1. Builds a lightweight `BenchmarkContext`.
2. Materializes dataset rows and profiles through `materialize_benchmark_context(...)`.
3. Assembles `dataset_insights`.
4. Calls `predict_actions(...)`.
5. Writes benchmark output, metadata, and a detailed trace.

## Dataset Information It Uses

This baseline uses structured local evidence directly, not via prompt text.

Current `dataset_insights` fields:
- `schema_profile`
- `missingness_profile`
- `numeric_profile`
- `boolean_like_profile`
- `join_profile`
- `target_profile`
- `target_column`
- `primary_key`

These are built from:
- the primary train CSV (`task["dataset"]["train_files"][0]`)
- per-table profiles across all referenced train/lookup CSVs
- an optional join summary when a visible `JOIN_LOOKUP` can be resolved to raw tables

Current join behavior:
- visible `JOIN_LOOKUP` metadata is preferred over `primary_key`
- if no raw-table join can be resolved, the runner falls back to a same-name join on `primary_key` when present and a lookup table exists
- if no join can be resolved at all, `join_profile` remains an empty/zero-coverage summary
- `primary_key` itself is optional in `dataset_insights`

Important contract detail:
- `schema_profile`, `missingness_profile`, `numeric_profile`, and `boolean_like_profile` come from `primary_train_profile`
- lookup-only columns do not enter those core evidence dicts
- lookup tables still matter through `join_profile` and through the rendered dataset summary used by other methods

## Candidate Action Visibility

Like every other method, `rule_based` only sees:
- `action_id`
- `action_type`
- `canonical_params`

It does not receive hidden bank metadata such as:
- `role`
- `eval_stage`
- `difficulty`
- provenance annotations

## Decision Loop

`predict_actions(...)` in [policy.py](/agent/rule_based/policy.py) iterates once over the visible action list.

Per action:
- if the action is not active in `context_action_ids`, it is treated as an add candidate
- if the action is active, it is treated as a remove candidate
- a decision record is produced either way

There is no:
- ranking
- retries
- beam search
- pairwise comparison stage

Simple examples:
- add example:
  - if `context_action_ids` is empty and a `JOIN_LOOKUP` action has acceptable join coverage, `rule_based` may select it into `predicted_add_action_ids`
- remove example:
  - if a currently active `DROP_COLUMNS` action targets the target column, primary key, identifier-like columns, or datetime-like columns, `rule_based` may select it into `predicted_remove_action_ids`

## Add Heuristics

Add-side logic currently covers families such as:
- `JOIN_LOOKUP`
- `PARSE_DATETIME`
- `IMPUTE_MISSING`
- `CREATE_MISSING_INDICATOR`
- `DROP_HIGH_NULL_COLUMNS`
- `DATE_PART_FEATURE`
- `CYCLICAL_ENCODE`
- `TIME_SINCE_REFERENCE`
- `ENCODE_CATEGORICAL`
- `CLIP_OUTLIERS`
- `DROP_COLUMNS`

The exact heuristics are in [scorers.py](/agent/rule_based/scorers.py) and the reusable lower-level checks are in [predicates.py](/agent/rule_based/predicates.py).

In practice, these heuristics are driven by:
- missing-rate thresholds
- numeric outlier evidence
- datetime-like detection
- join coverage
- boolean-like detection
- cardinality bands
- identifier-like / primary-key / target checks

## Remove Heuristics

Remove-side logic covers the same general idea from the opposite direction.

Current removal families include:
- `JOIN_LOOKUP`
- `PARSE_DATETIME`
- `DATE_PART_FEATURE`
- `CYCLICAL_ENCODE`
- `TIME_SINCE_REFERENCE`
- `IMPUTE_MISSING`
- `CREATE_MISSING_INDICATOR`
- `DROP_HIGH_NULL_COLUMNS`
- `ENCODE_CATEGORICAL`
- `CLIP_OUTLIERS`
- `DROP_COLUMNS`
- `FILTER_ROWS`

These remove rules are mostly local consistency checks, for example:
- wrong type for the transformation
- wrong cardinality band for the encoding
- no real outlier evidence for clipping
- null threshold not actually exceeded
- remove candidate not compatible with target/key/datetime protections

## Trace Behavior

This method writes a very explicit markdown trace.

For each action, the trace records:
- action id
- action type
- whether it was considered on add or remove side
- final decision
- triggered rule, if any
- rule-specific detail lines

That trace is intended for post-hoc error analysis, not just final prediction logging.

Typical record shape:

```text
### CA-000107
- Action type: `JOIN_LOOKUP`
- Candidate side: `add`
- Decision: `selected_add`
- triggered rule: `join_lookup_add`
- Details:
  - how=left
  - left_key_coverage_rate=1.0
```

## Strengths

- deterministic
- cheap to run
- easy to inspect
- no external provider dependency
- useful lower-bound and ablation baseline

## Limitations

- no semantic reasoning beyond the heuristics already encoded
- family-level rules can overfire when multiple similar variants exist
- threshold behavior is hand-tuned
- sampled summaries are approximate for large tables because materialization switches to deterministic uniform row sampling
- does not execute or validate an actual preprocessing pipeline

## Tests

Primary tests:
- [test_rule_based.py](/agent/tests/test_rule_based.py)
- [test_rule_based_runner.py](/agent/tests/test_rule_based_runner.py)

These cover:
- add/remove heuristic behavior
- decision logging
- runner output contract
