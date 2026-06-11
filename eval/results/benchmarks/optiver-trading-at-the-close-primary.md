# Benchmark Aggregate Report

## Configuration

- Stage scope: `primary`
- Success threshold: `0.5`
- Tasks included: `optiver-trading-at-the-close`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.619048`
- Mean Add Precision: `0.508962`
- Mean Add Recall: `0.223364`
- Mean Add F1: `0.293115`
- Mean Remove Precision: `0.600000`
- Mean Remove Recall: `0.666667`
- Mean Remove F1: `0.478141`
- Mean Task Completion Score: `0.479891`
- Mean Strict Task Completion Score: `0.385627`
- Mean Task Completion Variance: `0.003519`
- Mean Runtime (s): `191.526792`
- Mean Total Tokens: `12930.125000`
- Mean API Calls: `3.012500`
- Mean Tool Calls: `6.600000`
- Mean Cost (USD): `0.146638`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| optiver-trading-at-the-close | MAE | finance_tabular | regression | single_table | xlarge (5237980) | low (16) | medium (20) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| optiver-trading-at-the-close | 21 | 6 | 0.619048 | 4.047619 | 0.508962 | 0.223364 | 0.293115 | 0.600000 | 0.666667 | 0.478141 | 0.479891 | 0.385627 | 0.003519 | 191.526792 | 12930.125000 | 3.012500 | 6.600000 | 0.146638 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| optiver-trading-at-the-close | tc1_from_scratch | claude_code | try1 | 0.538462 | 0.500000 | 0.518519 | 1.000000 | 1.000000 | 1.000000 | 0.759259 | 0.759259 | `true` | 133.490374 | 3763 | `null` | 22 | 0.411152 |
| optiver-trading-at-the-close | tc1_from_scratch | claude_code | try2 | 0.416667 | 0.357143 | 0.384615 | 1.000000 | 1.000000 | 1.000000 | 0.692307 | 0.692307 | `true` | 119.310138 | 3307 | `null` | 16 | 0.250222 |
| optiver-trading-at-the-close | tc1_from_scratch | claude_code | try3 | 0.538462 | 0.500000 | 0.518519 | 1.000000 | 1.000000 | 1.000000 | 0.759259 | 0.759259 | `true` | 103.468422 | 3219 | `null` | 13 | 0.256297 |
| optiver-trading-at-the-close | tc1_from_scratch | claude_code | try4 | 0.615385 | 0.571429 | 0.592593 | 1.000000 | 1.000000 | 1.000000 | 0.796296 | 0.796296 | `true` | 207.306790 | 4188 | `null` | 21 | 0.398944 |
| optiver-trading-at-the-close | tc1_from_scratch | claude_code | try5 | 0.538462 | 0.500000 | 0.518519 | 1.000000 | 1.000000 | 1.000000 | 0.759259 | 0.759259 | `true` | 114.610164 | 3363 | `null` | 23 | 0.376601 |
| optiver-trading-at-the-close | tc1_from_scratch | generic_agent | try1 | 0.538462 | 0.500000 | 0.518519 | 1.000000 | 1.000000 | 1.000000 | 0.759259 | 0.759259 | `true` | 117.249000 | 26924 | 6 | 7 | 0.272959 |
| optiver-trading-at-the-close | tc1_from_scratch | generic_agent | try2 | 0.571429 | 0.571429 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 106.395000 | 24202 | 5 | 5 | 0.193121 |
| optiver-trading-at-the-close | tc1_from_scratch | generic_agent | try3 | 0.545455 | 0.428571 | 0.480000 | 1.000000 | 1.000000 | 1.000000 | 0.740000 | 0.740000 | `true` | 109.868000 | 21355 | 6 | 6 | 0.189221 |
| optiver-trading-at-the-close | tc1_from_scratch | generic_agent | try4 | 0.555556 | 0.357143 | 0.434783 | 1.000000 | 1.000000 | 1.000000 | 0.717391 | 0.717391 | `true` | 88.076000 | 20200 | 7 | 7 | 0.175701 |
| optiver-trading-at-the-close | tc1_from_scratch | generic_agent | try5 | 0.538462 | 0.500000 | 0.518519 | 1.000000 | 1.000000 | 1.000000 | 0.759259 | 0.759259 | `true` | 103.402000 | 19340 | 6 | 6 | 0.165186 |
| optiver-trading-at-the-close | tc1_from_scratch | human | human_tc1_sean_kraemer_v3_manual_rebuild | 1.000000 | 0.571429 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | `true` | 2400 | `null` | `null` | `null` | `null` |
| optiver-trading-at-the-close | tc1_from_scratch | proposed_agent | try1 | 0.615385 | 0.571429 | 0.592593 | 1.000000 | 1.000000 | 1.000000 | 0.796296 | 0.796296 | `true` | 137.011000 | 35168 | 7 | 10 | 0.335371 |
| optiver-trading-at-the-close | tc1_from_scratch | proposed_agent | try2 | 0.750000 | 0.642857 | 0.692308 | 1.000000 | 1.000000 | 1.000000 | 0.846154 | 0.846154 | `true` | 146.013000 | 39478 | 8 | 11 | 0.294802 |
| optiver-trading-at-the-close | tc1_from_scratch | proposed_agent | try3 | 0.750000 | 0.428571 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 92.357000 | 19540 | 5 | 7 | 0.153153 |
| optiver-trading-at-the-close | tc1_from_scratch | proposed_agent | try4 | 0.555556 | 0.357143 | 0.434783 | 1.000000 | 1.000000 | 1.000000 | 0.717391 | 0.717391 | `true` | 117.427000 | 31284 | 6 | 9 | 0.222552 |
| optiver-trading-at-the-close | tc1_from_scratch | proposed_agent | try5 | 0.750000 | 0.428571 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 115.419000 | 33718 | 8 | 11 | 0.244525 |
| optiver-trading-at-the-close | tc1_from_scratch | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc1_from_scratch | single_llm | try1 | 0.545455 | 0.428571 | 0.480000 | 1.000000 | 1.000000 | 1.000000 | 0.740000 | 0.740000 | `true` | 18.763000 | 1157 | 1 | 0 | 0.075964 |
| optiver-trading-at-the-close | tc1_from_scratch | single_llm | try2 | 0.777778 | 0.500000 | 0.608696 | 1.000000 | 1.000000 | 1.000000 | 0.804348 | 0.804348 | `true` | 18.754000 | 1015 | 1 | 0 | 0.020055 |
| optiver-trading-at-the-close | tc1_from_scratch | single_llm | try3 | 0.600000 | 0.428571 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 17.289000 | 901 | 1 | 0 | 0.018345 |
| optiver-trading-at-the-close | tc1_from_scratch | single_llm | try4 | 0.500000 | 0.428571 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 17.982000 | 1076 | 1 | 0 | 0.020970 |
| optiver-trading-at-the-close | tc1_from_scratch | single_llm | try5 | 0.600000 | 0.428571 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 17.431000 | 1001 | 1 | 0 | 0.019845 |
| optiver-trading-at-the-close | tc2_partial_good | claude_code | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 52.484532 | 2495 | `null` | 10 | 0.221282 |
| optiver-trading-at-the-close | tc2_partial_good | claude_code | try2 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 66.162292 | 1519 | `null` | 24 | 0.262688 |
| optiver-trading-at-the-close | tc2_partial_good | claude_code | try3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 43.186049 | 2260 | `null` | 8 | 0.185823 |
| optiver-trading-at-the-close | tc2_partial_good | claude_code | try4 | 0.666667 | 0.200000 | 0.307692 | 0.000000 | 1.000000 | 0.000000 | 0.653846 | 0.153846 | `true` | 391.388065 | 2447 | `null` | 35 | 0.636463 |
| optiver-trading-at-the-close | tc2_partial_good | claude_code | try5 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 97.894922 | 2495 | `null` | 26 | 0.275009 |
| optiver-trading-at-the-close | tc2_partial_good | generic_agent | try1 | 0.400000 | 0.200000 | 0.266667 | 0.000000 | 1.000000 | 0.000000 | 0.633333 | 0.133333 | `true` | 158.127000 | 22121 | 6 | 7 | 0.175363 |
| optiver-trading-at-the-close | tc2_partial_good | generic_agent | try2 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 51.182000 | 9845 | 4 | 4 | 0.087099 |
| optiver-trading-at-the-close | tc2_partial_good | generic_agent | try3 | 0.666667 | 0.200000 | 0.307692 | 0.000000 | 1.000000 | 0.000000 | 0.653846 | 0.153846 | `true` | 93.418000 | 17020 | 5 | 5 | 0.138268 |
| optiver-trading-at-the-close | tc2_partial_good | generic_agent | try4 | 0.500000 | 0.100000 | 0.166667 | 0.000000 | 1.000000 | 0.000000 | 0.583333 | 0.083334 | `true` | 107.630000 | 23922 | 7 | 8 | 0.202494 |
| optiver-trading-at-the-close | tc2_partial_good | generic_agent | try5 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 56.551000 | 9493 | 4 | 4 | 0.088515 |
| optiver-trading-at-the-close | tc2_partial_good | proposed_agent | try1 | 0.800000 | 0.400000 | 0.533333 | 0.000000 | 1.000000 | 0.000000 | 0.766666 | 0.266666 | `true` | 138.337000 | 23335 | 5 | 6 | 0.189651 |
| optiver-trading-at-the-close | tc2_partial_good | proposed_agent | try2 | 0.800000 | 0.400000 | 0.533333 | 0.000000 | 1.000000 | 0.000000 | 0.766666 | 0.266666 | `true` | 154.774000 | 30343 | 6 | 8 | 0.235360 |
| optiver-trading-at-the-close | tc2_partial_good | proposed_agent | try3 | 0.800000 | 0.400000 | 0.533333 | 0.000000 | 1.000000 | 0.000000 | 0.766666 | 0.266666 | `true` | 131.906000 | 24553 | 6 | 7 | 0.199635 |
| optiver-trading-at-the-close | tc2_partial_good | proposed_agent | try4 | 0.750000 | 0.300000 | 0.428571 | 0.000000 | 1.000000 | 0.000000 | 0.714286 | 0.214285 | `true` | 126.006000 | 21412 | 5 | 6 | 0.172934 |
| optiver-trading-at-the-close | tc2_partial_good | proposed_agent | try5 | 1.000000 | 0.400000 | 0.571429 | 0.000000 | 1.000000 | 0.000000 | 0.785714 | 0.285714 | `true` | 126.223000 | 20730 | 5 | 5 | 0.173335 |
| optiver-trading-at-the-close | tc2_partial_good | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc2_partial_good | single_llm | try1 | 0.666667 | 0.200000 | 0.307692 | 0.000000 | 1.000000 | 0.000000 | 0.653846 | 0.153846 | `true` | 34.094000 | 2144 | 1 | 0 | 0.036131 |
| optiver-trading-at-the-close | tc2_partial_good | single_llm | try2 | 0.500000 | 0.200000 | 0.285714 | 0.000000 | 1.000000 | 0.000000 | 0.642857 | 0.142857 | `true` | 34.914000 | 2157 | 1 | 0 | 0.037271 |
| optiver-trading-at-the-close | tc2_partial_good | single_llm | try3 | 0.500000 | 0.200000 | 0.285714 | 0.000000 | 1.000000 | 0.000000 | 0.642857 | 0.142857 | `true` | 43.606000 | 2466 | 1 | 0 | 0.041906 |
| optiver-trading-at-the-close | tc2_partial_good | single_llm | try4 | 0.750000 | 0.300000 | 0.428571 | 0.000000 | 1.000000 | 0.000000 | 0.714286 | 0.214285 | `true` | 36.201000 | 2151 | 1 | 0 | 0.037181 |
| optiver-trading-at-the-close | tc2_partial_good | single_llm | try5 | 0.500000 | 0.200000 | 0.285714 | 0.000000 | 1.000000 | 0.000000 | 0.642857 | 0.142857 | `true` | 37.217000 | 2131 | 1 | 0 | 0.036881 |
| optiver-trading-at-the-close | tc3_fault_injected | claude_code | try1 | 1.000000 | 0.071429 | 0.133333 | 1.000000 | 0.500000 | 0.666667 | 0.316667 | 0.400000 | `false` | 89.982781 | 3020 | `null` | 22 | 0.248707 |
| optiver-trading-at-the-close | tc3_fault_injected | claude_code | try2 | 0.500000 | 0.071429 | 0.125000 | 1.000000 | 0.750000 | 0.857143 | 0.437500 | 0.491071 | `false` | 77.479131 | 2238 | `null` | 19 | 0.245911 |
| optiver-trading-at-the-close | tc3_fault_injected | claude_code | try3 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.500000 | 0.666667 | 0.250000 | 0.333334 | `false` | 211.847492 | 1520 | `null` | 31 | 0.621263 |
| optiver-trading-at-the-close | tc3_fault_injected | claude_code | try4 | 0.666667 | 0.142857 | 0.235294 | 1.000000 | 0.750000 | 0.857143 | 0.492647 | 0.546218 | `false` | 189.297474 | 2390 | `null` | 17 | 0.232044 |
| optiver-trading-at-the-close | tc3_fault_injected | claude_code | try5 | 0.666667 | 0.142857 | 0.235294 | 1.000000 | 0.500000 | 0.666667 | 0.367647 | 0.450981 | `false` | 85.704304 | 1406 | `null` | 22 | 0.191604 |
| optiver-trading-at-the-close | tc3_fault_injected | generic_agent | try1 | 0.750000 | 0.214286 | 0.333333 | 1.000000 | 0.750000 | 0.857143 | 0.541667 | 0.595238 | `true` | 98.555000 | 20624 | 5 | 6 | 0.159901 |
| optiver-trading-at-the-close | tc3_fault_injected | generic_agent | try2 | 0.600000 | 0.214286 | 0.315789 | 1.000000 | 0.500000 | 0.666667 | 0.407894 | 0.491228 | `false` | 114.337000 | 22899 | 5 | 5 | 0.181429 |
| optiver-trading-at-the-close | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.142857 | 0.250000 | 1.000000 | 0.250000 | 0.400000 | 0.250000 | 0.325000 | `false` | 79.283000 | 17035 | 5 | 6 | 0.141872 |
| optiver-trading-at-the-close | tc3_fault_injected | generic_agent | try4 | 0.500000 | 0.071429 | 0.125000 | 1.000000 | 0.250000 | 0.400000 | 0.187500 | 0.262500 | `false` | 112.158000 | 21651 | 6 | 6 | 0.177277 |
| optiver-trading-at-the-close | tc3_fault_injected | generic_agent | try5 | 0.666667 | 0.285714 | 0.400000 | 1.000000 | 0.500000 | 0.666667 | 0.450000 | 0.533334 | `false` | 87.529000 | 15297 | 4 | 4 | 0.133670 |
| optiver-trading-at-the-close | tc3_fault_injected | proposed_agent | try1 | 0.750000 | 0.214286 | 0.333333 | 1.000000 | 0.500000 | 0.666667 | 0.416666 | 0.500000 | `false` | 131.782000 | 24720 | 6 | 6 | 0.194754 |
| optiver-trading-at-the-close | tc3_fault_injected | proposed_agent | try2 | 1.000000 | 0.214286 | 0.352941 | 1.000000 | 0.250000 | 0.400000 | 0.301470 | 0.376471 | `false` | 162.575000 | 28789 | 6 | 6 | 0.218408 |
| optiver-trading-at-the-close | tc3_fault_injected | proposed_agent | try3 | 0.750000 | 0.214286 | 0.333333 | 1.000000 | 0.500000 | 0.666667 | 0.416666 | 0.500000 | `false` | 127.511000 | 20302 | 5 | 5 | 0.166688 |
| optiver-trading-at-the-close | tc3_fault_injected | proposed_agent | try4 | 0.800000 | 0.285714 | 0.421053 | 1.000000 | 0.500000 | 0.666667 | 0.460527 | 0.543860 | `false` | 150.320000 | 23905 | 5 | 5 | 0.193517 |
| optiver-trading-at-the-close | tc3_fault_injected | proposed_agent | try5 | 0.500000 | 0.142857 | 0.222222 | 1.000000 | 0.500000 | 0.666667 | 0.361111 | 0.444445 | `false` | 152.571000 | 28630 | 6 | 6 | 0.223296 |
| optiver-trading-at-the-close | tc3_fault_injected | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.142857 | 0.250000 | 1.000000 | 0.500000 | 0.666667 | 0.375000 | 0.458334 | `false` | 71.856000 | 3401 | 1 | 0 | 0.054962 |
| optiver-trading-at-the-close | tc3_fault_injected | single_llm | try2 | 0.750000 | 0.214286 | 0.333333 | 1.000000 | 0.500000 | 0.666667 | 0.416666 | 0.500000 | `false` | 38.417000 | 2132 | 1 | 0 | 0.036904 |
| optiver-trading-at-the-close | tc3_fault_injected | single_llm | try3 | 0.500000 | 0.071429 | 0.125000 | 1.000000 | 0.500000 | 0.666667 | 0.312500 | 0.395834 | `false` | 41.194000 | 2234 | 1 | 0 | 0.038434 |
| optiver-trading-at-the-close | tc3_fault_injected | single_llm | try4 | 0.666667 | 0.142857 | 0.235294 | 1.000000 | 0.500000 | 0.666667 | 0.367647 | 0.450981 | `false` | 38.689000 | 2230 | 1 | 0 | 0.038374 |
| optiver-trading-at-the-close | tc3_fault_injected | single_llm | try5 | 0.800000 | 0.285714 | 0.421053 | 1.000000 | 0.500000 | 0.666667 | 0.460527 | 0.543860 | `false` | 36.047000 | 2113 | 1 | 0 | 0.036619 |
| optiver-trading-at-the-close | tc4_mixed_history | claude_code | try1 | 0.500000 | 0.181818 | 0.266667 | 0.000000 | 0.000000 | 0.000000 | 0.133333 | 0.133333 | `false` | 118.836988 | 4019 | `null` | 25 | 0.339386 |
| optiver-trading-at-the-close | tc4_mixed_history | claude_code | try2 | 0.666667 | 0.181818 | 0.285714 | 0.000000 | 0.000000 | 0.000000 | 0.142857 | 0.142857 | `false` | 102.006234 | 5723 | `null` | 13 | 0.309138 |
| optiver-trading-at-the-close | tc4_mixed_history | claude_code | try3 | 0.333333 | 0.090909 | 0.142857 | 0.000000 | 0.000000 | 0.000000 | 0.071429 | 0.071429 | `false` | 93.978636 | 2467 | `null` | 13 | 0.242032 |
| optiver-trading-at-the-close | tc4_mixed_history | claude_code | try4 | 0.333333 | 0.090909 | 0.142857 | 0.000000 | 0.000000 | 0.000000 | 0.071429 | 0.071429 | `false` | 173.892692 | 5311 | `null` | 29 | 0.349986 |
| optiver-trading-at-the-close | tc4_mixed_history | claude_code | try5 | 0.500000 | 0.181818 | 0.266667 | 1.000000 | 0.333333 | 0.500000 | 0.300000 | 0.383333 | `false` | 99.601665 | 2157 | `null` | 22 | 0.219846 |
| optiver-trading-at-the-close | tc4_mixed_history | generic_agent | try1 | 0.750000 | 0.272727 | 0.400000 | 1.000000 | 0.333333 | 0.500000 | 0.366667 | 0.450000 | `false` | 87.628000 | 18948 | 5 | 5 | 0.149607 |
| optiver-trading-at-the-close | tc4_mixed_history | generic_agent | try2 | 0.666667 | 0.181818 | 0.285714 | 0.000000 | 0.000000 | 0.000000 | 0.142857 | 0.142857 | `false` | 111.816000 | 22587 | 5 | 5 | 0.179555 |
| optiver-trading-at-the-close | tc4_mixed_history | generic_agent | try3 | 0.666667 | 0.181818 | 0.285714 | 1.000000 | 0.333333 | 0.500000 | 0.309524 | 0.392857 | `false` | 98.221000 | 22490 | 6 | 6 | 0.178470 |
| optiver-trading-at-the-close | tc4_mixed_history | generic_agent | try4 | 0.333333 | 0.090909 | 0.142857 | 1.000000 | 0.333333 | 0.500000 | 0.238095 | 0.321429 | `false` | 109.684000 | 22408 | 6 | 6 | 0.181143 |
| optiver-trading-at-the-close | tc4_mixed_history | generic_agent | try5 | 0.500000 | 0.181818 | 0.266667 | 1.000000 | 0.333333 | 0.500000 | 0.300000 | 0.383333 | `false` | 101.099000 | 21179 | 5 | 7 | 0.167572 |
| optiver-trading-at-the-close | tc4_mixed_history | proposed_agent | try1 | 0.800000 | 0.363636 | 0.500000 | 1.000000 | 0.333333 | 0.500000 | 0.416666 | 0.500000 | `false` | 150.509000 | 19360 | 4 | 4 | 0.180835 |
| optiver-trading-at-the-close | tc4_mixed_history | proposed_agent | try2 | 0.750000 | 0.272727 | 0.400000 | 1.000000 | 0.666667 | 0.800000 | 0.533334 | 0.600000 | `true` | 180.881000 | 27777 | 5 | 6 | 0.231345 |
| optiver-trading-at-the-close | tc4_mixed_history | proposed_agent | try3 | 0.800000 | 0.363636 | 0.500000 | 0.000000 | 0.000000 | 0.000000 | 0.250000 | 0.250000 | `false` | 217.660000 | 40485 | 6 | 8 | 0.299298 |
| optiver-trading-at-the-close | tc4_mixed_history | proposed_agent | try4 | 0.750000 | 0.272727 | 0.400000 | 1.000000 | 0.666667 | 0.800000 | 0.533334 | 0.600000 | `true` | 130.127000 | 16974 | 4 | 3 | 0.162828 |
| optiver-trading-at-the-close | tc4_mixed_history | proposed_agent | try5 | 0.750000 | 0.272727 | 0.400000 | 1.000000 | 0.333333 | 0.500000 | 0.366667 | 0.450000 | `false` | 117.507000 | 22857 | 5 | 5 | 0.176732 |
| optiver-trading-at-the-close | tc4_mixed_history | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc4_mixed_history | single_llm | try1 | 0.666667 | 0.181818 | 0.285714 | 1.000000 | 0.333333 | 0.500000 | 0.309524 | 0.392857 | `false` | 49.520000 | 3027 | 1 | 0 | 0.049256 |
| optiver-trading-at-the-close | tc4_mixed_history | single_llm | try2 | 1.000000 | 0.181818 | 0.307692 | 1.000000 | 0.333333 | 0.500000 | 0.320512 | 0.403846 | `false` | 45.373000 | 2576 | 1 | 0 | 0.043594 |
| optiver-trading-at-the-close | tc4_mixed_history | single_llm | try3 | 1.000000 | 0.181818 | 0.307692 | 1.000000 | 0.333333 | 0.500000 | 0.320512 | 0.403846 | `false` | 47.907000 | 2838 | 1 | 0 | 0.047524 |
| optiver-trading-at-the-close | tc4_mixed_history | single_llm | try4 | 1.000000 | 0.272727 | 0.428571 | 1.000000 | 0.333333 | 0.500000 | 0.380952 | 0.464286 | `false` | 33.367000 | 1945 | 1 | 0 | 0.034129 |
| optiver-trading-at-the-close | tc4_mixed_history | single_llm | try5 | 0.666667 | 0.181818 | 0.285714 | 0.000000 | 0.000000 | 0.000000 | 0.142857 | 0.142857 | `false` | 60.639000 | 3508 | 1 | 0 | 0.057574 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| optiver-trading-at-the-close | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.529488 | 0.485714 | 0.506553 | 1.000000 | 1.000000 | 1.000000 | 0.753276 | 0.753276 | 0.001135 | 135.637178 | 3568.000000 | `null` | 19.000000 | 0.338643 |
| optiver-trading-at-the-close | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.549873 | 0.471429 | 0.504650 | 1.000000 | 1.000000 | 1.000000 | 0.752325 | 0.752325 | 0.000517 | 104.998000 | 22404.200000 | 6.000000 | 6.200000 | 0.199238 |
| optiver-trading-at-the-close | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 0.571429 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | 0.000000 | 2400 | `null` | `null` | `null` | `null` |
| optiver-trading-at-the-close | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.684188 | 0.485714 | 0.562119 | 1.000000 | 1.000000 | 1.000000 | 0.781059 | 0.781059 | 0.001732 | 121.645400 | 31837.600000 | 6.800000 | 9.600000 | 0.250081 |
| optiver-trading-at-the-close | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.604647 | 0.442857 | 0.510047 | 1.000000 | 1.000000 | 1.000000 | 0.755023 | 0.755023 | 0.000659 | 18.043800 | 1030.000000 | 1.000000 | 0.000000 | 0.031036 |
| optiver-trading-at-the-close | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.133333 | 0.040000 | 0.061538 | 0.000000 | 1.000000 | 0.000000 | 0.530769 | 0.030769 | 0.003787 | 130.223172 | 2243.200000 | `null` | 20.600000 | 0.316253 |
| optiver-trading-at-the-close | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.313333 | 0.100000 | 0.148205 | 0.000000 | 1.000000 | 0.000000 | 0.574102 | 0.074103 | 0.004187 | 93.381600 | 16480.200000 | 5.200000 | 5.600000 | 0.138348 |
| optiver-trading-at-the-close | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.830000 | 0.380000 | 0.520000 | 0.000000 | 1.000000 | 0.000000 | 0.760000 | 0.259999 | 0.000577 | 135.449200 | 24074.600000 | 5.400000 | 6.400000 | 0.194183 |
| optiver-trading-at-the-close | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.583333 | 0.220000 | 0.318681 | 0.000000 | 1.000000 | 0.000000 | 0.659341 | 0.159340 | 0.000773 | 37.206400 | 2209.800000 | 1.000000 | 0.000000 | 0.037874 |
| optiver-trading-at-the-close | tc3_fault_injected | claude_code | 5 | `false` | 0.000000 | 0.566667 | 0.085714 | 0.145784 | 1.000000 | 0.600000 | 0.742857 | 0.372892 | 0.444321 | 0.007361 | 130.862237 | 2114.800000 | `null` | 22.200000 | 0.307906 |
| optiver-trading-at-the-close | tc3_fault_injected | generic_agent | 5 | `true` | 0.200000 | 0.703333 | 0.185714 | 0.284824 | 1.000000 | 0.450000 | 0.598095 | 0.367412 | 0.441460 | 0.016996 | 98.372400 | 19501.200000 | 5.000000 | 5.400000 | 0.158830 |
| optiver-trading-at-the-close | tc3_fault_injected | proposed_agent | 5 | `false` | 0.000000 | 0.760000 | 0.214286 | 0.332576 | 1.000000 | 0.450000 | 0.613334 | 0.391288 | 0.472955 | 0.003012 | 144.951800 | 25269.200000 | 5.600000 | 5.600000 | 0.199333 |
| optiver-trading-at-the-close | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc3_fault_injected | single_llm | 5 | `false` | 0.000000 | 0.743333 | 0.171429 | 0.272936 | 1.000000 | 0.500000 | 0.666667 | 0.386468 | 0.469802 | 0.002471 | 45.240600 | 2422.000000 | 1.000000 | 0.000000 | 0.041058 |
| optiver-trading-at-the-close | tc4_mixed_history | claude_code | 5 | `false` | 0.000000 | 0.466667 | 0.145454 | 0.220952 | 0.200000 | 0.066667 | 0.100000 | 0.143810 | 0.160476 | 0.006997 | 117.663243 | 3935.400000 | `null` | 20.400000 | 0.292078 |
| optiver-trading-at-the-close | tc4_mixed_history | generic_agent | 5 | `false` | 0.000000 | 0.583333 | 0.181818 | 0.276190 | 0.800000 | 0.266666 | 0.400000 | 0.271429 | 0.338095 | 0.005796 | 101.689600 | 21522.400000 | 5.400000 | 5.800000 | 0.171269 |
| optiver-trading-at-the-close | tc4_mixed_history | proposed_agent | 5 | `true` | 0.400000 | 0.770000 | 0.309091 | 0.440000 | 0.800000 | 0.400000 | 0.520000 | 0.420000 | 0.480000 | 0.011489 | 159.336800 | 25490.600000 | 4.800000 | 5.200000 | 0.210208 |
| optiver-trading-at-the-close | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc4_mixed_history | single_llm | 5 | `false` | 0.000000 | 0.866667 | 0.200000 | 0.323077 | 0.800000 | 0.266666 | 0.400000 | 0.294871 | 0.361538 | 0.006410 | 47.361200 | 2778.800000 | 1.000000 | 0.000000 | 0.046415 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 0.500000 | 5.000000 | 0.500000 | 0.424039 | 0.189220 | 0.233707 | 0.550000 | 0.666667 | 0.460714 | 0.450187 | 0.347210 | 0.004820 | 128.596457 | 2965.350000 | `null` | 20.550000 | 0.313720 |
| generic_agent | 4 | 0.750000 | 5.000000 | 0.550000 | 0.537468 | 0.234740 | 0.303467 | 0.700000 | 0.679167 | 0.499524 | 0.491317 | 0.401496 | 0.006874 | 99.610400 | 19977.000000 | 5.400000 | 5.750000 | 0.166921 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.571429 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | 0.000000 | 2400.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 0.750000 | 5.000000 | 0.600000 | 0.761047 | 0.347273 | 0.463674 | 0.700000 | 0.712500 | 0.533334 | 0.588087 | 0.498503 | 0.004202 | 140.345800 | 26668.000000 | 5.650000 | 6.700000 | 0.213451 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.000000 | 0.000000 | 0.000000 | 0.250000 | 0.500000 | 0.250000 | 0.250000 | 0.125000 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 0.500000 | 5.000000 | 0.500000 | 0.699495 | 0.258572 | 0.356185 | 0.700000 | 0.691666 | 0.516667 | 0.523926 | 0.436426 | 0.002578 | 36.963000 | 2110.150000 | 1.000000 | 0.000000 | 0.039096 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task optiver-trading-at-the-close --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/optiver-trading-at-the-close-primary.md
```
