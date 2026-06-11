# Benchmark Aggregate Report

## Configuration

- Stage scope: `primary`
- Success threshold: `0.5`
- Tasks included: `recruit-restaurant-visitor-forecasting`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.904762`
- Mean Add Precision: `0.826587`
- Mean Add Recall: `0.532937`
- Mean Add F1: `0.628183`
- Mean Remove Precision: `0.892063`
- Mean Remove Recall: `0.884127`
- Mean Remove F1: `0.841905`
- Mean Task Completion Score: `0.756155`
- Mean Strict Task Completion Score: `0.735044`
- Mean Task Completion Variance: `0.006101`
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
| recruit-restaurant-visitor-forecasting | 21 | 6 | 0.904762 | 4.047619 | 0.826587 | 0.532937 | 0.628183 | 0.892063 | 0.884127 | 0.841905 | 0.756155 | 0.735044 | 0.006101 | 158.428864 | 14326.462500 | 3.225000 | 4.660000 | 0.147001 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | claude_code | try1 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 289.291951 | 15503 | `null` | 9 | 0.432549 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | claude_code | try2 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 161.509115 | 9741 | `null` | 8 | 0.309897 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | claude_code | try3 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 120.763950 | 7110 | `null` | 6 | 0.250689 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | claude_code | try4 | 1.000000 | 0.916667 | 0.956522 | 1.000000 | 1.000000 | 1.000000 | 0.978261 | 0.978261 | `true` | 195.883446 | 11780 | `null` | 10 | 0.349928 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | claude_code | try5 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 135.736286 | 8390 | `null` | 8 | 0.273403 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | generic_agent | try1 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 101.995000 | 23510 | 6 | 6 | 0.229012 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | generic_agent | try2 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 96.134000 | 22352 | 6 | 6 | 0.216084 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | generic_agent | try3 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 83.020000 | 21001 | 5 | 5 | 0.186775 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | generic_agent | try4 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 122.984000 | 28504 | 7 | 7 | 0.266843 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | generic_agent | try5 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 100.787000 | 27069 | 6 | 6 | 0.243337 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | human | human_tc1_annotator_a_v1 | 0.625000 | 0.833333 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 1800 | `null` | `null` | `null` | `null` |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | proposed_agent | try1 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 82.902000 | 16790 | 5 | 5 | 0.195529 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | proposed_agent | try2 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 82.219000 | 19836 | 5 | 5 | 0.216491 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | proposed_agent | try3 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 88.153000 | 20255 | 5 | 6 | 0.169055 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | proposed_agent | try4 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 107.549000 | 27137 | 6 | 7 | 0.265676 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | proposed_agent | try5 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 142.671000 | 39278 | 6 | 9 | 0.325373 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | rule_based | try1 | 0.333333 | 0.166667 | 0.222222 | 1.000000 | 1.000000 | 1.000000 | 0.611111 | 0.611111 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | single_llm | try1 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 64.942000 | 3414 | 1 | 0 | 0.108113 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | single_llm | try2 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 16.187000 | 1087 | 1 | 0 | 0.020245 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | single_llm | try3 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 16.359000 | 1058 | 1 | 0 | 0.020393 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | single_llm | try4 | 1.000000 | 0.916667 | 0.956522 | 1.000000 | 1.000000 | 1.000000 | 0.978261 | 0.978261 | `true` | 58.352000 | 4345 | 1 | 0 | 0.069698 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | single_llm | try5 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 14.714000 | 999 | 1 | 0 | 0.019508 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | claude_code | try1 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 141.999925 | 9128 | `null` | 12 | 0.307338 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | claude_code | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 116.540355 | 6596 | `null` | 8 | 0.252881 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | claude_code | try3 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 105.991590 | 6874 | `null` | 8 | 0.247084 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | claude_code | try4 | 1.000000 | 0.375000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 118.203231 | 6901 | `null` | 9 | 0.265691 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | claude_code | try5 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 97.529769 | 5520 | `null` | 5 | 0.220279 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | generic_agent | try1 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 98.838000 | 24404 | 6 | 7 | 0.192247 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | generic_agent | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 72.115000 | 12413 | 4 | 4 | 0.110386 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | generic_agent | try3 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 63.835000 | 11005 | 4 | 4 | 0.132954 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | generic_agent | try4 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 75.610000 | 16832 | 6 | 6 | 0.144896 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | generic_agent | try5 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 101.346000 | 23244 | 6 | 7 | 0.189078 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | proposed_agent | try1 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 73.231000 | 14048 | 4 | 3 | 0.117305 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | proposed_agent | try2 | 1.000000 | 0.625000 | 0.769231 | 0.000000 | 1.000000 | 0.000000 | 0.884615 | 0.384615 | `true` | 130.281000 | 24147 | 5 | 6 | 0.196074 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | proposed_agent | try3 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 89.311000 | 22377 | 6 | 9 | 0.181663 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | proposed_agent | try4 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 129.141000 | 33340 | 8 | 11 | 0.277563 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | proposed_agent | try5 | 1.000000 | 0.500000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 121.331000 | 23849 | 6 | 9 | 0.198392 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | single_llm | try1 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 44.309000 | 3137 | 1 | 0 | 0.101555 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | single_llm | try2 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 42.730000 | 2919 | 1 | 0 | 0.048395 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | single_llm | try3 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 33.273000 | 2375 | 1 | 0 | 0.040235 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | single_llm | try4 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 44.230000 | 3027 | 1 | 0 | 0.050015 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | single_llm | try5 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 35.582000 | 2540 | 1 | 0 | 0.042710 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | claude_code | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 94.732466 | 5904 | `null` | 8 | 0.224314 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | claude_code | try2 | 1.000000 | 0.166667 | 0.285714 | 1.000000 | 0.666667 | 0.800000 | 0.476191 | 0.542857 | `false` | 132.214104 | 7144 | `null` | 9 | 0.273080 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | claude_code | try3 | 1.000000 | 0.166667 | 0.285714 | 1.000000 | 0.666667 | 0.800000 | 0.476191 | 0.542857 | `false` | 76.898475 | 4897 | `null` | 8 | 0.208013 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | claude_code | try4 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 68.272223 | 4664 | `null` | 10 | 0.215665 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | claude_code | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 0.666667 | 0.800000 | 0.533334 | 0.600000 | `true` | 129.681846 | 6739 | `null` | 9 | 0.263434 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 69.736000 | 15285 | 5 | 5 | 0.121214 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | generic_agent | try2 | 1.000000 | 0.416667 | 0.588235 | 1.000000 | 1.000000 | 1.000000 | 0.794118 | 0.794118 | `true` | 63.889000 | 11905 | 4 | 4 | 0.101769 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.666667 | 0.800000 | 0.666667 | 0.733334 | `true` | 73.018000 | 17636 | 5 | 5 | 0.133521 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | generic_agent | try4 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 76.417000 | 19007 | 5 | 5 | 0.140056 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | generic_agent | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 0.666667 | 0.800000 | 0.533334 | 0.600000 | `true` | 70.371000 | 15892 | 5 | 5 | 0.124068 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | proposed_agent | try1 | 1.000000 | 0.583333 | 0.736842 | 1.000000 | 0.333333 | 0.500000 | 0.535087 | 0.618421 | `true` | 136.017000 | 28307 | 7 | 11 | 0.235595 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | proposed_agent | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 93.396000 | 21287 | 6 | 9 | 0.181632 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | proposed_agent | try3 | 1.000000 | 0.333333 | 0.500000 | 0.000000 | 0.000000 | 0.000000 | 0.250000 | 0.250000 | `false` | 130.993000 | 26077 | 7 | 9 | 0.224237 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | proposed_agent | try4 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 107.100000 | 26288 | 7 | 10 | 0.242117 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | proposed_agent | try5 | 1.000000 | 0.583333 | 0.736842 | 1.000000 | 0.333333 | 0.500000 | 0.535087 | 0.618421 | `true` | 144.924000 | 30500 | 8 | 11 | 0.262311 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | rule_based | try1 | 0.400000 | 0.166667 | 0.235294 | 1.000000 | 0.666667 | 0.800000 | 0.450981 | 0.517647 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 36.476000 | 2557 | 1 | 0 | 0.041995 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | single_llm | try2 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.666667 | 0.800000 | 0.733334 | 0.800000 | `true` | 53.476000 | 3740 | 1 | 0 | 0.060717 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | single_llm | try3 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.666667 | 0.800000 | 0.733334 | 0.800000 | `true` | 41.770000 | 2675 | 1 | 0 | 0.044742 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | single_llm | try4 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 37.569000 | 2833 | 1 | 0 | 0.047112 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | single_llm | try5 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 0.666667 | 0.800000 | 0.761905 | 0.828572 | `true` | 43.364000 | 3017 | 1 | 0 | 0.049872 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | claude_code | try1 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 149.299471 | 9344 | `null` | 10 | 0.309194 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | claude_code | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.500000 | 0.666667 | 0.583333 | 0.666667 | `true` | 205.928197 | 11453 | `null` | 12 | 0.390309 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | claude_code | try3 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 149.609697 | 10112 | `null` | 12 | 0.341432 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | claude_code | try4 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 141.463129 | 8386 | `null` | 12 | 0.297181 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | claude_code | try5 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 172.426485 | 11803 | `null` | 13 | 0.393248 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | generic_agent | try1 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 88.423000 | 19820 | 6 | 6 | 0.159835 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | generic_agent | try2 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 67.192000 | 18316 | 5 | 5 | 0.130790 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | generic_agent | try3 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 104.690000 | 26719 | 8 | 8 | 0.212521 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | generic_agent | try4 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 110.103000 | 27029 | 7 | 7 | 0.213752 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | generic_agent | try5 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 114.380000 | 27690 | 8 | 9 | 0.232718 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | proposed_agent | try1 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.500000 | 0.666667 | 0.583333 | 0.666667 | `true` | 137.540000 | 36524 | 8 | 12 | 0.270106 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | proposed_agent | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 91.035000 | 21322 | 6 | 9 | 0.170625 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | proposed_agent | try3 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.500000 | 0.666667 | 0.583333 | 0.666667 | `true` | 131.227000 | 24565 | 5 | 4 | 0.195696 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | proposed_agent | try4 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.500000 | 0.666667 | 0.583333 | 0.666667 | `true` | 159.282000 | 30562 | 7 | 9 | 0.261529 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | proposed_agent | try5 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.500000 | 0.666667 | 0.583333 | 0.666667 | `true` | 130.324000 | 29802 | 7 | 9 | 0.230979 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.333333 | 0.500000 | 0.400000 | 0.250000 | 0.200000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | single_llm | try1 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 34.871000 | 2484 | 1 | 0 | 0.040661 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | single_llm | try2 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 38.987000 | 2686 | 1 | 0 | 0.044982 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | single_llm | try3 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 38.907000 | 2412 | 1 | 0 | 0.040872 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | single_llm | try4 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 36.959000 | 2497 | 1 | 0 | 0.042147 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | single_llm | try5 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 34.488000 | 2402 | 1 | 0 | 0.040722 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.833333 | 0.908188 | 1.000000 | 1.000000 | 1.000000 | 0.954094 | 0.954094 | 0.000247 | 180.636950 | 10504.800000 | `null` | 8.200000 | 0.323293 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.716667 | 0.834286 | 1.000000 | 1.000000 | 1.000000 | 0.917143 | 0.917143 | 0.000196 | 100.984000 | 24487.200000 | 6.000000 | 6.000000 | 0.228410 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | human | 1 | `true` | 1.000000 | 0.625000 | 0.833333 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | 0.000000 | 1800 | `null` | `null` | `null` | `null` |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.800000 | 0.888312 | 1.000000 | 1.000000 | 1.000000 | 0.944156 | 0.944156 | 0.000162 | 100.698800 | 24659.200000 | 5.400000 | 6.400000 | 0.234425 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.333333 | 0.166667 | 0.222222 | 1.000000 | 1.000000 | 1.000000 | 0.611111 | 0.611111 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.850000 | 0.918577 | 1.000000 | 1.000000 | 1.000000 | 0.959289 | 0.959289 | 0.000090 | 34.110800 | 2180.600000 | 1.000000 | 0.000000 | 0.047592 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.550000 | 0.703963 | 1.000000 | 1.000000 | 1.000000 | 0.851981 | 0.851981 | 0.001965 | 116.052974 | 7003.800000 | `null` | 8.400000 | 0.258654 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.600000 | 0.742857 | 1.000000 | 1.000000 | 1.000000 | 0.871428 | 0.871428 | 0.002177 | 82.348800 | 17579.600000 | 5.200000 | 5.600000 | 0.153912 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.650000 | 0.783883 | 0.600000 | 1.000000 | 0.600000 | 0.891941 | 0.691941 | 0.001245 | 108.659000 | 23552.200000 | 5.800000 | 7.600000 | 0.194199 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.675000 | 0.804396 | 1.000000 | 1.000000 | 1.000000 | 0.902197 | 0.902197 | 0.000464 | 40.024800 | 2799.600000 | 1.000000 | 0.000000 | 0.056582 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | claude_code | 5 | `true` | 0.600000 | 1.000000 | 0.216667 | 0.354286 | 1.000000 | 0.800000 | 0.880000 | 0.577143 | 0.617143 | 0.010498 | 100.359823 | 5869.600000 | `null` | 8.800000 | 0.236901 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.350000 | 0.510980 | 1.000000 | 0.866667 | 0.920000 | 0.688824 | 0.715490 | 0.007924 | 70.686200 | 15945.000000 | 4.800000 | 4.800000 | 0.124125 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | proposed_agent | 5 | `true` | 0.800000 | 1.000000 | 0.550000 | 0.699499 | 0.800000 | 0.533333 | 0.600000 | 0.616416 | 0.649749 | 0.058397 | 122.486000 | 26491.800000 | 7.000000 | 10.000000 | 0.229178 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.400000 | 0.166667 | 0.235294 | 1.000000 | 0.666667 | 0.800000 | 0.450981 | 0.517647 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.566667 | 0.704762 | 1.000000 | 0.800000 | 0.880000 | 0.752381 | 0.792381 | 0.002023 | 42.531000 | 2964.400000 | 1.000000 | 0.000000 | 0.048888 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.666667 | 0.790303 | 1.000000 | 0.900000 | 0.933333 | 0.845152 | 0.861818 | 0.019126 | 163.745396 | 10219.600000 | `null` | 11.800000 | 0.346273 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.733333 | 0.843636 | 1.000000 | 0.900000 | 0.933333 | 0.871818 | 0.888485 | 0.012896 | 96.957600 | 23914.800000 | 6.800000 | 7.000000 | 0.189923 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.600000 | 0.733334 | 0.633333 | 0.700000 | 0.010000 | 129.881600 | 28555.000000 | 6.600000 | 8.600000 | 0.225787 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.333333 | 0.500000 | 0.400000 | 0.250000 | 0.200000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| recruit-restaurant-visitor-forecasting | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.766667 | 0.865455 | 1.000000 | 1.000000 | 1.000000 | 0.932728 | 0.932728 | 0.000714 | 36.842400 | 2496.200000 | 1.000000 | 0.000000 | 0.041877 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 0.900000 | 1.000000 | 0.566667 | 0.689185 | 1.000000 | 0.925000 | 0.953333 | 0.807092 | 0.821259 | 0.007959 | 140.198786 | 8399.450000 | `null` | 9.300000 | 0.291280 |
| generic_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 1.000000 | 0.600000 | 0.732940 | 1.000000 | 0.941667 | 0.963333 | 0.837303 | 0.848136 | 0.005798 | 87.744150 | 20481.650000 | 5.700000 | 5.850000 | 0.174093 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 0.625000 | 0.833333 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | 0.000000 | 1800.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 0.950000 | 1.000000 | 0.625000 | 0.759590 | 0.850000 | 0.783333 | 0.733333 | 0.771462 | 0.746462 | 0.017451 | 115.431350 | 25814.550000 | 6.200000 | 8.150000 | 0.220897 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.183333 | 0.083334 | 0.114379 | 0.583333 | 0.791667 | 0.550000 | 0.453023 | 0.332189 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 1.000000 | 0.714584 | 0.823298 | 1.000000 | 0.950000 | 0.970000 | 0.886649 | 0.896649 | 0.000823 | 38.377250 | 2610.200000 | 1.000000 | 0.000000 | 0.048735 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task recruit-restaurant-visitor-forecasting --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/recruit-restaurant-visitor-forecasting-primary.md
```
