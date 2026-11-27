"""
A destructuring pattern in a function with no exception handler table leaves no dead cleanup code behind (98/11141).

`[, r2] = param1` compiles to the open-coded iterator chain plus a `Catch; IteratorClose it, 1; Throw` block at the
end. The function has no handler entry, so the block has no predecessor and no handler: nothing removed it with the
pattern, and it printed after the `return` (`r1.return(); throw caughtException;`).
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "destructuring_with_a_dead_cleanup_catch_98_11141.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 11141, strict=False), verbose=False, raw=False)


def test_the_cleanup_block_is_gone():
    out = _render()

    assert "[, r2] = param1;" in out
    assert "return r2 != null;" in out
    assert ".return()" not in out
    assert "caughtException" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
