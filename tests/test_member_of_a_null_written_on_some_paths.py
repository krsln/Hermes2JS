"""
A member read or store whose base register holds `null` on only some paths into a join names the register (96/998 `mapIntoArray`).

`switch (typeof child) { case "undefined": r14 = null; case "boolean": r14 = null }` writes `null` on two paths and
leaves the child in the register on the third; the loop's `r11[r7]` printed as `null[r7]`, which always throws.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "member_of_a_null_written_on_some_paths_96_998.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 998, strict=False), verbose=False, raw=False)


def test_the_base_is_the_register():
    out = _render()

    assert "r15 = r11[r7];" in out
    assert "null[" not in out
    assert "null." not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
