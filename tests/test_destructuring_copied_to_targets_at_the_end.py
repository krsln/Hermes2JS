"""
`[x, y, z] = src` into outer variables, the targets copied once at the end (98/13553; 98/11846 `HSVtoRGB`).

The element registers are temporaries; the last block copies every one into its target (last element first) and the
close block repeats those copies after `IteratorClose`. The pass knew the binding form that copies each target at the
next element's boundary and mixed the first copy up with such a boundary copy, so the open-coded `next()` ladder stayed.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "destructuring_copied_to_targets_at_the_end_98_13553.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_targets_are_the_pattern():
    out = _render()

    assert "[r7, r6, r5] = r11;" in out
    assert "GetIterator" not in out
    assert ".next()" not in out
    assert ".return()" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
