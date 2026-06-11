# Data Documentation

## 1) Canonical Action

Canonical actions are general-purpose preprocessing and feature-engineering actions for tabular supervised ML.
The purpose is to define a finite action set that a data preprocessing agent can choose from.

- Source of truth: `data/schema/canonical_actions.json`
- If an observed action is not covered, either:
  - extend an existing action with additional parameters, or
  - add a new canonical action
- If you find low-quality definitions (for example: duplicates, overly generic actions, ambiguous actions), update the canonical action set

## 2) About `tasks/` and How to Add a Task

For the current task authoring and evaluation artifact conventions, see `data/TASK_AUTHORING.md`.

### Directory structure

- Add each competition under `data/tasks/<competition_slug>/`
- Each competition directory must contain:
  - `golden_actions.json` (must follow `data/schema/golden_action.schema.json`)
  - `notes.md` (task context and summary of decisions)
- `data/reports/` stores organized information about competitions that exist in `data/tasks/`
- For required report content, follow `data/collector/data_collection_guide.md`

### Task onboarding workflow

1. Create a new branch before starting work.
   - Example: `git checkout -b codex/add-task-<competition-slug>`
2. Ask an agent (for example, Claude Code or Codex) to add one golden dataset in `data/tasks/` by following `data/collector/data_collection_guide.md`.
   - If you do not specify a dataset, the agent should choose a competition with many feature-engineering notebooks and high participation.
   - You may also explicitly specify the competition.
   - Prerequisites: Kaggle CLI installed and Kaggle API key configured.
   - Require use of repository scripts in `data/collector/scripts/` for collection/build steps.
   - Expected deliverables:
     - one new competition directory under `data/tasks/`
     - updated competition table under `data/reports/`
     - raw/intermediate artifacts saved under `data/collector/data/`
3. Most important: manually review the generated `golden_actions.json`.
   - Confirm each action is truly present in evidence notebooks.
   - Confirm input arguments (for example, column names) are explicit and correct.
   - Confirm the full action set is reasonable and internally consistent for the task.
4. Open a separate AI session and ask for an independent review of the golden dataset JSON.
   - Provide the same context used for human review (canonical actions, golden actions, evidence notebooks, etc.).
5. Open a PR and request review.
   - After opening the PR, automated tests should run.

### Example: adding `zillow-prize-1`

1. Prompt to the agent (first run)

```text
Add one golden task for Kaggle competition `zillow-prize-1` by following
`data/collector/data_collection_guide.md` exactly.

Deliverables:
- `data/tasks/zillow-prize-1/golden_actions.json`
- `data/tasks/zillow-prize-1/notes.md`
- update competition table/report files under `data/reports/`
- save raw/intermediate artifacts under `data/collector/data/`

Requirements:
- use `data/schema/canonical_actions.json` as source of truth
- ensure `golden_actions.json` conforms to `data/schema/golden_action.schema.json`
- do not skip manual close reading rules from the guide
- run collection/build via `data/collector/scripts/collect_notebooks.sh` and `python3 data/collector/scripts/build_golden_actions.py --competition zillow-prize-1` (no ad-hoc replacement scripts)
```

2. Prompt to AI for independent review (after manual review)

```text
Independently review this golden action dataset for `zillow-prize-1`.

Context files:
- canonical actions: `data/schema/canonical_actions.json`
- golden actions: `data/tasks/zillow-prize-1/golden_actions.json`
- notes: `data/tasks/zillow-prize-1/notes.md`
- collection guide: `data/collector/data_collection_guide.md`
- evidence notebooks/raw artifacts under `data/collector/data/kaggle/zillow-prize-1/`

Review checklist:
1) Is each action grounded in notebook evidence?
2) Are action arguments (especially column names) explicit and correct?
3) Any duplicated, over-generic, or missing actions?
4) Any schema or consistency issues?

Return:
- findings grouped by severity
- exact action IDs/fields to fix
- concrete patch suggestions
```

3. After opening PR, check on the web

- Confirm all CI checks are completed and passing.
- Confirm changed files match expected deliverables only.
- Request reviewers.
- Confirm no unresolved review comments before merge.
