from __future__ import annotations


class CostCapExceeded(RuntimeError):
    """Raised when a run exceeds its configured cost cap."""


def enforce_cost_cap(*, current_cost_usd: float, cost_cap_usd: float) -> None:
    if current_cost_usd > cost_cap_usd:
        raise CostCapExceeded(f"Run cost cap exceeded: {current_cost_usd:.6f} > {cost_cap_usd:.6f}")
