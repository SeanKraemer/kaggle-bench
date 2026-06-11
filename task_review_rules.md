# Task Review Rules

This document records the practical decision rules used while reviewing tasks for the action-bank benchmark.
It is not the machine-checked source of truth for schemas or evaluator behavior.

Use:

- `data/TASK_AUTHORING.md` for authoring-time workflow and artifact expectations
- `data/tasks/<competition_slug>/notes.md` for task-local benchmark notes
- `data/schema/*.json` for machine-checked artifact contracts
- `eval/README.md` for evaluator semantics
- this file for review-time judgment about whether a task artifact set is coherent enough to merge

## 1. Review Goal

The review goal is not to prove that a task is perfect.
The goal is to decide whether the task is:

- internally coherent
- aligned with the current eval contract
- deterministic to score
- reasonable as a benchmark of preprocessing diagnosis and repair over a fixed action bank

When in doubt, prefer:

- deterministic benchmark behavior
- simple bank curation rules
- conservative primary good scope

Avoid adding new evaluator rules just to rescue one task.

## 2. What Counts As A Blocker

Treat an issue as blocking when it causes any of the following:

- the same behavior is simultaneously rewarded and penalized
- a testcase context makes the derived add/remove targets ambiguous or incoherent
- the selected action set cannot admit a valid execution order under the task's hidden precedence rules
- primary good includes clearly non-core or strongly model-specific actions without justification
- example outputs are internally inconsistent with their implied selected action set
- task artifacts no longer match the benchmark contract

Treat an issue as non-blocking when it is mainly:

- a future curation improvement
- a reminder to strengthen provenance later
- a draft artifact that is clearly labeled as draft
- a style preference that does not change evaluation meaning

## 3. Good Candidate Review Rules

### 3.1 Primary Good Should Mean "Omission Should Hurt"

For `core_preprocessing`, the default standard is:

- if the agent fails to recover this action, add-side recall should reasonably drop

Do not put an action in primary good just because:

- it appeared once in a strong notebook
- it is clever
- it helps one model family

Actions that are valid but not broadly core should usually be:

- `model_specific_preprocessing`, or
- `validation_protocol`, or
- kept in notes/provenance but not used to enlarge the primary add-side denominator

### 3.2 Alternatives Should Not Both Count As Independent Add Units

If two good actions represent different ways of handling the same preprocessing need, do not let both contribute independent add-side credit.

Use one of:

- merge to one clearer bank action
- mark as an `equivalence_group`
- narrow one action so the two no longer overlap

Do not keep both as independent primary good units when they are really alternatives.

### 3.3 Good And Bad Candidates Must Not Collapse To The Same Behavior

The same effective behavior must not appear as:

- a good candidate to add, and
- a bad candidate to remove or avoid

If good and bad overlap, fix the bank curation, not the evaluator.

Typical fixes:

- narrow the good candidate
- narrow the bad candidate
- move one candidate out of primary scope
- split an overly broad candidate into clearer units

### 3.4 Good Provenance Should Be Strong, But Review Is Still Manual

Do not add hard cutoff rules just for notebook count.

Use provenance as a review signal:

- many independent refs usually support keeping a good candidate
- single-ref or low-ref good candidates deserve more scrutiny

But final judgment should still be manual.

Keep the benchmark simple:

- no eval-time provenance cutoffs
- no dynamic good filtering

### 3.5 Compact Good Candidates Are Fine If Scoring Stays Deterministic

Compact bank rows are acceptable when scoring semantics remain deterministic.

Examples:

- `ENCODE_CATEGORICAL`
- `IMPUTE_MISSING`
- `DROP_COLUMNS`

Review these for semantic coherence, not for compactness alone.

If a compact action hides mutually incompatible intent, narrow or split it.

### 3.6 Bank Coverage Should Be Broad Across Task-Applicable Canonical Families

Do not curate the bank as if the only meaningful action families are the ones that already appeared in legacy golden/fault artifacts.
Also do not restrict the bank only to strong winner-style actions.

Review with this standard:

- the bank should cover as many task-applicable canonical action families as reasonably possible
- this includes weak, awkward, or non-preferred branches if an agent could plausibly propose them
- the bank should include plausible alternative branches, not only exact legacy targets plus tiny perturbations
- if a reviewer can name a task-applicable canonical family and the bank has no representative for it, the bank is probably still too narrow

Use a narrow exclusion rule:

- exclude a canonical family only when it is clearly inapplicable to the task inputs, table structure, or available columns
- do not exclude a family just because it is low quality, unlikely to win, or not part of the benchmark-preferred path

For Zillow-like tasks, examples of canonical families worth considering include:

- join strategy choices
- datetime parsing and date-derived feature families
- missing-value handling families
- categorical encoding families
- outlier handling families
- destructive drop / pruning families
- scaling / transforms
- bucketization and rare-category handling
- text normalization / text featurization on available text columns
- grouped / temporal feature families when the table structure makes them at least mechanically possible

This is still a review-time judgment, not a machine-checked schema rule.

### 3.7 Action IDs Should Not Leak Labels

`action_id` ordering should be label-neutral.

Review with this standard:

- do not group `good` candidates into one contiguous or easily predictable `action_id` range
- keep `good` and `bad` candidates interleaved enough that `role` is not inferable from id position alone
- if a reviewer can guess `good` vs `bad` from the `action_id` pattern, the candidate ordering is too revealing

This is a curation rule for presentation and information hiding, not an evaluator rule.

### 3.8 Hidden Order Rules Must Preserve At Least One Valid Execution Order

Hidden scoring metadata is acceptable only when it stays coherent.

Review:

- `must_follow_action_ids`
- `invalidates_action_ids`
- `conflicts_with_action_ids`

with this standard:

