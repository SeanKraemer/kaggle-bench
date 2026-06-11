# Benchmark Aggregate Report

## Configuration

- Stage scope: `all`
- Success threshold: `0.5`
- Tasks included: `icr-identify-age-related-conditions`
- Evaluated run artifacts: `85`
- Evaluated grouped agent/testcase units: `21`

## Benchmark Overview

- Task Success Rate: `0.857143`
- Mean Add Precision: `0.856463`
- Mean Add Recall: `0.534286`
- Mean Add F1: `0.627978`
- Mean Remove Precision: `0.936508`
- Mean Remove Recall: `0.852381`
- Mean Remove F1: `0.845987`
- Mean Task Completion Score: `0.740179`
- Mean Strict Task Completion Score: `0.736982`
- Mean Task Completion Variance: `0.004244`
- Mean Runtime (s): `183.412748`
- Mean Total Tokens: `8122.275000`
- Mean API Calls: `2.537500`
- Mean Tool Calls: `3.380000`
- Mean Cost (USD): `0.093922`

## Task Characteristics

| Task | Metric | Domain | Problem | Table Structure | Dataset Size | Feature Dimensionality | Preprocessing Complexity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| icr-identify-age-related-conditions | balanced_log_loss | biomedical_tabular | binary_classification | multi_table_lookup | small (617) | medium (63) | medium (9) |

## Task Summary

| Task | Groups | Agents | Task Success Rate | Mean k | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| icr-identify-age-related-conditions | 21 | 6 | 0.857143 | 4.047619 | 0.856463 | 0.534286 | 0.627978 | 0.936508 | 0.852381 | 0.845987 | 0.740179 | 0.736982 | 0.004244 | 183.412748 | 8122.275000 | 2.537500 | 3.380000 | 0.093922 |

## Single-Run Artifacts

