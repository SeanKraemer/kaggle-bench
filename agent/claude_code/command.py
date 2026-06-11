from __future__ import annotations

import os
from pathlib import Path


def build_claude_command(
    *,
    model_name: str,
    workdir: Path,
    dataset_root: Path,
    prompt: str,
    max_thinking_tokens: int | None,
) -> list[str]:
    command = [
        "claude",
        "--print",
        "--verbose",
        "--output-format",
        "stream-json",
        "--include-partial-messages",
        "--model",
        model_name,
        "--permission-mode",
        "bypassPermissions",
        f"--add-dir={workdir}",
        f"--add-dir={dataset_root}",
    ]
    if max_thinking_tokens is not None:
        command.extend(["--max-thinking-tokens", str(max_thinking_tokens)])
    command.append(prompt)
    return command


def build_claude_environment(*, workdir: Path, auth_mode: str, api_key: str | None = None) -> dict[str, str]:
    env = dict(os.environ)
    if auth_mode == "subscription":
        env.pop("ANTHROPIC_API_KEY", None)
    elif auth_mode == "api_key":
        env["HOME"] = str(workdir / ".claude-home")
        env["ANTHROPIC_API_KEY"] = api_key or ""
    else:
        raise ValueError(f"Unsupported Claude Code auth_mode: {auth_mode}")
    env["CLAUDE_CODE_EFFORT_LEVEL"] = "auto"
    env.pop("MAX_THINKING_TOKENS", None)
    env.pop("CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING", None)
    return env
