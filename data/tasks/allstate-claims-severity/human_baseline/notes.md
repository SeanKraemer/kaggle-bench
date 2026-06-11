# Allstate Claims Severity Human Baseline Notes

This is my simple TC1 human baseline for Allstate after the task was migrated to the current action-bank format.
I used the migrated notebook notes and candidate bank as references, but I did not try to reconstruct the full curated answer key.

## Key Choices

| Decision | My choice |
|----------|-----------|
| Drop id column CA-000001? | Yes |
| Label encode CA-000005 or one-hot CA-000014 for cat1-cat116? | CA-000005 (label) |
| Add np.log CA-000009 or log1p CA-000027 target transform? | No, omitted from this simple baseline |

## TC1 Selection Rationale

I selected two actions:

- DROP_COLUMNS id (CA-000001)
- ENCODE_CATEGORICAL label encode cat1-cat116, fit on train+test levels (CA-000005)

I intentionally stopped there. A stronger Allstate workflow should log-transform the target, but I left that out so this artifact behaves like a quick first human pass rather than a perfect answer-key migration.

## Provenance Status

This is not a fresh Kaggle rerun. I re-authored the baseline from the stale `origin/allstate-claims` notes and the current candidate bank, and I kept the wording first-person here so reviewers can tell it is a human baseline judgment rather than benchmark ground truth.
