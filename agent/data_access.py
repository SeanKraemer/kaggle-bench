from __future__ import annotations

import csv
import io
import random
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


def _normalize_join_columns(columns: str | list[str] | None) -> list[str]:
    if isinstance(columns, str):
        return [columns] if columns else []
    if isinstance(columns, list):
        return [column for column in columns if isinstance(column, str) and column]
    return []


def _build_join_key(row: dict[str, str], columns: list[str]) -> str | tuple[str, ...] | None:
    values = tuple(row.get(column, "") for column in columns)
    if not columns or any(value == "" for value in values):
        return None
    if len(values) == 1:
        return values[0]
    return values


DEFAULT_FULL_LOAD_MAX_CELLS = 10_000_000
DEFAULT_FULL_LOAD_MAX_BYTES = 128 * 1024 * 1024
DEFAULT_SAMPLE_ROW_COUNT = 50_000
DEFAULT_SAMPLE_RANDOM_SEED = 0


@dataclass(frozen=True)
class TableInspection:
    row_count: int
    column_names: list[str]
    column_count: int
    file_size_bytes: int
    estimated_cells: int


@dataclass(frozen=True)
class TableLoadPlan:
    mode: str
    source_row_count: int
    source_column_count: int
    file_size_bytes: int
    estimated_cells: int
    sample_row_count: int | None


def default_zillow_data_dir(home_dir: str | Path | None = None) -> Path:
    home = Path.home() if home_dir is None else Path(home_dir)
    return home / "Downloads" / "zillow-prize-1"


def _open_csv_text(path: str | Path):
    csv_path = Path(path)
    if csv_path.suffix == ".zip":
        archive = zipfile.ZipFile(csv_path)
        member_names = [name for name in archive.namelist() if not name.endswith("/")]
        if not member_names:
            archive.close()
            raise FileNotFoundError(f"No CSV members found in archive: {csv_path.name}")
        member_handle = archive.open(member_names[0], "r")
        text_handle = io.TextIOWrapper(member_handle, encoding="utf-8", newline="")
        return archive, text_handle
    return None, csv_path.open("r", encoding="utf-8", newline="")


def resolve_dataset_paths(data_root: str | Path, task: dict[str, Any]) -> dict[str, list[Path]]:
    root = Path(data_root)
    dataset = task.get("dataset", {})
    train_paths = [root / name for name in dataset.get("train_files", [])]
    lookup_paths = [root / name for name in dataset.get("lookup_files", [])]

    for path in [*train_paths, *lookup_paths]:
        if not path.exists():
            raise FileNotFoundError(f"Required dataset file not found: {path.name}")

    return {
        "train_files": train_paths,
        "lookup_files": lookup_paths,
    }


def inspect_csv_table(path: str | Path) -> TableInspection:
    csv_path = Path(path)
    archive, handle = _open_csv_text(csv_path)
    with handle:
        reader = csv.DictReader(handle)
        column_names = list(reader.fieldnames or [])
        row_count = 0
        for _ in reader:
            row_count += 1
    if archive is not None:
        archive.close()
    file_size_bytes = csv_path.stat().st_size
    return TableInspection(
        row_count=row_count,
        column_names=column_names,
        column_count=len(column_names),
        file_size_bytes=file_size_bytes,
        estimated_cells=row_count * len(column_names),
    )


def build_table_load_plan(
    inspection: TableInspection,
    *,
    full_load_max_cells: int = DEFAULT_FULL_LOAD_MAX_CELLS,
    full_load_max_bytes: int = DEFAULT_FULL_LOAD_MAX_BYTES,
    sample_row_count: int = DEFAULT_SAMPLE_ROW_COUNT,
) -> TableLoadPlan:
    should_sample = inspection.estimated_cells > full_load_max_cells or inspection.file_size_bytes > full_load_max_bytes
    planned_sample_row_count = min(sample_row_count, inspection.row_count)
    if not should_sample or planned_sample_row_count == inspection.row_count:
        return TableLoadPlan(
            mode="full",
            source_row_count=inspection.row_count,
            source_column_count=inspection.column_count,
            file_size_bytes=inspection.file_size_bytes,
            estimated_cells=inspection.estimated_cells,
            sample_row_count=None,
        )
    return TableLoadPlan(
        mode="sampled",
        source_row_count=inspection.row_count,
        source_column_count=inspection.column_count,
        file_size_bytes=inspection.file_size_bytes,
        estimated_cells=inspection.estimated_cells,
        sample_row_count=planned_sample_row_count,
    )


