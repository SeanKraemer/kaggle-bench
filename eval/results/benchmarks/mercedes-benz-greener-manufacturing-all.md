# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `mercedes-benz-greener-manufacturing`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.904762`
- Mean Add Precision: `0.884921`
- Mean Add Recall: `0.408730`
- Mean Add F1: `0.536469`
- Mean Remove Precision: `0.928571`
- Mean Remove Recall: `0.909524`
- Mean Remove F1: `0.881406`
- Mean Task Completion Score: `0.722997`
- Mean Strict Task Completion Score: `0.708938`
- Mean Task Completion Variance: `0.001228`
- Mean Runtime (s): `155.505551`
- Mean Total Tokens: `5209.112500`
- Mean API Calls: `2.075000`
- Mean Tool Calls: `2.650000`
- Mean Cost (USD): `0.168386`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mercedes-benz-greener-manufacturing | R2 | manufacturing_tabular | regression | single_table | small (4209) | high (378) | medium (11) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mercedes-benz-greener-manufacturing | 21 | 6 | 0.904762 | 4.047619 | 0.884921 | 0.408730 | 0.536469 | 0.928571 | 0.909524 | 0.881406 | 0.722997 | 0.708938 | 0.001228 | 155.505551 | 5209.112500 | 2.075000 | 2.650000 | 0.168386 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | claude_code | try1 | 0.750000 | 0.500000 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 130.388045 | 5842 | `null` | 7 | 0.439927 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | claude_code | try2 | 0.750000 | 0.500000 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 105.910183 | 5428 | `null` | 9 | 0.438414 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | claude_code | try3 | 0.750000 | 0.500000 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 103.883514 | 5471 | `null` | 8 | 0.433120 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | claude_code | try4 | 0.750000 | 0.500000 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 131.932615 | 5758 | `null` | 8 | 0.463857 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | claude_code | try5 | 0.600000 | 0.500000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 102.436188 | 2871 | `null` | 11 | 0.453037 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | generic_agent | try1 | 0.750000 | 0.500000 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 60.926000 | 9225 | 4 | 4 | 0.352954 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | generic_agent | try2 | 0.600000 | 0.500000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 50.010000 | 7848 | 5 | 4 | 0.121369 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | generic_agent | try3 | 0.750000 | 0.500000 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 71.187000 | 13257 | 6 | 6 | 0.168796 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | generic_agent | try4 | 0.750000 | 0.500000 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 49.581000 | 8349 | 4 | 4 | 0.111560 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | generic_agent | try5 | 0.800000 | 0.666667 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | `true` | 58.277000 | 9175 | 6 | 5 | 0.144170 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | human | human_tc1_annotator_c_v1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 2400 | `null` | `null` | `null` | `null` |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | proposed_agent | try1 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 44.735000 | 5062 | 3 | 2 | 0.931556 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | proposed_agent | try2 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 42.455000 | 5668 | 3 | 2 | 0.167038 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | proposed_agent | try3 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 53.012000 | 5773 | 3 | 2 | 0.169669 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | proposed_agent | try4 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 43.132000 | 4638 | 3 | 2 | 0.159616 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | proposed_agent | try5 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 42.332000 | 4953 | 3 | 2 | 0.163861 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | rule_based | try1 | 0.666667 | 0.333333 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | single_llm | try1 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 10.195000 | 469 | 1 | 0 | 0.809985 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | single_llm | try2 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 10.438000 | 460 | 1 | 0 | 0.047174 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | single_llm | try3 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 8.803000 | 450 | 1 | 0 | 0.047024 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | single_llm | try4 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 8.990000 | 472 | 1 | 0 | 0.047354 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | single_llm | try5 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 9.936000 | 432 | 1 | 0 | 0.046754 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | claude_code | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 73.270044 | 3080 | `null` | 6 | 0.351730 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | claude_code | try2 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 75.480682 | 3534 | `null` | 7 | 0.402877 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | claude_code | try3 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 55.181205 | 2724 | `null` | 5 | 0.327370 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | claude_code | try4 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 82.409301 | 3565 | `null` | 6 | 0.365483 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | claude_code | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 31.844848 | 3032 | `null` | 7 | 0.310071 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | generic_agent | try1 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 52.963000 | 7876 | 4 | 3 | 0.107779 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | generic_agent | try2 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 48.303000 | 7597 | 4 | 4 | 0.105472 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | generic_agent | try3 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 47.517000 | 6878 | 4 | 4 | 0.099358 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | generic_agent | try4 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 52.810000 | 7805 | 5 | 4 | 0.120568 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | generic_agent | try5 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 44.114000 | 7764 | 4 | 4 | 0.105604 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | proposed_agent | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 50.512000 | 5684 | 3 | 1 | 0.168610 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | proposed_agent | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 54.765000 | 6254 | 3 | 2 | 0.174640 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | proposed_agent | try3 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 47.550000 | 5113 | 3 | 2 | 0.165808 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | proposed_agent | try4 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 66.832000 | 10438 | 4 | 3 | 0.229659 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | proposed_agent | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 51.128000 | 5747 | 3 | 2 | 0.169810 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | rule_based | try1 | 0.500000 | 0.250000 | 0.333333 | 0.000000 | 1.000000 | 0.000000 | 0.666667 | 0.166666 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | single_llm | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 17.944000 | 943 | 1 | 0 | 0.053705 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | single_llm | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 8.789000 | 430 | 1 | 0 | 0.046766 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | single_llm | try3 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 16.205000 | 877 | 1 | 0 | 0.053470 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | single_llm | try4 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 20.512000 | 1120 | 1 | 0 | 0.057115 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | single_llm | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 15.836000 | 770 | 1 | 0 | 0.051865 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | claude_code | try1 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 84.615107 | 3898 | `null` | 6 | 0.365156 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | claude_code | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 84.326990 | 4171 | `null` | 7 | 0.391487 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | claude_code | try3 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | `true` | 67.619682 | 3748 | `null` | 6 | 0.365242 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | claude_code | try4 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 98.288321 | 4491 | `null` | 11 | 0.499635 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | claude_code | try5 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 60.878060 | 2661 | `null` | 9 | 0.349808 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 46.617000 | 6999 | 3 | 2 | 0.090901 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | generic_agent | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 54.194000 | 10502 | 4 | 4 | 0.123793 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 59.174000 | 8767 | 5 | 4 | 0.126585 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | generic_agent | try4 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 51.323000 | 8928 | 4 | 4 | 0.114809 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | generic_agent | try5 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 49.912000 | 7901 | 4 | 3 | 0.110740 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | proposed_agent | try1 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 101.308000 | 14087 | 4 | 4 | 0.264866 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | proposed_agent | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 78.372000 | 9455 | 3 | 2 | 0.200407 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | proposed_agent | try3 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 84.819000 | 9151 | 3 | 2 | 0.201963 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | proposed_agent | try4 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 80.493000 | 9365 | 3 | 2 | 0.199453 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | proposed_agent | try5 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 77.494000 | 8805 | 3 | 2 | 0.198309 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | rule_based | try1 | 0.666667 | 0.333333 | 0.444444 | 1.000000 | 0.250000 | 0.400000 | 0.347222 | 0.422222 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 28.200000 | 1731 | 1 | 0 | 0.065356 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | single_llm | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 22.911000 | 1386 | 1 | 0 | 0.061158 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | single_llm | try3 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 24.683000 | 1574 | 1 | 0 | 0.063978 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | single_llm | try4 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 24.552000 | 1565 | 1 | 0 | 0.063843 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | single_llm | try5 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 26.862000 | 1577 | 1 | 0 | 0.064023 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | claude_code | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 71.201150 | 3258 | `null` | 6 | 0.354251 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | claude_code | try2 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 68.997489 | 2313 | `null` | 4 | 0.318981 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | claude_code | try3 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 74.164684 | 3588 | `null` | 6 | 0.364990 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | claude_code | try4 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 64.849384 | 2951 | `null` | 10 | 0.429208 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | claude_code | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 71.616400 | 3050 | `null` | 10 | 0.379854 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | generic_agent | try1 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 48.597000 | 8250 | 4 | 4 | 0.110515 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | generic_agent | try2 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 29.133000 | 3724 | 2 | 1 | 0.057311 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | generic_agent | try3 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 58.340000 | 8472 | 4 | 4 | 0.116738 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | generic_agent | try4 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 43.463000 | 5409 | 3 | 2 | 0.084144 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | generic_agent | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 30.514000 | 3464 | 2 | 1 | 0.056523 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | proposed_agent | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 100.710000 | 13342 | 4 | 3 | 0.268307 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | proposed_agent | try2 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 88.163000 | 12170 | 4 | 3 | 0.257267 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | proposed_agent | try3 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 0.500000 | 0.666667 | 0.450000 | 0.533334 | `false` | 87.154000 | 11685 | 4 | 3 | 0.254595 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | proposed_agent | try4 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 72.527000 | 7768 | 3 | 2 | 0.193420 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | proposed_agent | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 67.927000 | 7479 | 3 | 2 | 0.191989 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | rule_based | try1 | 1.000000 | 0.250000 | 0.400000 | 0.500000 | 0.500000 | 0.500000 | 0.450000 | 0.450000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | single_llm | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 19.634000 | 1371 | 1 | 0 | 0.060005 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | single_llm | try2 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 19.143000 | 1259 | 1 | 0 | 0.059238 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | single_llm | try3 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 14.673000 | 991 | 1 | 0 | 0.055218 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | single_llm | try4 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 18.581000 | 1230 | 1 | 0 | 0.058803 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | single_llm | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 19.527000 | 1361 | 1 | 0 | 0.060768 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.720000 | 0.500000 | 0.589091 | 1.000000 | 1.000000 | 1.000000 | 0.794546 | 0.794546 | 0.000119 | 114.910109 | 5074.000000 | `null` | 8.600000 | 0.445671 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.730000 | 0.533333 | 0.614546 | 1.000000 | 1.000000 | 1.000000 | 0.807273 | 0.807273 | 0.000906 | 57.996200 | 9570.800000 | 5.000000 | 4.600000 | 0.179770 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 2400 | `null` | `null` | `null` | `null` |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.633334 | 0.773333 | 1.000000 | 1.000000 | 1.000000 | 0.886667 | 0.886667 | 0.000711 | 45.133200 | 5218.800000 | 3.000000 | 2.000000 | 0.318348 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.666667 | 0.333333 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| mercedes-benz-greener-manufacturing | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | 0.000000 | 9.672400 | 456.600000 | 1.000000 | 0.000000 | 0.199658 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | 0.000000 | 63.637216 | 3187.000000 | `null` | 6.200000 | 0.351506 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | 0.000000 | 49.141400 | 7584.000000 | 4.200000 | 3.800000 | 0.107756 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.350000 | 0.506667 | 1.000000 | 1.000000 | 1.000000 | 0.753333 | 0.753333 | 0.004267 | 54.157400 | 6647.200000 | 3.200000 | 2.000000 | 0.181705 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.500000 | 0.250000 | 0.333333 | 0.000000 | 1.000000 | 0.000000 | 0.666667 | 0.166666 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| mercedes-benz-greener-manufacturing | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.300000 | 0.453333 | 1.000000 | 1.000000 | 1.000000 | 0.726667 | 0.726667 | 0.002844 | 15.857200 | 828.000000 | 1.000000 | 0.000000 | 0.052584 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.433333 | 0.600000 | 1.000000 | 0.700000 | 0.819048 | 0.650000 | 0.709524 | 0.006667 | 79.145632 | 3793.800000 | `null` | 7.800000 | 0.394266 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | 0.000000 | 52.244000 | 8619.400000 | 4.000000 | 3.400000 | 0.113366 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | 0.000000 | 84.497200 | 10172.600000 | 3.200000 | 2.400000 | 0.212999 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.666667 | 0.333333 | 0.444444 | 1.000000 | 0.250000 | 0.400000 | 0.347222 | 0.422222 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| mercedes-benz-greener-manufacturing | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | 0.000000 | 25.441600 | 1566.600000 | 1.000000 | 0.000000 | 0.063672 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | 0.000000 | 70.165821 | 3032.000000 | `null` | 7.200000 | 0.369457 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 0.800000 | 0.250000 | 0.373333 | 1.000000 | 1.000000 | 1.000000 | 0.686667 | 0.686667 | 0.000267 | 42.009400 | 5863.800000 | 3.000000 | 2.400000 | 0.085046 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | proposed_agent | 5 | `true` | 0.800000 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 0.900000 | 0.933333 | 0.650000 | 0.666667 | 0.010000 | 83.296200 | 10488.800000 | 3.600000 | 2.600000 | 0.233116 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 1.000000 | 0.250000 | 0.400000 | 0.500000 | 0.500000 | 0.500000 | 0.450000 | 0.450000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| mercedes-benz-greener-manufacturing | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | 0.000000 | 18.311600 | 1242.400000 | 1.000000 | 0.000000 | 0.058806 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 1.000000 | 0.930000 | 0.358333 | 0.497273 | 1.000000 | 0.925000 | 0.954762 | 0.711136 | 0.726017 | 0.001697 | 81.964695 | 3771.700000 | `null` | 7.450000 | 0.390225 |
| generic_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.757500 | 0.383333 | 0.496970 | 1.000000 | 0.937500 | 0.964286 | 0.717235 | 0.730628 | 0.000293 | 50.347750 | 7909.500000 | 4.050000 | 3.550000 | 0.121484 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 2400.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 0.950000 | 1.000000 | 0.433333 | 0.586667 | 1.000000 | 0.975000 | 0.983333 | 0.780833 | 0.785000 | 0.003744 | 66.771000 | 8131.850000 | 3.250000 | 2.250000 | 0.236542 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.708333 | 0.291666 | 0.405555 | 0.625000 | 0.687500 | 0.475000 | 0.546528 | 0.440277 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 1.000000 | 0.429167 | 0.580000 | 1.000000 | 1.000000 | 1.000000 | 0.790000 | 0.790000 | 0.000711 | 17.320700 | 1023.400000 | 1.000000 | 0.000000 | 0.093680 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task mercedes-benz-greener-manufacturing --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/mercedes-benz-greener-manufacturing-all.md
```
