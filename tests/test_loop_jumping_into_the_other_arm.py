"""
A jump from one arm of an `if` onto the first block of the other arm prints as a labeled block (F-314, 98/2775).

    if (null === task) { A } else { loop { ... if (null === task) goto A; ... } }

The loop in the `else` arm leaves into the code of the `then` arm. No sibling follows the jump, so the last resort
of the retry ladder wraps the two arms (`label_A_end: { label_A: { if (!c) { else arm; break label_A_end; } } A }`)
and the jumps become `break label_A;`. Without it the function printed five raw `goto`s.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "loop_jumping_into_the_other_arm_98_2775.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 2775, strict=False), verbose=False, raw=False)


def test_the_jumps_into_the_other_arm_become_labeled_breaks():
    out = _render()

    assert "goto label_" not in out
    assert "label_433_end: {" in out
    assert out.count("break label_433;") == 3


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_labeled_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
