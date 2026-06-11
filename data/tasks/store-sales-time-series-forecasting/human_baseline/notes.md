# Store Sales Human Baseline - TC1 Review Notes

## Selection rationale

I treated this as a broad time-series preprocessing pass and selected the steps I would normally reach for first:

- PARSE_DATETIME
- JOIN stores, oil, holidays (left joins)
- APPLY_EXPRESSION oil interpolation
- FILTER transferred missing-or-False / clear transferred holiday labels
- DATE_PART full calendar (year, month, dayofweek, quarter)
- ENCODE_CATEGORICAL label for family
- DROP id

I did not include the transactions join, the oil rolling-window feature, the Work Day holiday cleanup, or grouped sales lag features in this baseline pass. That keeps the run plausible rather than perfect: all four are useful, but they are easier to miss when moving quickly from the competition description to a first feature set.
