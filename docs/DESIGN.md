# KaggleBench Design Notes

Why the benchmark looks the way it does: the problem formulation, the ground-truth pipeline,
the metrics, and what each baseline isolates. The headline results live in the
[README](../README.md); this document explains the machinery behind them.

## The problem: repair, not generation

Most of the practical effort in tabular ML goes into preprocessing and feature engineering, and
most of the *damage* comes from preprocessing that looks plausible but is wrong for the task —
leakage through an encoded target, imputation that erases a signal-bearing missingness pattern,
a time-aware split applied after a shuffle. Existing agent benchmarks largely test writing a
pipeline from a blank slate and score the end model. That misses two things real workflows have:
**history** (you inherit someone's half-finished, partially wrong pipeline) and **action-level
accountability** (knowing *which step* is harmful matters more than nudging a leaderboard
metric).

KaggleBench therefore poses preprocessing as a **repair problem over a constrained action
space**. Given a task context, a dataset profile, a fixed bank of candidate actions, and a set
of currently-active actions, the agent outputs two lists: action IDs to **add** and active
action IDs to **remove**. No free-form code is scored; the action bank is the contract.

Three properties fall out of this formulation:

1. **Deterministic, model-free scoring.** Evaluation is JSON-against-JSON set comparison —
   no LLM judge, no model training, no flaky execution sandbox. 1,700 runs cost API spend only
   at generation time, and re-scoring is free.
2. **Same menu for every system.** The action-bank visibility policy
   ([agent/action_bank.py](../agent/action_bank.py)) strips authoring metadata so every agent
   sees identical candidate actions (ID, type, canonical params) — a rule-based script and a
   commercial coding agent compete on the same footing.
3. **Repair skill is isolated from task knowledge.** All four scenarios of a task share its
   gold actions; only the starting history differs. Score deltas between scenarios measure the
   repair behavior itself.

## Ground truth: distilled from experts, not bootstrapped from models

Gold actions per task come from human review of top-scoring public Kaggle notebooks for that
competition, mapped onto a canonical action vocabulary
([data/schema/canonical_actions.json](../data/schema/canonical_actions.json)). We deliberately
did **not** generate ground truth with an LLM and grade agents against it — that converges on
measuring agreement with the grader model. Kaggle leaderboards give an external, outcome-backed
signal of which preprocessing decisions actually mattered for each dataset.

The authoring pipeline per task: collect candidate notebooks
([data/collector/](../data/collector/), [src/kaggle_benchmark_builder/](../src/kaggle_benchmark_builder/))
→ distill recurring, outcome-relevant preprocessing decisions into gold actions → pad the
candidate bank with distractors drawn from the same vocabulary (plausible-but-wrong or
irrelevant actions, including the harmful ones injected by TC3/TC4) → author the four scenario
testcases → independent review against [task_review_rules.md](../task_review_rules.md) →
build a human baseline with provenance. Banks range from 14 to 137 candidates (median 61;
1,268 total across 20 tasks).

## Scenarios

| Testcase | Active history | What it isolates |
| --- | --- | --- |
| `tc1_from_scratch` | empty | pure add-side recovery |
| `tc2_partial_good` | some gold actions | respecting correct prior work |
| `tc3_fault_injected` | harmful actions | rollback: detect and remove damage |
| `tc4_mixed_history` | gold + harmful mixed | selective editing under ambiguity |

TC3/TC4 are the discriminating scenarios: every LLM-based system scores within noise of the
human reference on TC1, and every system drops 0.15–0.25 in task completion once harmful
actions hide inside otherwise-reasonable history.

## Metrics

Per run, against the testcase's expected adds and removes:

- **Add precision / recall / F1** over predicted add IDs.
- **Remove precision / recall / F1** over predicted remove IDs.
- **Task completion = 0.5 · Add F1 + 0.5 · Remove recall.** Remove *recall* (not F1) on the
  remove side: with a small number of genuinely harmful active actions, missing one is the
  costly error, and remove precision is partially captured by the add side staying clean.
- **Strict completion = 0.5 · Add F1 + 0.5 · Remove F1** — the same blend with remove
  *precision* back in play, so over-removal that the headline metric forgives shows up here.
- **Success** = completion ≥ 0.5; aggregate success rate is the pass rate over task–scenario
  groups (group = task × scenario × agent, best-effort mean over tries).
- **Telemetry**: runtime, tokens, API/tool calls, estimated cost from per-model pricing
  ([agent/llm/pricing.py](../agent/llm/pricing.py)).

Scoring lives in [eval/eval.py](../eval/eval.py); grouping and benchmark-wide aggregation in
[eval/aggregate.py](../eval/aggregate.py) (`--stage-scope primary` scores the curated primary
action set; `all` includes secondary actions).

## What each baseline isolates

| System | Question it answers |
| --- | --- |
| Human reference | What does careful manual review achieve on add-side recovery? |
| `rule_based` | How far do deterministic data-shape heuristics get with zero API cost? |
| `single_llm` | How far does context engineering alone get — one call, no tools, profiles precomputed? |
| `generic_agent` | Does generic tool-use autonomy (inspect, query, iterate) beat a good prompt? |
| `claude_code` | What does a strong commercial coding agent do with the same contract? |
| `proposed_agent` | Does a domain-specific design — separate add and remove passes with preprocessing-aware tools and a reconciliation step — beat both? |

Stochastic systems ran 5 tries per task–scenario; the rule-based system is deterministic and
ran once. The answer the 2026 campaign produced: `single_llm` wins overall (0.777) because
nothing recovered its context-quality-per-dollar, and `proposed_agent` wins exactly where its
design aimed (best TC2, tied-best add F1) while its rollback pass over-removes — informative
in both directions, and reported as measured.

## Threats to validity

- **Curation bias**: gold actions inherit reviewer judgment about which notebook practices
  were load-bearing. A defensible action absent from the gold set scores as a false positive.
- **Action-level ≠ outcome-level**: no models are trained at eval time, so an unconventional
  pipeline that would have worked gets no credit.
- **Human reference covers TC1 only**, bounding add-side but not repair performance.
- **Single model family** powers the LLM baselines at fixed versions; absolute numbers will
  drift with model updates even though the harness, tasks, and scoring are frozen.
