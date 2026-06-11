# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `allstate-claims-severity`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.952381`
- Mean Add Precision: `0.657937`
- Mean Add Recall: `0.660318`
- Mean Add F1: `0.619002`
- Mean Remove Precision: `0.652381`
- Mean Remove Recall: `0.857143`
- Mean Remove F1: `0.622222`
- Mean Task Completion Score: `0.738072`
- Mean Strict Task Completion Score: `0.620612`
- Mean Task Completion Variance: `0.002611`
- Mean Runtime (s): `121.178320`
- Mean Total Tokens: `4623.300000`
- Mean API Calls: `2.100000`
- Mean Tool Calls: `2.730000`
- Mean Cost (USD): `0.076929`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| allstate-claims-severity | MAE | insurance | regression | single_table | medium (188318) | high (131) | low (3) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| allstate-claims-severity | 21 | 6 | 0.952381 | 4.047619 | 0.657937 | 0.660318 | 0.619002 | 0.652381 | 0.857143 | 0.622222 | 0.738072 | 0.620612 | 0.002611 | 121.178320 | 4623.300000 | 2.100000 | 2.730000 | 0.076929 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| allstate-claims-severity | tc1_from_scratch | claude_code | try1 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 121.907467 | 5773 | `null` | 11 | 0.265451 |
| allstate-claims-severity | tc1_from_scratch | claude_code | try2 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 86.186204 | 4338 | `null` | 7 | 0.212058 |
| allstate-claims-severity | tc1_from_scratch | claude_code | try3 | 0.500000 | 0.666667 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 124.674825 | 6441 | `null` | 9 | 0.262337 |
| allstate-claims-severity | tc1_from_scratch | claude_code | try4 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 110.167166 | 5437 | `null` | 7 | 0.244802 |
| allstate-claims-severity | tc1_from_scratch | claude_code | try5 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 133.834440 | 6822 | `null` | 10 | 0.284813 |
| allstate-claims-severity | tc1_from_scratch | generic_agent | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 49.238000 | 7798 | 5 | 4 | 0.115940 |
| allstate-claims-severity | tc1_from_scratch | generic_agent | try2 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 34.246000 | 5715 | 4 | 3 | 0.056782 |
| allstate-claims-severity | tc1_from_scratch | generic_agent | try3 | 0.750000 | 1.000000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 60.575000 | 10228 | 4 | 4 | 0.090591 |
| allstate-claims-severity | tc1_from_scratch | generic_agent | try4 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 38.019000 | 6376 | 4 | 4 | 0.060164 |
| allstate-claims-severity | tc1_from_scratch | generic_agent | try5 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 34.083000 | 7239 | 3 | 3 | 0.057692 |
| allstate-claims-severity | tc1_from_scratch | human | human_tc1_sean_kraemer_v2_simple_baseline | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 1800 | `null` | `null` | `null` | `null` |
| allstate-claims-severity | tc1_from_scratch | proposed_agent | try1 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 46.050000 | 4786 | 3 | 2 | 0.153654 |
| allstate-claims-severity | tc1_from_scratch | proposed_agent | try2 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 32.908000 | 4331 | 3 | 2 | 0.057473 |
| allstate-claims-severity | tc1_from_scratch | proposed_agent | try3 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 33.126000 | 4078 | 3 | 2 | 0.056834 |
| allstate-claims-severity | tc1_from_scratch | proposed_agent | try4 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 36.370000 | 4214 | 3 | 2 | 0.058358 |
| allstate-claims-severity | tc1_from_scratch | proposed_agent | try5 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 42.506000 | 4944 | 3 | 2 | 0.063764 |
| allstate-claims-severity | tc1_from_scratch | rule_based | try1 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| allstate-claims-severity | tc1_from_scratch | single_llm | try1 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 6.290000 | 335 | 1 | 0 | 0.102131 |
| allstate-claims-severity | tc1_from_scratch | single_llm | try2 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 6.787000 | 315 | 1 | 0 | 0.012635 |
| allstate-claims-severity | tc1_from_scratch | single_llm | try3 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 5.491000 | 301 | 1 | 0 | 0.012425 |
| allstate-claims-severity | tc1_from_scratch | single_llm | try4 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 7.876000 | 336 | 1 | 0 | 0.012950 |
| allstate-claims-severity | tc1_from_scratch | single_llm | try5 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 8.758000 | 319 | 1 | 0 | 0.012695 |
| allstate-claims-severity | tc2_partial_good | claude_code | try1 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 74.463464 | 3409 | `null` | 8 | 0.205738 |
| allstate-claims-severity | tc2_partial_good | claude_code | try2 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 74.060551 | 3525 | `null` | 8 | 0.203784 |
| allstate-claims-severity | tc2_partial_good | claude_code | try3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 88.926829 | 3416 | `null` | 7 | 0.192611 |
| allstate-claims-severity | tc2_partial_good | claude_code | try4 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 65.421961 | 3005 | `null` | 6 | 0.183861 |
| allstate-claims-severity | tc2_partial_good | claude_code | try5 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 57.887171 | 3096 | `null` | 6 | 0.176743 |
| allstate-claims-severity | tc2_partial_good | generic_agent | try1 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 42.345000 | 7777 | 4 | 5 | 0.069677 |
| allstate-claims-severity | tc2_partial_good | generic_agent | try2 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 33.711000 | 7658 | 5 | 5 | 0.071857 |
| allstate-claims-severity | tc2_partial_good | generic_agent | try3 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 35.677000 | 6461 | 4 | 3 | 0.062432 |
| allstate-claims-severity | tc2_partial_good | generic_agent | try4 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 42.069000 | 6871 | 4 | 3 | 0.067184 |
| allstate-claims-severity | tc2_partial_good | generic_agent | try5 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 32.173000 | 6122 | 4 | 4 | 0.060450 |
| allstate-claims-severity | tc2_partial_good | proposed_agent | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 56.664000 | 6291 | 3 | 2 | 0.073133 |
| allstate-claims-severity | tc2_partial_good | proposed_agent | try2 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 1.000000 | 0.000000 | 1.000000 | 0.500000 | `true` | 46.345000 | 6067 | 3 | 2 | 0.069857 |
| allstate-claims-severity | tc2_partial_good | proposed_agent | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 55.445000 | 5765 | 3 | 2 | 0.072627 |
| allstate-claims-severity | tc2_partial_good | proposed_agent | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 60.126000 | 5566 | 3 | 2 | 0.068838 |
| allstate-claims-severity | tc2_partial_good | proposed_agent | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 47.322000 | 5583 | 3 | 2 | 0.068265 |
| allstate-claims-severity | tc2_partial_good | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| allstate-claims-severity | tc2_partial_good | single_llm | try1 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 8.179000 | 449 | 1 | 0 | 0.013930 |
| allstate-claims-severity | tc2_partial_good | single_llm | try2 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 6.765000 | 337 | 1 | 0 | 0.013006 |
| allstate-claims-severity | tc2_partial_good | single_llm | try3 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 9.322000 | 447 | 1 | 0 | 0.014656 |
| allstate-claims-severity | tc2_partial_good | single_llm | try4 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 9.142000 | 456 | 1 | 0 | 0.014791 |
| allstate-claims-severity | tc2_partial_good | single_llm | try5 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 7.473000 | 391 | 1 | 0 | 0.013816 |
| allstate-claims-severity | tc3_fault_injected | claude_code | try1 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 73.978025 | 3509 | `null` | 7 | 0.194095 |
| allstate-claims-severity | tc3_fault_injected | claude_code | try2 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 75.596901 | 3397 | `null` | 9 | 0.215568 |
| allstate-claims-severity | tc3_fault_injected | claude_code | try3 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 108.577700 | 5273 | `null` | 8 | 0.242166 |
| allstate-claims-severity | tc3_fault_injected | claude_code | try4 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 71.119794 | 2914 | `null` | 5 | 0.179624 |
| allstate-claims-severity | tc3_fault_injected | claude_code | try5 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 89.219115 | 4387 | `null` | 8 | 0.239193 |
| allstate-claims-severity | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 40.614000 | 8117 | 4 | 4 | 0.069136 |
| allstate-claims-severity | tc3_fault_injected | generic_agent | try2 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 45.863000 | 9178 | 5 | 5 | 0.081015 |
| allstate-claims-severity | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 45.992000 | 8255 | 5 | 4 | 0.081025 |
| allstate-claims-severity | tc3_fault_injected | generic_agent | try4 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 48.126000 | 10632 | 6 | 6 | 0.093906 |
| allstate-claims-severity | tc3_fault_injected | generic_agent | try5 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 37.587000 | 7352 | 4 | 4 | 0.066413 |
| allstate-claims-severity | tc3_fault_injected | proposed_agent | try1 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 52.576000 | 6308 | 3 | 2 | 0.074840 |
| allstate-claims-severity | tc3_fault_injected | proposed_agent | try2 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 47.532000 | 5990 | 3 | 2 | 0.069074 |
| allstate-claims-severity | tc3_fault_injected | proposed_agent | try3 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 54.643000 | 6009 | 3 | 2 | 0.075243 |
| allstate-claims-severity | tc3_fault_injected | proposed_agent | try4 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 57.380000 | 6235 | 3 | 2 | 0.076533 |
| allstate-claims-severity | tc3_fault_injected | proposed_agent | try5 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 55.346000 | 6073 | 3 | 2 | 0.075111 |
| allstate-claims-severity | tc3_fault_injected | rule_based | try1 | 1.000000 | 0.333333 | 0.500000 | 0.000000 | 0.000000 | 0.000000 | 0.250000 | 0.250000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| allstate-claims-severity | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 18.668000 | 1036 | 1 | 0 | 0.022711 |
| allstate-claims-severity | tc3_fault_injected | single_llm | try2 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 19.282000 | 1080 | 1 | 0 | 0.024158 |
| allstate-claims-severity | tc3_fault_injected | single_llm | try3 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 7.898000 | 377 | 1 | 0 | 0.013613 |
| allstate-claims-severity | tc3_fault_injected | single_llm | try4 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 7.051000 | 344 | 1 | 0 | 0.013118 |
| allstate-claims-severity | tc3_fault_injected | single_llm | try5 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | `true` | 19.604000 | 1030 | 1 | 0 | 0.023408 |
| allstate-claims-severity | tc4_mixed_history | claude_code | try1 | 0.000000 | 0.000000 | 0.000000 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 0.333334 | `true` | 54.296755 | 3290 | `null` | 7 | 0.181889 |
| allstate-claims-severity | tc4_mixed_history | claude_code | try2 | 0.000000 | 0.000000 | 0.000000 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 0.333334 | `true` | 69.449238 | 3843 | `null` | 7 | 0.203152 |
| allstate-claims-severity | tc4_mixed_history | claude_code | try3 | 0.000000 | 0.000000 | 0.000000 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 0.333334 | `true` | 51.606741 | 2923 | `null` | 7 | 0.175178 |
| allstate-claims-severity | tc4_mixed_history | claude_code | try4 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 1.000000 | 0.666667 | 0.833333 | 0.666667 | `true` | 58.947948 | 2916 | `null` | 8 | 0.193173 |
| allstate-claims-severity | tc4_mixed_history | claude_code | try5 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 1.000000 | 0.666667 | 0.833333 | 0.666667 | `true` | 61.003319 | 3521 | `null` | 8 | 0.195081 |
| allstate-claims-severity | tc4_mixed_history | generic_agent | try1 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 1.000000 | 0.666667 | 0.833333 | 0.666667 | `true` | 40.859000 | 8245 | 4 | 4 | 0.072930 |
| allstate-claims-severity | tc4_mixed_history | generic_agent | try2 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 1.000000 | 0.666667 | 0.833333 | 0.666667 | `true` | 28.891000 | 5213 | 3 | 2 | 0.048495 |
| allstate-claims-severity | tc4_mixed_history | generic_agent | try3 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 1.000000 | 0.666667 | 0.833333 | 0.666667 | `true` | 39.342000 | 7901 | 5 | 4 | 0.077923 |
| allstate-claims-severity | tc4_mixed_history | generic_agent | try4 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 1.000000 | 0.666667 | 0.833333 | 0.666667 | `true` | 38.610000 | 7301 | 4 | 3 | 0.070016 |
| allstate-claims-severity | tc4_mixed_history | generic_agent | try5 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 1.000000 | 0.666667 | 0.833333 | 0.666667 | `true` | 31.742000 | 4489 | 3 | 2 | 0.049002 |
| allstate-claims-severity | tc4_mixed_history | proposed_agent | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 62.060000 | 9965 | 4 | 3 | 0.100373 |
| allstate-claims-severity | tc4_mixed_history | proposed_agent | try2 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 1.000000 | 0.666667 | 1.000000 | 0.833333 | `true` | 70.031000 | 10451 | 4 | 3 | 0.105779 |
| allstate-claims-severity | tc4_mixed_history | proposed_agent | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 68.872000 | 9643 | 4 | 3 | 0.101189 |
| allstate-claims-severity | tc4_mixed_history | proposed_agent | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 59.495000 | 6474 | 3 | 2 | 0.079375 |
| allstate-claims-severity | tc4_mixed_history | proposed_agent | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 67.958000 | 9297 | 4 | 3 | 0.098422 |
| allstate-claims-severity | tc4_mixed_history | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 0.333334 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| allstate-claims-severity | tc4_mixed_history | single_llm | try1 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 1.000000 | 0.666667 | 0.833333 | 0.666667 | `true` | 19.676000 | 1164 | 1 | 0 | 0.024607 |
| allstate-claims-severity | tc4_mixed_history | single_llm | try2 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 1.000000 | 0.666667 | 0.833333 | 0.666667 | `true` | 8.473000 | 459 | 1 | 0 | 0.014851 |
| allstate-claims-severity | tc4_mixed_history | single_llm | try3 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 1.000000 | 0.666667 | 0.833333 | 0.666667 | `true` | 19.182000 | 1052 | 1 | 0 | 0.023746 |
| allstate-claims-severity | tc4_mixed_history | single_llm | try4 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 1.000000 | 0.666667 | 0.833333 | 0.666667 | `true` | 7.518000 | 403 | 1 | 0 | 0.014011 |
| allstate-claims-severity | tc4_mixed_history | single_llm | try5 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 1.000000 | 0.666667 | 0.833333 | 0.666667 | `true` | 16.446000 | 1000 | 1 | 0 | 0.022966 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| allstate-claims-severity | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.633334 | 0.666667 | 0.647619 | 1.000000 | 1.000000 | 1.000000 | 0.823809 | 0.823809 | 0.000363 | 115.354021 | 5762.200000 | `null` | 8.800000 | 0.253892 |
| allstate-claims-severity | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.750000 | 0.800000 | 0.771429 | 1.000000 | 1.000000 | 1.000000 | 0.885714 | 0.885714 | 0.004626 | 43.232200 | 7471.200000 | 4.000000 | 3.600000 | 0.076234 |
| allstate-claims-severity | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | 0.000000 | 1800 | `null` | `null` | `null` | `null` |
| allstate-claims-severity | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | 0.000000 | 38.192000 | 4470.600000 | 3.000000 | 2.000000 | 0.078017 |
| allstate-claims-severity | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.500000 | 0.333333 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| allstate-claims-severity | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.666667 | 0.666667 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | 0.000000 | 7.040400 | 321.200000 | 1.000000 | 0.000000 | 0.030567 |
| allstate-claims-severity | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.400000 | 0.800000 | 0.533334 | 0.000000 | 1.000000 | 0.000000 | 0.766666 | 0.266667 | 0.017778 | 72.151995 | 3290.200000 | `null` | 7.000000 | 0.192547 |
| allstate-claims-severity | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | 0.000000 | 37.195000 | 6977.800000 | 4.200000 | 4.000000 | 0.066320 |
| allstate-claims-severity | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 1.000000 | 0.800000 | 1.000000 | 0.900000 | 0.000000 | 53.180400 | 5854.400000 | 3.000000 | 2.000000 | 0.070544 |
| allstate-claims-severity | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| allstate-claims-severity | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.500000 | 1.000000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | 0.000000 | 8.176200 | 416.000000 | 1.000000 | 0.000000 | 0.014040 |
| allstate-claims-severity | tc3_fault_injected | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.533333 | 0.680000 | 1.000000 | 0.500000 | 0.666667 | 0.590000 | 0.673334 | 0.005400 | 83.698307 | 3896.000000 | `null` | 7.400000 | 0.214129 |
| allstate-claims-severity | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | 0.000000 | 43.636400 | 8706.800000 | 4.800000 | 4.600000 | 0.078299 |
| allstate-claims-severity | tc3_fault_injected | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | 0.000000 | 53.495400 | 6123.000000 | 3.000000 | 2.000000 | 0.074160 |
| allstate-claims-severity | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 1.000000 | 0.333333 | 0.500000 | 0.000000 | 0.000000 | 0.000000 | 0.250000 | 0.250000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| allstate-claims-severity | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 0.500000 | 0.666667 | 0.650000 | 0.733334 | 0.000000 | 14.500600 | 773.400000 | 1.000000 | 0.000000 | 0.019402 |
| allstate-claims-severity | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 0.200000 | 0.400000 | 0.266667 | 0.500000 | 1.000000 | 0.666667 | 0.633333 | 0.466667 | 0.026667 | 59.060800 | 3298.600000 | `null` | 7.400000 | 0.189694 |
| allstate-claims-severity | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 1.000000 | 0.666667 | 0.833333 | 0.666667 | 0.000000 | 35.888800 | 6629.800000 | 3.800000 | 3.000000 | 0.063673 |
| allstate-claims-severity | tc4_mixed_history | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 1.000000 | 0.933333 | 1.000000 | 0.966667 | 0.000000 | 65.683200 | 9166.000000 | 3.800000 | 2.800000 | 0.097028 |
| allstate-claims-severity | tc4_mixed_history | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 0.333334 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| allstate-claims-severity | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 0.500000 | 1.000000 | 0.666667 | 0.500000 | 1.000000 | 0.666667 | 0.833333 | 0.666667 | 0.000000 | 14.259000 | 815.600000 | 1.000000 | 0.000000 | 0.020036 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 1.000000 | 0.558334 | 0.600000 | 0.531905 | 0.625000 | 0.875000 | 0.583333 | 0.703452 | 0.557619 | 0.012552 | 82.566281 | 4061.750000 | `null` | 7.650000 | 0.212566 |
| generic_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.687500 | 0.866667 | 0.726191 | 0.625000 | 0.875000 | 0.583333 | 0.800595 | 0.654762 | 0.001156 | 39.988100 | 7446.400000 | 4.200000 | 3.800000 | 0.071132 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | 0.000000 | 1800.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.916667 | 0.833333 | 0.866667 | 0.925000 | 0.875000 | 0.850000 | 0.870833 | 0.858334 | 0.000000 | 52.637750 | 6403.500000 | 3.200000 | 2.200000 | 0.079937 |
| rule_based | 4 | 0.750000 | 1.000000 | 0.750000 | 0.375000 | 0.166666 | 0.225000 | 0.375000 | 0.750000 | 0.416667 | 0.487500 | 0.320833 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 0.666667 | 0.833333 | 0.700000 | 0.625000 | 0.875000 | 0.583333 | 0.787500 | 0.641667 | 0.000000 | 10.994050 | 581.550000 | 1.000000 | 0.000000 | 0.021011 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task allstate-claims-severity --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/allstate-claims-severity-all.md
```
