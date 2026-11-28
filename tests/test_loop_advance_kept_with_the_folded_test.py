"""The loop advance is printed when the loop test folded into the condition (98/8694 `saveSnapshot`).

`r2 = r6.parentElement` at the bottom of the body feeds `Mov r6, r2` at the top. The condition reads the member again
(`while (r6.parentElement)`), the copy was inlined into it and the assignment vanished, so the loop never advanced.
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


def test_the_advance_is_printed_before_the_condition():
    out = _render()

    assert "r2 = r6.parentElement;" in out
    assert out.index("r2 = r6.parentElement;") < out.index("} while (r6.parentElement)")


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0
