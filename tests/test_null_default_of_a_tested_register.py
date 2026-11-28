"""A `null` default of the register the jump just tested is read as the register (96/553, 98/12637 `TransformStream`).

`if (r9 === undefined) r9 = null; ...; r14 = r9; if (r14 != null)`: the reads after the `if` printed the arm's
`null` (`if (null != null)`), so every `transformer.cancel` / `.flush` / `.start` read was dead code.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "null_default_of_a_tested_register_96_553.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_reads_name_the_register():
    out = _render()

    assert "null != r9" in out
    assert "null != null" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0
