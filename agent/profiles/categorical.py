from __future__ import annotations

from agent.profiles._helpers import non_missing_values, top_values, try_parse_datetime, try_parse_float


def profile_categorical_columns(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {"columns": {}}

    columns = sorted({column for row in rows for column in row})
    profile = {}
    for column in columns:
        values = non_missing_values(rows, column)
        if not values:
            continue
        if all(try_parse_float(value) is not None for value in values):
            continue
        if all(try_parse_datetime(value) is not None for value in values):
            continue
        distinct_values = sorted(set(values))
        profile[column] = {
            "count": len(values),
            "distinct_count": len(distinct_values),
            "distinct_ratio": len(distinct_values) / len(values),
            "top_values": top_values(values),
        }
    return {"columns": profile}
