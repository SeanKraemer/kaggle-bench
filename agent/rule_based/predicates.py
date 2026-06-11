from __future__ import annotations

import re

from agent.rule_based.thresholds import (
    HIGH_NULL_DROP_THRESHOLD,
    JOIN_COVERAGE_THRESHOLD,
    LOW_CARDINALITY_THRESHOLD,
    MEDIUM_CARDINALITY_THRESHOLD,
    MISSING_INDICATOR_MIN_RATE,
    NUMERIC_MISSINGNESS_THRESHOLD,
    OUTLIER_IQR_FACTOR,
)


NUMERIC_LITERAL_PATTERN = re.compile(r"-?\d+(?:\.\d+)?")
IDENTIFIER_RATIO_THRESHOLD = 0.95


def get_schema_column(dataset_insights: dict, column: str) -> dict:
    return dataset_insights.get("schema_profile", {}).get("columns", {}).get(column, {})


def get_missing_rate(dataset_insights: dict, column: str) -> float:
    return dataset_insights.get("missingness_profile", {}).get("columns", {}).get(column, {}).get("missing_rate", 0.0)


def is_datetime_like(dataset_insights: dict, column: str) -> bool:
    return get_schema_column(dataset_insights, column).get("inferred_type") == "datetime_like"


def is_numeric_like(dataset_insights: dict, column: str) -> bool:
    return get_schema_column(dataset_insights, column).get("inferred_type") in {"integer_like", "numeric_like"}


def distinct_count(dataset_insights: dict, column: str) -> int:
    return get_schema_column(dataset_insights, column).get("distinct_count", 0)


def distinct_ratio(dataset_insights: dict, column: str) -> float:
    return get_schema_column(dataset_insights, column).get("distinct_ratio", 0.0)


def is_identifier_like(dataset_insights: dict, column: str) -> bool:
    return distinct_ratio(dataset_insights, column) >= IDENTIFIER_RATIO_THRESHOLD


def is_boolean_like(dataset_insights: dict, column: str) -> bool:
    return column in dataset_insights.get("boolean_like_profile", {}).get("columns", {})


def is_low_cardinality(dataset_insights: dict, column: str) -> bool:
    count = distinct_count(dataset_insights, column)
    return 1 < count <= LOW_CARDINALITY_THRESHOLD


def is_medium_cardinality(dataset_insights: dict, column: str) -> bool:
    count = distinct_count(dataset_insights, column)
    return LOW_CARDINALITY_THRESHOLD < count <= MEDIUM_CARDINALITY_THRESHOLD


def is_nonnegative_sparse_numeric(dataset_insights: dict, column: str) -> bool:
    numeric = dataset_insights.get("numeric_profile", {}).get("columns", {}).get(column)
    if numeric is None:
        return False
    return numeric.get("min", 0.0) >= 0 and distinct_count(dataset_insights, column) <= LOW_CARDINALITY_THRESHOLD


def is_narrow_target_range(dataset_insights: dict, predicate: str) -> bool:
    referenced_columns = [
        column
        for column in dataset_insights.get("numeric_profile", {}).get("columns", {})
        if column in predicate
    ]
    if not referenced_columns:
        return False
    values = [float(value) for value in NUMERIC_LITERAL_PATTERN.findall(predicate)]
    if len(values) < 2:
        return False
    lower, upper = min(values), max(values)
    range_width = upper - lower
    for column in referenced_columns:
        numeric_profile = dataset_insights.get("numeric_profile", {}).get("columns", {}).get(column)
        if numeric_profile is None:
            continue
        p25 = numeric_profile.get("p25")
        p75 = numeric_profile.get("p75")
        if p25 is None or p75 is None:
            continue
        iqr = p75 - p25
        if iqr > 0 and range_width < 0.5 * iqr:
            return True
    return False


def should_add_join(dataset_insights: dict, action: dict) -> bool:
    params = action.get("canonical_params", {})
    return (
        action.get("action_type") == "JOIN_LOOKUP"
        and params.get("how") in {"left", "inner"}
        and dataset_insights.get("join_profile", {}).get("left_key_coverage_rate", 0.0) >= JOIN_COVERAGE_THRESHOLD
    )


def should_add_parse_datetime(dataset_insights: dict, action: dict) -> bool:
    columns = action.get("canonical_params", {}).get("columns", [])
    return (
        action.get("action_type") == "PARSE_DATETIME"
        and any(is_datetime_like(dataset_insights, column) for column in columns)
    )


