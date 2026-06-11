# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `sberbank-russian-housing-market`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.666667`
- Mean Add Precision: `0.499439`
- Mean Add Recall: `0.324037`
- Mean Add F1: `0.360765`
- Mean Remove Precision: `0.952381`
- Mean Remove Recall: `0.745397`
- Mean Remove F1: `0.806311`
- Mean Task Completion Score: `0.553081`
- Mean Strict Task Completion Score: `0.583538`
- Mean Task Completion Variance: `0.000928`
- Mean Runtime (s): `176.395620`
- Mean Total Tokens: `19358.637500`
- Mean API Calls: `4.025000`
- Mean Tool Calls: `6.270000`
- Mean Cost (USD): `0.199553`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sberbank-russian-housing-market | Root Mean Squared Logarithmic Error | real_estate_tabular | regression | multi_table_lookup | small (30471) | high (391) | high (22) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sberbank-russian-housing-market | 21 | 6 | 0.666667 | 4.047619 | 0.499439 | 0.324037 | 0.360765 | 0.952381 | 0.745397 | 0.806311 | 0.553081 | 0.583538 | 0.000928 | 176.395620 | 19358.637500 | 4.025000 | 6.270000 | 0.199553 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sberbank-russian-housing-market | tc1_from_scratch | claude_code | try1 | 0.576923 | 0.681818 | 0.625000 | 1.000000 | 1.000000 | 1.000000 | 0.812500 | 0.812500 | `true` | 296.442135 | 17465 | `null` | 13 | 0.511221 |
| sberbank-russian-housing-market | tc1_from_scratch | claude_code | try2 | 0.448276 | 0.590909 | 0.509804 | 1.000000 | 1.000000 | 1.000000 | 0.754902 | 0.754902 | `true` | 234.639215 | 13428 | `null` | 9 | 0.413091 |
| sberbank-russian-housing-market | tc1_from_scratch | claude_code | try3 | 0.457143 | 0.727273 | 0.561404 | 1.000000 | 1.000000 | 1.000000 | 0.780702 | 0.780702 | `true` | 220.029293 | 12256 | `null` | 12 | 0.416591 |
| sberbank-russian-housing-market | tc1_from_scratch | claude_code | try4 | 0.464286 | 0.590909 | 0.520000 | 1.000000 | 1.000000 | 1.000000 | 0.760000 | 0.760000 | `true` | 173.136836 | 12331 | `null` | 11 | 0.415343 |
| sberbank-russian-housing-market | tc1_from_scratch | claude_code | try5 | 0.435897 | 0.772727 | 0.557377 | 1.000000 | 1.000000 | 1.000000 | 0.778689 | 0.778689 | `true` | 256.733251 | 15289 | `null` | 10 | 0.452498 |
| sberbank-russian-housing-market | tc1_from_scratch | generic_agent | try1 | 0.583333 | 0.636364 | 0.608696 | 1.000000 | 1.000000 | 1.000000 | 0.804348 | 0.804348 | `true` | 144.607000 | 37499 | 7 | 9 | 0.337155 |
| sberbank-russian-housing-market | tc1_from_scratch | generic_agent | try2 | 0.434783 | 0.454545 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 147.066000 | 32985 | 8 | 9 | 0.325646 |
| sberbank-russian-housing-market | tc1_from_scratch | generic_agent | try3 | 0.482759 | 0.636364 | 0.549020 | 1.000000 | 1.000000 | 1.000000 | 0.774510 | 0.774510 | `true` | 138.479000 | 31779 | 9 | 9 | 0.320849 |
| sberbank-russian-housing-market | tc1_from_scratch | generic_agent | try4 | 0.500000 | 0.545455 | 0.521739 | 1.000000 | 1.000000 | 1.000000 | 0.760869 | 0.760869 | `true` | 116.070000 | 29415 | 9 | 9 | 0.298970 |
| sberbank-russian-housing-market | tc1_from_scratch | generic_agent | try5 | 0.576923 | 0.681818 | 0.625000 | 1.000000 | 1.000000 | 1.000000 | 0.812500 | 0.812500 | `true` | 124.744000 | 31309 | 6 | 6 | 0.289423 |
| sberbank-russian-housing-market | tc1_from_scratch | human | human_tc1_annotator_a_working_v1 | 0.451613 | 0.636364 | 0.528302 | 1.000000 | 1.000000 | 1.000000 | 0.764151 | 0.764151 | `true` | 1800 | `null` | `null` | `null` | `null` |
| sberbank-russian-housing-market | tc1_from_scratch | proposed_agent | try1 | 0.541667 | 0.590909 | 0.565217 | 1.000000 | 1.000000 | 1.000000 | 0.782609 | 0.782609 | `true` | 186.662000 | 42849 | 6 | 7 | 0.382506 |
| sberbank-russian-housing-market | tc1_from_scratch | proposed_agent | try2 | 0.592593 | 0.727273 | 0.653061 | 1.000000 | 1.000000 | 1.000000 | 0.826531 | 0.826531 | `true` | 237.371000 | 58503 | 8 | 11 | 0.537231 |
| sberbank-russian-housing-market | tc1_from_scratch | proposed_agent | try3 | 0.541667 | 0.590909 | 0.565217 | 1.000000 | 1.000000 | 1.000000 | 0.782609 | 0.782609 | `true` | 139.834000 | 25520 | 5 | 6 | 0.288126 |
| sberbank-russian-housing-market | tc1_from_scratch | proposed_agent | try4 | 0.481481 | 0.590909 | 0.530612 | 1.000000 | 1.000000 | 1.000000 | 0.765306 | 0.765306 | `true` | 143.725000 | 36613 | 6 | 7 | 0.338862 |
| sberbank-russian-housing-market | tc1_from_scratch | proposed_agent | try5 | 0.636364 | 0.636364 | 0.636364 | 1.000000 | 1.000000 | 1.000000 | 0.818182 | 0.818182 | `true` | 126.535000 | 32636 | 6 | 7 | 0.341529 |
| sberbank-russian-housing-market | tc1_from_scratch | rule_based | try1 | 0.250000 | 0.181818 | 0.210526 | 1.000000 | 1.000000 | 1.000000 | 0.605263 | 0.605263 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc1_from_scratch | single_llm | try1 | 0.590909 | 0.590909 | 0.590909 | 1.000000 | 1.000000 | 1.000000 | 0.795454 | 0.795454 | `true` | 105.423000 | 5128 | 1 | 0 | 0.685219 |
| sberbank-russian-housing-market | tc1_from_scratch | single_llm | try2 | 0.550000 | 0.500000 | 0.523810 | 1.000000 | 1.000000 | 1.000000 | 0.761905 | 0.761905 | `true` | 25.080000 | 1449 | 1 | 0 | 0.028352 |
| sberbank-russian-housing-market | tc1_from_scratch | single_llm | try3 | 0.481481 | 0.590909 | 0.530612 | 1.000000 | 1.000000 | 1.000000 | 0.765306 | 0.765306 | `true` | 32.578000 | 1801 | 1 | 0 | 0.034215 |
| sberbank-russian-housing-market | tc1_from_scratch | single_llm | try4 | 0.480000 | 0.545455 | 0.510638 | 1.000000 | 1.000000 | 1.000000 | 0.755319 | 0.755319 | `true` | 26.048000 | 1546 | 1 | 0 | 0.030390 |
| sberbank-russian-housing-market | tc1_from_scratch | single_llm | try5 | 0.541667 | 0.590909 | 0.565217 | 1.000000 | 1.000000 | 1.000000 | 0.782609 | 0.782609 | `true` | 28.793000 | 1601 | 1 | 0 | 0.031215 |
| sberbank-russian-housing-market | tc2_partial_good | claude_code | try1 | 0.750000 | 0.157895 | 0.260870 | 1.000000 | 1.000000 | 1.000000 | 0.630435 | 0.630435 | `true` | 163.242124 | 9532 | `null` | 29 | 0.437061 |
| sberbank-russian-housing-market | tc2_partial_good | claude_code | try2 | 0.666667 | 0.210526 | 0.320000 | 1.000000 | 1.000000 | 1.000000 | 0.660000 | 0.660000 | `true` | 130.803618 | 7104 | `null` | 12 | 0.321231 |
| sberbank-russian-housing-market | tc2_partial_good | claude_code | try3 | 0.833333 | 0.263158 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 200.154153 | 12450 | `null` | 16 | 0.451736 |
| sberbank-russian-housing-market | tc2_partial_good | claude_code | try4 | 0.500000 | 0.052632 | 0.095238 | 1.000000 | 1.000000 | 1.000000 | 0.547619 | 0.547619 | `true` | 101.894445 | 5422 | `null` | 10 | 0.251996 |
| sberbank-russian-housing-market | tc2_partial_good | claude_code | try5 | 0.666667 | 0.210526 | 0.320000 | 1.000000 | 1.000000 | 1.000000 | 0.660000 | 0.660000 | `true` | 129.778211 | 6301 | `null` | 10 | 0.268630 |
| sberbank-russian-housing-market | tc2_partial_good | generic_agent | try1 | 0.625000 | 0.263158 | 0.370370 | 1.000000 | 1.000000 | 1.000000 | 0.685185 | 0.685185 | `true` | 95.455000 | 22996 | 8 | 9 | 0.192706 |
| sberbank-russian-housing-market | tc2_partial_good | generic_agent | try2 | 0.500000 | 0.210526 | 0.296296 | 1.000000 | 1.000000 | 1.000000 | 0.648148 | 0.648148 | `true` | 109.953000 | 35448 | 7 | 7 | 0.239866 |
| sberbank-russian-housing-market | tc2_partial_good | generic_agent | try3 | 0.428571 | 0.315789 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 109.061000 | 23938 | 10 | 10 | 0.215500 |
| sberbank-russian-housing-market | tc2_partial_good | generic_agent | try4 | 0.600000 | 0.315789 | 0.413793 | 1.000000 | 1.000000 | 1.000000 | 0.706897 | 0.706897 | `true` | 152.984000 | 38811 | 8 | 11 | 0.310130 |
| sberbank-russian-housing-market | tc2_partial_good | generic_agent | try5 | 0.500000 | 0.368421 | 0.424242 | 1.000000 | 1.000000 | 1.000000 | 0.712121 | 0.712121 | `true` | 122.338000 | 30233 | 8 | 9 | 0.242619 |
| sberbank-russian-housing-market | tc2_partial_good | proposed_agent | try1 | 0.600000 | 0.473684 | 0.529412 | 1.000000 | 1.000000 | 1.000000 | 0.764706 | 0.764706 | `true` | 146.586000 | 40909 | 8 | 14 | 0.332667 |
| sberbank-russian-housing-market | tc2_partial_good | proposed_agent | try2 | 0.500000 | 0.368421 | 0.424242 | 1.000000 | 1.000000 | 1.000000 | 0.712121 | 0.712121 | `true` | 119.175000 | 37191 | 9 | 13 | 0.393845 |
| sberbank-russian-housing-market | tc2_partial_good | proposed_agent | try3 | 0.533333 | 0.421053 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | `true` | 137.259000 | 39323 | 9 | 13 | 0.320295 |
| sberbank-russian-housing-market | tc2_partial_good | proposed_agent | try4 | 0.583333 | 0.368421 | 0.451613 | 1.000000 | 1.000000 | 1.000000 | 0.725807 | 0.725807 | `true` | 137.658000 | 34279 | 7 | 10 | 0.291198 |
| sberbank-russian-housing-market | tc2_partial_good | proposed_agent | try5 | 0.533333 | 0.421053 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | `true` | 148.808000 | 38065 | 8 | 12 | 0.338580 |
| sberbank-russian-housing-market | tc2_partial_good | rule_based | try1 | 0.250000 | 0.210526 | 0.228571 | 1.000000 | 1.000000 | 1.000000 | 0.614286 | 0.614286 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc2_partial_good | single_llm | try1 | 0.538462 | 0.368421 | 0.437500 | 1.000000 | 1.000000 | 1.000000 | 0.718750 | 0.718750 | `true` | 86.881000 | 3840 | 1 | 0 | 0.145626 |
| sberbank-russian-housing-market | tc2_partial_good | single_llm | try2 | 0.571429 | 0.421053 | 0.484848 | 1.000000 | 1.000000 | 1.000000 | 0.742424 | 0.742424 | `true` | 44.708000 | 2678 | 1 | 0 | 0.047433 |
| sberbank-russian-housing-market | tc2_partial_good | single_llm | try3 | 0.583333 | 0.368421 | 0.451613 | 1.000000 | 1.000000 | 1.000000 | 0.725807 | 0.725807 | `true` | 53.448000 | 3114 | 1 | 0 | 0.053973 |
| sberbank-russian-housing-market | tc2_partial_good | single_llm | try4 | 0.545455 | 0.315789 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 56.383000 | 3211 | 1 | 0 | 0.055428 |
| sberbank-russian-housing-market | tc2_partial_good | single_llm | try5 | 0.533333 | 0.421053 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | `true` | 54.638000 | 3509 | 1 | 0 | 0.059898 |
| sberbank-russian-housing-market | tc3_fault_injected | claude_code | try1 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.800000 | 0.888889 | 0.400000 | 0.444445 | `false` | 131.655427 | 8513 | `null` | 15 | 0.339169 |
| sberbank-russian-housing-market | tc3_fault_injected | claude_code | try2 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.800000 | 0.888889 | 0.400000 | 0.444445 | `false` | 120.696645 | 7683 | `null` | 9 | 0.287164 |
| sberbank-russian-housing-market | tc3_fault_injected | claude_code | try3 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.800000 | 0.888889 | 0.400000 | 0.444445 | `false` | 89.961321 | 5387 | `null` | 9 | 0.238735 |
| sberbank-russian-housing-market | tc3_fault_injected | claude_code | try4 | 0.500000 | 0.045455 | 0.083333 | 1.000000 | 0.600000 | 0.750000 | 0.341666 | 0.416666 | `false` | 98.956329 | 5647 | `null` | 10 | 0.266242 |
| sberbank-russian-housing-market | tc3_fault_injected | claude_code | try5 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.800000 | 0.888889 | 0.400000 | 0.444445 | `false` | 111.022158 | 6942 | `null` | 8 | 0.289267 |
| sberbank-russian-housing-market | tc3_fault_injected | generic_agent | try1 | 0.500000 | 0.045455 | 0.083333 | 1.000000 | 0.600000 | 0.750000 | 0.341666 | 0.416666 | `false` | 76.189000 | 17210 | 6 | 7 | 0.142628 |
| sberbank-russian-housing-market | tc3_fault_injected | generic_agent | try2 | 0.666667 | 0.181818 | 0.285714 | 1.000000 | 0.800000 | 0.888889 | 0.542857 | 0.587302 | `true` | 103.482000 | 22535 | 7 | 7 | 0.237481 |
| sberbank-russian-housing-market | tc3_fault_injected | generic_agent | try3 | 0.750000 | 0.136364 | 0.230769 | 1.000000 | 0.800000 | 0.888889 | 0.515385 | 0.559829 | `true` | 118.364000 | 29219 | 9 | 10 | 0.244526 |
| sberbank-russian-housing-market | tc3_fault_injected | generic_agent | try4 | 0.600000 | 0.272727 | 0.375000 | 1.000000 | 0.800000 | 0.888889 | 0.587500 | 0.631945 | `true` | 93.948000 | 21434 | 6 | 6 | 0.178097 |
| sberbank-russian-housing-market | tc3_fault_injected | generic_agent | try5 | 0.666667 | 0.181818 | 0.285714 | 1.000000 | 0.800000 | 0.888889 | 0.542857 | 0.587302 | `true` | 89.492000 | 20084 | 6 | 7 | 0.167663 |
| sberbank-russian-housing-market | tc3_fault_injected | proposed_agent | try1 | 0.545455 | 0.272727 | 0.363636 | 1.000000 | 0.600000 | 0.750000 | 0.481818 | 0.556818 | `false` | 177.537000 | 38637 | 8 | 12 | 0.330410 |
| sberbank-russian-housing-market | tc3_fault_injected | proposed_agent | try2 | 0.750000 | 0.272727 | 0.400000 | 1.000000 | 0.600000 | 0.750000 | 0.500000 | 0.575000 | `true` | 161.611000 | 30806 | 6 | 6 | 0.255951 |
| sberbank-russian-housing-market | tc3_fault_injected | proposed_agent | try3 | 0.636364 | 0.318182 | 0.424242 | 1.000000 | 0.600000 | 0.750000 | 0.512121 | 0.587121 | `true` | 184.604000 | 44570 | 9 | 13 | 0.365975 |
| sberbank-russian-housing-market | tc3_fault_injected | proposed_agent | try4 | 0.727273 | 0.363636 | 0.484848 | 1.000000 | 0.600000 | 0.750000 | 0.542424 | 0.617424 | `true` | 204.115000 | 47182 | 9 | 13 | 0.405370 |
| sberbank-russian-housing-market | tc3_fault_injected | proposed_agent | try5 | 0.714286 | 0.227273 | 0.344828 | 1.000000 | 0.600000 | 0.750000 | 0.472414 | 0.547414 | `false` | 146.849000 | 29893 | 6 | 9 | 0.249333 |
| sberbank-russian-housing-market | tc3_fault_injected | rule_based | try1 | 0.250000 | 0.181818 | 0.210526 | 1.000000 | 0.400000 | 0.571429 | 0.305263 | 0.390977 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc3_fault_injected | single_llm | try1 | 0.750000 | 0.409091 | 0.529412 | 1.000000 | 0.800000 | 0.888889 | 0.664706 | 0.709151 | `true` | 59.715000 | 3655 | 1 | 0 | 0.061070 |
| sberbank-russian-housing-market | tc3_fault_injected | single_llm | try2 | 0.500000 | 0.272727 | 0.352941 | 1.000000 | 0.800000 | 0.888889 | 0.576470 | 0.620915 | `true` | 53.055000 | 3128 | 1 | 0 | 0.054236 |
| sberbank-russian-housing-market | tc3_fault_injected | single_llm | try3 | 0.571429 | 0.363636 | 0.444444 | 1.000000 | 0.800000 | 0.888889 | 0.622222 | 0.666667 | `true` | 50.389000 | 2849 | 1 | 0 | 0.050051 |
| sberbank-russian-housing-market | tc3_fault_injected | single_llm | try4 | 0.583333 | 0.318182 | 0.411765 | 1.000000 | 0.800000 | 0.888889 | 0.605882 | 0.650327 | `true` | 51.332000 | 3138 | 1 | 0 | 0.054386 |
| sberbank-russian-housing-market | tc3_fault_injected | single_llm | try5 | 0.625000 | 0.227273 | 0.333333 | 1.000000 | 0.800000 | 0.888889 | 0.566666 | 0.611111 | `true` | 45.875000 | 2735 | 1 | 0 | 0.048341 |
| sberbank-russian-housing-market | tc4_mixed_history | claude_code | try1 | 0.800000 | 0.210526 | 0.333333 | 1.000000 | 0.333333 | 0.500000 | 0.333333 | 0.416666 | `false` | 209.605267 | 7781 | `null` | 16 | 0.373590 |
| sberbank-russian-housing-market | tc4_mixed_history | claude_code | try2 | 0.666667 | 0.105263 | 0.181818 | 1.000000 | 0.333333 | 0.500000 | 0.257576 | 0.340909 | `false` | 90.155250 | 5887 | `null` | 10 | 0.280481 |
| sberbank-russian-housing-market | tc4_mixed_history | claude_code | try3 | 0.666667 | 0.105263 | 0.181818 | 1.000000 | 0.333333 | 0.500000 | 0.257576 | 0.340909 | `false` | 101.153108 | 5441 | `null` | 10 | 0.252417 |
| sberbank-russian-housing-market | tc4_mixed_history | claude_code | try4 | 0.666667 | 0.105263 | 0.181818 | 1.000000 | 0.333333 | 0.500000 | 0.257576 | 0.340909 | `false` | 78.756942 | 4627 | `null` | 8 | 0.223890 |
| sberbank-russian-housing-market | tc4_mixed_history | claude_code | try5 | 0.666667 | 0.105263 | 0.181818 | 1.000000 | 0.333333 | 0.500000 | 0.257576 | 0.340909 | `false` | 123.125340 | 7161 | `null` | 13 | 0.306478 |
| sberbank-russian-housing-market | tc4_mixed_history | generic_agent | try1 | 0.800000 | 0.210526 | 0.333333 | 1.000000 | 0.333333 | 0.500000 | 0.333333 | 0.416666 | `false` | 88.976000 | 20762 | 6 | 8 | 0.168946 |
| sberbank-russian-housing-market | tc4_mixed_history | generic_agent | try2 | 0.666667 | 0.105263 | 0.181818 | 1.000000 | 0.333333 | 0.500000 | 0.257576 | 0.340909 | `false` | 64.729000 | 14219 | 5 | 5 | 0.114342 |
| sberbank-russian-housing-market | tc4_mixed_history | generic_agent | try3 | 0.666667 | 0.210526 | 0.320000 | 1.000000 | 0.333333 | 0.500000 | 0.326666 | 0.410000 | `false` | 95.247000 | 22343 | 9 | 10 | 0.198254 |
| sberbank-russian-housing-market | tc4_mixed_history | generic_agent | try4 | 0.666667 | 0.105263 | 0.181818 | 1.000000 | 0.333333 | 0.500000 | 0.257576 | 0.340909 | `false` | 90.132000 | 21359 | 7 | 7 | 0.174573 |
| sberbank-russian-housing-market | tc4_mixed_history | generic_agent | try5 | 0.750000 | 0.157895 | 0.260870 | 1.000000 | 0.333333 | 0.500000 | 0.297102 | 0.380435 | `false` | 84.571000 | 17232 | 6 | 6 | 0.151569 |
| sberbank-russian-housing-market | tc4_mixed_history | proposed_agent | try1 | 0.600000 | 0.315789 | 0.413793 | 1.000000 | 0.333333 | 0.500000 | 0.373563 | 0.456897 | `false` | 180.054000 | 39092 | 8 | 15 | 0.313195 |
| sberbank-russian-housing-market | tc4_mixed_history | proposed_agent | try2 | 0.583333 | 0.368421 | 0.451613 | 1.000000 | 0.333333 | 0.500000 | 0.392473 | 0.475807 | `false` | 175.805000 | 41633 | 8 | 11 | 0.323769 |
| sberbank-russian-housing-market | tc4_mixed_history | proposed_agent | try3 | 0.666667 | 0.421053 | 0.516129 | 1.000000 | 0.333333 | 0.500000 | 0.424731 | 0.508064 | `false` | 180.057000 | 49400 | 9 | 16 | 0.393815 |
| sberbank-russian-housing-market | tc4_mixed_history | proposed_agent | try4 | 0.500000 | 0.210526 | 0.296296 | 1.000000 | 0.333333 | 0.500000 | 0.314814 | 0.398148 | `false` | 171.228000 | 43524 | 10 | 15 | 0.354070 |
| sberbank-russian-housing-market | tc4_mixed_history | proposed_agent | try5 | 0.625000 | 0.263158 | 0.370370 | 1.000000 | 0.333333 | 0.500000 | 0.351851 | 0.435185 | `false` | 179.404000 | 43670 | 10 | 16 | 0.372110 |
| sberbank-russian-housing-market | tc4_mixed_history | rule_based | try1 | 0.214286 | 0.157895 | 0.181818 | 0.000000 | 0.000000 | 0.000000 | 0.090909 | 0.090909 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc4_mixed_history | single_llm | try1 | 0.700000 | 0.368421 | 0.482759 | 1.000000 | 0.333333 | 0.500000 | 0.408046 | 0.491379 | `false` | 48.973000 | 2982 | 1 | 0 | 0.050951 |
| sberbank-russian-housing-market | tc4_mixed_history | single_llm | try2 | 0.666667 | 0.315789 | 0.428571 | 1.000000 | 0.333333 | 0.500000 | 0.380952 | 0.464286 | `false` | 44.665000 | 2550 | 1 | 0 | 0.045573 |
| sberbank-russian-housing-market | tc4_mixed_history | single_llm | try3 | 0.666667 | 0.421053 | 0.516129 | 1.000000 | 0.333333 | 0.500000 | 0.424731 | 0.508064 | `false` | 46.977000 | 2706 | 1 | 0 | 0.047913 |
| sberbank-russian-housing-market | tc4_mixed_history | single_llm | try4 | 0.714286 | 0.263158 | 0.384615 | 1.000000 | 0.333333 | 0.500000 | 0.358974 | 0.442307 | `false` | 43.274000 | 2410 | 1 | 0 | 0.043473 |
| sberbank-russian-housing-market | tc4_mixed_history | single_llm | try5 | 0.545455 | 0.315789 | 0.400000 | 1.000000 | 0.333333 | 0.500000 | 0.366667 | 0.450000 | `false` | 50.600000 | 2909 | 1 | 0 | 0.050958 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sberbank-russian-housing-market | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.476505 | 0.672727 | 0.554717 | 1.000000 | 1.000000 | 1.000000 | 0.777359 | 0.777359 | 0.000411 | 236.196146 | 14153.800000 | `null` | 11.000000 | 0.441749 |
| sberbank-russian-housing-market | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.515560 | 0.590909 | 0.549780 | 1.000000 | 1.000000 | 1.000000 | 0.774890 | 0.774890 | 0.001051 | 134.193200 | 32597.400000 | 7.800000 | 8.400000 | 0.314409 |
| sberbank-russian-housing-market | tc1_from_scratch | human | 1 | `true` | 1.000000 | 0.451613 | 0.636364 | 0.528302 | 1.000000 | 1.000000 | 1.000000 | 0.764151 | 0.764151 | 0.000000 | 1800 | `null` | `null` | `null` | `null` |
| sberbank-russian-housing-market | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.558754 | 0.627273 | 0.590094 | 1.000000 | 1.000000 | 1.000000 | 0.795047 | 0.795047 | 0.000544 | 166.825400 | 39224.200000 | 6.200000 | 7.600000 | 0.377651 |
| sberbank-russian-housing-market | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.250000 | 0.181818 | 0.210526 | 1.000000 | 1.000000 | 1.000000 | 0.605263 | 0.605263 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.528811 | 0.563636 | 0.544237 | 1.000000 | 1.000000 | 1.000000 | 0.772119 | 0.772119 | 0.000218 | 43.584400 | 2305.000000 | 1.000000 | 0.000000 | 0.161878 |
| sberbank-russian-housing-market | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.683333 | 0.178947 | 0.279222 | 1.000000 | 1.000000 | 1.000000 | 0.639611 | 0.639611 | 0.002605 | 145.174510 | 8161.800000 | `null` | 15.400000 | 0.346131 |
| sberbank-russian-housing-market | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.530714 | 0.294737 | 0.373667 | 1.000000 | 1.000000 | 1.000000 | 0.686834 | 0.686834 | 0.000513 | 117.958200 | 30285.200000 | 8.200000 | 9.200000 | 0.240164 |
| sberbank-russian-housing-market | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.550000 | 0.410526 | 0.469289 | 1.000000 | 1.000000 | 1.000000 | 0.734644 | 0.734644 | 0.000298 | 137.897200 | 37953.400000 | 8.200000 | 12.400000 | 0.335317 |
| sberbank-russian-housing-market | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.250000 | 0.210526 | 0.228571 | 1.000000 | 1.000000 | 1.000000 | 0.614286 | 0.614286 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.554402 | 0.378947 | 0.448910 | 1.000000 | 1.000000 | 1.000000 | 0.724455 | 0.724455 | 0.000215 | 59.211600 | 3270.400000 | 1.000000 | 0.000000 | 0.072472 |
| sberbank-russian-housing-market | tc3_fault_injected | claude_code | 5 | `false` | 0.000000 | 0.100000 | 0.009091 | 0.016667 | 1.000000 | 0.760000 | 0.861111 | 0.388333 | 0.438889 | 0.000544 | 110.458376 | 6834.400000 | `null` | 10.200000 | 0.284115 |
| sberbank-russian-housing-market | tc3_fault_injected | generic_agent | 5 | `true` | 0.800000 | 0.636667 | 0.163636 | 0.252106 | 1.000000 | 0.760000 | 0.861111 | 0.506053 | 0.556609 | 0.007291 | 96.295000 | 22096.400000 | 6.800000 | 7.400000 | 0.194079 |
| sberbank-russian-housing-market | tc3_fault_injected | proposed_agent | 5 | `true` | 0.600000 | 0.674676 | 0.290909 | 0.403511 | 1.000000 | 0.600000 | 0.750000 | 0.501755 | 0.576755 | 0.000605 | 174.943200 | 38217.600000 | 7.600000 | 10.600000 | 0.321408 |
| sberbank-russian-housing-market | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.250000 | 0.181818 | 0.210526 | 1.000000 | 0.400000 | 0.571429 | 0.305263 | 0.390977 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 0.605952 | 0.318182 | 0.414379 | 1.000000 | 0.800000 | 0.888889 | 0.607189 | 0.651634 | 0.001224 | 52.073200 | 3101.000000 | 1.000000 | 0.000000 | 0.053617 |
| sberbank-russian-housing-market | tc4_mixed_history | claude_code | 5 | `false` | 0.000000 | 0.693334 | 0.126316 | 0.212121 | 1.000000 | 0.333333 | 0.500000 | 0.272727 | 0.356060 | 0.000918 | 120.559181 | 6179.400000 | `null` | 11.400000 | 0.287371 |
| sberbank-russian-housing-market | tc4_mixed_history | generic_agent | 5 | `false` | 0.000000 | 0.710000 | 0.157895 | 0.255568 | 1.000000 | 0.333333 | 0.500000 | 0.294451 | 0.377784 | 0.001055 | 84.731000 | 19183.000000 | 6.600000 | 7.200000 | 0.161537 |
| sberbank-russian-housing-market | tc4_mixed_history | proposed_agent | 5 | `false` | 0.000000 | 0.595000 | 0.315789 | 0.409640 | 1.000000 | 0.333333 | 0.500000 | 0.371486 | 0.454820 | 0.001375 | 177.309600 | 43463.800000 | 9.000000 | 14.600000 | 0.351392 |
| sberbank-russian-housing-market | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.214286 | 0.157895 | 0.181818 | 0.000000 | 0.000000 | 0.000000 | 0.090909 | 0.090909 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc4_mixed_history | single_llm | 5 | `false` | 0.000000 | 0.658615 | 0.336842 | 0.442415 | 1.000000 | 0.333333 | 0.500000 | 0.387874 | 0.471207 | 0.000620 | 46.897800 | 2711.400000 | 1.000000 | 0.000000 | 0.047774 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 0.500000 | 5.000000 | 0.500000 | 0.488293 | 0.246770 | 0.265682 | 1.000000 | 0.773333 | 0.840278 | 0.519508 | 0.552980 | 0.001120 | 153.097053 | 8832.350000 | `null` | 12.000000 | 0.339842 |
| generic_agent | 4 | 0.750000 | 5.000000 | 0.700000 | 0.598235 | 0.301794 | 0.357780 | 1.000000 | 0.773333 | 0.840278 | 0.565557 | 0.599029 | 0.002478 | 108.294350 | 26040.500000 | 7.350000 | 8.050000 | 0.227547 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 0.451613 | 0.636364 | 0.528302 | 1.000000 | 1.000000 | 1.000000 | 0.764151 | 0.764151 | 0.000000 | 1800.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 0.750000 | 5.000000 | 0.650000 | 0.594607 | 0.411124 | 0.468133 | 1.000000 | 0.733333 | 0.812500 | 0.600733 | 0.640316 | 0.000705 | 164.243850 | 39714.750000 | 7.750000 | 11.300000 | 0.346442 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.241071 | 0.183014 | 0.207860 | 0.750000 | 0.600000 | 0.642857 | 0.403930 | 0.425359 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 0.750000 | 5.000000 | 0.750000 | 0.586945 | 0.399402 | 0.462485 | 1.000000 | 0.783333 | 0.847222 | 0.622909 | 0.654854 | 0.000569 | 50.441750 | 2846.950000 | 1.000000 | 0.000000 | 0.083935 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task sberbank-russian-housing-market --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/sberbank-russian-housing-market-all.md
```
