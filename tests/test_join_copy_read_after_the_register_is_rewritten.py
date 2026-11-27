"""
A copy of a join value is read by the copy's own register once the join register holds something else (96/5569 `render`).

`r7` holds the header flag (0 or 1, a join), `Mov r11, r7` copies it, then `IteratorBegin r7, ...` reuses `r7` for the
iterator. The repair that names the join register for its readers also repointed the later `Mov r13, r11` to `r7`, so
the loop read the iterator, and the `GetIterator` line stayed because `r7` was still read by name. The copy now reads
`r11`, which prints as `r11 = r7`.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "join_copy_read_after_the_register_is_rewritten_96_5569.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 5569, strict=False), verbose=False, raw=False)


def test_the_copy_is_read_by_its_own_register():
    out = _render()

    assert "r11 = r7;" in out
    assert "r13 = r11;" in out
    assert "r13 = r7;" not in out
    assert "GetIterator" not in out
    assert "for (let r13 of r10)" in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
