"""
A `break` out of a `for-of` whose arm is several blocks long stays inside the loop (98/11038 `getStateForAction`).

`for (r14 of routes) { if (key === key) { <several blocks, an if/else inside>; break; } ... }`: Hermes lays the arm out
behind the loop and ends it with a jump to the loop's own merge. Only a one-block arm was moved into the loop; a longer
one stayed behind it, where the loop's normal end (the iterator is done) ran it too - the printed code did the work of
the arm for a list without a match. The arm now becomes the `if` body and each end that rejoins the merge a `break`.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "for_of_break_with_a_several_block_body_98_11038.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_arm_is_the_if_body_and_ends_in_a_break():
    out = _render()
    lines = [line.strip() for line in out.splitlines()]

    start = next(i for i, line in enumerate(lines) if line.startswith("for (let r14 of r10)"))
    body = lines[start:start + 30]

    assert "if (r16 === r14) {" in body
    assert "break;" in body
    assert body.index("break;") > body.index("if (r16 === r14) {")
    assert "GetIterator" not in out
    assert "label_1810" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
