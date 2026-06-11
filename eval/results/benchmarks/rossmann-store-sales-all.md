# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `rossmann-store-sales`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.904762`
- Mean Add Precision: `0.581277`
- Mean Add Recall: `0.475340`
- Mean Add F1: `0.517051`
- Mean Remove Precision: `0.800000`
- Mean Remove Recall: `0.862698`
- Mean Remove F1: `0.751383`
- Mean Task Completion Score: `0.689874`
- Mean Strict Task Completion Score: `0.634217`
- Mean Task Completion Variance: `0.002361`
- Mean Runtime (s): `204.758290`
- Mean Total Tokens: `10088.975000`
- Mean API Calls: `2.650000`
- Mean Tool Calls: `4.870000`
- Mean Cost (USD): `0.117668`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rossmann-store-sales | RMSPE | retail_forecasting | forecasting | multi_table_lookup | large (1017209) | low (19) | medium (12) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rossmann-store-sales | 21 | 6 | 0.904762 | 4.047619 | 0.581277 | 0.475340 | 0.517051 | 0.800000 | 0.862698 | 0.751383 | 0.689874 | 0.634217 | 0.002361 | 204.758290 | 10088.975000 | 2.650000 | 4.870000 | 0.117668 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rossmann-store-sales | tc1_from_scratch | claude_code | try1 | 0.750000 | 0.642857 | 0.692308 | 1.000000 | 1.000000 | 1.000000 | 0.846154 | 0.846154 | `true` | 191.171621 | 3670 | `null` | 13 | 0.389118 |
| rossmann-store-sales | tc1_from_scratch | claude_code | try2 | 0.714286 | 0.714286 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 87.752521 | 2744 | `null` | 10 | 0.222440 |
| rossmann-store-sales | tc1_from_scratch | claude_code | try3 | 0.714286 | 0.714286 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 281.772794 | 3983 | `null` | 29 | 0.496720 |
| rossmann-store-sales | tc1_from_scratch | claude_code | try4 | 0.714286 | 0.714286 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 62.054146 | 2935 | `null` | 7 | 0.186640 |
| rossmann-store-sales | tc1_from_scratch | claude_code | try5 | 0.666667 | 0.714286 | 0.689655 | 1.000000 | 1.000000 | 1.000000 | 0.844828 | 0.844828 | `true` | 139.341543 | 3419 | `null` | 15 | 0.244571 |
| rossmann-store-sales | tc1_from_scratch | generic_agent | try1 | 0.642857 | 0.642857 | 0.642857 | 1.000000 | 1.000000 | 1.000000 | 0.821429 | 0.821429 | `true` | 93.650000 | 16143 | 5 | 6 | 0.171023 |
| rossmann-store-sales | tc1_from_scratch | generic_agent | try2 | 0.692308 | 0.642857 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 62.613000 | 15718 | 5 | 6 | 0.123995 |
| rossmann-store-sales | tc1_from_scratch | generic_agent | try3 | 0.714286 | 0.714286 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 56.254000 | 9556 | 4 | 5 | 0.087173 |
| rossmann-store-sales | tc1_from_scratch | generic_agent | try4 | 0.642857 | 0.642857 | 0.642857 | 1.000000 | 1.000000 | 1.000000 | 0.821429 | 0.821429 | `true` | 69.586000 | 12326 | 5 | 6 | 0.112990 |
| rossmann-store-sales | tc1_from_scratch | generic_agent | try5 | 0.714286 | 0.714286 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 70.546000 | 15485 | 5 | 7 | 0.122745 |
| rossmann-store-sales | tc1_from_scratch | human | human_tc1_sean_kraemer_v4_manual_rebuild | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 3000 | `null` | `null` | `null` | `null` |
| rossmann-store-sales | tc1_from_scratch | proposed_agent | try1 | 0.727273 | 0.571429 | 0.640000 | 1.000000 | 1.000000 | 1.000000 | 0.820000 | 0.820000 | `true` | 70.258000 | 16599 | 5 | 4 | 0.159278 |
| rossmann-store-sales | tc1_from_scratch | proposed_agent | try2 | 0.750000 | 0.642857 | 0.692308 | 1.000000 | 1.000000 | 1.000000 | 0.846154 | 0.846154 | `true` | 93.494000 | 20945 | 5 | 5 | 0.159983 |
| rossmann-store-sales | tc1_from_scratch | proposed_agent | try3 | 0.833333 | 0.714286 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 64.681000 | 14406 | 5 | 4 | 0.109504 |
| rossmann-store-sales | tc1_from_scratch | proposed_agent | try4 | 0.727273 | 0.571429 | 0.640000 | 1.000000 | 1.000000 | 1.000000 | 0.820000 | 0.820000 | `true` | 84.809000 | 18804 | 5 | 5 | 0.145058 |
| rossmann-store-sales | tc1_from_scratch | proposed_agent | try5 | 0.692308 | 0.642857 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 101.381000 | 26657 | 6 | 6 | 0.192726 |
| rossmann-store-sales | tc1_from_scratch | rule_based | try1 | 0.285714 | 0.285714 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc1_from_scratch | single_llm | try1 | 0.769231 | 0.714286 | 0.740741 | 1.000000 | 1.000000 | 1.000000 | 0.870370 | 0.870370 | `true` | 15.203000 | 974 | 1 | 0 | 0.017523 |
| rossmann-store-sales | tc1_from_scratch | single_llm | try2 | 0.846154 | 0.785714 | 0.814815 | 1.000000 | 1.000000 | 1.000000 | 0.907407 | 0.907407 | `true` | 16.182000 | 875 | 1 | 0 | 0.016621 |
| rossmann-store-sales | tc1_from_scratch | single_llm | try3 | 0.846154 | 0.785714 | 0.814815 | 1.000000 | 1.000000 | 1.000000 | 0.907407 | 0.907407 | `true` | 15.687000 | 917 | 1 | 0 | 0.017251 |
| rossmann-store-sales | tc1_from_scratch | single_llm | try4 | 0.846154 | 0.785714 | 0.814815 | 1.000000 | 1.000000 | 1.000000 | 0.907407 | 0.907407 | `true` | 14.676000 | 917 | 1 | 0 | 0.017251 |
| rossmann-store-sales | tc1_from_scratch | single_llm | try5 | 0.846154 | 0.785714 | 0.814815 | 1.000000 | 1.000000 | 1.000000 | 0.907407 | 0.907407 | `true` | 14.390000 | 883 | 1 | 0 | 0.016741 |
| rossmann-store-sales | tc2_partial_good | claude_code | try1 | 0.400000 | 0.250000 | 0.307692 | 0.000000 | 1.000000 | 0.000000 | 0.653846 | 0.153846 | `true` | 77.553572 | 2778 | `null` | 20 | 0.211240 |
| rossmann-store-sales | tc2_partial_good | claude_code | try2 | 0.666667 | 0.500000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 54.174196 | 1914 | `null` | 7 | 0.149457 |
| rossmann-store-sales | tc2_partial_good | claude_code | try3 | 0.500000 | 0.250000 | 0.333333 | 0.000000 | 1.000000 | 0.000000 | 0.666667 | 0.166666 | `true` | 55.348012 | 2823 | `null` | 8 | 0.162127 |
| rossmann-store-sales | tc2_partial_good | claude_code | try4 | 0.500000 | 0.375000 | 0.428571 | 0.000000 | 1.000000 | 0.000000 | 0.714286 | 0.214285 | `true` | 77.822109 | 2282 | `null` | 20 | 0.194021 |
| rossmann-store-sales | tc2_partial_good | claude_code | try5 | 0.333333 | 0.125000 | 0.181818 | 1.000000 | 1.000000 | 1.000000 | 0.590909 | 0.590909 | `true` | 67.540925 | 2627 | `null` | 10 | 0.208420 |
| rossmann-store-sales | tc2_partial_good | generic_agent | try1 | 0.571429 | 0.500000 | 0.533333 | 0.000000 | 1.000000 | 0.000000 | 0.766666 | 0.266666 | `true` | 82.478000 | 18784 | 5 | 7 | 0.140580 |
| rossmann-store-sales | tc2_partial_good | generic_agent | try2 | 0.428571 | 0.375000 | 0.400000 | 0.000000 | 1.000000 | 0.000000 | 0.700000 | 0.200000 | `true` | 96.607000 | 23108 | 7 | 7 | 0.174169 |
| rossmann-store-sales | tc2_partial_good | generic_agent | try3 | 0.400000 | 0.250000 | 0.307692 | 1.000000 | 1.000000 | 1.000000 | 0.653846 | 0.653846 | `true` | 72.172000 | 11901 | 4 | 5 | 0.104278 |
| rossmann-store-sales | tc2_partial_good | generic_agent | try4 | 0.428571 | 0.375000 | 0.400000 | 0.000000 | 1.000000 | 0.000000 | 0.700000 | 0.200000 | `true` | 86.289000 | 17185 | 6 | 7 | 0.147106 |
| rossmann-store-sales | tc2_partial_good | generic_agent | try5 | 0.500000 | 0.375000 | 0.428571 | 0.000000 | 1.000000 | 0.000000 | 0.714286 | 0.214285 | `true` | 89.121000 | 23625 | 6 | 8 | 0.174165 |
| rossmann-store-sales | tc2_partial_good | proposed_agent | try1 | 0.714286 | 0.625000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 74.019000 | 9940 | 3 | 2 | 0.098211 |
| rossmann-store-sales | tc2_partial_good | proposed_agent | try2 | 0.714286 | 0.625000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 87.447000 | 20347 | 5 | 6 | 0.142098 |
| rossmann-store-sales | tc2_partial_good | proposed_agent | try3 | 0.857143 | 0.750000 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 89.077000 | 17815 | 5 | 4 | 0.135857 |
| rossmann-store-sales | tc2_partial_good | proposed_agent | try4 | 0.714286 | 0.625000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 104.553000 | 23201 | 6 | 7 | 0.177135 |
| rossmann-store-sales | tc2_partial_good | proposed_agent | try5 | 0.714286 | 0.625000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 103.719000 | 26044 | 6 | 7 | 0.187291 |
| rossmann-store-sales | tc2_partial_good | rule_based | try1 | 0.090909 | 0.125000 | 0.105263 | 0.000000 | 1.000000 | 0.000000 | 0.552631 | 0.052631 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc2_partial_good | single_llm | try1 | 0.666667 | 0.500000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 39.177000 | 2365 | 1 | 0 | 0.076991 |
| rossmann-store-sales | tc2_partial_good | single_llm | try2 | 0.714286 | 0.625000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 46.125000 | 2755 | 1 | 0 | 0.044952 |
| rossmann-store-sales | tc2_partial_good | single_llm | try3 | 0.625000 | 0.625000 | 0.625000 | 0.000000 | 1.000000 | 0.000000 | 0.812500 | 0.312500 | `true` | 42.159000 | 2457 | 1 | 0 | 0.040482 |
| rossmann-store-sales | tc2_partial_good | single_llm | try4 | 0.666667 | 0.500000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 35.730000 | 2097 | 1 | 0 | 0.035082 |
| rossmann-store-sales | tc2_partial_good | single_llm | try5 | 0.714286 | 0.625000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 43.800000 | 2703 | 1 | 0 | 0.044172 |
| rossmann-store-sales | tc3_fault_injected | claude_code | try1 | 0.666667 | 0.571429 | 0.615385 | 1.000000 | 1.000000 | 1.000000 | 0.807692 | 0.807692 | `true` | 63.821234 | 3784 | `null` | 10 | 0.188621 |
| rossmann-store-sales | tc3_fault_injected | claude_code | try2 | 0.545455 | 0.428571 | 0.480000 | 1.000000 | 1.000000 | 1.000000 | 0.740000 | 0.740000 | `true` | 89.351452 | 3443 | `null` | 16 | 0.298387 |
| rossmann-store-sales | tc3_fault_injected | claude_code | try3 | 0.500000 | 0.357143 | 0.416667 | 1.000000 | 1.000000 | 1.000000 | 0.708333 | 0.708333 | `true` | 57.707521 | 3194 | `null` | 10 | 0.172513 |
| rossmann-store-sales | tc3_fault_injected | claude_code | try4 | 0.583333 | 0.500000 | 0.538462 | 1.000000 | 1.000000 | 1.000000 | 0.769231 | 0.769231 | `true` | 59.217999 | 3134 | `null` | 9 | 0.176102 |
| rossmann-store-sales | tc3_fault_injected | claude_code | try5 | 0.545455 | 0.428571 | 0.480000 | 1.000000 | 1.000000 | 1.000000 | 0.740000 | 0.740000 | `true` | 77.140110 | 2237 | `null` | 13 | 0.181127 |
| rossmann-store-sales | tc3_fault_injected | generic_agent | try1 | 0.615385 | 0.571429 | 0.592593 | 1.000000 | 1.000000 | 1.000000 | 0.796296 | 0.796296 | `true` | 68.326000 | 11746 | 4 | 4 | 0.107349 |
| rossmann-store-sales | tc3_fault_injected | generic_agent | try2 | 0.545455 | 0.428571 | 0.480000 | 1.000000 | 1.000000 | 1.000000 | 0.740000 | 0.740000 | `true` | 70.225000 | 17617 | 5 | 6 | 0.136140 |
| rossmann-store-sales | tc3_fault_injected | generic_agent | try3 | 0.545455 | 0.428571 | 0.480000 | 1.000000 | 1.000000 | 1.000000 | 0.740000 | 0.740000 | `true` | 81.304000 | 14375 | 5 | 7 | 0.128880 |
| rossmann-store-sales | tc3_fault_injected | generic_agent | try4 | 0.545455 | 0.428571 | 0.480000 | 1.000000 | 1.000000 | 1.000000 | 0.740000 | 0.740000 | `true` | 61.617000 | 10942 | 4 | 5 | 0.100886 |
| rossmann-store-sales | tc3_fault_injected | generic_agent | try5 | 0.583333 | 0.500000 | 0.538462 | 1.000000 | 1.000000 | 1.000000 | 0.769231 | 0.769231 | `true` | 80.421000 | 14405 | 5 | 5 | 0.128960 |
| rossmann-store-sales | tc3_fault_injected | proposed_agent | try1 | 0.555556 | 0.357143 | 0.434783 | 1.000000 | 0.500000 | 0.666667 | 0.467391 | 0.550725 | `false` | 94.082000 | 14143 | 4 | 3 | 0.127365 |
| rossmann-store-sales | tc3_fault_injected | proposed_agent | try2 | 0.625000 | 0.357143 | 0.454545 | 1.000000 | 1.000000 | 1.000000 | 0.727272 | 0.727272 | `true` | 71.526000 | 10267 | 3 | 2 | 0.100068 |
| rossmann-store-sales | tc3_fault_injected | proposed_agent | try3 | 0.666667 | 0.428571 | 0.521739 | 1.000000 | 0.500000 | 0.666667 | 0.510869 | 0.594203 | `true` | 92.376000 | 14477 | 4 | 3 | 0.130115 |
| rossmann-store-sales | tc3_fault_injected | proposed_agent | try4 | 0.666667 | 0.428571 | 0.521739 | 1.000000 | 0.500000 | 0.666667 | 0.510869 | 0.594203 | `true` | 80.398000 | 12941 | 4 | 3 | 0.115451 |
| rossmann-store-sales | tc3_fault_injected | proposed_agent | try5 | 0.666667 | 0.428571 | 0.521739 | 1.000000 | 0.500000 | 0.666667 | 0.510869 | 0.594203 | `true` | 92.178000 | 18139 | 5 | 5 | 0.142598 |
| rossmann-store-sales | tc3_fault_injected | rule_based | try1 | 0.333333 | 0.285714 | 0.307692 | 1.000000 | 0.250000 | 0.400000 | 0.278846 | 0.353846 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc3_fault_injected | single_llm | try1 | 0.769231 | 0.714286 | 0.740741 | 1.000000 | 1.000000 | 1.000000 | 0.870370 | 0.870370 | `true` | 49.745000 | 3305 | 1 | 0 | 0.052188 |
| rossmann-store-sales | tc3_fault_injected | single_llm | try2 | 0.769231 | 0.714286 | 0.740741 | 1.000000 | 1.000000 | 1.000000 | 0.870370 | 0.870370 | `true` | 42.737000 | 2809 | 1 | 0 | 0.045725 |
| rossmann-store-sales | tc3_fault_injected | single_llm | try3 | 0.636364 | 0.500000 | 0.560000 | 1.000000 | 1.000000 | 1.000000 | 0.780000 | 0.780000 | `true` | 43.391000 | 2914 | 1 | 0 | 0.047300 |
| rossmann-store-sales | tc3_fault_injected | single_llm | try4 | 0.636364 | 0.500000 | 0.560000 | 1.000000 | 1.000000 | 1.000000 | 0.780000 | 0.780000 | `true` | 51.668000 | 3271 | 1 | 0 | 0.052655 |
| rossmann-store-sales | tc3_fault_injected | single_llm | try5 | 0.846154 | 0.785714 | 0.814815 | 1.000000 | 1.000000 | 1.000000 | 0.907407 | 0.907407 | `true` | 47.008000 | 3078 | 1 | 0 | 0.049760 |
| rossmann-store-sales | tc4_mixed_history | claude_code | try1 | 0.750000 | 0.428571 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 73.573852 | 3214 | `null` | 13 | 0.265804 |
| rossmann-store-sales | tc4_mixed_history | claude_code | try2 | 0.600000 | 0.428571 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 254.056336 | 2452 | `null` | 19 | 0.483433 |
| rossmann-store-sales | tc4_mixed_history | claude_code | try3 | 0.500000 | 0.428571 | 0.461538 | 0.750000 | 1.000000 | 0.857143 | 0.730769 | 0.659340 | `true` | 104.779697 | 3329 | `null` | 13 | 0.235377 |
| rossmann-store-sales | tc4_mixed_history | claude_code | try4 | 0.600000 | 0.428571 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 74.268010 | 3082 | `null` | 13 | 0.186947 |
| rossmann-store-sales | tc4_mixed_history | claude_code | try5 | 0.800000 | 0.571429 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 288.646826 | 2257 | `null` | 30 | 0.592032 |
| rossmann-store-sales | tc4_mixed_history | generic_agent | try1 | 0.666667 | 0.571429 | 0.615385 | 1.000000 | 1.000000 | 1.000000 | 0.807692 | 0.807692 | `true` | 82.605000 | 19788 | 5 | 5 | 0.147721 |
| rossmann-store-sales | tc4_mixed_history | generic_agent | try2 | 0.666667 | 0.571429 | 0.615385 | 0.750000 | 1.000000 | 0.857143 | 0.807692 | 0.736264 | `true` | 61.506000 | 13435 | 4 | 3 | 0.109245 |
| rossmann-store-sales | tc4_mixed_history | generic_agent | try3 | 0.428571 | 0.428571 | 0.428571 | 0.750000 | 1.000000 | 0.857143 | 0.714286 | 0.642857 | `true` | 72.927000 | 13621 | 4 | 4 | 0.120768 |
| rossmann-store-sales | tc4_mixed_history | generic_agent | try4 | 0.666667 | 0.571429 | 0.615385 | 0.750000 | 1.000000 | 0.857143 | 0.807692 | 0.736264 | `true` | 79.332000 | 15791 | 5 | 6 | 0.132725 |
| rossmann-store-sales | tc4_mixed_history | generic_agent | try5 | 0.666667 | 0.571429 | 0.615385 | 1.000000 | 1.000000 | 1.000000 | 0.807692 | 0.807692 | `true` | 98.182000 | 18748 | 5 | 7 | 0.157980 |
| rossmann-store-sales | tc4_mixed_history | proposed_agent | try1 | 0.500000 | 0.285714 | 0.363636 | 1.000000 | 0.333333 | 0.500000 | 0.348484 | 0.431818 | `false` | 177.146000 | 32005 | 5 | 4 | 0.242964 |
| rossmann-store-sales | tc4_mixed_history | proposed_agent | try2 | 0.500000 | 0.285714 | 0.363636 | 0.000000 | 0.000000 | 0.000000 | 0.181818 | 0.181818 | `false` | 110.033000 | 18127 | 4 | 3 | 0.156693 |
| rossmann-store-sales | tc4_mixed_history | proposed_agent | try3 | 0.750000 | 0.428571 | 0.545455 | 1.000000 | 0.666667 | 0.800000 | 0.606061 | 0.672728 | `true` | 143.497000 | 26236 | 5 | 6 | 0.206427 |
| rossmann-store-sales | tc4_mixed_history | proposed_agent | try4 | 0.600000 | 0.428571 | 0.500000 | 1.000000 | 0.333333 | 0.500000 | 0.416666 | 0.500000 | `false` | 122.529000 | 25340 | 5 | 4 | 0.184095 |
| rossmann-store-sales | tc4_mixed_history | proposed_agent | try5 | 0.500000 | 0.285714 | 0.363636 | 0.000000 | 0.000000 | 0.000000 | 0.181818 | 0.181818 | `false` | 145.650000 | 21894 | 4 | 3 | 0.195096 |
| rossmann-store-sales | tc4_mixed_history | rule_based | try1 | 0.100000 | 0.142857 | 0.117647 | 0.000000 | 0.000000 | 0.000000 | 0.058824 | 0.058824 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc4_mixed_history | single_llm | try1 | 0.714286 | 0.714286 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 36.787000 | 2385 | 1 | 0 | 0.038004 |
| rossmann-store-sales | tc4_mixed_history | single_llm | try2 | 0.833333 | 0.714286 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 48.569000 | 2883 | 1 | 0 | 0.046955 |
| rossmann-store-sales | tc4_mixed_history | single_llm | try3 | 0.666667 | 0.571429 | 0.615385 | 1.000000 | 1.000000 | 1.000000 | 0.807692 | 0.807692 | `true` | 36.123000 | 2261 | 1 | 0 | 0.037625 |
| rossmann-store-sales | tc4_mixed_history | single_llm | try4 | 0.666667 | 0.571429 | 0.615385 | 1.000000 | 1.000000 | 1.000000 | 0.807692 | 0.807692 | `true` | 40.644000 | 2574 | 1 | 0 | 0.042320 |
| rossmann-store-sales | tc4_mixed_history | single_llm | try5 | 0.714286 | 0.714286 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 44.111000 | 2768 | 1 | 0 | 0.045230 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rossmann-store-sales | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.711905 | 0.700000 | 0.704964 | 1.000000 | 1.000000 | 1.000000 | 0.852482 | 0.852482 | 0.000033 | 152.418525 | 3350.200000 | `null` | 14.800000 | 0.307898 |
| rossmann-store-sales | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.681319 | 0.671429 | 0.676191 | 1.000000 | 1.000000 | 1.000000 | 0.838095 | 0.838095 | 0.000261 | 70.529800 | 13845.600000 | 4.800000 | 6.000000 | 0.123585 |
| rossmann-store-sales | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | 0.000000 | 3000 | `null` | `null` | `null` | `null` |
| rossmann-store-sales | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.746037 | 0.628572 | 0.681641 | 1.000000 | 1.000000 | 1.000000 | 0.840820 | 0.840820 | 0.000574 | 82.924600 | 19482.200000 | 5.200000 | 4.800000 | 0.153310 |
| rossmann-store-sales | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.285714 | 0.285714 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.830769 | 0.771428 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | 0.000219 | 15.227600 | 913.200000 | 1.000000 | 0.000000 | 0.017078 |
| rossmann-store-sales | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.480000 | 0.300000 | 0.364569 | 0.400000 | 1.000000 | 0.400000 | 0.682284 | 0.382284 | 0.004225 | 66.487763 | 2484.800000 | `null` | 13.000000 | 0.185053 |
| rossmann-store-sales | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.465714 | 0.375000 | 0.413919 | 0.200000 | 1.000000 | 0.200000 | 0.706960 | 0.306959 | 0.001307 | 85.333400 | 18920.600000 | 5.600000 | 6.800000 | 0.148059 |
| rossmann-store-sales | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.742857 | 0.650000 | 0.693334 | 1.000000 | 1.000000 | 1.000000 | 0.846666 | 0.846666 | 0.000711 | 91.763000 | 19469.400000 | 5.000000 | 5.200000 | 0.148118 |
| rossmann-store-sales | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.090909 | 0.125000 | 0.105263 | 0.000000 | 1.000000 | 0.000000 | 0.552631 | 0.052631 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.677381 | 0.575000 | 0.620238 | 0.800000 | 1.000000 | 0.800000 | 0.810119 | 0.710119 | 0.000455 | 41.398200 | 2475.400000 | 1.000000 | 0.000000 | 0.048336 |
| rossmann-store-sales | tc3_fault_injected | claude_code | 5 | `true` | 1.000000 | 0.568182 | 0.457143 | 0.506103 | 1.000000 | 1.000000 | 1.000000 | 0.753051 | 0.753051 | 0.001118 | 69.447663 | 3158.400000 | `null` | 11.600000 | 0.203350 |
| rossmann-store-sales | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 0.567017 | 0.471428 | 0.514211 | 1.000000 | 1.000000 | 1.000000 | 0.757105 | 0.757105 | 0.000512 | 72.378600 | 13817.000000 | 4.600000 | 5.400000 | 0.120443 |
| rossmann-store-sales | tc3_fault_injected | proposed_agent | 5 | `true` | 0.800000 | 0.636111 | 0.400000 | 0.490909 | 1.000000 | 0.600000 | 0.733334 | 0.545454 | 0.612121 | 0.008548 | 86.112000 | 13993.400000 | 4.000000 | 3.200000 | 0.123119 |
| rossmann-store-sales | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.333333 | 0.285714 | 0.307692 | 1.000000 | 0.250000 | 0.400000 | 0.278846 | 0.353846 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 0.731469 | 0.642857 | 0.683259 | 1.000000 | 1.000000 | 1.000000 | 0.841629 | 0.841629 | 0.002715 | 46.909800 | 3075.400000 | 1.000000 | 0.000000 | 0.049526 |
| rossmann-store-sales | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 0.650000 | 0.457143 | 0.534732 | 0.950000 | 1.000000 | 0.971429 | 0.767366 | 0.753080 | 0.001265 | 159.064944 | 2866.800000 | `null` | 17.600000 | 0.352719 |
| rossmann-store-sales | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 0.619048 | 0.542857 | 0.578022 | 0.850000 | 1.000000 | 0.914286 | 0.789011 | 0.746154 | 0.001396 | 78.910400 | 16276.600000 | 4.600000 | 5.000000 | 0.133688 |
| rossmann-store-sales | tc4_mixed_history | proposed_agent | 5 | `true` | 0.200000 | 0.570000 | 0.342857 | 0.427273 | 0.600000 | 0.266667 | 0.360000 | 0.346969 | 0.393636 | 0.025308 | 139.771000 | 24720.400000 | 4.600000 | 4.000000 | 0.197055 |
| rossmann-store-sales | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.100000 | 0.142857 | 0.117647 | 0.000000 | 0.000000 | 0.000000 | 0.058824 | 0.058824 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 0.719048 | 0.657143 | 0.685715 | 1.000000 | 1.000000 | 1.000000 | 0.842857 | 0.842857 | 0.000925 | 41.246800 | 2574.200000 | 1.000000 | 0.000000 | 0.042027 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 1.000000 | 0.602522 | 0.478571 | 0.527592 | 0.837500 | 1.000000 | 0.842857 | 0.763796 | 0.685224 | 0.001660 | 111.854724 | 2965.050000 | `null` | 14.250000 | 0.262255 |
| generic_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.583275 | 0.515178 | 0.545586 | 0.762500 | 1.000000 | 0.778571 | 0.772793 | 0.662078 | 0.000869 | 76.788050 | 15714.950000 | 4.900000 | 5.800000 | 0.131444 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | 0.000000 | 3000.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 0.750000 | 0.673751 | 0.505357 | 0.573289 | 0.900000 | 0.716667 | 0.773334 | 0.644977 | 0.673311 | 0.008785 | 100.142650 | 19416.350000 | 4.700000 | 4.300000 | 0.155400 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.202489 | 0.209821 | 0.204079 | 0.500000 | 0.562500 | 0.350000 | 0.383290 | 0.277039 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 0.739667 | 0.661607 | 0.697303 | 0.950000 | 1.000000 | 0.950000 | 0.848651 | 0.823651 | 0.001079 | 36.195600 | 2259.550000 | 1.000000 | 0.000000 | 0.039242 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task rossmann-store-sales --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/rossmann-store-sales-all.md
```
