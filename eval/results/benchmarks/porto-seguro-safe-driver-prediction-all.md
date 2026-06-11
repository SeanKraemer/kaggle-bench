# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `porto-seguro-safe-driver-prediction`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.857143`
- Mean Add Precision: `0.816667`
- Mean Add Recall: `0.299607`
- Mean Add F1: `0.430035`
- Mean Remove Precision: `0.952381`
- Mean Remove Recall: `0.806349`
- Mean Remove F1: `0.850159`
- Mean Task Completion Score: `0.618192`
- Mean Strict Task Completion Score: `0.640097`
- Mean Task Completion Variance: `0.006545`
- Mean Runtime (s): `203.481399`
- Mean Total Tokens: `12283.775000`
- Mean API Calls: `2.850000`
- Mean Tool Calls: `6.250000`
- Mean Cost (USD): `0.154660`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| porto-seguro-safe-driver-prediction | NormalizedGini | insurance_tabular | binary_classification | single_table | large (595212) | medium (57) | low (7) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| porto-seguro-safe-driver-prediction | 21 | 6 | 0.857143 | 4.047619 | 0.816667 | 0.299607 | 0.430035 | 0.952381 | 0.806349 | 0.850159 | 0.618192 | 0.640097 | 0.006545 | 203.481399 | 12283.775000 | 2.850000 | 6.250000 | 0.154660 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | claude_code | try1 | 1.000000 | 0.461538 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 112.894780 | 4130 | `null` | 15 | 0.308145 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | claude_code | try2 | 0.875000 | 0.538462 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 310.855433 | 2627 | `null` | 23 | 0.376065 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | claude_code | try3 | 0.875000 | 0.538462 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 148.431304 | 1813 | `null` | 20 | 0.333218 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | claude_code | try4 | 1.000000 | 0.461538 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 340.661209 | 1854 | `null` | 26 | 0.595390 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | claude_code | try5 | 1.000000 | 0.538462 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | `true` | 150.273795 | 2017 | `null` | 15 | 0.306679 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | generic_agent | try1 | 0.833333 | 0.384615 | 0.526316 | 1.000000 | 1.000000 | 1.000000 | 0.763158 | 0.763158 | `true` | 64.629000 | 16578 | 5 | 5 | 0.153948 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | generic_agent | try2 | 1.000000 | 0.615385 | 0.761905 | 1.000000 | 1.000000 | 1.000000 | 0.880953 | 0.880953 | `true` | 68.573000 | 15637 | 4 | 4 | 0.156104 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | generic_agent | try3 | 1.000000 | 0.538462 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | `true` | 81.606000 | 20595 | 5 | 5 | 0.147441 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | generic_agent | try4 | 1.000000 | 0.461538 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 75.097000 | 14687 | 6 | 5 | 0.126690 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | generic_agent | try5 | 1.000000 | 0.461538 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 66.617000 | 11818 | 5 | 4 | 0.106365 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | human | human_tc1_sean_kraemer_v3_manual_rebuild | 1.000000 | 0.307692 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | `true` | 2700 | `null` | `null` | `null` | `null` |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | proposed_agent | try1 | 1.000000 | 0.538462 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | `true` | 75.551000 | 20073 | 4 | 5 | 0.240357 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | proposed_agent | try2 | 1.000000 | 0.538462 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | `true` | 80.750000 | 24776 | 5 | 6 | 0.183118 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | proposed_agent | try3 | 1.000000 | 0.538462 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | `true` | 84.271000 | 17619 | 4 | 4 | 0.146622 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | proposed_agent | try4 | 1.000000 | 0.538462 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | `true` | 85.382000 | 25403 | 5 | 6 | 0.189225 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | proposed_agent | try5 | 1.000000 | 0.538462 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | `true` | 89.703000 | 21691 | 4 | 4 | 0.167154 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | rule_based | try1 | 0.200000 | 0.076923 | 0.111111 | 1.000000 | 1.000000 | 1.000000 | 0.555555 | 0.555555 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | single_llm | try1 | 1.000000 | 0.538462 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | `true` | 11.076000 | 691 | 1 | 0 | 0.101490 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | single_llm | try2 | 1.000000 | 0.538462 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | `true` | 11.981000 | 734 | 1 | 0 | 0.018441 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | single_llm | try3 | 1.000000 | 0.538462 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | `true` | 13.070000 | 809 | 1 | 0 | 0.019566 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | single_llm | try4 | 1.000000 | 0.538462 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | `true` | 12.265000 | 683 | 1 | 0 | 0.017093 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | single_llm | try5 | 1.000000 | 0.538462 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | `true` | 11.828000 | 654 | 1 | 0 | 0.017241 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | claude_code | try1 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 350.953314 | 2791 | `null` | 24 | 0.592767 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | claude_code | try2 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 80.926943 | 3688 | `null` | 15 | 0.253567 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | claude_code | try3 | 0.750000 | 0.300000 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | `true` | 141.978798 | 1829 | `null` | 15 | 0.298296 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | claude_code | try4 | 1.000000 | 0.300000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 91.164569 | 1820 | `null` | 17 | 0.226374 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | claude_code | try5 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 348.580583 | 2748 | `null` | 43 | 0.759244 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | generic_agent | try1 | 0.666667 | 0.200000 | 0.307692 | 1.000000 | 1.000000 | 1.000000 | 0.653846 | 0.653846 | `true` | 81.557000 | 20068 | 5 | 5 | 0.181729 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | generic_agent | try2 | 0.666667 | 0.200000 | 0.307692 | 1.000000 | 1.000000 | 1.000000 | 0.653846 | 0.653846 | `true` | 51.683000 | 9852 | 4 | 4 | 0.086489 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | generic_agent | try3 | 1.000000 | 0.300000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 87.245000 | 16956 | 6 | 5 | 0.138319 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | generic_agent | try4 | 1.000000 | 0.300000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 96.650000 | 19764 | 7 | 6 | 0.166285 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | generic_agent | try5 | 1.000000 | 0.300000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 113.872000 | 28834 | 7 | 8 | 0.220711 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | proposed_agent | try1 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 84.986000 | 21676 | 5 | 6 | 0.171220 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | proposed_agent | try2 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 64.618000 | 9677 | 3 | 2 | 0.101847 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | proposed_agent | try3 | 1.000000 | 0.300000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 84.218000 | 21395 | 5 | 6 | 0.171583 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | proposed_agent | try4 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 93.390000 | 16090 | 4 | 3 | 0.156752 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | proposed_agent | try5 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 92.183000 | 21057 | 5 | 5 | 0.177337 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | rule_based | try1 | 0.200000 | 0.100000 | 0.133333 | 1.000000 | 1.000000 | 1.000000 | 0.566666 | 0.566666 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | single_llm | try1 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 37.749000 | 2426 | 1 | 0 | 0.127311 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | single_llm | try2 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 35.048000 | 2244 | 1 | 0 | 0.041155 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | single_llm | try3 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 33.696000 | 2181 | 1 | 0 | 0.040210 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | single_llm | try4 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 44.903000 | 2919 | 1 | 0 | 0.051280 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | single_llm | try5 | 1.000000 | 0.300000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 55.347000 | 3479 | 1 | 0 | 0.059680 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | claude_code | try1 | 1.000000 | 0.307692 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | `true` | 76.373896 | 2026 | `null` | 17 | 0.211160 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | claude_code | try2 | 1.000000 | 0.307692 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | `true` | 126.685109 | 2838 | `null` | 30 | 0.338184 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | claude_code | try3 | 1.000000 | 0.461538 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 90.829482 | 2567 | `null` | 22 | 0.249591 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | claude_code | try4 | 1.000000 | 0.384615 | 0.555556 | 1.000000 | 1.000000 | 1.000000 | 0.777778 | 0.777778 | `true` | 80.858295 | 2273 | `null` | 19 | 0.209036 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | claude_code | try5 | 1.000000 | 0.461538 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 306.178913 | 2515 | `null` | 50 | 0.937506 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.384615 | 0.555556 | 1.000000 | 1.000000 | 1.000000 | 0.777778 | 0.777778 | `true` | 83.247000 | 19958 | 5 | 5 | 0.147988 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | generic_agent | try2 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.500000 | 0.666667 | 0.250000 | 0.333334 | `false` | 95.535000 | 26135 | 6 | 6 | 0.183786 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.230769 | 0.375000 | 1.000000 | 0.500000 | 0.666667 | 0.437500 | 0.520833 | `false` | 93.623000 | 23738 | 6 | 7 | 0.174337 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | generic_agent | try4 | 1.000000 | 0.384615 | 0.555556 | 1.000000 | 1.000000 | 1.000000 | 0.777778 | 0.777778 | `true` | 93.841000 | 25703 | 5 | 6 | 0.175565 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | generic_agent | try5 | 1.000000 | 0.307692 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | `true` | 65.020000 | 22069 | 5 | 5 | 0.139429 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | proposed_agent | try1 | 1.000000 | 0.153846 | 0.266667 | 1.000000 | 0.500000 | 0.666667 | 0.383333 | 0.466667 | `false` | 83.259000 | 17914 | 5 | 5 | 0.147359 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | proposed_agent | try2 | 1.000000 | 0.230769 | 0.375000 | 1.000000 | 0.500000 | 0.666667 | 0.437500 | 0.520833 | `false` | 89.674000 | 19475 | 5 | 5 | 0.158402 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | proposed_agent | try3 | 1.000000 | 0.153846 | 0.266667 | 1.000000 | 0.500000 | 0.666667 | 0.383333 | 0.466667 | `false` | 108.147000 | 22853 | 5 | 5 | 0.185940 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | proposed_agent | try4 | 1.000000 | 0.230769 | 0.375000 | 1.000000 | 0.500000 | 0.666667 | 0.437500 | 0.520833 | `false` | 108.434000 | 22442 | 5 | 4 | 0.183843 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | proposed_agent | try5 | 1.000000 | 0.307692 | 0.470588 | 1.000000 | 0.500000 | 0.666667 | 0.485294 | 0.568628 | `false` | 72.289000 | 16678 | 4 | 4 | 0.138775 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | rule_based | try1 | 0.200000 | 0.076923 | 0.111111 | 0.000000 | 0.000000 | 0.000000 | 0.055556 | 0.055556 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.153846 | 0.266667 | 1.000000 | 0.500000 | 0.666667 | 0.383333 | 0.466667 | `false` | 42.172000 | 2542 | 1 | 0 | 0.044822 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | single_llm | try2 | 1.000000 | 0.307692 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | `true` | 36.035000 | 2194 | 1 | 0 | 0.040390 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | single_llm | try3 | 1.000000 | 0.230769 | 0.375000 | 1.000000 | 1.000000 | 1.000000 | 0.687500 | 0.687500 | `true` | 39.005000 | 2373 | 1 | 0 | 0.042287 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | single_llm | try4 | 1.000000 | 0.153846 | 0.266667 | 1.000000 | 0.500000 | 0.666667 | 0.383333 | 0.466667 | `false` | 37.050000 | 2126 | 1 | 0 | 0.039370 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | single_llm | try5 | 1.000000 | 0.230769 | 0.375000 | 1.000000 | 0.500000 | 0.666667 | 0.437500 | 0.520833 | `false` | 40.003000 | 2369 | 1 | 0 | 0.043015 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | claude_code | try1 | 0.666667 | 0.181818 | 0.285714 | 1.000000 | 0.666667 | 0.800000 | 0.476191 | 0.542857 | `false` | 102.719577 | 2260 | `null` | 19 | 0.223678 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | claude_code | try2 | 1.000000 | 0.272727 | 0.428571 | 1.000000 | 0.666667 | 0.800000 | 0.547619 | 0.614286 | `true` | 125.958092 | 2204 | `null` | 12 | 0.357257 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | claude_code | try3 | 1.000000 | 0.363636 | 0.533333 | 1.000000 | 1.000000 | 1.000000 | 0.766666 | 0.766666 | `true` | 83.934312 | 1782 | `null` | 14 | 0.231813 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | claude_code | try4 | 1.000000 | 0.272727 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | `true` | 101.708480 | 2564 | `null` | 13 | 0.252503 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | claude_code | try5 | 1.000000 | 0.363636 | 0.533333 | 1.000000 | 1.000000 | 1.000000 | 0.766666 | 0.766666 | `true` | 73.897027 | 3054 | `null` | 8 | 0.211618 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | generic_agent | try1 | 1.000000 | 0.272727 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | `true` | 64.297000 | 14577 | 6 | 5 | 0.126102 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | generic_agent | try2 | 1.000000 | 0.363636 | 0.533333 | 1.000000 | 1.000000 | 1.000000 | 0.766666 | 0.766666 | `true` | 99.788000 | 24352 | 7 | 6 | 0.192859 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | generic_agent | try3 | 0.666667 | 0.181818 | 0.285714 | 1.000000 | 0.333333 | 0.500000 | 0.309524 | 0.392857 | `false` | 86.303000 | 23055 | 5 | 5 | 0.165290 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | generic_agent | try4 | 0.750000 | 0.272727 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 87.189000 | 21155 | 6 | 5 | 0.162348 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | generic_agent | try5 | 1.000000 | 0.272727 | 0.428571 | 1.000000 | 0.666667 | 0.800000 | 0.547619 | 0.614286 | `true` | 76.683000 | 21327 | 6 | 6 | 0.157755 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | proposed_agent | try1 | 1.000000 | 0.363636 | 0.533333 | 1.000000 | 0.333333 | 0.500000 | 0.433333 | 0.516666 | `false` | 176.302000 | 40579 | 6 | 7 | 0.319846 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | proposed_agent | try2 | 1.000000 | 0.272727 | 0.428571 | 1.000000 | 0.333333 | 0.500000 | 0.380952 | 0.464286 | `false` | 158.960000 | 33913 | 6 | 7 | 0.274319 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | proposed_agent | try3 | 1.000000 | 0.363636 | 0.533333 | 1.000000 | 0.666667 | 0.800000 | 0.600000 | 0.666667 | `true` | 296.432000 | 55647 | 7 | 8 | 0.467129 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | proposed_agent | try4 | 1.000000 | 0.363636 | 0.533333 | 1.000000 | 0.333333 | 0.500000 | 0.433333 | 0.516666 | `false` | 192.566000 | 36889 | 5 | 4 | 0.297340 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | proposed_agent | try5 | 1.000000 | 0.272727 | 0.428571 | 1.000000 | 0.333333 | 0.500000 | 0.380952 | 0.464286 | `false` | 114.281000 | 24086 | 5 | 5 | 0.194899 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | rule_based | try1 | 0.200000 | 0.090909 | 0.125000 | 1.000000 | 0.333333 | 0.500000 | 0.229166 | 0.312500 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | single_llm | try1 | 1.000000 | 0.272727 | 0.428571 | 1.000000 | 0.666667 | 0.800000 | 0.547619 | 0.614286 | `true` | 46.629000 | 2919 | 1 | 0 | 0.050309 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | single_llm | try2 | 1.000000 | 0.272727 | 0.428571 | 1.000000 | 0.666667 | 0.800000 | 0.547619 | 0.614286 | `true` | 78.295000 | 4935 | 1 | 0 | 0.081557 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | single_llm | try3 | 1.000000 | 0.272727 | 0.428571 | 1.000000 | 0.333333 | 0.500000 | 0.380952 | 0.464286 | `false` | 55.094000 | 3521 | 1 | 0 | 0.060347 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | single_llm | try4 | 1.000000 | 0.181818 | 0.307692 | 1.000000 | 0.333333 | 0.500000 | 0.320512 | 0.403846 | `false` | 50.939000 | 3202 | 1 | 0 | 0.055562 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | single_llm | try5 | 1.000000 | 0.272727 | 0.428571 | 1.000000 | 0.666667 | 0.800000 | 0.547619 | 0.614286 | `true` | 59.047000 | 3510 | 1 | 0 | 0.060182 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.950000 | 0.507692 | 0.659298 | 1.000000 | 1.000000 | 1.000000 | 0.829649 | 0.829649 | 0.000165 | 212.623304 | 2488.200000 | `null` | 19.800000 | 0.383899 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.966667 | 0.492308 | 0.650276 | 1.000000 | 1.000000 | 1.000000 | 0.825138 | 0.825138 | 0.001550 | 71.304400 | 15863.000000 | 5.000000 | 4.600000 | 0.138110 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 0.307692 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | 0.000000 | 2700 | `null` | `null` | `null` | `null` |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.538462 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | 0.000000 | 83.131400 | 21912.400000 | 4.400000 | 5.000000 | 0.185295 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.200000 | 0.076923 | 0.111111 | 1.000000 | 1.000000 | 1.000000 | 0.555555 | 0.555555 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| porto-seguro-safe-driver-prediction | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.538462 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | 0.000000 | 12.044000 | 714.200000 | 1.000000 | 0.000000 | 0.034766 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.950000 | 0.360000 | 0.520879 | 1.000000 | 1.000000 | 1.000000 | 0.760439 | 0.760439 | 0.000985 | 202.720841 | 2575.200000 | `null` | 22.800000 | 0.426050 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.866667 | 0.260000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | 0.001420 | 86.201400 | 19094.800000 | 5.800000 | 5.600000 | 0.158707 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.380000 | 0.549451 | 1.000000 | 1.000000 | 1.000000 | 0.774725 | 0.774725 | 0.000483 | 83.879000 | 17979.000000 | 4.400000 | 4.400000 | 0.155748 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.200000 | 0.100000 | 0.133333 | 1.000000 | 1.000000 | 1.000000 | 0.566666 | 0.566666 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| porto-seguro-safe-driver-prediction | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.340000 | 0.501832 | 1.000000 | 1.000000 | 1.000000 | 0.750916 | 0.750916 | 0.002227 | 41.348600 | 2649.800000 | 1.000000 | 0.000000 | 0.063927 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.384615 | 0.551978 | 1.000000 | 1.000000 | 1.000000 | 0.775989 | 0.775989 | 0.001297 | 136.185139 | 2443.800000 | `null` | 27.600000 | 0.389095 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | generic_agent | 5 | `true` | 0.600000 | 0.800000 | 0.261538 | 0.391340 | 1.000000 | 0.800000 | 0.866667 | 0.595670 | 0.629003 | 0.046065 | 86.253200 | 23520.600000 | 5.400000 | 5.800000 | 0.164221 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | proposed_agent | 5 | `false` | 0.000000 | 1.000000 | 0.215384 | 0.350784 | 1.000000 | 0.500000 | 0.666667 | 0.425392 | 0.508726 | 0.001484 | 92.360600 | 19872.400000 | 4.800000 | 4.600000 | 0.162864 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.200000 | 0.076923 | 0.111111 | 0.000000 | 0.000000 | 0.000000 | 0.055556 | 0.055556 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| porto-seguro-safe-driver-prediction | tc3_fault_injected | single_llm | 5 | `true` | 0.400000 | 1.000000 | 0.215384 | 0.350784 | 1.000000 | 0.700000 | 0.800000 | 0.525392 | 0.575392 | 0.023685 | 38.853000 | 2320.800000 | 1.000000 | 0.000000 | 0.041977 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | claude_code | 5 | `true` | 0.800000 | 0.933333 | 0.290909 | 0.441904 | 1.000000 | 0.866667 | 0.920000 | 0.654286 | 0.680952 | 0.014391 | 97.643498 | 2372.800000 | `null` | 13.200000 | 0.255374 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | generic_agent | 5 | `true` | 0.800000 | 0.883333 | 0.272727 | 0.415238 | 1.000000 | 0.800000 | 0.860000 | 0.607619 | 0.637619 | 0.027534 | 82.852000 | 20893.200000 | 6.000000 | 5.400000 | 0.160871 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | proposed_agent | 5 | `true` | 0.200000 | 1.000000 | 0.327272 | 0.491428 | 1.000000 | 0.400000 | 0.560000 | 0.445714 | 0.525714 | 0.006500 | 187.708200 | 38222.800000 | 5.800000 | 6.200000 | 0.310707 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.200000 | 0.090909 | 0.125000 | 1.000000 | 0.333333 | 0.500000 | 0.229166 | 0.312500 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| porto-seguro-safe-driver-prediction | tc4_mixed_history | single_llm | 5 | `true` | 0.600000 | 1.000000 | 0.254545 | 0.404395 | 1.000000 | 0.533333 | 0.680000 | 0.468864 | 0.542198 | 0.009669 | 58.000800 | 3617.400000 | 1.000000 | 0.000000 | 0.061592 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 0.950000 | 0.958333 | 0.385804 | 0.543515 | 1.000000 | 0.966667 | 0.980000 | 0.755091 | 0.761757 | 0.004209 | 162.293195 | 2470.000000 | `null` | 20.850000 | 0.363604 |
| generic_agent | 4 | 1.000000 | 5.000000 | 0.850000 | 0.879167 | 0.321643 | 0.464214 | 1.000000 | 0.900000 | 0.931667 | 0.682107 | 0.697940 | 0.019142 | 81.652750 | 19842.900000 | 5.550000 | 5.350000 | 0.155477 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.307692 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | 0.000000 | 2700.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 0.750000 | 5.000000 | 0.550000 | 1.000000 | 0.365279 | 0.522916 | 1.000000 | 0.725000 | 0.806667 | 0.623958 | 0.664791 | 0.002117 | 111.769800 | 24496.650000 | 4.850000 | 5.050000 | 0.203653 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.200000 | 0.086189 | 0.120139 | 0.750000 | 0.583333 | 0.625000 | 0.351736 | 0.372569 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 0.750000 | 1.000000 | 0.337098 | 0.489253 | 1.000000 | 0.808333 | 0.870000 | 0.648793 | 0.679627 | 0.008895 | 37.561600 | 2325.550000 | 1.000000 | 0.000000 | 0.050565 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task porto-seguro-safe-driver-prediction --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/porto-seguro-safe-driver-prediction-all.md
```
