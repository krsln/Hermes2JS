"""
A `for-of` inside the body of another `for-of` prints as a `for-of` (96/10393 `dfs`).

The inner loop's protected range (`IteratorClose` on a throw) lies inside the inner loop's body, but the outer
loop's body holds the inner loop behind an `if`. `_find_loop_nested_home` stopped at the first loop it met, put the
`try` around the whole `if`, and the inner loop stayed a `while (true)` over `GetIterator(..)` with the close printed
as a `finally`. Two changes: the home search goes down to the deepest loop that holds every protected block, and the
done test of the inner loop (`if (rN === undefined) continue outer;`, the exit jumps to the outer latch) is dropped
when the loop is the last thing of the outer body: a `for-of` ends by itself.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "nested_for_of_in_a_for_of_96_10393.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_both_loops_are_for_of():
    out = _render()

    assert "for (let r9 of r2)" in out
    assert "for (const r11 of r7)" in out
    assert "GetIterator" not in out
    assert "while (true)" not in out


def test_no_close_or_done_test_is_left():
    out = _render()

    assert "finally" not in out
    assert ".return()" not in out
    assert "continue loop_1" not in out
    assert "=== undefined" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
