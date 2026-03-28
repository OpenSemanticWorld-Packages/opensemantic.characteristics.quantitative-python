"""Ensure all example scripts in examples/ run without errors."""

import subprocess
import sys
from pathlib import Path

import pytest

EXAMPLES_DIR = Path(__file__).resolve().parent.parent / "examples"
EXAMPLE_SCRIPTS = sorted(EXAMPLES_DIR.glob("*.py"))


@pytest.mark.parametrize(
    "script",
    EXAMPLE_SCRIPTS,
    ids=[s.stem for s in EXAMPLE_SCRIPTS],
)
def test_example_runs(script):
    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert result.returncode == 0, (
        f"{script.name} failed with exit code {result.returncode}\n"
        f"stderr:\n{result.stderr}"
    )
