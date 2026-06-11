# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `ieee-fraud-detection`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.904762`
- Mean Add Precision: `0.504921`
- Mean Add Recall: `0.292857`
- Mean Add F1: `0.330030`
- Mean Remove Precision: `0.900000`
- Mean Remove Recall: `0.901905`
- Mean Remove F1: `0.840212`
- Mean Task Completion Score: `0.615967`
- Mean Strict Task Completion Score: `0.585121`
- Mean Task Completion Variance: `0.002782`
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
| ieee-fraud-detection | 21 | 6 | 0.904762 | 4.047619 | 0.504921 | 0.292857 | 0.330030 | 0.900000 | 0.901905 | 0.840212 | 0.615967 | 0.585121 | 0.002782 | 179.375403 | 14080.700000 | 3.050000 | 4.850000 | 0.177087 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ieee-fraud-detection | tc1_from_scratch | claude_code | try1 | 0.560000 | 1.000000 | 0.717949 | 1.000000 | 1.000000 | 1.000000 | 0.858974 | 0.858974 | `true` | 547.361663 | 15435 | `null` | 26 | 0.506802 |
| ieee-fraud-detection | tc1_from_scratch | claude_code | try2 | 0.647059 | 0.785714 | 0.709677 | 1.000000 | 1.000000 | 1.000000 | 0.854839 | 0.854839 | `true` | 188.267040 | 11989 | `null` | 10 | 0.401864 |
| ieee-fraud-detection | tc1_from_scratch | claude_code | try3 | 0.722222 | 0.928571 | 0.812500 | 1.000000 | 1.000000 | 1.000000 | 0.906250 | 0.906250 | `true` | 213.430662 | 12299 | `null` | 12 | 0.376170 |
| ieee-fraud-detection | tc1_from_scratch | claude_code | try4 | 0.733333 | 0.785714 | 0.758621 | 1.000000 | 1.000000 | 1.000000 | 0.879310 | 0.879310 | `true` | 169.500838 | 9808 | `null` | 12 | 0.348167 |
| ieee-fraud-detection | tc1_from_scratch | claude_code | try5 | 0.466667 | 1.000000 | 0.636364 | 1.000000 | 1.000000 | 1.000000 | 0.818182 | 0.818182 | `true` | 292.022114 | 17092 | `null` | 11 | 0.480534 |
| ieee-fraud-detection | tc1_from_scratch | generic_agent | try1 | 0.526316 | 0.714286 | 0.606061 | 1.000000 | 1.000000 | 1.000000 | 0.803030 | 0.803030 | `true` | 122.599000 | 27260 | 6 | 7 | 0.243251 |
| ieee-fraud-detection | tc1_from_scratch | generic_agent | try2 | 0.785714 | 0.785714 | 0.785714 | 1.000000 | 1.000000 | 1.000000 | 0.892857 | 0.892857 | `true` | 175.190000 | 26868 | 7 | 7 | 0.250922 |
| ieee-fraud-detection | tc1_from_scratch | generic_agent | try3 | 0.714286 | 0.714286 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 121.952000 | 26425 | 6 | 7 | 0.246726 |
| ieee-fraud-detection | tc1_from_scratch | generic_agent | try4 | 0.714286 | 0.714286 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 139.013000 | 25532 | 9 | 10 | 0.257872 |
| ieee-fraud-detection | tc1_from_scratch | generic_agent | try5 | 0.833333 | 0.714286 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 144.540000 | 25228 | 6 | 8 | 0.223803 |
| ieee-fraud-detection | tc1_from_scratch | human | human_tc1_annotator_a_v1 | 0.176471 | 0.214286 | 0.193548 | 1.000000 | 1.000000 | 1.000000 | 0.596774 | 0.596774 | `true` | 1800 | `null` | `null` | `null` | `null` |
| ieee-fraud-detection | tc1_from_scratch | proposed_agent | try1 | 0.666667 | 0.857143 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 168.961000 | 31059 | 7 | 9 | 0.314181 |
| ieee-fraud-detection | tc1_from_scratch | proposed_agent | try2 | 0.611111 | 0.785714 | 0.687500 | 1.000000 | 1.000000 | 1.000000 | 0.843750 | 0.843750 | `true` | 103.372000 | 22660 | 4 | 4 | 0.259688 |
| ieee-fraud-detection | tc1_from_scratch | proposed_agent | try3 | 0.750000 | 0.642857 | 0.692308 | 1.000000 | 1.000000 | 1.000000 | 0.846154 | 0.846154 | `true` | 181.615000 | 24185 | 5 | 6 | 0.276912 |
| ieee-fraud-detection | tc1_from_scratch | proposed_agent | try4 | 0.692308 | 0.642857 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 85.148000 | 18622 | 4 | 4 | 0.226526 |
| ieee-fraud-detection | tc1_from_scratch | proposed_agent | try5 | 0.687500 | 0.785714 | 0.733333 | 1.000000 | 1.000000 | 1.000000 | 0.866667 | 0.866667 | `true` | 84.936000 | 19816 | 4 | 4 | 0.234392 |
| ieee-fraud-detection | tc1_from_scratch | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc1_from_scratch | single_llm | try1 | 0.714286 | 0.714286 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 99.244000 | 1254 | 1 | 0 | 0.671107 |
| ieee-fraud-detection | tc1_from_scratch | single_llm | try2 | 0.565217 | 0.928571 | 0.702703 | 1.000000 | 1.000000 | 1.000000 | 0.851352 | 0.851352 | `true` | 58.449000 | 4334 | 1 | 0 | 0.148466 |
| ieee-fraud-detection | tc1_from_scratch | single_llm | try3 | 0.647059 | 0.785714 | 0.709677 | 1.000000 | 1.000000 | 1.000000 | 0.854839 | 0.854839 | `true` | 52.048000 | 3327 | 1 | 0 | 0.056140 |
| ieee-fraud-detection | tc1_from_scratch | single_llm | try4 | 0.687500 | 0.785714 | 0.733333 | 1.000000 | 1.000000 | 1.000000 | 0.866667 | 0.866667 | `true` | 50.921000 | 3518 | 1 | 0 | 0.059588 |
| ieee-fraud-detection | tc1_from_scratch | single_llm | try5 | 0.642857 | 0.642857 | 0.642857 | 1.000000 | 1.000000 | 1.000000 | 0.821429 | 0.821429 | `true` | 16.997000 | 1099 | 1 | 0 | 0.023303 |
| ieee-fraud-detection | tc2_partial_good | claude_code | try1 | 0.333333 | 0.125000 | 0.181818 | 1.000000 | 1.000000 | 1.000000 | 0.590909 | 0.590909 | `true` | 108.294420 | 6952 | `null` | 11 | 0.271864 |
| ieee-fraud-detection | tc2_partial_good | claude_code | try2 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 104.650221 | 6876 | `null` | 11 | 0.271738 |
| ieee-fraud-detection | tc2_partial_good | claude_code | try3 | 0.333333 | 0.125000 | 0.181818 | 1.000000 | 1.000000 | 1.000000 | 0.590909 | 0.590909 | `true` | 140.593781 | 8244 | `null` | 14 | 0.307935 |
| ieee-fraud-detection | tc2_partial_good | claude_code | try4 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 124.270874 | 8319 | `null` | 14 | 0.308521 |
| ieee-fraud-detection | tc2_partial_good | claude_code | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 145.647243 | 8709 | `null` | 8 | 0.307442 |
| ieee-fraud-detection | tc2_partial_good | generic_agent | try1 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 110.420000 | 21172 | 5 | 7 | 0.165677 |
| ieee-fraud-detection | tc2_partial_good | generic_agent | try2 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 102.962000 | 13094 | 5 | 5 | 0.115907 |
| ieee-fraud-detection | tc2_partial_good | generic_agent | try3 | 0.600000 | 0.375000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 104.467000 | 20303 | 7 | 10 | 0.165419 |
| ieee-fraud-detection | tc2_partial_good | generic_agent | try4 | 0.800000 | 0.500000 | 0.615385 | 1.000000 | 1.000000 | 1.000000 | 0.807692 | 0.807692 | `true` | 131.631000 | 22830 | 6 | 7 | 0.176051 |
| ieee-fraud-detection | tc2_partial_good | generic_agent | try5 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 79.356000 | 17472 | 4 | 5 | 0.125854 |
| ieee-fraud-detection | tc2_partial_good | proposed_agent | try1 | 0.714286 | 0.625000 | 0.666667 | 0.000000 | 1.000000 | 0.000000 | 0.833333 | 0.333334 | `true` | 277.794000 | 42263 | 8 | 10 | 0.407343 |
| ieee-fraud-detection | tc2_partial_good | proposed_agent | try2 | 0.600000 | 0.375000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 205.536000 | 36635 | 7 | 8 | 0.297457 |
| ieee-fraud-detection | tc2_partial_good | proposed_agent | try3 | 0.800000 | 0.500000 | 0.615385 | 0.000000 | 1.000000 | 0.000000 | 0.807692 | 0.307692 | `true` | 191.635000 | 34796 | 7 | 9 | 0.291207 |
| ieee-fraud-detection | tc2_partial_good | proposed_agent | try4 | 0.666667 | 0.500000 | 0.571429 | 0.000000 | 1.000000 | 0.000000 | 0.785714 | 0.285714 | `true` | 176.293000 | 28761 | 5 | 5 | 0.219971 |
| ieee-fraud-detection | tc2_partial_good | proposed_agent | try5 | 0.500000 | 0.250000 | 0.333333 | 0.000000 | 1.000000 | 0.000000 | 0.666667 | 0.166666 | `true` | 144.955000 | 28849 | 6 | 8 | 0.250165 |
| ieee-fraud-detection | tc2_partial_good | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc2_partial_good | single_llm | try1 | 0.750000 | 0.375000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 132.004000 | 3144 | 1 | 0 | 0.699037 |
| ieee-fraud-detection | tc2_partial_good | single_llm | try2 | 0.750000 | 0.375000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 41.563000 | 2569 | 1 | 0 | 0.045484 |
| ieee-fraud-detection | tc2_partial_good | single_llm | try3 | 0.500000 | 0.250000 | 0.333333 | 0.000000 | 1.000000 | 0.000000 | 0.666667 | 0.166666 | `true` | 41.460000 | 2708 | 1 | 0 | 0.046435 |
| ieee-fraud-detection | tc2_partial_good | single_llm | try4 | 0.750000 | 0.375000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 47.247000 | 2822 | 1 | 0 | 0.049279 |
| ieee-fraud-detection | tc2_partial_good | single_llm | try5 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 47.878000 | 2799 | 1 | 0 | 0.048934 |
| ieee-fraud-detection | tc3_fault_injected | claude_code | try1 | 0.500000 | 0.071429 | 0.125000 | 1.000000 | 1.000000 | 1.000000 | 0.562500 | 0.562500 | `true` | 141.399212 | 6775 | `null` | 11 | 0.255149 |
| ieee-fraud-detection | tc3_fault_injected | claude_code | try2 | 0.500000 | 0.071429 | 0.125000 | 1.000000 | 0.800000 | 0.888889 | 0.462500 | 0.506945 | `false` | 81.947905 | 4738 | `null` | 9 | 0.218891 |
| ieee-fraud-detection | tc3_fault_injected | claude_code | try3 | 0.500000 | 0.071429 | 0.125000 | 1.000000 | 0.800000 | 0.888889 | 0.462500 | 0.506945 | `false` | 96.843363 | 5291 | `null` | 9 | 0.222678 |
| ieee-fraud-detection | tc3_fault_injected | claude_code | try4 | 0.500000 | 0.071429 | 0.125000 | 1.000000 | 1.000000 | 1.000000 | 0.562500 | 0.562500 | `true` | 119.789414 | 6227 | `null` | 8 | 0.239303 |
| ieee-fraud-detection | tc3_fault_injected | claude_code | try5 | 0.500000 | 0.071429 | 0.125000 | 1.000000 | 0.800000 | 0.888889 | 0.462500 | 0.506945 | `false` | 111.325234 | 6519 | `null` | 12 | 0.265259 |
| ieee-fraud-detection | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.142857 | 0.250000 | 1.000000 | 0.600000 | 0.750000 | 0.425000 | 0.500000 | `false` | 83.598000 | 15009 | 4 | 5 | 0.123676 |
| ieee-fraud-detection | tc3_fault_injected | generic_agent | try2 | 1.000000 | 0.071429 | 0.133333 | 1.000000 | 0.800000 | 0.888889 | 0.466667 | 0.511111 | `false` | 129.341000 | 20165 | 8 | 8 | 0.175036 |
| ieee-fraud-detection | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.285714 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 85.676000 | 15557 | 5 | 5 | 0.135318 |
| ieee-fraud-detection | tc3_fault_injected | generic_agent | try4 | 1.000000 | 0.214286 | 0.352941 | 1.000000 | 0.800000 | 0.888889 | 0.576470 | 0.620915 | `true` | 124.146000 | 17806 | 6 | 6 | 0.152813 |
| ieee-fraud-detection | tc3_fault_injected | generic_agent | try5 | 1.000000 | 0.071429 | 0.133333 | 1.000000 | 0.800000 | 0.888889 | 0.466667 | 0.511111 | `false` | 89.989000 | 16099 | 6 | 6 | 0.139189 |
| ieee-fraud-detection | tc3_fault_injected | proposed_agent | try1 | 0.333333 | 0.142857 | 0.200000 | 1.000000 | 0.600000 | 0.750000 | 0.400000 | 0.475000 | `false` | 194.144000 | 20675 | 5 | 5 | 0.175397 |
| ieee-fraud-detection | tc3_fault_injected | proposed_agent | try2 | 0.600000 | 0.214286 | 0.315789 | 1.000000 | 0.800000 | 0.888889 | 0.557894 | 0.602339 | `true` | 147.464000 | 24167 | 5 | 5 | 0.195352 |
| ieee-fraud-detection | tc3_fault_injected | proposed_agent | try3 | 0.285714 | 0.142857 | 0.190476 | 1.000000 | 0.600000 | 0.750000 | 0.395238 | 0.470238 | `false` | 199.902000 | 21817 | 5 | 5 | 0.186634 |
| ieee-fraud-detection | tc3_fault_injected | proposed_agent | try4 | 0.250000 | 0.071429 | 0.111111 | 1.000000 | 0.600000 | 0.750000 | 0.355555 | 0.430555 | `false` | 187.976000 | 19530 | 5 | 5 | 0.171086 |
| ieee-fraud-detection | tc3_fault_injected | proposed_agent | try5 | 0.250000 | 0.071429 | 0.111111 | 1.000000 | 0.600000 | 0.750000 | 0.355555 | 0.430555 | `false` | 180.961000 | 18499 | 5 | 5 | 0.160541 |
| ieee-fraud-detection | tc3_fault_injected | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.600000 | 0.750000 | 0.300000 | 0.375000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.071429 | 0.133333 | 1.000000 | 0.600000 | 0.750000 | 0.366667 | 0.441667 | `false` | 117.639000 | 2270 | 1 | 0 | 0.685975 |
| ieee-fraud-detection | tc3_fault_injected | single_llm | try2 | 0.666667 | 0.142857 | 0.235294 | 1.000000 | 0.800000 | 0.888889 | 0.517647 | 0.562091 | `true` | 27.645000 | 1790 | 1 | 0 | 0.032713 |
| ieee-fraud-detection | tc3_fault_injected | single_llm | try3 | 0.500000 | 0.071429 | 0.125000 | 1.000000 | 0.800000 | 0.888889 | 0.462500 | 0.506945 | `false` | 30.407000 | 1905 | 1 | 0 | 0.035509 |
| ieee-fraud-detection | tc3_fault_injected | single_llm | try4 | 0.500000 | 0.071429 | 0.125000 | 1.000000 | 0.800000 | 0.888889 | 0.462500 | 0.506945 | `false` | 39.349000 | 2233 | 1 | 0 | 0.040429 |
| ieee-fraud-detection | tc3_fault_injected | single_llm | try5 | 0.500000 | 0.071429 | 0.125000 | 1.000000 | 0.600000 | 0.750000 | 0.362500 | 0.437500 | `false` | 38.072000 | 2256 | 1 | 0 | 0.040774 |
| ieee-fraud-detection | tc4_mixed_history | claude_code | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 136.013307 | 5973 | `null` | 9 | 0.258478 |
| ieee-fraud-detection | tc4_mixed_history | claude_code | try2 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 111.812195 | 4873 | `null` | 8 | 0.231028 |
| ieee-fraud-detection | tc4_mixed_history | claude_code | try3 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 92.648945 | 5795 | `null` | 9 | 0.232383 |
| ieee-fraud-detection | tc4_mixed_history | claude_code | try4 | 0.500000 | 0.125000 | 0.200000 | 1.000000 | 1.000000 | 1.000000 | 0.600000 | 0.600000 | `true` | 105.931256 | 6786 | `null` | 12 | 0.263509 |
| ieee-fraud-detection | tc4_mixed_history | claude_code | try5 | 1.000000 | 0.125000 | 0.222222 | 1.000000 | 1.000000 | 1.000000 | 0.611111 | 0.611111 | `true` | 124.599577 | 7572 | `null` | 12 | 0.312723 |
| ieee-fraud-detection | tc4_mixed_history | generic_agent | try1 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 88.843000 | 13109 | 4 | 5 | 0.112253 |
| ieee-fraud-detection | tc4_mixed_history | generic_agent | try2 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 102.853000 | 16113 | 4 | 5 | 0.124599 |
| ieee-fraud-detection | tc4_mixed_history | generic_agent | try3 | 0.750000 | 0.375000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 72.766000 | 11855 | 5 | 4 | 0.109456 |
| ieee-fraud-detection | tc4_mixed_history | generic_agent | try4 | 0.500000 | 0.125000 | 0.200000 | 1.000000 | 1.000000 | 1.000000 | 0.600000 | 0.600000 | `true` | 95.561000 | 17951 | 6 | 6 | 0.145445 |
| ieee-fraud-detection | tc4_mixed_history | generic_agent | try5 | 0.500000 | 0.250000 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 71.750000 | 13613 | 4 | 5 | 0.109925 |
| ieee-fraud-detection | tc4_mixed_history | proposed_agent | try1 | 0.333333 | 0.250000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 182.470000 | 31547 | 6 | 8 | 0.272875 |
| ieee-fraud-detection | tc4_mixed_history | proposed_agent | try2 | 0.600000 | 0.375000 | 0.461538 | 0.500000 | 1.000000 | 0.666667 | 0.730769 | 0.564102 | `true` | 165.066000 | 28809 | 6 | 8 | 0.253558 |
| ieee-fraud-detection | tc4_mixed_history | proposed_agent | try3 | 0.750000 | 0.375000 | 0.500000 | 1.000000 | 0.500000 | 0.666667 | 0.500000 | 0.583333 | `true` | 104.656000 | 21706 | 5 | 6 | 0.176761 |
| ieee-fraud-detection | tc4_mixed_history | proposed_agent | try4 | 0.750000 | 0.375000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 183.544000 | 31385 | 7 | 9 | 0.257283 |
| ieee-fraud-detection | tc4_mixed_history | proposed_agent | try5 | 0.600000 | 0.375000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 107.153000 | 22335 | 5 | 6 | 0.181493 |
| ieee-fraud-detection | tc4_mixed_history | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.500000 | 0.666667 | 0.250000 | 0.333334 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc4_mixed_history | single_llm | try1 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 251.707000 | 2624 | 1 | 0 | 0.691118 |
| ieee-fraud-detection | tc4_mixed_history | single_llm | try2 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 0.500000 | 0.666667 | 0.431818 | 0.515151 | `false` | 39.469000 | 2284 | 1 | 0 | 0.039955 |
| ieee-fraud-detection | tc4_mixed_history | single_llm | try3 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 35.023000 | 2118 | 1 | 0 | 0.038756 |
| ieee-fraud-detection | tc4_mixed_history | single_llm | try4 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 29.821000 | 1772 | 1 | 0 | 0.033566 |
| ieee-fraud-detection | tc4_mixed_history | single_llm | try5 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 30.891000 | 1781 | 1 | 0 | 0.033701 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ieee-fraud-detection | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.625856 | 0.900000 | 0.727022 | 1.000000 | 1.000000 | 1.000000 | 0.863511 | 0.863511 | 0.000845 | 282.116463 | 13324.600000 | `null` | 14.200000 | 0.422708 |
| ieee-fraud-detection | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.714787 | 0.728572 | 0.717916 | 1.000000 | 1.000000 | 1.000000 | 0.858958 | 0.858958 | 0.000988 | 140.658800 | 26262.600000 | 6.800000 | 7.800000 | 0.244515 |
| ieee-fraud-detection | tc1_from_scratch | human | 1 | `true` | 1.000000 | 0.176471 | 0.214286 | 0.193548 | 1.000000 | 1.000000 | 1.000000 | 0.596774 | 0.596774 | 0.000000 | 1800 | `null` | `null` | `null` | `null` |
| ieee-fraud-detection | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.681517 | 0.742857 | 0.705962 | 1.000000 | 1.000000 | 1.000000 | 0.852981 | 0.852981 | 0.000238 | 124.806400 | 23268.400000 | 4.800000 | 5.400000 | 0.262339 |
| ieee-fraud-detection | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.651384 | 0.771428 | 0.700571 | 1.000000 | 1.000000 | 1.000000 | 0.850286 | 0.850286 | 0.000234 | 55.531800 | 2706.400000 | 1.000000 | 0.000000 | 0.191721 |
| ieee-fraud-detection | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.600000 | 0.200000 | 0.298182 | 1.000000 | 1.000000 | 1.000000 | 0.649091 | 0.649091 | 0.002301 | 124.691308 | 7820.000000 | `null` | 11.600000 | 0.293500 |
| ieee-fraud-detection | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.646667 | 0.325000 | 0.427506 | 1.000000 | 1.000000 | 1.000000 | 0.713753 | 0.713753 | 0.002674 | 105.767200 | 18974.200000 | 5.400000 | 6.800000 | 0.149782 |
| ieee-fraud-detection | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.656191 | 0.450000 | 0.529670 | 0.200000 | 1.000000 | 0.200000 | 0.764835 | 0.364835 | 0.003552 | 199.242600 | 34260.800000 | 6.600000 | 8.000000 | 0.293228 |
| ieee-fraud-detection | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.683333 | 0.325000 | 0.439394 | 0.800000 | 1.000000 | 0.800000 | 0.719697 | 0.619697 | 0.001400 | 62.030400 | 2808.400000 | 1.000000 | 0.000000 | 0.177834 |
| ieee-fraud-detection | tc3_fault_injected | claude_code | 5 | `true` | 0.400000 | 0.500000 | 0.071429 | 0.125000 | 1.000000 | 0.880000 | 0.933333 | 0.502500 | 0.529167 | 0.002400 | 110.261026 | 5910.000000 | `null` | 9.800000 | 0.240256 |
| ieee-fraud-detection | tc3_fault_injected | generic_agent | 5 | `true` | 0.400000 | 1.000000 | 0.157143 | 0.262810 | 1.000000 | 0.800000 | 0.883333 | 0.531405 | 0.573072 | 0.011629 | 102.550000 | 16927.200000 | 5.800000 | 6.000000 | 0.145206 |
| ieee-fraud-detection | tc3_fault_injected | proposed_agent | 5 | `true` | 0.200000 | 0.343809 | 0.128572 | 0.185697 | 1.000000 | 0.640000 | 0.777778 | 0.412848 | 0.481737 | 0.005616 | 182.089400 | 20937.600000 | 5.000000 | 5.000000 | 0.177802 |
| ieee-fraud-detection | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.600000 | 0.750000 | 0.300000 | 0.375000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc3_fault_injected | single_llm | 5 | `true` | 0.200000 | 0.633333 | 0.085715 | 0.148725 | 1.000000 | 0.720000 | 0.833333 | 0.434363 | 0.491030 | 0.003653 | 50.622400 | 2090.800000 | 1.000000 | 0.000000 | 0.167080 |
| ieee-fraud-detection | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 0.833333 | 0.200000 | 0.317172 | 1.000000 | 1.000000 | 1.000000 | 0.658586 | 0.658586 | 0.001931 | 114.201056 | 6199.800000 | `null` | 10.000000 | 0.259624 |
| ieee-fraud-detection | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 0.583333 | 0.250000 | 0.346060 | 1.000000 | 1.000000 | 1.000000 | 0.673030 | 0.673030 | 0.002283 | 86.354600 | 14528.200000 | 4.600000 | 5.000000 | 0.120336 |
| ieee-fraud-detection | tc4_mixed_history | proposed_agent | 5 | `true` | 1.000000 | 0.606667 | 0.350000 | 0.441758 | 0.900000 | 0.900000 | 0.866667 | 0.670879 | 0.654212 | 0.008684 | 148.577800 | 27156.400000 | 5.800000 | 7.400000 | 0.228394 |
| ieee-fraud-detection | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.500000 | 0.666667 | 0.250000 | 0.333334 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| ieee-fraud-detection | tc4_mixed_history | single_llm | 5 | `true` | 0.800000 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 0.900000 | 0.933333 | 0.631818 | 0.648485 | 0.010000 | 77.382200 | 2115.800000 | 1.000000 | 0.000000 | 0.167419 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 0.850000 | 0.639797 | 0.342857 | 0.366844 | 1.000000 | 0.970000 | 0.983333 | 0.668422 | 0.675089 | 0.001869 | 157.817463 | 8313.600000 | `null` | 11.400000 | 0.304022 |
| generic_agent | 4 | 1.000000 | 5.000000 | 0.850000 | 0.736197 | 0.365179 | 0.438573 | 1.000000 | 0.950000 | 0.970833 | 0.694287 | 0.704703 | 0.004393 | 108.832650 | 19173.050000 | 5.650000 | 6.400000 | 0.164960 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 0.176471 | 0.214286 | 0.193548 | 1.000000 | 1.000000 | 1.000000 | 0.596774 | 0.596774 | 0.000000 | 1800.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 0.800000 | 0.572046 | 0.417857 | 0.465772 | 0.775000 | 0.885000 | 0.711111 | 0.675386 | 0.588441 | 0.004523 | 163.679050 | 26405.800000 | 5.550000 | 6.450000 | 0.240441 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.000000 | 0.000000 | 0.000000 | 0.750000 | 0.775000 | 0.604167 | 0.387500 | 0.302084 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 0.750000 | 0.658679 | 0.358036 | 0.413081 | 0.950000 | 0.905000 | 0.891667 | 0.659041 | 0.652374 | 0.003822 | 61.391700 | 2430.350000 | 1.000000 | 0.000000 | 0.176013 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task ieee-fraud-detection --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/ieee-fraud-detection-all.md
```
