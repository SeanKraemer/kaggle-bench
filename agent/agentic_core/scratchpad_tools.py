from __future__ import annotations

from typing import Any

from agent.agentic_core.scratchpad import JsonScratchpad
from agent.agentic_core.types import AgenticToolSpec


def build_scratchpad_tool_specs(
    *,
    scratchpad: JsonScratchpad,
    read_description: str = "Read the run-local scratchpad.",
    write_description: str = "Append an entry to the run-local scratchpad.",
) -> list[AgenticToolSpec]:
    def scratchpad_read_handler(_: dict[str, Any]) -> dict[str, Any]:
        return scratchpad.read()

    def scratchpad_write_handler(payload: dict[str, Any]) -> dict[str, Any]:
        if "entry" in payload:
            entry = payload["entry"]
        elif "note" in payload:
            entry = payload["note"]
        else:
            entry = payload
        return scratchpad.write(entry)

    return [
        AgenticToolSpec(
            name="scratchpad_read",
            description=read_description,
            input_schema={"type": "object", "properties": {}},
            handler=scratchpad_read_handler,
        ),
        AgenticToolSpec(
            name="scratchpad_write",
            description=write_description,
            input_schema={
                "type": "object",
                "properties": {"entry": {}, "note": {"type": "string"}},
            },
            handler=scratchpad_write_handler,
        ),
    ]
