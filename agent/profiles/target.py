from __future__ import annotations

from agent.profiles._helpers import non_missing_values, quantile, try_parse_float


def profile_target_distribution(rows: list[dict[str, str]], target_column: str) -> dict:
    values = [try_parse_float(value) for value in non_missing_values(rows, target_column)]
    numeric_values = sorted(value for value in values if value is not None)
    if not numeric_values:
        return {
            "count": 0,
            "min": None,
            "max": None,
            "p25": None,
            "p50": None,
            "p75": None,
        }
    return {
        "count": len(numeric_values),
        "min": numeric_values[0],
        "max": numeric_values[-1],
        "p25": quantile(numeric_values, 0.25),
        "p50": quantile(numeric_values, 0.5),
        "p75": quantile(numeric_values, 0.75),
    }
