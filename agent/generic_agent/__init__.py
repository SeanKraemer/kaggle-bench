from __future__ import annotations

from typing import Any


def run_generic_agent(*args: Any, **kwargs: Any):
    from agent.generic_agent.runner import run_generic_agent as _run_generic_agent

    return _run_generic_agent(*args, **kwargs)


__all__ = ["run_generic_agent"]
