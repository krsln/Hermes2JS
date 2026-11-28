"""A member of the global object keeps `globalThis` as its base (98/11768 `anonymous`).

`r4 = globalThis; r8 = r4.Object; r7 = r8.entries; <r4 = default | r4 = parse(...)>; r4 = r7(r8, r4)`: the member's base
was the very node of the printed `r4 = globalThis`, a pass that repoints the readers of that node made it `r4`, and
the call printed `r4.Object.entries(r4)` after the arms had overwritten `r4`.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "global_base_kept_when_the_register_is_overwritten_98_11768.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_call_reads_the_global():
    out = _render()

    assert "r4 = Object.entries(r4);" in out
    assert "r4.Object" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0
