from __future__ import annotations

import unittest

from agent.generic_agent import run_generic_agent
from agent.proposed_agent import run_proposed_agent


class AgentPackageExportTests(unittest.TestCase):
    def test_agentic_method_package_exports_are_symmetric(self) -> None:
        self.assertTrue(callable(run_generic_agent))
        self.assertTrue(callable(run_proposed_agent))


if __name__ == "__main__":
    unittest.main()
