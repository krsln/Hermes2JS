"""A `null` written by a `catch` handler does not replace the try body's value after the `try` (96/6880, 96/6826).

`try { r1 = requireNativeModule("ExpoGo") } catch { r1 = null }; env[0] = r1`: the store behind the `try` printed
`env[0] = null`, so the module was thrown away on the path that did not throw.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "null_written_by_a_catch_handler_96_6880.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_store_reads_the_register():
    out = _render()

    assert "r2[0] = r1;" in out
    assert "r2[0] = null;" not in out


def test_the_handler_still_assigns_null():
    assert "} catch (caughtException) {\n        r1 = null;\n    }" in _render()


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0
