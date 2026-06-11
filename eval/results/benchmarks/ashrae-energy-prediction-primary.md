# Benchmark Aggregate Report

## Configuration

- Stage scope: `primary`
- Success threshold: `0.5`
- Tasks included: `ashrae-energy-prediction`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.857143`
- Mean Add Precision: `0.824452`
- Mean Add Recall: `0.792063`
- Mean Add F1: `0.796585`
- Mean Remove Precision: `0.838095`
- Mean Remove Recall: `0.795238`
- Mean Remove F1: `0.774603`
- Mean Task Completion Score: `0.795912`
- Mean Strict Task Completion Score: `0.785594`
- Mean Task Completion Variance: `0.004237`
- Mean Runtime (s): `192.679459`
- Mean Total Tokens: `8066.425000`
- Mean API Calls: `2.400000`
- Mean Tool Calls: `3.790000`
- Mean Cost (USD): `0.087468`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ashrae-energy-prediction | RMSLE | energy_forecasting_tabular | forecasting | multi_table_lookup | xlarge (41697600) | low (17) | medium (11) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ashrae-energy-prediction | 21 | 6 | 0.857143 | 4.047619 | 0.824452 | 0.792063 | 0.796585 | 0.838095 | 0.795238 | 0.774603 | 0.795912 | 0.785594 | 0.004237 | 192.679459 | 8066.425000 | 2.400000 | 3.790000 | 0.087468 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ashrae-energy-prediction | tc1_from_scratch | claude_code | try1 | 0.857143 | 1.000000 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 135.326165 | 5890 | `null` | 11 | 0.194443 |
| ashrae-energy-prediction | tc1_from_scratch | claude_code | try2 | 0.857143 | 1.000000 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 137.711177 | 6198 | `null` | 10 | 0.207845 |
| ashrae-energy-prediction | tc1_from_scratch | claude_code | try3 | 0.857143 | 1.000000 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 125.691681 | 5429 | `null` | 8 | 0.186802 |
| ashrae-energy-prediction | tc1_from_scratch | claude_code | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 157.478269 | 7887 | `null` | 12 | 0.226668 |
| ashrae-energy-prediction | tc1_from_scratch | claude_code | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 82.833055 | 4587 | `null` | 10 | 0.170221 |
| ashrae-energy-prediction | tc1_from_scratch | generic_agent | try1 | 0.857143 | 1.000000 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 89.959000 | 10328 | 4 | 5 | 0.099816 |
| ashrae-energy-prediction | tc1_from_scratch | generic_agent | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 125.123000 | 14083 | 4 | 5 | 0.099038 |
| ashrae-energy-prediction | tc1_from_scratch | generic_agent | try3 | 0.857143 | 1.000000 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 105.765000 | 14973 | 5 | 5 | 0.106004 |
| ashrae-energy-prediction | tc1_from_scratch | generic_agent | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 106.308000 | 14546 | 4 | 5 | 0.103488 |
| ashrae-energy-prediction | tc1_from_scratch | generic_agent | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 50.055000 | 8659 | 4 | 4 | 0.070830 |
| ashrae-energy-prediction | tc1_from_scratch | human | human_tc1_annotator_c_v1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 2700 | `null` | `null` | `null` | `null` |
| ashrae-energy-prediction | tc1_from_scratch | proposed_agent | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 143.868000 | 12075 | 4 | 4 | 0.161569 |
| ashrae-energy-prediction | tc1_from_scratch | proposed_agent | try2 | 0.857143 | 1.000000 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 50.016000 | 11602 | 4 | 4 | 0.087276 |
| ashrae-energy-prediction | tc1_from_scratch | proposed_agent | try3 | 0.857143 | 1.000000 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 44.355000 | 6539 | 3 | 2 | 0.066332 |
| ashrae-energy-prediction | tc1_from_scratch | proposed_agent | try4 | 0.750000 | 1.000000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 55.483000 | 9207 | 4 | 2 | 0.082060 |
| ashrae-energy-prediction | tc1_from_scratch | proposed_agent | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 62.875000 | 13474 | 4 | 5 | 0.103440 |
| ashrae-energy-prediction | tc1_from_scratch | rule_based | try1 | 0.111111 | 0.166667 | 0.133333 | 1.000000 | 1.000000 | 1.000000 | 0.566666 | 0.566666 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| ashrae-energy-prediction | tc1_from_scratch | single_llm | try1 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 10.909000 | 659 | 1 | 0 | 0.052252 |
| ashrae-energy-prediction | tc1_from_scratch | single_llm | try2 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 11.009000 | 663 | 1 | 0 | 0.052312 |
| ashrae-energy-prediction | tc1_from_scratch | single_llm | try3 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 12.586000 | 715 | 1 | 0 | 0.053093 |
| ashrae-energy-prediction | tc1_from_scratch | single_llm | try4 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 11.207000 | 648 | 1 | 0 | 0.052087 |
| ashrae-energy-prediction | tc1_from_scratch | single_llm | try5 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 10.792000 | 633 | 1 | 0 | 0.013026 |
| ashrae-energy-prediction | tc2_partial_good | claude_code | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 150.308036 | 4109 | `null` | 7 | 0.175117 |
| ashrae-energy-prediction | tc2_partial_good | claude_code | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 83.519645 | 4593 | `null` | 10 | 0.183268 |
| ashrae-energy-prediction | tc2_partial_good | claude_code | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 168.556260 | 4727 | `null` | 9 | 0.174697 |
| ashrae-energy-prediction | tc2_partial_good | claude_code | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 83.250646 | 4733 | `null` | 6 | 0.166056 |
| ashrae-energy-prediction | tc2_partial_good | claude_code | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 122.013081 | 4389 | `null` | 9 | 0.174709 |
| ashrae-energy-prediction | tc2_partial_good | generic_agent | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 85.900000 | 8726 | 4 | 5 | 0.071268 |
| ashrae-energy-prediction | tc2_partial_good | generic_agent | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 96.380000 | 11902 | 5 | 7 | 0.097970 |
| ashrae-energy-prediction | tc2_partial_good | generic_agent | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 48.310000 | 7470 | 4 | 6 | 0.062287 |
| ashrae-energy-prediction | tc2_partial_good | generic_agent | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 94.238000 | 10042 | 5 | 6 | 0.082848 |
| ashrae-energy-prediction | tc2_partial_good | generic_agent | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 41.162000 | 5789 | 3 | 3 | 0.050476 |
| ashrae-energy-prediction | tc2_partial_good | proposed_agent | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 55.563000 | 11092 | 4 | 4 | 0.090066 |
| ashrae-energy-prediction | tc2_partial_good | proposed_agent | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 44.242000 | 6151 | 3 | 2 | 0.061219 |
| ashrae-energy-prediction | tc2_partial_good | proposed_agent | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 45.640000 | 6122 | 3 | 2 | 0.065422 |
| ashrae-energy-prediction | tc2_partial_good | proposed_agent | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 60.969000 | 15376 | 6 | 7 | 0.123865 |
| ashrae-energy-prediction | tc2_partial_good | proposed_agent | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 55.356000 | 11139 | 4 | 4 | 0.090339 |
| ashrae-energy-prediction | tc2_partial_good | rule_based | try1 | 0.142857 | 0.333333 | 0.200000 | 0.000000 | 1.000000 | 0.000000 | 0.600000 | 0.100000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| ashrae-energy-prediction | tc2_partial_good | single_llm | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 28.533000 | 1582 | 1 | 0 | 0.026474 |
| ashrae-energy-prediction | tc2_partial_good | single_llm | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 32.802000 | 1904 | 1 | 0 | 0.031304 |
| ashrae-energy-prediction | tc2_partial_good | single_llm | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 27.762000 | 1686 | 1 | 0 | 0.028034 |
| ashrae-energy-prediction | tc2_partial_good | single_llm | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 12.345000 | 739 | 1 | 0 | 0.013829 |
| ashrae-energy-prediction | tc2_partial_good | single_llm | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 25.077000 | 1420 | 1 | 0 | 0.024894 |
| ashrae-energy-prediction | tc3_fault_injected | claude_code | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.857143 | 0.875000 | 0.928571 | `true` | 269.305576 | 9112 | `null` | 10 | 0.280779 |
| ashrae-energy-prediction | tc3_fault_injected | claude_code | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 104.559754 | 5121 | `null` | 10 | 0.189281 |
| ashrae-energy-prediction | tc3_fault_injected | claude_code | try3 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.500000 | 0.666667 | 0.583333 | 0.666667 | `true` | 159.454017 | 7382 | `null` | 10 | 0.242904 |
| ashrae-energy-prediction | tc3_fault_injected | claude_code | try4 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 0.500000 | 0.666667 | 0.704546 | 0.787879 | `true` | 261.226049 | 7587 | `null` | 11 | 0.243540 |
| ashrae-energy-prediction | tc3_fault_injected | claude_code | try5 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 0.500000 | 0.666667 | 0.704546 | 0.787879 | `true` | 288.296542 | 8733 | `null` | 11 | 0.258282 |
| ashrae-energy-prediction | tc3_fault_injected | generic_agent | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.857143 | 0.875000 | 0.928571 | `true` | 50.744000 | 9497 | 4 | 5 | 0.073744 |
| ashrae-energy-prediction | tc3_fault_injected | generic_agent | try2 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 0.500000 | 0.666667 | 0.704546 | 0.787879 | `true` | 101.238000 | 15271 | 5 | 6 | 0.110114 |
| ashrae-energy-prediction | tc3_fault_injected | generic_agent | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.857143 | 0.875000 | 0.928571 | `true` | 66.027000 | 10061 | 4 | 6 | 0.084372 |
| ashrae-energy-prediction | tc3_fault_injected | generic_agent | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.857143 | 0.875000 | 0.928571 | `true` | 105.152000 | 10472 | 4 | 6 | 0.088715 |
| ashrae-energy-prediction | tc3_fault_injected | generic_agent | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.857143 | 0.875000 | 0.928571 | `true` | 82.117000 | 11425 | 4 | 6 | 0.094755 |
| ashrae-energy-prediction | tc3_fault_injected | proposed_agent | try1 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.250000 | 0.400000 | 0.458334 | 0.533334 | `false` | 142.605000 | 12429 | 4 | 4 | 0.110073 |
| ashrae-energy-prediction | tc3_fault_injected | proposed_agent | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.250000 | 0.400000 | 0.458334 | 0.533334 | `false` | 84.254000 | 16950 | 5 | 4 | 0.127688 |
| ashrae-energy-prediction | tc3_fault_injected | proposed_agent | try3 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.250000 | 0.400000 | 0.458334 | 0.533334 | `false` | 74.329000 | 12250 | 4 | 4 | 0.105443 |
| ashrae-energy-prediction | tc3_fault_injected | proposed_agent | try4 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.250000 | 0.400000 | 0.458334 | 0.533334 | `false` | 86.017000 | 16455 | 5 | 4 | 0.128111 |
| ashrae-energy-prediction | tc3_fault_injected | proposed_agent | try5 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.250000 | 0.400000 | 0.458334 | 0.533334 | `false` | 79.009000 | 16355 | 5 | 5 | 0.125855 |
| ashrae-energy-prediction | tc3_fault_injected | rule_based | try1 | 0.142857 | 0.166667 | 0.153846 | 0.000000 | 0.000000 | 0.000000 | 0.076923 | 0.076923 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| ashrae-energy-prediction | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 0.500000 | 0.666667 | 0.704546 | 0.787879 | `true` | 51.783000 | 3105 | 1 | 0 | 0.049223 |
| ashrae-energy-prediction | tc3_fault_injected | single_llm | try2 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 0.500000 | 0.666667 | 0.704546 | 0.787879 | `true` | 38.234000 | 2086 | 1 | 0 | 0.033938 |
| ashrae-energy-prediction | tc3_fault_injected | single_llm | try3 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 0.500000 | 0.666667 | 0.704546 | 0.787879 | `true` | 32.835000 | 2026 | 1 | 0 | 0.033038 |
| ashrae-energy-prediction | tc3_fault_injected | single_llm | try4 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 0.500000 | 0.666667 | 0.704546 | 0.787879 | `true` | 40.926000 | 2403 | 1 | 0 | 0.038693 |
| ashrae-energy-prediction | tc3_fault_injected | single_llm | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.857143 | 0.875000 | 0.928571 | `true` | 47.069000 | 2843 | 1 | 0 | 0.046269 |
| ashrae-energy-prediction | tc4_mixed_history | claude_code | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 141.714317 | 4284 | `null` | 7 | 0.157427 |
| ashrae-energy-prediction | tc4_mixed_history | claude_code | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 108.211758 | 3811 | `null` | 7 | 0.157182 |
| ashrae-energy-prediction | tc4_mixed_history | claude_code | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 81.720913 | 4693 | `null` | 11 | 0.175347 |
| ashrae-energy-prediction | tc4_mixed_history | claude_code | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 100.758416 | 5015 | `null` | 9 | 0.202152 |
| ashrae-energy-prediction | tc4_mixed_history | claude_code | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 126.839835 | 5879 | `null` | 9 | 0.203863 |
| ashrae-energy-prediction | tc4_mixed_history | generic_agent | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 88.717000 | 10076 | 4 | 5 | 0.082549 |
| ashrae-energy-prediction | tc4_mixed_history | generic_agent | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 59.273000 | 10482 | 4 | 5 | 0.082360 |
| ashrae-energy-prediction | tc4_mixed_history | generic_agent | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 104.418000 | 14572 | 5 | 6 | 0.109800 |
| ashrae-energy-prediction | tc4_mixed_history | generic_agent | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 67.309000 | 14452 | 4 | 6 | 0.104822 |
| ashrae-energy-prediction | tc4_mixed_history | generic_agent | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 128.891000 | 19804 | 6 | 7 | 0.154263 |
| ashrae-energy-prediction | tc4_mixed_history | proposed_agent | try1 | 1.000000 | 0.666667 | 0.800000 | 0.000000 | 0.000000 | 0.000000 | 0.400000 | 0.400000 | `false` | 98.219000 | 18231 | 5 | 6 | 0.142055 |
| ashrae-energy-prediction | tc4_mixed_history | proposed_agent | try2 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 90.272000 | 13882 | 4 | 3 | 0.122604 |
| ashrae-energy-prediction | tc4_mixed_history | proposed_agent | try3 | 1.000000 | 0.666667 | 0.800000 | 0.000000 | 0.000000 | 0.000000 | 0.400000 | 0.400000 | `false` | 95.663000 | 18202 | 5 | 6 | 0.144076 |
| ashrae-energy-prediction | tc4_mixed_history | proposed_agent | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 115.195000 | 20056 | 5 | 5 | 0.154130 |
| ashrae-energy-prediction | tc4_mixed_history | proposed_agent | try5 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 81.184000 | 17148 | 5 | 6 | 0.132362 |
| ashrae-energy-prediction | tc4_mixed_history | rule_based | try1 | 0.166667 | 0.333333 | 0.222222 | 0.000000 | 0.000000 | 0.000000 | 0.111111 | 0.111111 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| ashrae-energy-prediction | tc4_mixed_history | single_llm | try1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 39.871000 | 2270 | 1 | 0 | 0.036674 |
| ashrae-energy-prediction | tc4_mixed_history | single_llm | try2 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 37.572000 | 2131 | 1 | 0 | 0.034589 |
| ashrae-energy-prediction | tc4_mixed_history | single_llm | try3 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 35.766000 | 2055 | 1 | 0 | 0.033449 |
| ashrae-energy-prediction | tc4_mixed_history | single_llm | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 36.820000 | 2068 | 1 | 0 | 0.033644 |
| ashrae-energy-prediction | tc4_mixed_history | single_llm | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 36.470000 | 2154 | 1 | 0 | 0.035942 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ashrae-energy-prediction | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.914286 | 1.000000 | 0.953846 | 1.000000 | 1.000000 | 1.000000 | 0.976923 | 0.976923 | 0.000355 | 127.808069 | 5998.200000 | `null` | 10.200000 | 0.197196 |
| ashrae-energy-prediction | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.942857 | 1.000000 | 0.969231 | 1.000000 | 1.000000 | 1.000000 | 0.984616 | 0.984616 | 0.000355 | 95.442000 | 12517.800000 | 4.200000 | 4.800000 | 0.095835 |
| ashrae-energy-prediction | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 2700 | `null` | `null` | `null` | `null` |
| ashrae-energy-prediction | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.892857 | 1.000000 | 0.940659 | 1.000000 | 1.000000 | 1.000000 | 0.970330 | 0.970330 | 0.000732 | 71.319400 | 10579.400000 | 3.800000 | 3.400000 | 0.100135 |
| ashrae-energy-prediction | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.111111 | 0.166667 | 0.133333 | 1.000000 | 1.000000 | 1.000000 | 0.566666 | 0.566666 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| ashrae-energy-prediction | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | 0.000000 | 11.300600 | 663.600000 | 1.000000 | 0.000000 | 0.044554 |
| ashrae-energy-prediction | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 121.529534 | 4510.200000 | `null` | 8.200000 | 0.174769 |
| ashrae-energy-prediction | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 73.198000 | 8785.800000 | 4.200000 | 5.400000 | 0.072970 |
| ashrae-energy-prediction | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 52.354000 | 9976.000000 | 4.000000 | 3.800000 | 0.086182 |
| ashrae-energy-prediction | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.142857 | 0.333333 | 0.200000 | 0.000000 | 1.000000 | 0.000000 | 0.600000 | 0.100000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| ashrae-energy-prediction | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 25.303800 | 1466.200000 | 1.000000 | 0.000000 | 0.024907 |
| ashrae-energy-prediction | tc3_fault_injected | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.733333 | 0.830303 | 1.000000 | 0.600000 | 0.742857 | 0.715152 | 0.786580 | 0.008640 | 216.568388 | 7587.000000 | `null` | 10.400000 | 0.242957 |
| ashrae-energy-prediction | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.966667 | 0.981818 | 1.000000 | 0.700000 | 0.819048 | 0.840909 | 0.900433 | 0.004649 | 81.055600 | 11345.200000 | 4.200000 | 5.800000 | 0.090340 |
| ashrae-energy-prediction | tc3_fault_injected | proposed_agent | 5 | `false` | 0.000000 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.250000 | 0.400000 | 0.458334 | 0.533334 | 0.000000 | 93.242800 | 14887.800000 | 4.600000 | 4.200000 | 0.119434 |
| ashrae-energy-prediction | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.142857 | 0.166667 | 0.153846 | 0.000000 | 0.000000 | 0.000000 | 0.076923 | 0.076923 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| ashrae-energy-prediction | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.866666 | 0.927273 | 1.000000 | 0.550000 | 0.704762 | 0.738637 | 0.816017 | 0.004649 | 42.169400 | 2492.600000 | 1.000000 | 0.000000 | 0.040232 |
| ashrae-energy-prediction | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 111.849048 | 4736.400000 | `null` | 8.600000 | 0.179194 |
| ashrae-energy-prediction | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 89.721600 | 13877.200000 | 4.600000 | 5.800000 | 0.106759 |
| ashrae-energy-prediction | tc4_mixed_history | proposed_agent | 5 | `true` | 0.600000 | 1.000000 | 0.733334 | 0.840000 | 0.600000 | 0.600000 | 0.600000 | 0.720000 | 0.720000 | 0.069600 | 96.106600 | 17503.800000 | 4.800000 | 5.200000 | 0.139045 |
| ashrae-energy-prediction | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.166667 | 0.333333 | 0.222222 | 0.000000 | 0.000000 | 0.000000 | 0.111111 | 0.111111 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| ashrae-energy-prediction | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 37.299800 | 2135.600000 | 1.000000 | 0.000000 | 0.034859 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 1.000000 | 0.978572 | 0.933333 | 0.946037 | 1.000000 | 0.900000 | 0.935714 | 0.923019 | 0.940876 | 0.002249 | 144.438760 | 5707.950000 | `null` | 9.350000 | 0.198529 |
| generic_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.985714 | 0.991667 | 0.987762 | 1.000000 | 0.925000 | 0.954762 | 0.956381 | 0.971262 | 0.001251 | 84.854300 | 11631.500000 | 4.300000 | 5.450000 | 0.091476 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 2700.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 0.750000 | 5.000000 | 0.650000 | 0.973214 | 0.808334 | 0.861831 | 0.900000 | 0.712500 | 0.750000 | 0.787166 | 0.805916 | 0.017583 | 78.255700 | 13236.750000 | 4.300000 | 4.150000 | 0.111199 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.140873 | 0.250000 | 0.177350 | 0.250000 | 0.500000 | 0.250000 | 0.338675 | 0.213675 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 1.000000 | 0.925000 | 0.959091 | 1.000000 | 0.887500 | 0.926191 | 0.923296 | 0.942641 | 0.001162 | 29.018400 | 1689.500000 | 1.000000 | 0.000000 | 0.036138 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task ashrae-energy-prediction --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/ashrae-energy-prediction-primary.md
```
