"""
`const [a, b] = x` where `a` lives in the closure environment and `b` in a register (98/9949).

Element 1 is stored into an environment slot through a scratch register (`r5`), and element 2 then takes that same
register as its own target. `ArrayDestructuringCfgPass._match` refused any pattern whose scratch register was also a
leaf. A scratch register that a later element takes over holds the later element afterwards, so there is nothing of
the first one to restore and the pattern is printed.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "destructuring_slot_then_register_98_9949.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_pattern_is_printed():
    out = _render()

    assert "[__environment__[0], r5] = param1;" in out
    assert "GetIterator" not in out
    assert ".return()" not in out
    assert "r5 = r5.map(function_12722);" in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
