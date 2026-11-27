"""
A copy of a parameter that the loop rewrites is read as the register, not as the parameter (98/8694 `saveSnapshot`).

`Mov r2, r1` (the parameter) before the loop, `r2 = r6.parentElement` at the bottom of the body, `Mov r6, r2` and
`r2.scrollTop` at the top. The copy kept the parameter's name for every read, so each iteration read `param1` again
and the loop never advanced (`r6 = param1`, 98/9777 `reconcileChildFibersImpl`: `r21 = param2`).
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "parameter_copy_rewritten_by_the_loop_98_8694.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_loop_reads_the_register():
    out = _render()

    assert "r2 = param1;" in out
    assert "r7 = r2.scrollTop;" in out
    assert "r6 = r2;" in out
    assert "r6 = param1;" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
