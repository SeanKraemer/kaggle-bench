# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `home-credit-default-risk`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.904762`
- Mean Add Precision: `0.556125`
- Mean Add Recall: `0.266304`
- Mean Add F1: `0.329041`
- Mean Remove Precision: `0.714286`
- Mean Remove Recall: `0.900000`
- Mean Remove F1: `0.714739`
- Mean Task Completion Score: `0.614520`
- Mean Strict Task Completion Score: `0.521890`
- Mean Task Completion Variance: `0.001041`
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
| home-credit-default-risk | 21 | 6 | 0.904762 | 4.047619 | 0.556125 | 0.266304 | 0.329041 | 0.714286 | 0.900000 | 0.714739 | 0.614520 | 0.521890 | 0.001041 | 194.979394 | 17095.375000 | 3.200000 | 4.870000 | 0.184236 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| home-credit-default-risk | tc1_from_scratch | claude_code | try1 | 0.692308 | 0.450000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 150.711236 | 9619 | `null` | 10 | 0.359905 |
| home-credit-default-risk | tc1_from_scratch | claude_code | try2 | 0.625000 | 0.500000 | 0.555556 | 1.000000 | 1.000000 | 1.000000 | 0.777778 | 0.777778 | `true` | 116.482129 | 8145 | `null` | 10 | 0.333732 |
| home-credit-default-risk | tc1_from_scratch | claude_code | try3 | 0.642857 | 0.450000 | 0.529412 | 1.000000 | 1.000000 | 1.000000 | 0.764706 | 0.764706 | `true` | 109.337751 | 7592 | `null` | 9 | 0.306964 |
| home-credit-default-risk | tc1_from_scratch | claude_code | try4 | 0.692308 | 0.450000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 124.442266 | 8766 | `null` | 10 | 0.361534 |
| home-credit-default-risk | tc1_from_scratch | claude_code | try5 | 0.750000 | 0.750000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 191.282594 | 13098 | `null` | 11 | 0.466413 |
| home-credit-default-risk | tc1_from_scratch | generic_agent | try1 | 0.666667 | 0.500000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 121.930000 | 28458 | 6 | 9 | 0.274913 |
| home-credit-default-risk | tc1_from_scratch | generic_agent | try2 | 0.588235 | 0.500000 | 0.540541 | 1.000000 | 1.000000 | 1.000000 | 0.770271 | 0.770271 | `true` | 146.846000 | 31307 | 9 | 9 | 0.310865 |
| home-credit-default-risk | tc1_from_scratch | generic_agent | try3 | 0.555556 | 0.500000 | 0.526316 | 1.000000 | 1.000000 | 1.000000 | 0.763158 | 0.763158 | `true` | 135.023000 | 34485 | 10 | 9 | 0.342165 |
| home-credit-default-risk | tc1_from_scratch | generic_agent | try4 | 0.500000 | 0.500000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 121.025000 | 31558 | 9 | 11 | 0.310054 |
| home-credit-default-risk | tc1_from_scratch | generic_agent | try5 | 0.600000 | 0.450000 | 0.514286 | 1.000000 | 1.000000 | 1.000000 | 0.757143 | 0.757143 | `true` | 114.479000 | 31264 | 9 | 9 | 0.295682 |
| home-credit-default-risk | tc1_from_scratch | human | human_tc1_annotator_a_v3 | 0.434783 | 0.500000 | 0.465116 | 1.000000 | 1.000000 | 1.000000 | 0.732558 | 0.732558 | `true` | 2400 | `null` | `null` | `null` | `null` |
| home-credit-default-risk | tc1_from_scratch | proposed_agent | try1 | 0.555556 | 0.500000 | 0.526316 | 1.000000 | 1.000000 | 1.000000 | 0.763158 | 0.763158 | `true` | 162.801000 | 40948 | 6 | 7 | 0.454949 |
| home-credit-default-risk | tc1_from_scratch | proposed_agent | try2 | 0.687500 | 0.550000 | 0.611111 | 1.000000 | 1.000000 | 1.000000 | 0.805555 | 0.805555 | `true` | 103.804000 | 21366 | 4 | 4 | 0.305576 |
| home-credit-default-risk | tc1_from_scratch | proposed_agent | try3 | 0.588235 | 0.500000 | 0.540541 | 1.000000 | 1.000000 | 1.000000 | 0.770271 | 0.770271 | `true` | 88.618000 | 22800 | 4 | 4 | 0.310358 |
| home-credit-default-risk | tc1_from_scratch | proposed_agent | try4 | 0.647059 | 0.550000 | 0.594595 | 1.000000 | 1.000000 | 1.000000 | 0.797297 | 0.797297 | `true` | 105.331000 | 28590 | 5 | 6 | 0.366384 |
| home-credit-default-risk | tc1_from_scratch | proposed_agent | try5 | 0.555556 | 0.500000 | 0.526316 | 1.000000 | 1.000000 | 1.000000 | 0.763158 | 0.763158 | `true` | 112.350000 | 26149 | 4 | 4 | 0.339113 |
| home-credit-default-risk | tc1_from_scratch | rule_based | try1 | 0.166667 | 0.050000 | 0.076923 | 1.000000 | 1.000000 | 1.000000 | 0.538462 | 0.538462 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc1_from_scratch | single_llm | try1 | 0.588235 | 0.500000 | 0.540541 | 1.000000 | 1.000000 | 1.000000 | 0.770271 | 0.770271 | `true` | 156.167000 | 1191 | 1 | 0 | 0.350812 |
| home-credit-default-risk | tc1_from_scratch | single_llm | try2 | 0.636364 | 0.700000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 55.568000 | 4448 | 1 | 0 | 0.076855 |
| home-credit-default-risk | tc1_from_scratch | single_llm | try3 | 0.727273 | 0.800000 | 0.761905 | 1.000000 | 1.000000 | 1.000000 | 0.880953 | 0.880953 | `true` | 68.818000 | 5383 | 1 | 0 | 0.091462 |
| home-credit-default-risk | tc1_from_scratch | single_llm | try4 | 0.666667 | 0.600000 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 54.956000 | 4119 | 1 | 0 | 0.072502 |
| home-credit-default-risk | tc1_from_scratch | single_llm | try5 | 0.538462 | 0.700000 | 0.608696 | 1.000000 | 1.000000 | 1.000000 | 0.804348 | 0.804348 | `true` | 62.483000 | 4777 | 1 | 0 | 0.082372 |
| home-credit-default-risk | tc2_partial_good | claude_code | try1 | 0.250000 | 0.071429 | 0.111111 | 0.000000 | 1.000000 | 0.000000 | 0.555555 | 0.055556 | `true` | 124.507047 | 8633 | `null` | 12 | 0.345837 |
| home-credit-default-risk | tc2_partial_good | claude_code | try2 | 1.000000 | 0.071429 | 0.133333 | 0.000000 | 1.000000 | 0.000000 | 0.566666 | 0.066667 | `true` | 103.932415 | 5972 | `null` | 9 | 0.270294 |
| home-credit-default-risk | tc2_partial_good | claude_code | try3 | 0.500000 | 0.071429 | 0.125000 | 0.000000 | 1.000000 | 0.000000 | 0.562500 | 0.062500 | `true` | 148.975959 | 7988 | `null` | 10 | 0.347726 |
| home-credit-default-risk | tc2_partial_good | claude_code | try4 | 1.000000 | 0.071429 | 0.133333 | 0.000000 | 1.000000 | 0.000000 | 0.566666 | 0.066667 | `true` | 144.863102 | 7039 | `null` | 10 | 0.315664 |
| home-credit-default-risk | tc2_partial_good | claude_code | try5 | 1.000000 | 0.071429 | 0.133333 | 0.000000 | 1.000000 | 0.000000 | 0.566666 | 0.066667 | `true` | 152.740578 | 7559 | `null` | 11 | 0.311734 |
| home-credit-default-risk | tc2_partial_good | generic_agent | try1 | 0.250000 | 0.071429 | 0.111111 | 0.000000 | 1.000000 | 0.000000 | 0.555555 | 0.055556 | `true` | 99.322000 | 24853 | 7 | 11 | 0.195825 |
| home-credit-default-risk | tc2_partial_good | generic_agent | try2 | 0.142857 | 0.071429 | 0.095238 | 0.000000 | 1.000000 | 0.000000 | 0.547619 | 0.047619 | `true` | 99.761000 | 24473 | 6 | 8 | 0.189933 |
| home-credit-default-risk | tc2_partial_good | generic_agent | try3 | 0.333333 | 0.071429 | 0.117647 | 0.000000 | 1.000000 | 0.000000 | 0.558824 | 0.058824 | `true` | 113.490000 | 27619 | 7 | 9 | 0.231584 |
| home-credit-default-risk | tc2_partial_good | generic_agent | try4 | 0.285714 | 0.142857 | 0.190476 | 0.000000 | 1.000000 | 0.000000 | 0.595238 | 0.095238 | `true` | 115.274000 | 29343 | 8 | 8 | 0.242278 |
| home-credit-default-risk | tc2_partial_good | generic_agent | try5 | 0.200000 | 0.071429 | 0.105263 | 0.000000 | 1.000000 | 0.000000 | 0.552631 | 0.052631 | `true` | 114.183000 | 27188 | 6 | 9 | 0.210527 |
| home-credit-default-risk | tc2_partial_good | proposed_agent | try1 | 0.666667 | 0.285714 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 155.535000 | 37039 | 6 | 7 | 0.302091 |
| home-credit-default-risk | tc2_partial_good | proposed_agent | try2 | 0.714286 | 0.357143 | 0.476190 | 1.000000 | 1.000000 | 1.000000 | 0.738095 | 0.738095 | `true` | 127.211000 | 19339 | 4 | 3 | 0.192418 |
| home-credit-default-risk | tc2_partial_good | proposed_agent | try3 | 0.571429 | 0.285714 | 0.380952 | 0.000000 | 1.000000 | 0.000000 | 0.690476 | 0.190476 | `true` | 176.729000 | 26530 | 4 | 4 | 0.258691 |
| home-credit-default-risk | tc2_partial_good | proposed_agent | try4 | 0.727273 | 0.571429 | 0.640000 | 1.000000 | 1.000000 | 1.000000 | 0.820000 | 0.820000 | `true` | 190.537000 | 49234 | 7 | 10 | 0.402528 |
| home-credit-default-risk | tc2_partial_good | proposed_agent | try5 | 0.714286 | 0.357143 | 0.476190 | 0.000000 | 1.000000 | 0.000000 | 0.738095 | 0.238095 | `true` | 163.983000 | 38549 | 6 | 8 | 0.312161 |
| home-credit-default-risk | tc2_partial_good | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc2_partial_good | single_llm | try1 | 0.555556 | 0.357143 | 0.434783 | 1.000000 | 1.000000 | 1.000000 | 0.717391 | 0.717391 | `true` | 54.550000 | 3847 | 1 | 0 | 0.189488 |
| home-credit-default-risk | tc2_partial_good | single_llm | try2 | 0.625000 | 0.357143 | 0.454545 | 0.000000 | 1.000000 | 0.000000 | 0.727272 | 0.227272 | `true` | 46.977000 | 3265 | 1 | 0 | 0.059824 |
| home-credit-default-risk | tc2_partial_good | single_llm | try3 | 0.571429 | 0.285714 | 0.380952 | 0.000000 | 1.000000 | 0.000000 | 0.690476 | 0.190476 | `true` | 44.217000 | 2943 | 1 | 0 | 0.054994 |
| home-credit-default-risk | tc2_partial_good | single_llm | try4 | 0.666667 | 0.428571 | 0.521739 | 1.000000 | 1.000000 | 1.000000 | 0.760869 | 0.760869 | `true` | 50.973000 | 3478 | 1 | 0 | 0.063019 |
| home-credit-default-risk | tc2_partial_good | single_llm | try5 | 0.625000 | 0.357143 | 0.454545 | 1.000000 | 1.000000 | 1.000000 | 0.727272 | 0.727272 | `true` | 51.103000 | 3747 | 1 | 0 | 0.067054 |
| home-credit-default-risk | tc3_fault_injected | claude_code | try1 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 101.513736 | 5830 | `null` | 11 | 0.314345 |
| home-credit-default-risk | tc3_fault_injected | claude_code | try2 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 102.758240 | 5544 | `null` | 9 | 0.288794 |
| home-credit-default-risk | tc3_fault_injected | claude_code | try3 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 97.242331 | 5368 | `null` | 9 | 0.283370 |
| home-credit-default-risk | tc3_fault_injected | claude_code | try4 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 63.579532 | 4411 | `null` | 7 | 0.227019 |
| home-credit-default-risk | tc3_fault_injected | claude_code | try5 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 106.381118 | 5589 | `null` | 10 | 0.287701 |
| home-credit-default-risk | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.300000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 87.614000 | 19648 | 5 | 6 | 0.168570 |
| home-credit-default-risk | tc3_fault_injected | generic_agent | try2 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 87.594000 | 17374 | 5 | 7 | 0.139812 |
| home-credit-default-risk | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 95.642000 | 21132 | 5 | 7 | 0.165885 |
| home-credit-default-risk | tc3_fault_injected | generic_agent | try4 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 83.857000 | 20658 | 5 | 7 | 0.166008 |
| home-credit-default-risk | tc3_fault_injected | generic_agent | try5 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 108.397000 | 26180 | 5 | 7 | 0.205527 |
| home-credit-default-risk | tc3_fault_injected | proposed_agent | try1 | 0.750000 | 0.300000 | 0.428571 | 1.000000 | 0.750000 | 0.857143 | 0.589286 | 0.642857 | `true` | 123.311000 | 34922 | 6 | 7 | 0.289162 |
| home-credit-default-risk | tc3_fault_injected | proposed_agent | try2 | 0.500000 | 0.150000 | 0.230769 | 1.000000 | 1.000000 | 1.000000 | 0.615385 | 0.615385 | `true` | 160.722000 | 40476 | 8 | 12 | 0.333530 |
| home-credit-default-risk | tc3_fault_injected | proposed_agent | try3 | 0.500000 | 0.150000 | 0.230769 | 1.000000 | 1.000000 | 1.000000 | 0.615385 | 0.615385 | `true` | 177.737000 | 43762 | 6 | 9 | 0.352947 |
| home-credit-default-risk | tc3_fault_injected | proposed_agent | try4 | 0.666667 | 0.300000 | 0.413793 | 1.000000 | 0.750000 | 0.857143 | 0.581897 | 0.635468 | `true` | 112.847000 | 31785 | 5 | 6 | 0.263929 |
| home-credit-default-risk | tc3_fault_injected | proposed_agent | try5 | 0.777778 | 0.350000 | 0.482759 | 1.000000 | 1.000000 | 1.000000 | 0.741379 | 0.741379 | `true` | 104.624000 | 30390 | 5 | 6 | 0.251327 |
| home-credit-default-risk | tc3_fault_injected | rule_based | try1 | 0.166667 | 0.050000 | 0.076923 | 0.000000 | 0.000000 | 0.000000 | 0.038462 | 0.038462 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 38.575000 | 2788 | 1 | 0 | 0.051655 |
| home-credit-default-risk | tc3_fault_injected | single_llm | try2 | 0.777778 | 0.350000 | 0.482759 | 1.000000 | 1.000000 | 1.000000 | 0.741379 | 0.741379 | `true` | 44.887000 | 3284 | 1 | 0 | 0.060071 |
| home-credit-default-risk | tc3_fault_injected | single_llm | try3 | 0.857143 | 0.300000 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 36.526000 | 2660 | 1 | 0 | 0.050711 |
| home-credit-default-risk | tc3_fault_injected | single_llm | try4 | 1.000000 | 0.350000 | 0.518519 | 1.000000 | 1.000000 | 1.000000 | 0.759259 | 0.759259 | `true` | 35.530000 | 2588 | 1 | 0 | 0.049631 |
| home-credit-default-risk | tc3_fault_injected | single_llm | try5 | 1.000000 | 0.300000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 42.281000 | 2796 | 1 | 0 | 0.052751 |
| home-credit-default-risk | tc4_mixed_history | claude_code | try1 | 0.500000 | 0.083333 | 0.142857 | 1.000000 | 1.000000 | 1.000000 | 0.571429 | 0.571429 | `true` | 107.619793 | 7173 | `null` | 10 | 0.313989 |
| home-credit-default-risk | tc4_mixed_history | claude_code | try2 | 1.000000 | 0.166667 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 125.590075 | 7503 | `null` | 12 | 0.324855 |
| home-credit-default-risk | tc4_mixed_history | claude_code | try3 | 1.000000 | 0.083333 | 0.153846 | 1.000000 | 1.000000 | 1.000000 | 0.576923 | 0.576923 | `true` | 103.169639 | 5791 | `null` | 9 | 0.263254 |
| home-credit-default-risk | tc4_mixed_history | claude_code | try4 | 0.500000 | 0.083333 | 0.142857 | 1.000000 | 1.000000 | 1.000000 | 0.571429 | 0.571429 | `true` | 113.601456 | 5623 | `null` | 9 | 0.273027 |
| home-credit-default-risk | tc4_mixed_history | claude_code | try5 | 1.000000 | 0.166667 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 157.901426 | 8427 | `null` | 10 | 0.353808 |
| home-credit-default-risk | tc4_mixed_history | generic_agent | try1 | 0.750000 | 0.250000 | 0.375000 | 0.500000 | 1.000000 | 0.666667 | 0.687500 | 0.520833 | `true` | 110.987000 | 25263 | 5 | 7 | 0.190396 |
| home-credit-default-risk | tc4_mixed_history | generic_agent | try2 | 0.500000 | 0.083333 | 0.142857 | 0.500000 | 1.000000 | 0.666667 | 0.571429 | 0.404762 | `true` | 117.130000 | 24200 | 5 | 7 | 0.186499 |
| home-credit-default-risk | tc4_mixed_history | generic_agent | try3 | 0.500000 | 0.083333 | 0.142857 | 1.000000 | 1.000000 | 1.000000 | 0.571429 | 0.571429 | `true` | 113.508000 | 23715 | 6 | 8 | 0.199556 |
| home-credit-default-risk | tc4_mixed_history | generic_agent | try4 | 0.600000 | 0.250000 | 0.352941 | 1.000000 | 1.000000 | 1.000000 | 0.676470 | 0.676470 | `true` | 95.641000 | 22409 | 6 | 8 | 0.184793 |
| home-credit-default-risk | tc4_mixed_history | generic_agent | try5 | 0.500000 | 0.083333 | 0.142857 | 1.000000 | 1.000000 | 1.000000 | 0.571429 | 0.571429 | `true` | 73.270000 | 16691 | 7 | 7 | 0.148691 |
| home-credit-default-risk | tc4_mixed_history | proposed_agent | try1 | 0.571429 | 0.333333 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 155.418000 | 23864 | 4 | 3 | 0.234805 |
| home-credit-default-risk | tc4_mixed_history | proposed_agent | try2 | 0.777778 | 0.583333 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 137.571000 | 32222 | 5 | 5 | 0.259957 |
| home-credit-default-risk | tc4_mixed_history | proposed_agent | try3 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 179.728000 | 34798 | 6 | 8 | 0.305771 |
| home-credit-default-risk | tc4_mixed_history | proposed_agent | try4 | 0.777778 | 0.583333 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 160.200000 | 43206 | 6 | 9 | 0.341212 |
| home-credit-default-risk | tc4_mixed_history | proposed_agent | try5 | 0.600000 | 0.250000 | 0.352941 | 1.000000 | 1.000000 | 1.000000 | 0.676470 | 0.676470 | `true` | 151.219000 | 24709 | 4 | 4 | 0.228532 |
| home-credit-default-risk | tc4_mixed_history | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc4_mixed_history | single_llm | try1 | 0.571429 | 0.333333 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 33.731000 | 2595 | 1 | 0 | 0.048376 |
| home-credit-default-risk | tc4_mixed_history | single_llm | try2 | 0.571429 | 0.333333 | 0.421053 | 1.000000 | 1.000000 | 1.000000 | 0.710527 | 0.710527 | `true` | 32.467000 | 2200 | 1 | 0 | 0.043931 |
| home-credit-default-risk | tc4_mixed_history | single_llm | try3 | 0.500000 | 0.166667 | 0.250000 | 1.000000 | 1.000000 | 1.000000 | 0.625000 | 0.625000 | `true` | 41.472000 | 2886 | 1 | 0 | 0.054221 |
| home-credit-default-risk | tc4_mixed_history | single_llm | try4 | 0.500000 | 0.166667 | 0.250000 | 1.000000 | 1.000000 | 1.000000 | 0.625000 | 0.625000 | `true` | 37.294000 | 2433 | 1 | 0 | 0.047426 |
| home-credit-default-risk | tc4_mixed_history | single_llm | try5 | 0.600000 | 0.250000 | 0.352941 | 1.000000 | 1.000000 | 1.000000 | 0.676470 | 0.676470 | `true` | 32.380000 | 2036 | 1 | 0 | 0.041471 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| home-credit-default-risk | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.680495 | 0.520000 | 0.585176 | 1.000000 | 1.000000 | 1.000000 | 0.792588 | 0.792588 | 0.001715 | 138.451195 | 9444.000000 | `null` | 10.000000 | 0.365710 |
| home-credit-default-risk | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.582092 | 0.490000 | 0.530514 | 1.000000 | 1.000000 | 1.000000 | 0.765257 | 0.765257 | 0.000149 | 127.860600 | 31414.400000 | 8.600000 | 9.400000 | 0.306736 |
| home-credit-default-risk | tc1_from_scratch | human | 1 | `true` | 1.000000 | 0.434783 | 0.500000 | 0.465116 | 1.000000 | 1.000000 | 1.000000 | 0.732558 | 0.732558 | 0.000000 | 2400 | `null` | `null` | `null` | `null` |
| home-credit-default-risk | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.606781 | 0.520000 | 0.559776 | 1.000000 | 1.000000 | 1.000000 | 0.779888 | 0.779888 | 0.000323 | 114.580800 | 27970.600000 | 4.600000 | 5.000000 | 0.355276 |
| home-credit-default-risk | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.166667 | 0.050000 | 0.076923 | 1.000000 | 1.000000 | 1.000000 | 0.538462 | 0.538462 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.631400 | 0.660000 | 0.641878 | 1.000000 | 1.000000 | 1.000000 | 0.820939 | 0.820939 | 0.001325 | 79.598400 | 3983.600000 | 1.000000 | 0.000000 | 0.134801 |
| home-credit-default-risk | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.750000 | 0.071429 | 0.127222 | 0.000000 | 1.000000 | 0.000000 | 0.563611 | 0.063611 | 0.000019 | 135.003820 | 7438.200000 | `null` | 10.400000 | 0.318251 |
| home-credit-default-risk | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.242381 | 0.085715 | 0.123947 | 0.000000 | 1.000000 | 0.000000 | 0.561973 | 0.061974 | 0.000290 | 108.406000 | 26695.200000 | 6.800000 | 9.000000 | 0.214030 |
| home-credit-default-risk | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.678788 | 0.371429 | 0.474666 | 0.600000 | 1.000000 | 0.600000 | 0.737333 | 0.537333 | 0.002085 | 162.799000 | 34138.200000 | 5.400000 | 6.400000 | 0.293578 |
| home-credit-default-risk | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.608730 | 0.357143 | 0.449313 | 0.600000 | 1.000000 | 0.600000 | 0.724656 | 0.524656 | 0.000509 | 49.564000 | 3456.000000 | 1.000000 | 0.000000 | 0.086875 |
| home-credit-default-risk | tc3_fault_injected | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | 0.000000 | 94.294991 | 5348.400000 | `null` | 9.200000 | 0.280246 |
| home-credit-default-risk | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.240000 | 0.385641 | 1.000000 | 1.000000 | 1.000000 | 0.692821 | 0.692821 | 0.000582 | 92.620800 | 20998.400000 | 5.000000 | 6.800000 | 0.169160 |
| home-credit-default-risk | tc3_fault_injected | proposed_agent | 5 | `true` | 1.000000 | 0.638889 | 0.250000 | 0.357332 | 1.000000 | 0.900000 | 0.942857 | 0.628666 | 0.650095 | 0.003359 | 135.848200 | 36267.000000 | 6.000000 | 8.000000 | 0.298179 |
| home-credit-default-risk | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.166667 | 0.050000 | 0.076923 | 0.000000 | 0.000000 | 0.000000 | 0.038462 | 0.038462 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 0.926984 | 0.310000 | 0.461452 | 1.000000 | 1.000000 | 1.000000 | 0.730726 | 0.730726 | 0.000389 | 39.559800 | 2823.200000 | 1.000000 | 0.000000 | 0.052964 |
| home-credit-default-risk | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 0.800000 | 0.116667 | 0.202198 | 1.000000 | 1.000000 | 1.000000 | 0.601099 | 0.601099 | 0.001167 | 121.576478 | 6903.400000 | `null` | 10.000000 | 0.305786 |
| home-credit-default-risk | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 0.570000 | 0.150000 | 0.231302 | 0.800000 | 1.000000 | 0.866667 | 0.615651 | 0.548985 | 0.002946 | 102.107200 | 22455.600000 | 5.800000 | 7.400000 | 0.181987 |
| home-credit-default-risk | tc4_mixed_history | proposed_agent | 5 | `true` | 1.000000 | 0.645397 | 0.400000 | 0.488132 | 1.000000 | 1.000000 | 1.000000 | 0.744066 | 0.744066 | 0.005524 | 156.827200 | 31759.800000 | 5.000000 | 5.800000 | 0.274055 |
| home-credit-default-risk | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| home-credit-default-risk | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 0.548572 | 0.250000 | 0.339009 | 1.000000 | 1.000000 | 1.000000 | 0.669505 | 0.669505 | 0.001475 | 35.468800 | 2430.000000 | 1.000000 | 0.000000 | 0.047085 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 1.000000 | 0.807624 | 0.227024 | 0.311982 | 0.750000 | 1.000000 | 0.750000 | 0.655991 | 0.530991 | 0.000725 | 122.331621 | 7283.500000 | `null` | 9.900000 | 0.317498 |
| generic_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.598618 | 0.241429 | 0.317851 | 0.700000 | 1.000000 | 0.716667 | 0.658925 | 0.517259 | 0.000992 | 107.748650 | 25390.900000 | 6.550000 | 8.150000 | 0.217978 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 0.434783 | 0.500000 | 0.465116 | 1.000000 | 1.000000 | 1.000000 | 0.732558 | 0.732558 | 0.000000 | 2400.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.642464 | 0.385357 | 0.469977 | 0.900000 | 0.975000 | 0.885714 | 0.722488 | 0.677845 | 0.002823 | 142.513800 | 32533.900000 | 5.250000 | 6.300000 | 0.305272 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.083334 | 0.025000 | 0.038462 | 0.250000 | 0.500000 | 0.250000 | 0.269231 | 0.144231 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 0.678921 | 0.394286 | 0.472913 | 0.900000 | 1.000000 | 0.900000 | 0.736456 | 0.686457 | 0.000924 | 51.047750 | 3173.200000 | 1.000000 | 0.000000 | 0.080431 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task home-credit-default-risk --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/home-credit-default-risk-all.md
```
