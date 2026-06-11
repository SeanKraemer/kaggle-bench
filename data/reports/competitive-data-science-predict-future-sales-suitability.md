# `competitive-data-science-predict-future-sales` Phase 1 Suitability Memo

Date: `2026-04-13`

## Scope

- Official competition only
- Target task characteristics:
  - `problem_type = forecasting`
  - `table_structure = multi_table_relational`
  - `ml_domain = retail_time_series_tabular`

## Official Files And Dataset Shape

Official competition file descriptions confirm the required file set exists:

- `sales_train.csv`
- `test.csv`
- `items.csv`
- `item_categories.csv`
- `shops.csv`
- `sample_submission.csv`

Observed public shape summary for the official files:

| File | Role | Rows x Cols | Notes |
|---|---|---:|---|
| `sales_train.csv` | Daily training transactions | `2,935,849 x 6` | Includes `date`, `date_block_num`, `shop_id`, `item_id`, `item_price`, `item_cnt_day` |
| `test.csv` | November 2015 prediction pairs | `214,200 x 3` | Contains `(ID, shop_id, item_id)` |
| `items.csv` | Item lookup | `22,170 x 3` | Includes `item_category_id` |
| `item_categories.csv` | Category lookup | `84 x 2` | Category id + name |
| `shops.csv` | Shop lookup | `60 x 2` | Shop id + name |
| `sample_submission.csv` | Submission template | `214,200 x 2` | Inferred from the one-to-one `ID` mapping with `test.csv` |

Assessment:

- This is clearly tabular supervised ML.
- The tables are relational and joinable through stable keys.
- The official raw data volume is far below the collector QA gate of `50GB`.
  - Public notebook inspection shows `sales_train.csv` alone loads to about `134.4 MB` in memory, and the remaining official tables are KB-to-low-MB scale.

## Notebook Supply

Result: sufficient to continue.

Evidence:

- The competition is the final project for the Coursera course “How to Win a Data Science Competition”, which materially increases public notebook supply and tutorial-style writeups.
- Web search surfaced multiple distinct Kaggle code notebooks directly tied to this competition, including:
  - `Predict Future Sales - LightGBM`
  - `Predict Future Sales using Catboost`
  - `Top 1% Predict Future Sales, features + LightGBM`
  - `Predict Future Sales | CatBoost`
- Public writeups also show deep FE-heavy pipelines rather than model-only solutions.

Assessment:

- I cannot directly count Kaggle notebooks from this machine because the local `kaggle` CLI is not installed.
- Based on the visible public Kaggle code supply plus the course-final-project nature of the competition, I assess the `>= 30` FE/preprocessing-notebook target as achievable.
- This is an inference, but it is a strong one.

## Canonical-Action Fit

Result: sufficient to continue, with one caveat.

Current canonical actions already cover the main benchmark spine needed for an official-only version of this task:

| Workflow need | Canonical action fit |
|---|---|
| Parse raw sales dates | `PARSE_DATETIME` |
| Extract year / month style date parts | `DATE_PART_FEATURE` |
| Aggregate daily sales to month level | `GROUP_AGG` |
| Join item / category / shop lookup metadata | `JOIN_LOOKUP` |
| Build monthly history features | `LAG_FEATURE` |
| Build trailing statistics | `ROLLING_WINDOW_FEATURE` |
| Build elapsed-time / recency style features | `TIME_SINCE_REFERENCE` |
| Fill lag/aggregate nulls conservatively | `IMPUTE_MISSING` |

Important caveat:

- The common `shop-item-month` full grid expansion pattern does **not** currently have a first-class canonical action.
- That is not a Phase 1 blocker, because the rest of the forecasting pipeline is well covered by the existing ontology.
- It **is** a Phase 2 curation constraint:
  - do not model full cartesian grid construction as a standalone primary-good action unless the ontology is extended first
  - instead, treat it as a composite workflow assumption documented in `notes.md` and supported by surrounding aggregation / join / fill actions

Assessment:

- No new evaluator rule is required.
- No schema change is required for Phase 2 to proceed.
- The benchmark can remain within the current tabular-first contract.

## External Data Policy

External data should be excluded from the benchmark scope.

Reasoning:

- Official-only pipelines already exist and are strong enough to define a deterministic benchmark spine:
  - daily-to-monthly aggregation
  - lookup joins
  - lag features
  - grouped monthly statistics
  - time-aware validation
- Excluding external data keeps the task aligned with the current evaluator contract and avoids avoidable ambiguity in provenance and action applicability.

Decision:

- `external data excluded = yes`
- external-data notebooks may still be consulted during review as background context, but they should not define primary good actions

## Final Go/No-Go Decision

Decision: `GO`

Why this is a go:

- The competition is tabular and fits the current benchmark contract.
- The official file set is complete and relational.
- The raw data size is comfortably inside the collector QA gate.
- The public notebook ecosystem appears strong enough to support the required evidence collection.
- The core official-only workflow is feasible without external data.
- Primary good can be made conservative and deterministic without changing evaluator behavior.

Phase 2 note:

- Keep the benchmark official-only.
- Keep `raw daily -> monthly aggregation -> lag/history features` as the spine.
- Treat full grid completion as a documented workflow assumption or composite pattern, not as a standalone canonical action row unless ontology changes are made first.

## Operational Note

This machine currently does not have a working `kaggle` CLI on `PATH`, so Phase 2 collection work will need either:

- Kaggle CLI installation/configuration, or
- another approved way to fetch competition notebooks and metadata

This is an environment issue, not a suitability blocker.

## Sources

- Official competition task summary mirror: <https://huggingface.co/datasets/OPT-Bench/OPT-Bench/blob/main/example_tasks/competitive-data-science-predict-future-sales/competitive-data-science-predict-future-sales.md>
- Public competition walkthrough with file shapes and FE pipeline: <https://tdody.github.io/Sales-Forecast/>
- Representative Kaggle code search results:
  - <https://www.kaggle.com/code/valentingerbet/predict-future-sales-lightgbm>
  - <https://www.kaggle.com/code/weiwsc/predict-future-sales-using-catboost>
  - <https://www.kaggle.com/code/deinforcement/top-1-predict-future-sales-features-lightgbm>
  - <https://www.kaggle.com/code/ahmedabdulhamid/predict-future-sales-catboost/notebook>
