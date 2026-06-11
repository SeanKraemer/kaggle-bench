# Manual Decisions Log

This document records the rationale used when `finalizing numeric thresholds` in collection/labeling/QA.

## Log Template

### [YYYY-MM-DD] <competition_or_corpus_scope>
- Scope: (for example, amex-default-prediction / corpus-wide)
- Data scope: (for example, top 100 notebooks, 3 competitions)
- Candidate values:
  - <metric_or_threshold>: [a, b, c]
- Comparison result:
  - Value a: <core metric>
  - Value b: <core metric>
  - Value c: <core metric>
- Final selection:
  - <metric_or_threshold>=<value>
- Selection rationale:
  - <reason 1>
  - <reason 2>
- Sensitivity:
  - <summary of impact when value changes>
- Reproduction commands:
  - `<script and args>`
