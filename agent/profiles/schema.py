from __future__ import annotations

from agent.profiles._helpers import non_missing_values, try_parse_datetime, try_parse_float, try_parse_int


def infer_column_type(values: list[str]) -> str:
    if not values:
        return "empty"
    if all(try_parse_int(value) is not None for value in values):
        return "integer_like"
    if all(try_parse_float(value) is not None for value in values):
        return "numeric_like"
    if all(try_parse_datetime(value) is not None for value in values):
        return "datetime_like"
    return "string"


def profile_table_schema(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {"row_count": 0, "column_count": 0, "columns": {}}

    columns = sorted({column for row in rows for column in row})
    profile = {}
    for column in columns:
        values = non_missing_values(rows, column)
        distinct_values = set(values)
        profile[column] = {
            "non_missing_count": len(values),
            "distinct_count": len(distinct_values),
            "distinct_ratio": 0.0 if not rows else len(distinct_values) / len(rows),
            "inferred_type": infer_column_type(values),
        }
    return {
        "row_count": len(rows),
        "column_count": len(columns),
        "columns": profile,
    }
