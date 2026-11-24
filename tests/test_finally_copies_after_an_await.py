"""
`try { return await x; } finally { cleanup }` in an async function prints without the resume placeholders (F-312,
96/14945).

Two things were left behind: (1) the entry resume's guard came as `if (!__resumeIsReturn) { body } else { return r0 }`
(the structurer made the larger arm the `then`), the state-machine pass only knew the pad as the `then` arm, so
`r0 = await yield;` stayed on top; (2) behind the `try` the guard of the second suspend has two arms that both run
the copy of the `finally` body and `return r1;`, so the placeholder `r1 = await yield;` stayed in the `try`. The arms
are the same code, so one copy stays behind the `try`.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "finally_copies_after_an_await_96_14945.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_resume_placeholder_or_guard_is_left():
    out = _render()

    assert "await yield" not in out
    assert "__resumeIsReturn" not in out
    assert out.count("return r1;") == 2  # the `finally` body ends in an `if`, each of its arms returns


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