| Task | Testcase | Agent | Run | Add P | Add R | Add F1 | Remove P | Remove R | Remove F1 | Task Completion | Strict Completion | Success | Time (s) | Tokens | API Calls | Tool Calls | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| icr-identify-age-related-conditions | tc1_from_scratch | claude_code | try1 | 1.000000 | 0.714286 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 92.645379 | 5029 | `null` | 7 | 0.197217 |
| icr-identify-age-related-conditions | tc1_from_scratch | claude_code | try2 | 1.000000 | 0.571429 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | `true` | 113.539840 | 4459 | `null` | 8 | 0.180637 |
| icr-identify-age-related-conditions | tc1_from_scratch | claude_code | try3 | 1.000000 | 0.857143 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 103.991306 | 5373 | `null` | 8 | 0.198300 |
| icr-identify-age-related-conditions | tc1_from_scratch | claude_code | try4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 125.191228 | 6502 | `null` | 8 | 0.217774 |
| icr-identify-age-related-conditions | tc1_from_scratch | claude_code | try5 | 1.000000 | 0.428571 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 97.164885 | 5122 | `null` | 8 | 0.193519 |
| icr-identify-age-related-conditions | tc1_from_scratch | generic_agent | try1 | 1.000000 | 0.857143 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 71.544000 | 11317 | 5 | 5 | 0.111610 |
| icr-identify-age-related-conditions | tc1_from_scratch | generic_agent | try2 | 1.000000 | 0.714286 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 47.482000 | 10813 | 4 | 5 | 0.073616 |
| icr-identify-age-related-conditions | tc1_from_scratch | generic_agent | try3 | 1.000000 | 0.857143 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 47.806000 | 10073 | 6 | 5 | 0.080453 |
| icr-identify-age-related-conditions | tc1_from_scratch | generic_agent | try4 | 1.000000 | 0.714286 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 50.267000 | 7968 | 4 | 5 | 0.062771 |
| icr-identify-age-related-conditions | tc1_from_scratch | generic_agent | try5 | 1.000000 | 0.857143 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 53.227000 | 9113 | 6 | 5 | 0.078447 |
| icr-identify-age-related-conditions | tc1_from_scratch | human | human_tc1_annotator_c_v1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | `true` | 2700 | `null` | `null` | `null` | `null` |
| icr-identify-age-related-conditions | tc1_from_scratch | proposed_agent | try1 | 1.000000 | 0.857143 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 69.304000 | 11351 | 4 | 4 | 0.203985 |
| icr-identify-age-related-conditions | tc1_from_scratch | proposed_agent | try2 | 1.000000 | 0.857143 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 59.117000 | 10115 | 4 | 4 | 0.090241 |
| icr-identify-age-related-conditions | tc1_from_scratch | proposed_agent | try3 | 1.000000 | 0.714286 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 62.150000 | 12327 | 5 | 5 | 0.106437 |
| icr-identify-age-related-conditions | tc1_from_scratch | proposed_agent | try4 | 1.000000 | 0.714286 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 71.211000 | 13404 | 5 | 5 | 0.115211 |
| icr-identify-age-related-conditions | tc1_from_scratch | proposed_agent | try5 | 1.000000 | 0.857143 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 45.385000 | 5835 | 3 | 2 | 0.065127 |
| icr-identify-age-related-conditions | tc1_from_scratch | rule_based | try1 | 0.285714 | 0.285714 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| icr-identify-age-related-conditions | tc1_from_scratch | single_llm | try1 | 1.000000 | 0.857143 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 10.200000 | 574 | 1 | 0 | 0.076507 |
| icr-identify-age-related-conditions | tc1_from_scratch | single_llm | try2 | 1.000000 | 0.857143 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 10.635000 | 585 | 1 | 0 | 0.076672 |
| icr-identify-age-related-conditions | tc1_from_scratch | single_llm | try3 | 1.000000 | 0.857143 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 10.392000 | 606 | 1 | 0 | 0.076987 |
| icr-identify-age-related-conditions | tc1_from_scratch | single_llm | try4 | 1.000000 | 0.714286 | 0.833333 | 1.000000 | 1.000000 | 1.000000 | 0.916667 | 0.916667 | `true` | 8.960000 | 509 | 1 | 0 | 0.075532 |
| icr-identify-age-related-conditions | tc1_from_scratch | single_llm | try5 | 1.000000 | 0.857143 | 0.923077 | 1.000000 | 1.000000 | 1.000000 | 0.961539 | 0.961539 | `true` | 11.672000 | 616 | 1 | 0 | 0.014813 |
| icr-identify-age-related-conditions | tc2_partial_good | claude_code | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 75.947151 | 4140 | `null` | 8 | 0.175019 |
| icr-identify-age-related-conditions | tc2_partial_good | claude_code | try2 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 67.878044 | 3814 | `null` | 9 | 0.169496 |
| icr-identify-age-related-conditions | tc2_partial_good | claude_code | try3 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 96.793319 | 3600 | `null` | 10 | 0.179101 |
| icr-identify-age-related-conditions | tc2_partial_good | claude_code | try4 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 84.214547 | 4438 | `null` | 10 | 0.200110 |
| icr-identify-age-related-conditions | tc2_partial_good | claude_code | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 68.680000 | 3185 | `null` | 6 | 0.146542 |
| icr-identify-age-related-conditions | tc2_partial_good | generic_agent | try1 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 60.871000 | 9597 | 6 | 5 | 0.082483 |
| icr-identify-age-related-conditions | tc2_partial_good | generic_agent | try2 | 1.000000 | 0.500000 | 0.666667 | 1.000000 | 1.000000 | 1.000000 | 0.833333 | 0.833333 | `true` | 55.202000 | 8487 | 5 | 4 | 0.096559 |
| icr-identify-age-related-conditions | tc2_partial_good | generic_agent | try3 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 37.662000 | 5811 | 4 | 3 | 0.052143 |
| icr-identify-age-related-conditions | tc2_partial_good | generic_agent | try4 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 46.627000 | 5951 | 4 | 3 | 0.051730 |
| icr-identify-age-related-conditions | tc2_partial_good | generic_agent | try5 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | `true` | 47.646000 | 5270 | 4 | 3 | 0.050751 |
| icr-identify-age-related-conditions | tc2_partial_good | proposed_agent | try1 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 69.269000 | 9517 | 4 | 3 | 0.092647 |
| icr-identify-age-related-conditions | tc2_partial_good | proposed_agent | try2 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 54.387000 | 6103 | 3 | 1 | 0.068127 |
| icr-identify-age-related-conditions | tc2_partial_good | proposed_agent | try3 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 62.597000 | 12591 | 4 | 3 | 0.094981 |
| icr-identify-age-related-conditions | tc2_partial_good | proposed_agent | try4 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 67.841000 | 12361 | 4 | 3 | 0.096775 |
| icr-identify-age-related-conditions | tc2_partial_good | proposed_agent | try5 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 59.315000 | 6388 | 3 | 2 | 0.070962 |
| icr-identify-age-related-conditions | tc2_partial_good | rule_based | try1 | 0.166667 | 0.250000 | 0.200000 | 0.000000 | 1.000000 | 0.000000 | 0.600000 | 0.100000 | `true` | 0 | `null` | 0 | 0 | 0.000000 |
| icr-identify-age-related-conditions | tc2_partial_good | single_llm | try1 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 9.062000 | 598 | 1 | 0 | 0.013756 |
| icr-identify-age-related-conditions | tc2_partial_good | single_llm | try2 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 8.973000 | 564 | 1 | 0 | 0.013246 |
| icr-identify-age-related-conditions | tc2_partial_good | single_llm | try3 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 22.428000 | 665 | 1 | 0 | 0.014761 |
| icr-identify-age-related-conditions | tc2_partial_good | single_llm | try4 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 10.476000 | 606 | 1 | 0 | 0.013876 |
| icr-identify-age-related-conditions | tc2_partial_good | single_llm | try5 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | `true` | 10.977000 | 603 | 1 | 0 | 0.014682 |
| icr-identify-age-related-conditions | tc3_fault_injected | claude_code | try1 | 1.000000 | 0.285714 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 138.020635 | 7694 | `null` | 7 | 0.245956 |
| icr-identify-age-related-conditions | tc3_fault_injected | claude_code | try2 | 1.000000 | 0.285714 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 131.176824 | 8765 | `null` | 7 | 0.253626 |
| icr-identify-age-related-conditions | tc3_fault_injected | claude_code | try3 | 1.000000 | 0.428571 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 111.154680 | 6556 | `null` | 6 | 0.213080 |
| icr-identify-age-related-conditions | tc3_fault_injected | claude_code | try4 | 1.000000 | 0.285714 | 0.444444 | 1.000000 | 1.000000 | 1.000000 | 0.722222 | 0.722222 | `true` | 100.735143 | 4762 | `null` | 7 | 0.186440 |
| icr-identify-age-related-conditions | tc3_fault_injected | claude_code | try5 | 1.000000 | 0.428571 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 98.448054 | 4494 | `null` | 8 | 0.193957 |
| icr-identify-age-related-conditions | tc3_fault_injected | generic_agent | try1 | 1.000000 | 0.428571 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 87.639000 | 13187 | 4 | 7 | 0.114318 |
| icr-identify-age-related-conditions | tc3_fault_injected | generic_agent | try2 | 1.000000 | 0.428571 | 0.600000 | 1.000000 | 1.000000 | 1.000000 | 0.800000 | 0.800000 | `true` | 60.693000 | 10027 | 5 | 4 | 0.082546 |
| icr-identify-age-related-conditions | tc3_fault_injected | generic_agent | try3 | 1.000000 | 0.285714 | 0.444444 | 1.000000 | 0.500000 | 0.666667 | 0.472222 | 0.555555 | `false` | 89.203000 | 14633 | 4 | 5 | 0.122787 |
| icr-identify-age-related-conditions | tc3_fault_injected | generic_agent | try4 | 1.000000 | 0.428571 | 0.600000 | 1.000000 | 0.750000 | 0.857143 | 0.675000 | 0.728571 | `true` | 81.868000 | 14501 | 5 | 4 | 0.110953 |
| icr-identify-age-related-conditions | tc3_fault_injected | generic_agent | try5 | 1.000000 | 0.428571 | 0.600000 | 1.000000 | 0.750000 | 0.857143 | 0.675000 | 0.728571 | `true` | 108.834000 | 17838 | 5 | 6 | 0.131008 |
| icr-identify-age-related-conditions | tc3_fault_injected | proposed_agent | try1 | 1.000000 | 0.571429 | 0.727273 | 1.000000 | 0.500000 | 0.666667 | 0.613636 | 0.696970 | `true` | 141.318000 | 23467 | 5 | 5 | 0.191638 |
| icr-identify-age-related-conditions | tc3_fault_injected | proposed_agent | try2 | 1.000000 | 0.428571 | 0.600000 | 1.000000 | 0.500000 | 0.666667 | 0.550000 | 0.633333 | `true` | 101.747000 | 13655 | 4 | 3 | 0.128329 |
| icr-identify-age-related-conditions | tc3_fault_injected | proposed_agent | try3 | 1.000000 | 0.285714 | 0.444444 | 1.000000 | 0.500000 | 0.666667 | 0.472222 | 0.555555 | `false` | 127.185000 | 20570 | 5 | 5 | 0.171775 |
| icr-identify-age-related-conditions | tc3_fault_injected | proposed_agent | try4 | 1.000000 | 0.428571 | 0.600000 | 1.000000 | 0.500000 | 0.666667 | 0.550000 | 0.633333 | `true` | 118.630000 | 20720 | 6 | 6 | 0.172177 |
| icr-identify-age-related-conditions | tc3_fault_injected | proposed_agent | try5 | 1.000000 | 0.285714 | 0.444444 | 1.000000 | 0.500000 | 0.666667 | 0.472222 | 0.555555 | `false` | 119.199000 | 18425 | 6 | 7 | 0.166094 |
| icr-identify-age-related-conditions | tc3_fault_injected | rule_based | try1 | 0.333333 | 0.285714 | 0.307692 | 1.000000 | 0.250000 | 0.400000 | 0.278846 | 0.353846 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| icr-identify-age-related-conditions | tc3_fault_injected | single_llm | try1 | 1.000000 | 0.571429 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | `true` | 35.673000 | 2482 | 1 | 0 | 0.041920 |
| icr-identify-age-related-conditions | tc3_fault_injected | single_llm | try2 | 1.000000 | 0.571429 | 0.727273 | 1.000000 | 0.750000 | 0.857143 | 0.738636 | 0.792208 | `true` | 29.321000 | 2076 | 1 | 0 | 0.035830 |
| icr-identify-age-related-conditions | tc3_fault_injected | single_llm | try3 | 1.000000 | 0.571429 | 0.727273 | 1.000000 | 1.000000 | 1.000000 | 0.863636 | 0.863636 | `true` | 32.295000 | 2162 | 1 | 0 | 0.037120 |
| icr-identify-age-related-conditions | tc3_fault_injected | single_llm | try4 | 1.000000 | 0.571429 | 0.727273 | 1.000000 | 0.750000 | 0.857143 | 0.738636 | 0.792208 | `true` | 37.804000 | 2555 | 1 | 0 | 0.043015 |
| icr-identify-age-related-conditions | tc3_fault_injected | single_llm | try5 | 1.000000 | 0.428571 | 0.600000 | 1.000000 | 0.750000 | 0.857143 | 0.675000 | 0.728571 | `true` | 47.954000 | 3088 | 1 | 0 | 0.051987 |
| icr-identify-age-related-conditions | tc4_mixed_history | claude_code | try1 | 1.000000 | 0.800000 | 0.888889 | 1.000000 | 1.000000 | 1.000000 | 0.944445 | 0.944445 | `true` | 130.415435 | 7385 | `null` | 9 | 0.244833 |
| icr-identify-age-related-conditions | tc4_mixed_history | claude_code | try2 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 0.500000 | 0.666667 | 0.535714 | 0.619048 | `true` | 147.381450 | 7897 | `null` | 10 | 0.262634 |
| icr-identify-age-related-conditions | tc4_mixed_history | claude_code | try3 | 1.000000 | 0.800000 | 0.888889 | 1.000000 | 1.000000 | 1.000000 | 0.944445 | 0.944445 | `true` | 130.457538 | 8393 | `null` | 9 | 0.266316 |
| icr-identify-age-related-conditions | tc4_mixed_history | claude_code | try4 | 1.000000 | 0.400000 | 0.571429 | 1.000000 | 0.750000 | 0.857143 | 0.660714 | 0.714286 | `true` | 144.983691 | 8303 | `null` | 10 | 0.273082 |
| icr-identify-age-related-conditions | tc4_mixed_history | claude_code | try5 | 1.000000 | 0.800000 | 0.888889 | 1.000000 | 1.000000 | 1.000000 | 0.944445 | 0.944445 | `true` | 114.005406 | 6696 | `null` | 8 | 0.224277 |
| icr-identify-age-related-conditions | tc4_mixed_history | generic_agent | try1 | 1.000000 | 0.800000 | 0.888889 | 1.000000 | 1.000000 | 1.000000 | 0.944445 | 0.944445 | `true` | 71.948000 | 12929 | 5 | 6 | 0.100484 |
| icr-identify-age-related-conditions | tc4_mixed_history | generic_agent | try2 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 0.750000 | 0.857143 | 0.750000 | 0.803571 | `true` | 69.110000 | 12144 | 6 | 7 | 0.102824 |
| icr-identify-age-related-conditions | tc4_mixed_history | generic_agent | try3 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 0.750000 | 0.857143 | 0.750000 | 0.803571 | `true` | 69.439000 | 12080 | 5 | 6 | 0.096940 |
| icr-identify-age-related-conditions | tc4_mixed_history | generic_agent | try4 | 1.000000 | 0.800000 | 0.888889 | 1.000000 | 1.000000 | 1.000000 | 0.944445 | 0.944445 | `true` | 68.073000 | 16248 | 4 | 5 | 0.103778 |
| icr-identify-age-related-conditions | tc4_mixed_history | generic_agent | try5 | 1.000000 | 0.800000 | 0.888889 | 1.000000 | 1.000000 | 1.000000 | 0.944445 | 0.944445 | `true` | 94.468000 | 17407 | 5 | 7 | 0.128315 |
| icr-identify-age-related-conditions | tc4_mixed_history | proposed_agent | try1 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 0.250000 | 0.400000 | 0.291666 | 0.366667 | `false` | 129.201000 | 16776 | 4 | 3 | 0.153100 |
| icr-identify-age-related-conditions | tc4_mixed_history | proposed_agent | try2 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 0.500000 | 0.666667 | 0.416666 | 0.500000 | `false` | 108.597000 | 14053 | 4 | 3 | 0.129271 |
| icr-identify-age-related-conditions | tc4_mixed_history | proposed_agent | try3 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 0.500000 | 0.666667 | 0.416666 | 0.500000 | `false` | 112.843000 | 17688 | 5 | 4 | 0.143282 |
| icr-identify-age-related-conditions | tc4_mixed_history | proposed_agent | try4 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 0.500000 | 0.666667 | 0.416666 | 0.500000 | `false` | 110.017000 | 18863 | 5 | 4 | 0.150178 |
| icr-identify-age-related-conditions | tc4_mixed_history | proposed_agent | try5 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 0.500000 | 0.666667 | 0.416666 | 0.500000 | `false` | 107.549000 | 13766 | 4 | 3 | 0.127894 |
| icr-identify-age-related-conditions | tc4_mixed_history | rule_based | try1 | 0.200000 | 0.200000 | 0.200000 | 0.666667 | 0.500000 | 0.571429 | 0.350000 | 0.385714 | `false` | 0 | `null` | 0 | 0 | 0.000000 |
| icr-identify-age-related-conditions | tc4_mixed_history | single_llm | try1 | 1.000000 | 0.800000 | 0.888889 | 1.000000 | 0.750000 | 0.857143 | 0.819445 | 0.873016 | `true` | 42.157000 | 2755 | 1 | 0 | 0.045919 |
| icr-identify-age-related-conditions | tc4_mixed_history | single_llm | try2 | 1.000000 | 0.800000 | 0.888889 | 1.000000 | 1.000000 | 1.000000 | 0.944445 | 0.944445 | `true` | 34.619000 | 2330 | 1 | 0 | 0.039544 |
| icr-identify-age-related-conditions | tc4_mixed_history | single_llm | try3 | 1.000000 | 0.800000 | 0.888889 | 1.000000 | 1.000000 | 1.000000 | 0.944445 | 0.944445 | `true` | 36.335000 | 2448 | 1 | 0 | 0.041314 |
| icr-identify-age-related-conditions | tc4_mixed_history | single_llm | try4 | 1.000000 | 0.600000 | 0.750000 | 1.000000 | 0.500000 | 0.666667 | 0.625000 | 0.708333 | `true` | 29.215000 | 2082 | 1 | 0 | 0.035824 |
| icr-identify-age-related-conditions | tc4_mixed_history | single_llm | try5 | 1.000000 | 0.800000 | 0.888889 | 1.000000 | 0.750000 | 0.857143 | 0.819445 | 0.873016 | `true` | 29.895000 | 1902 | 1 | 0 | 0.034227 |

