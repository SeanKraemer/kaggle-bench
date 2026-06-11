# Data Collection Guide

This document defines the operational standards for building a feature-engineering-centered golden action dataset based on Kaggle competitions.
The core principle is: **collection/download can be automated, but action extraction/labeling requires mandatory manual close reading**.

## 0. Goal

- Goal: Collect high-quality FE notebooks from `50 competitions` and build a competition-level `golden action set (JSON)`.
- Core deliverables:
  - Competition candidate/selection/summary table
  - Competition-level golden action set JSON
  - Canonical action schema (`data/schema/canonical_actions.json`)
  - Canonical change log (`data/collector/canonical_action_decisions.md`)
  - Operational decision log (`data/collector/decisions.md`)

## 1. Competition Collection and Selection

### 1.1 Collection Method (Kaggle CLI)

- Core principles:
  - Only tabular competitions (row/column structure such as `CSV/Parquet`) are in scope.
  - Total size of raw competition data (train/test + core metadata) must be `50GB or less`.
  - Participation scale must be sufficiently large.
  - The Code tab must reliably provide high-quality FE notebooks.
  - Each competition must support collecting at least `30` FE notebooks.
- Example commands:

```bash
kaggle competitions list --csv > data/collector/data/kaggle/competitions_raw.csv
kaggle kernels list --competition <slug> --sort-by scoreDescending --page-size 20 --page 1 --csv
kaggle kernels list --competition <slug> --sort-by voteCount --page-size 100 --page 1 --csv
```

### 1.2 Notebook Selection Rules (Fixed)

Do not use a weighted `quality score` formula. Use the following hard rules.

1. Traverse the Code tab in descending order of `public score`.
2. From the same competition's `most votes` list, get the vote value at `rank 100`.
3. Keep only notebooks with `votes >= votes_at_rank_100`.
4. Exclude notebooks without FE signals from the passing candidates.
5. Continue until at least 30 FE notebooks are collected for the competition.

Supplementary rules:

- FE signal is determined by actual transformation/feature-creation code (missing-value handling, encoding, aggregation, lag/rolling, ratio/interaction, etc.).
- Notebooks focused only on model ensembling/blending are excluded from the FE set.
- Include both `winner_style` and `explanatory_style` notebooks.

### 1.3 Competition Selection Table (Initial)

The following columns are required.

| competition_slug | url | year | summary | teams/participants | reward | difficulty(1-5) | high_quality_fe_notebooks_count | fe_complexity(1-5) | domain |
|---| ---|---:|---|---:|---|---:|---:|---:|---|

- `fe_complexity` guide:
  - 1: mostly missing-value handling/encoding
  - 3: group aggregation + some lag/rolling
  - 5: includes time-series/relational/OOF/complex interactions

## 2. Competition-Level Manual Curation Loop

The basic operating unit is **one competition**.
Complete the following sequence one competition at a time, then move on.

1. Update the competition selection table
2. Save `votes_metadata.csv`
3. Collect raw FE notebooks by traversing public score
4. Manually write `action_candidates.jsonl` after close reading notebooks
5. Generate/validate `golden_actions.json`
6. Update notes/decision logs
7. Check QA gate and then move to the next competition

### 2.1 Per-Competition Collection Deliverables

- `data/collector/data/kaggle/<competition_slug>/notebooks.json`:
  - Notebook summary metadata + `content` text
  - `content` is a single text blob that preserves the original markdown/code cell order.
  - Do not use separated `code`/`markdown` fields; unify into `content`.
- `data/collector/data/kaggle/<competition_slug>/metadata/`:
  - `votes_metadata.csv`
- `data/collector/data/kaggle/<competition_slug>/notebooks/`:
  - Raw notebook files (`.ipynb`, `.py`, and other text files if needed)
- `data/collector/data/golden/<competition_slug>/` (intermediate extraction artifacts):
  - `action_candidates.jsonl`
  - `action_proposals.jsonl`
- `data/tasks/<competition_slug>/` (final task outputs):
  - `golden_actions.json`
  - `notes.md`

### 2.2 Notebook Close Reading and Action Derivation (Mandatory)

- **Directly read** notebook code and map FE/preprocessing actions to canonical actions.
- Reference document: `data/schema/canonical_actions.json`
- Rules:
  - If an existing action expresses the meaning exactly, use it as-is.
  - If the meaning is completely new, add a new canonical action.
  - If it is similar but not general enough, update the existing action schema.
  - Deprecated aliases (`GROUP_AGG_FEATURE`, `GROUP_AGG_JOIN`, `COUNT_ENCODING`, `FREQ_ENCODING`) should be normalized to canonical action names.

