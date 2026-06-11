# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `restaurant-revenue-prediction`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.904762`
- Mean Add Precision: `0.804365`
- Mean Add Recall: `0.499762`
- Mean Add F1: `0.600482`
- Mean Remove Precision: `0.876190`
- Mean Remove Recall: `0.907143`
- Mean Remove F1: `0.848073`
- Mean Task Completion Score: `0.753812`
- Mean Strict Task Completion Score: `0.724277`
- Mean Task Completion Variance: `0.002038`
- Mean Runtime (s): `158.014277`
- Mean Total Tokens: `5700.662500`
- Mean API Calls: `2.100000`
- Mean Tool Calls: `2.710000`
- Mean Cost (USD): `0.070882`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| restaurant-revenue-prediction | RMSE | restaurant_tabular | regression | single_table | small (100000) | medium (44) | medium (11) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| restaurant-revenue-prediction | 21 | 6 | 0.904762 | 4.047619 | 0.804365 | 0.499762 | 0.600482 | 0.876190 | 0.907143 | 0.848073 | 0.753812 | 0.724277 | 0.002038 | 158.014277 | 5700.662500 | 2.100000 | 2.710000 | 0.070882 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| restaurant-revenue-prediction | tc1_from_scratch | claude_code | try1 | 0.833333 | 0.625000 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 87.090967 | 4689 | `null` | 7 | 0.166466 |
| restaurant-revenue-prediction | tc1_from_scratch | claude_code | try2 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 116.308036 | 6129 | `null` | 7 | 0.190275 |
| restaurant-revenue-prediction | tc1_from_scratch | claude_code | try3 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 103.685646 | 5935 | `null` | 7 | 0.185826 |
| restaurant-revenue-prediction | tc1_from_scratch | claude_code | try4 | 1.000000 | 0.875000 | 0.933333 | 1.000000 | 1.000000 | 1.000000 | 0.966666 | 0.966666 | `true` | 95.995008 | 5389 | `null` | 9 | 0.192751 |
| restaurant-revenue-prediction | tc1_from_scratch | claude_code | try5 | 1.000000 | 0.875000 | 0.933333 | 1.000000 | 1.000000 | 1.000000 | 0.966666 | 0.966666 | `true` | 114.357450 | 5862 | `null` | 8 | 0.186996 |
| restaurant-revenue-prediction | tc1_from_scratch | generic_agent | try1 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 63.848000 | 8077 | 4 | 4 | 0.074234 |
| restaurant-revenue-prediction | tc1_from_scratch | generic_agent | try2 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 48.017000 | 7192 | 4 | 4 | 0.054516 |
| restaurant-revenue-prediction | tc1_from_scratch | generic_agent | try3 | 0.857143 | 0.750000 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 41.230000 | 6140 | 4 | 3 | 0.052403 |
| restaurant-revenue-prediction | tc1_from_scratch | generic_agent | try4 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 63.076000 | 6919 | 4 | 4 | 0.052776 |
| restaurant-revenue-prediction | tc1_from_scratch | generic_agent | try5 | 0.833333 | 0.625000 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 75.369000 | 9733 | 5 | 5 | 0.076757 |
| restaurant-revenue-prediction | tc1_from_scratch | human | human_tc1_annotator_c_v1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 2400 | `null` | `null` | `null` | `null` |
| restaurant-revenue-prediction | tc1_from_scratch | proposed_agent | try1 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 48.032000 | 8842 | 4 | 3 | 0.147475 |
| restaurant-revenue-prediction | tc1_from_scratch | proposed_agent | try2 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 55.913000 | 9413 | 4 | 3 | 0.079305 |
| restaurant-revenue-prediction | tc1_from_scratch | proposed_agent | try3 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 49.126000 | 8149 | 4 | 3 | 0.072154 |
| restaurant-revenue-prediction | tc1_from_scratch | proposed_agent | try4 | 1.000000 | 0.875000 | 0.933333 | 1.000000 | 1.000000 | 1.000000 | 0.966666 | 0.966666 | `true` | 47.787000 | 8037 | 4 | 3 | 0.071854 |
| restaurant-revenue-prediction | tc1_from_scratch | proposed_agent | try5 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 43.777000 | 7730 | 4 | 3 | 0.067489 |
| restaurant-revenue-prediction | tc1_from_scratch | rule_based | try1 | 0.375000 | 0.375000 | 0.375000 | 1.000000 | 1.000000 | 1.000000 | 0.687500 | 0.687500 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| restaurant-revenue-prediction | tc1_from_scratch | single_llm | try1 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 8.834000 | 506 | 1 | 0 | 0.051949 |
| restaurant-revenue-prediction | tc1_from_scratch | single_llm | try2 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 8.758000 | 515 | 1 | 0 | 0.052084 |
| restaurant-revenue-prediction | tc1_from_scratch | single_llm | try3 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 11.323000 | 572 | 1 | 0 | 0.052935 |
| restaurant-revenue-prediction | tc1_from_scratch | single_llm | try4 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 8.566000 | 507 | 1 | 0 | 0.051960 |
| restaurant-revenue-prediction | tc1_from_scratch | single_llm | try5 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 8.677000 | 498 | 1 | 0 | 0.011160 |
| restaurant-revenue-prediction | tc2_partial_good | claude_code | try1 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 85.048408 | 4290 | `null` | 7 | 0.156128 |
| restaurant-revenue-prediction | tc2_partial_good | claude_code | try2 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 71.634227 | 4047 | `null` | 7 | 0.153069 |
| restaurant-revenue-prediction | tc2_partial_good | claude_code | try3 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 59.452656 | 3024 | `null` | 6 | 0.128069 |
| restaurant-revenue-prediction | tc2_partial_good | claude_code | try4 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 52.212769 | 2927 | `null` | 4 | 0.120792 |
| restaurant-revenue-prediction | tc2_partial_good | claude_code | try5 | 0.666667 | 0.400000 | 0.500000 | 0.000000 | 1.000000 | 0.000000 | 0.750000 | 0.250000 | `true` | 81.912407 | 4202 | `null` | 8 | 0.156771 |
| restaurant-revenue-prediction | tc2_partial_good | generic_agent | try1 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 64.776000 | 7303 | 4 | 3 | 0.063084 |
| restaurant-revenue-prediction | tc2_partial_good | generic_agent | try2 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 57.396000 | 6688 | 4 | 3 | 0.051939 |
| restaurant-revenue-prediction | tc2_partial_good | generic_agent | try3 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 46.643000 | 5413 | 3 | 2 | 0.047188 |
| restaurant-revenue-prediction | tc2_partial_good | generic_agent | try4 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 46.504000 | 6876 | 4 | 3 | 0.053541 |
| restaurant-revenue-prediction | tc2_partial_good | generic_agent | try5 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 45.546000 | 8939 | 3 | 3 | 0.056506 |
| restaurant-revenue-prediction | tc2_partial_good | proposed_agent | try1 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 40.270000 | 5494 | 3 | 2 | 0.055405 |
| restaurant-revenue-prediction | tc2_partial_good | proposed_agent | try2 | 1.000000 | 0.800000 | 0.888889 | 1.000000 | 1.000000 | 1.000000 | 0.944445 | 0.944445 | `true` | 52.485000 | 6360 | 3 | 2 | 0.066967 |
| restaurant-revenue-prediction | tc2_partial_good | proposed_agent | try3 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 46.039000 | 5341 | 3 | 2 | 0.057724 |
| restaurant-revenue-prediction | tc2_partial_good | proposed_agent | try4 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 40.633000 | 4990 | 3 | 2 | 0.056347 |
| restaurant-revenue-prediction | tc2_partial_good | proposed_agent | try5 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 48.057000 | 5315 | 3 | 2 | 0.059482 |
| restaurant-revenue-prediction | tc2_partial_good | rule_based | try1 | 0.166667 | 0.200000 | 0.181818 | 0.000000 | 1.000000 | 0.000000 | 0.590909 | 0.090909 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| restaurant-revenue-prediction | tc2_partial_good | single_llm | try1 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 26.702000 | 1475 | 1 | 0 | 0.025028 |
| restaurant-revenue-prediction | tc2_partial_good | single_llm | try2 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 31.756000 | 1470 | 1 | 0 | 0.024953 |
| restaurant-revenue-prediction | tc2_partial_good | single_llm | try3 | 0.750000 | 0.600000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 12.659000 | 749 | 1 | 0 | 0.014138 |
| restaurant-revenue-prediction | tc2_partial_good | single_llm | try4 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 31.909000 | 1812 | 1 | 0 | 0.030083 |
| restaurant-revenue-prediction | tc2_partial_good | single_llm | try5 | 0.666667 | 0.400000 | 0.500000 | 0.000000 | 1.000000 | 0.000000 | 0.750000 | 0.250000 | `true` | 12.623000 | 653 | 1 | 0 | 0.013548 |
| restaurant-revenue-prediction | tc3_fault_injected | claude_code | try1 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 94.768879 | 5016 | `null` | 10 | 0.186363 |
| restaurant-revenue-prediction | tc3_fault_injected | claude_code | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 107.552069 | 5545 | `null` | 7 | 0.182925 |
| restaurant-revenue-prediction | tc3_fault_injected | claude_code | try3 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 80.858604 | 4927 | `null` | 12 | 0.187611 |
| restaurant-revenue-prediction | tc3_fault_injected | claude_code | try4 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 100.431692 | 6272 | `null` | 8 | 0.200303 |
| restaurant-revenue-prediction | tc3_fault_injected | claude_code | try5 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 85.307190 | 4424 | `null` | 11 | 0.174428 |
| restaurant-revenue-prediction | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 53.955000 | 9865 | 4 | 4 | 0.070015 |
| restaurant-revenue-prediction | tc3_fault_injected | generic_agent | try2 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 45.236000 | 7049 | 3 | 3 | 0.056269 |
| restaurant-revenue-prediction | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 54.441000 | 4830 | 3 | 3 | 0.046989 |
| restaurant-revenue-prediction | tc3_fault_injected | generic_agent | try4 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 42.163000 | 5709 | 3 | 2 | 0.049626 |
| restaurant-revenue-prediction | tc3_fault_injected | generic_agent | try5 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 31.460000 | 2831 | 2 | 1 | 0.031565 |
| restaurant-revenue-prediction | tc3_fault_injected | proposed_agent | try1 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 61.874000 | 7672 | 3 | 2 | 0.080635 |
| restaurant-revenue-prediction | tc3_fault_injected | proposed_agent | try2 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 85.627000 | 17958 | 6 | 5 | 0.144321 |
| restaurant-revenue-prediction | tc3_fault_injected | proposed_agent | try3 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 95.417000 | 17505 | 5 | 5 | 0.144376 |
| restaurant-revenue-prediction | tc3_fault_injected | proposed_agent | try4 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 0.750000 | 0.857143 | 0.759615 | 0.813187 | `true` | 61.200000 | 8993 | 4 | 3 | 0.085349 |
| restaurant-revenue-prediction | tc3_fault_injected | proposed_agent | try5 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 67.140000 | 7762 | 3 | 2 | 0.084406 |
| restaurant-revenue-prediction | tc3_fault_injected | rule_based | try1 | 0.428571 | 0.375000 | 0.400000 | 1.000000 | 0.500000 | 0.666667 | 0.450000 | 0.533334 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| restaurant-revenue-prediction | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 26.133000 | 1626 | 1 | 0 | 0.027197 |
| restaurant-revenue-prediction | tc3_fault_injected | single_llm | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 28.702000 | 1564 | 1 | 0 | 0.026267 |
| restaurant-revenue-prediction | tc3_fault_injected | single_llm | try3 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 34.065000 | 2074 | 1 | 0 | 0.033917 |
| restaurant-revenue-prediction | tc3_fault_injected | single_llm | try4 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 29.229000 | 1808 | 1 | 0 | 0.029927 |
| restaurant-revenue-prediction | tc3_fault_injected | single_llm | try5 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 22.827000 | 1428 | 1 | 0 | 0.025203 |
| restaurant-revenue-prediction | tc4_mixed_history | claude_code | try1 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | `true` | 109.316825 | 5308 | `null` | 7 | 0.177761 |
| restaurant-revenue-prediction | tc4_mixed_history | claude_code | try2 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | `true` | 129.919528 | 6559 | `null` | 6 | 0.191678 |
| restaurant-revenue-prediction | tc4_mixed_history | claude_code | try3 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 101.471159 | 5826 | `null` | 8 | 0.186491 |
| restaurant-revenue-prediction | tc4_mixed_history | claude_code | try4 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 117.091646 | 6156 | `null` | 6 | 0.184366 |
| restaurant-revenue-prediction | tc4_mixed_history | claude_code | try5 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | `true` | 69.737920 | 3903 | `null` | 7 | 0.149994 |
| restaurant-revenue-prediction | tc4_mixed_history | generic_agent | try1 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 52.508000 | 7019 | 3 | 2 | 0.059539 |
| restaurant-revenue-prediction | tc4_mixed_history | generic_agent | try2 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 46.534000 | 6477 | 3 | 2 | 0.055273 |
| restaurant-revenue-prediction | tc4_mixed_history | generic_agent | try3 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 72.116000 | 10100 | 4 | 4 | 0.081549 |
| restaurant-revenue-prediction | tc4_mixed_history | generic_agent | try4 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 51.983000 | 6615 | 3 | 2 | 0.056391 |
| restaurant-revenue-prediction | tc4_mixed_history | generic_agent | try5 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 52.450000 | 6996 | 3 | 2 | 0.059010 |
| restaurant-revenue-prediction | tc4_mixed_history | proposed_agent | try1 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 86.075000 | 15389 | 5 | 4 | 0.119971 |
| restaurant-revenue-prediction | tc4_mixed_history | proposed_agent | try2 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 65.938000 | 10157 | 4 | 3 | 0.092001 |
| restaurant-revenue-prediction | tc4_mixed_history | proposed_agent | try3 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 73.463000 | 14043 | 5 | 5 | 0.113340 |
| restaurant-revenue-prediction | tc4_mixed_history | proposed_agent | try4 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 66.146000 | 9489 | 4 | 3 | 0.089083 |
| restaurant-revenue-prediction | tc4_mixed_history | proposed_agent | try5 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 70.893000 | 9735 | 4 | 3 | 0.169012 |
| restaurant-revenue-prediction | tc4_mixed_history | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| restaurant-revenue-prediction | tc4_mixed_history | single_llm | try1 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 31.552000 | 1817 | 1 | 0 | 0.029966 |
| restaurant-revenue-prediction | tc4_mixed_history | single_llm | try2 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 33.438000 | 1930 | 1 | 0 | 0.031661 |
| restaurant-revenue-prediction | tc4_mixed_history | single_llm | try3 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 32.799000 | 1875 | 1 | 0 | 0.030836 |
| restaurant-revenue-prediction | tc4_mixed_history | single_llm | try4 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 29.947000 | 1663 | 1 | 0 | 0.027656 |
| restaurant-revenue-prediction | tc4_mixed_history | single_llm | try5 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | `true` | 35.704000 | 1936 | 1 | 0 | 0.032853 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| restaurant-revenue-prediction | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.966667 | 0.775000 | 0.859048 | 1.000000 | 1.000000 | 1.000000 | 0.929523 | 0.929523 | 0.001600 | 103.487421 | 5600.800000 | `null` | 7.600000 | 0.184463 |
| restaurant-revenue-prediction | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.938095 | 0.725000 | 0.817143 | 1.000000 | 1.000000 | 1.000000 | 0.908571 | 0.908571 | 0.000784 | 58.308000 | 7612.200000 | 4.200000 | 4.000000 | 0.062137 |
| restaurant-revenue-prediction | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 2400 | `null` | `null` | `null` | `null` |
| restaurant-revenue-prediction | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.775000 | 0.872381 | 1.000000 | 1.000000 | 1.000000 | 0.936190 | 0.936190 | 0.000232 | 48.927000 | 8434.200000 | 4.000000 | 3.000000 | 0.087655 |
| restaurant-revenue-prediction | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.375000 | 0.375000 | 0.375000 | 1.000000 | 1.000000 | 1.000000 | 0.687500 | 0.687500 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| restaurant-revenue-prediction | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | 0.000000 | 9.231600 | 519.600000 | 1.000000 | 0.000000 | 0.044017 |
| restaurant-revenue-prediction | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.933333 | 0.400000 | 0.557143 | 0.800000 | 1.000000 | 0.800000 | 0.778571 | 0.678571 | 0.000204 | 70.052093 | 3698.000000 | `null` | 6.400000 | 0.142966 |
| restaurant-revenue-prediction | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.560000 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | 0.001276 | 52.173000 | 7043.800000 | 3.600000 | 2.800000 | 0.054452 |
| restaurant-revenue-prediction | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.640000 | 0.777778 | 1.000000 | 1.000000 | 1.000000 | 0.888889 | 0.888889 | 0.000772 | 45.496800 | 5500.000000 | 3.000000 | 2.000000 | 0.059185 |
| restaurant-revenue-prediction | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.166667 | 0.200000 | 0.181818 | 0.000000 | 1.000000 | 0.000000 | 0.590909 | 0.090909 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| restaurant-revenue-prediction | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.883333 | 0.520000 | 0.647619 | 0.600000 | 1.000000 | 0.600000 | 0.823809 | 0.623810 | 0.002446 | 23.129800 | 1231.800000 | 1.000000 | 0.000000 | 0.021550 |
| restaurant-revenue-prediction | tc3_fault_injected | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.525000 | 0.687180 | 1.000000 | 1.000000 | 1.000000 | 0.843589 | 0.843589 | 0.000421 | 93.783687 | 5236.800000 | `null` | 9.600000 | 0.186326 |
| restaurant-revenue-prediction | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.625000 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | 0.000000 | 45.451000 | 6056.800000 | 3.000000 | 2.600000 | 0.050893 |
| restaurant-revenue-prediction | tc3_fault_injected | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.550000 | 0.707693 | 1.000000 | 0.800000 | 0.885714 | 0.753846 | 0.796703 | 0.004670 | 74.251600 | 11978.000000 | 4.200000 | 3.400000 | 0.107817 |
| restaurant-revenue-prediction | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.428571 | 0.375000 | 0.400000 | 1.000000 | 0.500000 | 0.666667 | 0.450000 | 0.533334 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| restaurant-revenue-prediction | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | 0.000000 | 28.191200 | 1700.000000 | 1.000000 | 0.000000 | 0.028502 |
| restaurant-revenue-prediction | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 0.400000 | 0.133333 | 0.200000 | 1.000000 | 1.000000 | 1.000000 | 0.600000 | 0.600000 | 0.015000 | 105.507416 | 5550.400000 | `null` | 6.800000 | 0.178058 |
| restaurant-revenue-prediction | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | 0.000000 | 55.118200 | 7441.400000 | 3.200000 | 2.400000 | 0.062352 |
| restaurant-revenue-prediction | tc4_mixed_history | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.466667 | 0.620000 | 1.000000 | 1.000000 | 1.000000 | 0.810000 | 0.810000 | 0.005400 | 72.503000 | 11762.600000 | 4.400000 | 3.600000 | 0.116682 |
| restaurant-revenue-prediction | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| restaurant-revenue-prediction | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 0.800000 | 0.266666 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | 0.010000 | 32.688000 | 1844.200000 | 1.000000 | 0.000000 | 0.030594 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 1.000000 | 0.825000 | 0.458333 | 0.575843 | 0.950000 | 1.000000 | 0.950000 | 0.787921 | 0.762921 | 0.004306 | 93.207654 | 5021.500000 | `null` | 7.600000 | 0.172953 |
| generic_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.984524 | 0.560833 | 0.700165 | 1.000000 | 1.000000 | 1.000000 | 0.850082 | 0.850082 | 0.000515 | 52.762550 | 7038.550000 | 3.500000 | 2.950000 | 0.057458 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 2400.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 1.000000 | 0.607917 | 0.744463 | 1.000000 | 0.950000 | 0.971429 | 0.847231 | 0.857946 | 0.002769 | 60.294600 | 9418.700000 | 3.900000 | 3.000000 | 0.092835 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.242559 | 0.237500 | 0.239205 | 0.500000 | 0.625000 | 0.416667 | 0.432102 | 0.327936 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 0.920833 | 0.509166 | 0.642857 | 0.900000 | 0.937500 | 0.864286 | 0.790178 | 0.753572 | 0.003112 | 23.310150 | 1323.900000 | 1.000000 | 0.000000 | 0.031166 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task restaurant-revenue-prediction --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/restaurant-revenue-prediction-all.md
```
