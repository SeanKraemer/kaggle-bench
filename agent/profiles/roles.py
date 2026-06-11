from __future__ import annotations

from agent.profiles.schema import profile_table_schema


def infer_column_roles(rows: list[dict[str, str]], task: dict) -> dict[str, str]:
    schema_profile = profile_table_schema(rows)
    dataset = task.get("dataset", {})
    primary_key = dataset.get("primary_key")
    target_column = dataset.get("target_column")

    roles: dict[str, str] = {}
    for column, column_profile in schema_profile["columns"].items():
        if column == primary_key:
            roles[column] = "primary_key"
            continue
        if column == target_column:
            roles[column] = "target"
            continue
        inferred_type = column_profile["inferred_type"]
        if inferred_type == "datetime_like":
            roles[column] = "datetime_feature"
        elif inferred_type in {"integer_like", "numeric_like"}:
            roles[column] = "numeric_feature"
        else:
            roles[column] = "categorical_feature"
    return roles
