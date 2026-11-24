"""
`return await x;` inside a `try` of an async function prints without the second suspend (F-312, 96/12653).

The function suspends twice: once for `await r4.json()` and once more before it leaves the `try` with the value. The
second pair left the resume placeholder (`r3 = await yield;`, not valid JavaScript) in the `try` and an `if
(__resumeIsReturn) { return r3; } else { return r3; }` behind it. Both arms return the same register, so the guard
decides nothing: the placeholder, the flag and the guard go and `return r3;` stands behind the `try`.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "return_await_inside_a_try_96_12653.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_second_suspend_and_its_guard_are_gone():
    out = _render()

    assert "await yield" not in out
    assert "__resumeIsReturn" not in out
    assert "r3 = await r4.json();\n        } catch (caughtException) {" in out
    assert "        }\n        return r3;\n    } else {" in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    # `getEnvironment`-style helper names are plain identifiers, the file only has to parse
    assert done.returncode == 0, done.stderr
