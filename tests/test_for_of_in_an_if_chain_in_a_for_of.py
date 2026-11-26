"""
A `for-of` behind a chain of `if`s inside another `for-of` keeps its own close handler (98/8056 `filterCSSAndStyleProperties`).

The inner loop's protected range starts inside it and ends with a `continue` trampoline block (a lone `JmpLong`) that
lies in the outer loop's region, outside the `if` chain that holds the rest of the range. The descent into the chain
wanted every protected block inside it, gave up, and wrapped BOTH handlers around the outer loop - `try { try {
for ... } catch (e) { r19.return(); throw e } } catch (e) { r7.return(); throw e }` - which kept both
`GetIterator` lines. A jump-only block no longer blocks the descent.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "for_of_in_an_if_chain_in_a_for_of_98_8056.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 8056, strict=False), verbose=False, raw=False)


def test_both_loops_are_plain_for_of_loops():
    out = _render()

    assert "for (const [r17, r16] of r11)" in out
    assert "for (const [r14, r13] of r18)" in out
    assert "GetIterator" not in out
    assert ".return()" not in out
    assert "try {" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
