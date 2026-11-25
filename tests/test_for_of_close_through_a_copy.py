"""
The close of a `for-of` that leaves through a `return` prints nothing, copy included (98/13334 `findInMenu`).

Hermes closes the iterator on every way out of the loop, reading it through a scratch register (`r11 = r2;
r11.return(); return r8;`). The loop's own close already covers the `return`, so `_strip_inline_closes` drops the
close; it kept the copy (`r11 = r2;`) and the `GetIterator(..)` setup that the copy still read. It now takes the pair
before a `return` as well as before a `break`, and a copy left alone before a `return` when nothing after reads it.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "for_of_close_through_a_copy_98_13334.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_copy_or_setup_of_the_iterator_is_left():
    out = _render()

    assert "for (let r10 of r6)" in out
    assert "GetIterator" not in out
    assert "r11 = r2" not in out
    assert ".return()" not in out
    assert "return r8;" in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
