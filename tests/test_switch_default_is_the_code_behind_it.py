"""
A jump table whose default target is the code BEHIND the switch builds a `switch` followed by that code (F-321,
98/2672 `unwindUnitOfWork`).

    do { switch (fiber.tag) { case 24: ...; break; ... case 19: ... } <test of the completed work> ... } while (r6)

Every arm jumps to that code and so does the default. Its test (`if (completedWork !== null)`) had become an `if`
without a `source_block` (`LoopBreakStructurer` consumes its branch), so the switch did not find it as its default
item, took it for the last case's body and the other arms' jumps into it stayed `goto label_1119`.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "switch_default_is_the_code_behind_it_98_2672.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 2672, strict=False), verbose=False, raw=False)


def test_the_code_behind_the_switch_follows_it():
    out = _render()

    assert "goto label_" not in out
    assert "\n        }\n        if (null !== r10) {\n" in out
    assert "case 19:" not in out.split("if (null !== r10) {")[1]


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
