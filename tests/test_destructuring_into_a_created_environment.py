"""
Array destructuring whose elements go into the slots of an environment made by `createEnvironment()` (98/13030).

The slots (`r4[0]`, `r4[1]`) are those of a `StoreToEnvironment`, plain variables like the members of the function's
own `__environment__`, but the pass only knew the latter, so the open-coded `next()` ladder stayed. The two
registers the elements went through are read afterwards; each is restored from ITS slot (the first element's fetch
register is also the second element's register and must not be restored from the first slot).
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "destructuring_into_a_created_environment_98_13030.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_slots_are_a_pattern_and_each_register_is_restored_from_its_own_slot():
    out = _render()

    assert "[r4[0], r4[1]] = r9;" in out
    assert "r6 = r4[0];" in out
    assert "r7 = r4[1];" in out
    assert "GetIterator" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
