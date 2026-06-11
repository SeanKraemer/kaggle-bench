from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = ROOT.parents[1] if ROOT.parent.name == "worktrees" else ROOT
DEFAULT_API_KEY_PATH = ROOT / "api_key.txt"
if not DEFAULT_API_KEY_PATH.exists():
    DEFAULT_API_KEY_PATH = WORKSPACE_ROOT / "api_key.txt"
DEFAULT_COMPETITION_SLUG = "zillow-prize-1"
DEFAULT_MODEL_NAME = "claude-sonnet-4-6"
DEFAULT_RUN_BY = "agent_runner"
DEFAULT_CLAUDE_CODE_AUTH_MODE = "subscription"
