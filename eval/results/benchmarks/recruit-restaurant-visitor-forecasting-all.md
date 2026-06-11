# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `recruit-restaurant-visitor-forecasting`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.904762`
- Mean Add Precision: `0.645197`
- Mean Add Recall: `0.325660`
- Mean Add F1: `0.410773`
- Mean Remove Precision: `0.901587`
- Mean Remove Recall: `0.888095`
- Mean Remove F1: `0.846893`
- Mean Task Completion Score: `0.649434`
- Mean Strict Task Completion Score: `0.628833`
- Mean Task Completion Variance: `0.004263`
- Mean Runtime (s): `158.428864`
- Mean Total Tokens: `14326.462500`
- Mean API Calls: `3.225000`
- Mean Tool Calls: `4.660000`
- Mean Cost (USD): `0.147001`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| recruit-restaurant-visitor-forecasting | Root Mean Squared Logarithmic Error | restaurant_demand_forecasting | forecasting | multi_table_relational | xlarge (2000320) | low (17) | medium (12) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| recruit-restaurant-visitor-forecasting | 21 | 6 | 0.904762 | 4.047619 | 0.645197 | 0.325660 | 0.410773 | 0.901587 | 0.888095 | 0.846893 | 0.649434 | 0.628833 | 0.004263 | 158.428864 | 14326.462500 | 3.225000 | 4.660000 | 0.147001 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | claude_code | try1 | 0.625000 | 0.526316 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 289.291951 | 15503 | `null` | 9 | 0.432549 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | claude_code | try2 | 0.714286 | 0.526316 | 0.606061 | 1.000000 | 1.000000 | 1.000000 | 0.803030 | 0.803030 | `true` | 161.509115 | 9741 | `null` | 8 | 0.309897 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | claude_code | try3 | 0.642857 | 0.473684 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 120.763950 | 7110 | `null` | 6 | 0.250689 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | claude_code | try4 | 0.687500 | 0.578947 | 0.628571 | 1.000000 | 1.000000 | 1.000000 | 0.814285 | 0.814285 | `true` | 195.883446 | 11780 | `null` | 10 | 0.349928 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | claude_code | try5 | 0.666667 | 0.526316 | 0.588235 | 1.000000 | 1.000000 | 1.000000 | 0.794118 | 0.794118 | `true` | 135.736286 | 8390 | `null` | 8 | 0.273403 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | generic_agent | try1 | 0.642857 | 0.473684 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 101.995000 | 23510 | 6 | 6 | 0.229012 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | generic_agent | try2 | 0.666667 | 0.421053 | 0.516129 | 1.000000 | 1.000000 | 1.000000 | 0.758064 | 0.758064 | `true` | 96.134000 | 22352 | 6 | 6 | 0.216084 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | generic_agent | try3 | 0.600000 | 0.473684 | 0.529412 | 1.000000 | 1.000000 | 1.000000 | 0.764706 | 0.764706 | `true` | 83.020000 | 21001 | 5 | 5 | 0.186775 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | generic_agent | try4 | 0.571429 | 0.421053 | 0.484848 | 1.000000 | 1.000000 | 1.000000 | 0.742424 | 0.742424 | `true` | 122.984000 | 28504 | 7 | 7 | 0.266843 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | generic_agent | try5 | 0.600000 | 0.473684 | 0.529412 | 1.000000 | 1.000000 | 1.000000 | 0.764706 | 0.764706 | `true` | 100.787000 | 27069 | 6 | 6 | 0.243337 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | human | human_tc1_annotator_a_v1 | 0.565217 | 0.684211 | 0.619048 | 1.000000 | 1.000000 | 1.000000 | 0.809524 | 0.809524 | `true` | 1800 | `null` | `null` | `null` | `null` |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | proposed_agent | try1 | 0.642857 | 0.473684 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 82.902000 | 16790 | 5 | 5 | 0.195529 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | proposed_agent | try2 | 0.714286 | 0.526316 | 0.606061 | 1.000000 | 1.000000 | 1.000000 | 0.803030 | 0.803030 | `true` | 82.219000 | 19836 | 5 | 5 | 0.216491 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | proposed_agent | try3 | 0.642857 | 0.473684 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 88.153000 | 20255 | 5 | 6 | 0.169055 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | proposed_agent | try4 | 0.785714 | 0.578947 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 107.549000 | 27137 | 6 | 7 | 0.265676 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | proposed_agent | try5 | 0.846154 | 0.578947 | 0.687500 | 1.000000 | 1.000000 | 1.000000 | 0.843750 | 0.843750 | `true` | 142.671000 | 39278 | 6 | 9 | 0.325373 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | rule_based | try1 | 0.333333 | 0.105263 | 0.160000 | 1.000000 | 1.000000 | 1.000000 | 0.580000 | 0.580000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | single_llm | try1 | 0.785714 | 0.578947 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 64.942000 | 3414 | 1 | 0 | 0.108113 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | single_llm | try2 | 0.687500 | 0.578947 | 0.628571 | 1.000000 | 1.000000 | 1.000000 | 0.814285 | 0.814285 | `true` | 16.187000 | 1087 | 1 | 0 | 0.020245 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | single_llm | try3 | 0.647059 | 0.578947 | 0.611111 | 1.000000 | 1.000000 | 1.000000 | 0.805555 | 0.805555 | `true` | 16.359000 | 1058 | 1 | 0 | 0.020393 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | single_llm | try4 | 0.666667 | 0.631579 | 0.648649 | 1.000000 | 1.000000 | 1.000000 | 0.824325 | 0.824325 | `true` | 58.352000 | 4345 | 1 | 0 | 0.069698 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | single_llm | try5 | 0.647059 | 0.578947 | 0.611111 | 1.000000 | 1.000000 | 1.000000 | 0.805555 | 0.805555 | `true` | 14.714000 | 999 | 1 | 0 | 0.019508 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | claude_code | try1 | 0.714286 | 0.333333 | 0.454545 | 1.000000 | 1.000000 | 1.000000 | 0.727272 | 0.727272 | `true` | 141.999925 | 9128 | `null` | 12 | 0.307338 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | claude_code | try2 | 0.800000 | 0.266667 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 116.540355 | 6596 | `null` | 8 | 0.252881 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | claude_code | try3 | 0.714286 | 0.333333 | 0.454545 | 1.000000 | 1.000000 | 1.000000 | 0.727272 | 0.727272 | `true` | 105.991590 | 6874 | `null` | 8 | 0.247084 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | claude_code | try4 | 0.750000 | 0.200000 | 0.315789 | 1.000000 | 1.000000 | 1.000000 | 0.657895 | 0.657895 | `true` | 118.203231 | 6901 | `null` | 9 | 0.265691 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | claude_code | try5 | 0.714286 | 0.333333 | 0.454545 | 1.000000 | 1.000000 | 1.000000 | 0.727272 | 0.727272 | `true` | 97.529769 | 5520 | `null` | 5 | 0.220279 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | generic_agent | try1 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 98.838000 | 24404 | 6 | 7 | 0.192247 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | generic_agent | try2 | 0.666667 | 0.266667 | 0.380952 | 1.000000 | 1.000000 | 1.000000 | 0.690476 | 0.690476 | `true` | 72.115000 | 12413 | 4 | 4 | 0.110386 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | generic_agent | try3 | 0.666667 | 0.266667 | 0.380952 | 1.000000 | 1.000000 | 1.000000 | 0.690476 | 0.690476 | `true` | 63.835000 | 11005 | 4 | 4 | 0.132954 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | generic_agent | try4 | 0.666667 | 0.266667 | 0.380952 | 1.000000 | 1.000000 | 1.000000 | 0.690476 | 0.690476 | `true` | 75.610000 | 16832 | 6 | 6 | 0.144896 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | generic_agent | try5 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 101.346000 | 23244 | 6 | 7 | 0.189078 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | proposed_agent | try1 | 0.714286 | 0.333333 | 0.454545 | 1.000000 | 1.000000 | 1.000000 | 0.727272 | 0.727272 | `true` | 73.231000 | 14048 | 4 | 3 | 0.117305 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | proposed_agent | try2 | 0.625000 | 0.333333 | 0.434783 | 0.000000 | 1.000000 | 0.000000 | 0.717391 | 0.217391 | `true` | 130.281000 | 24147 | 5 | 6 | 0.196074 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | proposed_agent | try3 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 89.311000 | 22377 | 6 | 9 | 0.181663 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | proposed_agent | try4 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 129.141000 | 33340 | 8 | 11 | 0.277563 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | proposed_agent | try5 | 0.714286 | 0.333333 | 0.454545 | 0.000000 | 1.000000 | 0.000000 | 0.727272 | 0.227272 | `true` | 121.331000 | 23849 | 6 | 9 | 0.198392 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | single_llm | try1 | 0.875000 | 0.466667 | 0.608696 | 1.000000 | 1.000000 | 1.000000 | 0.804348 | 0.804348 | `true` | 44.309000 | 3137 | 1 | 0 | 0.101555 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | single_llm | try2 | 0.750000 | 0.400000 | 0.521739 | 1.000000 | 1.000000 | 1.000000 | 0.760869 | 0.760869 | `true` | 42.730000 | 2919 | 1 | 0 | 0.048395 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | single_llm | try3 | 0.750000 | 0.400000 | 0.521739 | 1.000000 | 1.000000 | 1.000000 | 0.760869 | 0.760869 | `true` | 33.273000 | 2375 | 1 | 0 | 0.040235 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | single_llm | try4 | 0.875000 | 0.466667 | 0.608696 | 1.000000 | 1.000000 | 1.000000 | 0.804348 | 0.804348 | `true` | 44.230000 | 3027 | 1 | 0 | 0.050015 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | single_llm | try5 | 0.857143 | 0.400000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 35.582000 | 2540 | 1 | 0 | 0.042710 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | claude_code | try1 | 1.000000 | 0.157895 | 0.272727 | 1.000000 | 1.000000 | 1.000000 | 0.636363 | 0.636363 | `true` | 94.732466 | 5904 | `null` | 8 | 0.224314 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | claude_code | try2 | 1.000000 | 0.105263 | 0.190476 | 1.000000 | 0.750000 | 0.857143 | 0.470238 | 0.523810 | `false` | 132.214104 | 7144 | `null` | 9 | 0.273080 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | claude_code | try3 | 1.000000 | 0.105263 | 0.190476 | 1.000000 | 0.750000 | 0.857143 | 0.470238 | 0.523810 | `false` | 76.898475 | 4897 | `null` | 8 | 0.208013 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | claude_code | try4 | 1.000000 | 0.157895 | 0.272727 | 1.000000 | 1.000000 | 1.000000 | 0.636363 | 0.636363 | `true` | 68.272223 | 4664 | `null` | 10 | 0.215665 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | claude_code | try5 | 1.000000 | 0.157895 | 0.272727 | 1.000000 | 0.750000 | 0.857143 | 0.511363 | 0.564935 | `true` | 129.681846 | 6739 | `null` | 9 | 0.263434 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.157895 | 0.272727 | 1.000000 | 1.000000 | 1.000000 | 0.636363 | 0.636363 | `true` | 69.736000 | 15285 | 5 | 5 | 0.121214 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | generic_agent | try2 | 1.000000 | 0.263158 | 0.416667 | 1.000000 | 1.000000 | 1.000000 | 0.708333 | 0.708333 | `true` | 63.889000 | 11905 | 4 | 4 | 0.101769 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | generic_agent | try3 | 0.857143 | 0.315789 | 0.461538 | 1.000000 | 0.750000 | 0.857143 | 0.605769 | 0.659340 | `true` | 73.018000 | 17636 | 5 | 5 | 0.133521 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | generic_agent | try4 | 1.000000 | 0.210526 | 0.347826 | 1.000000 | 1.000000 | 1.000000 | 0.673913 | 0.673913 | `true` | 76.417000 | 19007 | 5 | 5 | 0.140056 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | generic_agent | try5 | 1.000000 | 0.157895 | 0.272727 | 1.000000 | 0.750000 | 0.857143 | 0.511363 | 0.564935 | `true` | 70.371000 | 15892 | 5 | 5 | 0.124068 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | proposed_agent | try1 | 0.700000 | 0.368421 | 0.482759 | 1.000000 | 0.500000 | 0.666667 | 0.491379 | 0.574713 | `false` | 136.017000 | 28307 | 7 | 11 | 0.235595 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | proposed_agent | try2 | 0.750000 | 0.315789 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 93.396000 | 21287 | 6 | 9 | 0.181632 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | proposed_agent | try3 | 0.666667 | 0.210526 | 0.320000 | 1.000000 | 0.250000 | 0.400000 | 0.285000 | 0.360000 | `false` | 130.993000 | 26077 | 7 | 9 | 0.224237 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | proposed_agent | try4 | 0.909091 | 0.526316 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 107.100000 | 26288 | 7 | 10 | 0.242117 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | proposed_agent | try5 | 0.800000 | 0.421053 | 0.551724 | 1.000000 | 0.500000 | 0.666667 | 0.525862 | 0.609196 | `true` | 144.924000 | 30500 | 8 | 11 | 0.262311 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | rule_based | try1 | 0.400000 | 0.105263 | 0.166667 | 1.000000 | 0.500000 | 0.666667 | 0.333334 | 0.416667 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.157895 | 0.272727 | 1.000000 | 1.000000 | 1.000000 | 0.636363 | 0.636363 | `true` | 36.476000 | 2557 | 1 | 0 | 0.041995 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | single_llm | try2 | 1.000000 | 0.473684 | 0.642857 | 1.000000 | 0.750000 | 0.857143 | 0.696429 | 0.750000 | `true` | 53.476000 | 3740 | 1 | 0 | 0.060717 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | single_llm | try3 | 0.900000 | 0.473684 | 0.620690 | 1.000000 | 0.750000 | 0.857143 | 0.685345 | 0.738916 | `true` | 41.770000 | 2675 | 1 | 0 | 0.044742 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | single_llm | try4 | 1.000000 | 0.368421 | 0.538462 | 1.000000 | 1.000000 | 1.000000 | 0.769231 | 0.769231 | `true` | 37.569000 | 2833 | 1 | 0 | 0.047112 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | single_llm | try5 | 1.000000 | 0.526316 | 0.689655 | 1.000000 | 0.750000 | 0.857143 | 0.719828 | 0.773399 | `true` | 43.364000 | 3017 | 1 | 0 | 0.049872 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | claude_code | try1 | 0.750000 | 0.230769 | 0.352941 | 1.000000 | 1.000000 | 1.000000 | 0.676470 | 0.676470 | `true` | 149.299471 | 9344 | `null` | 10 | 0.309194 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | claude_code | try2 | 0.750000 | 0.230769 | 0.352941 | 1.000000 | 0.500000 | 0.666667 | 0.426470 | 0.509804 | `false` | 205.928197 | 11453 | `null` | 12 | 0.390309 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | claude_code | try3 | 0.800000 | 0.307692 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 149.609697 | 10112 | `null` | 12 | 0.341432 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | claude_code | try4 | 0.714286 | 0.384615 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 141.463129 | 8386 | `null` | 12 | 0.297181 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | claude_code | try5 | 0.833333 | 0.384615 | 0.526316 | 1.000000 | 1.000000 | 1.000000 | 0.763158 | 0.763158 | `true` | 172.426485 | 11803 | `null` | 13 | 0.393248 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | generic_agent | try1 | 0.833333 | 0.384615 | 0.526316 | 1.000000 | 1.000000 | 1.000000 | 0.763158 | 0.763158 | `true` | 88.423000 | 19820 | 6 | 6 | 0.159835 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | generic_agent | try2 | 0.714286 | 0.384615 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 67.192000 | 18316 | 5 | 5 | 0.130790 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | generic_agent | try3 | 0.666667 | 0.307692 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 104.690000 | 26719 | 8 | 8 | 0.212521 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | generic_agent | try4 | 0.666667 | 0.307692 | 0.421053 | 1.000000 | 0.500000 | 0.666667 | 0.460527 | 0.543860 | `false` | 110.103000 | 27029 | 7 | 7 | 0.213752 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | generic_agent | try5 | 0.800000 | 0.307692 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 114.380000 | 27690 | 8 | 9 | 0.232718 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | proposed_agent | try1 | 0.500000 | 0.230769 | 0.315789 | 1.000000 | 0.500000 | 0.666667 | 0.407894 | 0.491228 | `false` | 137.540000 | 36524 | 8 | 12 | 0.270106 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | proposed_agent | try2 | 0.500000 | 0.230769 | 0.315789 | 1.000000 | 1.000000 | 1.000000 | 0.657895 | 0.657895 | `true` | 91.035000 | 21322 | 6 | 9 | 0.170625 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | proposed_agent | try3 | 0.600000 | 0.230769 | 0.333333 | 1.000000 | 0.500000 | 0.666667 | 0.416666 | 0.500000 | `false` | 131.227000 | 24565 | 5 | 4 | 0.195696 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | proposed_agent | try4 | 0.500000 | 0.230769 | 0.315789 | 1.000000 | 0.500000 | 0.666667 | 0.407894 | 0.491228 | `false` | 159.282000 | 30562 | 7 | 9 | 0.261529 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | proposed_agent | try5 | 0.800000 | 0.307692 | 0.444444 | 1.000000 | 0.500000 | 0.666667 | 0.472222 | 0.555555 | `false` | 130.324000 | 29802 | 7 | 9 | 0.230979 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.333333 | 0.500000 | 0.400000 | 0.250000 | 0.200000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | single_llm | try1 | 0.857143 | 0.461538 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 34.871000 | 2484 | 1 | 0 | 0.040661 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | single_llm | try2 | 0.857143 | 0.461538 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 38.987000 | 2686 | 1 | 0 | 0.044982 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | single_llm | try3 | 0.833333 | 0.384615 | 0.526316 | 1.000000 | 1.000000 | 1.000000 | 0.763158 | 0.763158 | `true` | 38.907000 | 2412 | 1 | 0 | 0.040872 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | single_llm | try4 | 0.857143 | 0.461538 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 36.959000 | 2497 | 1 | 0 | 0.042147 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | single_llm | try5 | 0.833333 | 0.384615 | 0.526316 | 1.000000 | 1.000000 | 1.000000 | 0.763158 | 0.763158 | `true` | 34.488000 | 2402 | 1 | 0 | 0.040722 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.667262 | 0.526316 | 0.587950 | 1.000000 | 1.000000 | 1.000000 | 0.793975 | 0.793975 | 0.000203 | 180.636950 | 10504.800000 | `null` | 8.200000 | 0.323293 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.616191 | 0.452632 | 0.521051 | 1.000000 | 1.000000 | 1.000000 | 0.760526 | 0.760526 | 0.000104 | 100.984000 | 24487.200000 | 6.000000 | 6.000000 | 0.228410 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | human | 1 | `true` | 1.000000 | 0.565217 | 0.684211 | 0.619048 | 1.000000 | 1.000000 | 1.000000 | 0.809524 | 0.809524 | 0.000000 | 1800 | `null` | `null` | `null` | `null` |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.726374 | 0.526316 | 0.610228 | 1.000000 | 1.000000 | 1.000000 | 0.805114 | 0.805114 | 0.000878 | 100.698800 | 24659.200000 | 5.400000 | 6.400000 | 0.234425 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.333333 | 0.105263 | 0.160000 | 1.000000 | 1.000000 | 1.000000 | 0.580000 | 0.580000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.686800 | 0.589473 | 0.633222 | 1.000000 | 1.000000 | 1.000000 | 0.816611 | 0.816611 | 0.000118 | 34.110800 | 2180.600000 | 1.000000 | 0.000000 | 0.047592 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.738572 | 0.293333 | 0.415885 | 1.000000 | 1.000000 | 1.000000 | 0.707942 | 0.707942 | 0.000738 | 116.052974 | 7003.800000 | `null` | 8.400000 | 0.258654 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.666667 | 0.320000 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | 0.000850 | 82.348800 | 17579.600000 | 5.200000 | 5.600000 | 0.153912 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.677381 | 0.360000 | 0.468775 | 0.600000 | 1.000000 | 0.600000 | 0.734387 | 0.534387 | 0.000176 | 108.659000 | 23552.200000 | 5.800000 | 7.600000 | 0.194199 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.821429 | 0.426667 | 0.561265 | 1.000000 | 1.000000 | 1.000000 | 0.780632 | 0.780632 | 0.000394 | 40.024800 | 2799.600000 | 1.000000 | 0.000000 | 0.056582 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | claude_code | 5 | `true` | 0.600000 | 1.000000 | 0.136842 | 0.239827 | 1.000000 | 0.850000 | 0.914286 | 0.544913 | 0.577056 | 0.005801 | 100.359823 | 5869.600000 | `null` | 8.800000 | 0.236901 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 0.971429 | 0.221053 | 0.354297 | 1.000000 | 0.900000 | 0.942857 | 0.627148 | 0.648577 | 0.004545 | 70.686200 | 15945.000000 | 4.800000 | 4.800000 | 0.124125 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | proposed_agent | 5 | `true` | 0.600000 | 0.765152 | 0.368421 | 0.493119 | 1.000000 | 0.650000 | 0.746667 | 0.571559 | 0.619893 | 0.036372 | 122.486000 | 26491.800000 | 7.000000 | 10.000000 | 0.229178 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.400000 | 0.105263 | 0.166667 | 1.000000 | 0.500000 | 0.666667 | 0.333334 | 0.416667 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 0.980000 | 0.400000 | 0.552878 | 1.000000 | 0.850000 | 0.914286 | 0.701439 | 0.733582 | 0.001891 | 42.531000 | 2964.400000 | 1.000000 | 0.000000 | 0.048888 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | claude_code | 5 | `true` | 0.800000 | 0.769524 | 0.307692 | 0.435328 | 1.000000 | 0.900000 | 0.933333 | 0.667664 | 0.684331 | 0.015425 | 163.745396 | 10219.600000 | `null` | 11.800000 | 0.346273 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | generic_agent | 5 | `true` | 0.800000 | 0.736191 | 0.338461 | 0.462573 | 1.000000 | 0.900000 | 0.933333 | 0.681287 | 0.697953 | 0.012538 | 96.957600 | 23914.800000 | 6.800000 | 7.000000 | 0.189923 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | proposed_agent | 5 | `true` | 0.200000 | 0.580000 | 0.246154 | 0.345029 | 1.000000 | 0.600000 | 0.733334 | 0.472514 | 0.539181 | 0.009167 | 129.881600 | 28555.000000 | 6.600000 | 8.600000 | 0.225787 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.333333 | 0.500000 | 0.400000 | 0.250000 | 0.200000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 0.847619 | 0.430769 | 0.570526 | 1.000000 | 1.000000 | 1.000000 | 0.785263 | 0.785263 | 0.000326 | 36.842400 | 2496.200000 | 1.000000 | 0.000000 | 0.041877 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 0.850000 | 0.793840 | 0.316046 | 0.419747 | 1.000000 | 0.937500 | 0.961905 | 0.678624 | 0.690826 | 0.005542 | 140.198786 | 8399.450000 | `null` | 9.300000 | 0.291280 |
| generic_agent | 4 | 1.000000 | 5.000000 | 0.950000 | 0.747619 | 0.333037 | 0.441623 | 1.000000 | 0.950000 | 0.969047 | 0.695812 | 0.705336 | 0.004509 | 87.744150 | 20481.650000 | 5.700000 | 5.850000 | 0.174093 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 0.565217 | 0.684211 | 0.619048 | 1.000000 | 1.000000 | 1.000000 | 0.809524 | 0.809524 | 0.000000 | 1800.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 0.700000 | 0.687227 | 0.375223 | 0.479288 | 0.900000 | 0.812500 | 0.770000 | 0.645894 | 0.624644 | 0.011648 | 115.431350 | 25814.550000 | 6.200000 | 8.150000 | 0.220897 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.183333 | 0.052631 | 0.081667 | 0.583333 | 0.750000 | 0.516667 | 0.415833 | 0.299167 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 0.833962 | 0.461727 | 0.579473 | 1.000000 | 0.962500 | 0.978572 | 0.770986 | 0.779022 | 0.000682 | 38.377250 | 2610.200000 | 1.000000 | 0.000000 | 0.048735 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task recruit-restaurant-visitor-forecasting --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/recruit-restaurant-visitor-forecasting-all.md
```
