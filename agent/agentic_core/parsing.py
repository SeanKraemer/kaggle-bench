from __future__ import annotations

from pathlib import Path
from typing import Callable


def parse_text_or_prediction_file(
    raw_text: str,
    *,
    prediction_path: str | Path,
    parse_and_validate: Callable[[str], tuple[dict, list[str]]],
) -> tuple[dict, list[str]]:
    try:
        return parse_and_validate(raw_text)
    except Exception as text_error:
        path = Path(prediction_path)
        if not path.exists():
            raise text_error
        return parse_and_validate(path.read_text(encoding="utf-8"))
