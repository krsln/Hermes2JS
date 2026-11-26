"""
`[, , a, b] = x` is recognised as a pattern when the first hole copies the check's result into the shared flag
register (98/13555).

A leading hole has no initial value to load after the `StrictEq`; Hermes copies the result into the flag register the
later checks use (`Mov r4 <- r2`) instead of the `LoadConstUndefined` the pass expected, so the head block was
parsed as something else and the open-coded `next()` ladder stayed.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "destructuring_with_two_leading_holes_98_13555.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 13555, strict=False), verbose=False, raw=False)


def test_the_holes_stay_holes_in_the_pattern():
    out = _render()

    assert "[, , r5, r6] = r7;" in out
    assert "[r11, r10] = r5;" in out
    assert "GetIterator" not in out
    assert ".next()" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
