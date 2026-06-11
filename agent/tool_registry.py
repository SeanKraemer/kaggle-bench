from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from agent.action_bank import build_agent_visible_action_bank
from agent.data_access import load_csv_rows, load_joined_training_view, resolve_dataset_paths
from agent.profiles.boolean_like import profile_boolean_like_columns
from agent.profiles.join import profile_join_key
from agent.profiles.missingness import profile_missingness
from agent.profiles.numeric import profile_numeric_columns
from agent.profiles.schema import profile_table_schema
from agent.profiles.target import profile_target_distribution
from agent.task_bundle import load_task_bundle


@dataclass(frozen=True)
class ToolSpec:
    name: str
    description: str
    handler: Callable[..., Any]
    input_schema: dict[str, Any] = field(default_factory=dict)


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, ToolSpec] = {}

    def register(self, tool: ToolSpec) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> ToolSpec:
        return self._tools[name]

    def list_tool_names(self) -> list[str]:
        return sorted(self._tools)

    def call(self, name: str, *args, **kwargs):
        return self.get(name).handler(*args, **kwargs)


def build_benchmark_tool_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register(ToolSpec(name="load_task_bundle", description="Load benchmark task, testcase, and candidate actions.", handler=load_task_bundle))
    registry.register(ToolSpec(name="build_agent_visible_action_bank", description="Build the agent-visible candidate action bank.", handler=build_agent_visible_action_bank))
    registry.register(ToolSpec(name="resolve_dataset_paths", description="Resolve benchmark dataset file paths.", handler=resolve_dataset_paths))
    registry.register(ToolSpec(name="load_csv_rows", description="Load CSV rows into memory.", handler=load_csv_rows))
    registry.register(ToolSpec(name="load_joined_training_view", description="Build the joined training view using resolved join columns.", handler=load_joined_training_view))
    registry.register(ToolSpec(name="profile_table_schema", description="Profile schema and inferred types for a table.", handler=profile_table_schema))
    registry.register(ToolSpec(name="profile_missingness", description="Profile column-level missingness.", handler=profile_missingness))
    registry.register(ToolSpec(name="profile_numeric_columns", description="Profile numeric column distributions.", handler=profile_numeric_columns))
    registry.register(ToolSpec(name="profile_boolean_like_columns", description="Profile boolean-like columns.", handler=profile_boolean_like_columns))
    registry.register(ToolSpec(name="profile_join_key", description="Profile join-key overlap and coverage.", handler=profile_join_key))
    registry.register(ToolSpec(name="profile_target_distribution", description="Profile target-column distribution.", handler=profile_target_distribution))
    return registry
