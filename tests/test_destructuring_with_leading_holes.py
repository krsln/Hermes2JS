"""
`[, , a, b, c, d] = x` with the first elements skipped is recognised as a pattern (98/7996 `C`).

With the source copied first (`Mov t <- src`), the `undefined` the done checks compare with is loaded between the
fetch and the check, ahead of the `StrictEq` (a shape the pass only knew without the copy, for a single element). It
is no element's initial value, so only a pattern whose first element is a hole can use it; the open-coded
`next()`/`=== undefined` ladder was left otherwise.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "destructuring_with_leading_holes_98_7996.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_holes_stay_holes_in_the_pattern():
    out = _render()

    assert "[, , r9, r8, r7, r6] = r10;" in out
    assert "GetIterator" not in out
    assert ".next()" not in out
    assert ".return()" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
