from __future__ import annotations

from math import sqrt

from agent.profiles._helpers import non_missing_values, quantile, try_parse_float


def profile_numeric_columns(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {"columns": {}}

    columns = sorted({column for row in rows for column in row})
    profile = {}
    for column in columns:
        values = [try_parse_float(value) for value in non_missing_values(rows, column)]
        if not values or any(value is None for value in values):
            continue
        numeric_values = sorted(value for value in values if value is not None)
        mean = sum(numeric_values) / len(numeric_values)
        variance = sum((value - mean) ** 2 for value in numeric_values) / len(numeric_values)
        profile[column] = {
            "count": len(numeric_values),
            "distinct_count": len(set(numeric_values)),
            "min": numeric_values[0],
            "max": numeric_values[-1],
            "mean": mean,
            "std": sqrt(variance),
            "p25": quantile(numeric_values, 0.25),
            "p50": quantile(numeric_values, 0.5),
            "p75": quantile(numeric_values, 0.75),
        }
    return {"columns": profile}
