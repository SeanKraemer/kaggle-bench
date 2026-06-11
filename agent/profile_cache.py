from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from agent.context_builder import BenchmarkContext


PROFILE_CACHE_VERSION = 1


def default_profile_cache_dir() -> Path:
    return Path.home() / ".cache" / "kaggle_bench" / "benchmark_profiles"


def _fingerprint_path(path: Path) -> dict[str, int | str]:
    stat = path.stat()
    return {
        "path": str(path.resolve()),
        "size": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
    }


def build_profile_cache_key(benchmark: BenchmarkContext) -> str:
    payload = {
        "version": PROFILE_CACHE_VERSION,
        "task": benchmark.bundle.task,
        "visible_actions": benchmark.visible_actions,
        "dataset_paths": {
            "train_files": [
                _fingerprint_path(path)
                for path in benchmark.dataset_paths.get("train_files", [])
            ],
            "lookup_files": [
                _fingerprint_path(path)
                for path in benchmark.dataset_paths.get("lookup_files", [])
            ],
        },
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def load_profile_cache(*, cache_dir: str | Path | None, cache_key: str) -> dict | None:
    root = default_profile_cache_dir() if cache_dir is None else Path(cache_dir)
    cache_path = root / f"{cache_key}.json"
    if not cache_path.exists():
        return None
    try:
        payload = json.loads(cache_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return payload if isinstance(payload, dict) else None


def write_profile_cache(*, cache_dir: str | Path | None, cache_key: str, payload: dict) -> Path:
    root = default_profile_cache_dir() if cache_dir is None else Path(cache_dir)
    root.mkdir(parents=True, exist_ok=True)
    cache_path = root / f"{cache_key}.json"
    cache_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return cache_path
