from __future__ import annotations

from agent.rule_based.decision_records import build_decision_record
from agent.rule_based.predicates import (
    HIGH_NULL_DROP_THRESHOLD,
    JOIN_COVERAGE_THRESHOLD,
    LOW_CARDINALITY_THRESHOLD,
    MEDIUM_CARDINALITY_THRESHOLD,
    MISSING_INDICATOR_MIN_RATE,
    NUMERIC_MISSINGNESS_THRESHOLD,
    OUTLIER_IQR_FACTOR,
    distinct_count,
    get_missing_rate,
    is_boolean_like,
    is_datetime_like,
    is_identifier_like,
    is_medium_cardinality,
    is_narrow_target_range,
    is_nonnegative_sparse_numeric,
    is_numeric_like,
    is_low_cardinality,
    should_add_categorical_encoding,
    should_add_clip_outliers,
    should_add_constant_imputation,
    should_add_date_feature,
    should_add_drop_columns,
    should_add_drop_high_null_columns,
    should_add_join,
    should_add_median_imputation,
    should_add_missing_indicator,
    should_add_parse_datetime,
    should_remove_bad_categorical_encoding,
    should_remove_bad_clip_outliers,
    should_remove_bad_date_feature,
    should_remove_bad_drop_columns,
    should_remove_bad_drop_high_null_columns,
    should_remove_bad_filter,
    should_remove_bad_imputation,
    should_remove_bad_join,
    should_remove_bad_missing_indicator,
    should_remove_bad_parse_datetime,
)


def evaluate_add_action(dataset_insights: dict, action: dict) -> dict:
    action_type = action.get("action_type")
    params = action.get("canonical_params", {})

    if action_type == "JOIN_LOOKUP":
        matched = should_add_join(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="add",
            decision="selected_add" if matched else "skipped",
            triggered_rule="should_add_join" if matched else None,
            details=[
                f"how={params.get('how')}",
                f"left_key_coverage_rate={dataset_insights.get('join_profile', {}).get('left_key_coverage_rate', 0.0)}",
                f"threshold={JOIN_COVERAGE_THRESHOLD}",
            ],
        )

    if action_type == "PARSE_DATETIME":
        columns = params.get("columns", [])
        matched = should_add_parse_datetime(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="add",
            decision="selected_add" if matched else "skipped",
            triggered_rule="should_add_parse_datetime" if matched else None,
            details=[
                f"columns={columns}",
                f"datetime_like_columns={[column for column in columns if is_datetime_like(dataset_insights, column)]}",
            ],
        )

    if action_type == "IMPUTE_MISSING":
        strategy = params.get("strategy")
        columns = params.get("columns", [])
        missing_rates = {column: get_missing_rate(dataset_insights, column) for column in columns}
        if strategy == "median":
            matched = should_add_median_imputation(dataset_insights, action)
            return build_decision_record(
                action=action,
                candidate_side="add",
                decision="selected_add" if matched else "skipped",
                triggered_rule="should_add_median_imputation" if matched else None,
                details=[
                    f"strategy={strategy}",
                    f"missing_rates={missing_rates}",
                    f"threshold={NUMERIC_MISSINGNESS_THRESHOLD}",
                ],
            )
        if strategy == "constant":
            matched = should_add_constant_imputation(dataset_insights, action)
            return build_decision_record(
                action=action,
                candidate_side="add",
                decision="selected_add" if matched else "skipped",
                triggered_rule="should_add_constant_imputation" if matched else None,
                details=[
                    f"strategy={strategy}",
                    f"fill_value={params.get('fill_value')}",
                    f"missing_rates={missing_rates}",
                ],
            )
        return build_decision_record(
            action=action,
            candidate_side="add",
            decision="skipped",
            triggered_rule=None,
            details=[f"unsupported_imputation_strategy={strategy}"],
        )

    if action_type == "CREATE_MISSING_INDICATOR":
        columns = params.get("columns", [])
        matched = should_add_missing_indicator(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="add",
            decision="selected_add" if matched else "skipped",
            triggered_rule="should_add_missing_indicator" if matched else None,
            details=[
                f"columns={columns}",
                f"missing_rates={{ {', '.join(f'{column}: {get_missing_rate(dataset_insights, column)}' for column in columns)} }}",
                f"min_rate={MISSING_INDICATOR_MIN_RATE}",
                f"max_rate={HIGH_NULL_DROP_THRESHOLD}",
            ],
        )

    if action_type == "DROP_HIGH_NULL_COLUMNS":
        columns = params.get("columns", [])
        threshold = params.get("null_ratio_threshold", HIGH_NULL_DROP_THRESHOLD)
        matched = should_add_drop_high_null_columns(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="add",
            decision="selected_add" if matched else "skipped",
            triggered_rule="should_add_drop_high_null_columns" if matched else None,
            details=[
                f"columns={columns}",
                f"missing_rates={{ {', '.join(f'{column}: {get_missing_rate(dataset_insights, column)}' for column in columns)} }}",
                f"threshold={threshold}",
            ],
        )

    if action_type in {"DATE_PART_FEATURE", "CYCLICAL_ENCODE", "TIME_SINCE_REFERENCE"}:
        candidate_columns = (
            params.get("date_columns")
            or params.get("columns")
            or params.get("reference_date_columns")
            or []
        )
        matched = should_add_date_feature(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="add",
            decision="selected_add" if matched else "skipped",
            triggered_rule="should_add_date_feature" if matched else None,
            details=[
                f"candidate_columns={candidate_columns}",
                f"datetime_like_columns={[column for column in candidate_columns if is_datetime_like(dataset_insights, column)]}",
            ],
        )

    if action_type == "ENCODE_CATEGORICAL":
        columns = params.get("columns", [])
        matched = should_add_categorical_encoding(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="add",
            decision="selected_add" if matched else "skipped",
            triggered_rule="should_add_categorical_encoding" if matched else None,
            details=[
                f"method={params.get('method')}",
                f"distinct_counts={{ {', '.join(f'{column}: {distinct_count(dataset_insights, column)}' for column in columns)} }}",
                f"low_cardinality_threshold={LOW_CARDINALITY_THRESHOLD}",
                f"medium_cardinality_threshold={MEDIUM_CARDINALITY_THRESHOLD}",
            ],
        )

    if action_type == "CLIP_OUTLIERS":
        columns = params.get("columns", [])
        matched = should_add_clip_outliers(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="add",
            decision="selected_add" if matched else "skipped",
            triggered_rule="should_add_clip_outliers" if matched else None,
            details=[
                f"columns={columns}",
                f"outlier_iqr_factor={OUTLIER_IQR_FACTOR}",
            ],
        )

    if action_type == "DROP_COLUMNS":
        columns = params.get("columns", [])
        matched = should_add_drop_columns(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="add",
            decision="selected_add" if matched else "skipped",
            triggered_rule="should_add_drop_columns" if matched else None,
            details=[
                f"columns={columns}",
                f"identifier_like_columns={[column for column in columns if is_identifier_like(dataset_insights, column)]}",
                f"datetime_like_columns={[column for column in columns if is_datetime_like(dataset_insights, column)]}",
                f"primary_key={dataset_insights.get('primary_key')}",
                f"target_column={dataset_insights.get('target_column')}",
            ],
        )

    return build_decision_record(
        action=action,
        candidate_side="add",
        decision="skipped",
        triggered_rule=None,
        details=[f"no_generic_add_heuristic_for_action_type={action_type}"],
    )


