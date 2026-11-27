"""
A `CreateThisForNew` placeholder and its copy in a block that throws print nothing (98/3382 `normalizeRootMargin`).

`new SyntaxError(r13)` folds the construction, but the compiler had allocated the `this` object in `r8` and copied it
to `r14` right before the throw. `DeadThisPlaceholderPass` only dropped a placeholder whose register is mentioned
nowhere else in the function, and `r8` is reused, so the line printed as `r8 = CreateThisForNew(r9)` reading `r9`,
which the folded `new` had already consumed.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "this_placeholder_copied_before_a_throw_98_3382.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 3382, strict=False), verbose=False, raw=False)


def test_the_placeholder_and_its_copy_are_gone():
    out = _render()

    assert "throw new SyntaxError(r13);" in out
    assert "CreateThisForNew(r9)" not in out
    assert "r14 = r8;" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
