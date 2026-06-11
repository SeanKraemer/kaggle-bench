from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DEFAULT_SCRATCHPAD_MAX_CHARS = 20_000


class JsonScratchpad:
    def __init__(self, path: str | Path, *, max_chars: int = DEFAULT_SCRATCHPAD_MAX_CHARS) -> None:
        self.path = Path(path)
        self.max_chars = max_chars
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self._write_payload({"entries": []})

    def read(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"entries": []}
        return json.loads(self.path.read_text(encoding="utf-8"))

    def list_entries(self) -> list[Any]:
        payload = self.read()
        entries = payload.get("entries", [])
        return entries if isinstance(entries, list) else []

    def write(self, entry: Any) -> dict[str, Any]:
        payload = self.read()
        entries = payload.get("entries", [])
        if not isinstance(entries, list):
            entries = []
        entries.append(entry)
        next_payload = {"entries": entries}
        self._write_payload(next_payload)
        return next_payload

    def _write_payload(self, payload: dict[str, Any]) -> None:
        rendered = json.dumps(payload, indent=2)
        if len(rendered) > self.max_chars:
            raise ValueError(
                f"scratchpad size limit exceeded: {len(rendered)} > {self.max_chars}"
            )
        self.path.write_text(rendered, encoding="utf-8")