### 2.3 Disallowed/Allowed Criteria for Manual Authoring

- Disallowed:
  - Writing estimated actions without reading code
  - Directly applying automated extraction output as final results
  - Using modeling-only notebooks as FE action evidence
- Allowed:
  - Automating candidate collection/filtering and notebook download/caching
  - Using only code snippets directly verified by humans as evidence
  - For uncertain items, conservatively keep them and mark `(estimated)` in `context_notes`

### 2.4 Canonical Change Logging (Required)

When canonical changes occur, record the following in `data/collector/canonical_action_decisions.md`.

- Date
- competition / notebook_ref
- Change type (`add|update|deprecate`)
- Schema before/after change
- Reason for change (need for generalization, leakage prevention, ambiguity resolution)
- Impact scope (whether existing datasets need reprocessing)

### 2.5 Deduplication and Metadata

Deduplication:

- Dedupe by `action_type + canonical_params`
- For semantically identical actions, accumulate provenance only

Required metadata for each action:

- `action_id`
- `action_type`
- `canonical_params`
- `provenance_refs`
- `confidence`
- `rareness`
- `reasoning_summary`
- `evidence_snippets`
- `context_notes` (mark `(estimated)` if uncertain)
- `source_profile` (`winner_style|explanatory_style`)

### 2.6 Parameter Detailing Principles (Required)

- Apply this principle consistently to **all action families**, including numeric/categorical/text/date.
- Do not leave `canonical_params` as placeholders (`all_feature_columns`, `numeric_feature_columns`, etc.).
- Record **only items where the action is actually applied in code**.
  - Include if it is applied in code
  - Exclude if it is not applied in code
- If automatic selection logic is used (`select_dtypes`, skew/distribution-based selection, model-based selection, etc.):
  - Record the selection criteria (logic) in `canonical_params` or `context_notes`.
  - When possible, also record the actual selected column list.
- If column-selection evidence is ambiguous, record the reason and mark `(estimated)` in `context_notes`.
- Note: Do not blanket-exclude/include IDs like `parcelid`, code-like columns such as `regionid*`/`fips`, or coordinates like `latitude`/`longitude`.
  Decide **only by whether the code actually applies the action**.

### 2.7 Handling Conflicting Choices Across Notebooks (Required)

- If notebooks solving the same problem differ on an action choice (for example, label vs one-hot, median vs constant):
  - Do not fix only one option; **record all alternative actions**.
- Keep these alternatives as independent actions, and link `provenance_refs` separately for each action.
- Explicitly mark them as `alternative (OR)` in `context_notes`.
  - Example: `Alternative at same step: A/B; either one can satisfy the requirement`
- Alternative actions are not dedupe targets against each other (if `canonical_params` differ, keep separately).

### 2.8 Execution Unit for Manual Close Reading (Required)

- Perform manual close reading **per notebook** after generating `notebooks.json`.
- Loop rules:
  1. Select exactly one next `notebook_ref`.
  2. Open and read the notebook source in terminal (for example, `cat`, `sed`, `jq`).
  3. Immediately write an initial record to `action_candidates.jsonl` or `action_proposals.jsonl` using only read evidence.
  4. Save and move to the next notebook.
- Move to `golden_actions.json` generation/validation only after all notebooks are processed through this loop.

## 3. Schema Enforcement + Schema Evolution

### 3.1 Schema Enforcement Principles

- Validate golden action JSON with JSON Schema.
- Path: `data/schema/golden_action.schema.json`
- Treat required-field omissions/type errors as failures.

### 3.2 Handling New Actions (Important)

Do not fail the entire save operation just because a new action is discovered.

Processing order:

1. Save new candidates to `data/collector/data/golden/<competition_slug>/action_proposals.jsonl`.
2. Record required additions/updates in `data/collector/canonical_action_decisions.md`.
3. After canonical updates, revalidate/regenerate `golden_actions.json`.

Consistency principles:

- For action naming, prohibit dataset-specific terms.
- Check first whether the meaning duplicates an existing action.
- Prefer merging into a more general definition when possible.

## 4. Labeling Rulebook

The numbers below are `initial proposal values (temporary)`, and final values must be manually confirmed based on real collected data.

### 4.1 Confidence Rubric

- `0.90`: code + explanation + result (score improvement) are all clear
- `0.75`: code is clear, explanation is partially lacking
- `0.60`: code pattern exists but includes contextual inference
- `0.40`: only indirect evidence exists; review required

### 4.2 Rareness Rubric (Within Competition)

- `common`: repeated in at least 20% of FE notebooks
- `uncommon`: at least 5% and below 20%
- `rare`: below 5%

### 4.3 Source Profile Rubric

