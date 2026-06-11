# `allstate-claims-severity` Benchmark Notes

This task root defines the action-bank benchmark task for `allstate-claims-severity`.

## Migration Scope

- Source material was salvaged from `origin/allstate-claims`.
- The branch was rebuilt on current `main`; it is not a continuation of the stale remote branch.
- The stale task contract was migrated to the current schemas for `task.json`, testcases, candidate bank, and human-baseline outputs.
- The official Kaggle CSVs and collected notebook dump are not mirrored locally, so this migration preserves the stale branch's notebook-backed evidence rather than recollecting notebooks.

## Task Contract

- The benchmark is single-table and official-only.
- The fixed official scope is:
  - `train.csv`
  - `test.csv`
  - `sample_submission.csv`
- The full action bank lives in `candidate_actions.json`.
- Every testcase uses the same full bank and stores only `input.context_action_ids`.
- Hidden scoring metadata stays in the bank; testcases do not store explicit expected add/remove IDs.

## Primary Spine

The conservative primary good spine has three effective units:

1. Drop the `id` identifier column.
2. Encode all `cat1`-`cat116` categorical predictors.
3. Log-transform the right-skewed `loss` target before model fitting.

The bank preserves two valid OR alternatives:

- `CA-000005` label-encodes `cat1`-`cat116`; `CA-000014` one-hot encodes them.
- `CA-000009` applies `np.log(loss)`; `CA-000027` applies `np.log1p(loss)`.

## Bank Snapshot

- Bank size: `28`
- Good actions: `5`
- Bad actions: `23`
- Primary effective good units after equivalence collapse: `3`
- Represented canonical families: `11`
- Candidate IDs were renumbered and mixed with old and new rows to remove the original bad-first/good-last ordering leak.
- The bank now has substantial bad-action margin above the `bad >= 3 * primary_effective_good_units` gate and covers categorical handling, numeric treatment, target clipping, feature selection, and interaction near-misses.

## Testcase Semantics

- `tc1_from_scratch`: empty context; all three primary good units should be recovered.
- `tc2_partial_good`: already has `CA-000001` and `CA-000005`; target transformation remains missing.
- `tc3_fault_injected`: contains `CA-000002` train-only label encoding and `CA-000007` destructive target clipping as faults.
- `tc4_mixed_history`: keeps the good drop-id and label-encoding path but injects `CA-000015`, one-hot encoding of the identifier.

## Human Baseline

- `human_baseline/tc1_human.json` selects `CA-000001` and `CA-000005`, intentionally omitting the target transform.
- The human baseline is a deliberately simple first-person baseline re-authored from migrated notes, not a newly executed local Kaggle run and not a perfect answer-key migration.
- `human_baseline/provenance/metadata.json` records the stale source branch and the non-executed notebook status.

## Shared Reports

- Shared report files were updated from current `main` plus this competition only.
- Allstate was added with 30 selected notebooks and `ok` collection status.
- Kaggle CLI metadata used for the shared table: Recruitment category, Jobs reward, 3,045 teams, deadline `2016-12-12 23:59:00`.

## QA Gate

Before merge, run:

- `uv run python eval/scripts/validate_artifacts.py`
- `uv run python -m unittest discover -s eval/tests -p 'test_*.py'`
- `uv run pre-commit run --all-files`
