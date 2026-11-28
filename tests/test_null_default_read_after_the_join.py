"""A parameter's `null` default is read as the register after the join (96/998 `mapIntoArray`, 98/3523 `parseURL`).

`LoadParam r11; if (r11 === undefined) r11 = null; ...; read r11`: the read after the `if` was the inlined `null`
(`!null || r11.key !== r3.key`), although the register holds the parameter on the other path.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "null_default_read_after_the_join_96_998.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_read_names_the_register():
    out = _render()

    assert "(!r11 || r11.key !== r3.key)" in out
    assert "!null" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0