## Grouped Agent/Testcase Results

| Task | Testcase | Agent | k | Pass@k | Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| icr-identify-age-related-conditions | tc1_from_scratch | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.714286 | 0.816737 | 1.000000 | 1.000000 | 1.000000 | 0.908368 | 0.908368 | 0.005007 | 106.506527 | 5297.000000 | `null` | 7.800000 | 0.197489 |
| icr-identify-age-related-conditions | tc1_from_scratch | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.800000 | 0.887179 | 1.000000 | 1.000000 | 1.000000 | 0.943590 | 0.943590 | 0.000483 | 54.065200 | 9856.800000 | 5.000000 | 5.000000 | 0.081379 |
| icr-identify-age-related-conditions | tc1_from_scratch | human | 1 | `true` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 2700 | `null` | `null` | `null` | `null` |
| icr-identify-age-related-conditions | tc1_from_scratch | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.800000 | 0.887179 | 1.000000 | 1.000000 | 1.000000 | 0.943590 | 0.943590 | 0.000483 | 61.433400 | 10606.400000 | 4.200000 | 4.000000 | 0.116200 |
| icr-identify-age-related-conditions | tc1_from_scratch | rule_based | 1 | `true` | 1.000000 | 0.285714 | 0.285714 | 0.285714 | 1.000000 | 1.000000 | 1.000000 | 0.642857 | 0.642857 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| icr-identify-age-related-conditions | tc1_from_scratch | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.828572 | 0.905128 | 1.000000 | 1.000000 | 1.000000 | 0.952565 | 0.952565 | 0.000322 | 10.371800 | 578.000000 | 1.000000 | 0.000000 | 0.064103 |
| icr-identify-age-related-conditions | tc2_partial_good | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.250000 | 0.400000 | 1.000000 | 1.000000 | 1.000000 | 0.700000 | 0.700000 | 0.000000 | 78.702612 | 3835.400000 | `null` | 8.600000 | 0.174054 |
| icr-identify-age-related-conditions | tc2_partial_good | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.300000 | 0.453333 | 1.000000 | 1.000000 | 1.000000 | 0.726667 | 0.726667 | 0.002844 | 49.601600 | 7023.200000 | 4.600000 | 3.600000 | 0.066733 |
| icr-identify-age-related-conditions | tc2_partial_good | proposed_agent | 5 | `true` | 1.000000 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | 0.000000 | 62.681800 | 9392.000000 | 3.600000 | 2.400000 | 0.084698 |
| icr-identify-age-related-conditions | tc2_partial_good | rule_based | 1 | `true` | 1.000000 | 0.166667 | 0.250000 | 0.200000 | 0.000000 | 1.000000 | 0.000000 | 0.600000 | 0.100000 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| icr-identify-age-related-conditions | tc2_partial_good | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.750000 | 0.857143 | 1.000000 | 1.000000 | 1.000000 | 0.928571 | 0.928571 | 0.000000 | 12.383200 | 607.200000 | 1.000000 | 0.000000 | 0.014064 |
| icr-identify-age-related-conditions | tc3_fault_injected | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.342857 | 0.506666 | 1.000000 | 1.000000 | 1.000000 | 0.753333 | 0.753333 | 0.001452 | 115.907067 | 6454.200000 | `null` | 7.000000 | 0.218612 |
| icr-identify-age-related-conditions | tc3_fault_injected | generic_agent | 5 | `true` | 0.800000 | 1.000000 | 0.400000 | 0.568889 | 1.000000 | 0.800000 | 0.876191 | 0.684444 | 0.722539 | 0.014385 | 85.647400 | 14037.200000 | 4.600000 | 5.200000 | 0.112322 |
| icr-identify-age-related-conditions | tc3_fault_injected | proposed_agent | 5 | `true` | 0.600000 | 1.000000 | 0.400000 | 0.563232 | 1.000000 | 0.500000 | 0.666667 | 0.531616 | 0.614949 | 0.002892 | 121.615800 | 19367.400000 | 5.200000 | 5.200000 | 0.166003 |
| icr-identify-age-related-conditions | tc3_fault_injected | rule_based | 1 | `false` | 0.000000 | 0.333333 | 0.285714 | 0.307692 | 1.000000 | 0.250000 | 0.400000 | 0.278846 | 0.353846 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| icr-identify-age-related-conditions | tc3_fault_injected | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.542857 | 0.701818 | 1.000000 | 0.850000 | 0.914286 | 0.775909 | 0.808052 | 0.005671 | 36.609400 | 2472.600000 | 1.000000 | 0.000000 | 0.041975 |
| icr-identify-age-related-conditions | tc4_mixed_history | claude_code | 5 | `true` | 1.000000 | 1.000000 | 0.640000 | 0.761905 | 1.000000 | 0.850000 | 0.904762 | 0.805953 | 0.833334 | 0.030333 | 133.448704 | 7734.800000 | `null` | 9.200000 | 0.254228 |
| icr-identify-age-related-conditions | tc4_mixed_history | generic_agent | 5 | `true` | 1.000000 | 1.000000 | 0.720000 | 0.833333 | 1.000000 | 0.900000 | 0.942857 | 0.866667 | 0.888095 | 0.009074 | 74.607600 | 14161.600000 | 5.000000 | 6.200000 | 0.106468 |
| icr-identify-age-related-conditions | tc4_mixed_history | proposed_agent | 5 | `false` | 0.000000 | 1.000000 | 0.200000 | 0.333333 | 1.000000 | 0.450000 | 0.613334 | 0.391666 | 0.473333 | 0.002500 | 113.641400 | 16229.200000 | 4.400000 | 3.400000 | 0.140745 |
| icr-identify-age-related-conditions | tc4_mixed_history | rule_based | 1 | `false` | 0.000000 | 0.200000 | 0.200000 | 0.200000 | 0.666667 | 0.500000 | 0.571429 | 0.350000 | 0.385714 | 0.000000 | 0 | `null` | 0 | 0 | 0.000000 |
| icr-identify-age-related-conditions | tc4_mixed_history | single_llm | 5 | `true` | 1.000000 | 1.000000 | 0.760000 | 0.861111 | 1.000000 | 0.800000 | 0.876191 | 0.830556 | 0.868651 | 0.013688 | 34.444200 | 2303.400000 | 1.000000 | 0.000000 | 0.039366 |

