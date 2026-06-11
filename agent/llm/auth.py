from __future__ import annotations

from pathlib import Path


def load_api_key(path: str | Path) -> str:
    key_path = Path(path)
    raw_key = key_path.read_text(encoding="utf-8").strip()
    if not raw_key:
        raise ValueError(f"empty API key in {key_path}")
    return raw_key
