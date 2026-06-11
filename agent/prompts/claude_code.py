from __future__ import annotations

from agent.prompts.shared import render_shared_prompt


def build_claude_code_prompt(
    *,
    task_text: str,
    context_summary: str,
    candidate_actions: str,
    output_format: str,
    prediction_filename: str,
    dataset_symlink_path: str,
) -> str:
    method_instruction = (
        "Use the provided workspace files to analyze the benchmark instance and "
        f"write the final JSON prediction to `{prediction_filename}`. "
        "You may inspect files in the current working directory, including the "
        f"actual raw dataset files exposed at `{dataset_symlink_path}`. Avoid "
        "loading large dataset files fully into memory unless it is clearly "
        "necessary. Keep the final answer limited to the required benchmark "
        "prediction structure."
    )
    return render_shared_prompt(
        task_text=task_text,
        method_instruction=method_instruction,
        dataset_summary=(
            "No precomputed dataset summary is provided for this method. "
            f"Inspect the raw dataset files under `{dataset_symlink_path}` and any workspace files as needed."
        ),
        context_summary=context_summary,
        candidate_actions=candidate_actions,
        output_format=output_format,
    )