## Agent Summary

| Agent | Groups | Task Success Rate | Mean k | Mean Run Success Rate | Mean Add P | Mean Add R | Mean Add F1 | Mean Remove P | Mean Remove R | Mean Remove F1 | Mean Task Completion | Mean Strict Completion | Mean Variance | Mean Time (s) | Mean Tokens | Mean API Calls | Mean Tool Calls | Mean Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude_code | 4 | 1.000000 | 5.000000 | 1.000000 | 1.000000 | 0.486786 | 0.621327 | 1.000000 | 0.962500 | 0.976190 | 0.791913 | 0.798759 | 0.009198 | 108.641227 | 5830.350000 | `null` | 8.150000 | 0.211096 |
| generic_agent | 4 | 1.000000 | 5.000000 | 0.950000 | 1.000000 | 0.555000 | 0.685684 | 1.000000 | 0.925000 | 0.954762 | 0.805342 | 0.820223 | 0.006697 | 65.980450 | 11269.700000 | 4.800000 | 5.000000 | 0.091726 |
| human | 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 2700.000000 | `null` | `null` | `null` | `null` |
| proposed_agent | 4 | 0.750000 | 5.000000 | 0.650000 | 1.000000 | 0.537500 | 0.660222 | 1.000000 | 0.737500 | 0.820000 | 0.698861 | 0.740111 | 0.001469 | 89.843100 | 13898.750000 | 4.350000 | 3.750000 | 0.126912 |
| rule_based | 4 | 0.500000 | 1.000000 | 0.500000 | 0.246428 | 0.255357 | 0.248352 | 0.666667 | 0.687500 | 0.492857 | 0.467926 | 0.370604 | 0.000000 | 0.000000 | `null` | 0.000000 | 0.000000 | 0.000000 |
| single_llm | 4 | 1.000000 | 5.000000 | 1.000000 | 1.000000 | 0.720357 | 0.831300 | 1.000000 | 0.912500 | 0.947619 | 0.871900 | 0.889460 | 0.004920 | 23.452150 | 1490.300000 | 1.000000 | 0.000000 | 0.039877 |

## Reproducible Commands

```bash
uv run python eval/scripts/validate_artifacts.py
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
uv run python eval/aggregate.py --task icr-identify-age-related-conditions --stage-scope all --format markdown --success-threshold 0.5 --output eval/results/benchmarks/icr-identify-age-related-conditions-all.md
```
