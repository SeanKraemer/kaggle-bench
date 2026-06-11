# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: "1.3"
#       jupytext_version: "1.16.0"
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # AMEX Default Prediction Human Baseline Work
#
# Consulted scratch script paired with `work.ipynb`.
# This artifact supports a conservative manual AMEX TC1 baseline.
# It is evidence for the reasoning pass, not the final selection record.

# %%
import numpy as np
import pandas as pd

CAT_COLS = [
    "B_30",
    "B_38",
    "D_114",
    "D_116",
    "D_117",
    "D_120",
    "D_126",
    "D_63",
    "D_64",
    "D_66",
    "D_68",
]
NON_PREDICTOR_COLS = ["customer_ID", "S_2", "target"]

# Assumes the Kaggle AMEX training table has already been loaded into `train`.

# %% [markdown]
# ## Raw Schema Audit
#
# First pass:
# - separate known categorical statement columns from the wide numeric block
# - flag obvious identifiers / non-predictors
# - preview the standard AMEX numeric rounding trick without turning this notebook into a mapping guide

# %%
known_cat_set = set(CAT_COLS)
non_predictor_set = set(NON_PREDICTOR_COLS)
numeric_cols = [col for col in train.columns if col not in known_cat_set | non_predictor_set]

schema_audit = pd.DataFrame({"column": train.columns})
schema_audit["role"] = np.select(
    [
        schema_audit["column"].isin(CAT_COLS),
        schema_audit["column"].isin(NON_PREDICTOR_COLS),
    ],
    [
        "categorical",
        "descriptive_or_target",
    ],
    default="numeric",
)
schema_audit["dtype"] = schema_audit["column"].map(train.dtypes.astype(str).to_dict())
schema_audit["null_ratio"] = schema_audit["column"].map(train.isna().mean().to_dict())

rounded_numeric_preview = train[numeric_cols].round(2).head()
categorical_block = train[CAT_COLS].astype("Int64").head()

schema_audit.sort_values(["role", "null_ratio"], ascending=[True, False]).head(20)

# %% [markdown]
# ## Categorical Handling
#
# Inspect the small AMEX categorical block, check whether rare levels are severe,
# and keep the final baseline at simple label-ready encoding.

# %%
def collapse_rare_levels(series: pd.Series, min_share: float = 0.01) -> pd.Series:
    shares = series.value_counts(dropna=False, normalize=True)
    return series.where(series.map(shares) >= min_share, other=-1)


cat_level_profile = {
    col: train[col].value_counts(dropna=False, normalize=True).head(8).rename("share")
    for col in CAT_COLS
}
collapsed_cat_preview = train[CAT_COLS].apply(collapse_rare_levels)
label_ready_cats = collapsed_cat_preview.apply(lambda col: pd.factorize(col.fillna(-1), sort=True)[0]).astype("int16")

cat_level_profile["B_30"]

# %% [markdown]
# ## Missingness And Ordered Deltas
#
# Missingness is one of the clearest AMEX signals.
# Check the null-rate profile, create binary missing flags,
# and keep median imputation as the simple fallback for better-covered numeric columns.

# %%
median_ready_cols = [col for col in numeric_cols if train[col].notna().mean() >= 0.5]
distribution_cols = [col for col in ["P_2", "D_39", "B_9"] if col in train.columns]

missing_profile = train[numeric_cols].isna().mean().sort_values(ascending=False).to_frame("null_ratio")
distribution_probe = train[distribution_cols].describe(percentiles=[0.05, 0.5, 0.95]).T
missing_flags = train[median_ready_cols].isna().astype("int8").add_suffix("_is_missing")
median_imputed_preview = train[median_ready_cols].fillna(train[median_ready_cols].median(numeric_only=True))

ordered = train.sort_values(["customer_ID", "S_2"]).copy()
lag1_deltas = ordered.groupby("customer_ID")[numeric_cols].diff().add_suffix("_lag1_diff")

missing_profile.head(15)

# %% [markdown]
# ## Customer-Level Aggregations
#
# Collapse the monthly statement table to one row per customer.
# Keep the standard AMEX numeric and categorical aggregation families,
# but stop short of treating every extra branch as baseline-mandatory.

# %%
numeric_agg = ordered.groupby("customer_ID")[numeric_cols].agg(["first", "mean", "std", "min", "max", "last"])
categorical_agg = ordered.groupby("customer_ID")[CAT_COLS].agg(["count", "first", "last", "nunique"])

numeric_agg.head(2)

# %%
customer_features = pd.concat([numeric_agg, categorical_agg], axis=1)
customer_features.columns = [
    "_".join(str(part) for part in col_tuple if part)
    for col_tuple in customer_features.columns.to_flat_index()
]

simple_gap_cols = [
    col
    for col in ["P_2", "D_39", "B_9"]
    if f"{col}_last" in customer_features.columns and f"{col}_mean" in customer_features.columns
]
for col in simple_gap_cols:
    customer_features[f"{col}_last_mean_gap_preview"] = (
        customer_features[f"{col}_last"] - customer_features[f"{col}_mean"]
    )

customer_features.filter(regex="^(P_2|D_39|B_9)").head()

# %% [markdown]
# ## Final Matrix Prep
#
# Build the customer-level matrix, then drop only the columns that are clearly unusable as direct predictors.
# In this conservative pass that means removing the customer key and raw statement date after feature construction.

# %%
final_frame = customer_features.reset_index()
drop_after_feature_build = [col for col in ["customer_ID", "S_2"] if col in final_frame.columns]
model_frame = final_frame.drop(columns=drop_after_feature_build)

model_frame.shape
