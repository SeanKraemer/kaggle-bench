# Human Baseline Notes

- This directory holds the canonical human baseline artifacts for `ashrae-energy-prediction`.
- Initial scope is only `tc1_human`.
- The baseline is `true bank-id authoring`, not a legacy migration.
- The supporting notebook is intentionally `official-only`.
- It implements the conservative primary spine plus a few explicit model-specific branches that are also represented in the current bank.
- It intentionally does not implement:
  - leak filters
  - holiday features
  - public-kernel side inputs
  - grouped interpolation or heavier lag/rolling branches
