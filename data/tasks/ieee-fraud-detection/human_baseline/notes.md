# Human Baseline Notes

- This directory holds the current IEEE TC1 human baseline artifacts for the action-bank benchmark.
- Initial scope is only `tc1_human`.
- `tc1_human.json` records the exact `CA-*` bank ids manually selected by annotator_a after reviewing every IEEE candidate-action family.
- `tc1_action_selection_workspace.md` is the primary support artifact for this run.
- `work.ipynb` remains a scaffold file and was not used as primary evidence for the final action selection.
- This human output is a manual action-bank review, not a notebook-backed migration from the prior draft baseline.
- Total recorded time for the selection session is `30` minutes.
- Two dependency gaps remain in the chosen set and were intentionally not auto-corrected:
- `CA-000025` was selected without its `must_follow` action `CA-000020`.
- `CA-000029` was selected without its `must_follow` action `CA-000010`.
