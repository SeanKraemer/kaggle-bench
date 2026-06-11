# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `competitive-data-science-predict-future-sales`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.904762`
- Mean Add Precision: `0.789126`
- Mean Add Recall: `0.466148`
- Mean Add F1: `0.548127`
- Mean Remove Precision: `0.857143`
- Mean Remove Recall: `0.861111`
- Mean Remove F1: `0.830476`
- Mean Task Completion Score: `0.704619`
- Mean Strict Task Completion Score: `0.689302`
- Mean Task Completion Variance: `0.002045`
- Mean Runtime (s): `234.557168`
- Mean Total Tokens: `9787.287500`
- Mean API Calls: `2.412500`
- Mean Tool Calls: `3.360000`
- Mean Cost (USD): `0.099071`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| competitive-data-science-predict-future-sales | RMSE | retail_time_series_tabular | forecasting | multi_table_relational | xlarge (2935849) | low (12) | medium (13) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| competitive-data-science-predict-future-sales | 21 | 6 | 0.904762 | 4.047619 | 0.789126 | 0.466148 | 0.548127 | 0.857143 | 0.861111 | 0.830476 | 0.704619 | 0.689302 | 0.002045 | 234.557168 | 9787.287500 | 2.412500 | 3.360000 | 0.099071 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| competitive-data-science-predict-future-sales | tc1_from_scratch | claude_code | try1 | 0.750000 | 0.923077 | 0.827586 | 1.000000 | 1.000000 | 1.000000 | 0.913793 | 0.913793 | `true` | 134.395601 | 7827 | `null` | 8 | 0.237646 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | claude_code | try2 | 0.785714 | 0.846154 | 0.814815 | 1.000000 | 1.000000 | 1.000000 | 0.907407 | 0.907407 | `true` | 197.581829 | 10704 | `null` | 9 | 0.290371 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | claude_code | try3 | 0.750000 | 0.923077 | 0.827586 | 1.000000 | 1.000000 | 1.000000 | 0.913793 | 0.913793 | `true` | 184.062624 | 9142 | `null` | 8 | 0.260391 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | claude_code | try4 | 0.857143 | 0.923077 | 0.888889 | 1.000000 | 1.000000 | 1.000000 | 0.944445 | 0.944445 | `true` | 220.136042 | 11024 | `null` | 10 | 0.305298 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | claude_code | try5 | 0.631579 | 0.923077 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 155.149965 | 10309 | `null` | 9 | 0.283151 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | generic_agent | try1 | 0.733333 | 0.846154 | 0.785714 | 1.000000 | 1.000000 | 1.000000 | 0.892857 | 0.892857 | `true` | 92.352000 | 18512 | 5 | 6 | 0.155600 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | generic_agent | try2 | 0.750000 | 0.923077 | 0.827586 | 1.000000 | 1.000000 | 1.000000 | 0.913793 | 0.913793 | `true` | 121.053000 | 21749 | 5 | 6 | 0.151200 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | generic_agent | try3 | 0.875000 | 0.538462 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 95.508000 | 20255 | 5 | 6 | 0.135481 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | generic_agent | try4 | 0.700000 | 0.538462 | 0.608696 | 1.000000 | 1.000000 | 1.000000 | 0.804348 | 0.804348 | `true` | 66.034000 | 11112 | 4 | 5 | 0.087389 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | generic_agent | try5 | 0.916667 | 0.846154 | 0.880000 | 1.000000 | 1.000000 | 1.000000 | 0.940000 | 0.940000 | `true` | 83.100000 | 17883 | 5 | 6 | 0.132997 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | human | human_tc1_annotator_c_v1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 3600 | `null` | `null` | `null` | `null` |
| competitive-data-science-predict-future-sales | tc1_from_scratch | proposed_agent | try1 | 0.733333 | 0.846154 | 0.785714 | 1.000000 | 1.000000 | 1.000000 | 0.892857 | 0.892857 | `true` | 103.598000 | 15649 | 4 | 4 | 0.167497 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | proposed_agent | try2 | 0.647059 | 0.846154 | 0.733333 | 1.000000 | 1.000000 | 1.000000 | 0.866667 | 0.866667 | `true` | 102.879000 | 17693 | 4 | 4 | 0.128728 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | proposed_agent | try3 | 0.687500 | 0.846154 | 0.758621 | 1.000000 | 1.000000 | 1.000000 | 0.879310 | 0.879310 | `true` | 122.192000 | 25347 | 5 | 6 | 0.178762 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | proposed_agent | try4 | 0.687500 | 0.846154 | 0.758621 | 1.000000 | 1.000000 | 1.000000 | 0.879310 | 0.879310 | `true` | 97.262000 | 19924 | 6 | 7 | 0.153426 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | proposed_agent | try5 | 0.750000 | 0.923077 | 0.827586 | 1.000000 | 1.000000 | 1.000000 | 0.913793 | 0.913793 | `true` | 136.548000 | 25550 | 5 | 6 | 0.189571 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | rule_based | try1 | 0.750000 | 0.230769 | 0.352941 | 1.000000 | 1.000000 | 1.000000 | 0.676470 | 0.676470 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | single_llm | try1 | 0.636364 | 0.538462 | 0.583333 | 1.000000 | 1.000000 | 1.000000 | 0.791667 | 0.791667 | `true` | 14.888000 | 944 | 1 | 0 | 0.046050 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | single_llm | try2 | 0.769231 | 0.769231 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 17.918000 | 1081 | 1 | 0 | 0.048105 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | single_llm | try3 | 0.714286 | 0.769231 | 0.740741 | 1.000000 | 1.000000 | 1.000000 | 0.870370 | 0.870370 | `true` | 16.390000 | 983 | 1 | 0 | 0.046635 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | single_llm | try4 | 0.769231 | 0.769231 | 0.769231 | 1.000000 | 1.000000 | 1.000000 | 0.884615 | 0.884615 | `true` | 14.989000 | 917 | 1 | 0 | 0.045645 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | single_llm | try5 | 0.700000 | 0.538462 | 0.608696 | 1.000000 | 1.000000 | 1.000000 | 0.804348 | 0.804348 | `true` | 12.362000 | 748 | 1 | 0 | 0.013912 |
| competitive-data-science-predict-future-sales | tc2_partial_good | claude_code | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 99.419012 | 5385 | `null` | 10 | 0.213979 |
| competitive-data-science-predict-future-sales | tc2_partial_good | claude_code | try2 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 121.412795 | 5909 | `null` | 9 | 0.217558 |
| competitive-data-science-predict-future-sales | tc2_partial_good | claude_code | try3 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 151.422773 | 6600 | `null` | 8 | 0.227909 |
| competitive-data-science-predict-future-sales | tc2_partial_good | claude_code | try4 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 106.366078 | 5009 | `null` | 8 | 0.182810 |
| competitive-data-science-predict-future-sales | tc2_partial_good | claude_code | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 139.269442 | 5730 | `null` | 11 | 0.245667 |
| competitive-data-science-predict-future-sales | tc2_partial_good | generic_agent | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 53.967000 | 8348 | 3 | 3 | 0.064661 |
| competitive-data-science-predict-future-sales | tc2_partial_good | generic_agent | try2 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 41.268000 | 6931 | 3 | 2 | 0.056102 |
| competitive-data-science-predict-future-sales | tc2_partial_good | generic_agent | try3 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 57.428000 | 8888 | 3 | 3 | 0.071076 |
| competitive-data-science-predict-future-sales | tc2_partial_good | generic_agent | try4 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 61.154000 | 7877 | 4 | 3 | 0.069880 |
| competitive-data-science-predict-future-sales | tc2_partial_good | generic_agent | try5 | 1.000000 | 0.375000 | 0.545455 | 1.000000 | 1.000000 | 1.000000 | 0.772728 | 0.772728 | `true` | 67.461000 | 9924 | 4 | 4 | 0.087859 |
| competitive-data-science-predict-future-sales | tc2_partial_good | proposed_agent | try1 | 0.428571 | 0.375000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 71.517000 | 8561 | 3 | 2 | 0.084787 |
| competitive-data-science-predict-future-sales | tc2_partial_good | proposed_agent | try2 | 0.666667 | 0.250000 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 91.089000 | 18269 | 5 | 5 | 0.134996 |
| competitive-data-science-predict-future-sales | tc2_partial_good | proposed_agent | try3 | 0.333333 | 0.250000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 81.141000 | 14928 | 4 | 4 | 0.111181 |
| competitive-data-science-predict-future-sales | tc2_partial_good | proposed_agent | try4 | 0.333333 | 0.250000 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 101.941000 | 17544 | 5 | 5 | 0.134026 |
| competitive-data-science-predict-future-sales | tc2_partial_good | proposed_agent | try5 | 0.428571 | 0.375000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 90.069000 | 14970 | 4 | 4 | 0.119503 |
| competitive-data-science-predict-future-sales | tc2_partial_good | rule_based | try1 | 0.666667 | 0.250000 | 0.363636 | 0.000000 | 1.000000 | 0.000000 | 0.681818 | 0.181818 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| competitive-data-science-predict-future-sales | tc2_partial_good | single_llm | try1 | 0.428571 | 0.375000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 40.321000 | 2565 | 1 | 0 | 0.040237 |
| competitive-data-science-predict-future-sales | tc2_partial_good | single_llm | try2 | 0.500000 | 0.375000 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | `true` | 37.951000 | 2161 | 1 | 0 | 0.034177 |
| competitive-data-science-predict-future-sales | tc2_partial_good | single_llm | try3 | 0.600000 | 0.375000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 33.290000 | 1957 | 1 | 0 | 0.031117 |
| competitive-data-science-predict-future-sales | tc2_partial_good | single_llm | try4 | 0.400000 | 0.250000 | 0.307692 | 1.000000 | 1.000000 | 1.000000 | 0.653846 | 0.653846 | `true` | 37.955000 | 2197 | 1 | 0 | 0.034717 |
| competitive-data-science-predict-future-sales | tc2_partial_good | single_llm | try5 | 0.500000 | 0.375000 | 0.428571 | 1.000000 | 1.000000 | 1.000000 | 0.714286 | 0.714286 | `true` | 37.432000 | 2197 | 1 | 0 | 0.035756 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | claude_code | try1 | 1.000000 | 0.153846 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | `true` | 90.473493 | 4235 | `null` | 6 | 0.168386 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | claude_code | try2 | 1.000000 | 0.307692 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | `true` | 70.097500 | 4476 | `null` | 6 | 0.164113 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | claude_code | try3 | 1.000000 | 0.230769 | 0.375000 | 1.000000 | 1.000000 | 1.000000 | 0.687500 | 0.687500 | `true` | 89.851853 | 4280 | `null` | 5 | 0.152677 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | claude_code | try4 | 1.000000 | 0.307692 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | `true` | 106.069322 | 5350 | `null` | 5 | 0.180683 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | claude_code | try5 | 1.000000 | 0.153846 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | `true` | 87.826207 | 5301 | `null` | 8 | 0.190049 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.384615 | 0.555556 | 1.000000 | 0.500000 | 0.666667 | 0.527778 | 0.611112 | `true` | 99.514000 | 17837 | 4 | 4 | 0.141032 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | generic_agent | try2 | 1.000000 | 0.307692 | 0.470588 | 1.000000 | 0.500000 | 0.666667 | 0.485294 | 0.568628 | `false` | 57.734000 | 9565 | 4 | 4 | 0.077792 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.384615 | 0.555556 | 1.000000 | 0.750000 | 0.857143 | 0.652778 | 0.706349 | `true` | 63.564000 | 12239 | 4 | 4 | 0.101318 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | generic_agent | try4 | 1.000000 | 0.384615 | 0.555556 | 1.000000 | 0.750000 | 0.857143 | 0.652778 | 0.706349 | `true` | 62.689000 | 10183 | 4 | 5 | 0.084457 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | generic_agent | try5 | 1.000000 | 0.384615 | 0.555556 | 1.000000 | 0.750000 | 0.857143 | 0.652778 | 0.706349 | `true` | 45.337000 | 7421 | 3 | 3 | 0.081155 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | proposed_agent | try1 | 1.000000 | 0.384615 | 0.555556 | 1.000000 | 1.000000 | 1.000000 | 0.777778 | 0.777778 | `true` | 74.104000 | 9942 | 3 | 2 | 0.090814 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | proposed_agent | try2 | 1.000000 | 0.461538 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 103.381000 | 14681 | 4 | 3 | 0.124780 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | proposed_agent | try3 | 1.000000 | 0.461538 | 0.631579 | 1.000000 | 1.000000 | 1.000000 | 0.815789 | 0.815789 | `true` | 108.531000 | 20491 | 5 | 5 | 0.148195 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | proposed_agent | try4 | 1.000000 | 0.384615 | 0.555556 | 1.000000 | 0.750000 | 0.857143 | 0.652778 | 0.706349 | `true` | 111.556000 | 23427 | 6 | 7 | 0.171243 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | proposed_agent | try5 | 1.000000 | 0.384615 | 0.555556 | 1.000000 | 1.000000 | 1.000000 | 0.777778 | 0.777778 | `true` | 98.506000 | 14212 | 4 | 3 | 0.119269 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | rule_based | try1 | 0.750000 | 0.230769 | 0.352941 | 0.000000 | 0.000000 | 0.000000 | 0.176471 | 0.176471 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.384615 | 0.555556 | 1.000000 | 0.750000 | 0.857143 | 0.652778 | 0.706349 | `true` | 32.320000 | 2010 | 1 | 0 | 0.031960 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | single_llm | try2 | 1.000000 | 0.461538 | 0.631579 | 1.000000 | 0.500000 | 0.666667 | 0.565789 | 0.649123 | `true` | 28.629000 | 1755 | 1 | 0 | 0.028135 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | single_llm | try3 | 1.000000 | 0.307692 | 0.470588 | 1.000000 | 1.000000 | 1.000000 | 0.735294 | 0.735294 | `true` | 34.553000 | 2200 | 1 | 0 | 0.034810 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | single_llm | try4 | 1.000000 | 0.307692 | 0.470588 | 1.000000 | 0.750000 | 0.857143 | 0.610294 | 0.663865 | `true` | 27.282000 | 1759 | 1 | 0 | 0.028195 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | single_llm | try5 | 1.000000 | 0.384615 | 0.555556 | 1.000000 | 0.750000 | 0.857143 | 0.652778 | 0.706349 | `true` | 28.621000 | 1738 | 1 | 0 | 0.028856 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | claude_code | try1 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 136.467192 | 7037 | `null` | 9 | 0.218290 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | claude_code | try2 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 132.333910 | 6743 | `null` | 7 | 0.217090 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | claude_code | try3 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 127.556619 | 5320 | `null` | 10 | 0.207139 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | claude_code | try4 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.666667 | 0.800000 | 0.583333 | 0.650000 | `true` | 142.847723 | 7380 | `null` | 8 | 0.255175 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | claude_code | try5 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 152.006686 | 7155 | `null` | 8 | 0.251370 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | generic_agent | try1 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 51.769000 | 10757 | 3 | 2 | 0.078464 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | generic_agent | try2 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 45.134000 | 8929 | 3 | 2 | 0.067988 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | generic_agent | try3 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 105.049000 | 18914 | 6 | 7 | 0.146340 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | generic_agent | try4 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 60.373000 | 12753 | 5 | 4 | 0.098005 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | generic_agent | try5 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 54.646000 | 11943 | 5 | 4 | 0.090929 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | proposed_agent | try1 | 0.428571 | 0.500000 | 0.461538 | 1.000000 | 1.000000 | 1.000000 | 0.730769 | 0.730769 | `true` | 110.163000 | 23804 | 5 | 4 | 0.162754 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | proposed_agent | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.666667 | 0.800000 | 0.666667 | 0.733334 | `true` | 92.449000 | 19239 | 5 | 5 | 0.134324 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | proposed_agent | try3 | 0.500000 | 0.500000 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 113.989000 | 22751 | 5 | 7 | 0.156295 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | proposed_agent | try4 | 0.750000 | 0.500000 | 0.600000 | 1.000000 | 0.666667 | 0.800000 | 0.633333 | 0.700000 | `true` | 98.529000 | 14767 | 4 | 3 | 0.118126 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | proposed_agent | try5 | 0.666667 | 0.333333 | 0.444444 | 1.000000 | 0.666667 | 0.800000 | 0.555555 | 0.622222 | `true` | 83.610000 | 17667 | 5 | 5 | 0.121111 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | rule_based | try1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | single_llm | try1 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 34.693000 | 2078 | 1 | 0 | 0.032596 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | single_llm | try2 | 0.750000 | 0.500000 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 38.719000 | 2390 | 1 | 0 | 0.037276 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | single_llm | try3 | 0.800000 | 0.666667 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | `true` | 39.492000 | 2401 | 1 | 0 | 0.037441 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | single_llm | try4 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 40.115000 | 2434 | 1 | 0 | 0.037936 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | single_llm | try5 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 37.648000 | 2116 | 1 | 0 | 0.034646 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| competitive-data-science-predict-future-sales | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.754887 | 0.907692 | 0.821775 | 1.000000 | 1.000000 | 1.000000 | 0.910888 | 0.910888 | 0.000489 | 178.265212 | 9801.200000 | `null` | 8.800000 | 0.275371 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.795000 | 0.738462 | 0.753733 | 1.000000 | 1.000000 | 1.000000 | 0.876866 | 0.876866 | 0.002552 | 91.609400 | 17902.200000 | 4.800000 | 5.800000 | 0.132533 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 3600 | `null` | `null` | `null` | `null` |
| competitive-data-science-predict-future-sales | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.701078 | 0.861539 | 0.772775 | 1.000000 | 1.000000 | 1.000000 | 0.886387 | 0.886387 | 0.000256 | 112.495800 | 20832.600000 | 4.800000 | 5.400000 | 0.163597 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.750000 | 0.230769 | 0.352941 | 1.000000 | 1.000000 | 1.000000 | 0.676470 | 0.676470 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| competitive-data-science-predict-future-sales | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.717822 | 0.676923 | 0.694246 | 1.000000 | 1.000000 | 1.000000 | 0.847123 | 0.847123 | 0.001651 | 15.309400 | 934.600000 | 1.000000 | 0.000000 | 0.040069 |
| competitive-data-science-predict-future-sales | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | 0.000000 | 123.578020 | 5726.600000 | `null` | 9.200000 | 0.217585 |
| competitive-data-science-predict-future-sales | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.933333 | 0.275000 | 0.421818 | 1.000000 | 1.000000 | 1.000000 | 0.710909 | 0.710909 | 0.001005 | 56.255600 | 8393.600000 | 3.400000 | 3.000000 | 0.069916 |
| competitive-data-science-predict-future-sales | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.438095 | 0.300000 | 0.347013 | 1.000000 | 1.000000 | 1.000000 | 0.673506 | 0.673506 | 0.000670 | 87.151400 | 14854.400000 | 4.200000 | 4.000000 | 0.116899 |
| competitive-data-science-predict-future-sales | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.666667 | 0.250000 | 0.363636 | 0.000000 | 1.000000 | 0.000000 | 0.681818 | 0.181818 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| competitive-data-science-predict-future-sales | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.485714 | 0.350000 | 0.405274 | 1.000000 | 1.000000 | 1.000000 | 0.702637 | 0.702637 | 0.000690 | 37.389800 | 2215.400000 | 1.000000 | 0.000000 | 0.035200 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.230769 | 0.369902 | 1.000000 | 1.000000 | 1.000000 | 0.684951 | 0.684951 | 0.002081 | 88.863675 | 4728.400000 | `null` | 6.000000 | 0.171182 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | generic_agent | 5 | `true` | 0.800000 | 1.000000 | 0.369230 | 0.538562 | 1.000000 | 0.650000 | 0.780953 | 0.594281 | 0.659757 | 0.005313 | 65.767600 | 11449.000000 | 3.800000 | 4.000000 | 0.097151 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.415384 | 0.585965 | 1.000000 | 0.950000 | 0.971429 | 0.767982 | 0.778697 | 0.003607 | 99.215600 | 16550.600000 | 4.400000 | 4.000000 | 0.130860 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.750000 | 0.230769 | 0.352941 | 0.000000 | 0.000000 | 0.000000 | 0.176471 | 0.176471 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| competitive-data-science-predict-future-sales | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.369230 | 0.536773 | 1.000000 | 0.750000 | 0.847619 | 0.643387 | 0.692196 | 0.003148 | 30.281000 | 1892.400000 | 1.000000 | 0.000000 | 0.030391 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.566667 | 0.713333 | 1.000000 | 0.933333 | 0.960000 | 0.823333 | 0.836667 | 0.015067 | 138.242426 | 6727.000000 | `null` | 8.400000 | 0.229813 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | 0.000000 | 63.394200 | 12659.200000 | 4.400000 | 3.800000 | 0.096346 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | proposed_agent | 5 | `true` | 1.000000 | 0.669048 | 0.466667 | 0.534530 | 1.000000 | 0.800000 | 0.880000 | 0.667265 | 0.707265 | 0.004902 | 99.748000 | 19645.600000 | 4.800000 | 4.800000 | 0.138522 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| competitive-data-science-predict-future-sales | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 0.910000 | 0.633334 | 0.745455 | 1.000000 | 1.000000 | 1.000000 | 0.872727 | 0.872727 | 0.001521 | 38.133400 | 2283.800000 | 1.000000 | 0.000000 | 0.035979 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 1.000000 | 0.938722 | 0.488782 | 0.576253 | 1.000000 | 0.983333 | 0.990000 | 0.779793 | 0.783127 | 0.004409 | 132.237333 | 6745.800000 | `null` | 8.100000 | 0.223488 |
| generic_agent | 4 | 1.000000 | 5.000000 | 0.950000 | 0.932083 | 0.512340 | 0.628528 | 1.000000 | 0.912500 | 0.945238 | 0.770514 | 0.786883 | 0.002217 | 69.256700 | 12601.000000 | 4.100000 | 4.150000 | 0.098987 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 3600.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.702055 | 0.510898 | 0.560071 | 1.000000 | 0.937500 | 0.962857 | 0.748785 | 0.761464 | 0.002359 | 99.652700 | 17970.800000 | 4.550000 | 4.550000 | 0.137469 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.541667 | 0.177885 | 0.267379 | 0.250000 | 0.500000 | 0.250000 | 0.383690 | 0.258690 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 0.778384 | 0.507372 | 0.595437 | 1.000000 | 0.937500 | 0.961905 | 0.766468 | 0.778671 | 0.001752 | 30.278400 | 1831.550000 | 1.000000 | 0.000000 | 0.035410 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task competitive-data-science-predict-future-sales --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/competitive-data-science-predict-future-sales-all.md
```
