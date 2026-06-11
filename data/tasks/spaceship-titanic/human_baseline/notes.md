# Human Baseline Notes

- This directory holds the canonical human baseline artifacts for Spaceship Titanic.
- `tc1_human.json` now uses the same bank-id output schema as normal benchmark outputs.
- The current artifact is a re-authored bank-id output built from the executed local notebook in `work.ipynb`.
- `provenance/action_trace.json` maps each selected bank action back to the notebook section that supports it.
- `provenance/metadata.json` records that this is a benchmark-aware reference artifact, not a blinded human study.
- The bank-id output keeps only actions with clear notebook support and defensible mappings into the current benchmark contract.
