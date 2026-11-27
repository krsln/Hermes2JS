"""
A `console.log` read that is passed on keeps its register (98/6517 `log`).

`r3 = console.log` is read later by `apply(r3, ...)` (a spread call through `arraySpread`/`apply`). The printer left the
`rN =` off every unused statement that starts with `console.log`, a rule meant for a discarded call, so the line
printed as a bare `console.log;` and `r3` was read without ever being set.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "console_log_read_passed_on_98_6517.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 6517, strict=False), verbose=False, raw=False)


def test_the_read_keeps_its_register():
    out = _render()

    assert "r3 = console.log;" in out
    assert "r9 = r3;" in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
