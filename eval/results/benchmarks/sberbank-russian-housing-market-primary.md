# Benchmark Aggregate Report

## Configuration

- Stage scope: `primary`
- Success threshold: `0.5`
- Tasks included: `sberbank-russian-housing-market`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.714286`
- Mean Add Precision: `0.384899`
- Mean Add Recall: `0.451190`
- Mean Add F1: `0.384928`
- Mean Remove Precision: `0.952381`
- Mean Remove Recall: `0.745397`
- Mean Remove F1: `0.806311`
- Mean Task Completion Score: `0.565162`
- Mean Strict Task Completion Score: `0.595620`
- Mean Task Completion Variance: `0.001300`
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
| sberbank-russian-housing-market | 21 | 6 | 0.714286 | 4.047619 | 0.384899 | 0.451190 | 0.384928 | 0.952381 | 0.745397 | 0.806311 | 0.565162 | 0.595620 | 0.001300 | 176.395620 | 19358.637500 | 4.025000 | 6.270000 | 0.199553 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sberbank-russian-housing-market | tc1_from_scratch | claude_code | try1 | 0.400000 | 0.750000 | 0.521739 | 1.000000 | 1.000000 | 1.000000 | 0.760869 | 0.760869 | `true` | 296.442135 | 17465 | `null` | 13 | 0.511221 |
| sberbank-russian-housing-market | tc1_from_scratch | claude_code | try2 | 0.263158 | 0.625000 | 0.370370 | 1.000000 | 1.000000 | 1.000000 | 0.685185 | 0.685185 | `true` | 234.639215 | 13428 | `null` | 9 | 0.413091 |
| sberbank-russian-housing-market | tc1_from_scratch | claude_code | try3 | 0.250000 | 0.750000 | 0.375000 | 1.000000 | 1.000000 | 1.000000 | 0.687500 | 0.687500 | `true` | 220.029293 | 12256 | `null` | 12 | 0.416591 |
| sberbank-russian-housing-market | tc1_from_scratch | claude_code | try4 | 0.300000 | 0.750000 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | `true` | 173.136836 | 12331 | `null` | 11 | 0.415343 |
| sberbank-russian-housing-market | tc1_from_scratch | claude_code | try5 | 0.260870 | 0.750000 | 0.387097 | 1.000000 | 1.000000 | 1.000000 | 0.693549 | 0.693549 | `true` | 256.733251 | 15289 | `null` | 10 | 0.452498 |
| sberbank-russian-housing-market | tc1_from_scratch | generic_agent | try1 | 0.428571 | 0.750000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 144.607000 | 37499 | 7 | 9 | 0.337155 |
| sberbank-russian-housing-market | tc1_from_scratch | generic_agent | try2 | 0.285714 | 0.500000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 147.066000 | 32985 | 8 | 9 | 0.325646 |
| sberbank-russian-housing-market | tc1_from_scratch | generic_agent | try3 | 0.315789 | 0.750000 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 138.479000 | 31779 | 9 | 9 | 0.320849 |
| sberbank-russian-housing-market | tc1_from_scratch | generic_agent | try4 | 0.333333 | 0.625000 | 0.434783 | 1.000000 | 1.000000 | 1.000000 | 0.717391 | 0.717391 | `true` | 116.070000 | 29415 | 9 | 9 | 0.298970 |
| sberbank-russian-housing-market | tc1_from_scratch | generic_agent | try5 | 0.357143 | 0.625000 | 0.454545 | 1.000000 | 1.000000 | 1.000000 | 0.727272 | 0.727272 | `true` | 124.744000 | 31309 | 6 | 6 | 0.289423 |
| sberbank-russian-housing-market | tc1_from_scratch | human | human_tc1_annotator_a_working_v1 | 0.300000 | 0.750000 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | `true` | 1800 | `null` | `null` | `null` | `null` |
| sberbank-russian-housing-market | tc1_from_scratch | proposed_agent | try1 | 0.416667 | 0.625000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 186.662000 | 42849 | 6 | 7 | 0.382506 |
| sberbank-russian-housing-market | tc1_from_scratch | proposed_agent | try2 | 0.416667 | 0.625000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 237.371000 | 58503 | 8 | 11 | 0.537231 |
| sberbank-russian-housing-market | tc1_from_scratch | proposed_agent | try3 | 0.384615 | 0.625000 | 0.476190 | 1.000000 | 1.000000 | 1.000000 | 0.738095 | 0.738095 | `true` | 139.834000 | 25520 | 5 | 6 | 0.288126 |
| sberbank-russian-housing-market | tc1_from_scratch | proposed_agent | try4 | 0.375000 | 0.750000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 143.725000 | 36613 | 6 | 7 | 0.338862 |
| sberbank-russian-housing-market | tc1_from_scratch | proposed_agent | try5 | 0.416667 | 0.625000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 126.535000 | 32636 | 6 | 7 | 0.341529 |
| sberbank-russian-housing-market | tc1_from_scratch | rule_based | try1 | 0.250000 | 0.375000 | 0.300000 | 1.000000 | 1.000000 | 1.000000 | 0.650000 | 0.650000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc1_from_scratch | single_llm | try1 | 0.363636 | 0.500000 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 105.423000 | 5128 | 1 | 0 | 0.685219 |
| sberbank-russian-housing-market | tc1_from_scratch | single_llm | try2 | 0.384615 | 0.625000 | 0.476190 | 1.000000 | 1.000000 | 1.000000 | 0.738095 | 0.738095 | `true` | 25.080000 | 1449 | 1 | 0 | 0.028352 |
| sberbank-russian-housing-market | tc1_from_scratch | single_llm | try3 | 0.294118 | 0.625000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 32.578000 | 1801 | 1 | 0 | 0.034215 |
| sberbank-russian-housing-market | tc1_from_scratch | single_llm | try4 | 0.400000 | 0.750000 | 0.521739 | 1.000000 | 1.000000 | 1.000000 | 0.760869 | 0.760869 | `true` | 26.048000 | 1546 | 1 | 0 | 0.030390 |
| sberbank-russian-housing-market | tc1_from_scratch | single_llm | try5 | 0.357143 | 0.625000 | 0.454545 | 1.000000 | 1.000000 | 1.000000 | 0.727272 | 0.727272 | `true` | 28.793000 | 1601 | 1 | 0 | 0.031215 |
| sberbank-russian-housing-market | tc2_partial_good | claude_code | try1 | 0.500000 | 0.200000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 163.242124 | 9532 | `null` | 29 | 0.437061 |
| sberbank-russian-housing-market | tc2_partial_good | claude_code | try2 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 130.803618 | 7104 | `null` | 12 | 0.321231 |
| sberbank-russian-housing-market | tc2_partial_good | claude_code | try3 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 200.154153 | 12450 | `null` | 16 | 0.451736 |
| sberbank-russian-housing-market | tc2_partial_good | claude_code | try4 | 0.500000 | 0.200000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 101.894445 | 5422 | `null` | 10 | 0.251996 |
| sberbank-russian-housing-market | tc2_partial_good | claude_code | try5 | 0.500000 | 0.400000 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 129.778211 | 6301 | `null` | 10 | 0.268630 |
| sberbank-russian-housing-market | tc2_partial_good | generic_agent | try1 | 0.333333 | 0.200000 | 0.250000 | 1.000000 | 1.000000 | 1.000000 | 0.625000 | 0.625000 | `true` | 95.455000 | 22996 | 8 | 9 | 0.192706 |
| sberbank-russian-housing-market | tc2_partial_good | generic_agent | try2 | 0.400000 | 0.400000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 109.953000 | 35448 | 7 | 7 | 0.239866 |
| sberbank-russian-housing-market | tc2_partial_good | generic_agent | try3 | 0.125000 | 0.200000 | 0.153846 | 1.000000 | 1.000000 | 1.000000 | 0.576923 | 0.576923 | `true` | 109.061000 | 23938 | 10 | 10 | 0.215500 |
| sberbank-russian-housing-market | tc2_partial_good | generic_agent | try4 | 0.200000 | 0.200000 | 0.200000 | 1.000000 | 1.000000 | 1.000000 | 0.600000 | 0.600000 | `true` | 152.984000 | 38811 | 8 | 11 | 0.310130 |
| sberbank-russian-housing-market | tc2_partial_good | generic_agent | try5 | 0.250000 | 0.400000 | 0.307692 | 1.000000 | 1.000000 | 1.000000 | 0.653846 | 0.653846 | `true` | 122.338000 | 30233 | 8 | 9 | 0.242619 |
| sberbank-russian-housing-market | tc2_partial_good | proposed_agent | try1 | 0.285714 | 0.400000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 146.586000 | 40909 | 8 | 14 | 0.332667 |
| sberbank-russian-housing-market | tc2_partial_good | proposed_agent | try2 | 0.142857 | 0.200000 | 0.166667 | 1.000000 | 1.000000 | 1.000000 | 0.583333 | 0.583333 | `true` | 119.175000 | 37191 | 9 | 13 | 0.393845 |
| sberbank-russian-housing-market | tc2_partial_good | proposed_agent | try3 | 0.250000 | 0.400000 | 0.307692 | 1.000000 | 1.000000 | 1.000000 | 0.653846 | 0.653846 | `true` | 137.259000 | 39323 | 9 | 13 | 0.320295 |
| sberbank-russian-housing-market | tc2_partial_good | proposed_agent | try4 | 0.333333 | 0.400000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 137.658000 | 34279 | 7 | 10 | 0.291198 |
| sberbank-russian-housing-market | tc2_partial_good | proposed_agent | try5 | 0.142857 | 0.200000 | 0.166667 | 1.000000 | 1.000000 | 1.000000 | 0.583333 | 0.583333 | `true` | 148.808000 | 38065 | 8 | 12 | 0.338580 |
| sberbank-russian-housing-market | tc2_partial_good | rule_based | try1 | 0.250000 | 0.600000 | 0.352941 | 1.000000 | 1.000000 | 1.000000 | 0.676470 | 0.676470 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc2_partial_good | single_llm | try1 | 0.285714 | 0.400000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 86.881000 | 3840 | 1 | 0 | 0.145626 |
| sberbank-russian-housing-market | tc2_partial_good | single_llm | try2 | 0.285714 | 0.400000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 44.708000 | 2678 | 1 | 0 | 0.047433 |
| sberbank-russian-housing-market | tc2_partial_good | single_llm | try3 | 0.333333 | 0.400000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 53.448000 | 3114 | 1 | 0 | 0.053973 |
| sberbank-russian-housing-market | tc2_partial_good | single_llm | try4 | 0.333333 | 0.400000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 56.383000 | 3211 | 1 | 0 | 0.055428 |
| sberbank-russian-housing-market | tc2_partial_good | single_llm | try5 | 0.250000 | 0.400000 | 0.307692 | 1.000000 | 1.000000 | 1.000000 | 0.653846 | 0.653846 | `true` | 54.638000 | 3509 | 1 | 0 | 0.059898 |
| sberbank-russian-housing-market | tc3_fault_injected | claude_code | try1 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.800000 | 0.888889 | 0.400000 | 0.444445 | `false` | 131.655427 | 8513 | `null` | 15 | 0.339169 |
| sberbank-russian-housing-market | tc3_fault_injected | claude_code | try2 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.800000 | 0.888889 | 0.400000 | 0.444445 | `false` | 120.696645 | 7683 | `null` | 9 | 0.287164 |
| sberbank-russian-housing-market | tc3_fault_injected | claude_code | try3 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.800000 | 0.888889 | 0.400000 | 0.444445 | `false` | 89.961321 | 5387 | `null` | 9 | 0.238735 |
| sberbank-russian-housing-market | tc3_fault_injected | claude_code | try4 | 0.500000 | 0.125000 | 0.200000 | 1.000000 | 0.600000 | 0.750000 | 0.400000 | 0.475000 | `false` | 98.956329 | 5647 | `null` | 10 | 0.266242 |
| sberbank-russian-housing-market | tc3_fault_injected | claude_code | try5 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.800000 | 0.888889 | 0.400000 | 0.444445 | `false` | 111.022158 | 6942 | `null` | 8 | 0.289267 |
| sberbank-russian-housing-market | tc3_fault_injected | generic_agent | try1 | 0.500000 | 0.125000 | 0.200000 | 1.000000 | 0.600000 | 0.750000 | 0.400000 | 0.475000 | `false` | 76.189000 | 17210 | 6 | 7 | 0.142628 |
| sberbank-russian-housing-market | tc3_fault_injected | generic_agent | try2 | 0.600000 | 0.375000 | 0.461538 | 1.000000 | 0.800000 | 0.888889 | 0.630769 | 0.675214 | `true` | 103.482000 | 22535 | 7 | 7 | 0.237481 |
| sberbank-russian-housing-market | tc3_fault_injected | generic_agent | try3 | 0.750000 | 0.375000 | 0.500000 | 1.000000 | 0.800000 | 0.888889 | 0.650000 | 0.694445 | `true` | 118.364000 | 29219 | 9 | 10 | 0.244526 |
| sberbank-russian-housing-market | tc3_fault_injected | generic_agent | try4 | 0.571429 | 0.500000 | 0.533333 | 1.000000 | 0.800000 | 0.888889 | 0.666667 | 0.711111 | `true` | 93.948000 | 21434 | 6 | 6 | 0.178097 |
| sberbank-russian-housing-market | tc3_fault_injected | generic_agent | try5 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 0.800000 | 0.888889 | 0.566666 | 0.611111 | `true` | 89.492000 | 20084 | 6 | 7 | 0.167663 |
| sberbank-russian-housing-market | tc3_fault_injected | proposed_agent | try1 | 0.428571 | 0.375000 | 0.400000 | 1.000000 | 0.600000 | 0.750000 | 0.500000 | 0.575000 | `true` | 177.537000 | 38637 | 8 | 12 | 0.330410 |
| sberbank-russian-housing-market | tc3_fault_injected | proposed_agent | try2 | 0.750000 | 0.375000 | 0.500000 | 1.000000 | 0.600000 | 0.750000 | 0.550000 | 0.625000 | `true` | 161.611000 | 30806 | 6 | 6 | 0.255951 |
| sberbank-russian-housing-market | tc3_fault_injected | proposed_agent | try3 | 0.500000 | 0.375000 | 0.428571 | 1.000000 | 0.600000 | 0.750000 | 0.514285 | 0.589286 | `true` | 184.604000 | 44570 | 9 | 13 | 0.365975 |
| sberbank-russian-housing-market | tc3_fault_injected | proposed_agent | try4 | 0.500000 | 0.375000 | 0.428571 | 1.000000 | 0.600000 | 0.750000 | 0.514285 | 0.589286 | `true` | 204.115000 | 47182 | 9 | 13 | 0.405370 |
| sberbank-russian-housing-market | tc3_fault_injected | proposed_agent | try5 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 0.600000 | 0.750000 | 0.481818 | 0.556818 | `false` | 146.849000 | 29893 | 6 | 9 | 0.249333 |
| sberbank-russian-housing-market | tc3_fault_injected | rule_based | try1 | 0.250000 | 0.375000 | 0.300000 | 1.000000 | 0.400000 | 0.571429 | 0.350000 | 0.435715 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc3_fault_injected | single_llm | try1 | 0.714286 | 0.625000 | 0.666667 | 1.000000 | 0.800000 | 0.888889 | 0.733334 | 0.777778 | `true` | 59.715000 | 3655 | 1 | 0 | 0.061070 |
| sberbank-russian-housing-market | tc3_fault_injected | single_llm | try2 | 0.375000 | 0.375000 | 0.375000 | 1.000000 | 0.800000 | 0.888889 | 0.587500 | 0.631945 | `true` | 53.055000 | 3128 | 1 | 0 | 0.054236 |
| sberbank-russian-housing-market | tc3_fault_injected | single_llm | try3 | 0.375000 | 0.375000 | 0.375000 | 1.000000 | 0.800000 | 0.888889 | 0.587500 | 0.631945 | `true` | 50.389000 | 2849 | 1 | 0 | 0.050051 |
| sberbank-russian-housing-market | tc3_fault_injected | single_llm | try4 | 0.428571 | 0.375000 | 0.400000 | 1.000000 | 0.800000 | 0.888889 | 0.600000 | 0.644445 | `true` | 51.332000 | 3138 | 1 | 0 | 0.054386 |
| sberbank-russian-housing-market | tc3_fault_injected | single_llm | try5 | 0.600000 | 0.375000 | 0.461538 | 1.000000 | 0.800000 | 0.888889 | 0.630769 | 0.675214 | `true` | 45.875000 | 2735 | 1 | 0 | 0.048341 |
| sberbank-russian-housing-market | tc4_mixed_history | claude_code | try1 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 0.333333 | 0.500000 | 0.416666 | 0.500000 | `false` | 209.605267 | 7781 | `null` | 16 | 0.373590 |
| sberbank-russian-housing-market | tc4_mixed_history | claude_code | try2 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 0.333333 | 0.500000 | 0.416666 | 0.500000 | `false` | 90.155250 | 5887 | `null` | 10 | 0.280481 |
| sberbank-russian-housing-market | tc4_mixed_history | claude_code | try3 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 0.333333 | 0.500000 | 0.416666 | 0.500000 | `false` | 101.153108 | 5441 | `null` | 10 | 0.252417 |
| sberbank-russian-housing-market | tc4_mixed_history | claude_code | try4 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 0.333333 | 0.500000 | 0.416666 | 0.500000 | `false` | 78.756942 | 4627 | `null` | 8 | 0.223890 |
| sberbank-russian-housing-market | tc4_mixed_history | claude_code | try5 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 0.333333 | 0.500000 | 0.416666 | 0.500000 | `false` | 123.125340 | 7161 | `null` | 13 | 0.306478 |
| sberbank-russian-housing-market | tc4_mixed_history | generic_agent | try1 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 0.333333 | 0.500000 | 0.416666 | 0.500000 | `false` | 88.976000 | 20762 | 6 | 8 | 0.168946 |
| sberbank-russian-housing-market | tc4_mixed_history | generic_agent | try2 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 0.333333 | 0.500000 | 0.416666 | 0.500000 | `false` | 64.729000 | 14219 | 5 | 5 | 0.114342 |
| sberbank-russian-housing-market | tc4_mixed_history | generic_agent | try3 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 0.333333 | 0.500000 | 0.416666 | 0.500000 | `false` | 95.247000 | 22343 | 9 | 10 | 0.198254 |
| sberbank-russian-housing-market | tc4_mixed_history | generic_agent | try4 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 0.333333 | 0.500000 | 0.416666 | 0.500000 | `false` | 90.132000 | 21359 | 7 | 7 | 0.174573 |
| sberbank-russian-housing-market | tc4_mixed_history | generic_agent | try5 | 0.500000 | 0.200000 | 0.285714 | 1.000000 | 0.333333 | 0.500000 | 0.309524 | 0.392857 | `false` | 84.571000 | 17232 | 6 | 6 | 0.151569 |
| sberbank-russian-housing-market | tc4_mixed_history | proposed_agent | try1 | 0.500000 | 0.600000 | 0.545455 | 1.000000 | 0.333333 | 0.500000 | 0.439394 | 0.522728 | `false` | 180.054000 | 39092 | 8 | 15 | 0.313195 |
| sberbank-russian-housing-market | tc4_mixed_history | proposed_agent | try2 | 0.333333 | 0.400000 | 0.363636 | 1.000000 | 0.333333 | 0.500000 | 0.348484 | 0.431818 | `false` | 175.805000 | 41633 | 8 | 11 | 0.323769 |
| sberbank-russian-housing-market | tc4_mixed_history | proposed_agent | try3 | 0.500000 | 0.600000 | 0.545455 | 1.000000 | 0.333333 | 0.500000 | 0.439394 | 0.522728 | `false` | 180.057000 | 49400 | 9 | 16 | 0.393815 |
| sberbank-russian-housing-market | tc4_mixed_history | proposed_agent | try4 | 0.500000 | 0.600000 | 0.545455 | 1.000000 | 0.333333 | 0.500000 | 0.439394 | 0.522728 | `false` | 171.228000 | 43524 | 10 | 15 | 0.354070 |
| sberbank-russian-housing-market | tc4_mixed_history | proposed_agent | try5 | 0.600000 | 0.600000 | 0.600000 | 1.000000 | 0.333333 | 0.500000 | 0.466666 | 0.550000 | `false` | 179.404000 | 43670 | 10 | 16 | 0.372110 |
| sberbank-russian-housing-market | tc4_mixed_history | rule_based | try1 | 0.200000 | 0.400000 | 0.266667 | 0.000000 | 0.000000 | 0.000000 | 0.133333 | 0.133333 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc4_mixed_history | single_llm | try1 | 0.500000 | 0.600000 | 0.545455 | 1.000000 | 0.333333 | 0.500000 | 0.439394 | 0.522728 | `false` | 48.973000 | 2982 | 1 | 0 | 0.050951 |
| sberbank-russian-housing-market | tc4_mixed_history | single_llm | try2 | 0.600000 | 0.600000 | 0.600000 | 1.000000 | 0.333333 | 0.500000 | 0.466666 | 0.550000 | `false` | 44.665000 | 2550 | 1 | 0 | 0.045573 |
| sberbank-russian-housing-market | tc4_mixed_history | single_llm | try3 | 0.500000 | 0.600000 | 0.545455 | 1.000000 | 0.333333 | 0.500000 | 0.439394 | 0.522728 | `false` | 46.977000 | 2706 | 1 | 0 | 0.047913 |
| sberbank-russian-housing-market | tc4_mixed_history | single_llm | try4 | 0.750000 | 0.600000 | 0.666667 | 1.000000 | 0.333333 | 0.500000 | 0.500000 | 0.583333 | `true` | 43.274000 | 2410 | 1 | 0 | 0.043473 |
| sberbank-russian-housing-market | tc4_mixed_history | single_llm | try5 | 0.333333 | 0.400000 | 0.363636 | 1.000000 | 0.333333 | 0.500000 | 0.348484 | 0.431818 | `false` | 50.600000 | 2909 | 1 | 0 | 0.050958 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sberbank-russian-housing-market | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.294806 | 0.725000 | 0.416555 | 1.000000 | 1.000000 | 1.000000 | 0.708278 | 0.708278 | 0.000797 | 236.196146 | 14153.800000 | `null` | 11.000000 | 0.441749 |
| sberbank-russian-housing-market | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.344110 | 0.650000 | 0.448573 | 1.000000 | 1.000000 | 1.000000 | 0.724286 | 0.724286 | 0.000842 | 134.193200 | 32597.400000 | 7.800000 | 8.400000 | 0.314409 |
| sberbank-russian-housing-market | tc1_from_scratch | human | 1 | `true` | 1.000000 | 0.300000 | 0.750000 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | 0.000000 | 1800 | `null` | `null` | `null` | `null` |
| sberbank-russian-housing-market | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.401923 | 0.650000 | 0.495238 | 1.000000 | 1.000000 | 1.000000 | 0.747619 | 0.747619 | 0.000023 | 166.825400 | 39224.200000 | 6.200000 | 7.600000 | 0.377651 |
| sberbank-russian-housing-market | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.250000 | 0.375000 | 0.300000 | 1.000000 | 1.000000 | 1.000000 | 0.650000 | 0.650000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.359902 | 0.625000 | 0.454705 | 1.000000 | 1.000000 | 1.000000 | 0.727353 | 0.727353 | 0.000454 | 43.584400 | 2305.000000 | 1.000000 | 0.000000 | 0.161878 |
| sberbank-russian-housing-market | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.566667 | 0.320000 | 0.403174 | 1.000000 | 1.000000 | 1.000000 | 0.701587 | 0.701587 | 0.002402 | 145.174510 | 8161.800000 | `null` | 15.400000 | 0.346131 |
| sberbank-russian-housing-market | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.261667 | 0.280000 | 0.262308 | 1.000000 | 1.000000 | 1.000000 | 0.631154 | 0.631154 | 0.001841 | 117.958200 | 30285.200000 | 8.200000 | 9.200000 | 0.240164 |
| sberbank-russian-housing-market | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.230952 | 0.320000 | 0.267599 | 1.000000 | 1.000000 | 1.000000 | 0.633799 | 0.633799 | 0.001776 | 137.897200 | 37953.400000 | 8.200000 | 12.400000 | 0.335317 |
| sberbank-russian-housing-market | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.250000 | 0.600000 | 0.352941 | 1.000000 | 1.000000 | 1.000000 | 0.676470 | 0.676470 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.297619 | 0.400000 | 0.340326 | 1.000000 | 1.000000 | 1.000000 | 0.670163 | 0.670163 | 0.000112 | 59.211600 | 3270.400000 | 1.000000 | 0.000000 | 0.072472 |
| sberbank-russian-housing-market | tc3_fault_injected | claude_code | 5 | `false` | 0.000000 | 0.100000 | 0.025000 | 0.040000 | 1.000000 | 0.760000 | 0.861111 | 0.400000 | 0.450556 | 0.000000 | 110.458376 | 6834.400000 | `null` | 10.200000 | 0.284115 |
| sberbank-russian-housing-market | tc3_fault_injected | generic_agent | 5 | `true` | 0.800000 | 0.584286 | 0.325000 | 0.405641 | 1.000000 | 0.760000 | 0.861111 | 0.582820 | 0.633376 | 0.009505 | 96.295000 | 22096.400000 | 6.800000 | 7.400000 | 0.194079 |
| sberbank-russian-housing-market | tc3_fault_injected | proposed_agent | 5 | `true` | 0.800000 | 0.569048 | 0.350000 | 0.424156 | 1.000000 | 0.600000 | 0.750000 | 0.512078 | 0.587078 | 0.000502 | 174.943200 | 38217.600000 | 7.600000 | 10.600000 | 0.321408 |
| sberbank-russian-housing-market | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.250000 | 0.375000 | 0.300000 | 1.000000 | 0.400000 | 0.571429 | 0.350000 | 0.435715 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 0.498571 | 0.425000 | 0.455641 | 1.000000 | 0.800000 | 0.888889 | 0.627821 | 0.672265 | 0.003033 | 52.073200 | 3101.000000 | 1.000000 | 0.000000 | 0.053617 |
| sberbank-russian-housing-market | tc4_mixed_history | claude_code | 5 | `false` | 0.000000 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 0.333333 | 0.500000 | 0.416666 | 0.500000 | 0.000000 | 120.559181 | 6179.400000 | `null` | 11.400000 | 0.287371 |
| sberbank-russian-housing-market | tc4_mixed_history | generic_agent | 5 | `false` | 0.000000 | 0.633334 | 0.360000 | 0.457143 | 1.000000 | 0.333333 | 0.500000 | 0.395238 | 0.478571 | 0.001837 | 84.731000 | 19183.000000 | 6.600000 | 7.200000 | 0.161537 |
| sberbank-russian-housing-market | tc4_mixed_history | proposed_agent | 5 | `false` | 0.000000 | 0.486667 | 0.560000 | 0.520000 | 1.000000 | 0.333333 | 0.500000 | 0.426666 | 0.510000 | 0.001640 | 177.309600 | 43463.800000 | 9.000000 | 14.600000 | 0.351392 |
| sberbank-russian-housing-market | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.200000 | 0.400000 | 0.266667 | 0.000000 | 0.000000 | 0.000000 | 0.133333 | 0.133333 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| sberbank-russian-housing-market | tc4_mixed_history | single_llm | 5 | `true` | 0.200000 | 0.536667 | 0.560000 | 0.544243 | 1.000000 | 0.333333 | 0.500000 | 0.438788 | 0.522121 | 0.002536 | 46.897800 | 2711.400000 | 1.000000 | 0.000000 | 0.047774 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 0.500000 | 5.000000 | 0.500000 | 0.407035 | 0.367500 | 0.339932 | 1.000000 | 0.773333 | 0.840278 | 0.556633 | 0.590105 | 0.000800 | 153.097053 | 8832.350000 | `null` | 12.000000 | 0.339842 |
| generic_agent | 4 | 0.750000 | 5.000000 | 0.700000 | 0.455849 | 0.403750 | 0.393416 | 1.000000 | 0.773333 | 0.840278 | 0.583375 | 0.616847 | 0.003506 | 108.294350 | 26040.500000 | 7.350000 | 8.050000 | 0.227547 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 0.300000 | 0.750000 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | 0.000000 | 1800.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 0.750000 | 5.000000 | 0.700000 | 0.422148 | 0.470000 | 0.426748 | 1.000000 | 0.733333 | 0.812500 | 0.580040 | 0.619624 | 0.000985 | 164.243850 | 39714.750000 | 7.750000 | 11.300000 | 0.346442 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.237500 | 0.437500 | 0.304902 | 0.750000 | 0.600000 | 0.642857 | 0.452451 | 0.473880 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 0.800000 | 0.423190 | 0.502500 | 0.448729 | 1.000000 | 0.783333 | 0.847222 | 0.616031 | 0.647976 | 0.001534 | 50.441750 | 2846.950000 | 1.000000 | 0.000000 | 0.083935 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task sberbank-russian-housing-market --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/sberbank-russian-housing-market-primary.md
```
