from __future__ import annotations

from collections import Counter
from datetime import datetime
from typing import Iterable

MISSING_VALUES = {"", "na", "n/a", "nan", "null", "none", "unknown"}


def is_missing(value: str | None) -> bool:
    if value is None:
        return True
    return value.strip().lower() in MISSING_VALUES


def non_missing_values(rows: list[dict[str, str]], column: str) -> list[str]:
    return [row[column] for row in rows if column in row and not is_missing(row[column])]


def try_parse_int(value: str) -> int | None:
    try:
        if "." in value:
            return None
        return int(value)
    except ValueError:
        return None


def try_parse_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None


def try_parse_datetime(value: str) -> datetime | None:
    candidate = value.strip()
    if not candidate:
        return None
    for parser in (datetime.fromisoformat,):
        try:
            return parser(candidate)
        except ValueError:
            continue
    return None


def quantile(sorted_values: list[float], q: float) -> float:
    if not sorted_values:
        raise ValueError("quantile requires at least one value")
    if len(sorted_values) == 1:
        return sorted_values[0]
    position = (len(sorted_values) - 1) * q
    lower = int(position)
    upper = min(lower + 1, len(sorted_values) - 1)
    weight = position - lower
    return sorted_values[lower] * (1 - weight) + sorted_values[upper] * weight


def top_values(values: Iterable[str], limit: int = 5) -> list[dict[str, int | str]]:
    counts = Counter(values)
    return [{"value": value, "count": count} for value, count in counts.most_common(limit)]
