# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `spaceship-titanic`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.952381`
- Mean Add Precision: `0.799291`
- Mean Add Recall: `0.540952`
- Mean Add F1: `0.628359`
- Mean Remove Precision: `1.000000`
- Mean Remove Recall: `0.881746`
- Mean Remove F1: `0.922041`
- Mean Task Completion Score: `0.755053`
- Mean Strict Task Completion Score: `0.775200`
- Mean Task Completion Variance: `0.003387`
- Mean Runtime (s): `191.387841`
- Mean Total Tokens: `10439.437500`
- Mean API Calls: `2.500000`
- Mean Tool Calls: `3.080000`
- Mean Cost (USD): `0.104933`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| spaceship-titanic | Accuracy | transportation_tabular | binary_classification | single_table | small (8693) | low (14) | medium (17) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| spaceship-titanic | 21 | 6 | 0.952381 | 4.047619 | 0.799291 | 0.540952 | 0.628359 | 1.000000 | 0.881746 | 0.922041 | 0.755053 | 0.775200 | 0.003387 | 191.387841 | 10439.437500 | 2.500000 | 3.080000 | 0.104933 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| spaceship-titanic | tc1_from_scratch | claude_code | try1 | 0.833333 | 0.833333 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 145.820873 | 8648 | `null` | 7 | 0.252674 |
| spaceship-titanic | tc1_from_scratch | claude_code | try2 | 0.909091 | 0.833333 | 0.869565 | 1.000000 | 1.000000 | 1.000000 | 0.934783 | 0.934783 | `true` | 131.417777 | 8881 | `null` | 8 | 0.265738 |
| spaceship-titanic | tc1_from_scratch | claude_code | try3 | 0.909091 | 0.833333 | 0.869565 | 1.000000 | 1.000000 | 1.000000 | 0.934783 | 0.934783 | `true` | 116.232351 | 7020 | `null` | 7 | 0.223059 |
| spaceship-titanic | tc1_from_scratch | claude_code | try4 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 123.845113 | 6389 | `null` | 6 | 0.209623 |
| spaceship-titanic | tc1_from_scratch | claude_code | try5 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 143.087967 | 7483 | `null` | 9 | 0.249368 |
| spaceship-titanic | tc1_from_scratch | generic_agent | try1 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 61.699000 | 18644 | 5 | 5 | 0.145894 |
| spaceship-titanic | tc1_from_scratch | generic_agent | try2 | 1.000000 | 0.916667 | 0.956522 | 1.000000 | 1.000000 | 1.000000 | 0.978261 | 0.978261 | `true` | 89.578000 | 14711 | 5 | 4 | 0.145158 |
| spaceship-titanic | tc1_from_scratch | generic_agent | try3 | 0.833333 | 0.833333 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 75.343000 | 14662 | 5 | 4 | 0.109896 |
| spaceship-titanic | tc1_from_scratch | generic_agent | try4 | 0.833333 | 0.833333 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 65.084000 | 8290 | 3 | 2 | 0.074456 |
| spaceship-titanic | tc1_from_scratch | generic_agent | try5 | 1.000000 | 0.916667 | 0.956522 | 1.000000 | 1.000000 | 1.000000 | 0.978261 | 0.978261 | `true` | 85.822000 | 18528 | 7 | 6 | 0.143859 |
| spaceship-titanic | tc1_from_scratch | human | human_tc1_annotator_c_v1 | 1.000000 | 0.916667 | 0.956522 | 1.000000 | 1.000000 | 1.000000 | 0.978261 | 0.978261 | `true` | 2700 | `null` | `null` | `null` | `null` |
| spaceship-titanic | tc1_from_scratch | proposed_agent | try1 | 0.818182 | 0.750000 | 0.782609 | 1.000000 | 1.000000 | 1.000000 | 0.891304 | 0.891304 | `true` | 68.083000 | 16995 | 4 | 4 | 0.162446 |
| spaceship-titanic | tc1_from_scratch | proposed_agent | try2 | 1.000000 | 0.916667 | 0.956522 | 1.000000 | 1.000000 | 1.000000 | 0.978261 | 0.978261 | `true` | 76.461000 | 14850 | 4 | 4 | 0.159859 |
| spaceship-titanic | tc1_from_scratch | proposed_agent | try3 | 0.818182 | 0.750000 | 0.782609 | 1.000000 | 1.000000 | 1.000000 | 0.891304 | 0.891304 | `true` | 89.269000 | 14262 | 4 | 4 | 0.104867 |
| spaceship-titanic | tc1_from_scratch | proposed_agent | try4 | 0.833333 | 0.833333 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 67.032000 | 13468 | 4 | 4 | 0.099077 |
| spaceship-titanic | tc1_from_scratch | proposed_agent | try5 | 0.833333 | 0.833333 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 88.196000 | 16621 | 4 | 3 | 0.121736 |
| spaceship-titanic | tc1_from_scratch | rule_based | try1 | 0.166667 | 0.083333 | 0.111111 | 1.000000 | 1.000000 | 1.000000 | 0.555555 | 0.555555 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| spaceship-titanic | tc1_from_scratch | single_llm | try1 | 1.000000 | 0.916667 | 0.956522 | 1.000000 | 1.000000 | 1.000000 | 0.978261 | 0.978261 | `true` | 12.227000 | 871 | 1 | 0 | 0.042645 |
| spaceship-titanic | tc1_from_scratch | single_llm | try2 | 1.000000 | 0.916667 | 0.956522 | 1.000000 | 1.000000 | 1.000000 | 0.978261 | 0.978261 | `true` | 11.249000 | 856 | 1 | 0 | 0.042420 |
| spaceship-titanic | tc1_from_scratch | single_llm | try3 | 1.000000 | 0.916667 | 0.956522 | 1.000000 | 1.000000 | 1.000000 | 0.978261 | 0.978261 | `true` | 14.645000 | 874 | 1 | 0 | 0.042686 |
| spaceship-titanic | tc1_from_scratch | single_llm | try4 | 1.000000 | 0.916667 | 0.956522 | 1.000000 | 1.000000 | 1.000000 | 0.978261 | 0.978261 | `true` | 15.198000 | 918 | 1 | 0 | 0.043346 |
| spaceship-titanic | tc1_from_scratch | single_llm | try5 | 1.000000 | 0.833333 | 0.909091 | 1.000000 | 1.000000 | 1.000000 | 0.954546 | 0.954546 | `true` | 12.516000 | 762 | 1 | 0 | 0.013937 |
| spaceship-titanic | tc2_partial_good | claude_code | try1 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 115.247069 | 7854 | `null` | 7 | 0.235890 |
| spaceship-titanic | tc2_partial_good | claude_code | try2 | 1.000000 | 0.555556 | 0.714286 | 1.000000 | 1.000000 | 1.000000 | 0.857143 | 0.857143 | `true` | 96.050164 | 5489 | `null` | 4 | 0.185219 |
| spaceship-titanic | tc2_partial_good | claude_code | try3 | 1.000000 | 0.777778 | 0.875000 | 1.000000 | 1.000000 | 1.000000 | 0.937500 | 0.937500 | `true` | 133.057268 | 7790 | `null` | 8 | 0.267769 |
| spaceship-titanic | tc2_partial_good | claude_code | try4 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 120.098664 | 6371 | `null` | 7 | 0.208945 |
| spaceship-titanic | tc2_partial_good | claude_code | try5 | 1.000000 | 0.777778 | 0.875000 | 1.000000 | 1.000000 | 1.000000 | 0.937500 | 0.937500 | `true` | 146.839291 | 7520 | `null` | 9 | 0.239906 |
| spaceship-titanic | tc2_partial_good | generic_agent | try1 | 1.000000 | 0.777778 | 0.875000 | 1.000000 | 1.000000 | 1.000000 | 0.937500 | 0.937500 | `true` | 62.434000 | 13113 | 4 | 3 | 0.104283 |
| spaceship-titanic | tc2_partial_good | generic_agent | try2 | 1.000000 | 0.777778 | 0.875000 | 1.000000 | 1.000000 | 1.000000 | 0.937500 | 0.937500 | `true` | 59.633000 | 9706 | 3 | 2 | 0.082677 |
| spaceship-titanic | tc2_partial_good | generic_agent | try3 | 1.000000 | 0.777778 | 0.875000 | 1.000000 | 1.000000 | 1.000000 | 0.937500 | 0.937500 | `true` | 81.068000 | 16586 | 5 | 4 | 0.128885 |
| spaceship-titanic | tc2_partial_good | generic_agent | try4 | 1.000000 | 0.777778 | 0.875000 | 1.000000 | 1.000000 | 1.000000 | 0.937500 | 0.937500 | `true` | 66.494000 | 9808 | 4 | 3 | 0.088008 |
| spaceship-titanic | tc2_partial_good | generic_agent | try5 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 72.254000 | 11813 | 5 | 4 | 0.100710 |
| spaceship-titanic | tc2_partial_good | proposed_agent | try1 | 1.000000 | 0.777778 | 0.875000 | 1.000000 | 1.000000 | 1.000000 | 0.937500 | 0.937500 | `true` | 64.207000 | 13454 | 4 | 3 | 0.106858 |
| spaceship-titanic | tc2_partial_good | proposed_agent | try2 | 1.000000 | 0.777778 | 0.875000 | 1.000000 | 1.000000 | 1.000000 | 0.937500 | 0.937500 | `true` | 79.696000 | 17319 | 4 | 5 | 0.116210 |
| spaceship-titanic | tc2_partial_good | proposed_agent | try3 | 0.750000 | 0.666667 | 0.705882 | 1.000000 | 1.000000 | 1.000000 | 0.852941 | 0.852941 | `true` | 81.555000 | 16556 | 5 | 4 | 0.125750 |
| spaceship-titanic | tc2_partial_good | proposed_agent | try4 | 1.000000 | 0.777778 | 0.875000 | 1.000000 | 1.000000 | 1.000000 | 0.937500 | 0.937500 | `true` | 87.813000 | 18647 | 4 | 4 | 0.128858 |
| spaceship-titanic | tc2_partial_good | proposed_agent | try5 | 0.750000 | 0.666667 | 0.705882 | 1.000000 | 1.000000 | 1.000000 | 0.852941 | 0.852941 | `true` | 80.007000 | 10448 | 3 | 2 | 0.093001 |
| spaceship-titanic | tc2_partial_good | rule_based | try1 | 0.166667 | 0.111111 | 0.133333 | 1.000000 | 1.000000 | 1.000000 | 0.566666 | 0.566666 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| spaceship-titanic | tc2_partial_good | single_llm | try1 | 0.714286 | 0.555556 | 0.625000 | 1.000000 | 1.000000 | 1.000000 | 0.812500 | 0.812500 | `true` | 40.564000 | 2664 | 1 | 0 | 0.041681 |
| spaceship-titanic | tc2_partial_good | single_llm | try2 | 1.000000 | 0.777778 | 0.875000 | 1.000000 | 1.000000 | 1.000000 | 0.937500 | 0.937500 | `true` | 35.451000 | 2543 | 1 | 0 | 0.039866 |
| spaceship-titanic | tc2_partial_good | single_llm | try3 | 1.000000 | 0.777778 | 0.875000 | 1.000000 | 1.000000 | 1.000000 | 0.937500 | 0.937500 | `true` | 43.570000 | 2795 | 1 | 0 | 0.043645 |
| spaceship-titanic | tc2_partial_good | single_llm | try4 | 1.000000 | 0.777778 | 0.875000 | 1.000000 | 1.000000 | 1.000000 | 0.937500 | 0.937500 | `true` | 41.797000 | 2733 | 1 | 0 | 0.042715 |
| spaceship-titanic | tc2_partial_good | single_llm | try5 | 0.750000 | 0.666667 | 0.705882 | 1.000000 | 1.000000 | 1.000000 | 0.852941 | 0.852941 | `true` | 42.626000 | 2749 | 1 | 0 | 0.043806 |
| spaceship-titanic | tc3_fault_injected | claude_code | try1 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | `true` | 72.397757 | 4549 | `null` | 8 | 0.178825 |
| spaceship-titanic | tc3_fault_injected | claude_code | try2 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | `true` | 108.684914 | 6677 | `null` | 9 | 0.225114 |
| spaceship-titanic | tc3_fault_injected | claude_code | try3 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 115.905850 | 5209 | `null` | 6 | 0.188035 |
| spaceship-titanic | tc3_fault_injected | claude_code | try4 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | `true` | 84.366802 | 5487 | `null` | 7 | 0.194608 |
| spaceship-titanic | tc3_fault_injected | claude_code | try5 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | `true` | 101.006423 | 5272 | `null` | 6 | 0.189019 |
| spaceship-titanic | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | `true` | 48.611000 | 9682 | 4 | 3 | 0.078175 |
| spaceship-titanic | tc3_fault_injected | generic_agent | try2 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | `true` | 52.905000 | 10744 | 5 | 4 | 0.085521 |
| spaceship-titanic | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | `true` | 49.461000 | 9982 | 5 | 4 | 0.084161 |
| spaceship-titanic | tc3_fault_injected | generic_agent | try4 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | `true` | 72.763000 | 9486 | 4 | 3 | 0.081687 |
| spaceship-titanic | tc3_fault_injected | generic_agent | try5 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | `true` | 70.788000 | 13396 | 5 | 5 | 0.121470 |
| spaceship-titanic | tc3_fault_injected | proposed_agent | try1 | 1.000000 | 0.583333 | 0.736842 | 1.000000 | 1.000000 | 1.000000 | 0.868421 | 0.868421 | `true` | 88.404000 | 13785 | 3 | 2 | 0.128796 |
| spaceship-titanic | tc3_fault_injected | proposed_agent | try2 | 1.000000 | 0.583333 | 0.736842 | 1.000000 | 0.750000 | 0.857143 | 0.743421 | 0.796992 | `true` | 174.460000 | 38991 | 7 | 9 | 0.271125 |
| spaceship-titanic | tc3_fault_injected | proposed_agent | try3 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 136.318000 | 33289 | 6 | 8 | 0.229438 |
| spaceship-titanic | tc3_fault_injected | proposed_agent | try4 | 1.000000 | 0.666667 | 0.800000 | 1.000000 | 1.000000 | 1.000000 | 0.900000 | 0.900000 | `true` | 101.576000 | 18564 | 4 | 3 | 0.142121 |
| spaceship-titanic | tc3_fault_injected | proposed_agent | try5 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.750000 | 0.857143 | 0.708333 | 0.761905 | `true` | 150.003000 | 32127 | 6 | 7 | 0.224937 |
| spaceship-titanic | tc3_fault_injected | rule_based | try1 | 0.166667 | 0.083333 | 0.111111 | 1.000000 | 0.250000 | 0.400000 | 0.180556 | 0.255555 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| spaceship-titanic | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.583333 | 0.736842 | 1.000000 | 0.750000 | 0.857143 | 0.743421 | 0.796992 | `true` | 32.940000 | 2620 | 1 | 0 | 0.040925 |
| spaceship-titanic | tc3_fault_injected | single_llm | try2 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | `true` | 23.914000 | 1775 | 1 | 0 | 0.028250 |
| spaceship-titanic | tc3_fault_injected | single_llm | try3 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | `true` | 26.841000 | 1680 | 1 | 0 | 0.026825 |
| spaceship-titanic | tc3_fault_injected | single_llm | try4 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | `true` | 28.414000 | 1786 | 1 | 0 | 0.028415 |
| spaceship-titanic | tc3_fault_injected | single_llm | try5 | 0.909091 | 0.833333 | 0.869565 | 1.000000 | 0.750000 | 0.857143 | 0.809783 | 0.863354 | `true` | 53.652000 | 3485 | 1 | 0 | 0.054876 |
| spaceship-titanic | tc4_mixed_history | claude_code | try1 | 0.800000 | 0.400000 | 0.533333 | 1.000000 | 0.666667 | 0.800000 | 0.600000 | 0.666667 | `true` | 143.368808 | 7890 | `null` | 7 | 0.252945 |
| spaceship-titanic | tc4_mixed_history | claude_code | try2 | 0.800000 | 0.400000 | 0.533333 | 1.000000 | 0.666667 | 0.800000 | 0.600000 | 0.666667 | `true` | 122.011732 | 6344 | `null` | 7 | 0.206474 |
| spaceship-titanic | tc4_mixed_history | claude_code | try3 | 0.800000 | 0.400000 | 0.533333 | 1.000000 | 0.666667 | 0.800000 | 0.600000 | 0.666667 | `true` | 175.542335 | 7895 | `null` | 8 | 0.247892 |
| spaceship-titanic | tc4_mixed_history | claude_code | try4 | 0.800000 | 0.400000 | 0.533333 | 1.000000 | 0.666667 | 0.800000 | 0.600000 | 0.666667 | `true` | 119.136932 | 6286 | `null` | 6 | 0.219239 |
| spaceship-titanic | tc4_mixed_history | claude_code | try5 | 0.800000 | 0.400000 | 0.533333 | 1.000000 | 0.666667 | 0.800000 | 0.600000 | 0.666667 | `true` | 128.482166 | 7653 | `null` | 8 | 0.249034 |
| spaceship-titanic | tc4_mixed_history | generic_agent | try1 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 63.986000 | 11063 | 4 | 4 | 0.096320 |
| spaceship-titanic | tc4_mixed_history | generic_agent | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 86.115000 | 15489 | 5 | 4 | 0.122530 |
| spaceship-titanic | tc4_mixed_history | generic_agent | try3 | 0.800000 | 0.400000 | 0.533333 | 1.000000 | 0.666667 | 0.800000 | 0.600000 | 0.666667 | `true` | 70.984000 | 12150 | 4 | 4 | 0.100124 |
| spaceship-titanic | tc4_mixed_history | generic_agent | try4 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.666667 | 0.800000 | 0.666667 | 0.733334 | `true` | 91.935000 | 12297 | 4 | 3 | 0.108615 |
| spaceship-titanic | tc4_mixed_history | generic_agent | try5 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.666667 | 0.800000 | 0.666667 | 0.733334 | `true` | 104.792000 | 21873 | 5 | 5 | 0.173911 |
| spaceship-titanic | tc4_mixed_history | proposed_agent | try1 | 0.857143 | 0.600000 | 0.705882 | 1.000000 | 0.666667 | 0.800000 | 0.686275 | 0.752941 | `true` | 121.052000 | 31737 | 6 | 8 | 0.221743 |
| spaceship-titanic | tc4_mixed_history | proposed_agent | try2 | 0.833333 | 0.500000 | 0.625000 | 1.000000 | 1.000000 | 1.000000 | 0.812500 | 0.812500 | `true` | 128.413000 | 16691 | 4 | 3 | 0.140042 |
| spaceship-titanic | tc4_mixed_history | proposed_agent | try3 | 0.833333 | 0.500000 | 0.625000 | 1.000000 | 1.000000 | 1.000000 | 0.812500 | 0.812500 | `true` | 123.443000 | 16626 | 4 | 4 | 0.144731 |
| spaceship-titanic | tc4_mixed_history | proposed_agent | try4 | 0.750000 | 0.300000 | 0.428571 | 1.000000 | 0.333333 | 0.500000 | 0.380952 | 0.464286 | `false` | 103.197000 | 14509 | 4 | 3 | 0.119264 |
| spaceship-titanic | tc4_mixed_history | proposed_agent | try5 | 0.857143 | 0.600000 | 0.705882 | 1.000000 | 0.666667 | 0.800000 | 0.686275 | 0.752941 | `true` | 143.956000 | 23178 | 5 | 4 | 0.173751 |
| spaceship-titanic | tc4_mixed_history | rule_based | try1 | 0.200000 | 0.100000 | 0.133333 | 1.000000 | 1.000000 | 1.000000 | 0.566666 | 0.566666 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| spaceship-titanic | tc4_mixed_history | single_llm | try1 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 41.588000 | 3041 | 1 | 0 | 0.047216 |
| spaceship-titanic | tc4_mixed_history | single_llm | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.666667 | 0.800000 | 0.666667 | 0.733334 | `true` | 38.970000 | 2722 | 1 | 0 | 0.042431 |
| spaceship-titanic | tc4_mixed_history | single_llm | try3 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 1.000000 | 1.000000 | 0.875000 | 0.875000 | `true` | 46.701000 | 2960 | 1 | 0 | 0.046000 |
| spaceship-titanic | tc4_mixed_history | single_llm | try4 | 1.000000 | 0.800000 | 0.888889 | 1.000000 | 1.000000 | 1.000000 | 0.944445 | 0.944445 | `true` | 63.029000 | 3977 | 1 | 0 | 0.061255 |
| spaceship-titanic | tc4_mixed_history | single_llm | try5 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 0.666667 | 0.800000 | 0.666667 | 0.733334 | `true` | 42.341000 | 2497 | 1 | 0 | 0.040063 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| spaceship-titanic | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.930303 | 0.866666 | 0.896311 | 1.000000 | 1.000000 | 1.000000 | 0.948156 | 0.948156 | 0.000816 | 132.080816 | 7684.200000 | `null` | 7.400000 | 0.240092 |
| spaceship-titanic | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.933333 | 0.866667 | 0.897760 | 1.000000 | 1.000000 | 1.000000 | 0.948880 | 0.948880 | 0.000767 | 75.505200 | 14967.000000 | 5.000000 | 4.200000 | 0.123853 |
| spaceship-titanic | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 0.916667 | 0.956522 | 1.000000 | 1.000000 | 1.000000 | 0.978261 | 0.978261 | 0.000000 | 2700 | `null` | `null` | `null` | `null` |
| spaceship-titanic | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.860606 | 0.816667 | 0.837681 | 1.000000 | 1.000000 | 1.000000 | 0.918841 | 0.918841 | 0.001011 | 77.808200 | 15239.200000 | 4.000000 | 3.800000 | 0.129597 |
| spaceship-titanic | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.166667 | 0.083333 | 0.111111 | 1.000000 | 1.000000 | 1.000000 | 0.555555 | 0.555555 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| spaceship-titanic | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.900000 | 0.947036 | 1.000000 | 1.000000 | 1.000000 | 0.973518 | 0.973518 | 0.000090 | 13.167000 | 856.200000 | 1.000000 | 0.000000 | 0.037007 |
| spaceship-titanic | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.688889 | 0.812857 | 1.000000 | 1.000000 | 1.000000 | 0.906429 | 0.906429 | 0.000889 | 122.258491 | 7004.800000 | `null` | 7.000000 | 0.227546 |
| spaceship-titanic | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.755556 | 0.860000 | 1.000000 | 1.000000 | 1.000000 | 0.930000 | 0.930000 | 0.000225 | 68.376600 | 12205.200000 | 4.200000 | 3.200000 | 0.100913 |
| spaceship-titanic | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.900000 | 0.733334 | 0.807353 | 1.000000 | 1.000000 | 1.000000 | 0.903676 | 0.903676 | 0.001716 | 78.655600 | 15284.800000 | 4.000000 | 3.600000 | 0.114135 |
| spaceship-titanic | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.166667 | 0.111111 | 0.133333 | 1.000000 | 1.000000 | 1.000000 | 0.566666 | 0.566666 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| spaceship-titanic | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.892857 | 0.711111 | 0.791176 | 1.000000 | 1.000000 | 1.000000 | 0.895588 | 0.895588 | 0.002798 | 40.801600 | 2696.800000 | 1.000000 | 0.000000 | 0.042343 |
| spaceship-titanic | tc3_fault_injected | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.800000 | 0.885714 | 0.650000 | 0.692857 | 0.002500 | 96.472349 | 5438.800000 | `null` | 7.200000 | 0.195120 |
| spaceship-titanic | tc3_fault_injected | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.333333 | 0.500000 | 1.000000 | 0.750000 | 0.857143 | 0.625000 | 0.678571 | 0.000000 | 58.905600 | 10658.000000 | 4.600000 | 3.800000 | 0.090203 |
| spaceship-titanic | tc3_fault_injected | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.616667 | 0.759499 | 1.000000 | 0.900000 | 0.942857 | 0.829749 | 0.851178 | 0.007678 | 130.152200 | 27351.200000 | 5.200000 | 5.800000 | 0.199283 |
| spaceship-titanic | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.166667 | 0.083333 | 0.111111 | 1.000000 | 0.250000 | 0.400000 | 0.180556 | 0.255555 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| spaceship-titanic | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 0.981818 | 0.483333 | 0.621281 | 1.000000 | 0.750000 | 0.857143 | 0.685641 | 0.739212 | 0.005956 | 33.152200 | 2269.200000 | 1.000000 | 0.000000 | 0.035858 |
| spaceship-titanic | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 0.800000 | 0.400000 | 0.533333 | 1.000000 | 0.666667 | 0.800000 | 0.600000 | 0.666667 | 0.000000 | 137.708395 | 7213.600000 | `null` | 7.200000 | 0.235117 |
| spaceship-titanic | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 0.960000 | 0.480000 | 0.640000 | 1.000000 | 0.800000 | 0.880000 | 0.720000 | 0.760000 | 0.009156 | 83.562400 | 14574.400000 | 4.400000 | 4.000000 | 0.120300 |
| spaceship-titanic | tc4_mixed_history | proposed_agent | 5 | `true` | 0.800000 | 0.826190 | 0.500000 | 0.618067 | 1.000000 | 0.733333 | 0.820000 | 0.675700 | 0.719034 | 0.024906 | 124.012200 | 20548.200000 | 4.600000 | 4.400000 | 0.159906 |
| spaceship-titanic | tc4_mixed_history | rule_based | 1 | `true` | 1.000000 | 0.200000 | 0.100000 | 0.133333 | 1.000000 | 1.000000 | 1.000000 | 0.566666 | 0.566666 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| spaceship-titanic | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.580000 | 0.727778 | 1.000000 | 0.866667 | 0.920000 | 0.797222 | 0.823889 | 0.012623 | 46.525800 | 3039.400000 | 1.000000 | 0.000000 | 0.047393 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 1.000000 | 0.932576 | 0.572222 | 0.685625 | 1.000000 | 0.866667 | 0.921428 | 0.776146 | 0.803527 | 0.001051 | 122.130013 | 6835.350000 | `null` | 7.200000 | 0.224469 |
| generic_agent | 4 | 1.000000 | 5.000000 | 1.000000 | 0.973333 | 0.608889 | 0.724440 | 1.000000 | 0.887500 | 0.934286 | 0.805970 | 0.829363 | 0.002537 | 71.587450 | 13101.150000 | 4.550000 | 3.800000 | 0.108817 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.956522 | 1.000000 | 1.000000 | 1.000000 | 0.978261 | 0.978261 | 0.000000 | 2700.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 1.000000 | 5.000000 | 0.950000 | 0.896699 | 0.666667 | 0.755650 | 1.000000 | 0.908333 | 0.940714 | 0.831991 | 0.848182 | 0.008828 | 102.657050 | 19605.850000 | 4.450000 | 4.400000 | 0.150730 |
| rule_based | 4 | 0.750000 | 1.000000 | 0.750000 | 0.175000 | 0.094444 | 0.122222 | 1.000000 | 0.812500 | 0.850000 | 0.467361 | 0.486111 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 0.968669 | 0.668611 | 0.771818 | 1.000000 | 0.904167 | 0.944286 | 0.837992 | 0.858052 | 0.005367 | 33.411650 | 2215.400000 | 1.000000 | 0.000000 | 0.040650 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task spaceship-titanic --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/spaceship-titanic-all.md
```