- `winner_style`: high public score/leaderboard performance, code-centric, short explanation acceptable
- `explanatory_style`: strong explanation of FE rationale and decision context

## 5. Golden Examples (Good/Bad)

### 5.1 Good Examples

1. `GROUP_AGG`
   - Evidence: Creates customer-level transaction statistics (mean/std/max) and joins back to base data.
2. `LAG_FEATURE` + `ROLLING_WINDOW_FEATURE`
   - Evidence: Creates lag 1,2,3 and rolling mean/std based on time order.
3. `TARGET_ENCODE_OOF`
   - Evidence: Creates target encoding with OOF splits (leakage prevention).

### 5.2 Bad Examples

1. A notebook that only performs model ensembling and has no FE code.
2. A case that only swaps the feature-selector model without feature creation/transformation.
3. A case with only transformer object declaration and no `fit/transform` application evidence.

## 6. Numeric Threshold Calibration (Manual)

### 6.1 Principle

- Thresholds (for example, minimum votes rank, confidence cutoff, QA threshold) are not fixed constants.
- Decide them through human comparison/judgment based on real collected data, and document reasons.

### 6.2 Manual Decision Method

- After collecting at least 3 competitions, compare threshold candidates in a table.
- Record pros/cons per candidate (coverage, quality, leakage risk).
- Finalize the selected values in `data/collector/decisions.md`.

### 6.3 Decision Log (Required)

When finalizing numeric values, always record them in `data/collector/decisions.md`.

- Which data was used for judgment
- Comparison table of candidate values
- Final value and reason for selection
- Sensitivity (impact when value changes)

## 7. QA Gate

### 7.1 Competition-Level Gate

- [ ] Confirm that the target competition dataset is tabular
- [ ] Confirm that total target competition raw data size is 50GB or less
- [ ] Secure at least 30 FE notebooks
- [ ] Connect at least one provenance to every golden action
- [ ] 100% schema validation pass rate
- [ ] `action_proposals` processed (0 unresolved)

### 7.2 Corpus-Level Gate

- [ ] Reach 50 competitions
- [ ] Meet distribution conditions for year/domain/difficulty
- [ ] Meet manual sample-validation metrics (use calibration results)
- [ ] Keep `data/collector/canonical_action_decisions.md` and `data/collector/decisions.md` up to date

### 7.3 QA Threshold Decision Method

- Do not lock threshold values as fixed initials.
- Finalize through manual review after collecting at least 3 competitions.
- Record finalized values in `data/reports/qa_threshold_decision.md` and `data/collector/decisions.md`.

## 8. Competition Summary Evaluation Update

After building the golden dataset, add the following columns to the competition table.

| competition_slug | golden_actions_count | unique_action_types | novelty_score(1-5) | reliability_score(1-5) | leakage_risk_notes | notable_fe_patterns |
|---|---:|---:|---:|---:|---|---|

Evaluation guide:

- `novelty_score`: ratio of FE patterns that are novel compared to other competitions
- `reliability_score`: ratio of actions repeatedly validated across many top notebooks
- `leakage_risk_notes`: target usage/time-boundary handling/OOF usage

## 9. Principles for Building a 50-Competition Portfolio

### 9.1 Diversity Axes

- Year diversity: 2017-2019 / 2020-2022 / 2023-present
- Popularity diversity: high / mid / low
- Domain diversity: finance, e-commerce, advertising, time series, healthcare, NLP, recommendation
- Difficulty diversity: evenly across 1-5
- FE novelty diversity: balanced conservative/mid/high-novelty

### 9.2 Recommended Minimum Quotas

- At least 5 per domain
- At least 10 competitions with time-series characteristics
- At least 10 competitions with high leakage risk
- At least 10 competitions with highly novel FE

## 10. Recommended Directory Structure

```text
data/
  schema/
    canonical_actions.json
    golden_action.schema.json
  collector/
    data/
      kaggle/
        competitions_raw.csv
        <competition_slug>/
          notebooks/
          metadata/
            votes_metadata.csv
      golden/
        <competition_slug>/
          action_candidates.jsonl
          action_proposals.jsonl
    scripts/
      collect_competitions.sh
      collect_notebooks.sh
      collect_competitions_and_notebooks.sh
      build_golden_actions.py
    decisions.md
    canonical_action_decisions.md
  reports/
      competitions_overview.md
      competitions_table.csv
      selected_competitions.txt
      notebook_collection_slugs.txt
      qa_threshold_decision.md
  tasks/
    <competition_slug>/
      golden_actions.json
      notes.md
```

## 11. Operating Practices (Mandatory)

