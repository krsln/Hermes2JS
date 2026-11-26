"""
A `return` out of a `for-of` leaves no iterator copy when the copy's register is reused for the value (98/8004 `deepEqual`).

Hermes closes the iterator before `return false` through the register that then holds the value (`r8 = r1;
r8.return(); r8 = false; return r8;`). The copy was kept because the `return` names `r8`, and it kept
`r1 = GetIterator(r0)` alive. A copy that is written again before anything reads it holds nothing and goes.
"""


import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "for_of_return_through_a_reused_copy_98_8004.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_iterator_setup_is_gone():
    out = _render()

    assert "of r0)" in out
    assert "GetIterator" not in out
    assert "return false;" in out
    assert ".return()" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
