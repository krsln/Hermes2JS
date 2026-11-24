"""
A jump that lands on the first block of one ARM of a later sibling `if` prints as a labeled block (F-314, 96/2141).

    if (26 === tag) { ... } else if (5 !== tag && 27 !== tag) goto A;   // A: the arm of the `if (r16)` below
    ...
    if (r16) { ... } else { A: ... }

The code that jumps and the test of the `if` go into `label_A: { ... }`, the other arm leaves the whole by
`break label_A_end;`. A jump out of a loop from inside a `switch` (`goto 718`) is the plain sibling case.
Without the split the function kept one `goto`.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "jump_onto_an_arm_of_a_later_if_96_2141.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 2141, strict=False), verbose=False, raw=False)


def test_the_jump_onto_the_arm_of_a_later_if_is_a_labeled_break():
    out = _render()

    assert "goto label_" not in out
    assert "label_413_end: {" in out
    assert "break label_413;" in out
    assert "break label_413_end;" in out
    assert out.count("break label_718;") == 3


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_labeled_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
