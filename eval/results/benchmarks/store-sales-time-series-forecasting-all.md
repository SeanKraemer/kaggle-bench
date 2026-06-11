# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `store-sales-time-series-forecasting`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.904762`
- Mean Add Precision: `0.635569`
- Mean Add Recall: `0.470647`
- Mean Add F1: `0.523913`
- Mean Remove Precision: `0.952381`
- Mean Remove Recall: `0.936508`
- Mean Remove F1: `0.942857`
- Mean Task Completion Score: `0.730210`
- Mean Strict Task Completion Score: `0.733385`
- Mean Task Completion Variance: `0.000910`
- Mean Runtime (s): `182.257419`
- Mean Total Tokens: `6922.287500`
- Mean API Calls: `2.237500`
- Mean Tool Calls: `5.080000`
- Mean Cost (USD): `0.088568`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| store-sales-time-series-forecasting | RMSLE | retail_forecasting | forecasting | multi_table_lookup | xlarge (3000888) | low (17) | medium (16) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| store-sales-time-series-forecasting | 21 | 6 | 0.904762 | 4.047619 | 0.635569 | 0.470647 | 0.523913 | 0.952381 | 0.936508 | 0.942857 | 0.730210 | 0.733385 | 0.000910 | 182.257419 | 6922.287500 | 2.237500 | 5.080000 | 0.088568 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| store-sales-time-series-forecasting | tc1_from_scratch | claude_code | try1 | 0.750000 | 0.692308 | 0.720000 | 1.000000 | 1.000000 | 1.000000 | 0.860000 | 0.860000 | `true` | 117.237378 | 2408 | `null` | 22 | 0.297886 |
| store-sales-time-series-forecasting | tc1_from_scratch | claude_code | try2 | 0.666667 | 0.615385 | 0.640000 | 1.000000 | 1.000000 | 1.000000 | 0.820000 | 0.820000 | `true` | 101.950802 | 2014 | `null` | 15 | 0.196339 |
| store-sales-time-series-forecasting | tc1_from_scratch | claude_code | try3 | 0.818182 | 0.692308 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 128.894580 | 1945 | `null` | 7 | 0.249121 |
| store-sales-time-series-forecasting | tc1_from_scratch | claude_code | try4 | 0.833333 | 0.769231 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 65.494753 | 1820 | `null` | 15 | 0.153096 |
| store-sales-time-series-forecasting | tc1_from_scratch | claude_code | try5 | 0.818182 | 0.692308 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 114.352778 | 2394 | `null` | 22 | 0.238689 |
| store-sales-time-series-forecasting | tc1_from_scratch | generic_agent | try1 | 0.615385 | 0.615385 | 0.615385 | 1.000000 | 1.000000 | 1.000000 | 0.807692 | 0.807692 | `true` | 76.012000 | 15342 | 5 | 5 | 0.149200 |
| store-sales-time-series-forecasting | tc1_from_scratch | generic_agent | try2 | 0.615385 | 0.615385 | 0.615385 | 1.000000 | 1.000000 | 1.000000 | 0.807692 | 0.807692 | `true` | 59.166000 | 9997 | 4 | 4 | 0.083803 |
| store-sales-time-series-forecasting | tc1_from_scratch | generic_agent | try3 | 0.727273 | 0.615385 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 60.885000 | 9451 | 4 | 5 | 0.080227 |
| store-sales-time-series-forecasting | tc1_from_scratch | generic_agent | try4 | 0.666667 | 0.615385 | 0.640000 | 1.000000 | 1.000000 | 1.000000 | 0.820000 | 0.820000 | `true` | 63.461000 | 8363 | 3 | 3 | 0.073299 |
| store-sales-time-series-forecasting | tc1_from_scratch | generic_agent | try5 | 0.692308 | 0.692308 | 0.692308 | 1.000000 | 1.000000 | 1.000000 | 0.846154 | 0.846154 | `true` | 73.817000 | 13623 | 5 | 5 | 0.106565 |
| store-sales-time-series-forecasting | tc1_from_scratch | human | human_tc1_v1 | 1.000000 | 0.692308 | 0.818182 | 1.000000 | 1.000000 | 1.000000 | 0.909091 | 0.909091 | `true` | 2700 | `null` | `null` | `null` | `null` |
| store-sales-time-series-forecasting | tc1_from_scratch | proposed_agent | try1 | 0.571429 | 0.615385 | 0.592593 | 1.000000 | 1.000000 | 1.000000 | 0.796296 | 0.796296 | `true` | 85.588000 | 11015 | 3 | 2 | 0.134120 |
| store-sales-time-series-forecasting | tc1_from_scratch | proposed_agent | try2 | 0.692308 | 0.692308 | 0.692308 | 1.000000 | 1.000000 | 1.000000 | 0.846154 | 0.846154 | `true` | 63.311000 | 7867 | 3 | 2 | 0.076298 |
| store-sales-time-series-forecasting | tc1_from_scratch | proposed_agent | try3 | 0.642857 | 0.692308 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 71.057000 | 12478 | 4 | 3 | 0.094895 |
| store-sales-time-series-forecasting | tc1_from_scratch | proposed_agent | try4 | 0.642857 | 0.692308 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 94.658000 | 14648 | 4 | 4 | 0.120245 |
| store-sales-time-series-forecasting | tc1_from_scratch | proposed_agent | try5 | 0.571429 | 0.615385 | 0.592593 | 1.000000 | 1.000000 | 1.000000 | 0.796296 | 0.796296 | `true` | 88.030000 | 15861 | 4 | 4 | 0.118748 |
| store-sales-time-series-forecasting | tc1_from_scratch | rule_based | try1 | 0.400000 | 0.307692 | 0.347826 | 1.000000 | 1.000000 | 1.000000 | 0.673913 | 0.673913 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| store-sales-time-series-forecasting | tc1_from_scratch | single_llm | try1 | 0.692308 | 0.692308 | 0.692308 | 1.000000 | 1.000000 | 1.000000 | 0.846154 | 0.846154 | `true` | 12.870000 | 811 | 1 | 0 | 0.045154 |
| store-sales-time-series-forecasting | tc1_from_scratch | single_llm | try2 | 0.692308 | 0.692308 | 0.692308 | 1.000000 | 1.000000 | 1.000000 | 0.846154 | 0.846154 | `true` | 13.944000 | 772 | 1 | 0 | 0.014360 |
| store-sales-time-series-forecasting | tc1_from_scratch | single_llm | try3 | 0.692308 | 0.692308 | 0.692308 | 1.000000 | 1.000000 | 1.000000 | 0.846154 | 0.846154 | `true` | 14.398000 | 811 | 1 | 0 | 0.014945 |
| store-sales-time-series-forecasting | tc1_from_scratch | single_llm | try4 | 0.692308 | 0.692308 | 0.692308 | 1.000000 | 1.000000 | 1.000000 | 0.846154 | 0.846154 | `true` | 12.510000 | 745 | 1 | 0 | 0.013955 |
| store-sales-time-series-forecasting | tc1_from_scratch | single_llm | try5 | 0.692308 | 0.692308 | 0.692308 | 1.000000 | 1.000000 | 1.000000 | 0.846154 | 0.846154 | `true` | 13.959000 | 799 | 1 | 0 | 0.014765 |
| store-sales-time-series-forecasting | tc2_partial_good | claude_code | try1 | 0.750000 | 0.300000 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | `true` | 71.060915 | 1485 | `null` | 13 | 0.158790 |
| store-sales-time-series-forecasting | tc2_partial_good | claude_code | try2 | 0.500000 | 0.200000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 53.454684 | 1789 | `null` | 13 | 0.124730 |
| store-sales-time-series-forecasting | tc2_partial_good | claude_code | try3 | 0.750000 | 0.600000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 104.467890 | 2122 | `null` | 20 | 0.219028 |
| store-sales-time-series-forecasting | tc2_partial_good | claude_code | try4 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 323.992875 | 1917 | `null` | 33 | 0.481711 |
| store-sales-time-series-forecasting | tc2_partial_good | claude_code | try5 | 0.500000 | 0.300000 | 0.375000 | 1.000000 | 1.000000 | 1.000000 | 0.687500 | 0.687500 | `true` | 75.304329 | 1844 | `null` | 19 | 0.132410 |
| store-sales-time-series-forecasting | tc2_partial_good | generic_agent | try1 | 0.714286 | 0.500000 | 0.588235 | 1.000000 | 1.000000 | 1.000000 | 0.794118 | 0.794118 | `true` | 37.232000 | 5225 | 3 | 3 | 0.047651 |
| store-sales-time-series-forecasting | tc2_partial_good | generic_agent | try2 | 0.500000 | 0.400000 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 71.472000 | 11339 | 5 | 6 | 0.097826 |
| store-sales-time-series-forecasting | tc2_partial_good | generic_agent | try3 | 0.625000 | 0.500000 | 0.555556 | 1.000000 | 1.000000 | 1.000000 | 0.777778 | 0.777778 | `true` | 64.935000 | 10397 | 4 | 7 | 0.084881 |
| store-sales-time-series-forecasting | tc2_partial_good | generic_agent | try4 | 0.625000 | 0.500000 | 0.555556 | 1.000000 | 1.000000 | 1.000000 | 0.777778 | 0.777778 | `true` | 74.858000 | 10782 | 4 | 5 | 0.092937 |
| store-sales-time-series-forecasting | tc2_partial_good | generic_agent | try5 | 0.571429 | 0.400000 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | `true` | 72.158000 | 14337 | 4 | 5 | 0.100942 |
| store-sales-time-series-forecasting | tc2_partial_good | proposed_agent | try1 | 0.500000 | 0.500000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 68.673000 | 8876 | 3 | 2 | 0.084652 |
| store-sales-time-series-forecasting | tc2_partial_good | proposed_agent | try2 | 0.600000 | 0.600000 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 79.485000 | 12843 | 4 | 4 | 0.103454 |
| store-sales-time-series-forecasting | tc2_partial_good | proposed_agent | try3 | 0.555556 | 0.500000 | 0.526316 | 1.000000 | 1.000000 | 1.000000 | 0.763158 | 0.763158 | `true` | 93.284000 | 14102 | 4 | 4 | 0.109487 |
| store-sales-time-series-forecasting | tc2_partial_good | proposed_agent | try4 | 0.555556 | 0.500000 | 0.526316 | 1.000000 | 1.000000 | 1.000000 | 0.763158 | 0.763158 | `true` | 80.996000 | 12250 | 4 | 4 | 0.098465 |
| store-sales-time-series-forecasting | tc2_partial_good | proposed_agent | try5 | 0.666667 | 0.600000 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 72.518000 | 12430 | 4 | 4 | 0.097511 |
| store-sales-time-series-forecasting | tc2_partial_good | rule_based | try1 | 0.333333 | 0.300000 | 0.315789 | 1.000000 | 1.000000 | 1.000000 | 0.657895 | 0.657895 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| store-sales-time-series-forecasting | tc2_partial_good | single_llm | try1 | 0.777778 | 0.700000 | 0.736842 | 1.000000 | 1.000000 | 1.000000 | 0.868421 | 0.868421 | `true` | 38.911000 | 2327 | 1 | 0 | 0.036898 |
| store-sales-time-series-forecasting | tc2_partial_good | single_llm | try2 | 0.500000 | 0.500000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 38.501000 | 2216 | 1 | 0 | 0.036084 |
| store-sales-time-series-forecasting | tc2_partial_good | single_llm | try3 | 0.666667 | 0.600000 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 37.826000 | 2216 | 1 | 0 | 0.036084 |
| store-sales-time-series-forecasting | tc2_partial_good | single_llm | try4 | 0.666667 | 0.600000 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 34.827000 | 2006 | 1 | 0 | 0.032934 |
| store-sales-time-series-forecasting | tc2_partial_good | single_llm | try5 | 0.666667 | 0.600000 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 37.918000 | 2311 | 1 | 0 | 0.037509 |
| store-sales-time-series-forecasting | tc3_fault_injected | claude_code | try1 | 0.666667 | 0.166667 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | `true` | 45.905643 | 1497 | `null` | 15 | 0.122006 |
| store-sales-time-series-forecasting | tc3_fault_injected | claude_code | try2 | 0.666667 | 0.166667 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | `true` | 80.660142 | 1684 | `null` | 8 | 0.172351 |
| store-sales-time-series-forecasting | tc3_fault_injected | claude_code | try3 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 93.906740 | 2361 | `null` | 24 | 0.301416 |
| store-sales-time-series-forecasting | tc3_fault_injected | claude_code | try4 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 58.650073 | 1468 | `null` | 8 | 0.124303 |
| store-sales-time-series-forecasting | tc3_fault_injected | claude_code | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 196.667027 | 1405 | `null` | 23 | 0.420281 |
| store-sales-time-series-forecasting | tc3_fault_injected | generic_agent | try1 | 0.666667 | 0.166667 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | `true` | 40.918000 | 6075 | 3 | 4 | 0.052049 |
| store-sales-time-series-forecasting | tc3_fault_injected | generic_agent | try2 | 0.666667 | 0.166667 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | `true` | 37.364000 | 6230 | 3 | 3 | 0.051278 |
| store-sales-time-series-forecasting | tc3_fault_injected | generic_agent | try3 | 0.666667 | 0.166667 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | `true` | 35.573000 | 5892 | 3 | 3 | 0.047869 |
| store-sales-time-series-forecasting | tc3_fault_injected | generic_agent | try4 | 0.666667 | 0.166667 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | `true` | 43.605000 | 6158 | 3 | 3 | 0.051500 |
| store-sales-time-series-forecasting | tc3_fault_injected | generic_agent | try5 | 0.666667 | 0.166667 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | `true` | 44.534000 | 7202 | 3 | 4 | 0.057535 |
| store-sales-time-series-forecasting | tc3_fault_injected | proposed_agent | try1 | 0.714286 | 0.416667 | 0.526316 | 1.000000 | 1.000000 | 1.000000 | 0.763158 | 0.763158 | `true` | 112.291000 | 14604 | 5 | 6 | 0.122814 |
| store-sales-time-series-forecasting | tc3_fault_injected | proposed_agent | try2 | 0.727273 | 0.666667 | 0.695652 | 1.000000 | 1.000000 | 1.000000 | 0.847826 | 0.847826 | `true` | 121.245000 | 24608 | 6 | 9 | 0.184208 |
| store-sales-time-series-forecasting | tc3_fault_injected | proposed_agent | try3 | 0.800000 | 0.666667 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | `true` | 107.644000 | 19910 | 4 | 4 | 0.146495 |
| store-sales-time-series-forecasting | tc3_fault_injected | proposed_agent | try4 | 0.700000 | 0.583333 | 0.636364 | 1.000000 | 1.000000 | 1.000000 | 0.818182 | 0.818182 | `true` | 91.331000 | 14721 | 4 | 4 | 0.115456 |
| store-sales-time-series-forecasting | tc3_fault_injected | proposed_agent | try5 | 0.625000 | 0.416667 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 123.188000 | 18040 | 6 | 7 | 0.145187 |
| store-sales-time-series-forecasting | tc3_fault_injected | rule_based | try1 | 0.333333 | 0.250000 | 0.285714 | 1.000000 | 0.666667 | 0.800000 | 0.476191 | 0.542857 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| store-sales-time-series-forecasting | tc3_fault_injected | single_llm | try1 | 0.777778 | 0.583333 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 33.787000 | 2193 | 1 | 0 | 0.034792 |
| store-sales-time-series-forecasting | tc3_fault_injected | single_llm | try2 | 0.800000 | 0.666667 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | `true` | 37.969000 | 2371 | 1 | 0 | 0.038439 |
| store-sales-time-series-forecasting | tc3_fault_injected | single_llm | try3 | 0.636364 | 0.583333 | 0.608696 | 1.000000 | 1.000000 | 1.000000 | 0.804348 | 0.804348 | `true` | 36.375000 | 2308 | 1 | 0 | 0.037494 |
| store-sales-time-series-forecasting | tc3_fault_injected | single_llm | try4 | 0.750000 | 0.500000 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 39.514000 | 2341 | 1 | 0 | 0.037989 |
| store-sales-time-series-forecasting | tc3_fault_injected | single_llm | try5 | 0.777778 | 0.583333 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 31.317000 | 1985 | 1 | 0 | 0.032649 |
| store-sales-time-series-forecasting | tc4_mixed_history | claude_code | try1 | 1.000000 | 0.300000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 70.732392 | 1819 | `null` | 8 | 0.159353 |
| store-sales-time-series-forecasting | tc4_mixed_history | claude_code | try2 | 0.400000 | 0.200000 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | `true` | 75.531972 | 2018 | `null` | 19 | 0.183576 |
| store-sales-time-series-forecasting | tc4_mixed_history | claude_code | try3 | 0.750000 | 0.300000 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | `true` | 85.002691 | 2905 | `null` | 14 | 0.202928 |
| store-sales-time-series-forecasting | tc4_mixed_history | claude_code | try4 | 0.500000 | 0.300000 | 0.375000 | 1.000000 | 1.000000 | 1.000000 | 0.687500 | 0.687500 | `true` | 76.589742 | 1941 | `null` | 21 | 0.160747 |
| store-sales-time-series-forecasting | tc4_mixed_history | claude_code | try5 | 0.400000 | 0.200000 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | `true` | 91.810572 | 1610 | `null` | 15 | 0.172124 |
| store-sales-time-series-forecasting | tc4_mixed_history | generic_agent | try1 | 0.666667 | 0.200000 | 0.307692 | 1.000000 | 1.000000 | 1.000000 | 0.653846 | 0.653846 | `true` | 46.387000 | 6778 | 3 | 3 | 0.057182 |
| store-sales-time-series-forecasting | tc4_mixed_history | generic_agent | try2 | 0.666667 | 0.400000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 60.951000 | 11009 | 5 | 6 | 0.087915 |
| store-sales-time-series-forecasting | tc4_mixed_history | generic_agent | try3 | 0.833333 | 0.500000 | 0.625000 | 1.000000 | 1.000000 | 1.000000 | 0.812500 | 0.812500 | `true` | 60.591000 | 9156 | 4 | 5 | 0.077780 |
| store-sales-time-series-forecasting | tc4_mixed_history | generic_agent | try4 | 0.833333 | 0.500000 | 0.625000 | 1.000000 | 1.000000 | 1.000000 | 0.812500 | 0.812500 | `true` | 50.771000 | 8229 | 4 | 4 | 0.070327 |
| store-sales-time-series-forecasting | tc4_mixed_history | generic_agent | try5 | 0.857143 | 0.600000 | 0.705882 | 1.000000 | 1.000000 | 1.000000 | 0.852941 | 0.852941 | `true` | 59.110000 | 8741 | 3 | 4 | 0.072449 |
| store-sales-time-series-forecasting | tc4_mixed_history | proposed_agent | try1 | 0.666667 | 0.600000 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 117.666000 | 21365 | 6 | 8 | 0.168496 |
| store-sales-time-series-forecasting | tc4_mixed_history | proposed_agent | try2 | 0.777778 | 0.700000 | 0.736842 | 1.000000 | 1.000000 | 1.000000 | 0.868421 | 0.868421 | `true` | 99.380000 | 14969 | 4 | 4 | 0.122096 |
| store-sales-time-series-forecasting | tc4_mixed_history | proposed_agent | try3 | 0.700000 | 0.700000 | 0.700000 | 1.000000 | 1.000000 | 1.000000 | 0.850000 | 0.850000 | `true` | 92.971000 | 10367 | 3 | 2 | 0.100561 |
| store-sales-time-series-forecasting | tc4_mixed_history | proposed_agent | try4 | 0.777778 | 0.700000 | 0.736842 | 1.000000 | 1.000000 | 1.000000 | 0.868421 | 0.868421 | `true` | 99.797000 | 15246 | 4 | 4 | 0.121604 |
| store-sales-time-series-forecasting | tc4_mixed_history | proposed_agent | try5 | 0.666667 | 0.600000 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 96.558000 | 18310 | 5 | 6 | 0.146128 |
| store-sales-time-series-forecasting | tc4_mixed_history | rule_based | try1 | 0.333333 | 0.300000 | 0.315789 | 0.000000 | 0.000000 | 0.000000 | 0.157894 | 0.157894 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| store-sales-time-series-forecasting | tc4_mixed_history | single_llm | try1 | 0.625000 | 0.500000 | 0.555556 | 1.000000 | 1.000000 | 1.000000 | 0.777778 | 0.777778 | `true` | 34.298000 | 2020 | 1 | 0 | 0.032174 |
| store-sales-time-series-forecasting | tc4_mixed_history | single_llm | try2 | 0.714286 | 0.500000 | 0.588235 | 1.000000 | 1.000000 | 1.000000 | 0.794118 | 0.794118 | `true` | 33.389000 | 1958 | 1 | 0 | 0.032251 |
| store-sales-time-series-forecasting | tc4_mixed_history | single_llm | try3 | 0.625000 | 0.500000 | 0.555556 | 1.000000 | 1.000000 | 1.000000 | 0.777778 | 0.777778 | `true` | 37.221000 | 2121 | 1 | 0 | 0.034696 |
| store-sales-time-series-forecasting | tc4_mixed_history | single_llm | try4 | 0.600000 | 0.600000 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 40.016000 | 2297 | 1 | 0 | 0.037337 |
| store-sales-time-series-forecasting | tc4_mixed_history | single_llm | try5 | 0.555556 | 0.500000 | 0.526316 | 1.000000 | 1.000000 | 1.000000 | 0.763158 | 0.763158 | `true` | 32.340000 | 1893 | 1 | 0 | 0.031276 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| store-sales-time-series-forecasting | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.777273 | 0.692308 | 0.732000 | 1.000000 | 1.000000 | 1.000000 | 0.866000 | 0.866000 | 0.000694 | 105.586058 | 2116.200000 | `null` | 16.200000 | 0.227026 |
| store-sales-time-series-forecasting | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.663404 | 0.630770 | 0.645949 | 1.000000 | 1.000000 | 1.000000 | 0.822974 | 0.822974 | 0.000224 | 66.668200 | 11355.200000 | 4.200000 | 4.400000 | 0.098619 |
| store-sales-time-series-forecasting | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 0.692308 | 0.818182 | 1.000000 | 1.000000 | 1.000000 | 0.909091 | 0.909091 | 0.000000 | 2700 | `null` | `null` | `null` | `null` |
| store-sales-time-series-forecasting | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.624176 | 0.661539 | 0.642166 | 1.000000 | 1.000000 | 1.000000 | 0.821082 | 0.821082 | 0.000431 | 80.528800 | 12373.800000 | 3.600000 | 3.000000 | 0.108861 |
| store-sales-time-series-forecasting | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.400000 | 0.307692 | 0.347826 | 1.000000 | 1.000000 | 1.000000 | 0.673913 | 0.673913 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| store-sales-time-series-forecasting | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.692308 | 0.692308 | 0.692308 | 1.000000 | 1.000000 | 1.000000 | 0.846154 | 0.846154 | 0.000000 | 13.536200 | 787.600000 | 1.000000 | 0.000000 | 0.020636 |
| store-sales-time-series-forecasting | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.633333 | 0.360000 | 0.451190 | 1.000000 | 1.000000 | 1.000000 | 0.725595 | 0.725595 | 0.004126 | 125.656138 | 1831.400000 | `null` | 19.600000 | 0.223334 |
| store-sales-time-series-forecasting | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.607143 | 0.460000 | 0.522876 | 1.000000 | 1.000000 | 1.000000 | 0.761438 | 0.761438 | 0.000765 | 64.131000 | 10416.000000 | 4.000000 | 5.200000 | 0.084847 |
| store-sales-time-series-forecasting | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.575556 | 0.540000 | 0.556842 | 1.000000 | 1.000000 | 1.000000 | 0.778421 | 0.778421 | 0.000627 | 78.991200 | 12100.200000 | 3.800000 | 3.600000 | 0.098714 |
| store-sales-time-series-forecasting | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.333333 | 0.300000 | 0.315789 | 1.000000 | 1.000000 | 1.000000 | 0.657895 | 0.657895 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| store-sales-time-series-forecasting | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.655556 | 0.600000 | 0.626316 | 1.000000 | 1.000000 | 1.000000 | 0.813158 | 0.813158 | 0.001413 | 37.596600 | 2215.200000 | 1.000000 | 0.000000 | 0.035902 |
| store-sales-time-series-forecasting | tc3_fault_injected | claude_code | 5 | `true` | 1.000000 | 0.866667 | 0.216667 | 0.346667 | 1.000000 | 1.000000 | 1.000000 | 0.673333 | 0.673333 | 0.001067 | 95.157925 | 1683.000000 | `null` | 15.600000 | 0.228071 |
| store-sales-time-series-forecasting | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 0.666667 | 0.166667 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | 0.000000 | 40.398800 | 6311.400000 | 3.000000 | 3.400000 | 0.052046 |
| store-sales-time-series-forecasting | tc3_fault_injected | proposed_agent | 5 | `true` | 1.000000 | 0.713312 | 0.550000 | 0.617121 | 1.000000 | 1.000000 | 1.000000 | 0.808560 | 0.808560 | 0.002032 | 111.139800 | 18376.600000 | 5.000000 | 6.000000 | 0.142832 |
| store-sales-time-series-forecasting | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.333333 | 0.250000 | 0.285714 | 1.000000 | 0.666667 | 0.800000 | 0.476191 | 0.542857 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| store-sales-time-series-forecasting | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 0.748384 | 0.583333 | 0.653861 | 1.000000 | 1.000000 | 1.000000 | 0.826930 | 0.826930 | 0.000533 | 35.792400 | 2239.600000 | 1.000000 | 0.000000 | 0.036273 |
| store-sales-time-series-forecasting | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 0.610000 | 0.260000 | 0.359689 | 1.000000 | 1.000000 | 1.000000 | 0.679844 | 0.679844 | 0.001633 | 79.933474 | 2058.600000 | `null` | 15.400000 | 0.175745 |
| store-sales-time-series-forecasting | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 0.771429 | 0.440000 | 0.552715 | 1.000000 | 1.000000 | 1.000000 | 0.776357 | 0.776357 | 0.004836 | 55.562000 | 8782.600000 | 3.800000 | 4.400000 | 0.073130 |
| store-sales-time-series-forecasting | tc4_mixed_history | proposed_agent | 5 | `true` | 1.000000 | 0.717778 | 0.660000 | 0.687368 | 1.000000 | 1.000000 | 1.000000 | 0.843684 | 0.843684 | 0.000564 | 101.274400 | 16051.400000 | 4.400000 | 4.800000 | 0.131777 |
| store-sales-time-series-forecasting | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.333333 | 0.300000 | 0.315789 | 0.000000 | 0.000000 | 0.000000 | 0.157894 | 0.157894 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| store-sales-time-series-forecasting | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 0.623968 | 0.520000 | 0.565133 | 1.000000 | 1.000000 | 1.000000 | 0.782566 | 0.782566 | 0.000172 | 35.452800 | 2057.800000 | 1.000000 | 0.000000 | 0.033547 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 1.000000 | 0.721818 | 0.382244 | 0.472386 | 1.000000 | 1.000000 | 1.000000 | 0.736193 | 0.736193 | 0.001880 | 101.583399 | 1922.300000 | `null` | 16.700000 | 0.213544 |
| generic_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.677161 | 0.424359 | 0.497052 | 1.000000 | 1.000000 | 1.000000 | 0.748525 | 0.748525 | 0.001456 | 56.690000 | 9216.300000 | 3.750000 | 4.350000 | 0.077161 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.692308 | 0.818182 | 1.000000 | 1.000000 | 1.000000 | 0.909091 | 0.909091 | 0.000000 | 2700.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.657705 | 0.602885 | 0.625874 | 1.000000 | 1.000000 | 1.000000 | 0.812937 | 0.812937 | 0.000914 | 92.983550 | 14725.500000 | 4.200000 | 4.350000 | 0.120546 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.350000 | 0.289423 | 0.316279 | 0.750000 | 0.666667 | 0.700000 | 0.491473 | 0.508140 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 0.680054 | 0.598910 | 0.634405 | 1.000000 | 1.000000 | 1.000000 | 0.817202 | 0.817202 | 0.000530 | 30.594500 | 1825.050000 | 1.000000 | 0.000000 | 0.031589 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task store-sales-time-series-forecasting --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/store-sales-time-series-forecasting-all.md
```
