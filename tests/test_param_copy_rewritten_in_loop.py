"""A register that holds a parameter on entry to a loop that rewrites it reads as the register inside the loop.

`r2 = param1; do { r4.push(r2); r2 = getParent(r2) } while (r2)`: the push and the call read `r2`, which is
`param1` on the first turn only. `resolve_get_by_argument`, `resolve_call_argument` and
`resolve_condition_argument` inlined the parameter's name without the loop check `get_register_reference` has
(96/1822 `traverseTwoPhase$1`, 96/2158 `captureCommitPhaseError`: `r11 = param2.tag` for `r10.tag`).
"""

import re
from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_loop_reads_the_register_not_the_parameter():
    hasm = (_DATA / "param_copy_rewritten_in_loop_96_1822.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 1822, strict=False), verbose=False, raw=False)

    assert "r3 = r4.push(r2);" in out
    assert re.search(r"r2 = .*\(undefined, r2\);", out)
    assert "(param1);" not in out.split("do {")[1].split("} while")[0]
    assert "r4.push(param1)" not in out
