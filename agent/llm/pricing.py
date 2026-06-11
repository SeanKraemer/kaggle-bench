from __future__ import annotations


def estimate_cost_usd(
    *,
    input_tokens: int | None,
    output_tokens: int | None,
    input_cost_per_million: float,
    output_cost_per_million: float,
    cache_read_input_tokens: int | None = None,
    cache_creation: dict | None = None,
    cache_creation_input_tokens: int | None = None,
    cache_read_cost_per_million: float = 0.0,
    cache_write_5m_cost_per_million: float = 0.0,
    cache_write_1h_cost_per_million: float = 0.0,
) -> float:
    in_tokens = 0 if input_tokens is None else input_tokens
    out_tokens = 0 if output_tokens is None else output_tokens
    cache_read_tokens = 0 if cache_read_input_tokens is None else cache_read_input_tokens
    cache_write_5m_tokens = 0
    cache_write_1h_tokens = 0
    if cache_creation:
        cache_write_5m_tokens = cache_creation.get("ephemeral_5m_input_tokens", 0)
        cache_write_1h_tokens = cache_creation.get("ephemeral_1h_input_tokens", 0)
    elif cache_creation_input_tokens is not None:
        cache_write_5m_tokens = cache_creation_input_tokens

    return (
        (in_tokens * input_cost_per_million / 1_000_000)
        + (out_tokens * output_cost_per_million / 1_000_000)
        + (cache_read_tokens * cache_read_cost_per_million / 1_000_000)
        + (cache_write_5m_tokens * cache_write_5m_cost_per_million / 1_000_000)
        + (cache_write_1h_tokens * cache_write_1h_cost_per_million / 1_000_000)
    )
