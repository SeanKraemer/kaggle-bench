# Benchmark Aggregate Report

## Configuration

- Stage scope: `primary`
- Success threshold: `0.5`
- Tasks included: `home-credit-default-risk`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.904762`
- Mean Add Precision: `0.587309`
- Mean Add Recall: `0.321270`
- Mean Add F1: `0.383994`
- Mean Remove Precision: `0.714286`
- Mean Remove Recall: `0.900000`
- Mean Remove F1: `0.714739`
- Mean Task Completion Score: `0.641997`
- Mean Strict Task Completion Score: `0.549366`
- Mean Task Completion Variance: `0.001503`
- Mean Runtime (s): `194.979394`
- Mean Total Tokens: `17095.375000`
- Mean API Calls: `3.200000`
- Mean Tool Calls: `4.870000`
- Mean Cost (USD): `0.184236`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| home-credit-default-risk | AUC | finance_tabular | binary_classification | multi_table_relational | xlarge (27299925) | high (195) | high (21) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| home-credit-default-risk | 21 | 6 | 0.904762 | 4.047619 | 0.587309 | 0.321270 | 0.383994 | 0.714286 | 0.900000 | 0.714739 | 0.641997 | 0.549366 | 0.001503 | 194.979394 | 17095.375000 | 3.200000 | 4.870000 | 0.184236 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| home-credit-default-risk | tc1_from_scratch | claude_code | try1 | 0.727273 | 0.533333 | 0.615385 | 1.000000 | 1.000000 | 1.000000 | 0.807692 | 0.807692 | `true` | 150.711236 | 9619 | `null` | 10 | 0.359905 |
| home-credit-default-risk | tc1_from_scratch | claude_code | try2 | 0.666667 | 0.533333 | 0.592593 | 1.000000 | 1.000000 | 1.000000 | 0.796296 | 0.796296 | `true` | 116.482129 | 8145 | `null` | 10 | 0.333732 |
| home-credit-default-risk | tc1_from_scratch | claude_code | try3 | 0.666667 | 0.533333 | 0.592593 | 1.000000 | 1.000000 | 1.000000 | 0.796296 | 0.796296 | `true` | 109.337751 | 7592 | `null` | 9 | 0.306964 |
| home-credit-default-risk | tc1_from_scratch | claude_code | try4 | 0.727273 | 0.533333 | 0.615385 | 1.000000 | 1.000000 | 1.000000 | 0.807692 | 0.807692 | `true` | 124.442266 | 8766 | `null` | 10 | 0.361534 |
| home-credit-default-risk | tc1_from_scratch | claude_code | try5 | 0.764706 | 0.866667 | 0.812500 | 1.000000 | 1.000000 | 1.000000 | 0.906250 | 0.906250 | `true` | 191.282594 | 13098 | `null` | 11 | 0.466413 |
| home-credit-default-risk | tc1_from_scratch | generic_agent | try1 | 0.666667 | 0.533333 | 0.592593 | 1.000000 | 1.000000 | 1.000000 | 0.796296 | 0.796296 | `true` | 121.930000 | 28458 | 6 | 9 | 0.274913 |
| home-credit-default-risk | tc1_from_scratch | generic_agent | try2 | 0.571429 | 0.533333 | 0.551724 | 1.000000 | 1.000000 | 1.000000 | 0.775862 | 0.775862 | `true` | 146.846000 | 31307 | 9 | 9 | 0.310865 |
| home-credit-default-risk | tc1_from_scratch | generic_agent | try3 | 0.571429 | 0.533333 | 0.551724 | 1.000000 | 1.000000 | 1.000000 | 0.775862 | 0.775862 | `true` | 135.023000 | 34485 | 10 | 9 | 0.342165 |
| home-credit-default-risk | tc1_from_scratch | generic_agent | try4 | 0.470588 | 0.533333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 121.025000 | 31558 | 9 | 11 | 0.310054 |
| home-credit-default-risk | tc1_from_scratch | generic_agent | try5 | 0.615385 | 0.533333 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 114.479000 | 31264 | 9 | 9 | 0.295682 |
| home-credit-default-risk | tc1_from_scratch | human | human_tc1_annotator_a_v3 | 0.500000 | 0.600000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 2400 | `null` | `null` | `null` | `null` |
| home-credit-default-risk | tc1_from_scratch | proposed_agent | try1 | 0.571429 | 0.533333 | 0.551724 | 1.000000 | 1.000000 | 1.000000 | 0.775862 | 0.775862 | `true` | 162.801000 | 40948 | 6 | 7 | 0.454949 |
| home-credit-default-risk | tc1_from_scratch | proposed_agent | try2 | 0.692308 | 0.600000 | 0.642857 | 1.000000 | 1.000000 | 1.000000 | 0.821429 | 0.821429 | `true` | 103.804000 | 21366 | 4 | 4 | 0.305576 |
| home-credit-default-risk | tc1_from_scratch | proposed_agent | try3 | 0.666667 | 0.533333 | 0.592593 | 1.000000 | 1.000000 | 1.000000 | 0.796296 | 0.796296 | `true` | 88.618000 | 22800 | 4 | 4 | 0.310358 |
| home-credit-default-risk | tc1_from_scratch | proposed_agent | try4 | 0.692308 | 0.600000 | 0.642857 | 1.000000 | 1.000000 | 1.000000 | 0.821429 | 0.821429 | `true` | 105.331000 | 28590 | 5 | 6 | 0.366384 |
| home-credit-default-risk | tc1_from_scratch | proposed_agent | try5 | 0.615385 | 0.533333 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 112.350000 | 26149 | 4 | 4 | 0.339113 |
| home-credit-default-risk | tc1_from_scratch | rule_based | try1 | 0.250000 | 0.066667 | 0.105263 | 1.000000 | 1.000000 | 1.000000 | 0.552631 | 0.552631 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc1_from_scratch | single_llm | try1 | 0.666667 | 0.533333 | 0.592593 | 1.000000 | 1.000000 | 1.000000 | 0.796296 | 0.796296 | `true` | 156.167000 | 1191 | 1 | 0 | 0.350812 |
| home-credit-default-risk | tc1_from_scratch | single_llm | try2 | 0.666667 | 0.800000 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | `true` | 55.568000 | 4448 | 1 | 0 | 0.076855 |
| home-credit-default-risk | tc1_from_scratch | single_llm | try3 | 0.736842 | 0.933333 | 0.823529 | 1.000000 | 1.000000 | 1.000000 | 0.911764 | 0.911764 | `true` | 68.818000 | 5383 | 1 | 0 | 0.091462 |
| home-credit-default-risk | tc1_from_scratch | single_llm | try4 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 54.956000 | 4119 | 1 | 0 | 0.072502 |
| home-credit-default-risk | tc1_from_scratch | single_llm | try5 | 0.600000 | 0.800000 | 0.685714 | 1.000000 | 1.000000 | 1.000000 | 0.842857 | 0.842857 | `true` | 62.483000 | 4777 | 1 | 0 | 0.082372 |
| home-credit-default-risk | tc2_partial_good | claude_code | try1 | 0.250000 | 0.100000 | 0.142857 | 0.000000 | 1.000000 | 0.000000 | 0.571429 | 0.071429 | `true` | 124.507047 | 8633 | `null` | 12 | 0.345837 |
| home-credit-default-risk | tc2_partial_good | claude_code | try2 | 1.000000 | 0.100000 | 0.181818 | 0.000000 | 1.000000 | 0.000000 | 0.590909 | 0.090909 | `true` | 103.932415 | 5972 | `null` | 9 | 0.270294 |
| home-credit-default-risk | tc2_partial_good | claude_code | try3 | 0.500000 | 0.100000 | 0.166667 | 0.000000 | 1.000000 | 0.000000 | 0.583333 | 0.083334 | `true` | 148.975959 | 7988 | `null` | 10 | 0.347726 |
| home-credit-default-risk | tc2_partial_good | claude_code | try4 | 1.000000 | 0.100000 | 0.181818 | 0.000000 | 1.000000 | 0.000000 | 0.590909 | 0.090909 | `true` | 144.863102 | 7039 | `null` | 10 | 0.315664 |
| home-credit-default-risk | tc2_partial_good | claude_code | try5 | 1.000000 | 0.100000 | 0.181818 | 0.000000 | 1.000000 | 0.000000 | 0.590909 | 0.090909 | `true` | 152.740578 | 7559 | `null` | 11 | 0.311734 |
| home-credit-default-risk | tc2_partial_good | generic_agent | try1 | 0.333333 | 0.100000 | 0.153846 | 0.000000 | 1.000000 | 0.000000 | 0.576923 | 0.076923 | `true` | 99.322000 | 24853 | 7 | 11 | 0.195825 |
| home-credit-default-risk | tc2_partial_good | generic_agent | try2 | 0.166667 | 0.100000 | 0.125000 | 0.000000 | 1.000000 | 0.000000 | 0.562500 | 0.062500 | `true` | 99.761000 | 24473 | 6 | 8 | 0.189933 |
| home-credit-default-risk | tc2_partial_good | generic_agent | try3 | 0.500000 | 0.100000 | 0.166667 | 0.000000 | 1.000000 | 0.000000 | 0.583333 | 0.083334 | `true` | 113.490000 | 27619 | 7 | 9 | 0.231584 |
| home-credit-default-risk | tc2_partial_good | generic_agent | try4 | 0.333333 | 0.200000 | 0.250000 | 0.000000 | 1.000000 | 0.000000 | 0.625000 | 0.125000 | `true` | 115.274000 | 29343 | 8 | 8 | 0.242278 |
| home-credit-default-risk | tc2_partial_good | generic_agent | try5 | 0.250000 | 0.100000 | 0.142857 | 0.000000 | 1.000000 | 0.000000 | 0.571429 | 0.071429 | `true` | 114.183000 | 27188 | 6 | 9 | 0.210527 |
| home-credit-default-risk | tc2_partial_good | proposed_agent | try1 | 0.800000 | 0.400000 | 0.533333 | 1.000000 | 1.000000 | 1.000000 | 0.766666 | 0.766666 | `true` | 155.535000 | 37039 | 6 | 7 | 0.302091 |
| home-credit-default-risk | tc2_partial_good | proposed_agent | try2 | 0.800000 | 0.400000 | 0.533333 | 1.000000 | 1.000000 | 1.000000 | 0.766666 | 0.766666 | `true` | 127.211000 | 19339 | 4 | 3 | 0.192418 |
| home-credit-default-risk | tc2_partial_good | proposed_agent | try3 | 0.666667 | 0.400000 | 0.500000 | 0.000000 | 1.000000 | 0.000000 | 0.750000 | 0.250000 | `true` | 176.729000 | 26530 | 4 | 4 | 0.258691 |
| home-credit-default-risk | tc2_partial_good | proposed_agent | try4 | 0.800000 | 0.800000 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 190.537000 | 49234 | 7 | 10 | 0.402528 |
| home-credit-default-risk | tc2_partial_good | proposed_agent | try5 | 0.800000 | 0.400000 | 0.533333 | 0.000000 | 1.000000 | 0.000000 | 0.766666 | 0.266666 | `true` | 163.983000 | 38549 | 6 | 8 | 0.312161 |
| home-credit-default-risk | tc2_partial_good | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc2_partial_good | single_llm | try1 | 0.571429 | 0.400000 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | `true` | 54.550000 | 3847 | 1 | 0 | 0.189488 |
| home-credit-default-risk | tc2_partial_good | single_llm | try2 | 0.666667 | 0.400000 | 0.500000 | 0.000000 | 1.000000 | 0.000000 | 0.750000 | 0.250000 | `true` | 46.977000 | 3265 | 1 | 0 | 0.059824 |
| home-credit-default-risk | tc2_partial_good | single_llm | try3 | 0.666667 | 0.400000 | 0.500000 | 0.000000 | 1.000000 | 0.000000 | 0.750000 | 0.250000 | `true` | 44.217000 | 2943 | 1 | 0 | 0.054994 |
| home-credit-default-risk | tc2_partial_good | single_llm | try4 | 0.714286 | 0.500000 | 0.588235 | 1.000000 | 1.000000 | 1.000000 | 0.794118 | 0.794118 | `true` | 50.973000 | 3478 | 1 | 0 | 0.063019 |
| home-credit-default-risk | tc2_partial_good | single_llm | try5 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 51.103000 | 3747 | 1 | 0 | 0.067054 |
| home-credit-default-risk | tc3_fault_injected | claude_code | try1 | 1.000000 | 0.266667 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 101.513736 | 5830 | `null` | 11 | 0.314345 |
| home-credit-default-risk | tc3_fault_injected | claude_code | try2 | 1.000000 | 0.266667 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 102.758240 | 5544 | `null` | 9 | 0.288794 |
| home-credit-default-risk | tc3_fault_injected | claude_code | try3 | 1.000000 | 0.266667 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 97.242331 | 5368 | `null` | 9 | 0.283370 |
| home-credit-default-risk | tc3_fault_injected | claude_code | try4 | 1.000000 | 0.266667 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 63.579532 | 4411 | `null` | 7 | 0.227019 |
| home-credit-default-risk | tc3_fault_injected | claude_code | try5 | 1.000000 | 0.266667 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 106.381118 | 5589 | `null` | 10 | 0.287701 |
| home-credit-default-risk | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 87.614000 | 19648 | 5 | 6 | 0.168570 |
| home-credit-default-risk | tc3_fault_injected | generic_agent | try2 | 1.000000 | 0.266667 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 87.594000 | 17374 | 5 | 7 | 0.139812 |
| home-credit-default-risk | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.266667 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 95.642000 | 21132 | 5 | 7 | 0.165885 |
| home-credit-default-risk | tc3_fault_injected | generic_agent | try4 | 1.000000 | 0.266667 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 83.857000 | 20658 | 5 | 7 | 0.166008 |
| home-credit-default-risk | tc3_fault_injected | generic_agent | try5 | 1.000000 | 0.266667 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 108.397000 | 26180 | 5 | 7 | 0.205527 |
| home-credit-default-risk | tc3_fault_injected | proposed_agent | try1 | 0.857143 | 0.400000 | 0.545455 | 1.000000 | 0.750000 | 0.857143 | 0.647728 | 0.701299 | `true` | 123.311000 | 34922 | 6 | 7 | 0.289162 |
| home-credit-default-risk | tc3_fault_injected | proposed_agent | try2 | 0.600000 | 0.200000 | 0.300000 | 1.000000 | 1.000000 | 1.000000 | 0.650000 | 0.650000 | `true` | 160.722000 | 40476 | 8 | 12 | 0.333530 |
| home-credit-default-risk | tc3_fault_injected | proposed_agent | try3 | 0.600000 | 0.200000 | 0.300000 | 1.000000 | 1.000000 | 1.000000 | 0.650000 | 0.650000 | `true` | 177.737000 | 43762 | 6 | 9 | 0.352947 |
| home-credit-default-risk | tc3_fault_injected | proposed_agent | try4 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | `true` | 112.847000 | 31785 | 5 | 6 | 0.263929 |
| home-credit-default-risk | tc3_fault_injected | proposed_agent | try5 | 0.777778 | 0.466667 | 0.583333 | 1.000000 | 1.000000 | 1.000000 | 0.791667 | 0.791667 | `true` | 104.624000 | 30390 | 5 | 6 | 0.251327 |
| home-credit-default-risk | tc3_fault_injected | rule_based | try1 | 0.250000 | 0.066667 | 0.105263 | 0.000000 | 0.000000 | 0.000000 | 0.052631 | 0.052631 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.266667 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 38.575000 | 2788 | 1 | 0 | 0.051655 |
| home-credit-default-risk | tc3_fault_injected | single_llm | try2 | 0.750000 | 0.400000 | 0.521739 | 1.000000 | 1.000000 | 1.000000 | 0.760869 | 0.760869 | `true` | 44.887000 | 3284 | 1 | 0 | 0.060071 |
| home-credit-default-risk | tc3_fault_injected | single_llm | try3 | 0.833333 | 0.333333 | 0.476190 | 1.000000 | 1.000000 | 1.000000 | 0.738095 | 0.738095 | `true` | 36.526000 | 2660 | 1 | 0 | 0.050711 |
| home-credit-default-risk | tc3_fault_injected | single_llm | try4 | 1.000000 | 0.466667 | 0.636364 | 1.000000 | 1.000000 | 1.000000 | 0.818182 | 0.818182 | `true` | 35.530000 | 2588 | 1 | 0 | 0.049631 |
| home-credit-default-risk | tc3_fault_injected | single_llm | try5 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 42.281000 | 2796 | 1 | 0 | 0.052751 |
| home-credit-default-risk | tc4_mixed_history | claude_code | try1 | 0.500000 | 0.125000 | 0.200000 | 1.000000 | 1.000000 | 1.000000 | 0.600000 | 0.600000 | `true` | 107.619793 | 7173 | `null` | 10 | 0.313989 |
| home-credit-default-risk | tc4_mixed_history | claude_code | try2 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 125.590075 | 7503 | `null` | 12 | 0.324855 |
| home-credit-default-risk | tc4_mixed_history | claude_code | try3 | 1.000000 | 0.125000 | 0.222222 | 1.000000 | 1.000000 | 1.000000 | 0.611111 | 0.611111 | `true` | 103.169639 | 5791 | `null` | 9 | 0.263254 |
| home-credit-default-risk | tc4_mixed_history | claude_code | try4 | 0.500000 | 0.125000 | 0.200000 | 1.000000 | 1.000000 | 1.000000 | 0.600000 | 0.600000 | `true` | 113.601456 | 5623 | `null` | 9 | 0.273027 |
| home-credit-default-risk | tc4_mixed_history | claude_code | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 157.901426 | 8427 | `null` | 10 | 0.353808 |
| home-credit-default-risk | tc4_mixed_history | generic_agent | try1 | 0.750000 | 0.375000 | 0.500000 | 0.500000 | 1.000000 | 0.666667 | 0.750000 | 0.583333 | `true` | 110.987000 | 25263 | 5 | 7 | 0.190396 |
| home-credit-default-risk | tc4_mixed_history | generic_agent | try2 | 0.500000 | 0.125000 | 0.200000 | 0.500000 | 1.000000 | 0.666667 | 0.600000 | 0.433334 | `true` | 117.130000 | 24200 | 5 | 7 | 0.186499 |
| home-credit-default-risk | tc4_mixed_history | generic_agent | try3 | 0.500000 | 0.125000 | 0.200000 | 1.000000 | 1.000000 | 1.000000 | 0.600000 | 0.600000 | `true` | 113.508000 | 23715 | 6 | 8 | 0.199556 |
| home-credit-default-risk | tc4_mixed_history | generic_agent | try4 | 0.750000 | 0.375000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 95.641000 | 22409 | 6 | 8 | 0.184793 |
| home-credit-default-risk | tc4_mixed_history | generic_agent | try5 | 0.500000 | 0.125000 | 0.200000 | 1.000000 | 1.000000 | 1.000000 | 0.600000 | 0.600000 | `true` | 73.270000 | 16691 | 7 | 7 | 0.148691 |
| home-credit-default-risk | tc4_mixed_history | proposed_agent | try1 | 0.500000 | 0.375000 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | `true` | 155.418000 | 23864 | 4 | 3 | 0.234805 |
| home-credit-default-risk | tc4_mixed_history | proposed_agent | try2 | 0.857143 | 0.750000 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 137.571000 | 32222 | 5 | 5 | 0.259957 |
| home-credit-default-risk | tc4_mixed_history | proposed_agent | try3 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 179.728000 | 34798 | 6 | 8 | 0.305771 |
| home-credit-default-risk | tc4_mixed_history | proposed_agent | try4 | 0.750000 | 0.750000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 160.200000 | 43206 | 6 | 9 | 0.341212 |
| home-credit-default-risk | tc4_mixed_history | proposed_agent | try5 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 151.219000 | 24709 | 4 | 4 | 0.228532 |
| home-credit-default-risk | tc4_mixed_history | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc4_mixed_history | single_llm | try1 | 0.600000 | 0.375000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 33.731000 | 2595 | 1 | 0 | 0.048376 |
| home-credit-default-risk | tc4_mixed_history | single_llm | try2 | 0.600000 | 0.375000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 32.467000 | 2200 | 1 | 0 | 0.043931 |
| home-credit-default-risk | tc4_mixed_history | single_llm | try3 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 41.472000 | 2886 | 1 | 0 | 0.054221 |
| home-credit-default-risk | tc4_mixed_history | single_llm | try4 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 37.294000 | 2433 | 1 | 0 | 0.047426 |
| home-credit-default-risk | tc4_mixed_history | single_llm | try5 | 0.600000 | 0.375000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 32.380000 | 2036 | 1 | 0 | 0.041471 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| home-credit-default-risk | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.710517 | 0.600000 | 0.645691 | 1.000000 | 1.000000 | 1.000000 | 0.822845 | 0.822845 | 0.001765 | 138.451195 | 9444.000000 | `null` | 10.000000 | 0.365710 |
| home-credit-default-risk | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.579100 | 0.533333 | 0.553494 | 1.000000 | 1.000000 | 1.000000 | 0.776747 | 0.776747 | 0.000236 | 127.860600 | 31414.400000 | 8.600000 | 9.400000 | 0.306736 |
| home-credit-default-risk | tc1_from_scratch | human | 1 | `true` | 1.000000 | 0.500000 | 0.600000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | 0.000000 | 2400 | `null` | `null` | `null` | `null` |
| home-credit-default-risk | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.647619 | 0.560000 | 0.600292 | 1.000000 | 1.000000 | 1.000000 | 0.800146 | 0.800146 | 0.000344 | 114.580800 | 27970.600000 | 4.600000 | 5.000000 | 0.355276 |
| home-credit-default-risk | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.250000 | 0.066667 | 0.105263 | 1.000000 | 1.000000 | 1.000000 | 0.552631 | 0.552631 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.667369 | 0.746667 | 0.699155 | 1.000000 | 1.000000 | 1.000000 | 0.849577 | 0.849577 | 0.001443 | 79.598400 | 3983.600000 | 1.000000 | 0.000000 | 0.134801 |
| home-credit-default-risk | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.750000 | 0.100000 | 0.170996 | 0.000000 | 1.000000 | 0.000000 | 0.585498 | 0.085498 | 0.000058 | 135.003820 | 7438.200000 | `null` | 10.400000 | 0.318251 |
| home-credit-default-risk | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.316667 | 0.120000 | 0.167674 | 0.000000 | 1.000000 | 0.000000 | 0.583837 | 0.083837 | 0.000470 | 108.406000 | 26695.200000 | 6.800000 | 9.000000 | 0.214030 |
| home-credit-default-risk | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.773333 | 0.480000 | 0.580000 | 0.600000 | 1.000000 | 0.600000 | 0.790000 | 0.590000 | 0.003067 | 162.799000 | 34138.200000 | 5.400000 | 6.400000 | 0.293578 |
| home-credit-default-risk | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.657143 | 0.420000 | 0.511765 | 0.600000 | 1.000000 | 0.600000 | 0.755882 | 0.555882 | 0.000398 | 49.564000 | 3456.000000 | 1.000000 | 0.000000 | 0.086875 |
| home-credit-default-risk | tc3_fault_injected | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.266667 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | 0.000000 | 94.294991 | 5348.400000 | `null` | 9.200000 | 0.280246 |
| home-credit-default-risk | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.280000 | 0.436842 | 1.000000 | 1.000000 | 1.000000 | 0.718422 | 0.718422 | 0.000249 | 92.620800 | 20998.400000 | 5.000000 | 6.800000 | 0.169160 |
| home-credit-default-risk | tc3_fault_injected | proposed_agent | 5 | `true` | 1.000000 | 0.700318 | 0.333333 | 0.445758 | 1.000000 | 0.900000 | 0.942857 | 0.672879 | 0.694307 | 0.003616 | 135.848200 | 36267.000000 | 6.000000 | 8.000000 | 0.298179 |
| home-credit-default-risk | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.250000 | 0.066667 | 0.105263 | 0.000000 | 0.000000 | 0.000000 | 0.052631 | 0.052631 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 0.916667 | 0.373333 | 0.525355 | 1.000000 | 1.000000 | 1.000000 | 0.762677 | 0.762677 | 0.001388 | 39.559800 | 2823.200000 | 1.000000 | 0.000000 | 0.052964 |
| home-credit-default-risk | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 0.800000 | 0.175000 | 0.284444 | 1.000000 | 1.000000 | 1.000000 | 0.642222 | 0.642222 | 0.002242 | 121.576478 | 6903.400000 | `null` | 10.000000 | 0.305786 |
| home-credit-default-risk | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 0.600000 | 0.225000 | 0.320000 | 0.800000 | 1.000000 | 0.866667 | 0.660000 | 0.593333 | 0.005400 | 102.107200 | 22455.600000 | 5.800000 | 7.400000 | 0.181987 |
| home-credit-default-risk | tc4_mixed_history | proposed_agent | 5 | `true` | 1.000000 | 0.654762 | 0.475000 | 0.535108 | 1.000000 | 1.000000 | 1.000000 | 0.767554 | 0.767554 | 0.009891 | 156.827200 | 31759.800000 | 5.000000 | 5.800000 | 0.274055 |
| home-credit-default-risk | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 0.560000 | 0.325000 | 0.410256 | 1.000000 | 1.000000 | 1.000000 | 0.705128 | 0.705128 | 0.000986 | 35.468800 | 2430.000000 | 1.000000 | 0.000000 | 0.047085 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 1.000000 | 0.815129 | 0.285417 | 0.380546 | 0.750000 | 1.000000 | 0.750000 | 0.690273 | 0.565273 | 0.001016 | 122.331621 | 7283.500000 | `null` | 9.900000 | 0.317498 |
| generic_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.623942 | 0.289583 | 0.369503 | 0.700000 | 1.000000 | 0.716667 | 0.684751 | 0.543085 | 0.001589 | 107.748650 | 25390.900000 | 6.550000 | 8.150000 | 0.217978 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.600000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | 0.000000 | 2400.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.694008 | 0.462083 | 0.540289 | 0.900000 | 0.975000 | 0.885714 | 0.757645 | 0.713002 | 0.004229 | 142.513800 | 32533.900000 | 5.250000 | 6.300000 | 0.305272 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.125000 | 0.033334 | 0.052631 | 0.250000 | 0.500000 | 0.250000 | 0.276315 | 0.151315 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 0.700295 | 0.466250 | 0.536633 | 0.900000 | 1.000000 | 0.900000 | 0.768316 | 0.718316 | 0.001054 | 51.047750 | 3173.200000 | 1.000000 | 0.000000 | 0.080431 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task home-credit-default-risk --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/home-credit-default-risk-primary.md
```
