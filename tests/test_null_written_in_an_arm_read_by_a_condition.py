"""
A `null` written in an `if` arm and read by the condition right after it names the register (98/3490 `TextDecoder`).

`r6 = lookup[...]; if (r6 == null) { r6 = null }` and then `r6 === null || r6.name === "replacement"`: the condition
held the arm's own `null` node and printed `null === null`. The repair looked for the reader of a test at the last
instruction BEFORE the `if` whose arm wrote the register, which cannot be reached from that write, so it left the
condition alone. The reader of a test is the last instruction of the region before it.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "null_written_in_an_arm_read_by_a_condition_98_3490.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 3490, strict=False), verbose=False, raw=False)


def test_the_condition_reads_the_register():
    out = _render()

    assert 'if (r6 === null || r6.name === "replacement") {' in out
    assert "null === null" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
