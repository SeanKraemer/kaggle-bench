# Sberbank Human Baseline Notes

- Benchmark contract: working manual label against the current `candidate_actions.json`
- Migration status: not a legacy exact-match migration
- Scope: `tc1_from_scratch` only
- Author: `annotator_a`

## Selection heuristic

- Record the actions manually selected during the current review pass, even when they mix core and model-specific branches.
- Keep the file synchronized with the actual `predicted_add_action_ids` in `tc1_human.json`.
- Treat this as a working human label state, not a finalized exact-match notebook reconstruction.

## Current Selection Snapshot

- Selected add actions: `31`
- Selected remove actions: `0`
- The current working set spans:
  - value cleanup and clipping
  - pruning and duplicate handling
  - timestamp parsing and date parts
  - macro join variants and grouped counts
  - categorical mappings and ordinalization
  - predictor and target transforms
  - housing ratio features

## Status

- This artifact is an in-progress human labeling pass.
- The notebook placeholder and provenance trace exist to keep the artifact set synchronized, but the manual selection may still change.
