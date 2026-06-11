# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `optiver-trading-at-the-close`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.571429`
- Mean Add Precision: `0.512880`
- Mean Add Recall: `0.177233`
- Mean Add F1: `0.247664`
- Mean Remove Precision: `0.600000`
- Mean Remove Recall: `0.666667`
- Mean Remove F1: `0.478141`
- Mean Task Completion Score: `0.457165`
- Mean Strict Task Completion Score: `0.362902`
- Mean Task Completion Variance: `0.003233`
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
| optiver-trading-at-the-close | 21 | 6 | 0.571429 | 4.047619 | 0.512880 | 0.177233 | 0.247664 | 0.600000 | 0.666667 | 0.478141 | 0.457165 | 0.362902 | 0.003233 | 191.526792 | 12930.125000 | 3.012500 | 6.600000 | 0.146638 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| optiver-trading-at-the-close | tc1_from_scratch | claude_code | try1 | 0.538462 | 0.388889 | 0.451613 | 1.000000 | 1.000000 | 1.000000 | 0.725807 | 0.725807 | `true` | 133.490374 | 3763 | `null` | 22 | 0.411152 |
| optiver-trading-at-the-close | tc1_from_scratch | claude_code | try2 | 0.500000 | 0.388889 | 0.437500 | 1.000000 | 1.000000 | 1.000000 | 0.718750 | 0.718750 | `true` | 119.310138 | 3307 | `null` | 16 | 0.250222 |
| optiver-trading-at-the-close | tc1_from_scratch | claude_code | try3 | 0.538462 | 0.388889 | 0.451613 | 1.000000 | 1.000000 | 1.000000 | 0.725807 | 0.725807 | `true` | 103.468422 | 3219 | `null` | 13 | 0.256297 |
| optiver-trading-at-the-close | tc1_from_scratch | claude_code | try4 | 0.666667 | 0.555556 | 0.606061 | 1.000000 | 1.000000 | 1.000000 | 0.803030 | 0.803030 | `true` | 207.306790 | 4188 | `null` | 21 | 0.398944 |
| optiver-trading-at-the-close | tc1_from_scratch | claude_code | try5 | 0.538462 | 0.388889 | 0.451613 | 1.000000 | 1.000000 | 1.000000 | 0.725807 | 0.725807 | `true` | 114.610164 | 3363 | `null` | 23 | 0.376601 |
| optiver-trading-at-the-close | tc1_from_scratch | generic_agent | try1 | 0.571429 | 0.444444 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 117.249000 | 26924 | 6 | 7 | 0.272959 |
| optiver-trading-at-the-close | tc1_from_scratch | generic_agent | try2 | 0.625000 | 0.555556 | 0.588235 | 1.000000 | 1.000000 | 1.000000 | 0.794118 | 0.794118 | `true` | 106.395000 | 24202 | 5 | 5 | 0.193121 |
| optiver-trading-at-the-close | tc1_from_scratch | generic_agent | try3 | 0.545455 | 0.333333 | 0.413793 | 1.000000 | 1.000000 | 1.000000 | 0.706897 | 0.706897 | `true` | 109.868000 | 21355 | 6 | 6 | 0.189221 |
| optiver-trading-at-the-close | tc1_from_scratch | generic_agent | try4 | 0.555556 | 0.277778 | 0.370370 | 1.000000 | 1.000000 | 1.000000 | 0.685185 | 0.685185 | `true` | 88.076000 | 20200 | 7 | 7 | 0.175701 |
| optiver-trading-at-the-close | tc1_from_scratch | generic_agent | try5 | 0.538462 | 0.388889 | 0.451613 | 1.000000 | 1.000000 | 1.000000 | 0.725807 | 0.725807 | `true` | 103.402000 | 19340 | 6 | 6 | 0.165186 |
| optiver-trading-at-the-close | tc1_from_scratch | human | human_tc1_sean_kraemer_v3_manual_rebuild | 1.000000 | 0.444444 | 0.615385 | 1.000000 | 1.000000 | 1.000000 | 0.807692 | 0.807692 | `true` | 2400 | `null` | `null` | `null` | `null` |
| optiver-trading-at-the-close | tc1_from_scratch | proposed_agent | try1 | 0.666667 | 0.555556 | 0.606061 | 1.000000 | 1.000000 | 1.000000 | 0.803030 | 0.803030 | `true` | 137.011000 | 35168 | 7 | 10 | 0.335371 |
| optiver-trading-at-the-close | tc1_from_scratch | proposed_agent | try2 | 0.785714 | 0.611111 | 0.687500 | 1.000000 | 1.000000 | 1.000000 | 0.843750 | 0.843750 | `true` | 146.013000 | 39478 | 8 | 11 | 0.294802 |
| optiver-trading-at-the-close | tc1_from_scratch | proposed_agent | try3 | 0.750000 | 0.333333 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 92.357000 | 19540 | 5 | 7 | 0.153153 |
| optiver-trading-at-the-close | tc1_from_scratch | proposed_agent | try4 | 0.555556 | 0.277778 | 0.370370 | 1.000000 | 1.000000 | 1.000000 | 0.685185 | 0.685185 | `true` | 117.427000 | 31284 | 6 | 9 | 0.222552 |
| optiver-trading-at-the-close | tc1_from_scratch | proposed_agent | try5 | 0.750000 | 0.333333 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 115.419000 | 33718 | 8 | 11 | 0.244525 |
| optiver-trading-at-the-close | tc1_from_scratch | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc1_from_scratch | single_llm | try1 | 0.615385 | 0.444444 | 0.516129 | 1.000000 | 1.000000 | 1.000000 | 0.758064 | 0.758064 | `true` | 18.763000 | 1157 | 1 | 0 | 0.075964 |
| optiver-trading-at-the-close | tc1_from_scratch | single_llm | try2 | 0.777778 | 0.388889 | 0.518519 | 1.000000 | 1.000000 | 1.000000 | 0.759259 | 0.759259 | `true` | 18.754000 | 1015 | 1 | 0 | 0.020055 |
| optiver-trading-at-the-close | tc1_from_scratch | single_llm | try3 | 0.600000 | 0.333333 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | `true` | 17.289000 | 901 | 1 | 0 | 0.018345 |
| optiver-trading-at-the-close | tc1_from_scratch | single_llm | try4 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 17.982000 | 1076 | 1 | 0 | 0.020970 |
| optiver-trading-at-the-close | tc1_from_scratch | single_llm | try5 | 0.600000 | 0.333333 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | `true` | 17.431000 | 1001 | 1 | 0 | 0.019845 |
| optiver-trading-at-the-close | tc2_partial_good | claude_code | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 52.484532 | 2495 | `null` | 10 | 0.221282 |
| optiver-trading-at-the-close | tc2_partial_good | claude_code | try2 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 66.162292 | 1519 | `null` | 24 | 0.262688 |
| optiver-trading-at-the-close | tc2_partial_good | claude_code | try3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 43.186049 | 2260 | `null` | 8 | 0.185823 |
| optiver-trading-at-the-close | tc2_partial_good | claude_code | try4 | 0.666667 | 0.142857 | 0.235294 | 0.000000 | 1.000000 | 0.000000 | 0.617647 | 0.117647 | `true` | 391.388065 | 2447 | `null` | 35 | 0.636463 |
| optiver-trading-at-the-close | tc2_partial_good | claude_code | try5 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 97.894922 | 2495 | `null` | 26 | 0.275009 |
| optiver-trading-at-the-close | tc2_partial_good | generic_agent | try1 | 0.400000 | 0.142857 | 0.210526 | 0.000000 | 1.000000 | 0.000000 | 0.605263 | 0.105263 | `true` | 158.127000 | 22121 | 6 | 7 | 0.175363 |
| optiver-trading-at-the-close | tc2_partial_good | generic_agent | try2 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 51.182000 | 9845 | 4 | 4 | 0.087099 |
| optiver-trading-at-the-close | tc2_partial_good | generic_agent | try3 | 0.666667 | 0.142857 | 0.235294 | 0.000000 | 1.000000 | 0.000000 | 0.617647 | 0.117647 | `true` | 93.418000 | 17020 | 5 | 5 | 0.138268 |
| optiver-trading-at-the-close | tc2_partial_good | generic_agent | try4 | 0.500000 | 0.071429 | 0.125000 | 0.000000 | 1.000000 | 0.000000 | 0.562500 | 0.062500 | `true` | 107.630000 | 23922 | 7 | 8 | 0.202494 |
| optiver-trading-at-the-close | tc2_partial_good | generic_agent | try5 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 56.551000 | 9493 | 4 | 4 | 0.088515 |
| optiver-trading-at-the-close | tc2_partial_good | proposed_agent | try1 | 0.800000 | 0.285714 | 0.421053 | 0.000000 | 1.000000 | 0.000000 | 0.710527 | 0.210527 | `true` | 138.337000 | 23335 | 5 | 6 | 0.189651 |
| optiver-trading-at-the-close | tc2_partial_good | proposed_agent | try2 | 0.800000 | 0.285714 | 0.421053 | 0.000000 | 1.000000 | 0.000000 | 0.710527 | 0.210527 | `true` | 154.774000 | 30343 | 6 | 8 | 0.235360 |
| optiver-trading-at-the-close | tc2_partial_good | proposed_agent | try3 | 0.800000 | 0.285714 | 0.421053 | 0.000000 | 1.000000 | 0.000000 | 0.710527 | 0.210527 | `true` | 131.906000 | 24553 | 6 | 7 | 0.199635 |
| optiver-trading-at-the-close | tc2_partial_good | proposed_agent | try4 | 0.750000 | 0.214286 | 0.333333 | 0.000000 | 1.000000 | 0.000000 | 0.666667 | 0.166666 | `true` | 126.006000 | 21412 | 5 | 6 | 0.172934 |
| optiver-trading-at-the-close | tc2_partial_good | proposed_agent | try5 | 1.000000 | 0.285714 | 0.444444 | 0.000000 | 1.000000 | 0.000000 | 0.722222 | 0.222222 | `true` | 126.223000 | 20730 | 5 | 5 | 0.173335 |
| optiver-trading-at-the-close | tc2_partial_good | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc2_partial_good | single_llm | try1 | 0.666667 | 0.142857 | 0.235294 | 0.000000 | 1.000000 | 0.000000 | 0.617647 | 0.117647 | `true` | 34.094000 | 2144 | 1 | 0 | 0.036131 |
| optiver-trading-at-the-close | tc2_partial_good | single_llm | try2 | 0.500000 | 0.142857 | 0.222222 | 0.000000 | 1.000000 | 0.000000 | 0.611111 | 0.111111 | `true` | 34.914000 | 2157 | 1 | 0 | 0.037271 |
| optiver-trading-at-the-close | tc2_partial_good | single_llm | try3 | 0.500000 | 0.142857 | 0.222222 | 0.000000 | 1.000000 | 0.000000 | 0.611111 | 0.111111 | `true` | 43.606000 | 2466 | 1 | 0 | 0.041906 |
| optiver-trading-at-the-close | tc2_partial_good | single_llm | try4 | 0.750000 | 0.214286 | 0.333333 | 0.000000 | 1.000000 | 0.000000 | 0.666667 | 0.166666 | `true` | 36.201000 | 2151 | 1 | 0 | 0.037181 |
| optiver-trading-at-the-close | tc2_partial_good | single_llm | try5 | 0.500000 | 0.142857 | 0.222222 | 0.000000 | 1.000000 | 0.000000 | 0.611111 | 0.111111 | `true` | 37.217000 | 2131 | 1 | 0 | 0.036881 |
| optiver-trading-at-the-close | tc3_fault_injected | claude_code | try1 | 1.000000 | 0.055556 | 0.105263 | 1.000000 | 0.500000 | 0.666667 | 0.302631 | 0.385965 | `false` | 89.982781 | 3020 | `null` | 22 | 0.248707 |
| optiver-trading-at-the-close | tc3_fault_injected | claude_code | try2 | 0.500000 | 0.055556 | 0.100000 | 1.000000 | 0.750000 | 0.857143 | 0.425000 | 0.478571 | `false` | 77.479131 | 2238 | `null` | 19 | 0.245911 |
| optiver-trading-at-the-close | tc3_fault_injected | claude_code | try3 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.500000 | 0.666667 | 0.250000 | 0.333334 | `false` | 211.847492 | 1520 | `null` | 31 | 0.621263 |
| optiver-trading-at-the-close | tc3_fault_injected | claude_code | try4 | 0.666667 | 0.111111 | 0.190476 | 1.000000 | 0.750000 | 0.857143 | 0.470238 | 0.523810 | `false` | 189.297474 | 2390 | `null` | 17 | 0.232044 |
| optiver-trading-at-the-close | tc3_fault_injected | claude_code | try5 | 0.666667 | 0.111111 | 0.190476 | 1.000000 | 0.500000 | 0.666667 | 0.345238 | 0.428571 | `false` | 85.704304 | 1406 | `null` | 22 | 0.191604 |
| optiver-trading-at-the-close | tc3_fault_injected | generic_agent | try1 | 0.750000 | 0.166667 | 0.272727 | 1.000000 | 0.750000 | 0.857143 | 0.511363 | 0.564935 | `true` | 98.555000 | 20624 | 5 | 6 | 0.159901 |
| optiver-trading-at-the-close | tc3_fault_injected | generic_agent | try2 | 0.600000 | 0.166667 | 0.260870 | 1.000000 | 0.500000 | 0.666667 | 0.380435 | 0.463769 | `false` | 114.337000 | 22899 | 5 | 5 | 0.181429 |
| optiver-trading-at-the-close | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.111111 | 0.200000 | 1.000000 | 0.250000 | 0.400000 | 0.225000 | 0.300000 | `false` | 79.283000 | 17035 | 5 | 6 | 0.141872 |
| optiver-trading-at-the-close | tc3_fault_injected | generic_agent | try4 | 0.500000 | 0.055556 | 0.100000 | 1.000000 | 0.250000 | 0.400000 | 0.175000 | 0.250000 | `false` | 112.158000 | 21651 | 6 | 6 | 0.177277 |
| optiver-trading-at-the-close | tc3_fault_injected | generic_agent | try5 | 0.666667 | 0.222222 | 0.333333 | 1.000000 | 0.500000 | 0.666667 | 0.416666 | 0.500000 | `false` | 87.529000 | 15297 | 4 | 4 | 0.133670 |
| optiver-trading-at-the-close | tc3_fault_injected | proposed_agent | try1 | 0.750000 | 0.166667 | 0.272727 | 1.000000 | 0.500000 | 0.666667 | 0.386363 | 0.469697 | `false` | 131.782000 | 24720 | 6 | 6 | 0.194754 |
| optiver-trading-at-the-close | tc3_fault_injected | proposed_agent | try2 | 1.000000 | 0.166667 | 0.285714 | 1.000000 | 0.250000 | 0.400000 | 0.267857 | 0.342857 | `false` | 162.575000 | 28789 | 6 | 6 | 0.218408 |
| optiver-trading-at-the-close | tc3_fault_injected | proposed_agent | try3 | 0.750000 | 0.166667 | 0.272727 | 1.000000 | 0.500000 | 0.666667 | 0.386363 | 0.469697 | `false` | 127.511000 | 20302 | 5 | 5 | 0.166688 |
| optiver-trading-at-the-close | tc3_fault_injected | proposed_agent | try4 | 0.800000 | 0.222222 | 0.347826 | 1.000000 | 0.500000 | 0.666667 | 0.423913 | 0.507247 | `false` | 150.320000 | 23905 | 5 | 5 | 0.193517 |
| optiver-trading-at-the-close | tc3_fault_injected | proposed_agent | try5 | 0.500000 | 0.111111 | 0.181818 | 1.000000 | 0.500000 | 0.666667 | 0.340909 | 0.424243 | `false` | 152.571000 | 28630 | 6 | 6 | 0.223296 |
| optiver-trading-at-the-close | tc3_fault_injected | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.111111 | 0.200000 | 1.000000 | 0.500000 | 0.666667 | 0.350000 | 0.433334 | `false` | 71.856000 | 3401 | 1 | 0 | 0.054962 |
| optiver-trading-at-the-close | tc3_fault_injected | single_llm | try2 | 0.750000 | 0.166667 | 0.272727 | 1.000000 | 0.500000 | 0.666667 | 0.386363 | 0.469697 | `false` | 38.417000 | 2132 | 1 | 0 | 0.036904 |
| optiver-trading-at-the-close | tc3_fault_injected | single_llm | try3 | 0.500000 | 0.055556 | 0.100000 | 1.000000 | 0.500000 | 0.666667 | 0.300000 | 0.383333 | `false` | 41.194000 | 2234 | 1 | 0 | 0.038434 |
| optiver-trading-at-the-close | tc3_fault_injected | single_llm | try4 | 0.666667 | 0.111111 | 0.190476 | 1.000000 | 0.500000 | 0.666667 | 0.345238 | 0.428571 | `false` | 38.689000 | 2230 | 1 | 0 | 0.038374 |
| optiver-trading-at-the-close | tc3_fault_injected | single_llm | try5 | 0.800000 | 0.222222 | 0.347826 | 1.000000 | 0.500000 | 0.666667 | 0.423913 | 0.507247 | `false` | 36.047000 | 2113 | 1 | 0 | 0.036619 |
| optiver-trading-at-the-close | tc4_mixed_history | claude_code | try1 | 0.500000 | 0.133333 | 0.210526 | 0.000000 | 0.000000 | 0.000000 | 0.105263 | 0.105263 | `false` | 118.836988 | 4019 | `null` | 25 | 0.339386 |
| optiver-trading-at-the-close | tc4_mixed_history | claude_code | try2 | 0.666667 | 0.133333 | 0.222222 | 0.000000 | 0.000000 | 0.000000 | 0.111111 | 0.111111 | `false` | 102.006234 | 5723 | `null` | 13 | 0.309138 |
| optiver-trading-at-the-close | tc4_mixed_history | claude_code | try3 | 0.333333 | 0.066667 | 0.111111 | 0.000000 | 0.000000 | 0.000000 | 0.055556 | 0.055556 | `false` | 93.978636 | 2467 | `null` | 13 | 0.242032 |
| optiver-trading-at-the-close | tc4_mixed_history | claude_code | try4 | 0.333333 | 0.066667 | 0.111111 | 0.000000 | 0.000000 | 0.000000 | 0.055556 | 0.055556 | `false` | 173.892692 | 5311 | `null` | 29 | 0.349986 |
| optiver-trading-at-the-close | tc4_mixed_history | claude_code | try5 | 0.500000 | 0.133333 | 0.210526 | 1.000000 | 0.333333 | 0.500000 | 0.271929 | 0.355263 | `false` | 99.601665 | 2157 | `null` | 22 | 0.219846 |
| optiver-trading-at-the-close | tc4_mixed_history | generic_agent | try1 | 0.750000 | 0.200000 | 0.315789 | 1.000000 | 0.333333 | 0.500000 | 0.324561 | 0.407894 | `false` | 87.628000 | 18948 | 5 | 5 | 0.149607 |
| optiver-trading-at-the-close | tc4_mixed_history | generic_agent | try2 | 0.666667 | 0.133333 | 0.222222 | 0.000000 | 0.000000 | 0.000000 | 0.111111 | 0.111111 | `false` | 111.816000 | 22587 | 5 | 5 | 0.179555 |
| optiver-trading-at-the-close | tc4_mixed_history | generic_agent | try3 | 0.666667 | 0.133333 | 0.222222 | 1.000000 | 0.333333 | 0.500000 | 0.277778 | 0.361111 | `false` | 98.221000 | 22490 | 6 | 6 | 0.178470 |
| optiver-trading-at-the-close | tc4_mixed_history | generic_agent | try4 | 0.333333 | 0.066667 | 0.111111 | 1.000000 | 0.333333 | 0.500000 | 0.222222 | 0.305555 | `false` | 109.684000 | 22408 | 6 | 6 | 0.181143 |
| optiver-trading-at-the-close | tc4_mixed_history | generic_agent | try5 | 0.500000 | 0.133333 | 0.210526 | 1.000000 | 0.333333 | 0.500000 | 0.271929 | 0.355263 | `false` | 101.099000 | 21179 | 5 | 7 | 0.167572 |
| optiver-trading-at-the-close | tc4_mixed_history | proposed_agent | try1 | 0.833333 | 0.333333 | 0.476190 | 1.000000 | 0.333333 | 0.500000 | 0.404761 | 0.488095 | `false` | 150.509000 | 19360 | 4 | 4 | 0.180835 |
| optiver-trading-at-the-close | tc4_mixed_history | proposed_agent | try2 | 0.750000 | 0.200000 | 0.315789 | 1.000000 | 0.666667 | 0.800000 | 0.491228 | 0.557894 | `false` | 180.881000 | 27777 | 5 | 6 | 0.231345 |
| optiver-trading-at-the-close | tc4_mixed_history | proposed_agent | try3 | 0.800000 | 0.266667 | 0.400000 | 0.000000 | 0.000000 | 0.000000 | 0.200000 | 0.200000 | `false` | 217.660000 | 40485 | 6 | 8 | 0.299298 |
| optiver-trading-at-the-close | tc4_mixed_history | proposed_agent | try4 | 0.750000 | 0.200000 | 0.315789 | 1.000000 | 0.666667 | 0.800000 | 0.491228 | 0.557894 | `false` | 130.127000 | 16974 | 4 | 3 | 0.162828 |
| optiver-trading-at-the-close | tc4_mixed_history | proposed_agent | try5 | 0.750000 | 0.200000 | 0.315789 | 1.000000 | 0.333333 | 0.500000 | 0.324561 | 0.407894 | `false` | 117.507000 | 22857 | 5 | 5 | 0.176732 |
| optiver-trading-at-the-close | tc4_mixed_history | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc4_mixed_history | single_llm | try1 | 0.666667 | 0.133333 | 0.222222 | 1.000000 | 0.333333 | 0.500000 | 0.277778 | 0.361111 | `false` | 49.520000 | 3027 | 1 | 0 | 0.049256 |
| optiver-trading-at-the-close | tc4_mixed_history | single_llm | try2 | 1.000000 | 0.133333 | 0.235294 | 1.000000 | 0.333333 | 0.500000 | 0.284313 | 0.367647 | `false` | 45.373000 | 2576 | 1 | 0 | 0.043594 |
| optiver-trading-at-the-close | tc4_mixed_history | single_llm | try3 | 1.000000 | 0.133333 | 0.235294 | 1.000000 | 0.333333 | 0.500000 | 0.284313 | 0.367647 | `false` | 47.907000 | 2838 | 1 | 0 | 0.047524 |
| optiver-trading-at-the-close | tc4_mixed_history | single_llm | try4 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 0.333333 | 0.500000 | 0.333333 | 0.416666 | `false` | 33.367000 | 1945 | 1 | 0 | 0.034129 |
| optiver-trading-at-the-close | tc4_mixed_history | single_llm | try5 | 0.666667 | 0.133333 | 0.222222 | 0.000000 | 0.000000 | 0.000000 | 0.111111 | 0.111111 | `false` | 60.639000 | 3508 | 1 | 0 | 0.057574 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| optiver-trading-at-the-close | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.556411 | 0.422222 | 0.479680 | 1.000000 | 1.000000 | 1.000000 | 0.739840 | 0.739840 | 0.001006 | 135.637178 | 3568.000000 | `null` | 19.000000 | 0.338643 |
| optiver-trading-at-the-close | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.567180 | 0.400000 | 0.464802 | 1.000000 | 1.000000 | 1.000000 | 0.732401 | 0.732401 | 0.001408 | 104.998000 | 22404.200000 | 6.000000 | 6.200000 | 0.199238 |
| optiver-trading-at-the-close | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 0.444444 | 0.615385 | 1.000000 | 1.000000 | 1.000000 | 0.807692 | 0.807692 | 0.000000 | 2400 | `null` | `null` | `null` | `null` |
| optiver-trading-at-the-close | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.701587 | 0.422222 | 0.517401 | 1.000000 | 1.000000 | 1.000000 | 0.758701 | 0.758701 | 0.003233 | 121.645400 | 31837.600000 | 6.800000 | 9.600000 | 0.250081 |
| optiver-trading-at-the-close | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.618633 | 0.366666 | 0.458358 | 1.000000 | 1.000000 | 1.000000 | 0.729179 | 0.729179 | 0.000607 | 18.043800 | 1030.000000 | 1.000000 | 0.000000 | 0.031036 |
| optiver-trading-at-the-close | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.133333 | 0.028571 | 0.047059 | 0.000000 | 1.000000 | 0.000000 | 0.523529 | 0.023529 | 0.002215 | 130.223172 | 2243.200000 | `null` | 20.600000 | 0.316253 |
| optiver-trading-at-the-close | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.313333 | 0.071429 | 0.114164 | 0.000000 | 1.000000 | 0.000000 | 0.557082 | 0.057082 | 0.002507 | 93.381600 | 16480.200000 | 5.200000 | 5.600000 | 0.138348 |
| optiver-trading-at-the-close | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.830000 | 0.271428 | 0.408187 | 0.000000 | 1.000000 | 0.000000 | 0.704094 | 0.204094 | 0.000371 | 135.449200 | 24074.600000 | 5.400000 | 6.400000 | 0.194183 |
| optiver-trading-at-the-close | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.583333 | 0.157143 | 0.247059 | 0.000000 | 1.000000 | 0.000000 | 0.623529 | 0.123529 | 0.000472 | 37.206400 | 2209.800000 | 1.000000 | 0.000000 | 0.037874 |
| optiver-trading-at-the-close | tc3_fault_injected | claude_code | 5 | `false` | 0.000000 | 0.566667 | 0.066667 | 0.117243 | 1.000000 | 0.600000 | 0.742857 | 0.358621 | 0.430050 | 0.006395 | 130.862237 | 2114.800000 | `null` | 22.200000 | 0.307906 |
| optiver-trading-at-the-close | tc3_fault_injected | generic_agent | 5 | `true` | 0.200000 | 0.703333 | 0.144445 | 0.233386 | 1.000000 | 0.450000 | 0.598095 | 0.341693 | 0.415741 | 0.015463 | 98.372400 | 19501.200000 | 5.000000 | 5.400000 | 0.158830 |
| optiver-trading-at-the-close | tc3_fault_injected | proposed_agent | 5 | `false` | 0.000000 | 0.760000 | 0.166667 | 0.272162 | 1.000000 | 0.450000 | 0.613334 | 0.361081 | 0.442748 | 0.002865 | 144.951800 | 25269.200000 | 5.600000 | 5.600000 | 0.199333 |
| optiver-trading-at-the-close | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc3_fault_injected | single_llm | 5 | `false` | 0.000000 | 0.743333 | 0.133333 | 0.222206 | 1.000000 | 0.500000 | 0.666667 | 0.361103 | 0.444436 | 0.001738 | 45.240600 | 2422.000000 | 1.000000 | 0.000000 | 0.041058 |
| optiver-trading-at-the-close | tc4_mixed_history | claude_code | 5 | `false` | 0.000000 | 0.466667 | 0.106667 | 0.173099 | 0.200000 | 0.066667 | 0.100000 | 0.119883 | 0.136550 | 0.006337 | 117.663243 | 3935.400000 | `null` | 20.400000 | 0.292078 |
| optiver-trading-at-the-close | tc4_mixed_history | generic_agent | 5 | `false` | 0.000000 | 0.583333 | 0.133333 | 0.216374 | 0.800000 | 0.266666 | 0.400000 | 0.241520 | 0.308187 | 0.005303 | 101.689600 | 21522.400000 | 5.400000 | 5.800000 | 0.171269 |
| optiver-trading-at-the-close | tc4_mixed_history | proposed_agent | 5 | `false` | 0.000000 | 0.776667 | 0.240000 | 0.364711 | 0.800000 | 0.400000 | 0.520000 | 0.382356 | 0.442355 | 0.012160 | 159.336800 | 25490.600000 | 4.800000 | 5.200000 | 0.210208 |
| optiver-trading-at-the-close | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| optiver-trading-at-the-close | tc4_mixed_history | single_llm | 5 | `false` | 0.000000 | 0.866667 | 0.146666 | 0.249673 | 0.800000 | 0.266666 | 0.400000 | 0.258170 | 0.324836 | 0.005805 | 47.361200 | 2778.800000 | 1.000000 | 0.000000 | 0.046415 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 0.500000 | 5.000000 | 0.500000 | 0.430770 | 0.156032 | 0.204270 | 0.550000 | 0.666667 | 0.460714 | 0.435468 | 0.332492 | 0.003988 | 128.596457 | 2965.350000 | `null` | 20.550000 | 0.313720 |
| generic_agent | 4 | 0.750000 | 5.000000 | 0.550000 | 0.541795 | 0.187302 | 0.257182 | 0.700000 | 0.679167 | 0.499524 | 0.468174 | 0.378353 | 0.006170 | 99.610400 | 19977.000000 | 5.400000 | 5.750000 | 0.166921 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.444444 | 0.615385 | 1.000000 | 1.000000 | 1.000000 | 0.807692 | 0.807692 | 0.000000 | 2400.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 0.500000 | 5.000000 | 0.500000 | 0.767064 | 0.275079 | 0.390615 | 0.700000 | 0.712500 | 0.533334 | 0.551558 | 0.461974 | 0.004657 | 140.345800 | 26668.000000 | 5.650000 | 6.700000 | 0.213451 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.000000 | 0.000000 | 0.000000 | 0.250000 | 0.500000 | 0.250000 | 0.250000 | 0.125000 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 0.500000 | 5.000000 | 0.500000 | 0.702991 | 0.200952 | 0.294324 | 0.700000 | 0.691666 | 0.516667 | 0.492995 | 0.405495 | 0.002155 | 36.963000 | 2110.150000 | 1.000000 | 0.000000 | 0.039096 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task optiver-trading-at-the-close --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/optiver-trading-at-the-close-all.md
```
