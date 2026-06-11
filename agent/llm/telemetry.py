from __future__ import annotations


def build_trace_entry(
    *,
    attempt_index: int,
    status: str,
    prompt_text: str,
    response_text: str,
    input_tokens: int | None,
    output_tokens: int | None,
    cost_usd: float | None,
    parsed_prediction: dict | None = None,
    validation_warnings: list[str] | None = None,
    error_message: str | None = None,
    thinking_summaries: list[str] | None = None,
    cache_usage: dict | None = None,
) -> dict:
    total_tokens = None
    if input_tokens is not None or output_tokens is not None:
        total_tokens = (input_tokens or 0) + (output_tokens or 0)
    return {
        "attempt_index": attempt_index,
        "status": status,
        "prompt_text": prompt_text,
        "response_text": response_text,
        "usage": {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
        },
        "cost_usd": cost_usd,
        "parsed_prediction": parsed_prediction,
        "validation_warnings": validation_warnings or [],
        "error_message": error_message,
        "thinking_summaries": thinking_summaries or [],
        "cache_usage": cache_usage or {},
    }


def render_trace_markdown(title: str, trace_entries: list[dict]) -> str:
    lines = [f"# {title}", ""]
    for entry in trace_entries:
        lines.append(f"## Attempt {entry['attempt_index']}")
        lines.append(f"- Status: `{entry['status']}`")
        lines.append(f"- Cost (USD): `{entry['cost_usd']}`")
        lines.append(f"- Input tokens: `{entry['usage']['input_tokens']}`")
        lines.append(f"- Output tokens: `{entry['usage']['output_tokens']}`")
        lines.append("")
        if entry.get("parsed_prediction") is not None:
            prediction = entry["parsed_prediction"]
            lines.append("### Prediction Summary")
            lines.append(f"- Parsed add ids: `{prediction.get('predicted_add_action_ids', [])}`")
            lines.append(f"- Parsed remove ids: `{prediction.get('predicted_remove_action_ids', [])}`")
            lines.append(f"- Parsed add count: `{len(prediction.get('predicted_add_action_ids', []))}`")
            lines.append(f"- Parsed remove count: `{len(prediction.get('predicted_remove_action_ids', []))}`")
            lines.append("")
            if prediction.get("notes"):
                lines.append("### Model Notes")
                lines.append(prediction["notes"])
                lines.append("")
            if prediction.get("action_rationales"):
                lines.append("### Action Rationales")
                for rationale in prediction["action_rationales"]:
                    lines.append(f"- `{rationale['action_id']}` (`{rationale['decision']}`): {rationale['reason']}")
                lines.append("")
        if entry.get("validation_warnings"):
            lines.append("### Validation Warnings")
            for warning in entry["validation_warnings"]:
                lines.append(f"- {warning}")
            lines.append("")
        if entry.get("thinking_summaries"):
            lines.append("### Thinking Summary")
            for thinking_summary in entry["thinking_summaries"]:
                lines.append(f"- {thinking_summary}")
            lines.append("")
        if entry.get("cache_usage"):
            lines.append("### Cache Usage")
            for key, value in entry["cache_usage"].items():
                lines.append(f"- {key}={value}")
            lines.append("")
        if entry.get("error_message"):
            lines.append("### Error")
            lines.append(entry["error_message"])
            lines.append("")
        lines.append("### Prompt")
        lines.append(entry["prompt_text"])
        lines.append("")
        lines.append("### Response")
        lines.append(entry["response_text"])
        lines.append("")
    return "\n".join(lines).strip() + "\n"
