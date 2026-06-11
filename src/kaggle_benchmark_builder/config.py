from __future__ import annotations

import os
from pathlib import Path


def _normalize_env_value(raw: str) -> str:
    # Supports plain values and one layer of matching quotes; escape expansion is intentionally not implemented.
    text = raw.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in {"'", '"'}:
        return text[1:-1]
    return text


def load_dotenv_file(path: str = ".env", override: bool = False) -> None:
    env_path = Path(path)
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        text = line.strip()
        if text.startswith("export "):
            text = text[len("export ") :].strip()
        if not text or text.startswith("#") or "=" not in text:
            continue
        key, value = text.split("=", 1)
        key = key.strip()
        value = _normalize_env_value(value)
        if not key:
            continue
        if key in os.environ and not override:
            continue
        os.environ[key] = value
