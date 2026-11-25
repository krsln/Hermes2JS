"""
Two `for-of` loops in the arms of an `if`, inside a `for (; cond; ...)` loop whose body ends in code (96/10225).

Each inner loop's `IteratorClose` handler covers only the block that ends the inner loop's body (the call and the
jump back). `_scan_loop_body_protected_extent` took "a latch at the start of the range" to mean the try wraps the
whole loop, so both `try`s went around the whole `if`, and the loops stayed `while (true)` over `GetIterator(..)`
with a `finally { r9.return() }`. A plain jump-back block that is not the first of its body can start the range.
The done test of each inner loop then lands on the outer loop's latch (`r1 = r7; r2 = r8;`), which is also what a
`for-of` falls into, so `_enclosing_loop_it_ends` stops looking for trailing code at that latch.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "for_of_in_a_loop_with_a_latch_96_10225.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_both_inner_loops_are_for_of():
    out = _render()

    assert "for (const r13 of r1)" in out
    assert "for (const r14 of r1)" in out
    assert "GetIterator" not in out
    assert "while (true)" not in out


def test_no_try_or_done_test_is_left():
    out = _render()

    assert "try" not in out
    assert "finally" not in out
    assert ".return()" not in out
    assert "continue loop_2" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
