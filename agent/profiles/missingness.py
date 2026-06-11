from __future__ import annotations

from agent.profiles._helpers import is_missing


def profile_missingness(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {"row_count": 0, "columns": {}}

    columns = sorted({column for row in rows for column in row})
    result = {}
    row_count = len(rows)
    for column in columns:
        missing_count = sum(1 for row in rows if is_missing(row.get(column)))
        result[column] = {
            "missing_count": missing_count,
            "missing_rate": missing_count / row_count,
        }
    return {
        "row_count": row_count,
        "columns": result,
    }
