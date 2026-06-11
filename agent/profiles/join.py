from __future__ import annotations


def _normalize_join_columns(columns: str | list[str] | None) -> list[str]:
    if isinstance(columns, str):
        return [columns] if columns else []
    if isinstance(columns, list):
        return [column for column in columns if isinstance(column, str) and column]
    return []


def _extract_join_keys(rows: list[dict[str, str]], columns: list[str]) -> list[str | tuple[str, ...]]:
    keys: list[str | tuple[str, ...]] = []
    for row in rows:
        values = tuple(row.get(column, "") for column in columns)
        if not columns or any(value == "" for value in values):
            continue
        keys.append(values[0] if len(values) == 1 else values)
    return keys


def profile_join_key(
    left_rows: list[dict[str, str]],
    right_rows: list[dict[str, str]],
    key: str | list[str] | None = None,
    *,
    left_key: str | list[str] | None = None,
    right_key: str | list[str] | None = None,
) -> dict:
    left_columns = _normalize_join_columns(left_key if left_key is not None else key)
    right_columns = _normalize_join_columns(right_key if right_key is not None else key)
    if not left_columns or not right_columns:
        raise ValueError("Join profiling requires non-empty join columns.")

    left_keys = _extract_join_keys(left_rows, left_columns)
    right_keys = _extract_join_keys(right_rows, right_columns)
    left_distinct = set(left_keys)
    right_distinct = set(right_keys)
    overlap = left_distinct & right_distinct
    return {
        "left_key_columns": left_columns,
        "right_key_columns": right_columns,
        "left_row_count": len(left_rows),
        "right_row_count": len(right_rows),
        "left_distinct_key_count": len(left_distinct),
        "right_distinct_key_count": len(right_distinct),
        "overlap_key_count": len(overlap),
        "left_key_coverage_rate": 0.0 if not left_distinct else len(overlap) / len(left_distinct),
        "right_key_coverage_rate": 0.0 if not right_distinct else len(overlap) / len(right_distinct),
    }
