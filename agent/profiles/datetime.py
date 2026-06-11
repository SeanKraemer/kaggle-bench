from __future__ import annotations

from agent.profiles._helpers import non_missing_values, try_parse_datetime


def profile_datetime_columns(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {"columns": {}}

    columns = sorted({column for row in rows for column in row})
    profile = {}
    for column in columns:
        values = non_missing_values(rows, column)
        if not values:
            continue
        parsed = [try_parse_datetime(value) for value in values]
        parseable = [value for value in parsed if value is not None]
        if not parseable:
            continue
        if len(parseable) != len(values):
            continue
        ordered = sorted(parseable)
        profile[column] = {
            "count": len(values),
            "parseable_count": len(parseable),
            "parse_rate": len(parseable) / len(values),
            "min": ordered[0].isoformat(),
            "max": ordered[-1].isoformat(),
        }
    return {"columns": profile}
