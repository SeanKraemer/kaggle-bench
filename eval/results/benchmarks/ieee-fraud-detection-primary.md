# Benchmark Aggregate Report

## Configuration

- Stage scope: `primary`
- Success threshold: `0.5`
- Tasks included: `ieee-fraud-detection`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.904762`
- Mean Add Precision: `0.492035`
- Mean Add Recall: `0.335714`
- Mean Add F1: `0.368892`
- Mean Remove Precision: `0.901587`
- Mean Remove Recall: `0.901905`
- Mean Remove F1: `0.841481`
- Mean Task Completion Score: `0.635399`
- Mean Strict Task Completion Score: `0.605187`
- Mean Task Completion Variance: `0.003744`
- Mean Runtime (s): `179.375403`
- Mean Total Tokens: `14080.700000`
- Mean API Calls: `3.050000`
- Mean Tool Calls: `4.850000`
- Mean Cost (USD): `0.177087`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ieee-fraud-detection | AUC | fraud_detection_tabular | binary_classification | multi_table_relational | large (590540) | high (434) | medium (16) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ieee-fraud-detection | 21 | 6 | 0.904762 | 4.047619 | 0.492035 | 0.335714 | 0.368892 | 0.901587 | 0.901905 | 0.841481 | 0.635399 | 0.605187 | 0.003744 | 179.375403 | 14080.700000 | 3.050000 | 4.850000 | 0.177087 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ieee-fraud-detection | tc1_from_scratch | claude_code | try1 | 0.714286 | 1.000000 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 547.361663 | 15435 | `null` | 26 | 0.506802 |
| ieee-fraud-detection | tc1_from_scratch | claude_code | try2 | 0.750000 | 0.900000 | 0.818182 | 1.000000 | 1.000000 | 1.000000 | 0.909091 | 0.909091 | `true` | 188.267040 | 11989 | `null` | 10 | 0.401864 |
| ieee-fraud-detection | tc1_from_scratch | claude_code | try3 | 0.818182 | 0.900000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 213.430662 | 12299 | `null` | 12 | 0.376170 |
| ieee-fraud-detection | tc1_from_scratch | claude_code | try4 | 0.818182 | 0.900000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 169.500838 | 9808 | `null` | 12 | 0.348167 |
| ieee-fraud-detection | tc1_from_scratch | claude_code | try5 | 0.588235 | 1.000000 | 0.740741 | 1.000000 | 1.000000 | 1.000000 | 0.870370 | 0.870370 | `true` | 292.022114 | 17092 | `null` | 11 | 0.480534 |
| ieee-fraud-detection | tc1_from_scratch | generic_agent | try1 | 0.666667 | 0.800000 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | `true` | 122.599000 | 27260 | 6 | 7 | 0.243251 |
| ieee-fraud-detection | tc1_from_scratch | generic_agent | try2 | 0.818182 | 0.900000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 175.190000 | 26868 | 7 | 7 | 0.250922 |
| ieee-fraud-detection | tc1_from_scratch | generic_agent | try3 | 0.800000 | 0.800000 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 121.952000 | 26425 | 6 | 7 | 0.246726 |
| ieee-fraud-detection | tc1_from_scratch | generic_agent | try4 | 0.727273 | 0.800000 | 0.761905 | 1.000000 | 1.000000 | 1.000000 | 0.880953 | 0.880953 | `true` | 139.013000 | 25532 | 9 | 10 | 0.257872 |
| ieee-fraud-detection | tc1_from_scratch | generic_agent | try5 | 0.800000 | 0.800000 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 144.540000 | 25228 | 6 | 8 | 0.223803 |
| ieee-fraud-detection | tc1_from_scratch | human | human_tc1_annotator_a_v1 | 0.153846 | 0.200000 | 0.173913 | 1.000000 | 1.000000 | 1.000000 | 0.586956 | 0.586956 | `true` | 1800 | `null` | `null` | `null` | `null` |
| ieee-fraud-detection | tc1_from_scratch | proposed_agent | try1 | 0.833333 | 1.000000 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 168.961000 | 31059 | 7 | 9 | 0.314181 |
| ieee-fraud-detection | tc1_from_scratch | proposed_agent | try2 | 0.818182 | 0.900000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 103.372000 | 22660 | 4 | 4 | 0.259688 |
| ieee-fraud-detection | tc1_from_scratch | proposed_agent | try3 | 0.777778 | 0.700000 | 0.736842 | 1.000000 | 1.000000 | 1.000000 | 0.868421 | 0.868421 | `true` | 181.615000 | 24185 | 5 | 6 | 0.276912 |
| ieee-fraud-detection | tc1_from_scratch | proposed_agent | try4 | 0.777778 | 0.700000 | 0.736842 | 1.000000 | 1.000000 | 1.000000 | 0.868421 | 0.868421 | `true` | 85.148000 | 18622 | 4 | 4 | 0.226526 |
| ieee-fraud-detection | tc1_from_scratch | proposed_agent | try5 | 0.818182 | 0.900000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 84.936000 | 19816 | 4 | 4 | 0.234392 |
| ieee-fraud-detection | tc1_from_scratch | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc1_from_scratch | single_llm | try1 | 0.800000 | 0.800000 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 99.244000 | 1254 | 1 | 0 | 0.671107 |
| ieee-fraud-detection | tc1_from_scratch | single_llm | try2 | 0.666667 | 1.000000 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 58.449000 | 4334 | 1 | 0 | 0.148466 |
| ieee-fraud-detection | tc1_from_scratch | single_llm | try3 | 0.750000 | 0.900000 | 0.818182 | 1.000000 | 1.000000 | 1.000000 | 0.909091 | 0.909091 | `true` | 52.048000 | 3327 | 1 | 0 | 0.056140 |
| ieee-fraud-detection | tc1_from_scratch | single_llm | try4 | 0.818182 | 0.900000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 50.921000 | 3518 | 1 | 0 | 0.059588 |
| ieee-fraud-detection | tc1_from_scratch | single_llm | try5 | 0.700000 | 0.700000 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | `true` | 16.997000 | 1099 | 1 | 0 | 0.023303 |
| ieee-fraud-detection | tc2_partial_good | claude_code | try1 | 0.333333 | 0.250000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 108.294420 | 6952 | `null` | 11 | 0.271864 |
| ieee-fraud-detection | tc2_partial_good | claude_code | try2 | 0.666667 | 0.500000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 104.650221 | 6876 | `null` | 11 | 0.271738 |
| ieee-fraud-detection | tc2_partial_good | claude_code | try3 | 0.333333 | 0.250000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 140.593781 | 8244 | `null` | 14 | 0.307935 |
| ieee-fraud-detection | tc2_partial_good | claude_code | try4 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 124.270874 | 8319 | `null` | 14 | 0.308521 |
| ieee-fraud-detection | tc2_partial_good | claude_code | try5 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 145.647243 | 8709 | `null` | 8 | 0.307442 |
| ieee-fraud-detection | tc2_partial_good | generic_agent | try1 | 0.333333 | 0.250000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 110.420000 | 21172 | 5 | 7 | 0.165677 |
| ieee-fraud-detection | tc2_partial_good | generic_agent | try2 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 102.962000 | 13094 | 5 | 5 | 0.115907 |
| ieee-fraud-detection | tc2_partial_good | generic_agent | try3 | 0.333333 | 0.250000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 104.467000 | 20303 | 7 | 10 | 0.165419 |
| ieee-fraud-detection | tc2_partial_good | generic_agent | try4 | 0.666667 | 0.500000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 131.631000 | 22830 | 6 | 7 | 0.176051 |
| ieee-fraud-detection | tc2_partial_good | generic_agent | try5 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 79.356000 | 17472 | 4 | 5 | 0.125854 |
| ieee-fraud-detection | tc2_partial_good | proposed_agent | try1 | 1.000000 | 0.750000 | 0.857143 | 0.000000 | 1.000000 | 0.000000 | 0.928571 | 0.428571 | `true` | 277.794000 | 42263 | 8 | 10 | 0.407343 |
| ieee-fraud-detection | tc2_partial_good | proposed_agent | try2 | 0.333333 | 0.250000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 205.536000 | 36635 | 7 | 8 | 0.297457 |
| ieee-fraud-detection | tc2_partial_good | proposed_agent | try3 | 0.666667 | 0.500000 | 0.571429 | 0.000000 | 1.000000 | 0.000000 | 0.785714 | 0.285714 | `true` | 191.635000 | 34796 | 7 | 9 | 0.291207 |
| ieee-fraud-detection | tc2_partial_good | proposed_agent | try4 | 0.500000 | 0.500000 | 0.500000 | 0.000000 | 1.000000 | 0.000000 | 0.750000 | 0.250000 | `true` | 176.293000 | 28761 | 5 | 5 | 0.219971 |
| ieee-fraud-detection | tc2_partial_good | proposed_agent | try5 | 0.333333 | 0.250000 | 0.285714 | 0.000000 | 1.000000 | 0.000000 | 0.642857 | 0.142857 | `true` | 144.955000 | 28849 | 6 | 8 | 0.250165 |
| ieee-fraud-detection | tc2_partial_good | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc2_partial_good | single_llm | try1 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 132.004000 | 3144 | 1 | 0 | 0.699037 |
| ieee-fraud-detection | tc2_partial_good | single_llm | try2 | 0.666667 | 0.500000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 41.563000 | 2569 | 1 | 0 | 0.045484 |
| ieee-fraud-detection | tc2_partial_good | single_llm | try3 | 0.500000 | 0.250000 | 0.333333 | 0.000000 | 1.000000 | 0.000000 | 0.666667 | 0.166666 | `true` | 41.460000 | 2708 | 1 | 0 | 0.046435 |
| ieee-fraud-detection | tc2_partial_good | single_llm | try4 | 0.666667 | 0.500000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 47.247000 | 2822 | 1 | 0 | 0.049279 |
| ieee-fraud-detection | tc2_partial_good | single_llm | try5 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 47.878000 | 2799 | 1 | 0 | 0.048934 |
| ieee-fraud-detection | tc3_fault_injected | claude_code | try1 | 0.500000 | 0.100000 | 0.166667 | 1.000000 | 1.000000 | 1.000000 | 0.583333 | 0.583333 | `true` | 141.399212 | 6775 | `null` | 11 | 0.255149 |
| ieee-fraud-detection | tc3_fault_injected | claude_code | try2 | 0.500000 | 0.100000 | 0.166667 | 1.000000 | 0.800000 | 0.888889 | 0.483334 | 0.527778 | `false` | 81.947905 | 4738 | `null` | 9 | 0.218891 |
| ieee-fraud-detection | tc3_fault_injected | claude_code | try3 | 0.500000 | 0.100000 | 0.166667 | 1.000000 | 0.800000 | 0.888889 | 0.483334 | 0.527778 | `false` | 96.843363 | 5291 | `null` | 9 | 0.222678 |
| ieee-fraud-detection | tc3_fault_injected | claude_code | try4 | 0.500000 | 0.100000 | 0.166667 | 1.000000 | 1.000000 | 1.000000 | 0.583333 | 0.583333 | `true` | 119.789414 | 6227 | `null` | 8 | 0.239303 |
| ieee-fraud-detection | tc3_fault_injected | claude_code | try5 | 0.500000 | 0.100000 | 0.166667 | 1.000000 | 0.800000 | 0.888889 | 0.483334 | 0.527778 | `false` | 111.325234 | 6519 | `null` | 12 | 0.265259 |
| ieee-fraud-detection | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 0.600000 | 0.750000 | 0.466666 | 0.541667 | `false` | 83.598000 | 15009 | 4 | 5 | 0.123676 |
| ieee-fraud-detection | tc3_fault_injected | generic_agent | try2 | 1.000000 | 0.100000 | 0.181818 | 1.000000 | 0.800000 | 0.888889 | 0.490909 | 0.535354 | `false` | 129.341000 | 20165 | 8 | 8 | 0.175036 |
| ieee-fraud-detection | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 85.676000 | 15557 | 5 | 5 | 0.135318 |
| ieee-fraud-detection | tc3_fault_injected | generic_agent | try4 | 1.000000 | 0.300000 | 0.461538 | 1.000000 | 0.800000 | 0.888889 | 0.630769 | 0.675214 | `true` | 124.146000 | 17806 | 6 | 6 | 0.152813 |
| ieee-fraud-detection | tc3_fault_injected | generic_agent | try5 | 1.000000 | 0.100000 | 0.181818 | 1.000000 | 0.800000 | 0.888889 | 0.490909 | 0.535354 | `false` | 89.989000 | 16099 | 6 | 6 | 0.139189 |
| ieee-fraud-detection | tc3_fault_injected | proposed_agent | try1 | 0.200000 | 0.100000 | 0.133333 | 1.000000 | 0.600000 | 0.750000 | 0.366667 | 0.441667 | `false` | 194.144000 | 20675 | 5 | 5 | 0.175397 |
| ieee-fraud-detection | tc3_fault_injected | proposed_agent | try2 | 0.600000 | 0.300000 | 0.400000 | 1.000000 | 0.800000 | 0.888889 | 0.600000 | 0.644445 | `true` | 147.464000 | 24167 | 5 | 5 | 0.195352 |
| ieee-fraud-detection | tc3_fault_injected | proposed_agent | try3 | 0.166667 | 0.100000 | 0.125000 | 1.000000 | 0.600000 | 0.750000 | 0.362500 | 0.437500 | `false` | 199.902000 | 21817 | 5 | 5 | 0.186634 |
| ieee-fraud-detection | tc3_fault_injected | proposed_agent | try4 | 0.250000 | 0.100000 | 0.142857 | 1.000000 | 0.600000 | 0.750000 | 0.371428 | 0.446429 | `false` | 187.976000 | 19530 | 5 | 5 | 0.171086 |
| ieee-fraud-detection | tc3_fault_injected | proposed_agent | try5 | 0.250000 | 0.100000 | 0.142857 | 1.000000 | 0.600000 | 0.750000 | 0.371428 | 0.446429 | `false` | 180.961000 | 18499 | 5 | 5 | 0.160541 |
| ieee-fraud-detection | tc3_fault_injected | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.600000 | 0.750000 | 0.300000 | 0.375000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.100000 | 0.181818 | 1.000000 | 0.600000 | 0.750000 | 0.390909 | 0.465909 | `false` | 117.639000 | 2270 | 1 | 0 | 0.685975 |
| ieee-fraud-detection | tc3_fault_injected | single_llm | try2 | 0.666667 | 0.200000 | 0.307692 | 1.000000 | 0.800000 | 0.888889 | 0.553846 | 0.598291 | `true` | 27.645000 | 1790 | 1 | 0 | 0.032713 |
| ieee-fraud-detection | tc3_fault_injected | single_llm | try3 | 0.500000 | 0.100000 | 0.166667 | 1.000000 | 0.800000 | 0.888889 | 0.483334 | 0.527778 | `false` | 30.407000 | 1905 | 1 | 0 | 0.035509 |
| ieee-fraud-detection | tc3_fault_injected | single_llm | try4 | 0.500000 | 0.100000 | 0.166667 | 1.000000 | 0.800000 | 0.888889 | 0.483334 | 0.527778 | `false` | 39.349000 | 2233 | 1 | 0 | 0.040429 |
| ieee-fraud-detection | tc3_fault_injected | single_llm | try5 | 0.500000 | 0.100000 | 0.166667 | 1.000000 | 0.600000 | 0.750000 | 0.383333 | 0.458334 | `false` | 38.072000 | 2256 | 1 | 0 | 0.040774 |
| ieee-fraud-detection | tc4_mixed_history | claude_code | try1 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 136.013307 | 5973 | `null` | 9 | 0.258478 |
| ieee-fraud-detection | tc4_mixed_history | claude_code | try2 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 1.000000 | 1.000000 | 0.785714 | 0.785714 | `true` | 111.812195 | 4873 | `null` | 8 | 0.231028 |
| ieee-fraud-detection | tc4_mixed_history | claude_code | try3 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 92.648945 | 5795 | `null` | 9 | 0.232383 |
| ieee-fraud-detection | tc4_mixed_history | claude_code | try4 | 0.500000 | 0.200000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 105.931256 | 6786 | `null` | 12 | 0.263509 |
| ieee-fraud-detection | tc4_mixed_history | claude_code | try5 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 124.599577 | 7572 | `null` | 12 | 0.312723 |
| ieee-fraud-detection | tc4_mixed_history | generic_agent | try1 | 0.500000 | 0.400000 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 88.843000 | 13109 | 4 | 5 | 0.112253 |
| ieee-fraud-detection | tc4_mixed_history | generic_agent | try2 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 102.853000 | 16113 | 4 | 5 | 0.124599 |
| ieee-fraud-detection | tc4_mixed_history | generic_agent | try3 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 72.766000 | 11855 | 5 | 4 | 0.109456 |
| ieee-fraud-detection | tc4_mixed_history | generic_agent | try4 | 0.500000 | 0.200000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 95.561000 | 17951 | 6 | 6 | 0.145445 |
| ieee-fraud-detection | tc4_mixed_history | generic_agent | try5 | 0.500000 | 0.400000 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 71.750000 | 13613 | 4 | 5 | 0.109925 |
| ieee-fraud-detection | tc4_mixed_history | proposed_agent | try1 | 0.333333 | 0.200000 | 0.250000 | 1.000000 | 1.000000 | 1.000000 | 0.625000 | 0.625000 | `true` | 182.470000 | 31547 | 6 | 8 | 0.272875 |
| ieee-fraud-detection | tc4_mixed_history | proposed_agent | try2 | 0.500000 | 0.400000 | 0.444444 | 0.666667 | 1.000000 | 0.800000 | 0.722222 | 0.622222 | `true` | 165.066000 | 28809 | 6 | 8 | 0.253558 |
| ieee-fraud-detection | tc4_mixed_history | proposed_agent | try3 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 104.656000 | 21706 | 5 | 6 | 0.176761 |
| ieee-fraud-detection | tc4_mixed_history | proposed_agent | try4 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 183.544000 | 31385 | 7 | 9 | 0.257283 |
| ieee-fraud-detection | tc4_mixed_history | proposed_agent | try5 | 0.500000 | 0.400000 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 107.153000 | 22335 | 5 | 6 | 0.181493 |
| ieee-fraud-detection | tc4_mixed_history | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.500000 | 0.666667 | 0.250000 | 0.333334 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc4_mixed_history | single_llm | try1 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 251.707000 | 2624 | 1 | 0 | 0.691118 |
| ieee-fraud-detection | tc4_mixed_history | single_llm | try2 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 39.469000 | 2284 | 1 | 0 | 0.039955 |
| ieee-fraud-detection | tc4_mixed_history | single_llm | try3 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 35.023000 | 2118 | 1 | 0 | 0.038756 |
| ieee-fraud-detection | tc4_mixed_history | single_llm | try4 | 0.500000 | 0.200000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 29.821000 | 1772 | 1 | 0 | 0.033566 |
| ieee-fraud-detection | tc4_mixed_history | single_llm | try5 | 0.500000 | 0.200000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 30.891000 | 1781 | 1 | 0 | 0.033701 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ieee-fraud-detection | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.737777 | 0.940000 | 0.821308 | 1.000000 | 1.000000 | 1.000000 | 0.910654 | 0.910654 | 0.000461 | 282.116463 | 13324.600000 | `null` | 14.200000 | 0.422708 |
| ieee-fraud-detection | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.762424 | 0.820000 | 0.789264 | 1.000000 | 1.000000 | 1.000000 | 0.894632 | 0.894632 | 0.000471 | 140.658800 | 26262.600000 | 6.800000 | 7.800000 | 0.244515 |
| ieee-fraud-detection | tc1_from_scratch | human | 1 | `true` | 1.000000 | 0.153846 | 0.200000 | 0.173913 | 1.000000 | 1.000000 | 1.000000 | 0.586956 | 0.586956 | 0.000000 | 1800 | `null` | `null` | `null` | `null` |
| ieee-fraud-detection | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.805051 | 0.840000 | 0.819412 | 1.000000 | 1.000000 | 1.000000 | 0.909706 | 0.909706 | 0.001226 | 124.806400 | 23268.400000 | 4.800000 | 5.400000 | 0.262339 |
| ieee-fraud-detection | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.746970 | 0.860000 | 0.795065 | 1.000000 | 1.000000 | 1.000000 | 0.897532 | 0.897532 | 0.000674 | 55.531800 | 2706.400000 | 1.000000 | 0.000000 | 0.191721 |
| ieee-fraud-detection | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.566667 | 0.350000 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | 0.006349 | 124.691308 | 7820.000000 | `null` | 11.600000 | 0.293500 |
| ieee-fraud-detection | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.466667 | 0.300000 | 0.361905 | 1.000000 | 1.000000 | 1.000000 | 0.680952 | 0.680952 | 0.002857 | 105.767200 | 18974.200000 | 5.400000 | 6.800000 | 0.149782 |
| ieee-fraud-detection | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.566667 | 0.450000 | 0.500000 | 0.200000 | 1.000000 | 0.200000 | 0.750000 | 0.350000 | 0.011224 | 199.242600 | 34260.800000 | 6.600000 | 8.000000 | 0.293228 |
| ieee-fraud-detection | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.566667 | 0.350000 | 0.428571 | 0.800000 | 1.000000 | 0.800000 | 0.714286 | 0.614286 | 0.003401 | 62.030400 | 2808.400000 | 1.000000 | 0.000000 | 0.177834 |
| ieee-fraud-detection | tc3_fault_injected | claude_code | 5 | `true` | 0.400000 | 0.500000 | 0.100000 | 0.166667 | 1.000000 | 0.880000 | 0.933333 | 0.523334 | 0.550000 | 0.002400 | 110.261026 | 5910.000000 | `null` | 9.800000 | 0.240256 |
| ieee-fraud-detection | tc3_fault_injected | generic_agent | 5 | `true` | 0.400000 | 1.000000 | 0.220000 | 0.345987 | 1.000000 | 0.800000 | 0.883333 | 0.572993 | 0.614661 | 0.014674 | 102.550000 | 16927.200000 | 5.800000 | 6.000000 | 0.145206 |
| ieee-fraud-detection | tc3_fault_injected | proposed_agent | 5 | `true` | 0.200000 | 0.293333 | 0.140000 | 0.188809 | 1.000000 | 0.640000 | 0.777778 | 0.414405 | 0.483294 | 0.008623 | 182.089400 | 20937.600000 | 5.000000 | 5.000000 | 0.177802 |
| ieee-fraud-detection | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.600000 | 0.750000 | 0.300000 | 0.375000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc3_fault_injected | single_llm | 5 | `true` | 0.200000 | 0.633333 | 0.120000 | 0.197902 | 1.000000 | 0.720000 | 0.833333 | 0.458951 | 0.515618 | 0.004108 | 50.622400 | 2090.800000 | 1.000000 | 0.000000 | 0.167080 |
| ieee-fraud-detection | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 0.833333 | 0.320000 | 0.452381 | 1.000000 | 1.000000 | 1.000000 | 0.726190 | 0.726190 | 0.003628 | 114.201056 | 6199.800000 | `null` | 10.000000 | 0.259624 |
| ieee-fraud-detection | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 0.566667 | 0.360000 | 0.434920 | 1.000000 | 1.000000 | 1.000000 | 0.717460 | 0.717460 | 0.001546 | 86.354600 | 14528.200000 | 4.600000 | 5.000000 | 0.120336 |
| ieee-fraud-detection | tc4_mixed_history | proposed_agent | 5 | `true` | 1.000000 | 0.533333 | 0.360000 | 0.427778 | 0.933333 | 0.900000 | 0.893333 | 0.663889 | 0.660555 | 0.008519 | 148.577800 | 27156.400000 | 5.800000 | 7.400000 | 0.228394 |
| ieee-fraud-detection | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.500000 | 0.666667 | 0.250000 | 0.333334 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 0.600000 | 0.320000 | 0.414286 | 1.000000 | 0.900000 | 0.933333 | 0.657143 | 0.673809 | 0.008469 | 77.382200 | 2115.800000 | 1.000000 | 0.000000 | 0.167419 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 0.850000 | 0.659444 | 0.427500 | 0.467232 | 1.000000 | 0.970000 | 0.983333 | 0.718616 | 0.725283 | 0.003209 | 157.817463 | 8313.600000 | `null` | 11.400000 | 0.304022 |
| generic_agent | 4 | 1.000000 | 5.000000 | 0.850000 | 0.698940 | 0.425000 | 0.483019 | 1.000000 | 0.950000 | 0.970833 | 0.716509 | 0.726926 | 0.004887 | 108.832650 | 19173.050000 | 5.650000 | 6.400000 | 0.164960 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 0.153846 | 0.200000 | 0.173913 | 1.000000 | 1.000000 | 1.000000 | 0.586956 | 0.586956 | 0.000000 | 1800.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 0.800000 | 0.549596 | 0.447500 | 0.484000 | 0.783333 | 0.885000 | 0.717778 | 0.684500 | 0.600889 | 0.007398 | 163.679050 | 26405.800000 | 5.550000 | 6.450000 | 0.240441 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.000000 | 0.000000 | 0.000000 | 0.750000 | 0.775000 | 0.604167 | 0.387500 | 0.302084 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 0.800000 | 0.636742 | 0.412500 | 0.458956 | 0.950000 | 0.905000 | 0.891667 | 0.681978 | 0.675311 | 0.004163 | 61.391700 | 2430.350000 | 1.000000 | 0.000000 | 0.176013 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task ieee-fraud-detection --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/ieee-fraud-detection-primary.md
```
