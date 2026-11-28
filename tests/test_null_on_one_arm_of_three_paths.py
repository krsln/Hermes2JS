"""A `null` written on one arm of a three-path join is read as the register (96/12871 `Color`).

`r3 = p; if (p) { r3 = p; if (p in table) r3 = null }; <read r3>`: the read sees `p`, `null` or the falsy `p`. The
nested-join guard named the register only for identifiers and binary expressions, so the constant was inlined:
`!r3 || null in table`, `if (!null) model = "rgb"`.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "null_on_one_arm_of_three_paths_96_12871.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_reads_name_the_register():
    out = _render()

    assert "!r3 || r3 in r4[2]" in out
    assert "if (!r3) {" in out
    assert "null in " not in out
    assert "!null" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0
