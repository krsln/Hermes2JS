"""
A `break` out of a `for-of` leaves no copy of the iterator behind either (98/5913 `convertRedirect`).

Hermes closes the iterator on the way out through a scratch register (`r4 = r5; r5.return(); break;`). The loop's
own close covers the `break`, so `_strip_inline_closes` drops the close; the copy stayed, read the iterator register
by name, and kept `r5 = GetIterator(r7)` alive in front of the loop. The copy goes with the close when nothing that
is still printed reads its register.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "for_of_break_through_a_copy_98_5913.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_iterator_setup_is_gone():
    out = _render()

    assert "of r7)" in out
    assert "GetIterator" not in out
    assert "break;" in out
    assert ".return()" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
