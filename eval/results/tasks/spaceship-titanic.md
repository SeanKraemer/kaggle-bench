# Spaceship Titanic Evaluation Results

This file records the current canonical evaluation results for the `spaceship-titanic` action-bank benchmark.

## Evaluator

- Script: `eval/eval.py`
- Repository root working directory assumed: repo root
- Validation and local reproduction command prefix:
  - `uv run python`

## Task Profile

- Metric: `Accuracy`
- ML domain: `transportation_tabular`
- Problem type: `binary_classification`
- Table structure: `single_table`
- Dataset size bucket: `small (8693)`
- Feature dimensionality bucket: `low (14)`
- Preprocessing complexity bucket: `medium (17)`
- Cross-testcase aggregate views:
  - `eval/results/benchmarks/spaceship-titanic-primary.md`
  - `eval/results/benchmarks/spaceship-titanic-all.md`

## Official Scoring Setup

- Official reporting scope: `--stage-scope primary`
  - filters scoring to `core_preprocessing` units
  - excludes the optional numeric-scaling equivalence group from headline metrics
- Supplementary analysis scope: `--stage-scope all`
  - includes non-primary `model_specific_preprocessing` actions
- Expected edits are derived from the canonical bank:
  - add-side targets are the task's good actions that are still missing from `context_action_ids`
  - remove-side targets are the bad actions already present in `context_action_ids`
- Hidden scoring semantics:
  - equivalence groups collapse alternate age-imputation and categorical-encoding strategies into one effective add-side unit
  - `must_follow_action_ids`, `invalidates_action_ids`, and `conflicts_with_action_ids` are checked against the selected final action set
- Success threshold:
  - `tau = 0.5`

## Canonical Task Snapshot

- Candidate bank: `51` actions
- Good actions: `15`
- Bad actions: `36`
- Effective primary good units: `11`
- The bank order was shuffled with seed `20260413` and all Spaceship `CA-*` ids were renumbered afterward.
- Standard testcases: `4`
- Evaluated run artifacts: `5`

## Single-Run Results

| Artifact | Agent | Testcase | Add F1 | Remove F1 | Rollback Accuracy | Task Completion | Strict Completion | Success | Time (s) |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| `human_baseline/tc1_human.json` | `human` | `tc1_from_scratch` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 2700 |
| `outputs/tc1_rule_based_try1.json` | `rule_based` | `tc1_from_scratch` | 0.952381 | 1.000000 | 1.000000 | 0.976190 | 0.976190 | `true` | 12 |
| `outputs/tc2_rule_based_try1.json` | `rule_based` | `tc2_partial_good` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 9 |
| `outputs/tc3_rule_based_try1.json` | `rule_based` | `tc3_fault_injected` | 0.900000 | 0.857143 | 0.750000 | 0.825000 | 0.878572 | `true` | 14 |
| `outputs/tc4_rule_based_try1.json` | `rule_based` | `tc4_mixed_history` | 1.000000 | 0.800000 | 0.666667 | 0.833333 | 0.900000 | `true` | 13 |

## Aggregate Summary

- Task success rate: `1.000000`
- Mean Add F1: `0.970476`
- Mean Remove F1: `0.931429`
- Mean Rollback Accuracy: `0.883333`
- Mean Task Completion Score: `0.926905`
- Mean Strict Task Completion Score: `0.950952`

## Notes

- `tc1_rule_based_try1` remains slightly incomplete on the add side because it still omits the explicit CryoSleep zero-spend rule.
- `tc3_rule_based_try1` repairs most of the injected state but still leaves one bad action in context and misses two good add targets.
- `tc4_rule_based_try1` restores all missing primary good actions, but rollback remains partial because one injected bad action survives.
- `tc1_human` is a re-authored bank-id reference artifact built from notebook evidence, not a blinded human study.

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/eval.py --testcase data/tasks/spaceship-titanic/testcases/tc1_from_scratch.json --input data/tasks/spaceship-titanic/human_baseline/tc1_human.json --stage-scope primary --pretty
uv run python eval/eval.py --testcase data/tasks/spaceship-titanic/testcases/tc3_fault_injected.json --input data/tasks/spaceship-titanic/outputs/tc3_rule_based_try1.json --stage-scope primary --pretty
uv run python eval/aggregate.py --task spaceship-titanic --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/spaceship-titanic-primary.md
uv run python eval/aggregate.py --task spaceship-titanic --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/spaceship-titanic-all.md
```