def load_csv_rows(path: str | Path, limit: int | None = None) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    archive, handle = _open_csv_text(path)
    with handle:
        reader = csv.DictReader(handle)
        for index, row in enumerate(reader):
            rows.append({key: value or "" for key, value in row.items()})
            if limit is not None and index + 1 >= limit:
                break
    if archive is not None:
        archive.close()
    return rows


def load_uniform_sample_rows(
    path: str | Path,
    *,
    sample_row_count: int,
    random_seed: int = DEFAULT_SAMPLE_RANDOM_SEED,
) -> list[dict[str, str]]:
    if sample_row_count <= 0:
        return []

    sampled_rows: list[dict[str, str]] = []
    rng = random.Random(random_seed)
    archive, handle = _open_csv_text(path)
    with handle:
        reader = csv.DictReader(handle)
        for index, row in enumerate(reader):
            normalized_row = {key: value or "" for key, value in row.items()}
            if index < sample_row_count:
                sampled_rows.append(normalized_row)
                continue
            replacement_index = rng.randint(0, index)
            if replacement_index < sample_row_count:
                sampled_rows[replacement_index] = normalized_row
    if archive is not None:
        archive.close()
    return sampled_rows


def load_table_rows_for_summary(
    path: str | Path,
    *,
    full_load_max_cells: int = DEFAULT_FULL_LOAD_MAX_CELLS,
    full_load_max_bytes: int = DEFAULT_FULL_LOAD_MAX_BYTES,
    sample_row_count: int = DEFAULT_SAMPLE_ROW_COUNT,
) -> tuple[list[dict[str, str]], TableLoadPlan]:
    inspection = inspect_csv_table(path)
    plan = build_table_load_plan(
        inspection,
        full_load_max_cells=full_load_max_cells,
        full_load_max_bytes=full_load_max_bytes,
        sample_row_count=sample_row_count,
    )
    if plan.mode == "sampled":
        return (
            load_uniform_sample_rows(path, sample_row_count=plan.sample_row_count or 0),
            plan,
        )
    return load_csv_rows(path), plan


def load_train_table(path: str | Path, limit: int | None = None) -> list[dict[str, str]]:
    return load_csv_rows(path, limit=limit)


def load_lookup_table(path: str | Path, limit: int | None = None) -> list[dict[str, str]]:
    return load_csv_rows(path, limit=limit)


def load_joined_training_view(
    *,
    train_path: str | Path,
    lookup_path: str | Path,
    key_column: str | list[str] | None = None,
    left_on: str | list[str] | None = None,
    right_on: str | list[str] | None = None,
) -> list[dict[str, str]]:
    left_columns = _normalize_join_columns(left_on if left_on is not None else key_column)
    right_columns = _normalize_join_columns(right_on if right_on is not None else key_column)
    if not left_columns or not right_columns:
        raise ValueError("Joined training view requires non-empty join columns.")

    train_rows = load_csv_rows(train_path)
    train_key_set = {join_key for row in train_rows if (join_key := _build_join_key(row, left_columns)) is not None}

    filtered_lookup_rows: dict[str | tuple[str, ...], dict[str, str]] = {}
    archive, handle = _open_csv_text(lookup_path)
    with handle:
        reader = csv.DictReader(handle)
        for row in reader:
            normalized_row = {field: value or "" for field, value in row.items()}
            join_key = _build_join_key(normalized_row, right_columns)
            if join_key is not None and join_key in train_key_set:
                filtered_lookup_rows[join_key] = normalized_row
    if archive is not None:
        archive.close()

    joined_rows: list[dict[str, str]] = []
    for train_row in train_rows:
        merged = dict(train_row)
        lookup_row = filtered_lookup_rows.get(_build_join_key(train_row, left_columns))
        if lookup_row is not None:
            for key, value in lookup_row.items():
                if key not in merged:
                    merged[key] = value
        joined_rows.append(merged)

    return joined_rows
