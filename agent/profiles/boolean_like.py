from __future__ import annotations

from agent.profiles._helpers import non_missing_values

BOOLEAN_VALUE_SETS = [
    {"true", "false"},
    {"0", "1"},
    {"yes", "no"},
    {"y", "n"},
]


def profile_boolean_like_columns(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {"columns": {}}

    columns = sorted({column for row in rows for column in row})
    profile = {}
    for column in columns:
        values = non_missing_values(rows, column)
        if not values:
            continue
        normalized = {value.strip().lower() for value in values}
        if any(normalized <= allowed for allowed in BOOLEAN_VALUE_SETS):
            profile[column] = {
                "count": len(values),
                "distinct_values": sorted(set(values)),
            }
    return {"columns": profile}
