# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `santander-customer-transaction-prediction`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.857143`
- Mean Add Precision: `0.742857`
- Mean Add Recall: `0.555555`
- Mean Add F1: `0.609524`
- Mean Remove Precision: `0.809524`
- Mean Remove Recall: `0.823810`
- Mean Remove F1: `0.755556`
- Mean Task Completion Score: `0.716667`
- Mean Strict Task Completion Score: `0.682540`
- Mean Task Completion Variance: `0.004571`
- Mean Runtime (s): `164.764765`
- Mean Total Tokens: `4826.375000`
- Mean API Calls: `2.100000`
- Mean Tool Calls: `3.550000`
- Mean Cost (USD): `0.061141`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| santander-customer-transaction-prediction | AUC | finance | binary_classification | single_table | medium (200000) | high (200) | low (3) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| santander-customer-transaction-prediction | 21 | 6 | 0.857143 | 4.047619 | 0.742857 | 0.555555 | 0.609524 | 0.809524 | 0.823810 | 0.755556 | 0.716667 | 0.682540 | 0.004571 | 164.764765 | 4826.375000 | 2.100000 | 3.550000 | 0.061141 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| santander-customer-transaction-prediction | tc1_from_scratch | claude_code | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 97.587103 | 4287 | `null` | 10 | 0.157542 |
| santander-customer-transaction-prediction | tc1_from_scratch | claude_code | try2 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 185.566584 | 9264 | `null` | 25 | 0.341607 |
| santander-customer-transaction-prediction | tc1_from_scratch | claude_code | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 88.363988 | 5247 | `null` | 14 | 0.221302 |
| santander-customer-transaction-prediction | tc1_from_scratch | claude_code | try4 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 114.681926 | 5853 | `null` | 13 | 0.198192 |
| santander-customer-transaction-prediction | tc1_from_scratch | claude_code | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 92.998502 | 4487 | `null` | 11 | 0.184289 |
| santander-customer-transaction-prediction | tc1_from_scratch | generic_agent | try1 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 40.623000 | 7228 | 4 | 5 | 0.066667 |
| santander-customer-transaction-prediction | tc1_from_scratch | generic_agent | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 46.273000 | 9065 | 5 | 5 | 0.066795 |
| santander-customer-transaction-prediction | tc1_from_scratch | generic_agent | try3 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 49.621000 | 9939 | 5 | 5 | 0.077198 |
| santander-customer-transaction-prediction | tc1_from_scratch | generic_agent | try4 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 29.980000 | 3158 | 3 | 3 | 0.033768 |
| santander-customer-transaction-prediction | tc1_from_scratch | generic_agent | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 40.269000 | 6493 | 4 | 4 | 0.052284 |
| santander-customer-transaction-prediction | tc1_from_scratch | human | human_tc1_v1 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 2700 | `null` | `null` | `null` | `null` |
| santander-customer-transaction-prediction | tc1_from_scratch | proposed_agent | try1 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 35.551000 | 5452 | 3 | 2 | 0.068977 |
| santander-customer-transaction-prediction | tc1_from_scratch | proposed_agent | try2 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 33.263000 | 5279 | 3 | 2 | 0.045379 |
| santander-customer-transaction-prediction | tc1_from_scratch | proposed_agent | try3 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 41.082000 | 8411 | 4 | 4 | 0.064000 |
| santander-customer-transaction-prediction | tc1_from_scratch | proposed_agent | try4 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 55.646000 | 7870 | 4 | 4 | 0.057673 |
| santander-customer-transaction-prediction | tc1_from_scratch | proposed_agent | try5 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 60.912000 | 8935 | 4 | 4 | 0.065092 |
| santander-customer-transaction-prediction | tc1_from_scratch | rule_based | try1 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| santander-customer-transaction-prediction | tc1_from_scratch | single_llm | try1 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 5.218000 | 282 | 1 | 0 | 0.022447 |
| santander-customer-transaction-prediction | tc1_from_scratch | single_llm | try2 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 9.260000 | 411 | 1 | 0 | 0.007764 |
| santander-customer-transaction-prediction | tc1_from_scratch | single_llm | try3 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 10.619000 | 591 | 1 | 0 | 0.010464 |
| santander-customer-transaction-prediction | tc1_from_scratch | single_llm | try4 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 10.264000 | 598 | 1 | 0 | 0.010569 |
| santander-customer-transaction-prediction | tc1_from_scratch | single_llm | try5 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 9.589000 | 465 | 1 | 0 | 0.008574 |
| santander-customer-transaction-prediction | tc2_partial_good | claude_code | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 64.485340 | 3472 | `null` | 7 | 0.129043 |
| santander-customer-transaction-prediction | tc2_partial_good | claude_code | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 73.628376 | 3979 | `null` | 11 | 0.161108 |
| santander-customer-transaction-prediction | tc2_partial_good | claude_code | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 90.376756 | 4039 | `null` | 11 | 0.164377 |
| santander-customer-transaction-prediction | tc2_partial_good | claude_code | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 79.940022 | 4065 | `null` | 12 | 0.167508 |
| santander-customer-transaction-prediction | tc2_partial_good | claude_code | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 87.179377 | 4417 | `null` | 13 | 0.189698 |
| santander-customer-transaction-prediction | tc2_partial_good | generic_agent | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 51.961000 | 8246 | 6 | 5 | 0.066813 |
| santander-customer-transaction-prediction | tc2_partial_good | generic_agent | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 38.372000 | 6711 | 4 | 5 | 0.050703 |
| santander-customer-transaction-prediction | tc2_partial_good | generic_agent | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 38.346000 | 6133 | 4 | 3 | 0.051426 |
| santander-customer-transaction-prediction | tc2_partial_good | generic_agent | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 31.905000 | 6848 | 4 | 5 | 0.050226 |
| santander-customer-transaction-prediction | tc2_partial_good | generic_agent | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 28.560000 | 4534 | 3 | 3 | 0.038323 |
| santander-customer-transaction-prediction | tc2_partial_good | proposed_agent | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 37.319000 | 5374 | 3 | 2 | 0.048545 |
| santander-customer-transaction-prediction | tc2_partial_good | proposed_agent | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 37.596000 | 5138 | 3 | 2 | 0.046156 |
| santander-customer-transaction-prediction | tc2_partial_good | proposed_agent | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 36.856000 | 4881 | 3 | 2 | 0.046733 |
| santander-customer-transaction-prediction | tc2_partial_good | proposed_agent | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 37.923000 | 4714 | 3 | 2 | 0.046352 |
| santander-customer-transaction-prediction | tc2_partial_good | proposed_agent | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 32.772000 | 4525 | 3 | 2 | 0.042173 |
| santander-customer-transaction-prediction | tc2_partial_good | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| santander-customer-transaction-prediction | tc2_partial_good | single_llm | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 7.165000 | 395 | 1 | 0 | 0.006809 |
| santander-customer-transaction-prediction | tc2_partial_good | single_llm | try2 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 8.217000 | 393 | 1 | 0 | 0.007535 |
| santander-customer-transaction-prediction | tc2_partial_good | single_llm | try3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 8.991000 | 363 | 1 | 0 | 0.007085 |
| santander-customer-transaction-prediction | tc2_partial_good | single_llm | try4 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 7.748000 | 379 | 1 | 0 | 0.007325 |
| santander-customer-transaction-prediction | tc2_partial_good | single_llm | try5 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 7.518000 | 382 | 1 | 0 | 0.007370 |
| santander-customer-transaction-prediction | tc3_fault_injected | claude_code | try1 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.500000 | 0.666667 | 0.250000 | 0.333334 | `false` | 78.988462 | 4168 | `null` | 8 | 0.154790 |
| santander-customer-transaction-prediction | tc3_fault_injected | claude_code | try2 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.500000 | 0.666667 | 0.250000 | 0.333334 | `false` | 93.786595 | 4714 | `null` | 10 | 0.180157 |
| santander-customer-transaction-prediction | tc3_fault_injected | claude_code | try3 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 0.500000 | 0.666667 | 0.450000 | 0.533334 | `false` | 76.512602 | 4002 | `null` | 8 | 0.158384 |
| santander-customer-transaction-prediction | tc3_fault_injected | claude_code | try4 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.500000 | 0.666667 | 0.250000 | 0.333334 | `false` | 73.534068 | 3460 | `null` | 8 | 0.148489 |
| santander-customer-transaction-prediction | tc3_fault_injected | claude_code | try5 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.500000 | 0.666667 | 0.250000 | 0.333334 | `false` | 162.842002 | 7818 | `null` | 16 | 0.289021 |
| santander-customer-transaction-prediction | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 36.206000 | 8420 | 3 | 3 | 0.057587 |
| santander-customer-transaction-prediction | tc3_fault_injected | generic_agent | try2 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 41.347000 | 7433 | 4 | 4 | 0.057975 |
| santander-customer-transaction-prediction | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 44.072000 | 7582 | 3 | 3 | 0.056455 |
| santander-customer-transaction-prediction | tc3_fault_injected | generic_agent | try4 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 47.959000 | 10238 | 5 | 4 | 0.071411 |
| santander-customer-transaction-prediction | tc3_fault_injected | generic_agent | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 45.729000 | 8770 | 3 | 3 | 0.065335 |
| santander-customer-transaction-prediction | tc3_fault_injected | proposed_agent | try1 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 70.949000 | 10798 | 5 | 5 | 0.077252 |
| santander-customer-transaction-prediction | tc3_fault_injected | proposed_agent | try2 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 51.503000 | 8379 | 4 | 3 | 0.068367 |
| santander-customer-transaction-prediction | tc3_fault_injected | proposed_agent | try3 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 54.766000 | 8073 | 4 | 3 | 0.067670 |
| santander-customer-transaction-prediction | tc3_fault_injected | proposed_agent | try4 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 73.751000 | 9604 | 5 | 4 | 0.071574 |
| santander-customer-transaction-prediction | tc3_fault_injected | proposed_agent | try5 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 56.970000 | 8777 | 4 | 3 | 0.073814 |
| santander-customer-transaction-prediction | tc3_fault_injected | rule_based | try1 | 1.000000 | 0.333333 | 0.500000 | 0.000000 | 0.000000 | 0.000000 | 0.250000 | 0.250000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| santander-customer-transaction-prediction | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 6.813000 | 400 | 1 | 0 | 0.006860 |
| santander-customer-transaction-prediction | tc3_fault_injected | single_llm | try2 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 7.234000 | 380 | 1 | 0 | 0.007347 |
| santander-customer-transaction-prediction | tc3_fault_injected | single_llm | try3 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 7.949000 | 397 | 1 | 0 | 0.007602 |
| santander-customer-transaction-prediction | tc3_fault_injected | single_llm | try4 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 5.894000 | 326 | 1 | 0 | 0.006537 |
| santander-customer-transaction-prediction | tc3_fault_injected | single_llm | try5 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 7.671000 | 360 | 1 | 0 | 0.007047 |
| santander-customer-transaction-prediction | tc4_mixed_history | claude_code | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 106.115539 | 5008 | `null` | 15 | 0.209907 |
| santander-customer-transaction-prediction | tc4_mixed_history | claude_code | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 60.104877 | 3125 | `null` | 6 | 0.121337 |
| santander-customer-transaction-prediction | tc4_mixed_history | claude_code | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 72.718932 | 3347 | `null` | 7 | 0.126114 |
| santander-customer-transaction-prediction | tc4_mixed_history | claude_code | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 59.943269 | 3575 | `null` | 9 | 0.143603 |
| santander-customer-transaction-prediction | tc4_mixed_history | claude_code | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 76.438010 | 3563 | `null` | 9 | 0.149512 |
| santander-customer-transaction-prediction | tc4_mixed_history | generic_agent | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 31.351000 | 6638 | 4 | 4 | 0.048566 |
| santander-customer-transaction-prediction | tc4_mixed_history | generic_agent | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 27.494000 | 6047 | 3 | 2 | 0.041612 |
| santander-customer-transaction-prediction | tc4_mixed_history | generic_agent | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 36.419000 | 6997 | 4 | 5 | 0.053838 |
| santander-customer-transaction-prediction | tc4_mixed_history | generic_agent | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 25.190000 | 3733 | 2 | 2 | 0.032309 |
| santander-customer-transaction-prediction | tc4_mixed_history | generic_agent | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 26.915000 | 3969 | 2 | 2 | 0.034205 |
| santander-customer-transaction-prediction | tc4_mixed_history | proposed_agent | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 51.852000 | 8393 | 4 | 3 | 0.067341 |
| santander-customer-transaction-prediction | tc4_mixed_history | proposed_agent | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 54.216000 | 8732 | 4 | 3 | 0.071082 |
| santander-customer-transaction-prediction | tc4_mixed_history | proposed_agent | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 57.649000 | 9097 | 4 | 3 | 0.076190 |
| santander-customer-transaction-prediction | tc4_mixed_history | proposed_agent | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 47.526000 | 5975 | 3 | 2 | 0.057781 |
| santander-customer-transaction-prediction | tc4_mixed_history | proposed_agent | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 53.255000 | 5876 | 3 | 2 | 0.059152 |
| santander-customer-transaction-prediction | tc4_mixed_history | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| santander-customer-transaction-prediction | tc4_mixed_history | single_llm | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 19.360000 | 1142 | 1 | 0 | 0.017966 |
| santander-customer-transaction-prediction | tc4_mixed_history | single_llm | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 23.331000 | 1224 | 1 | 0 | 0.020015 |
| santander-customer-transaction-prediction | tc4_mixed_history | single_llm | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 22.262000 | 1182 | 1 | 0 | 0.019385 |
| santander-customer-transaction-prediction | tc4_mixed_history | single_llm | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 19.624000 | 1025 | 1 | 0 | 0.017030 |
| santander-customer-transaction-prediction | tc4_mixed_history | single_llm | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 19.832000 | 1060 | 1 | 0 | 0.017555 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| santander-customer-transaction-prediction | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.800000 | 0.733333 | 0.760000 | 1.000000 | 1.000000 | 1.000000 | 0.880000 | 0.880000 | 0.021600 | 115.839621 | 5827.600000 | `null` | 14.600000 | 0.220587 |
| santander-customer-transaction-prediction | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.700000 | 0.600000 | 0.640000 | 1.000000 | 1.000000 | 1.000000 | 0.820000 | 0.820000 | 0.021600 | 41.353200 | 7176.600000 | 4.200000 | 4.400000 | 0.059342 |
| santander-customer-transaction-prediction | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | 0.000000 | 2700 | `null` | `null` | `null` | `null` |
| santander-customer-transaction-prediction | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | 0.000000 | 45.290800 | 7189.400000 | 3.600000 | 3.200000 | 0.060224 |
| santander-customer-transaction-prediction | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| santander-customer-transaction-prediction | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | 0.000000 | 8.990000 | 469.400000 | 1.000000 | 0.000000 | 0.011963 |
| santander-customer-transaction-prediction | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 79.121974 | 3994.400000 | `null` | 10.800000 | 0.162347 |
| santander-customer-transaction-prediction | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 37.828800 | 6494.400000 | 4.200000 | 4.200000 | 0.051498 |
| santander-customer-transaction-prediction | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 36.493200 | 4926.400000 | 3.000000 | 2.000000 | 0.045992 |
| santander-customer-transaction-prediction | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| santander-customer-transaction-prediction | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | 0.000000 | 7.927800 | 382.400000 | 1.000000 | 0.000000 | 0.007225 |
| santander-customer-transaction-prediction | tc3_fault_injected | claude_code | 5 | `false` | 0.000000 | 0.100000 | 0.066667 | 0.080000 | 1.000000 | 0.500000 | 0.666667 | 0.290000 | 0.373334 | 0.006400 | 97.132746 | 4832.400000 | `null` | 10.000000 | 0.186168 |
| santander-customer-transaction-prediction | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.600000 | 0.720000 | 1.000000 | 0.800000 | 0.866667 | 0.760000 | 0.793333 | 0.046400 | 43.062600 | 8488.600000 | 3.600000 | 3.400000 | 0.061753 |
| santander-customer-transaction-prediction | tc3_fault_injected | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | 0.000000 | 61.587800 | 9126.200000 | 4.400000 | 3.600000 | 0.071735 |
| santander-customer-transaction-prediction | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 1.000000 | 0.333333 | 0.500000 | 0.000000 | 0.000000 | 0.000000 | 0.250000 | 0.250000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| santander-customer-transaction-prediction | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | 0.000000 | 7.112200 | 372.600000 | 1.000000 | 0.000000 | 0.007079 |
| santander-customer-transaction-prediction | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 75.064126 | 3723.600000 | `null` | 9.200000 | 0.150095 |
| santander-customer-transaction-prediction | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 29.473800 | 5476.800000 | 3.000000 | 3.000000 | 0.042106 |
| santander-customer-transaction-prediction | tc4_mixed_history | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 52.899600 | 7614.600000 | 3.600000 | 2.600000 | 0.066309 |
| santander-customer-transaction-prediction | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| santander-customer-transaction-prediction | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 20.881800 | 1126.600000 | 1.000000 | 0.000000 | 0.018390 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 0.750000 | 5.000000 | 0.750000 | 0.725000 | 0.700000 | 0.710000 | 1.000000 | 0.875000 | 0.916667 | 0.792500 | 0.813334 | 0.007000 | 91.789617 | 4594.500000 | `null` | 11.150000 | 0.179799 |
| generic_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.925000 | 0.800000 | 0.840000 | 1.000000 | 0.950000 | 0.966667 | 0.895000 | 0.903333 | 0.017000 | 37.929600 | 6909.100000 | 3.750000 | 3.750000 | 0.053675 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | 0.000000 | 2700.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.875000 | 0.666667 | 0.725000 | 1.000000 | 0.875000 | 0.916667 | 0.800000 | 0.820833 | 0.000000 | 49.067850 | 7214.150000 | 3.650000 | 2.850000 | 0.061065 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.500000 | 0.166666 | 0.250000 | 0.250000 | 0.500000 | 0.250000 | 0.375000 | 0.250000 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 0.625000 | 0.416666 | 0.475000 | 0.750000 | 0.875000 | 0.666667 | 0.675000 | 0.570833 | 0.000000 | 11.227950 | 587.750000 | 1.000000 | 0.000000 | 0.011164 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task santander-customer-transaction-prediction --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/santander-customer-transaction-prediction-all.md
```
