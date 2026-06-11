# sberbank-russian-housing-market Benchmark Notes

This task root defines the canonical action-bank benchmark task for Sberbank.

## Benchmark Shape

- Task artifacts live under `data/tasks/sberbank-russian-housing-market/`.
- Machine-checked schemas live under `data/schema/`.
- Evaluator code and reports live under `eval/`.

## Task Contract

- This benchmark slice is fixed to `train.csv` / `test.csv` housing rows keyed by `id`, with `macro.csv` as the timestamp-aligned lookup table.
- The task-level bank lives in `candidate_actions.json`.
- Every testcase uses the same full bank.
- Each testcase stores only `input.context_action_ids`.
- The evaluator derives:
  - `candidate_action_ids = full_bank_action_ids - context_action_ids`
  - expected add units from the active good portion of the derived candidate side
  - expected remove units from the active bad portion of the context side

## Scoring Metadata

The bank may include hidden scoring metadata that should stay out of agent-facing benchmark renderings:

- `equivalence_group`
- `must_follow_action_ids`
- `invalidates_action_ids`
- `conflicts_with_action_ids`

These fields are for evaluator logic only.

## Scope

- `primary` scores only `eval_stage = core_preprocessing`
- `all` scores every active stage

## Sberbank Benchmark Shape

- The preferred primary good path is a compact notebook-backed housing-cleaning and macro-join spine:
  - normalize impossible `build_year`, `kitch_sq`, and `life_sq` values
  - parse `timestamp`
  - derive `year/month/week/dayofweek`
  - cast mixed categorical flags to string
  - optionally filter extreme `life_sq`
  - left-join selected macro indicators by `timestamp`
- Model-specific follow-ons include grouped temporal counts, selected imputations, compact category mappings, housing ratios, interactions, and optional `log1p(price_doc)`.
- The benchmark penalizes especially harmful local mistakes:
  - dropping the core apartment-size columns
  - investment-only train filtering
  - zero-filling area fields
  - lossy or mismatched macro joins
  - denominator-swapped housing ratios
  - target-leaking grouped aggregates

## Current Bank Snapshot

- Current draft bank size: 124 actions
- Good actions: 22
- Bad actions: 102
- Primary effective good units after equivalence-group collapse: 8
- All-scope effective good units after equivalence-group collapse: 22
- The validator hard gate is `bad >= 3 * primary effective good units`.
- The current draft keeps canonical action-type coverage at `40 / 40` against `data/schema/canonical_actions.json`.
- Difficulty distribution is currently medium-heavy: `79 medium`, `30 hard`, `15 easy`.
- Good-stage split is `8 core_preprocessing` and `14 model_specific_preprocessing`.

## Testcase Semantics

The four standard testcase roles are:

- [tc1_from_scratch.json](testcases/tc1_from_scratch.json)
  - empty context
  - checks recovery of the full Sberbank spine from scratch
- [tc2_partial_good.json](testcases/tc2_partial_good.json)
  - context contains only the early apartment-geometry cleanup actions `CA-000001`, `CA-000013`, `CA-000019`
  - leaves the parse/date/macro primary spine still missing
  - acts as a true continuation testcase rather than a near-finished state
- [tc3_fault_injected.json](testcases/tc3_fault_injected.json)
  - context contains only bad actions: `CA-000028`, `CA-000050`, `CA-000065`, `CA-000070`, `CA-000102`
  - keeps the rollback scenario self-contained without depending on absent good prerequisites
- [tc4_mixed_history.json](testcases/tc4_mixed_history.json)
  - context contains both good and bad history
  - the retained good side is intentionally small: `CA-000001`, `CA-000013`, `CA-000105`
  - the bad side is `CA-000050`, `CA-000062`, `CA-000103`
  - this keeps both add-side and remove-side decisions live instead of collapsing the testcase into mostly removals

## Example Output Scope

- Committed example outputs include `rule_based`, `single_llm`, and `naive_agent` artifacts across the standard four testcases.
- These are illustrative score carriers, not claims of finalized agent baselines.
- Their provenance traces should stay aligned with the current testcase semantics whenever testcase membership changes.

## Provenance Basis

- The bank reuses notebook evidence collected under:
  - `data/collector/data/kaggle/sberbank-russian-housing-market/notebooks.json`
  - `data/collector/data/golden/sberbank-russian-housing-market/action_candidates.jsonl`
- Strong evidence backbone notebooks include:
  - `aharless/latest-iteration-in-this-silly-game`
  - `aharless/exercising-the-exorcism`
  - `bguberfain/naive-xgb-lb-0-317`
  - `sudalairajkumar/feature-engineering-validation-strategy`
  - `valadi/magic-numbers-new-change`

## Authoring Reminders

- Treat this as a standalone benchmark contract even when reusing Sberbank notebook evidence.
- Keep notebook-backed evidence explicit for good actions.
- Maintain the strongly imbalanced bank with `bad >> good`.
- Keep testcase difficulty in the contexts, not in custom per-testcase candidate subsets.
- Re-check testcase coherence and example outputs whenever the bank changes.
- A committed draft human baseline is present under `human_baseline/`; treat it as placeholder evidence rather than a finalized manual benchmark.
