"""
A `yield` inside a `try` whose `finally` is copied onto the return and the throw paths prints as a `yield`, with the
right value in each copy (F-312, 96/8059).

`Save/Ret` then `ResumeGenerator` and `JmpTrue <isReturn>`: the guard's return arm is not just a `Ret`, it runs the
copy of the cleanup first, so the state-machine pass did not fold the pair and `await yield` was left behind (invalid
JavaScript). The test of the flag stays, the yield folds.

Two reads were wrong behind that:
- `Mov r2, r1` (the resumed value) sits in the arm the jump falls into, which ends in a `Ret`; the arm the jump goes
  to (and the `catch`) read `r2` as it was before, `undefined`, not the resumed value;
- the `Mov r6, r2` copy of that `undefined` shared the literal node of `r4 = undefined`, so the merge repair followed
  it by identity and made `return undefined` read `r6`.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "yield_in_try_with_finally_copy_96_8059.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_yield_is_folded():
    out = _render()

    assert "await yield" not in out
    assert "r1 = yield r3[0];" in out


def test_each_copy_reads_its_own_value():
    out = _render()

    # the return arm and the catch hold `undefined`; only the arm the jump falls into holds the resumed value
    assert out.count("[true, undefined]") == 2
    assert out.count("[true, r1]") == 1
    assert "return undefined;" in out
    assert "return r6" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
