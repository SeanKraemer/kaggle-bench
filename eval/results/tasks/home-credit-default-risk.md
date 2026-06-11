# Home Credit Evaluation Results

This branch-local summary tracks the current Home Credit artifacts after regenerating `rule_based` `try1` outputs for `tc1` through `tc4`.

## Evaluator

- Script: `eval/eval.py`
- Recommended runner: `uv run python`
- Official reporting scope: `primary`
- Success threshold: `tau = 0.5`

## Task Profile

- Metric: `AUC`
- ML domain: `finance_tabular`
- Problem type: `binary_classification`
- Table structure: `multi_table_relational`
- Dataset size bucket: `xlarge (27299925)`
- Feature dimensionality bucket: `high (195)`
- Preprocessing complexity bucket: `high (21)`
- Benchmark aggregate reports:
  - [home-credit-default-risk-primary.md](../benchmarks/home-credit-default-risk-primary.md)
  - [home-credit-default-risk-all.md](../benchmarks/home-credit-default-risk-all.md)

## Single-Run Results

| Artifact | Agent | Testcase | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Rollback | Task Completion | Success | Time (s) | Total Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| `human_baseline/tc1_human.json` | `human` | `tc1_from_scratch` | 0.500000 | 0.600000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | `true` | 2400 | `null` | `null` | `null` | `null` |
| `outputs/tc1_rule_based_try1.json` | `rule_based` | `tc1_from_scratch` | 0.250000 | 0.066667 | 0.105263 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.552631 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| `outputs/tc1_single_llm_try1.json` | `single_llm` | `tc1_from_scratch` | 0.666667 | 0.533333 | 0.592593 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.796296 | `true` | 156.167000 | 1191 | 1 | 0 | 0.350812 |
| `outputs/tc2_rule_based_try1.json` | `rule_based` | `tc2_partial_good` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 1.000000 | 0.500000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| `outputs/tc3_claude_code_try1.json` | `claude_code` | `tc3_fault_injected` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 37 | 5240 | 9 | 12 | 0.180000 |
| `outputs/tc3_rule_based_try1.json` | `rule_based` | `tc3_fault_injected` | 0.250000 | 0.066667 | 0.105263 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.052631 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| `outputs/tc4_naive_agent_try1.json` | `naive_agent` | `tc4_mixed_history` | 1.000000 | 0.375000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | `true` | 43 | 4790 | 2 | 1 | 0.030000 |
| `outputs/tc4_rule_based_try1.json` | `rule_based` | `tc4_mixed_history` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |

## Aggregate Summary

| Groups | Agents | Task Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Rollback | Mean Task Completion | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 8 | 5 | 0.750000 | 0.458333 | 0.330208 | 0.361754 | 0.625000 | 0.750000 | 0.625000 | 0.750000 | 0.555877 | 329.520875 | 3740.333333 | 1.714286 | 1.857143 | 0.080116 |

## Notes

- All current Home Credit artifacts validate under the action-bank contract.
- `rule_based` `try1` now exists for `tc1_from_scratch`, `tc2_partial_good`, `tc3_fault_injected`, and `tc4_mixed_history`.
- Best current primary-scope run: `outputs/tc3_claude_code_try1.json` with task completion `1.000000`.
- Weakest current primary-scope run: `outputs/tc4_rule_based_try1.json` with task completion `0.000000`.
- For grouped agent/testcase views and all-scope results, use the benchmark aggregate reports linked above.

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python eval/aggregate.py --task home-credit-default-risk --stage-scope primary --format markdown --output eval/results/benchmarks/home-credit-default-risk-primary.md
uv run python eval/aggregate.py --task home-credit-default-risk --stage-scope all --format markdown --output eval/results/benchmarks/home-credit-default-risk-all.md
```
