# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `elo-merchant-category-recommendation`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.904762`
- Mean Add Precision: `0.795269`
- Mean Add Recall: `0.519551`
- Mean Add F1: `0.609054`
- Mean Remove Precision: `0.842857`
- Mean Remove Recall: `0.821429`
- Mean Remove F1: `0.743628`
- Mean Task Completion Score: `0.715241`
- Mean Strict Task Completion Score: `0.676341`
- Mean Task Completion Variance: `0.004030`
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
| elo-merchant-category-recommendation | 21 | 6 | 0.904762 | 4.047619 | 0.795269 | 0.519551 | 0.609054 | 0.842857 | 0.821429 | 0.743628 | 0.715241 | 0.676341 | 0.004030 | 244.974098 | 15068.650000 | 2.875000 | 7.290000 | 0.166109 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| elo-merchant-category-recommendation | tc1_from_scratch | claude_code | try1 | 0.875000 | 0.875000 | 0.875000 | 1.000000 | 1.000000 | 1.000000 | 0.937500 | 0.937500 | `true` | 105.555035 | 4003 | `null` | 23 | 0.268478 |
| elo-merchant-category-recommendation | tc1_from_scratch | claude_code | try2 | 0.823529 | 0.875000 | 0.848485 | 1.000000 | 1.000000 | 1.000000 | 0.924243 | 0.924243 | `true` | 107.805091 | 4319 | `null` | 20 | 0.289698 |
| elo-merchant-category-recommendation | tc1_from_scratch | claude_code | try3 | 0.857143 | 0.750000 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 98.790380 | 3269 | `null` | 29 | 0.266461 |
| elo-merchant-category-recommendation | tc1_from_scratch | claude_code | try4 | 0.857143 | 0.750000 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 120.522328 | 4224 | `null` | 14 | 0.323705 |
| elo-merchant-category-recommendation | tc1_from_scratch | claude_code | try5 | 0.846154 | 0.687500 | 0.758621 | 1.000000 | 1.000000 | 1.000000 | 0.879310 | 0.879310 | `true` | 89.885441 | 2993 | `null` | 18 | 0.261378 |
| elo-merchant-category-recommendation | tc1_from_scratch | generic_agent | try1 | 0.846154 | 0.687500 | 0.758621 | 1.000000 | 1.000000 | 1.000000 | 0.879310 | 0.879310 | `true` | 149.069000 | 23929 | 4 | 3 | 0.205738 |
| elo-merchant-category-recommendation | tc1_from_scratch | generic_agent | try2 | 0.857143 | 0.750000 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 106.823000 | 23248 | 4 | 5 | 0.168533 |
| elo-merchant-category-recommendation | tc1_from_scratch | generic_agent | try3 | 0.833333 | 0.625000 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 109.888000 | 23416 | 5 | 8 | 0.181781 |
| elo-merchant-category-recommendation | tc1_from_scratch | generic_agent | try4 | 0.769231 | 0.625000 | 0.689655 | 1.000000 | 1.000000 | 1.000000 | 0.844828 | 0.844828 | `true` | 185.134000 | 23846 | 8 | 7 | 0.193039 |
| elo-merchant-category-recommendation | tc1_from_scratch | generic_agent | try5 | 0.750000 | 0.562500 | 0.642857 | 1.000000 | 1.000000 | 1.000000 | 0.821429 | 0.821429 | `true` | 108.957000 | 21521 | 5 | 7 | 0.162857 |
| elo-merchant-category-recommendation | tc1_from_scratch | human | human_tc1_sean_kraemer_v4_manual_rebuild | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 3300 | `null` | `null` | `null` | `null` |
| elo-merchant-category-recommendation | tc1_from_scratch | proposed_agent | try1 | 0.866667 | 0.812500 | 0.838710 | 1.000000 | 1.000000 | 1.000000 | 0.919355 | 0.919355 | `true` | 214.050000 | 32920 | 5 | 5 | 0.310910 |
| elo-merchant-category-recommendation | tc1_from_scratch | proposed_agent | try2 | 0.928571 | 0.812500 | 0.866667 | 1.000000 | 1.000000 | 1.000000 | 0.933334 | 0.933334 | `true` | 269.301000 | 50550 | 7 | 10 | 0.367971 |
| elo-merchant-category-recommendation | tc1_from_scratch | proposed_agent | try3 | 0.764706 | 0.812500 | 0.787879 | 1.000000 | 1.000000 | 1.000000 | 0.893939 | 0.893939 | `true` | 99.031000 | 23380 | 4 | 4 | 0.170121 |
| elo-merchant-category-recommendation | tc1_from_scratch | proposed_agent | try4 | 0.928571 | 0.812500 | 0.866667 | 1.000000 | 1.000000 | 1.000000 | 0.933334 | 0.933334 | `true` | 88.859000 | 22391 | 5 | 6 | 0.178041 |
| elo-merchant-category-recommendation | tc1_from_scratch | proposed_agent | try5 | 0.800000 | 0.750000 | 0.774194 | 1.000000 | 1.000000 | 1.000000 | 0.887097 | 0.887097 | `true` | 97.480000 | 24469 | 5 | 6 | 0.196173 |
| elo-merchant-category-recommendation | tc1_from_scratch | rule_based | try1 | 0.500000 | 0.187500 | 0.272727 | 1.000000 | 1.000000 | 1.000000 | 0.636363 | 0.636363 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc1_from_scratch | single_llm | try1 | 0.857143 | 0.750000 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 12.731000 | 1013 | 1 | 0 | 0.078383 |
| elo-merchant-category-recommendation | tc1_from_scratch | single_llm | try2 | 0.857143 | 0.750000 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 12.266000 | 1040 | 1 | 0 | 0.020796 |
| elo-merchant-category-recommendation | tc1_from_scratch | single_llm | try3 | 0.785714 | 0.687500 | 0.733333 | 1.000000 | 1.000000 | 1.000000 | 0.866667 | 0.866667 | `true` | 12.435000 | 1057 | 1 | 0 | 0.021051 |
| elo-merchant-category-recommendation | tc1_from_scratch | single_llm | try4 | 0.733333 | 0.687500 | 0.709677 | 1.000000 | 1.000000 | 1.000000 | 0.854839 | 0.854839 | `true` | 12.567000 | 1024 | 1 | 0 | 0.020556 |
| elo-merchant-category-recommendation | tc1_from_scratch | single_llm | try5 | 0.857143 | 0.750000 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 13.976000 | 1162 | 1 | 0 | 0.080618 |
| elo-merchant-category-recommendation | tc2_partial_good | claude_code | try1 | 0.800000 | 0.333333 | 0.470588 | 0.000000 | 1.000000 | 0.000000 | 0.735294 | 0.235294 | `true` | 42.278372 | 2094 | `null` | 9 | 0.160817 |
| elo-merchant-category-recommendation | tc2_partial_good | claude_code | try2 | 0.833333 | 0.416667 | 0.555556 | 0.000000 | 1.000000 | 0.000000 | 0.777778 | 0.277778 | `true` | 97.726163 | 1794 | `null` | 15 | 0.116701 |
| elo-merchant-category-recommendation | tc2_partial_good | claude_code | try3 | 0.666667 | 0.166667 | 0.266667 | 0.000000 | 1.000000 | 0.000000 | 0.633333 | 0.133333 | `true` | 91.100677 | 3082 | `null` | 22 | 0.245477 |
| elo-merchant-category-recommendation | tc2_partial_good | claude_code | try4 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 449.704050 | 4142 | `null` | 66 | 1.231438 |
| elo-merchant-category-recommendation | tc2_partial_good | claude_code | try5 | 0.800000 | 0.333333 | 0.470588 | 0.000000 | 1.000000 | 0.000000 | 0.735294 | 0.235294 | `true` | 641.900751 | 3295 | `null` | 42 | 0.808283 |
| elo-merchant-category-recommendation | tc2_partial_good | generic_agent | try1 | 0.714286 | 0.416667 | 0.526316 | 0.000000 | 1.000000 | 0.000000 | 0.763158 | 0.263158 | `true` | 129.839000 | 26037 | 5 | 5 | 0.195961 |
| elo-merchant-category-recommendation | tc2_partial_good | generic_agent | try2 | 0.666667 | 0.333333 | 0.444444 | 0.000000 | 1.000000 | 0.000000 | 0.722222 | 0.222222 | `true` | 76.995000 | 15121 | 6 | 5 | 0.124897 |
| elo-merchant-category-recommendation | tc2_partial_good | generic_agent | try3 | 0.857143 | 0.500000 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 116.873000 | 23159 | 5 | 5 | 0.185338 |
| elo-merchant-category-recommendation | tc2_partial_good | generic_agent | try4 | 0.666667 | 0.333333 | 0.444444 | 0.000000 | 1.000000 | 0.000000 | 0.722222 | 0.222222 | `true` | 93.966000 | 17747 | 4 | 5 | 0.139227 |
| elo-merchant-category-recommendation | tc2_partial_good | generic_agent | try5 | 0.800000 | 0.333333 | 0.470588 | 0.000000 | 1.000000 | 0.000000 | 0.735294 | 0.235294 | `true` | 112.443000 | 21599 | 5 | 6 | 0.173405 |
| elo-merchant-category-recommendation | tc2_partial_good | proposed_agent | try1 | 0.900000 | 0.750000 | 0.818182 | 1.000000 | 1.000000 | 1.000000 | 0.909091 | 0.909091 | `true` | 87.439000 | 23906 | 5 | 5 | 0.180431 |
| elo-merchant-category-recommendation | tc2_partial_good | proposed_agent | try2 | 0.888889 | 0.666667 | 0.761905 | 1.000000 | 1.000000 | 1.000000 | 0.880953 | 0.880953 | `true` | 123.594000 | 28876 | 6 | 7 | 0.229840 |
| elo-merchant-category-recommendation | tc2_partial_good | proposed_agent | try3 | 0.900000 | 0.750000 | 0.818182 | 1.000000 | 1.000000 | 1.000000 | 0.909091 | 0.909091 | `true` | 118.462000 | 29685 | 6 | 7 | 0.229350 |
| elo-merchant-category-recommendation | tc2_partial_good | proposed_agent | try4 | 0.777778 | 0.583333 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 123.406000 | 31421 | 5 | 6 | 0.242985 |
| elo-merchant-category-recommendation | tc2_partial_good | proposed_agent | try5 | 0.909091 | 0.833333 | 0.869565 | 1.000000 | 1.000000 | 1.000000 | 0.934783 | 0.934783 | `true` | 109.164000 | 22597 | 4 | 3 | 0.181111 |
| elo-merchant-category-recommendation | tc2_partial_good | rule_based | try1 | 0.400000 | 0.166667 | 0.235294 | 0.000000 | 1.000000 | 0.000000 | 0.617647 | 0.117647 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc2_partial_good | single_llm | try1 | 0.818182 | 0.750000 | 0.782609 | 1.000000 | 1.000000 | 1.000000 | 0.891304 | 0.891304 | `true` | 63.168000 | 4909 | 1 | 0 | 0.077972 |
| elo-merchant-category-recommendation | tc2_partial_good | single_llm | try2 | 0.833333 | 0.833333 | 0.833333 | 0.000000 | 1.000000 | 0.000000 | 0.916667 | 0.416666 | `true` | 59.283000 | 4344 | 1 | 0 | 0.069497 |
| elo-merchant-category-recommendation | tc2_partial_good | single_llm | try3 | 0.900000 | 0.750000 | 0.818182 | 1.000000 | 1.000000 | 1.000000 | 0.909091 | 0.909091 | `true` | 76.324000 | 5663 | 1 | 0 | 0.090227 |
| elo-merchant-category-recommendation | tc2_partial_good | single_llm | try4 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 45.366000 | 3442 | 1 | 0 | 0.056912 |
| elo-merchant-category-recommendation | tc2_partial_good | single_llm | try5 | 0.900000 | 0.750000 | 0.818182 | 1.000000 | 1.000000 | 1.000000 | 0.909091 | 0.909091 | `true` | 58.271000 | 4266 | 1 | 0 | 0.069272 |
| elo-merchant-category-recommendation | tc3_fault_injected | claude_code | try1 | 0.714286 | 0.312500 | 0.434783 | 1.000000 | 0.500000 | 0.666667 | 0.467391 | 0.550725 | `false` | 81.772361 | 2191 | `null` | 13 | 0.184998 |
| elo-merchant-category-recommendation | tc3_fault_injected | claude_code | try2 | 1.000000 | 0.375000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 261.700832 | 2411 | `null` | 37 | 0.533662 |
| elo-merchant-category-recommendation | tc3_fault_injected | claude_code | try3 | 0.909091 | 0.625000 | 0.740741 | 1.000000 | 1.000000 | 1.000000 | 0.870370 | 0.870370 | `true` | 125.233037 | 2763 | `null` | 25 | 0.235314 |
| elo-merchant-category-recommendation | tc3_fault_injected | claude_code | try4 | 0.857143 | 0.375000 | 0.521739 | 1.000000 | 1.000000 | 1.000000 | 0.760869 | 0.760869 | `true` | 120.805323 | 3000 | `null` | 28 | 0.384396 |
| elo-merchant-category-recommendation | tc3_fault_injected | claude_code | try5 | 0.857143 | 0.375000 | 0.521739 | 1.000000 | 0.750000 | 0.857143 | 0.635869 | 0.689441 | `true` | 94.864606 | 2883 | `null` | 21 | 0.308104 |
| elo-merchant-category-recommendation | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.562500 | 0.720000 | 1.000000 | 0.750000 | 0.857143 | 0.735000 | 0.788571 | `true` | 125.264000 | 22648 | 4 | 5 | 0.177821 |
| elo-merchant-category-recommendation | tc3_fault_injected | generic_agent | try2 | 0.888889 | 0.500000 | 0.640000 | 1.000000 | 0.500000 | 0.666667 | 0.570000 | 0.653334 | `true` | 137.053000 | 21109 | 4 | 4 | 0.162041 |
| elo-merchant-category-recommendation | tc3_fault_injected | generic_agent | try3 | 0.909091 | 0.625000 | 0.740741 | 1.000000 | 0.750000 | 0.857143 | 0.745370 | 0.798942 | `true` | 162.369000 | 24833 | 4 | 4 | 0.191053 |
| elo-merchant-category-recommendation | tc3_fault_injected | generic_agent | try4 | 0.857143 | 0.375000 | 0.521739 | 1.000000 | 0.750000 | 0.857143 | 0.635869 | 0.689441 | `true` | 107.951000 | 21883 | 4 | 5 | 0.162553 |
| elo-merchant-category-recommendation | tc3_fault_injected | generic_agent | try5 | 0.800000 | 0.500000 | 0.615385 | 1.000000 | 0.500000 | 0.666667 | 0.557692 | 0.641026 | `true` | 119.421000 | 25095 | 4 | 6 | 0.203367 |
| elo-merchant-category-recommendation | tc3_fault_injected | proposed_agent | try1 | 1.000000 | 0.687500 | 0.814815 | 1.000000 | 0.500000 | 0.666667 | 0.657407 | 0.740741 | `true` | 120.046000 | 26840 | 5 | 5 | 0.213169 |
| elo-merchant-category-recommendation | tc3_fault_injected | proposed_agent | try2 | 0.857143 | 0.750000 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 141.642000 | 31192 | 6 | 7 | 0.259431 |
| elo-merchant-category-recommendation | tc3_fault_injected | proposed_agent | try3 | 0.916667 | 0.687500 | 0.785714 | 1.000000 | 0.500000 | 0.666667 | 0.642857 | 0.726190 | `true` | 128.002000 | 30401 | 6 | 7 | 0.238048 |
| elo-merchant-category-recommendation | tc3_fault_injected | proposed_agent | try4 | 0.846154 | 0.687500 | 0.758621 | 1.000000 | 0.500000 | 0.666667 | 0.629310 | 0.712644 | `true` | 181.360000 | 34614 | 5 | 5 | 0.274012 |
| elo-merchant-category-recommendation | tc3_fault_injected | proposed_agent | try5 | 0.928571 | 0.812500 | 0.866667 | 1.000000 | 0.750000 | 0.857143 | 0.808334 | 0.861905 | `true` | 132.791000 | 33351 | 6 | 8 | 0.268077 |
| elo-merchant-category-recommendation | tc3_fault_injected | rule_based | try1 | 0.600000 | 0.187500 | 0.285714 | 1.000000 | 0.500000 | 0.666667 | 0.392857 | 0.476191 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc3_fault_injected | single_llm | try1 | 0.928571 | 0.812500 | 0.866667 | 1.000000 | 0.500000 | 0.666667 | 0.683334 | 0.766667 | `true` | 56.957000 | 4466 | 1 | 0 | 0.071303 |
| elo-merchant-category-recommendation | tc3_fault_injected | single_llm | try2 | 0.916667 | 0.687500 | 0.785714 | 1.000000 | 0.750000 | 0.857143 | 0.767857 | 0.821429 | `true` | 50.853000 | 3756 | 1 | 0 | 0.061630 |
| elo-merchant-category-recommendation | tc3_fault_injected | single_llm | try3 | 0.909091 | 0.625000 | 0.740741 | 1.000000 | 0.750000 | 0.857143 | 0.745370 | 0.798942 | `true` | 36.673000 | 2796 | 1 | 0 | 0.047230 |
| elo-merchant-category-recommendation | tc3_fault_injected | single_llm | try4 | 0.923077 | 0.750000 | 0.827586 | 1.000000 | 0.750000 | 0.857143 | 0.788793 | 0.842364 | `true` | 45.443000 | 3637 | 1 | 0 | 0.059845 |
| elo-merchant-category-recommendation | tc3_fault_injected | single_llm | try5 | 0.833333 | 0.625000 | 0.714286 | 1.000000 | 0.750000 | 0.857143 | 0.732143 | 0.785714 | `true` | 42.298000 | 3377 | 1 | 0 | 0.054968 |
| elo-merchant-category-recommendation | tc4_mixed_history | claude_code | try1 | 0.800000 | 0.307692 | 0.444444 | 1.000000 | 0.666667 | 0.800000 | 0.555555 | 0.622222 | `true` | 103.473469 | 4660 | `null` | 23 | 0.288315 |
| elo-merchant-category-recommendation | tc4_mixed_history | claude_code | try2 | 1.000000 | 0.461538 | 0.631579 | 1.000000 | 0.666667 | 0.800000 | 0.649123 | 0.715790 | `true` | 84.390012 | 2310 | `null` | 17 | 0.185960 |
| elo-merchant-category-recommendation | tc4_mixed_history | claude_code | try3 | 1.000000 | 0.230769 | 0.375000 | 1.000000 | 1.000000 | 1.000000 | 0.687500 | 0.687500 | `true` | 83.144428 | 2233 | `null` | 20 | 0.252625 |
| elo-merchant-category-recommendation | tc4_mixed_history | claude_code | try4 | 1.000000 | 0.461538 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 102.621930 | 3004 | `null` | 26 | 0.286584 |
| elo-merchant-category-recommendation | tc4_mixed_history | claude_code | try5 | 1.000000 | 0.153846 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | `true` | 129.615971 | 2732 | `null` | 20 | 0.270165 |
| elo-merchant-category-recommendation | tc4_mixed_history | generic_agent | try1 | 0.857143 | 0.461538 | 0.600000 | 1.000000 | 0.666667 | 0.800000 | 0.633333 | 0.700000 | `true` | 128.993000 | 24346 | 7 | 7 | 0.198356 |
| elo-merchant-category-recommendation | tc4_mixed_history | generic_agent | try2 | 0.750000 | 0.461538 | 0.571429 | 1.000000 | 0.666667 | 0.800000 | 0.619048 | 0.685715 | `true` | 109.766000 | 18794 | 5 | 8 | 0.156627 |
| elo-merchant-category-recommendation | tc4_mixed_history | generic_agent | try3 | 0.750000 | 0.461538 | 0.571429 | 1.000000 | 0.666667 | 0.800000 | 0.619048 | 0.685715 | `true` | 111.574000 | 17917 | 3 | 4 | 0.143241 |
| elo-merchant-category-recommendation | tc4_mixed_history | generic_agent | try4 | 0.800000 | 0.307692 | 0.444444 | 1.000000 | 0.666667 | 0.800000 | 0.555555 | 0.622222 | `true` | 156.185000 | 24882 | 7 | 8 | 0.204483 |
| elo-merchant-category-recommendation | tc4_mixed_history | generic_agent | try5 | 0.833333 | 0.384615 | 0.526316 | 1.000000 | 0.333333 | 0.500000 | 0.429824 | 0.513158 | `false` | 95.110000 | 16444 | 5 | 6 | 0.142408 |
| elo-merchant-category-recommendation | tc4_mixed_history | proposed_agent | try1 | 0.909091 | 0.769231 | 0.833333 | 1.000000 | 0.666667 | 0.800000 | 0.750000 | 0.816666 | `true` | 150.726000 | 35663 | 6 | 7 | 0.271112 |
| elo-merchant-category-recommendation | tc4_mixed_history | proposed_agent | try2 | 0.900000 | 0.692308 | 0.782609 | 1.000000 | 0.666667 | 0.800000 | 0.724638 | 0.791305 | `true` | 158.403000 | 31921 | 5 | 5 | 0.243244 |
| elo-merchant-category-recommendation | tc4_mixed_history | proposed_agent | try3 | 0.833333 | 0.769231 | 0.800000 | 1.000000 | 0.333333 | 0.500000 | 0.566666 | 0.650000 | `true` | 185.765000 | 43192 | 7 | 8 | 0.342977 |
| elo-merchant-category-recommendation | tc4_mixed_history | proposed_agent | try4 | 0.909091 | 0.769231 | 0.833333 | 1.000000 | 0.666667 | 0.800000 | 0.750000 | 0.816666 | `true` | 178.155000 | 44375 | 7 | 8 | 0.342108 |
| elo-merchant-category-recommendation | tc4_mixed_history | proposed_agent | try5 | 0.916667 | 0.846154 | 0.880000 | 1.000000 | 0.666667 | 0.800000 | 0.773334 | 0.840000 | `true` | 189.918000 | 41019 | 7 | 9 | 0.324826 |
| elo-merchant-category-recommendation | tc4_mixed_history | rule_based | try1 | 0.400000 | 0.153846 | 0.222222 | 0.500000 | 0.333333 | 0.400000 | 0.277778 | 0.311111 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc4_mixed_history | single_llm | try1 | 0.900000 | 0.692308 | 0.782609 | 1.000000 | 0.666667 | 0.800000 | 0.724638 | 0.791305 | `true` | 46.185000 | 3392 | 1 | 0 | 0.055097 |
| elo-merchant-category-recommendation | tc4_mixed_history | single_llm | try2 | 1.000000 | 0.230769 | 0.375000 | 1.000000 | 0.333333 | 0.500000 | 0.354166 | 0.437500 | `false` | 39.150000 | 2545 | 1 | 0 | 0.042392 |
| elo-merchant-category-recommendation | tc4_mixed_history | single_llm | try3 | 0.916667 | 0.846154 | 0.880000 | 1.000000 | 0.666667 | 0.800000 | 0.773334 | 0.840000 | `true` | 44.316000 | 3185 | 1 | 0 | 0.053095 |
| elo-merchant-category-recommendation | tc4_mixed_history | single_llm | try4 | 1.000000 | 0.846154 | 0.916667 | 1.000000 | 0.666667 | 0.800000 | 0.791667 | 0.858334 | `true` | 55.478000 | 4011 | 1 | 0 | 0.065485 |
| elo-merchant-category-recommendation | tc4_mixed_history | single_llm | try5 | 0.750000 | 0.692308 | 0.720000 | 1.000000 | 0.666667 | 0.800000 | 0.693334 | 0.760000 | `true` | 64.383000 | 4668 | 1 | 0 | 0.075340 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| elo-merchant-category-recommendation | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.851794 | 0.787500 | 0.816421 | 1.000000 | 1.000000 | 1.000000 | 0.908211 | 0.908211 | 0.000417 | 104.511655 | 3761.600000 | `null` | 20.800000 | 0.281944 |
| elo-merchant-category-recommendation | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.811172 | 0.650000 | 0.721084 | 1.000000 | 1.000000 | 1.000000 | 0.860542 | 0.860542 | 0.000739 | 131.974200 | 23192.000000 | 5.200000 | 6.000000 | 0.182390 |
| elo-merchant-category-recommendation | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | 0.000000 | 3300 | `null` | `null` | `null` | `null` |
| elo-merchant-category-recommendation | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.857703 | 0.800000 | 0.826823 | 1.000000 | 1.000000 | 1.000000 | 0.913412 | 0.913412 | 0.000380 | 153.744200 | 30742.000000 | 5.200000 | 6.200000 | 0.244643 |
| elo-merchant-category-recommendation | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.500000 | 0.187500 | 0.272727 | 1.000000 | 1.000000 | 1.000000 | 0.636363 | 0.636363 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.818095 | 0.725000 | 0.768602 | 1.000000 | 1.000000 | 1.000000 | 0.884301 | 0.884301 | 0.000384 | 12.795000 | 1059.200000 | 1.000000 | 0.000000 | 0.044281 |
| elo-merchant-category-recommendation | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.820000 | 0.350000 | 0.486013 | 0.200000 | 1.000000 | 0.200000 | 0.743006 | 0.343006 | 0.004303 | 264.542002 | 2881.400000 | `null` | 30.800000 | 0.512543 |
| elo-merchant-category-recommendation | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.740953 | 0.383333 | 0.503474 | 0.200000 | 1.000000 | 0.200000 | 0.751737 | 0.351737 | 0.001249 | 106.023200 | 20732.600000 | 5.000000 | 5.200000 | 0.163766 |
| elo-merchant-category-recommendation | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.875152 | 0.716667 | 0.786900 | 1.000000 | 1.000000 | 1.000000 | 0.893450 | 0.893450 | 0.001194 | 112.413000 | 27297.000000 | 5.200000 | 5.600000 | 0.212743 |
| elo-merchant-category-recommendation | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.400000 | 0.166667 | 0.235294 | 0.000000 | 1.000000 | 0.000000 | 0.617647 | 0.117647 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.890303 | 0.783333 | 0.832279 | 0.800000 | 1.000000 | 0.800000 | 0.916140 | 0.816140 | 0.000438 | 60.482400 | 4524.800000 | 1.000000 | 0.000000 | 0.072776 |
| elo-merchant-category-recommendation | tc3_fault_injected | claude_code | 5 | `true` | 0.800000 | 0.867533 | 0.412500 | 0.552891 | 1.000000 | 0.850000 | 0.904762 | 0.701445 | 0.728827 | 0.019246 | 136.875232 | 2649.600000 | `null` | 24.800000 | 0.329295 |
| elo-merchant-category-recommendation | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 0.891025 | 0.512500 | 0.647573 | 1.000000 | 0.650000 | 0.780953 | 0.648786 | 0.714263 | 0.006287 | 130.411600 | 23113.600000 | 4.000000 | 4.800000 | 0.179367 |
| elo-merchant-category-recommendation | tc3_fault_injected | proposed_agent | 5 | `true` | 1.000000 | 0.909707 | 0.725000 | 0.805163 | 1.000000 | 0.550000 | 0.704762 | 0.677582 | 0.754963 | 0.004360 | 140.768200 | 31279.600000 | 5.600000 | 6.400000 | 0.250547 |
| elo-merchant-category-recommendation | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.600000 | 0.187500 | 0.285714 | 1.000000 | 0.500000 | 0.666667 | 0.392857 | 0.476191 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 0.902148 | 0.700000 | 0.786999 | 1.000000 | 0.700000 | 0.819048 | 0.743499 | 0.803023 | 0.001279 | 46.444800 | 3606.400000 | 1.000000 | 0.000000 | 0.058995 |
| elo-merchant-category-recommendation | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 0.960000 | 0.323077 | 0.469854 | 1.000000 | 0.866667 | 0.920000 | 0.668260 | 0.694927 | 0.007285 | 100.649162 | 2987.800000 | `null` | 21.200000 | 0.256730 |
| elo-merchant-category-recommendation | tc4_mixed_history | generic_agent | 5 | `true` | 0.800000 | 0.798095 | 0.415384 | 0.542724 | 1.000000 | 0.600000 | 0.740000 | 0.571362 | 0.641362 | 0.005734 | 120.325600 | 20476.600000 | 5.400000 | 6.600000 | 0.169023 |
| elo-merchant-category-recommendation | tc4_mixed_history | proposed_agent | 5 | `true` | 1.000000 | 0.893636 | 0.769231 | 0.825855 | 1.000000 | 0.600000 | 0.740000 | 0.712928 | 0.782927 | 0.005585 | 172.593400 | 39234.000000 | 6.400000 | 7.400000 | 0.304854 |
| elo-merchant-category-recommendation | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.400000 | 0.153846 | 0.222222 | 0.500000 | 0.333333 | 0.400000 | 0.277778 | 0.311111 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| elo-merchant-category-recommendation | tc4_mixed_history | single_llm | 5 | `true` | 0.800000 | 0.913333 | 0.661539 | 0.734855 | 1.000000 | 0.600000 | 0.740000 | 0.667428 | 0.737428 | 0.025746 | 49.902400 | 3560.200000 | 1.000000 | 0.000000 | 0.058282 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 0.950000 | 0.874832 | 0.468269 | 0.581295 | 0.800000 | 0.929167 | 0.756190 | 0.755231 | 0.668743 | 0.007813 | 151.644513 | 3070.100000 | `null` | 24.400000 | 0.345128 |
| generic_agent | 4 | 1.000000 | 5.000000 | 0.950000 | 0.810311 | 0.490304 | 0.603714 | 0.800000 | 0.812500 | 0.680238 | 0.708107 | 0.641976 | 0.003502 | 122.183650 | 21878.700000 | 4.900000 | 5.650000 | 0.173636 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | 0.000000 | 3300.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.884050 | 0.752725 | 0.811185 | 1.000000 | 0.787500 | 0.861190 | 0.799343 | 0.836188 | 0.002880 | 144.879700 | 32138.150000 | 5.600000 | 6.400000 | 0.253197 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.475000 | 0.173878 | 0.253989 | 0.625000 | 0.708333 | 0.516667 | 0.481161 | 0.385328 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 0.950000 | 0.880970 | 0.717468 | 0.780684 | 0.950000 | 0.825000 | 0.839762 | 0.802842 | 0.810223 | 0.006962 | 42.406150 | 3187.650000 | 1.000000 | 0.000000 | 0.058583 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task elo-merchant-category-recommendation --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/elo-merchant-category-recommendation-all.md
```
