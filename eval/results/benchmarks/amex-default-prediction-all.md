# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `amex-default-prediction`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.857143`
- Mean Add Precision: `0.707846`
- Mean Add Recall: `0.199277`
- Mean Add F1: `0.297769`
- Mean Remove Precision: `0.895238`
- Mean Remove Recall: `0.789683`
- Mean Remove F1: `0.789796`
- Mean Task Completion Score: `0.543726`
- Mean Strict Task Completion Score: `0.543782`
- Mean Task Completion Variance: `0.002155`
- Mean Runtime (s): `140.080874`
- Mean Total Tokens: `15994.925000`
- Mean API Calls: `2.587500`
- Mean Tool Calls: `3.300000`
- Mean Cost (USD): `0.396029`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amex-default-prediction | AMEX Weighted Gini + Top 4% Capture | finance_tabular | binary_classification | single_table | xlarge (11363762) | high (192) | medium (14) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| amex-default-prediction | 21 | 6 | 0.857143 | 4.047619 | 0.707846 | 0.199277 | 0.297769 | 0.895238 | 0.789683 | 0.789796 | 0.543726 | 0.543782 | 0.002155 | 140.080874 | 15994.925000 | 2.587500 | 3.300000 | 0.396029 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| amex-default-prediction | tc1_from_scratch | claude_code | try1 | 0.857143 | 0.352941 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 163.940561 | 9349 | `null` | 12 | 1.118224 |
| amex-default-prediction | tc1_from_scratch | claude_code | try2 | 0.833333 | 0.294118 | 0.434783 | 1.000000 | 1.000000 | 1.000000 | 0.717391 | 0.717391 | `true` | 121.891358 | 6357 | `null` | 9 | 1.025284 |
| amex-default-prediction | tc1_from_scratch | claude_code | try3 | 0.750000 | 0.352941 | 0.480000 | 1.000000 | 1.000000 | 1.000000 | 0.740000 | 0.740000 | `true` | 198.885434 | 11829 | `null` | 10 | 1.084346 |
| amex-default-prediction | tc1_from_scratch | claude_code | try4 | 0.833333 | 0.294118 | 0.434783 | 1.000000 | 1.000000 | 1.000000 | 0.717391 | 0.717391 | `true` | 312.944458 | 10424 | `null` | 16 | 1.187422 |
| amex-default-prediction | tc1_from_scratch | claude_code | try5 | 0.750000 | 0.352941 | 0.480000 | 1.000000 | 1.000000 | 1.000000 | 0.740000 | 0.740000 | `true` | 156.337215 | 8005 | `null` | 9 | 1.142611 |
| amex-default-prediction | tc1_from_scratch | generic_agent | try1 | 0.833333 | 0.294118 | 0.434783 | 1.000000 | 1.000000 | 1.000000 | 0.717391 | 0.717391 | `true` | 92.746000 | 25495 | 4 | 5 | 0.726013 |
| amex-default-prediction | tc1_from_scratch | generic_agent | try2 | 0.714286 | 0.294118 | 0.416667 | 1.000000 | 1.000000 | 1.000000 | 0.708333 | 0.708333 | `true` | 145.765000 | 27964 | 7 | 7 | 0.462929 |
| amex-default-prediction | tc1_from_scratch | generic_agent | try3 | 0.800000 | 0.235294 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 57.640000 | 10460 | 5 | 5 | 0.260338 |
| amex-default-prediction | tc1_from_scratch | generic_agent | try4 | 0.750000 | 0.352941 | 0.480000 | 1.000000 | 1.000000 | 1.000000 | 0.740000 | 0.740000 | `true` | 144.527000 | 29254 | 4 | 5 | 0.340971 |
| amex-default-prediction | tc1_from_scratch | generic_agent | try5 | 0.857143 | 0.352941 | 0.500000 | 1.000000 | 1.000000 | 1.000000 | 0.750000 | 0.750000 | `true` | 71.450000 | 15833 | 3 | 4 | 0.213391 |
| amex-default-prediction | tc1_from_scratch | human | human_tc1_sean_kraemer_v4_manual_rebuild | 1.000000 | 0.470588 | 0.640000 | 1.000000 | 1.000000 | 1.000000 | 0.820000 | 0.820000 | `true` | 900 | `null` | `null` | `null` | `null` |
| amex-default-prediction | tc1_from_scratch | proposed_agent | try1 | 0.800000 | 0.235294 | 0.363636 | 1.000000 | 1.000000 | 1.000000 | 0.681818 | 0.681818 | `true` | 124.775000 | 26971 | 5 | 5 | 0.996254 |
| amex-default-prediction | tc1_from_scratch | proposed_agent | try2 | 0.714286 | 0.294118 | 0.416667 | 1.000000 | 1.000000 | 1.000000 | 0.708333 | 0.708333 | `true` | 353.304000 | 30608 | 4 | 4 | 0.392573 |
| amex-default-prediction | tc1_from_scratch | proposed_agent | try3 | 0.833333 | 0.294118 | 0.434783 | 1.000000 | 1.000000 | 1.000000 | 0.717391 | 0.717391 | `true` | 62.081000 | 11896 | 4 | 3 | 0.277577 |
| amex-default-prediction | tc1_from_scratch | proposed_agent | try4 | 0.600000 | 0.176471 | 0.272727 | 1.000000 | 1.000000 | 1.000000 | 0.636363 | 0.636363 | `true` | 101.748000 | 23446 | 4 | 7 | 0.339491 |
| amex-default-prediction | tc1_from_scratch | proposed_agent | try5 | 0.714286 | 0.294118 | 0.416667 | 1.000000 | 1.000000 | 1.000000 | 0.708333 | 0.708333 | `true` | 137.622000 | 33139 | 4 | 4 | 0.405878 |
| amex-default-prediction | tc1_from_scratch | rule_based | try1 | 0.500000 | 0.235294 | 0.320000 | 1.000000 | 1.000000 | 1.000000 | 0.660000 | 0.660000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| amex-default-prediction | tc1_from_scratch | single_llm | try1 | 0.666667 | 0.235294 | 0.347826 | 1.000000 | 1.000000 | 1.000000 | 0.673913 | 0.673913 | `true` | 13.185000 | 624 | 1 | 0 | 0.609574 |
| amex-default-prediction | tc1_from_scratch | single_llm | try2 | 0.750000 | 0.352941 | 0.480000 | 1.000000 | 1.000000 | 1.000000 | 0.740000 | 0.740000 | `true` | 18.131000 | 865 | 1 | 0 | 0.061133 |
| amex-default-prediction | tc1_from_scratch | single_llm | try3 | 0.666667 | 0.235294 | 0.347826 | 1.000000 | 1.000000 | 1.000000 | 0.673913 | 0.673913 | `true` | 14.318000 | 712 | 1 | 0 | 0.058838 |
| amex-default-prediction | tc1_from_scratch | single_llm | try4 | 0.666667 | 0.235294 | 0.347826 | 1.000000 | 1.000000 | 1.000000 | 0.673913 | 0.673913 | `true` | 12.145000 | 634 | 1 | 0 | 0.057668 |
| amex-default-prediction | tc1_from_scratch | single_llm | try5 | 0.666667 | 0.235294 | 0.347826 | 1.000000 | 1.000000 | 1.000000 | 0.673913 | 0.673913 | `true` | 24.473000 | 693 | 1 | 0 | 0.058553 |
| amex-default-prediction | tc2_partial_good | claude_code | try1 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | `true` | 349.698845 | 21391 | `null` | 4 | 1.183199 |
| amex-default-prediction | tc2_partial_good | claude_code | try2 | 1.000000 | 0.076923 | 0.142857 | 1.000000 | 1.000000 | 1.000000 | 0.571429 | 0.571429 | `true` | 68.557094 | 3942 | `null` | 1 | 0.715081 |
| amex-default-prediction | tc2_partial_good | claude_code | try3 | 1.000000 | 0.076923 | 0.142857 | 1.000000 | 1.000000 | 1.000000 | 0.571429 | 0.571429 | `true` | 159.748051 | 9180 | `null` | 4 | 0.931540 |
| amex-default-prediction | tc2_partial_good | claude_code | try4 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | `true` | 155.125308 | 9373 | `null` | 7 | 1.082999 |
| amex-default-prediction | tc2_partial_good | claude_code | try5 | 1.000000 | 0.076923 | 0.142857 | 1.000000 | 1.000000 | 1.000000 | 0.571429 | 0.571429 | `true` | 298.544870 | 19615 | `null` | 6 | 1.241145 |
| amex-default-prediction | tc2_partial_good | generic_agent | try1 | 1.000000 | 0.153846 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | `true` | 78.076000 | 13117 | 4 | 3 | 0.248464 |
| amex-default-prediction | tc2_partial_good | generic_agent | try2 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | `true` | 97.120000 | 17683 | 4 | 3 | 0.285959 |
| amex-default-prediction | tc2_partial_good | generic_agent | try3 | 0.500000 | 0.076923 | 0.133333 | 0.000000 | 1.000000 | 0.000000 | 0.566666 | 0.066667 | `true` | 85.572000 | 16553 | 5 | 4 | 0.314682 |
| amex-default-prediction | tc2_partial_good | generic_agent | try4 | 0.500000 | 0.076923 | 0.133333 | 1.000000 | 1.000000 | 1.000000 | 0.566666 | 0.566666 | `true` | 112.506000 | 21128 | 5 | 5 | 0.352088 |
| amex-default-prediction | tc2_partial_good | generic_agent | try5 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 1.000000 | 0.500000 | 0.500000 | `true` | 126.018000 | 25343 | 4 | 5 | 0.333418 |
| amex-default-prediction | tc2_partial_good | proposed_agent | try1 | 0.666667 | 0.153846 | 0.250000 | 1.000000 | 1.000000 | 1.000000 | 0.625000 | 0.625000 | `true` | 162.741000 | 33186 | 5 | 5 | 0.464886 |
| amex-default-prediction | tc2_partial_good | proposed_agent | try2 | 1.000000 | 0.230769 | 0.375000 | 0.000000 | 1.000000 | 0.000000 | 0.687500 | 0.187500 | `true` | 177.033000 | 27916 | 4 | 3 | 0.423677 |
| amex-default-prediction | tc2_partial_good | proposed_agent | try3 | 0.666667 | 0.153846 | 0.250000 | 0.000000 | 1.000000 | 0.000000 | 0.625000 | 0.125000 | `true` | 138.454000 | 21838 | 4 | 3 | 0.366611 |
| amex-default-prediction | tc2_partial_good | proposed_agent | try4 | 0.666667 | 0.153846 | 0.250000 | 0.000000 | 1.000000 | 0.000000 | 0.625000 | 0.125000 | `true` | 149.411000 | 23578 | 4 | 3 | 0.382235 |
| amex-default-prediction | tc2_partial_good | proposed_agent | try5 | 1.000000 | 0.153846 | 0.266667 | 1.000000 | 1.000000 | 1.000000 | 0.633333 | 0.633333 | `true` | 184.530000 | 28315 | 4 | 3 | 0.423806 |
| amex-default-prediction | tc2_partial_good | rule_based | try1 | 0.428571 | 0.230769 | 0.300000 | 1.000000 | 1.000000 | 1.000000 | 0.650000 | 0.650000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| amex-default-prediction | tc2_partial_good | single_llm | try1 | 0.500000 | 0.153846 | 0.235294 | 1.000000 | 1.000000 | 1.000000 | 0.617647 | 0.617647 | `true` | 73.229000 | 4245 | 1 | 0 | 0.110974 |
| amex-default-prediction | tc2_partial_good | single_llm | try2 | 0.666667 | 0.153846 | 0.250000 | 1.000000 | 1.000000 | 1.000000 | 0.625000 | 0.625000 | `true` | 66.654000 | 3830 | 1 | 0 | 0.105694 |
| amex-default-prediction | tc2_partial_good | single_llm | try3 | 0.666667 | 0.153846 | 0.250000 | 1.000000 | 1.000000 | 1.000000 | 0.625000 | 0.625000 | `true` | 90.829000 | 5115 | 1 | 0 | 0.124969 |
| amex-default-prediction | tc2_partial_good | single_llm | try4 | 0.500000 | 0.076923 | 0.133333 | 1.000000 | 1.000000 | 1.000000 | 0.566666 | 0.566666 | `true` | 116.548000 | 6557 | 1 | 0 | 0.146599 |
| amex-default-prediction | tc2_partial_good | single_llm | try5 | 1.000000 | 0.153846 | 0.266667 | 0.000000 | 1.000000 | 0.000000 | 0.633333 | 0.133333 | `true` | 107.847000 | 6179 | 1 | 0 | 0.140930 |
| amex-default-prediction | tc3_fault_injected | claude_code | try1 | 1.000000 | 0.058824 | 0.111111 | 1.000000 | 0.750000 | 0.857143 | 0.430555 | 0.484127 | `false` | 99.441287 | 6458 | `null` | 4 | 0.868697 |
| amex-default-prediction | tc3_fault_injected | claude_code | try2 | 0.500000 | 0.058824 | 0.105263 | 1.000000 | 0.750000 | 0.857143 | 0.427631 | 0.481203 | `false` | 139.649506 | 9362 | `null` | 4 | 0.919279 |
| amex-default-prediction | tc3_fault_injected | claude_code | try3 | 1.000000 | 0.235294 | 0.380952 | 1.000000 | 0.750000 | 0.857143 | 0.565476 | 0.619047 | `true` | 155.742498 | 9745 | `null` | 11 | 1.131898 |
| amex-default-prediction | tc3_fault_injected | claude_code | try4 | 1.000000 | 0.058824 | 0.111111 | 1.000000 | 0.750000 | 0.857143 | 0.430555 | 0.484127 | `false` | 173.498236 | 9830 | `null` | 7 | 1.093725 |
| amex-default-prediction | tc3_fault_injected | claude_code | try5 | 1.000000 | 0.058824 | 0.111111 | 1.000000 | 0.750000 | 0.857143 | 0.430555 | 0.484127 | `false` | 123.329172 | 6928 | `null` | 6 | 0.994599 |
| amex-default-prediction | tc3_fault_injected | generic_agent | try1 | 0.750000 | 0.176471 | 0.285714 | 1.000000 | 0.750000 | 0.857143 | 0.517857 | 0.571429 | `true` | 92.877000 | 25818 | 5 | 5 | 0.356076 |
| amex-default-prediction | tc3_fault_injected | generic_agent | try2 | 0.750000 | 0.176471 | 0.285714 | 1.000000 | 0.750000 | 0.857143 | 0.517857 | 0.571429 | `true` | 71.055000 | 15005 | 4 | 3 | 0.265139 |
| amex-default-prediction | tc3_fault_injected | generic_agent | try3 | 0.750000 | 0.176471 | 0.285714 | 1.000000 | 0.750000 | 0.857143 | 0.517857 | 0.571429 | `true` | 149.860000 | 30761 | 6 | 7 | 0.432721 |
| amex-default-prediction | tc3_fault_injected | generic_agent | try4 | 0.666667 | 0.117647 | 0.200000 | 1.000000 | 0.750000 | 0.857143 | 0.475000 | 0.528571 | `false` | 82.271000 | 19553 | 4 | 4 | 0.285562 |
| amex-default-prediction | tc3_fault_injected | generic_agent | try5 | 0.800000 | 0.235294 | 0.363636 | 1.000000 | 0.750000 | 0.857143 | 0.556818 | 0.610390 | `true` | 103.527000 | 29339 | 4 | 4 | 0.332644 |
| amex-default-prediction | tc3_fault_injected | proposed_agent | try1 | 0.800000 | 0.235294 | 0.363636 | 1.000000 | 0.500000 | 0.666667 | 0.431818 | 0.515151 | `false` | 156.284000 | 31065 | 5 | 5 | 0.453951 |
| amex-default-prediction | tc3_fault_injected | proposed_agent | try2 | 0.600000 | 0.176471 | 0.272727 | 1.000000 | 0.250000 | 0.400000 | 0.261363 | 0.336364 | `false` | 183.547000 | 27501 | 4 | 3 | 0.427664 |
| amex-default-prediction | tc3_fault_injected | proposed_agent | try3 | 0.750000 | 0.176471 | 0.285714 | 1.000000 | 0.250000 | 0.400000 | 0.267857 | 0.342857 | `false` | 95.049000 | 14698 | 4 | 3 | 0.311447 |
| amex-default-prediction | tc3_fault_injected | proposed_agent | try4 | 0.750000 | 0.176471 | 0.285714 | 1.000000 | 0.500000 | 0.666667 | 0.392857 | 0.476191 | `false` | 153.839000 | 28253 | 5 | 5 | 0.444651 |
| amex-default-prediction | tc3_fault_injected | proposed_agent | try5 | 0.750000 | 0.176471 | 0.285714 | 1.000000 | 0.250000 | 0.400000 | 0.267857 | 0.342857 | `false` | 104.414000 | 23730 | 5 | 5 | 0.393546 |
| amex-default-prediction | tc3_fault_injected | rule_based | try1 | 0.571429 | 0.235294 | 0.333333 | 1.000000 | 0.250000 | 0.400000 | 0.291666 | 0.366667 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| amex-default-prediction | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.176471 | 0.300000 | 1.000000 | 0.500000 | 0.666667 | 0.400000 | 0.483333 | `false` | 69.907000 | 4190 | 1 | 0 | 0.110126 |
| amex-default-prediction | tc3_fault_injected | single_llm | try2 | 0.800000 | 0.235294 | 0.363636 | 1.000000 | 0.500000 | 0.666667 | 0.431818 | 0.515151 | `false` | 58.558000 | 3645 | 1 | 0 | 0.102927 |
| amex-default-prediction | tc3_fault_injected | single_llm | try3 | 0.750000 | 0.176471 | 0.285714 | 1.000000 | 0.500000 | 0.666667 | 0.392857 | 0.476191 | `false` | 57.180000 | 3304 | 1 | 0 | 0.097812 |
| amex-default-prediction | tc3_fault_injected | single_llm | try4 | 0.750000 | 0.176471 | 0.285714 | 1.000000 | 0.750000 | 0.857143 | 0.517857 | 0.571429 | `true` | 60.770000 | 3817 | 1 | 0 | 0.105507 |
| amex-default-prediction | tc3_fault_injected | single_llm | try5 | 1.000000 | 0.235294 | 0.380952 | 1.000000 | 0.500000 | 0.666667 | 0.440476 | 0.523810 | `false` | 55.773000 | 3439 | 1 | 0 | 0.099837 |
| amex-default-prediction | tc4_mixed_history | claude_code | try1 | 1.000000 | 0.071429 | 0.133333 | 1.000000 | 0.666667 | 0.800000 | 0.400000 | 0.466667 | `false` | 288.858311 | 12733 | `null` | 8 | 1.188366 |
| amex-default-prediction | tc4_mixed_history | claude_code | try2 | 1.000000 | 0.071429 | 0.133333 | 1.000000 | 0.666667 | 0.800000 | 0.400000 | 0.466667 | `false` | 183.380224 | 9425 | `null` | 7 | 1.038793 |
| amex-default-prediction | tc4_mixed_history | claude_code | try3 | 1.000000 | 0.071429 | 0.133333 | 1.000000 | 0.333333 | 0.500000 | 0.233333 | 0.316667 | `false` | 217.205608 | 11576 | `null` | 7 | 1.080170 |
| amex-default-prediction | tc4_mixed_history | claude_code | try4 | 1.000000 | 0.071429 | 0.133333 | 1.000000 | 1.000000 | 1.000000 | 0.566666 | 0.566666 | `true` | 122.145020 | 6355 | `null` | 5 | 0.888519 |
| amex-default-prediction | tc4_mixed_history | claude_code | try5 | 1.000000 | 0.071429 | 0.133333 | 1.000000 | 0.666667 | 0.800000 | 0.400000 | 0.466667 | `false` | 160.990699 | 8405 | `null` | 6 | 1.019583 |
| amex-default-prediction | tc4_mixed_history | generic_agent | try1 | 1.000000 | 0.071429 | 0.133333 | 1.000000 | 0.666667 | 0.800000 | 0.400000 | 0.466667 | `false` | 112.515000 | 24899 | 4 | 5 | 0.321925 |
| amex-default-prediction | tc4_mixed_history | generic_agent | try2 | 0.500000 | 0.071429 | 0.125000 | 1.000000 | 1.000000 | 1.000000 | 0.562500 | 0.562500 | `true` | 129.866000 | 22581 | 6 | 7 | 0.376313 |
| amex-default-prediction | tc4_mixed_history | generic_agent | try3 | 0.666667 | 0.142857 | 0.235294 | 1.000000 | 0.666667 | 0.800000 | 0.450981 | 0.517647 | `false` | 132.754000 | 29795 | 8 | 7 | 0.511240 |
| amex-default-prediction | tc4_mixed_history | generic_agent | try4 | 0.666667 | 0.142857 | 0.235294 | 0.666667 | 0.666667 | 0.666667 | 0.450981 | 0.450981 | `false` | 133.188000 | 23457 | 6 | 7 | 0.385718 |
| amex-default-prediction | tc4_mixed_history | generic_agent | try5 | 0.500000 | 0.071429 | 0.125000 | 0.666667 | 0.666667 | 0.666667 | 0.395834 | 0.395834 | `false` | 100.522000 | 23531 | 7 | 7 | 0.428999 |
| amex-default-prediction | tc4_mixed_history | proposed_agent | try1 | 0.750000 | 0.214286 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 205.840000 | 39987 | 5 | 5 | 0.515397 |
| amex-default-prediction | tc4_mixed_history | proposed_agent | try2 | 0.750000 | 0.214286 | 0.333333 | 1.000000 | 0.666667 | 0.800000 | 0.500000 | 0.566666 | `true` | 204.321000 | 29494 | 4 | 3 | 0.443375 |
| amex-default-prediction | tc4_mixed_history | proposed_agent | try3 | 1.000000 | 0.214286 | 0.352941 | 0.666667 | 0.666667 | 0.666667 | 0.509804 | 0.509804 | `true` | 217.898000 | 43361 | 5 | 6 | 0.535107 |
| amex-default-prediction | tc4_mixed_history | proposed_agent | try4 | 0.750000 | 0.214286 | 0.333333 | 1.000000 | 0.666667 | 0.800000 | 0.500000 | 0.566666 | `true` | 179.584000 | 38639 | 5 | 6 | 0.498825 |
| amex-default-prediction | tc4_mixed_history | proposed_agent | try5 | 0.600000 | 0.214286 | 0.315789 | 1.000000 | 1.000000 | 1.000000 | 0.657895 | 0.657895 | `true` | 179.632000 | 27256 | 4 | 4 | 0.419141 |
| amex-default-prediction | tc4_mixed_history | rule_based | try1 | 0.500000 | 0.214286 | 0.300000 | 0.000000 | 0.000000 | 0.000000 | 0.150000 | 0.150000 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| amex-default-prediction | tc4_mixed_history | single_llm | try1 | 0.666667 | 0.142857 | 0.235294 | 1.000000 | 0.666667 | 0.800000 | 0.450981 | 0.517647 | `false` | 66.159000 | 3998 | 1 | 0 | 0.107149 |
| amex-default-prediction | tc4_mixed_history | single_llm | try2 | 0.666667 | 0.142857 | 0.235294 | 1.000000 | 0.666667 | 0.800000 | 0.450981 | 0.517647 | `false` | 61.015000 | 3441 | 1 | 0 | 0.099897 |
| amex-default-prediction | tc4_mixed_history | single_llm | try3 | 0.750000 | 0.214286 | 0.333333 | 1.000000 | 0.666667 | 0.800000 | 0.500000 | 0.566666 | `true` | 53.348000 | 3138 | 1 | 0 | 0.095352 |
| amex-default-prediction | tc4_mixed_history | single_llm | try4 | 0.750000 | 0.214286 | 0.333333 | 1.000000 | 0.666667 | 0.800000 | 0.500000 | 0.566666 | `true` | 66.912000 | 3782 | 1 | 0 | 0.105012 |
| amex-default-prediction | tc4_mixed_history | single_llm | try5 | 0.750000 | 0.214286 | 0.333333 | 1.000000 | 1.000000 | 1.000000 | 0.666667 | 0.666667 | `true` | 79.635000 | 4658 | 1 | 0 | 0.118152 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| amex-default-prediction | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 0.804762 | 0.329412 | 0.465913 | 1.000000 | 1.000000 | 1.000000 | 0.732956 | 0.732956 | 0.000175 | 190.799805 | 9192.800000 | `null` | 11.200000 | 1.111577 |
| amex-default-prediction | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 0.790952 | 0.305882 | 0.439017 | 1.000000 | 1.000000 | 1.000000 | 0.719508 | 0.719508 | 0.000580 | 102.425600 | 21801.200000 | 4.600000 | 5.200000 | 0.400728 |
| amex-default-prediction | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 0.470588 | 0.640000 | 1.000000 | 1.000000 | 1.000000 | 0.820000 | 0.820000 | 0.000000 | 900 | `null` | `null` | `null` | `null` |
| amex-default-prediction | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 0.732381 | 0.258824 | 0.380896 | 1.000000 | 1.000000 | 1.000000 | 0.690448 | 0.690448 | 0.000873 | 155.906000 | 25212.000000 | 4.200000 | 4.600000 | 0.482354 |
| amex-default-prediction | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.500000 | 0.235294 | 0.320000 | 1.000000 | 1.000000 | 1.000000 | 0.660000 | 0.660000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| amex-default-prediction | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 0.683334 | 0.258823 | 0.374261 | 1.000000 | 1.000000 | 1.000000 | 0.687130 | 0.687130 | 0.000699 | 16.450400 | 705.600000 | 1.000000 | 0.000000 | 0.169153 |
| amex-default-prediction | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 0.600000 | 0.046154 | 0.085714 | 1.000000 | 1.000000 | 1.000000 | 0.542857 | 0.542857 | 0.001225 | 206.334834 | 12700.200000 | `null` | 4.400000 | 1.030793 |
| amex-default-prediction | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 0.400000 | 0.061538 | 0.106667 | 0.800000 | 1.000000 | 0.800000 | 0.553333 | 0.453333 | 0.002489 | 99.858400 | 18764.800000 | 4.400000 | 4.000000 | 0.306922 |
| amex-default-prediction | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 0.800000 | 0.169231 | 0.278333 | 0.400000 | 1.000000 | 0.400000 | 0.639167 | 0.339167 | 0.000594 | 162.433800 | 26966.600000 | 4.200000 | 3.400000 | 0.412243 |
| amex-default-prediction | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.428571 | 0.230769 | 0.300000 | 1.000000 | 1.000000 | 1.000000 | 0.650000 | 0.650000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| amex-default-prediction | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 0.666667 | 0.138461 | 0.227059 | 0.800000 | 1.000000 | 0.800000 | 0.613529 | 0.513529 | 0.000574 | 91.021400 | 5185.200000 | 1.000000 | 0.000000 | 0.125833 |
| amex-default-prediction | tc3_fault_injected | claude_code | 5 | `true` | 0.200000 | 0.900000 | 0.094118 | 0.163910 | 1.000000 | 0.750000 | 0.857143 | 0.456954 | 0.510526 | 0.002946 | 138.332140 | 8464.600000 | `null` | 6.400000 | 1.001640 |
| amex-default-prediction | tc3_fault_injected | generic_agent | 5 | `true` | 0.800000 | 0.743333 | 0.176471 | 0.284156 | 1.000000 | 0.750000 | 0.857143 | 0.517078 | 0.570650 | 0.000670 | 99.918000 | 24095.200000 | 4.600000 | 4.600000 | 0.334428 |
| amex-default-prediction | tc3_fault_injected | proposed_agent | 5 | `false` | 0.000000 | 0.730000 | 0.188236 | 0.298701 | 1.000000 | 0.350000 | 0.506667 | 0.324350 | 0.402684 | 0.005319 | 138.626600 | 25049.400000 | 4.600000 | 4.200000 | 0.406252 |
| amex-default-prediction | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.571429 | 0.235294 | 0.333333 | 1.000000 | 0.250000 | 0.400000 | 0.291666 | 0.366667 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| amex-default-prediction | tc3_fault_injected | single_llm | 5 | `true` | 0.200000 | 0.860000 | 0.200000 | 0.323203 | 1.000000 | 0.550000 | 0.704762 | 0.436602 | 0.513983 | 0.001979 | 60.437600 | 3679.000000 | 1.000000 | 0.000000 | 0.103242 |
| amex-default-prediction | tc4_mixed_history | claude_code | 5 | `true` | 0.200000 | 1.000000 | 0.071429 | 0.133333 | 1.000000 | 0.666667 | 0.780000 | 0.400000 | 0.456667 | 0.011111 | 194.515972 | 9698.800000 | `null` | 6.600000 | 1.043086 |
| amex-default-prediction | tc4_mixed_history | generic_agent | 5 | `true` | 0.200000 | 0.666667 | 0.100000 | 0.170784 | 0.866667 | 0.733334 | 0.786667 | 0.452059 | 0.478726 | 0.003614 | 121.769000 | 24852.600000 | 6.200000 | 6.600000 | 0.404839 |
| amex-default-prediction | tc4_mixed_history | proposed_agent | 5 | `true` | 1.000000 | 0.770000 | 0.214286 | 0.333746 | 0.933333 | 0.800000 | 0.853333 | 0.566873 | 0.593540 | 0.006089 | 197.455000 | 35747.400000 | 4.600000 | 4.800000 | 0.482369 |
| amex-default-prediction | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.500000 | 0.214286 | 0.300000 | 0.000000 | 0.000000 | 0.000000 | 0.150000 | 0.150000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| amex-default-prediction | tc4_mixed_history | single_llm | 5 | `true` | 0.600000 | 0.716667 | 0.185714 | 0.294117 | 1.000000 | 0.733334 | 0.840000 | 0.513726 | 0.567059 | 0.006328 | 65.413800 | 3803.400000 | 1.000000 | 0.000000 | 0.105112 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 0.600000 | 0.826191 | 0.135278 | 0.212218 | 1.000000 | 0.854167 | 0.909286 | 0.533192 | 0.560752 | 0.003864 | 182.495688 | 10014.100000 | `null` | 7.150000 | 1.046774 |
| generic_agent | 4 | 1.000000 | 5.000000 | 0.750000 | 0.650238 | 0.160973 | 0.250156 | 0.916667 | 0.870834 | 0.860953 | 0.560495 | 0.555554 | 0.001838 | 105.992750 | 22378.450000 | 4.950000 | 5.100000 | 0.361729 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.470588 | 0.640000 | 1.000000 | 1.000000 | 1.000000 | 0.820000 | 0.820000 | 0.000000 | 900.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 0.750000 | 5.000000 | 0.750000 | 0.758095 | 0.207644 | 0.322919 | 0.833333 | 0.787500 | 0.690000 | 0.555210 | 0.506460 | 0.003219 | 163.605350 | 28243.850000 | 4.400000 | 4.250000 | 0.445804 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.500000 | 0.228911 | 0.313333 | 0.750000 | 0.562500 | 0.600000 | 0.437916 | 0.456667 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 0.700000 | 0.731667 | 0.195750 | 0.304660 | 0.950000 | 0.820833 | 0.836191 | 0.562747 | 0.570425 | 0.002395 | 58.330800 | 3343.300000 | 1.000000 | 0.000000 | 0.125835 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task amex-default-prediction --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/amex-default-prediction-all.md
```
