"""
`const [a] = x` with one element prints as a pattern, and what reads `a` afterwards reads `a` (98/9900).

For one element Hermes loads a single `undefined` that serves as the value the done check compares with and as the
element's initial value, and fetches from the source register itself: `IteratorNext, Mov, LoadConstUndefined,
StrictEq, JmpTrue`. `ArrayDestructuringCfgPass._parse` knew the shapes with a separate load and left this one as
`GetIterator(..)` with `if (rIt !== undefined)` guards. Matching it exposed a second thing: the frontend had read
`a` through the dropped `Mov a <- v` as the fetched register `v`, so `return a === b` printed `return r3 === r1`.
The reads that hold that very node now read the target register.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "single_element_destructuring_98_9900.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_pattern_is_printed():
    out = _render()

    assert "[r2] = param1;" in out
    assert "GetIterator" not in out
    assert ".return()" not in out


def test_the_element_is_read_from_its_own_register():
    out = _render()

    assert "return r2 === r1;" in out
    assert "r3" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
