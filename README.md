# Kaggle Bench

Kaggle Bench is a benchmark for evaluating whether data-science agents can repair tabular preprocessing plans. Each task gives an agent a Kaggle competition context, a dataset profile, a constrained action bank, and a scenario describing which preprocessing actions are already active. The agent predicts which useful actions to add and which harmful prior actions to remove.

This is a private portfolio copy of a team-origin research project. It preserves the benchmark code, task definitions, schemas, fixtures, and compact reports while keeping generated raw run artifacts out of the public-ready tree.

## What It Evaluates

Each task has four scenario styles:

- `tc1_from_scratch`: no prior preprocessing actions.
- `tc2_partial_good`: some useful actions are already active.
- `tc3_fault_injected`: harmful prior actions should be removed.
- `tc4_mixed_history`: useful and harmful prior actions are mixed.

Outputs are scored as edits over a fixed candidate action bank:

- `predicted_add_action_ids` for actions to add.
- `predicted_remove_action_ids` for harmful active actions to remove.

The evaluator reports add/remove precision, recall, F1, task completion, strict completion, runtime, token usage, API calls, tool calls, and estimated cost when those fields are present.

## Repository Structure

```text
agent/                              Agent implementations, prompts, tools, and tests
data/schema/                        JSON schemas and canonical action vocabulary
data/tasks/<slug>/                  Task bundles, action banks, testcases, notes, fixtures
data/reports/                       Competition registry and collection reports
data/collector/                     Notebook collection and task-authoring utilities
eval/eval.py                        Single-output evaluator
eval/aggregate.py                   Aggregate benchmark report generator
eval/results/                       Compact generated benchmark summaries and figures
eval/scripts/validate_artifacts.py  Repository-wide benchmark artifact validator
```

Raw Kaggle datasets, notebook collection intermediates, and high-volume agent run outputs are not committed. See [ARTIFACT_POLICY.md](ARTIFACT_POLICY.md).

## Setup

Install `uv`, then sync the development environment:

```bash
brew install uv
uv sync --dev
```

Register pre-commit hooks:

```bash
uv run pre-commit install
```

Run configured checks:

```bash
uv run pre-commit run --all-files
```

## Kaggle Credentials

Kaggle credentials are required only when collecting notebooks or downloading raw competition data. Use Kaggle legacy API credentials and keep them outside the repository:

```bash
uv pip install kaggle
mkdir -p ~/.kaggle
# Place kaggle.json from Kaggle Settings -> API -> Create New Token
chmod 600 ~/.kaggle/kaggle.json
```

Do not commit Kaggle credentials, downloaded datasets, notebook caches, or generated agent traces.

## Validation

Run evaluator unit tests:

```bash
uv run python -m unittest discover -s eval/tests -p 'test_*.py'
```

Run the full artifact validator only after restoring generated task outputs:

```bash
uv run python eval/scripts/validate_artifacts.py
```

Regenerate one benchmark report from available outputs:

```bash
uv run python eval/aggregate.py --task zillow-prize-1 --stage-scope primary --format markdown --success-threshold 0.5 --output eval/results/benchmarks/zillow-prize-1-primary.md
```

## Portfolio Notes

This project was built collaboratively. Before public release, keep collaborator attribution visible, replace remaining absolute-path documentation links with repository-relative links, and decide whether generated result summaries should be regenerated from a clean artifact bundle.
