"""
A destructuring whose environment creation was moved in front of it (98/5651 `useThenable`).

`const [x] = useState(p)` where `x` lives in the closure environment: Hermes creates the environment in the middle of
the chain (`CreateTopLevelEnvironment r3` between the element and its close check) into the register that also holds
the source (`r3 = r4; ... GetIterator(r3)`). `ArrayDestructuringCfgPass` moves such a creation in front of the
pattern and gave up when the source read the created register, so the first pattern stayed open-coded with its
`if (rIt !== undefined)` guards. The creation now runs after the pattern in that case.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "destructuring_before_a_moved_environment_98_5651.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_all_three_patterns_are_printed():
    out = _render()

    assert "[__environment__[0]] = r3;" in out
    assert "[r2, __environment__[2]] = r9;" in out
    assert "[__environment__[3]] = r5;" in out
    assert "GetIterator" not in out
    assert ".return()" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
