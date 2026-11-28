"""A `null` that two jumps land on is read as the register, and the copy on the other path prints (98/2044 `mapIntoArray`).

`Mov r14, p; <boolean test> -> L; r14 = null; L:` entered from `undefined` too. The read after the span saw only the
`null` (`if (null !== null)`), and the copy `r14 = param1` was printed nowhere, so the default path left `r14` unset.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "null_met_by_two_jumps_98_2044.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_read_names_the_register():
    out = _render()

    assert "null !== r14" in out
    assert "if (null !== null)" not in out


def test_the_copy_on_the_other_path_prints():
    assert "r14 = param1;" in _render()


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0
