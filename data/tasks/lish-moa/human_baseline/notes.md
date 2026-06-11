# Human Baseline Notes

- This directory holds the TC1 human baseline artifacts for LISH-MoA.
- Initial scope is only `tc1_human`.
- `tc1_human.json` uses the output schema in `data/schema/output.schema.json`.
- This is a true bank-ID authoring under the current benchmark contract, not a migration from a legacy action format.
- The human selected from the current `candidate_actions.json` bank after seeing action IDs, action types, canonical parameter summaries, and pros/cons.
- The selection prompt intentionally hid action `role`, `eval_stage`, equivalence groups, expected add targets, and expected remove targets.
- TC1 has an empty context, so the human baseline predicts only add actions and no remove actions.
- No scratch notebook was used for this run.
- Selection time was not instrumented; `tc1_human.json` records a coarse 60-minute estimate so aggregate reports do not treat the human baseline as instantaneous.
