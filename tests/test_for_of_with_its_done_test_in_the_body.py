"""
A `for-of` whose done test stayed in the loop body prints as a `for-of` (96/3625 `generateValues`).

`for (const s of m.values()) for (const x of s) yield x;`: the inner loop has no exception handler and ends in the
outer loop's latch, so its `IteratorNext` test is not the loop's condition but `if (rN === undefined) continue outer;`
at the top of the body. The bare for-of recognition only knew the loop condition; it now also takes this body test
(when the loop is the last thing of the outer body) and drops it, as `_drop_exit_test` does for the other variants.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "for_of_in_a_generator_loop_96_3625.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_inner_loop_is_a_for_of():
    out = _render()

    assert "for (const r4 of r6)" in out
    assert "yield r4;" in out
    assert "GetIterator" not in out
    assert "while (true)" not in out
    assert "continue loop_2" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
