"""A copy of a shared tail never reads a register only the OTHER path sets (F-247, 96/43 `formatValue`).

    r6 = !param2.name ? "" : r15;        // r15 is written by the unrelated `[Function` path only

Retry rungs copy a tail; the copy's instructions are new, so `UnfoldedMergeRepairPass` could not tell they lie
behind a different write and handed them the register of the first path's `": " + name`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_copy_keeps_its_own_value():
    hasm = (_DATA / "tail_copy_register_leak_96_43.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 43, strict=False), verbose=False, raw=False)

    assert '"" : r15' not in out
    assert 'r6 = "[Function" + (!param2.name ? "" : ": " + param2.name) + "]";' in out
