"""A branch test reads the register that merges `null` with other values (98/2151 `normalizeColor`, 98/2671).

`switch (name) { case ...: r7 = 0xff0000ff; ... default: r7 = null }` and then `if (r7 != null)`: the test inlined the
`null` of the last write (`null != null`), so the whole `if` was constant.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "null_merge_in_a_branch_test_98_2151.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_test_reads_the_register():
    out = _render()

    assert "if (r7 != null) {" in out
    assert "null != null" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0
