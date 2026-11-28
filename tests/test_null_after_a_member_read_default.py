"""A `null` that defaults a member read is read as the register after the join (98/5017 `Asset`, 96/13091).

`r6 = x.y; if (r6 == null) r6 = null; ...; if (r6)`: the test after the `if` printed the arm's `null` (`if (null)`),
although the register holds the member value on the other path.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "null_after_a_member_read_default_98_5017.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_test_reads_the_register():
    out = _render()

    assert "if (r6) {" in out
    assert "if (null) {" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0
