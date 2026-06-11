# Benchmark Aggregate Report

## Configuration

- Stage scope: `primary`
- Success threshold: `0.5`
- Tasks included: `elo-merchant-category-recommendation`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.904762`
- Mean Add Precision: `0.784238`
- Mean Add Recall: `0.530526`
- Mean Add F1: `0.619280`
- Mean Remove Precision: `0.842857`
- Mean Remove Recall: `0.821429`
- Mean Remove F1: `0.743628`
- Mean Task Completion Score: `0.720354`
- Mean Strict Task Completion Score: `0.681454`
- Mean Task Completion Variance: `0.003876`
- Mean Runtime (s): `244.974098`
- Mean Total Tokens: `15068.650000`
- Mean API Calls: `2.875000`
- Mean Tool Calls: `7.290000`
- Mean Cost (USD): `0.166109`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| elo-merchant-category-recommendation | RMSE | finance_tabular | regression | multi_table_relational | xlarge (29112361) | medium (34) | medium (14) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| elo-merchant-category-recommendation | 21 | 6 | 0.904762 | 4.047619 | 0.784238 | 0.530526 | 0.619280 | 0.842857 | 0.821429 | 0.743628 | 0.720354 | 0.681454 | 0.003876 | 244.974098 | 15068.650000 | 2.875000 | 7.290000 | 0.166109 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| elo-merchant-category-recommendation | tc1_from_scratch | claude_code | try1 | 0.857143 | 0.857143 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 105.555035 | 4003 | `null` | 23 | 0.268478 |
| elo-merchant-category-recommendation | tc1_from_scratch | claude_code | try2 | 0.800000 | 0.857143 | 0.827586 | 1.000000 | 1.000000 | 1.000000 | 0.913793 | 0.913793 | `true` | 107.805091 | 4319 | `null` | 20 | 0.289698 |
| elo-merchant-category-recommendation | tc1_from_scratch | claude_code | try3 | 0.833333 | 0.714286 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 98.790380 | 3269 | `null` | 29 | 0.266461 |
| elo-merchant-category-recommendation | tc1_from_scratch | claude_code | try4 | 0.833333 | 0.714286 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 120.522328 | 4224 | `null` | 14 | 0.323705 |
| elo-merchant-category-recommendation | tc1_from_scratch | claude_code | try5 | 0.818182 | 0.642857 | 0.720000 | 1.000000 | 1.000000 | 1.000000 | 0.860000 | 0.860000 | `true` | 89.885441 | 2993 | `null` | 18 | 0.261378 |
| elo-merchant-category-recommendation | tc1_from_scratch | generic_agent | try1 | 0.818182 | 0.642857 | 0.720000 | 1.000000 | 1.000000 | 1.000000 | 0.860000 | 0.860000 | `true` | 149.069000 | 23929 | 4 | 3 | 0.205738 |
| elo-merchant-category-recommendation | tc1_from_scratch | generic_agent | try2 | 0.833333 | 0.714286 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 106.823000 | 23248 | 4 | 5 | 0.168533 |
| elo-merchant-category-recommendation | tc1_from_scratch | generic_agent | try3 | 0.833333 | 0.714286 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 109.888000 | 23416 | 5 | 8 | 0.181781 |
| elo-merchant-category-recommendation | tc1_from_scratch | generic_agent | try4 | 0.727273 | 0.571429 | 0.640000 | 1.000000 | 1.000000 | 1.000000 | 0.820000 | 0.820000 | `true` | 185.134000 | 23846 | 8 | 7 | 0.193039 |
| elo-merchant-category-recommendation | tc1_from_scratch | generic_agent | try5 | 0.750000 | 0.642857 | 0.692308 | 1.000000 | 1.000000 | 1.000000 | 0.846154 | 0.846154 | `true` | 108.957000 | 21521 | 5 | 7 | 0.162857 |
| elo-merchant-category-recommendation | tc1_from_scratch | human | human_tc1_sean_kraemer_v4_manual_rebuild | 1.000000 | 0.571429 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | `true` | 3300 | `null` | `null` | `null` | `null` |
| elo-merchant-category-recommendation | tc1_from_scratch | proposed_agent | try1 | 0.846154 | 0.785714 | 0.814815 | 1.000000 | 1.000000 | 1.000000 | 0.907407 | 0.907407 | `true` | 214.050000 | 32920 | 5 | 5 | 0.310910 |
| elo-merchant-category-recommendation | tc1_from_scratch | proposed_agent | try2 | 0.916667 | 0.785714 | 0.846154 | 1.000000 | 1.000000 | 1.000000 | 0.923077 | 0.923077 | `true` | 269.301000 | 50550 | 7 | 10 | 0.367971 |
| elo-merchant-category-recommendation | tc1_from_scratch | proposed_agent | try3 | 0.733333 | 0.785714 | 0.758621 | 1.000000 | 1.000000 | 1.000000 | 0.879310 | 0.879310 | `true` | 99.031000 | 23380 | 4 | 4 | 0.170121 |
| elo-merchant-category-recommendation | tc1_from_scratch | proposed_agent | try4 | 0.916667 | 0.785714 | 0.846154 | 1.000000 | 1.000000 | 1.000000 | 0.923077 | 0.923077 | `true` | 88.859000 | 22391 | 5 | 6 | 0.178041 |
| elo-merchant-category-recommendation | tc1_from_scratch | proposed_agent | try5 | 0.769231 | 0.714286 | 0.740741 | 1.000000 | 1.000000 | 1.000000 | 0.870370 | 0.870370 | `true` | 97.480000 | 24469 | 5 | 6 | 0.196173 |
| elo-merchant-category-recommendation | tc1_from_scratch | rule_based | try1 | 0.500000 | 0.214286 | 0.300000 | 1.000000 | 1.000000 | 1.000000 | 0.650000 | 0.650000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc1_from_scratch | single_llm | try1 | 0.833333 | 0.714286 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 12.731000 | 1013 | 1 | 0 | 0.078383 |
| elo-merchant-category-recommendation | tc1_from_scratch | single_llm | try2 | 0.833333 | 0.714286 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 12.266000 | 1040 | 1 | 0 | 0.020796 |
| elo-merchant-category-recommendation | tc1_from_scratch | single_llm | try3 | 0.750000 | 0.642857 | 0.692308 | 1.000000 | 1.000000 | 1.000000 | 0.846154 | 0.846154 | `true` | 12.435000 | 1057 | 1 | 0 | 0.021051 |
| elo-merchant-category-recommendation | tc1_from_scratch | single_llm | try4 | 0.692308 | 0.642857 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 12.567000 | 1024 | 1 | 0 | 0.020556 |
| elo-merchant-category-recommendation | tc1_from_scratch | single_llm | try5 | 0.833333 | 0.714286 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 13.976000 | 1162 | 1 | 0 | 0.080618 |
| elo-merchant-category-recommendation | tc2_partial_good | claude_code | try1 | 0.800000 | 0.400000 | 0.533333 | 0.000000 | 1.000000 | 0.000000 | 0.766666 | 0.266666 | `true` | 42.278372 | 2094 | `null` | 9 | 0.160817 |
| elo-merchant-category-recommendation | tc2_partial_good | claude_code | try2 | 0.833333 | 0.500000 | 0.625000 | 0.000000 | 1.000000 | 0.000000 | 0.812500 | 0.312500 | `true` | 97.726163 | 1794 | `null` | 15 | 0.116701 |
| elo-merchant-category-recommendation | tc2_partial_good | claude_code | try3 | 0.666667 | 0.200000 | 0.307692 | 0.000000 | 1.000000 | 0.000000 | 0.653846 | 0.153846 | `true` | 91.100677 | 3082 | `null` | 22 | 0.245477 |
| elo-merchant-category-recommendation | tc2_partial_good | claude_code | try4 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 449.704050 | 4142 | `null` | 66 | 1.231438 |
| elo-merchant-category-recommendation | tc2_partial_good | claude_code | try5 | 0.800000 | 0.400000 | 0.533333 | 0.000000 | 1.000000 | 0.000000 | 0.766666 | 0.266666 | `true` | 641.900751 | 3295 | `null` | 42 | 0.808283 |
| elo-merchant-category-recommendation | tc2_partial_good | generic_agent | try1 | 0.714286 | 0.500000 | 0.588235 | 0.000000 | 1.000000 | 0.000000 | 0.794118 | 0.294117 | `true` | 129.839000 | 26037 | 5 | 5 | 0.195961 |
| elo-merchant-category-recommendation | tc2_partial_good | generic_agent | try2 | 0.666667 | 0.400000 | 0.500000 | 0.000000 | 1.000000 | 0.000000 | 0.750000 | 0.250000 | `true` | 76.995000 | 15121 | 6 | 5 | 0.124897 |
| elo-merchant-category-recommendation | tc2_partial_good | generic_agent | try3 | 0.857143 | 0.600000 | 0.705882 | 1.000000 | 1.000000 | 1.000000 | 0.852941 | 0.852941 | `true` | 116.873000 | 23159 | 5 | 5 | 0.185338 |
| elo-merchant-category-recommendation | tc2_partial_good | generic_agent | try4 | 0.666667 | 0.400000 | 0.500000 | 0.000000 | 1.000000 | 0.000000 | 0.750000 | 0.250000 | `true` | 93.966000 | 17747 | 4 | 5 | 0.139227 |
| elo-merchant-category-recommendation | tc2_partial_good | generic_agent | try5 | 0.800000 | 0.400000 | 0.533333 | 0.000000 | 1.000000 | 0.000000 | 0.766666 | 0.266666 | `true` | 112.443000 | 21599 | 5 | 6 | 0.173405 |
| elo-merchant-category-recommendation | tc2_partial_good | proposed_agent | try1 | 0.875000 | 0.700000 | 0.777778 | 1.000000 | 1.000000 | 1.000000 | 0.888889 | 0.888889 | `true` | 87.439000 | 23906 | 5 | 5 | 0.180431 |
| elo-merchant-category-recommendation | tc2_partial_good | proposed_agent | try2 | 0.857143 | 0.600000 | 0.705882 | 1.000000 | 1.000000 | 1.000000 | 0.852941 | 0.852941 | `true` | 123.594000 | 28876 | 6 | 7 | 0.229840 |
| elo-merchant-category-recommendation | tc2_partial_good | proposed_agent | try3 | 0.875000 | 0.700000 | 0.777778 | 1.000000 | 1.000000 | 1.000000 | 0.888889 | 0.888889 | `true` | 118.462000 | 29685 | 6 | 7 | 0.229350 |
| elo-merchant-category-recommendation | tc2_partial_good | proposed_agent | try4 | 0.714286 | 0.500000 | 0.588235 | 1.000000 | 1.000000 | 1.000000 | 0.794118 | 0.794118 | `true` | 123.406000 | 31421 | 5 | 6 | 0.242985 |
| elo-merchant-category-recommendation | tc2_partial_good | proposed_agent | try5 | 0.888889 | 0.800000 | 0.842105 | 1.000000 | 1.000000 | 1.000000 | 0.921053 | 0.921053 | `true` | 109.164000 | 22597 | 4 | 3 | 0.181111 |
| elo-merchant-category-recommendation | tc2_partial_good | rule_based | try1 | 0.400000 | 0.200000 | 0.266667 | 0.000000 | 1.000000 | 0.000000 | 0.633333 | 0.133333 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc2_partial_good | single_llm | try1 | 0.777778 | 0.700000 | 0.736842 | 1.000000 | 1.000000 | 1.000000 | 0.868421 | 0.868421 | `true` | 63.168000 | 4909 | 1 | 0 | 0.077972 |
| elo-merchant-category-recommendation | tc2_partial_good | single_llm | try2 | 0.800000 | 0.800000 | 0.800000 | 0.000000 | 1.000000 | 0.000000 | 0.900000 | 0.400000 | `true` | 59.283000 | 4344 | 1 | 0 | 0.069497 |
| elo-merchant-category-recommendation | tc2_partial_good | single_llm | try3 | 0.875000 | 0.700000 | 0.777778 | 1.000000 | 1.000000 | 1.000000 | 0.888889 | 0.888889 | `true` | 76.324000 | 5663 | 1 | 0 | 0.090227 |
| elo-merchant-category-recommendation | tc2_partial_good | single_llm | try4 | 1.000000 | 0.800000 | 0.888889 | 1.000000 | 1.000000 | 1.000000 | 0.944445 | 0.944445 | `true` | 45.366000 | 3442 | 1 | 0 | 0.056912 |
| elo-merchant-category-recommendation | tc2_partial_good | single_llm | try5 | 0.875000 | 0.700000 | 0.777778 | 1.000000 | 1.000000 | 1.000000 | 0.888889 | 0.888889 | `true` | 58.271000 | 4266 | 1 | 0 | 0.069272 |
| elo-merchant-category-recommendation | tc3_fault_injected | claude_code | try1 | 0.714286 | 0.357143 | 0.476190 | 1.000000 | 0.500000 | 0.666667 | 0.488095 | 0.571429 | `false` | 81.772361 | 2191 | `null` | 13 | 0.184998 |
| elo-merchant-category-recommendation | tc3_fault_injected | claude_code | try2 | 1.000000 | 0.428571 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 261.700832 | 2411 | `null` | 37 | 0.533662 |
| elo-merchant-category-recommendation | tc3_fault_injected | claude_code | try3 | 0.888889 | 0.571429 | 0.695652 | 1.000000 | 1.000000 | 1.000000 | 0.847826 | 0.847826 | `true` | 125.233037 | 2763 | `null` | 25 | 0.235314 |
| elo-merchant-category-recommendation | tc3_fault_injected | claude_code | try4 | 0.857143 | 0.428571 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 120.805323 | 3000 | `null` | 28 | 0.384396 |
| elo-merchant-category-recommendation | tc3_fault_injected | claude_code | try5 | 0.857143 | 0.428571 | 0.571429 | 1.000000 | 0.750000 | 0.857143 | 0.660714 | 0.714286 | `true` | 94.864606 | 2883 | `null` | 21 | 0.308104 |
| elo-merchant-category-recommendation | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.642857 | 0.782609 | 1.000000 | 0.750000 | 0.857143 | 0.766304 | 0.819876 | `true` | 125.264000 | 22648 | 4 | 5 | 0.177821 |
| elo-merchant-category-recommendation | tc3_fault_injected | generic_agent | try2 | 0.888889 | 0.571429 | 0.695652 | 1.000000 | 0.500000 | 0.666667 | 0.597826 | 0.681160 | `true` | 137.053000 | 21109 | 4 | 4 | 0.162041 |
| elo-merchant-category-recommendation | tc3_fault_injected | generic_agent | try3 | 0.909091 | 0.714286 | 0.800000 | 1.000000 | 0.750000 | 0.857143 | 0.775000 | 0.828572 | `true` | 162.369000 | 24833 | 4 | 4 | 0.191053 |
| elo-merchant-category-recommendation | tc3_fault_injected | generic_agent | try4 | 0.857143 | 0.428571 | 0.571429 | 1.000000 | 0.750000 | 0.857143 | 0.660714 | 0.714286 | `true` | 107.951000 | 21883 | 4 | 5 | 0.162553 |
| elo-merchant-category-recommendation | tc3_fault_injected | generic_agent | try5 | 0.800000 | 0.571429 | 0.666667 | 1.000000 | 0.500000 | 0.666667 | 0.583333 | 0.666667 | `true` | 119.421000 | 25095 | 4 | 6 | 0.203367 |
| elo-merchant-category-recommendation | tc3_fault_injected | proposed_agent | try1 | 1.000000 | 0.642857 | 0.782609 | 1.000000 | 0.500000 | 0.666667 | 0.641304 | 0.724638 | `true` | 120.046000 | 26840 | 5 | 5 | 0.213169 |
| elo-merchant-category-recommendation | tc3_fault_injected | proposed_agent | try2 | 0.833333 | 0.714286 | 0.769231 | 1.000000 | 0.500000 | 0.666667 | 0.634615 | 0.717949 | `true` | 141.642000 | 31192 | 6 | 7 | 0.259431 |
| elo-merchant-category-recommendation | tc3_fault_injected | proposed_agent | try3 | 0.900000 | 0.642857 | 0.750000 | 1.000000 | 0.500000 | 0.666667 | 0.625000 | 0.708333 | `true` | 128.002000 | 30401 | 6 | 7 | 0.238048 |
| elo-merchant-category-recommendation | tc3_fault_injected | proposed_agent | try4 | 0.818182 | 0.642857 | 0.720000 | 1.000000 | 0.500000 | 0.666667 | 0.610000 | 0.693334 | `true` | 181.360000 | 34614 | 5 | 5 | 0.274012 |
| elo-merchant-category-recommendation | tc3_fault_injected | proposed_agent | try5 | 0.916667 | 0.785714 | 0.846154 | 1.000000 | 0.750000 | 0.857143 | 0.798077 | 0.851649 | `true` | 132.791000 | 33351 | 6 | 8 | 0.268077 |
| elo-merchant-category-recommendation | tc3_fault_injected | rule_based | try1 | 0.600000 | 0.214286 | 0.315789 | 1.000000 | 0.500000 | 0.666667 | 0.407894 | 0.491228 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc3_fault_injected | single_llm | try1 | 0.916667 | 0.785714 | 0.846154 | 1.000000 | 0.500000 | 0.666667 | 0.673077 | 0.756410 | `true` | 56.957000 | 4466 | 1 | 0 | 0.071303 |
| elo-merchant-category-recommendation | tc3_fault_injected | single_llm | try2 | 0.900000 | 0.642857 | 0.750000 | 1.000000 | 0.750000 | 0.857143 | 0.750000 | 0.803571 | `true` | 50.853000 | 3756 | 1 | 0 | 0.061630 |
| elo-merchant-category-recommendation | tc3_fault_injected | single_llm | try3 | 0.888889 | 0.571429 | 0.695652 | 1.000000 | 0.750000 | 0.857143 | 0.722826 | 0.776398 | `true` | 36.673000 | 2796 | 1 | 0 | 0.047230 |
| elo-merchant-category-recommendation | tc3_fault_injected | single_llm | try4 | 0.909091 | 0.714286 | 0.800000 | 1.000000 | 0.750000 | 0.857143 | 0.775000 | 0.828572 | `true` | 45.443000 | 3637 | 1 | 0 | 0.059845 |
| elo-merchant-category-recommendation | tc3_fault_injected | single_llm | try5 | 0.800000 | 0.571429 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 42.298000 | 3377 | 1 | 0 | 0.054968 |
| elo-merchant-category-recommendation | tc4_mixed_history | claude_code | try1 | 0.800000 | 0.363636 | 0.500000 | 1.000000 | 0.666667 | 0.800000 | 0.583333 | 0.650000 | `true` | 103.473469 | 4660 | `null` | 23 | 0.288315 |
| elo-merchant-category-recommendation | tc4_mixed_history | claude_code | try2 | 1.000000 | 0.545455 | 0.705882 | 1.000000 | 0.666667 | 0.800000 | 0.686275 | 0.752941 | `true` | 84.390012 | 2310 | `null` | 17 | 0.185960 |
| elo-merchant-category-recommendation | tc4_mixed_history | claude_code | try3 | 1.000000 | 0.272727 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | `true` | 83.144428 | 2233 | `null` | 20 | 0.252625 |
| elo-merchant-category-recommendation | tc4_mixed_history | claude_code | try4 | 1.000000 | 0.545455 | 0.705882 | 1.000000 | 1.000000 | 1.000000 | 0.852941 | 0.852941 | `true` | 102.621930 | 3004 | `null` | 26 | 0.286584 |
| elo-merchant-category-recommendation | tc4_mixed_history | claude_code | try5 | 1.000000 | 0.181818 | 0.307692 | 1.000000 | 1.000000 | 1.000000 | 0.653846 | 0.653846 | `true` | 129.615971 | 2732 | `null` | 20 | 0.270165 |
| elo-merchant-category-recommendation | tc4_mixed_history | generic_agent | try1 | 0.857143 | 0.545455 | 0.666667 | 1.000000 | 0.666667 | 0.800000 | 0.666667 | 0.733334 | `true` | 128.993000 | 24346 | 7 | 7 | 0.198356 |
| elo-merchant-category-recommendation | tc4_mixed_history | generic_agent | try2 | 0.750000 | 0.545455 | 0.631579 | 1.000000 | 0.666667 | 0.800000 | 0.649123 | 0.715790 | `true` | 109.766000 | 18794 | 5 | 8 | 0.156627 |
| elo-merchant-category-recommendation | tc4_mixed_history | generic_agent | try3 | 0.750000 | 0.545455 | 0.631579 | 1.000000 | 0.666667 | 0.800000 | 0.649123 | 0.715790 | `true` | 111.574000 | 17917 | 3 | 4 | 0.143241 |
| elo-merchant-category-recommendation | tc4_mixed_history | generic_agent | try4 | 0.800000 | 0.363636 | 0.500000 | 1.000000 | 0.666667 | 0.800000 | 0.583333 | 0.650000 | `true` | 156.185000 | 24882 | 7 | 8 | 0.204483 |
| elo-merchant-category-recommendation | tc4_mixed_history | generic_agent | try5 | 0.833333 | 0.454545 | 0.588235 | 1.000000 | 0.333333 | 0.500000 | 0.460784 | 0.544118 | `false` | 95.110000 | 16444 | 5 | 6 | 0.142408 |
| elo-merchant-category-recommendation | tc4_mixed_history | proposed_agent | try1 | 0.888889 | 0.727273 | 0.800000 | 1.000000 | 0.666667 | 0.800000 | 0.733334 | 0.800000 | `true` | 150.726000 | 35663 | 6 | 7 | 0.271112 |
| elo-merchant-category-recommendation | tc4_mixed_history | proposed_agent | try2 | 0.875000 | 0.636364 | 0.736842 | 1.000000 | 0.666667 | 0.800000 | 0.701755 | 0.768421 | `true` | 158.403000 | 31921 | 5 | 5 | 0.243244 |
| elo-merchant-category-recommendation | tc4_mixed_history | proposed_agent | try3 | 0.800000 | 0.727273 | 0.761905 | 1.000000 | 0.333333 | 0.500000 | 0.547619 | 0.630953 | `true` | 185.765000 | 43192 | 7 | 8 | 0.342977 |
| elo-merchant-category-recommendation | tc4_mixed_history | proposed_agent | try4 | 0.888889 | 0.727273 | 0.800000 | 1.000000 | 0.666667 | 0.800000 | 0.733334 | 0.800000 | `true` | 178.155000 | 44375 | 7 | 8 | 0.342108 |
| elo-merchant-category-recommendation | tc4_mixed_history | proposed_agent | try5 | 0.900000 | 0.818182 | 0.857143 | 1.000000 | 0.666667 | 0.800000 | 0.761905 | 0.828572 | `true` | 189.918000 | 41019 | 7 | 9 | 0.324826 |
| elo-merchant-category-recommendation | tc4_mixed_history | rule_based | try1 | 0.400000 | 0.181818 | 0.250000 | 0.500000 | 0.333333 | 0.400000 | 0.291666 | 0.325000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc4_mixed_history | single_llm | try1 | 0.875000 | 0.636364 | 0.736842 | 1.000000 | 0.666667 | 0.800000 | 0.701755 | 0.768421 | `true` | 46.185000 | 3392 | 1 | 0 | 0.055097 |
| elo-merchant-category-recommendation | tc4_mixed_history | single_llm | try2 | 1.000000 | 0.272727 | 0.428571 | 1.000000 | 0.333333 | 0.500000 | 0.380952 | 0.464286 | `false` | 39.150000 | 2545 | 1 | 0 | 0.042392 |
| elo-merchant-category-recommendation | tc4_mixed_history | single_llm | try3 | 0.900000 | 0.818182 | 0.857143 | 1.000000 | 0.666667 | 0.800000 | 0.761905 | 0.828572 | `true` | 44.316000 | 3185 | 1 | 0 | 0.053095 |
| elo-merchant-category-recommendation | tc4_mixed_history | single_llm | try4 | 1.000000 | 0.818182 | 0.900000 | 1.000000 | 0.666667 | 0.800000 | 0.783334 | 0.850000 | `true` | 55.478000 | 4011 | 1 | 0 | 0.065485 |
| elo-merchant-category-recommendation | tc4_mixed_history | single_llm | try5 | 0.700000 | 0.636364 | 0.666667 | 1.000000 | 0.666667 | 0.800000 | 0.666667 | 0.733334 | `true` | 64.383000 | 4668 | 1 | 0 | 0.075340 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| elo-merchant-category-recommendation | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.828398 | 0.757143 | 0.788638 | 1.000000 | 1.000000 | 1.000000 | 0.894319 | 0.894319 | 0.000584 | 104.511655 | 3761.600000 | `null` | 20.800000 | 0.281944 |
| elo-merchant-category-recommendation | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.792424 | 0.657143 | 0.718154 | 1.000000 | 1.000000 | 1.000000 | 0.859077 | 0.859077 | 0.000600 | 131.974200 | 23192.000000 | 5.200000 | 6.000000 | 0.182390 |
| elo-merchant-category-recommendation | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 0.571429 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | 0.000000 | 3300 | `null` | `null` | `null` | `null` |
| elo-merchant-category-recommendation | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.836410 | 0.771428 | 0.801297 | 1.000000 | 1.000000 | 1.000000 | 0.900648 | 0.900648 | 0.000485 | 153.744200 | 30742.000000 | 5.200000 | 6.200000 | 0.244643 |
| elo-merchant-category-recommendation | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.500000 | 0.214286 | 0.300000 | 1.000000 | 1.000000 | 1.000000 | 0.650000 | 0.650000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.788461 | 0.685714 | 0.733334 | 1.000000 | 1.000000 | 1.000000 | 0.866666 | 0.866666 | 0.000500 | 12.795000 | 1059.200000 | 1.000000 | 0.000000 | 0.044281 |
| elo-merchant-category-recommendation | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.820000 | 0.420000 | 0.549872 | 0.200000 | 1.000000 | 0.200000 | 0.774936 | 0.374936 | 0.005245 | 264.542002 | 2881.400000 | `null` | 30.800000 | 0.512543 |
| elo-merchant-category-recommendation | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.740953 | 0.460000 | 0.565490 | 0.200000 | 1.000000 | 0.200000 | 0.782745 | 0.382745 | 0.001492 | 106.023200 | 20732.600000 | 5.000000 | 5.200000 | 0.163766 |
| elo-merchant-category-recommendation | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.842064 | 0.660000 | 0.738356 | 1.000000 | 1.000000 | 1.000000 | 0.869178 | 0.869178 | 0.001873 | 112.413000 | 27297.000000 | 5.200000 | 5.600000 | 0.212743 |
| elo-merchant-category-recommendation | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.400000 | 0.200000 | 0.266667 | 0.000000 | 1.000000 | 0.000000 | 0.633333 | 0.133333 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.865556 | 0.740000 | 0.796257 | 0.800000 | 1.000000 | 0.800000 | 0.898129 | 0.798129 | 0.000640 | 60.482400 | 4524.800000 | 1.000000 | 0.000000 | 0.072776 |
| elo-merchant-category-recommendation | tc3_fault_injected | claude_code | 5 | `true` | 0.800000 | 0.863492 | 0.442857 | 0.582940 | 1.000000 | 0.850000 | 0.904762 | 0.716470 | 0.743851 | 0.016858 | 136.875232 | 2649.600000 | `null` | 24.800000 | 0.329295 |
| elo-merchant-category-recommendation | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 0.891025 | 0.585714 | 0.703271 | 1.000000 | 0.650000 | 0.780953 | 0.676635 | 0.742112 | 0.006577 | 130.411600 | 23113.600000 | 4.000000 | 4.800000 | 0.179367 |
| elo-merchant-category-recommendation | tc3_fault_injected | proposed_agent | 5 | `true` | 1.000000 | 0.893636 | 0.685714 | 0.773599 | 1.000000 | 0.550000 | 0.704762 | 0.661799 | 0.739181 | 0.004754 | 140.768200 | 31279.600000 | 5.600000 | 6.400000 | 0.250547 |
| elo-merchant-category-recommendation | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.600000 | 0.214286 | 0.315789 | 1.000000 | 0.500000 | 0.666667 | 0.407894 | 0.491228 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 0.882929 | 0.657143 | 0.751695 | 1.000000 | 0.700000 | 0.819048 | 0.725847 | 0.785371 | 0.001220 | 46.444800 | 3606.400000 | 1.000000 | 0.000000 | 0.058995 |
| elo-merchant-category-recommendation | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 0.960000 | 0.381818 | 0.529605 | 1.000000 | 0.866667 | 0.920000 | 0.698136 | 0.724803 | 0.007901 | 100.649162 | 2987.800000 | `null` | 21.200000 | 0.256730 |
| elo-merchant-category-recommendation | tc4_mixed_history | generic_agent | 5 | `true` | 0.800000 | 0.798095 | 0.490909 | 0.603612 | 1.000000 | 0.600000 | 0.740000 | 0.601806 | 0.671806 | 0.005783 | 120.325600 | 20476.600000 | 5.400000 | 6.600000 | 0.169023 |
| elo-merchant-category-recommendation | tc4_mixed_history | proposed_agent | 5 | `true` | 1.000000 | 0.870556 | 0.727273 | 0.791178 | 1.000000 | 0.600000 | 0.740000 | 0.695589 | 0.765589 | 0.005836 | 172.593400 | 39234.000000 | 6.400000 | 7.400000 | 0.304854 |
| elo-merchant-category-recommendation | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.400000 | 0.181818 | 0.250000 | 0.500000 | 0.333333 | 0.400000 | 0.291666 | 0.325000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc4_mixed_history | single_llm | 5 | `true` | 0.800000 | 0.895000 | 0.636364 | 0.717845 | 1.000000 | 0.600000 | 0.740000 | 0.658923 | 0.728923 | 0.021049 | 49.902400 | 3560.200000 | 1.000000 | 0.000000 | 0.058282 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 0.950000 | 0.867973 | 0.500455 | 0.612764 | 0.800000 | 0.929167 | 0.756190 | 0.770965 | 0.684477 | 0.007647 | 151.644513 | 3070.100000 | `null` | 24.400000 | 0.345128 |
| generic_agent | 4 | 1.000000 | 5.000000 | 0.950000 | 0.805624 | 0.548442 | 0.647632 | 0.800000 | 0.812500 | 0.680238 | 0.730066 | 0.663935 | 0.003613 | 122.183650 | 21878.700000 | 4.900000 | 5.650000 | 0.173636 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.571429 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | 0.000000 | 3300.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.860667 | 0.711104 | 0.776108 | 1.000000 | 0.787500 | 0.861190 | 0.781803 | 0.818649 | 0.003237 | 144.879700 | 32138.150000 | 5.600000 | 6.400000 | 0.253197 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.475000 | 0.202598 | 0.283114 | 0.625000 | 0.708333 | 0.516667 | 0.495723 | 0.399890 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 0.950000 | 0.857986 | 0.679805 | 0.749783 | 0.950000 | 0.825000 | 0.839762 | 0.787391 | 0.794772 | 0.005852 | 42.406150 | 3187.650000 | 1.000000 | 0.000000 | 0.058583 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task elo-merchant-category-recommendation --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/elo-merchant-category-recommendation-primary.md
```
