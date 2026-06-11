from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from agent.agentic_core.scratchpad import JsonScratchpad
from agent.agentic_core.tool_runtime import AgenticToolRuntime
from agent.agentic_core.types import AgenticToolCall
from agent.generic_agent.tools import build_generic_tool_specs


class GenericAgentToolTests(unittest.TestCase):
    def test_bash_tool_runs_inside_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            (workdir / "sample.txt").write_text("hello", encoding="utf-8")
            scratchpad = JsonScratchpad(workdir / "scratchpad.json")
            runtime = AgenticToolRuntime(
                build_generic_tool_specs(
                    workdir=workdir,
                    scratchpad=scratchpad,
                    repo_root=Path("/repo-root"),
                )
            )

            result = runtime.call(
                AgenticToolCall(
                    tool_call_id="toolu_bash",
                    name="bash",
                    input={"command": "cat sample.txt"},
                )
            )

        self.assertFalse(result.is_error)
        self.assertEqual(result.output["stdout"], "hello")

    def test_python_tool_runs_inside_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            scratchpad = JsonScratchpad(workdir / "scratchpad.json")
            runtime = AgenticToolRuntime(
                build_generic_tool_specs(
                    workdir=workdir,
                    scratchpad=scratchpad,
                    repo_root=Path("/repo-root"),
                )
            )

            result = runtime.call(
                AgenticToolCall(
                    tool_call_id="toolu_python",
                    name="python",
                    input={"code": "from pathlib import Path; print(Path.cwd().name)"},
                )
            )

        self.assertFalse(result.is_error)
        self.assertIn(Path(tmp).name, result.output["stdout"])

    def test_tool_output_truncates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            scratchpad = JsonScratchpad(workdir / "scratchpad.json")
            runtime = AgenticToolRuntime(
                build_generic_tool_specs(
                    workdir=workdir,
                    scratchpad=scratchpad,
                    repo_root=Path("/repo-root"),
                    max_output_chars=5,
                )
            )

            result = runtime.call(
                AgenticToolCall(
                    tool_call_id="toolu_python",
                    name="python",
                    input={"code": "print('abcdef')"},
                )
            )

        self.assertEqual(result.output["stdout"], "abcde")
        self.assertTrue(result.output["stdout_truncated"])

    def test_scratchpad_tools_work(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            scratchpad = JsonScratchpad(workdir / "scratchpad.json")
            runtime = AgenticToolRuntime(
                build_generic_tool_specs(
                    workdir=workdir,
                    scratchpad=scratchpad,
                    repo_root=Path("/repo-root"),
                )
            )

            runtime.call(
                AgenticToolCall(
                    tool_call_id="toolu_write",
                    name="scratchpad_write",
                    input={"entry": {"note": "remember"}},
                )
            )
            read_result = runtime.call(AgenticToolCall(tool_call_id="toolu_read", name="scratchpad_read", input={}))

        self.assertEqual(read_result.output["entries"], [{"note": "remember"}])

    def test_tools_reject_repo_helper_access(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            scratchpad = JsonScratchpad(workdir / "scratchpad.json")
            runtime = AgenticToolRuntime(
                build_generic_tool_specs(
                    workdir=workdir,
                    scratchpad=scratchpad,
                    repo_root=Path("/repo-root"),
                )
            )

            result = runtime.call(
                AgenticToolCall(
                    tool_call_id="toolu_python",
                    name="python",
                    input={"code": "import agent.tool_registry"},
                )
            )

        self.assertTrue(result.is_error)
        self.assertIn("blocked fragment", result.output_text)


if __name__ == "__main__":
    unittest.main()
