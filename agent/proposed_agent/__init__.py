from __future__ import annotations

from typing import Any


def run_proposed_agent(*args: Any, **kwargs: Any):
    from agent.proposed_agent.runner import run_proposed_agent as _run_proposed_agent

    return _run_proposed_agent(*args, **kwargs)


__all__ = ["run_proposed_agent"]