- Keep extractor-side work under `data/collector/`, and final task outputs under `data/tasks/`.
- Use `kaggle cli` for competition candidate scraping and notebook downloads.
- In this repository, collection/build steps must run through `data/collector/scripts/` (for example, `collect_competitions.sh`, `collect_notebooks.sh`, `build_golden_actions.py`) rather than ad-hoc replacement scripts.
- Repetitive collection/download/caching work may use automation scripts in `data/collector/scripts/`.
- Save raw notebook files locally for every competition so re-review remains possible.
- Golden actions must record not only extraction results but also the `why` context.
- If reasoning is unclear from notebooks alone, mark it as `(estimated)`.
- After finishing each competition, immediately update and save related md/json files.
- Use both winner-style notebooks and explanatory notebooks.
- Record the basis for `source_profile` classification (public score, votes, explanation depth) in notes.
- For uncertain items, ask the user before proceeding.

## 12. Operating Principles

- Competition collection/filtering and notebook download/caching can be automated.
- Action extraction/labeling/evidence judgment must not be automated and must be done only by manual close reading.
- Conservatively exclude ambiguous actions and leave evidence.
- Keep canonical actions general rather than dataset-specific.
- Every change must always include `documentation + decision log + impact scope`.

## 13. Manual Execution Sequence (Must Be One Competition at a Time)

### 13.1 Prerequisites

```bash
source .venv/bin/activate
kaggle --version
```

### 13.2 Competition Candidate Investigation

```bash
kaggle competitions list --csv > data/collector/data/kaggle/competitions_raw.csv

# Required repository script
data/collector/scripts/collect_competitions.sh
```

Manually create/update:

- `data/reports/competitions_table.csv`
- `data/reports/selected_competitions.txt`
- `data/reports/competitions_overview.md`

### 13.3 Procedure for Processing One Competition

Example: `<slug>`

1. Collect vote-based baseline

```bash
kaggle kernels list --competition <slug> --sort-by voteCount --page-size 100 --page 1 --csv \
  > data/collector/data/kaggle/<slug>/metadata/votes_metadata.csv

# Required repository script (creates votes_metadata.csv + notebooks.json + notebook cache)
data/collector/scripts/collect_notebooks.sh
```

2. Traverse by public score and collect raw notebooks

```bash
kaggle kernels list --competition <slug> --sort-by scoreDescending --page-size 20 --page 1 --csv
kaggle kernels pull <kernel_ref> --path data/collector/data/kaggle/<slug>/notebooks/<kernel_ref_sanitized>
```

3. Run per-notebook close-reading loop and manually write `action_candidates.jsonl`/`action_proposals.jsonl`

- Select one notebook from `notebooks.json`
- Open and read source text, then immediately write candidate/deferred entries
- Save and repeat for the next notebook

4. Generate/validate `golden_actions.json` from `action_candidates.jsonl`

```bash
# Required repository script
python3 data/collector/scripts/build_golden_actions.py --competition <slug>
```

5. Immediately update `data/collector/data/golden/<slug>/action_proposals.jsonl`, `data/tasks/<slug>/notes.md`, and decision logs
6. Confirm QA gate pass, then move to the next competition

### 13.4 `action_candidates.jsonl` Input Spec

Format:

- JSON Lines (one action JSON object per line)

Required (practical):

- `action_type`: string
- `canonical_params`: object (`action_params` may be used instead)
- `provenance_refs`: string[] (at least one) or `notebook_ref`: string
- `evidence_snippets`: string[] (at least one) or `evidence_snippet`: string or `evidence_examples[].raw_snippet`

Recommended:

- `confidence`: number (0~1)
- `source_profile`: `winner_style | explanatory_style`
- `reasoning_summary`: string
- `context_notes`: string

Examples:

```json
{"action_type":"GROUP_AGG","canonical_params":{"group_by_columns":["customer_id"],"target_columns":["amount"],"agg_functions":["mean"],"join_back":true},"notebook_ref":"user/notebook-a","provenance_refs":["user/notebook-a"],"confidence":0.75,"evidence_snippets":["train.groupby('customer_id')['amount'].mean()"],"reasoning_summary":"Derived customer-level average transaction amount","context_notes":"","source_profile":"winner_style"}
{"action_type":"TARGET_ENCODE_OOF","canonical_params":{"columns":["merchant_id"],"target_column":"is_default","cv_strategy":"kfold","n_splits":5},"provenance_refs":["user/notebook-b"],"confidence":0.90,"evidence_snippets":["for trn_idx, val_idx in folds.split(X, y): ..."],"reasoning_summary":"Leakage-safe encoding with OOF splits","context_notes":"","source_profile":"explanatory_style"}
```
