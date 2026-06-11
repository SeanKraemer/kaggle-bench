from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Any

from agent.agentic_core.scratchpad import DEFAULT_SCRATCHPAD_MAX_CHARS, JsonScratchpad
from agent.agentic_core.scratchpad_tools import build_scratchpad_tool_specs
from agent.agentic_core.types import AgenticToolSpec


GENERIC_TOOL_NAMES = ["bash", "python", "scratchpad_read", "scratchpad_write"]
DEFAULT_TOOL_TIMEOUT_SECONDS = 30
DEFAULT_TOOL_OUTPUT_MAX_CHARS = 4000
DEFAULT_OUTPUT_MAX_CHARS = DEFAULT_TOOL_OUTPUT_MAX_CHARS


def _truncate(text: str, *, max_chars: int) -> tuple[str, bool]:
    if len(text) <= max_chars:
        return text, False
    return text[:max_chars], True


def _guard_generic_code(text: str, *, repo_root: Path) -> None:
    blocked_fragments = [
        str(repo_root),
        "import agent",
        "from agent",
        "agent.tool_registry",
        "agent.profiles",
        "agent.context_builder",
        "agent.data_access",
        "../",
        "..\\",
    ]
    for fragment in blocked_fragments:
        if fragment and fragment in text:
            raise ValueError(f"generic tool input references blocked fragment: {fragment}")


def _default_executor(
    *,
    command: str | list[str],
    cwd: Path,
    env: dict[str, str],
    timeout_seconds: int | float,
    shell: bool,
) -> dict[str, Any]:
    result = subprocess.run(
        command,
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True,
        check=False,
        timeout=timeout_seconds,
        shell=shell,
    )
    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def _tool_env() -> dict[str, str]:
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    return env


def _normalize_exec_result(result: dict[str, Any], *, max_output_chars: int) -> dict[str, Any]:
    stdout, stdout_truncated = _truncate(str(result.get("stdout", "")), max_chars=max_output_chars)
    stderr, stderr_truncated = _truncate(str(result.get("stderr", "")), max_chars=max_output_chars)
    return {
        "returncode": result.get("returncode"),
        "stdout": stdout,
        "stderr": stderr,
        "stdout_truncated": stdout_truncated,
        "stderr_truncated": stderr_truncated,
    }


def build_generic_tool_specs(
    *,
    workdir: Path,
    scratchpad: JsonScratchpad,
    repo_root: Path,
    timeout_seconds: int | float = DEFAULT_TOOL_TIMEOUT_SECONDS,
    max_output_chars: int = DEFAULT_TOOL_OUTPUT_MAX_CHARS,
    bash_executor=_default_executor,
    python_executor=_default_executor,
) -> list[AgenticToolSpec]:
    resolved_workdir = workdir.resolve()
    resolved_repo_root = repo_root.resolve()

    def bash_handler(payload: dict[str, Any]) -> dict[str, Any]:
        command = payload.get("command")
        if not isinstance(command, str) or not command.strip():
            raise ValueError("bash tool requires a non-empty string `command`")
        _guard_generic_code(command, repo_root=resolved_repo_root)
        result = bash_executor(
            command=command,
            cwd=resolved_workdir,
            env=_tool_env(),
            timeout_seconds=timeout_seconds,
            shell=True,
        )
        return _normalize_exec_result(result, max_output_chars=max_output_chars)

    def python_handler(payload: dict[str, Any]) -> dict[str, Any]:
        code = payload.get("code")
        script_path = payload.get("script_path")
        if isinstance(code, str) and code.strip():
            _guard_generic_code(code, repo_root=resolved_repo_root)
            command: str | list[str] = [sys.executable, "-c", code]
        elif isinstance(script_path, str) and script_path.strip():
            _guard_generic_code(script_path, repo_root=resolved_repo_root)
            resolved_script = (resolved_workdir / script_path).resolve()
            if not str(resolved_script).startswith(str(resolved_workdir)):
                raise ValueError("python script_path must stay inside the prepared workspace")
            command = [sys.executable, str(resolved_script)]
        else:
            raise ValueError("python tool requires `code` or `script_path`")
        result = python_executor(
            command=command,
            cwd=resolved_workdir,
            env=_tool_env(),
            timeout_seconds=timeout_seconds,
            shell=False,
        )
        return _normalize_exec_result(result, max_output_chars=max_output_chars)

    tools = [
        AgenticToolSpec(
            name="bash",
            description="Run a shell command inside the prepared generic-agent workspace.",
            input_schema={
                "type": "object",
                "properties": {"command": {"type": "string"}},
                "required": ["command"],
            },
            handler=bash_handler,
        ),
        AgenticToolSpec(
            name="python",
            description="Run Python code or a Python script inside the prepared workspace.",
            input_schema={
                "type": "object",
                "properties": {
                    "code": {"type": "string"},
                    "script_path": {"type": "string"},
                },
            },
            handler=python_handler,
        ),
    ]
    tools.extend(build_scratchpad_tool_specs(scratchpad=scratchpad))
    return tools