def should_add_median_imputation(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "IMPUTE_MISSING":
        return False
    params = action.get("canonical_params", {})
    if params.get("strategy") != "median":
        return False
    missingness_profile = dataset_insights.get("missingness_profile", {}).get("columns", {})
    return any(
        missingness_profile.get(column, {}).get("missing_rate", 0.0) >= NUMERIC_MISSINGNESS_THRESHOLD
        for column in params.get("columns", [])
    )


def should_add_constant_imputation(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "IMPUTE_MISSING":
        return False
    params = action.get("canonical_params", {})
    if params.get("strategy") != "constant":
        return False
    columns = params.get("columns", [])
    fill_value = params.get("fill_value")
    if fill_value in {"FALSE", "False", "false", False}:
        return all(is_boolean_like(dataset_insights, column) for column in columns)
    if fill_value == 0:
        return all(
            is_nonnegative_sparse_numeric(dataset_insights, column)
            and get_missing_rate(dataset_insights, column) >= NUMERIC_MISSINGNESS_THRESHOLD
            for column in columns
        )
    return False


def should_add_missing_indicator(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "CREATE_MISSING_INDICATOR":
        return False
    columns = action.get("canonical_params", {}).get("columns", [])
    return any(
        MISSING_INDICATOR_MIN_RATE <= get_missing_rate(dataset_insights, column) < HIGH_NULL_DROP_THRESHOLD
        for column in columns
    )


def should_add_drop_high_null_columns(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "DROP_HIGH_NULL_COLUMNS":
        return False
    params = action.get("canonical_params", {})
    threshold = params.get("null_ratio_threshold", HIGH_NULL_DROP_THRESHOLD)
    columns = params.get("columns", [])
    return bool(columns) and all(get_missing_rate(dataset_insights, column) >= threshold for column in columns)


def should_add_date_feature(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") not in {"DATE_PART_FEATURE", "CYCLICAL_ENCODE", "TIME_SINCE_REFERENCE"}:
        return False
    params = action.get("canonical_params", {})
    candidate_columns = (
        params.get("date_columns")
        or params.get("columns")
        or params.get("reference_date_columns")
        or []
    )
    return bool(candidate_columns) and all(is_datetime_like(dataset_insights, column) for column in candidate_columns)


def should_add_categorical_encoding(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "ENCODE_CATEGORICAL":
        return False
    params = action.get("canonical_params", {})
    columns = params.get("columns", [])
    method = params.get("method")
    if not columns:
        return False
    if method == "onehot":
        return all(is_low_cardinality(dataset_insights, column) for column in columns)
    if method == "label":
        return all(is_medium_cardinality(dataset_insights, column) or is_low_cardinality(dataset_insights, column) for column in columns)
    if method == "count":
        return all(distinct_count(dataset_insights, column) > LOW_CARDINALITY_THRESHOLD for column in columns)
    return False


def should_add_clip_outliers(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "CLIP_OUTLIERS":
        return False
    columns = action.get("canonical_params", {}).get("columns", [])
    if not columns:
        return False
    for column in columns:
        numeric_profile = dataset_insights.get("numeric_profile", {}).get("columns", {}).get(column)
        if numeric_profile is None:
            continue
        p25 = numeric_profile.get("p25")
        p75 = numeric_profile.get("p75")
        min_value = numeric_profile.get("min")
        max_value = numeric_profile.get("max")
        if None in {p25, p75, min_value, max_value}:
            continue
        iqr = p75 - p25
        if iqr > 0 and ((max_value - p75) > OUTLIER_IQR_FACTOR * iqr or (p25 - min_value) > OUTLIER_IQR_FACTOR * iqr):
            return True
    return False


def should_add_drop_columns(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "DROP_COLUMNS":
        return False
    columns = action.get("canonical_params", {}).get("columns", [])
    target_column = dataset_insights.get("target_column")
    primary_key = dataset_insights.get("primary_key")
    return any(
        column in {target_column, primary_key}
        or is_identifier_like(dataset_insights, column)
        or is_datetime_like(dataset_insights, column)
        for column in columns
    )


def should_remove_bad_join(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "JOIN_LOOKUP":
        return False
    params = action.get("canonical_params", {})
    join_how = params.get("how")
    coverage = dataset_insights.get("join_profile", {}).get("left_key_coverage_rate", 0.0)
    return join_how not in {"left", "inner"} or (join_how == "inner" and coverage < JOIN_COVERAGE_THRESHOLD)


def should_remove_bad_parse_datetime(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "PARSE_DATETIME":
        return False
    columns = action.get("canonical_params", {}).get("columns", [])
    return not columns or not all(is_datetime_like(dataset_insights, column) for column in columns)


def should_remove_bad_imputation(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "IMPUTE_MISSING":
        return False
    params = action.get("canonical_params", {})
    strategy = params.get("strategy")
    columns = params.get("columns", [])
    if not columns:
        return True
    if strategy == "median":
        return not all(
            is_numeric_like(dataset_insights, column)
            and not is_identifier_like(dataset_insights, column)
            and not is_datetime_like(dataset_insights, column)
            for column in columns
        )
    if strategy == "constant":
        fill_value = params.get("fill_value")
        if fill_value in {"FALSE", "False", "false", False}:
            return not all(is_boolean_like(dataset_insights, column) for column in columns)
        if fill_value == 0:
            return not all(
                is_nonnegative_sparse_numeric(dataset_insights, column)
                and get_missing_rate(dataset_insights, column) >= NUMERIC_MISSINGNESS_THRESHOLD
                for column in columns
            )
    return False


def should_remove_bad_missing_indicator(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "CREATE_MISSING_INDICATOR":
        return False
    columns = action.get("canonical_params", {}).get("columns", [])
    if not columns:
        return True
    return any(
        get_missing_rate(dataset_insights, column) < MISSING_INDICATOR_MIN_RATE
        or get_missing_rate(dataset_insights, column) >= HIGH_NULL_DROP_THRESHOLD
        for column in columns
    )


def should_remove_bad_drop_high_null_columns(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "DROP_HIGH_NULL_COLUMNS":
        return False
    params = action.get("canonical_params", {})
    columns = params.get("columns", [])
    threshold = params.get("null_ratio_threshold", HIGH_NULL_DROP_THRESHOLD)
    return not columns or any(get_missing_rate(dataset_insights, column) < threshold for column in columns)


def should_remove_bad_date_feature(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") not in {"DATE_PART_FEATURE", "CYCLICAL_ENCODE", "TIME_SINCE_REFERENCE"}:
        return False
    params = action.get("canonical_params", {})
    candidate_columns = (
        params.get("date_columns")
        or params.get("columns")
        or params.get("reference_date_columns")
        or []
    )
    return not candidate_columns or not all(is_datetime_like(dataset_insights, column) for column in candidate_columns)


def should_remove_bad_categorical_encoding(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "ENCODE_CATEGORICAL":
        return False
    params = action.get("canonical_params", {})
    columns = params.get("columns", [])
    method = params.get("method")
    if not columns:
        return True
    if any(is_identifier_like(dataset_insights, column) or is_datetime_like(dataset_insights, column) for column in columns):
        return True
    if method == "onehot":
        return not all(is_low_cardinality(dataset_insights, column) for column in columns)
    if method == "label":
        return not all(is_medium_cardinality(dataset_insights, column) or is_low_cardinality(dataset_insights, column) for column in columns)
    if method == "count":
        return not all(distinct_count(dataset_insights, column) > LOW_CARDINALITY_THRESHOLD for column in columns)
    return False


def should_remove_bad_clip_outliers(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "CLIP_OUTLIERS":
        return False
    columns = action.get("canonical_params", {}).get("columns", [])
    if not columns:
        return True
    if any(not is_numeric_like(dataset_insights, column) for column in columns):
        return True
    return not should_add_clip_outliers(dataset_insights, action)


def should_remove_bad_drop_columns(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "DROP_COLUMNS":
        return False
    params = action.get("canonical_params", {})
    target_column = dataset_insights.get("target_column")
    primary_key = dataset_insights.get("primary_key")
    return any(
        column in {target_column, primary_key}
        or is_identifier_like(dataset_insights, column)
        or is_datetime_like(dataset_insights, column)
        for column in params.get("columns", [])
    )


def should_remove_bad_filter(dataset_insights: dict, action: dict) -> bool:
    if action.get("action_type") != "FILTER_ROWS":
        return False
    predicate = action.get("canonical_params", {}).get("predicate", "")
    return is_narrow_target_range(dataset_insights, predicate)