def evaluate_remove_action(dataset_insights: dict, action: dict) -> dict:
    action_type = action.get("action_type")
    params = action.get("canonical_params", {})

    if action_type == "JOIN_LOOKUP":
        matched = should_remove_bad_join(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="remove",
            decision="selected_remove" if matched else "skipped",
            triggered_rule="should_remove_bad_join" if matched else None,
            details=[
                f"how={params.get('how')}",
                f"left_key_coverage_rate={dataset_insights.get('join_profile', {}).get('left_key_coverage_rate', 0.0)}",
                f"threshold={JOIN_COVERAGE_THRESHOLD}",
            ],
        )

    if action_type == "PARSE_DATETIME":
        columns = params.get("columns", [])
        matched = should_remove_bad_parse_datetime(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="remove",
            decision="selected_remove" if matched else "skipped",
            triggered_rule="should_remove_bad_parse_datetime" if matched else None,
            details=[
                f"columns={columns}",
                f"datetime_like_columns={[column for column in columns if is_datetime_like(dataset_insights, column)]}",
            ],
        )

    if action_type in {"DATE_PART_FEATURE", "CYCLICAL_ENCODE", "TIME_SINCE_REFERENCE"}:
        candidate_columns = (
            params.get("date_columns")
            or params.get("columns")
            or params.get("reference_date_columns")
            or []
        )
        matched = should_remove_bad_date_feature(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="remove",
            decision="selected_remove" if matched else "skipped",
            triggered_rule="should_remove_bad_date_feature" if matched else None,
            details=[
                f"candidate_columns={candidate_columns}",
                f"datetime_like_columns={[column for column in candidate_columns if is_datetime_like(dataset_insights, column)]}",
            ],
        )

    if action_type == "IMPUTE_MISSING":
        strategy = params.get("strategy")
        columns = params.get("columns", [])
        missing_rates = {column: get_missing_rate(dataset_insights, column) for column in columns}
        matched = should_remove_bad_imputation(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="remove",
            decision="selected_remove" if matched else "skipped",
            triggered_rule="should_remove_bad_imputation" if matched else None,
            details=[
                f"strategy={strategy}",
                f"fill_value={params.get('fill_value')}",
                f"columns={columns}",
                f"missing_rates={missing_rates}",
                f"boolean_like_columns={[column for column in columns if is_boolean_like(dataset_insights, column)]}",
                f"numeric_like_columns={[column for column in columns if is_numeric_like(dataset_insights, column)]}",
            ],
        )

    if action_type == "CREATE_MISSING_INDICATOR":
        columns = params.get("columns", [])
        matched = should_remove_bad_missing_indicator(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="remove",
            decision="selected_remove" if matched else "skipped",
            triggered_rule="should_remove_bad_missing_indicator" if matched else None,
            details=[
                f"columns={columns}",
                f"missing_rates={{ {', '.join(f'{column}: {get_missing_rate(dataset_insights, column)}' for column in columns)} }}",
                f"min_rate={MISSING_INDICATOR_MIN_RATE}",
                f"max_rate={HIGH_NULL_DROP_THRESHOLD}",
            ],
        )

    if action_type == "DROP_HIGH_NULL_COLUMNS":
        columns = params.get("columns", [])
        threshold = params.get("null_ratio_threshold", HIGH_NULL_DROP_THRESHOLD)
        matched = should_remove_bad_drop_high_null_columns(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="remove",
            decision="selected_remove" if matched else "skipped",
            triggered_rule="should_remove_bad_drop_high_null_columns" if matched else None,
            details=[
                f"columns={columns}",
                f"missing_rates={{ {', '.join(f'{column}: {get_missing_rate(dataset_insights, column)}' for column in columns)} }}",
                f"threshold={threshold}",
            ],
        )

    if action_type == "ENCODE_CATEGORICAL":
        columns = params.get("columns", [])
        matched = should_remove_bad_categorical_encoding(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="remove",
            decision="selected_remove" if matched else "skipped",
            triggered_rule="should_remove_bad_categorical_encoding" if matched else None,
            details=[
                f"method={params.get('method')}",
                f"columns={columns}",
                f"distinct_counts={{ {', '.join(f'{column}: {distinct_count(dataset_insights, column)}' for column in columns)} }}",
                f"identifier_like_columns={[column for column in columns if is_identifier_like(dataset_insights, column)]}",
                f"datetime_like_columns={[column for column in columns if is_datetime_like(dataset_insights, column)]}",
            ],
        )

    if action_type == "CLIP_OUTLIERS":
        columns = params.get("columns", [])
        matched = should_remove_bad_clip_outliers(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="remove",
            decision="selected_remove" if matched else "skipped",
            triggered_rule="should_remove_bad_clip_outliers" if matched else None,
            details=[
                f"columns={columns}",
                f"numeric_like_columns={[column for column in columns if is_numeric_like(dataset_insights, column)]}",
                f"outlier_iqr_factor={OUTLIER_IQR_FACTOR}",
            ],
        )

    if action_type == "DROP_COLUMNS":
        columns = params.get("columns", [])
        matched = should_remove_bad_drop_columns(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="remove",
            decision="selected_remove" if matched else "skipped",
            triggered_rule="should_remove_bad_drop" if matched else None,
            details=[
                f"columns={columns}",
                f"identifier_like_columns={[column for column in columns if is_identifier_like(dataset_insights, column)]}",
                f"datetime_like_columns={[column for column in columns if is_datetime_like(dataset_insights, column)]}",
                f"primary_key={dataset_insights.get('primary_key')}",
                f"target_column={dataset_insights.get('target_column')}",
            ],
        )

    if action_type == "FILTER_ROWS":
        matched = should_remove_bad_filter(dataset_insights, action)
        return build_decision_record(
            action=action,
            candidate_side="remove",
            decision="selected_remove" if matched else "skipped",
            triggered_rule="should_remove_narrow_filter" if matched else None,
            details=[
                f"predicate={params.get('predicate')}",
                f"numeric_profile_columns={list(dataset_insights.get('numeric_profile', {}).get('columns', {}).keys())}",
            ],
        )

    return build_decision_record(
        action=action,
        candidate_side="remove",
        decision="skipped",
        triggered_rule=None,
        details=[f"no_generic_remove_heuristic_for_action_type={action_type}"],
    )
