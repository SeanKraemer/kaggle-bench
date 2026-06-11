# Benchmark Aggregate Report

## Configuration

- Stage scope: `primary`
- Success threshold: `0.5`
- Tasks included: `rossmann-store-sales`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.904762`
- Mean Add Precision: `0.512032`
- Mean Add Recall: `0.441111`
- Mean Add F1: `0.469812`
- Mean Remove Precision: `0.800000`
- Mean Remove Recall: `0.862698`
- Mean Remove F1: `0.751383`
- Mean Task Completion Score: `0.666255`
- Mean Strict Task Completion Score: `0.610598`
- Mean Task Completion Variance: `0.002883`
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
| rossmann-store-sales | 21 | 6 | 0.904762 | 4.047619 | 0.512032 | 0.441111 | 0.469812 | 0.800000 | 0.862698 | 0.751383 | 0.666255 | 0.610598 | 0.002883 | 204.758290 | 10088.975000 | 2.650000 | 4.870000 | 0.117668 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rossmann-store-sales | tc1_from_scratch | claude_code | try1 | 0.700000 | 0.583333 | 0.636364 | 1.000000 | 1.000000 | 1.000000 | 0.818182 | 0.818182 | `true` | 191.171621 | 3670 | `null` | 13 | 0.389118 |
| rossmann-store-sales | tc1_from_scratch | claude_code | try2 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 87.752521 | 2744 | `null` | 10 | 0.222440 |
| rossmann-store-sales | tc1_from_scratch | claude_code | try3 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 281.772794 | 3983 | `null` | 29 | 0.496720 |
| rossmann-store-sales | tc1_from_scratch | claude_code | try4 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 62.054146 | 2935 | `null` | 7 | 0.186640 |
| rossmann-store-sales | tc1_from_scratch | claude_code | try5 | 0.615385 | 0.666667 | 0.640000 | 1.000000 | 1.000000 | 1.000000 | 0.820000 | 0.820000 | `true` | 139.341543 | 3419 | `null` | 15 | 0.244571 |
| rossmann-store-sales | tc1_from_scratch | generic_agent | try1 | 0.583333 | 0.583333 | 0.583333 | 1.000000 | 1.000000 | 1.000000 | 0.791667 | 0.791667 | `true` | 93.650000 | 16143 | 5 | 6 | 0.171023 |
| rossmann-store-sales | tc1_from_scratch | generic_agent | try2 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 62.613000 | 15718 | 5 | 6 | 0.123995 |
| rossmann-store-sales | tc1_from_scratch | generic_agent | try3 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 56.254000 | 9556 | 4 | 5 | 0.087173 |
| rossmann-store-sales | tc1_from_scratch | generic_agent | try4 | 0.583333 | 0.583333 | 0.583333 | 1.000000 | 1.000000 | 1.000000 | 0.791667 | 0.791667 | `true` | 69.586000 | 12326 | 5 | 6 | 0.112990 |
| rossmann-store-sales | tc1_from_scratch | generic_agent | try5 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 70.546000 | 15485 | 5 | 7 | 0.122745 |
| rossmann-store-sales | tc1_from_scratch | human | human_tc1_sean_kraemer_v4_manual_rebuild | 1.000000 | 0.583333 | 0.736842 | 1.000000 | 1.000000 | 1.000000 | 0.868421 | 0.868421 | `true` | 3000 | `null` | `null` | `null` | `null` |
| rossmann-store-sales | tc1_from_scratch | proposed_agent | try1 | 0.700000 | 0.583333 | 0.636364 | 1.000000 | 1.000000 | 1.000000 | 0.818182 | 0.818182 | `true` | 70.258000 | 16599 | 5 | 4 | 0.159278 |
| rossmann-store-sales | tc1_from_scratch | proposed_agent | try2 | 0.727273 | 0.666667 | 0.695652 | 1.000000 | 1.000000 | 1.000000 | 0.847826 | 0.847826 | `true` | 93.494000 | 20945 | 5 | 5 | 0.159983 |
| rossmann-store-sales | tc1_from_scratch | proposed_agent | try3 | 0.818182 | 0.750000 | 0.782609 | 1.000000 | 1.000000 | 1.000000 | 0.891304 | 0.891304 | `true` | 64.681000 | 14406 | 5 | 4 | 0.109504 |
| rossmann-store-sales | tc1_from_scratch | proposed_agent | try4 | 0.700000 | 0.583333 | 0.636364 | 1.000000 | 1.000000 | 1.000000 | 0.818182 | 0.818182 | `true` | 84.809000 | 18804 | 5 | 5 | 0.145058 |
| rossmann-store-sales | tc1_from_scratch | proposed_agent | try5 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 101.381000 | 26657 | 6 | 6 | 0.192726 |
| rossmann-store-sales | tc1_from_scratch | rule_based | try1 | 0.230769 | 0.250000 | 0.240000 | 1.000000 | 1.000000 | 1.000000 | 0.620000 | 0.620000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc1_from_scratch | single_llm | try1 | 0.750000 | 0.750000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 15.203000 | 974 | 1 | 0 | 0.017523 |
| rossmann-store-sales | tc1_from_scratch | single_llm | try2 | 0.833333 | 0.833333 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 16.182000 | 875 | 1 | 0 | 0.016621 |
| rossmann-store-sales | tc1_from_scratch | single_llm | try3 | 0.833333 | 0.833333 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 15.687000 | 917 | 1 | 0 | 0.017251 |
| rossmann-store-sales | tc1_from_scratch | single_llm | try4 | 0.833333 | 0.833333 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 14.676000 | 917 | 1 | 0 | 0.017251 |
| rossmann-store-sales | tc1_from_scratch | single_llm | try5 | 0.833333 | 0.833333 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 14.390000 | 883 | 1 | 0 | 0.016741 |
| rossmann-store-sales | tc2_partial_good | claude_code | try1 | 0.400000 | 0.333333 | 0.363636 | 0.000000 | 1.000000 | 0.000000 | 0.681818 | 0.181818 | `true` | 77.553572 | 2778 | `null` | 20 | 0.211240 |
| rossmann-store-sales | tc2_partial_good | claude_code | try2 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 54.174196 | 1914 | `null` | 7 | 0.149457 |
| rossmann-store-sales | tc2_partial_good | claude_code | try3 | 0.500000 | 0.333333 | 0.400000 | 0.000000 | 1.000000 | 0.000000 | 0.700000 | 0.200000 | `true` | 55.348012 | 2823 | `null` | 8 | 0.162127 |
| rossmann-store-sales | tc2_partial_good | claude_code | try4 | 0.500000 | 0.500000 | 0.500000 | 0.000000 | 1.000000 | 0.000000 | 0.750000 | 0.250000 | `true` | 77.822109 | 2282 | `null` | 20 | 0.194021 |
| rossmann-store-sales | tc2_partial_good | claude_code | try5 | 0.333333 | 0.166667 | 0.222222 | 1.000000 | 1.000000 | 1.000000 | 0.611111 | 0.611111 | `true` | 67.540925 | 2627 | `null` | 10 | 0.208420 |
| rossmann-store-sales | tc2_partial_good | generic_agent | try1 | 0.400000 | 0.333333 | 0.363636 | 0.000000 | 1.000000 | 0.000000 | 0.681818 | 0.181818 | `true` | 82.478000 | 18784 | 5 | 7 | 0.140580 |
| rossmann-store-sales | tc2_partial_good | generic_agent | try2 | 0.200000 | 0.166667 | 0.181818 | 0.000000 | 1.000000 | 0.000000 | 0.590909 | 0.090909 | `true` | 96.607000 | 23108 | 7 | 7 | 0.174169 |
| rossmann-store-sales | tc2_partial_good | generic_agent | try3 | 0.250000 | 0.166667 | 0.200000 | 1.000000 | 1.000000 | 1.000000 | 0.600000 | 0.600000 | `true` | 72.172000 | 11901 | 4 | 5 | 0.104278 |
| rossmann-store-sales | tc2_partial_good | generic_agent | try4 | 0.200000 | 0.166667 | 0.181818 | 0.000000 | 1.000000 | 0.000000 | 0.590909 | 0.090909 | `true` | 86.289000 | 17185 | 6 | 7 | 0.147106 |
| rossmann-store-sales | tc2_partial_good | generic_agent | try5 | 0.250000 | 0.166667 | 0.200000 | 0.000000 | 1.000000 | 0.000000 | 0.600000 | 0.100000 | `true` | 89.121000 | 23625 | 6 | 8 | 0.174165 |
| rossmann-store-sales | tc2_partial_good | proposed_agent | try1 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 74.019000 | 9940 | 3 | 2 | 0.098211 |
| rossmann-store-sales | tc2_partial_good | proposed_agent | try2 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 87.447000 | 20347 | 5 | 6 | 0.142098 |
| rossmann-store-sales | tc2_partial_good | proposed_agent | try3 | 0.833333 | 0.833333 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 89.077000 | 17815 | 5 | 4 | 0.135857 |
| rossmann-store-sales | tc2_partial_good | proposed_agent | try4 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 104.553000 | 23201 | 6 | 7 | 0.177135 |
| rossmann-store-sales | tc2_partial_good | proposed_agent | try5 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 103.719000 | 26044 | 6 | 7 | 0.187291 |
| rossmann-store-sales | tc2_partial_good | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc2_partial_good | single_llm | try1 | 0.600000 | 0.500000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 39.177000 | 2365 | 1 | 0 | 0.076991 |
| rossmann-store-sales | tc2_partial_good | single_llm | try2 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 46.125000 | 2755 | 1 | 0 | 0.044952 |
| rossmann-store-sales | tc2_partial_good | single_llm | try3 | 0.571429 | 0.666667 | 0.615385 | 0.000000 | 1.000000 | 0.000000 | 0.807692 | 0.307692 | `true` | 42.159000 | 2457 | 1 | 0 | 0.040482 |
| rossmann-store-sales | tc2_partial_good | single_llm | try4 | 0.600000 | 0.500000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 35.730000 | 2097 | 1 | 0 | 0.035082 |
| rossmann-store-sales | tc2_partial_good | single_llm | try5 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 43.800000 | 2703 | 1 | 0 | 0.044172 |
| rossmann-store-sales | tc3_fault_injected | claude_code | try1 | 0.600000 | 0.500000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 63.821234 | 3784 | `null` | 10 | 0.188621 |
| rossmann-store-sales | tc3_fault_injected | claude_code | try2 | 0.444444 | 0.333333 | 0.380952 | 1.000000 | 1.000000 | 1.000000 | 0.690476 | 0.690476 | `true` | 89.351452 | 3443 | `null` | 16 | 0.298387 |
| rossmann-store-sales | tc3_fault_injected | claude_code | try3 | 0.375000 | 0.250000 | 0.300000 | 1.000000 | 1.000000 | 1.000000 | 0.650000 | 0.650000 | `true` | 57.707521 | 3194 | `null` | 10 | 0.172513 |
| rossmann-store-sales | tc3_fault_injected | claude_code | try4 | 0.500000 | 0.416667 | 0.454545 | 1.000000 | 1.000000 | 1.000000 | 0.727272 | 0.727272 | `true` | 59.217999 | 3134 | `null` | 9 | 0.176102 |
| rossmann-store-sales | tc3_fault_injected | claude_code | try5 | 0.444444 | 0.333333 | 0.380952 | 1.000000 | 1.000000 | 1.000000 | 0.690476 | 0.690476 | `true` | 77.140110 | 2237 | `null` | 13 | 0.181127 |
| rossmann-store-sales | tc3_fault_injected | generic_agent | try1 | 0.545455 | 0.500000 | 0.521739 | 1.000000 | 1.000000 | 1.000000 | 0.760869 | 0.760869 | `true` | 68.326000 | 11746 | 4 | 4 | 0.107349 |
| rossmann-store-sales | tc3_fault_injected | generic_agent | try2 | 0.444444 | 0.333333 | 0.380952 | 1.000000 | 1.000000 | 1.000000 | 0.690476 | 0.690476 | `true` | 70.225000 | 17617 | 5 | 6 | 0.136140 |
| rossmann-store-sales | tc3_fault_injected | generic_agent | try3 | 0.444444 | 0.333333 | 0.380952 | 1.000000 | 1.000000 | 1.000000 | 0.690476 | 0.690476 | `true` | 81.304000 | 14375 | 5 | 7 | 0.128880 |
| rossmann-store-sales | tc3_fault_injected | generic_agent | try4 | 0.444444 | 0.333333 | 0.380952 | 1.000000 | 1.000000 | 1.000000 | 0.690476 | 0.690476 | `true` | 61.617000 | 10942 | 4 | 5 | 0.100886 |
| rossmann-store-sales | tc3_fault_injected | generic_agent | try5 | 0.500000 | 0.416667 | 0.454545 | 1.000000 | 1.000000 | 1.000000 | 0.727272 | 0.727272 | `true` | 80.421000 | 14405 | 5 | 5 | 0.128960 |
| rossmann-store-sales | tc3_fault_injected | proposed_agent | try1 | 0.555556 | 0.416667 | 0.476190 | 1.000000 | 0.500000 | 0.666667 | 0.488095 | 0.571429 | `false` | 94.082000 | 14143 | 4 | 3 | 0.127365 |
| rossmann-store-sales | tc3_fault_injected | proposed_agent | try2 | 0.625000 | 0.416667 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 71.526000 | 10267 | 3 | 2 | 0.100068 |
| rossmann-store-sales | tc3_fault_injected | proposed_agent | try3 | 0.666667 | 0.500000 | 0.571429 | 1.000000 | 0.500000 | 0.666667 | 0.535714 | 0.619048 | `true` | 92.376000 | 14477 | 4 | 3 | 0.130115 |
| rossmann-store-sales | tc3_fault_injected | proposed_agent | try4 | 0.666667 | 0.500000 | 0.571429 | 1.000000 | 0.500000 | 0.666667 | 0.535714 | 0.619048 | `true` | 80.398000 | 12941 | 4 | 3 | 0.115451 |
| rossmann-store-sales | tc3_fault_injected | proposed_agent | try5 | 0.666667 | 0.500000 | 0.571429 | 1.000000 | 0.500000 | 0.666667 | 0.535714 | 0.619048 | `true` | 92.178000 | 18139 | 5 | 5 | 0.142598 |
| rossmann-store-sales | tc3_fault_injected | rule_based | try1 | 0.272727 | 0.250000 | 0.260870 | 1.000000 | 0.250000 | 0.400000 | 0.255435 | 0.330435 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc3_fault_injected | single_llm | try1 | 0.750000 | 0.750000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 49.745000 | 3305 | 1 | 0 | 0.052188 |
| rossmann-store-sales | tc3_fault_injected | single_llm | try2 | 0.750000 | 0.750000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 42.737000 | 2809 | 1 | 0 | 0.045725 |
| rossmann-store-sales | tc3_fault_injected | single_llm | try3 | 0.600000 | 0.500000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 43.391000 | 2914 | 1 | 0 | 0.047300 |
| rossmann-store-sales | tc3_fault_injected | single_llm | try4 | 0.555556 | 0.416667 | 0.476190 | 1.000000 | 1.000000 | 1.000000 | 0.738095 | 0.738095 | `true` | 51.668000 | 3271 | 1 | 0 | 0.052655 |
| rossmann-store-sales | tc3_fault_injected | single_llm | try5 | 0.818182 | 0.750000 | 0.782609 | 1.000000 | 1.000000 | 1.000000 | 0.891304 | 0.891304 | `true` | 47.008000 | 3078 | 1 | 0 | 0.049760 |
| rossmann-store-sales | tc4_mixed_history | claude_code | try1 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 73.573852 | 3214 | `null` | 13 | 0.265804 |
| rossmann-store-sales | tc4_mixed_history | claude_code | try2 | 0.500000 | 0.400000 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 254.056336 | 2452 | `null` | 19 | 0.483433 |
| rossmann-store-sales | tc4_mixed_history | claude_code | try3 | 0.400000 | 0.400000 | 0.400000 | 0.750000 | 1.000000 | 0.857143 | 0.700000 | 0.628572 | `true` | 104.779697 | 3329 | `null` | 13 | 0.235377 |
| rossmann-store-sales | tc4_mixed_history | claude_code | try4 | 0.500000 | 0.400000 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 74.268010 | 3082 | `null` | 13 | 0.186947 |
| rossmann-store-sales | tc4_mixed_history | claude_code | try5 | 0.750000 | 0.600000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 288.646826 | 2257 | `null` | 30 | 0.592032 |
| rossmann-store-sales | tc4_mixed_history | generic_agent | try1 | 0.500000 | 0.400000 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 82.605000 | 19788 | 5 | 5 | 0.147721 |
| rossmann-store-sales | tc4_mixed_history | generic_agent | try2 | 0.500000 | 0.400000 | 0.444444 | 0.750000 | 1.000000 | 0.857143 | 0.722222 | 0.650794 | `true` | 61.506000 | 13435 | 4 | 3 | 0.109245 |
| rossmann-store-sales | tc4_mixed_history | generic_agent | try3 | 0.333333 | 0.400000 | 0.363636 | 0.750000 | 1.000000 | 0.857143 | 0.681818 | 0.610390 | `true` | 72.927000 | 13621 | 4 | 4 | 0.120768 |
| rossmann-store-sales | tc4_mixed_history | generic_agent | try4 | 0.600000 | 0.600000 | 0.600000 | 0.750000 | 1.000000 | 0.857143 | 0.800000 | 0.728571 | `true` | 79.332000 | 15791 | 5 | 6 | 0.132725 |
| rossmann-store-sales | tc4_mixed_history | generic_agent | try5 | 0.500000 | 0.400000 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 98.182000 | 18748 | 5 | 7 | 0.157980 |
| rossmann-store-sales | tc4_mixed_history | proposed_agent | try1 | 0.333333 | 0.200000 | 0.250000 | 1.000000 | 0.333333 | 0.500000 | 0.291666 | 0.375000 | `false` | 177.146000 | 32005 | 5 | 4 | 0.242964 |
| rossmann-store-sales | tc4_mixed_history | proposed_agent | try2 | 0.333333 | 0.200000 | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.125000 | 0.125000 | `false` | 110.033000 | 18127 | 4 | 3 | 0.156693 |
| rossmann-store-sales | tc4_mixed_history | proposed_agent | try3 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 0.666667 | 0.800000 | 0.583333 | 0.650000 | `true` | 143.497000 | 26236 | 5 | 6 | 0.206427 |
| rossmann-store-sales | tc4_mixed_history | proposed_agent | try4 | 0.500000 | 0.400000 | 0.444444 | 1.000000 | 0.333333 | 0.500000 | 0.388888 | 0.472222 | `false` | 122.529000 | 25340 | 5 | 4 | 0.184095 |
| rossmann-store-sales | tc4_mixed_history | proposed_agent | try5 | 0.333333 | 0.200000 | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.125000 | 0.125000 | `false` | 145.650000 | 21894 | 4 | 3 | 0.195096 |
| rossmann-store-sales | tc4_mixed_history | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc4_mixed_history | single_llm | try1 | 0.600000 | 0.600000 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 36.787000 | 2385 | 1 | 0 | 0.038004 |
| rossmann-store-sales | tc4_mixed_history | single_llm | try2 | 0.750000 | 0.600000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 48.569000 | 2883 | 1 | 0 | 0.046955 |
| rossmann-store-sales | tc4_mixed_history | single_llm | try3 | 0.500000 | 0.400000 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 36.123000 | 2261 | 1 | 0 | 0.037625 |
| rossmann-store-sales | tc4_mixed_history | single_llm | try4 | 0.500000 | 0.400000 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 40.644000 | 2574 | 1 | 0 | 0.042320 |
| rossmann-store-sales | tc4_mixed_history | single_llm | try5 | 0.600000 | 0.600000 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 44.111000 | 2768 | 1 | 0 | 0.045230 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rossmann-store-sales | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.663077 | 0.650000 | 0.655273 | 1.000000 | 1.000000 | 1.000000 | 0.827636 | 0.827636 | 0.000049 | 152.418525 | 3350.200000 | `null` | 14.800000 | 0.307898 |
| rossmann-store-sales | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.633333 | 0.633333 | 0.633333 | 1.000000 | 1.000000 | 1.000000 | 0.816667 | 0.816667 | 0.000417 | 70.529800 | 13845.600000 | 4.800000 | 6.000000 | 0.123585 |
| rossmann-store-sales | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 0.583333 | 0.736842 | 1.000000 | 1.000000 | 1.000000 | 0.868421 | 0.868421 | 0.000000 | 3000 | `null` | `null` | `null` | `null` |
| rossmann-store-sales | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.722424 | 0.650000 | 0.683531 | 1.000000 | 1.000000 | 1.000000 | 0.841765 | 0.841765 | 0.000735 | 82.924600 | 19482.200000 | 5.200000 | 4.800000 | 0.153310 |
| rossmann-store-sales | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.230769 | 0.250000 | 0.240000 | 1.000000 | 1.000000 | 1.000000 | 0.620000 | 0.620000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.816666 | 0.816666 | 0.816666 | 1.000000 | 1.000000 | 1.000000 | 0.908334 | 0.908334 | 0.000278 | 15.227600 | 913.200000 | 1.000000 | 0.000000 | 0.017078 |
| rossmann-store-sales | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.480000 | 0.400000 | 0.430505 | 0.400000 | 1.000000 | 0.400000 | 0.715252 | 0.415252 | 0.005469 | 66.487763 | 2484.800000 | `null` | 13.000000 | 0.185053 |
| rossmann-store-sales | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.260000 | 0.200000 | 0.225454 | 0.200000 | 1.000000 | 0.200000 | 0.612727 | 0.212727 | 0.001210 | 85.333400 | 18920.600000 | 5.600000 | 6.800000 | 0.148059 |
| rossmann-store-sales | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.700000 | 0.700000 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | 0.001111 | 91.763000 | 19469.400000 | 5.000000 | 5.200000 | 0.148118 |
| rossmann-store-sales | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.620953 | 0.600000 | 0.607926 | 0.800000 | 1.000000 | 0.800000 | 0.803963 | 0.703963 | 0.000738 | 41.398200 | 2475.400000 | 1.000000 | 0.000000 | 0.048336 |
| rossmann-store-sales | tc3_fault_injected | claude_code | 5 | `true` | 1.000000 | 0.472778 | 0.366667 | 0.412381 | 1.000000 | 1.000000 | 1.000000 | 0.706190 | 0.706190 | 0.001705 | 69.447663 | 3158.400000 | `null` | 11.600000 | 0.203350 |
| rossmann-store-sales | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 0.475757 | 0.383333 | 0.423828 | 1.000000 | 1.000000 | 1.000000 | 0.711914 | 0.711914 | 0.000802 | 72.378600 | 13817.000000 | 4.600000 | 5.400000 | 0.120443 |
| rossmann-store-sales | tc3_fault_injected | proposed_agent | 5 | `true` | 0.800000 | 0.636111 | 0.466667 | 0.538095 | 1.000000 | 0.600000 | 0.733334 | 0.569047 | 0.635715 | 0.008526 | 86.112000 | 13993.400000 | 4.000000 | 3.200000 | 0.123119 |
| rossmann-store-sales | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.272727 | 0.250000 | 0.260870 | 1.000000 | 0.250000 | 0.400000 | 0.255435 | 0.330435 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 0.694748 | 0.633333 | 0.660851 | 1.000000 | 1.000000 | 1.000000 | 0.830425 | 0.830425 | 0.003907 | 46.909800 | 3075.400000 | 1.000000 | 0.000000 | 0.049526 |
| rossmann-store-sales | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 0.563333 | 0.440000 | 0.491111 | 0.950000 | 1.000000 | 0.971429 | 0.745555 | 0.731270 | 0.002178 | 159.064944 | 2866.800000 | `null` | 17.600000 | 0.352719 |
| rossmann-store-sales | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 0.486667 | 0.440000 | 0.459394 | 0.850000 | 1.000000 | 0.914286 | 0.729697 | 0.686840 | 0.001481 | 78.910400 | 16276.600000 | 4.600000 | 5.000000 | 0.133688 |
| rossmann-store-sales | tc4_mixed_history | proposed_agent | 5 | `true` | 0.200000 | 0.433333 | 0.280000 | 0.338889 | 0.600000 | 0.266667 | 0.360000 | 0.302777 | 0.349444 | 0.029892 | 139.771000 | 24720.400000 | 4.600000 | 4.000000 | 0.197055 |
| rossmann-store-sales | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| rossmann-store-sales | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 0.590000 | 0.520000 | 0.551111 | 1.000000 | 1.000000 | 1.000000 | 0.775555 | 0.775555 | 0.002044 | 41.246800 | 2574.200000 | 1.000000 | 0.000000 | 0.042027 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 1.000000 | 0.544797 | 0.464167 | 0.497318 | 0.837500 | 1.000000 | 0.842857 | 0.748658 | 0.670087 | 0.002350 | 111.854724 | 2965.050000 | `null` | 14.250000 | 0.262255 |
| generic_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.463939 | 0.414166 | 0.435502 | 0.762500 | 1.000000 | 0.778571 | 0.717751 | 0.607037 | 0.000977 | 76.788050 | 15714.950000 | 4.900000 | 5.800000 | 0.131444 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.583333 | 0.736842 | 1.000000 | 1.000000 | 1.000000 | 0.868421 | 0.868421 | 0.000000 | 3000.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 0.750000 | 0.622967 | 0.524167 | 0.565129 | 0.900000 | 0.716667 | 0.773334 | 0.640897 | 0.669231 | 0.010066 | 100.142650 | 19416.350000 | 4.700000 | 4.300000 | 0.155400 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.125874 | 0.125000 | 0.125217 | 0.500000 | 0.562500 | 0.350000 | 0.343859 | 0.237609 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 0.680592 | 0.642500 | 0.659138 | 0.950000 | 1.000000 | 0.950000 | 0.829569 | 0.804569 | 0.001742 | 36.195600 | 2259.550000 | 1.000000 | 0.000000 | 0.039242 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task rossmann-store-sales --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/rossmann-store-sales-primary.md
```