- if the benchmark expects a set of good actions to coexist, there must be at least one valid execution order for that set

Do not use `conflicts_with_action_ids` for cases that are really salvageable by ordering.
Use true conflict metadata only for combinations that no ordering can rescue.

## 4. Bad Candidate Review Rules

Bad candidates should be:

- plausible mistakes
- harmful enough that remove-side scoring is meaningful
- specific enough to evaluate deterministically

Prefer bad candidates that reflect likely errors such as:

- early destructive drops
- wrong join source or join type
- harmful over-aggressive filtering
- invalid imputation choices
- poor encoding choices for categorical or geographic identifiers

Avoid bad candidates that are really just:

- another valid strategy
- a mild style preference
- only distinguishable by fuzzy semantic interpretation

### 4.1 Synthetic Bad Candidates Are Allowed, But Must Be Traceable

Synthetic bad candidates are fine in the benchmark.

But they should still be reviewable:

- the derivation should be explicit
- the parent good action or notebook evidence should be clear
- the negative should be meaningfully different from the rewarded behavior

Do not allow arbitrary garbage negatives just to increase bank size.

### 4.2 Bank Composition Matters More Than Before

Because every testcase sees the full bank, bad-candidate quality is part of the benchmark itself.

Review for:

- validator hard gate: `bad >= 3 * primary effective good units`
- strong `hard bad` coverage
- enough medium/hard near-miss and distractor style negatives
- no collapse into mostly trivial easy negatives
- each represented canonical action family should have at least `n = 2` nearby bank members, counting the rewarded row if present
- high-salience or benchmark-target canonical action families should usually reach `n = 3`
- "nearby" means same family / same local decision boundary, not just same broad task

Examples:

- a rewarded join action should usually have multiple nearby join alternatives in the bank
- a rewarded sparse-imputation action should usually have multiple nearby fill variants in the bank
- a rewarded encoding action should usually have multiple nearby encoding alternatives in the bank

Do not satisfy this rule with random garbage negatives.
The nearby actions should still be plausible enough that choosing among them says something useful about the agent.

`primary effective good units` means:

- `role = good`
- `eval_stage = core_preprocessing`
- with `equivalence_group` alternatives collapsed to one unit

## 5. Testcase Review Rules

### 5.1 Testcases Inherit Bank Problems

A testcase can be structurally valid and still be wrong because its upstream bank curation is wrong.

Therefore, when the bank changes:

- re-check `context_action_ids`
- re-check the derived add targets
- re-check the derived remove targets
- re-check the active scope interpretation

Do not assume testcase correctness survives a bank change automatically.

### 5.2 Scenario Semantics Should Stay Clear

Use the four standard testcase roles consistently:

- `tc1_from_scratch`: empty context
- `tc2_partial_good`: some good actions already present
- `tc3_fault_injected`: harmful actions present in context
- `tc4_mixed_history`: both good and bad history present

If a testcase no longer feels like its intended scenario after bank edits, refresh it.

### 5.3 Context Should Drive Difficulty Cleanly

Every testcase uses the same full bank.
Therefore testcase difficulty should come from context, not from hand-picked candidate subsets.

Review:

- whether the context clearly changes what should be added
- whether the context clearly changes what should be removed
- whether the context accidentally creates contradictory or degenerate states

### 5.4 Context Should Not Smuggle In Ambiguous Good-State Alternatives

Be careful when context already contains good actions from overlapping families.

If context makes it unclear whether the preprocessing need is already satisfied, fix the bank or the testcase.

Typical fixes:

- collapse alternatives with `equivalence_group`
- narrow the candidate definitions
- simplify the testcase context

## 6. Example Output Review Rules

Example outputs are not just score carriers.
They should also be internally plausible.

Review for:

- valid add/remove membership
- no duplicate ids
- no overlap between add and remove predictions
- implied selected action set coherence
- believable capability differences across baseline types

A good example of a blocking output issue is:

- an output adds a date-feature action while also removing the only required parsed date state, and the selected set admits no valid execution order

That kind of mismatch should be fixed even though the output is now unordered.

Non-blocking output issues are usually:

- stylistic notes that do not change the predicted ids
- omissions that simply make a baseline weaker without making it incoherent

## 7. Human Baseline Review Rules

A human baseline may be merged as a draft if it is clearly labeled as draft.

That is non-blocking when:

- the artifact bundle is internally consistent
- provenance is honest about draft or re-authored status
- the task does not falsely present it as a finalized human benchmark

The benchmark adds one extra review question:

- is the human baseline a true bank-id authoring, or merely a lossy migration from the old canonical-action output

That distinction should be stated explicitly in notes and provenance.

## 8. Report Review Rules

Task and benchmark reports should reflect the current eval contract.

Review reports for:

- correct stage-scope interpretation
- notes that match the current bank curation state
- correct add/remove semantics
- no stale claims after bank, testcase, or human-baseline edits

If curation changes primary good scope, hidden scoring metadata, testcase contexts, or example outputs:

- regenerate the reports

## 9. Preferred Review Workflow

Use this order:

1. Check good/bad bank coherence.
2. Check whether primary good is too broad.
3. Check hidden order metadata for valid-order coherence.
4. Check testcase contexts against the latest bank.
5. Check example outputs for internal consistency and believable gradients.
6. Check human baseline status and honesty.
7. Regenerate validation/tests/reports if anything above changes.

## 10. Practical Biases

These biases should remain intentional in benchmark task reviews:

- keep evaluator rules simple
- prefer curation fixes over evaluator heuristics
- prefer explicit bank semantics over fuzzy rescue logic
- keep primary good conservative
- treat draft or re-authored human baselines as follow-up work unless misrepresented
- only escalate comments that are actionable and materially improve benchmark quality
