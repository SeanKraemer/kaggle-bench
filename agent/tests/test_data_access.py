from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA_ACCESS_PATH = ROOT / "agent" / "data_access.py"


def load_data_access_module():
    spec = importlib.util.spec_from_file_location("agent_data_access", DATA_ACCESS_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load data_access module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class DataAccessTests(unittest.TestCase):
    def test_default_zillow_data_dir_uses_downloads_subdirectory(self) -> None:
        data_access = load_data_access_module()

        data_dir = data_access.default_zillow_data_dir(home_dir=Path("/tmp/fake-home"))

        self.assertEqual(data_dir, Path("/tmp/fake-home/Downloads/zillow-prize-1"))
