"""An entry `rN = undefined;` is dead when the only reads of `rN` that nothing writes before are in later `if` conditions.

`DeadUndefinedStorePass` treated every register read by an expression living on a region object as live
everywhere, so `r1 = undefined;` at the top of 96/9291 `parseRange` survived although `r1 = new Map()` runs
before the only reads (`if (r5 > 1 && r1.has(""))`). An `if` condition is evaluated at the end of the block whose
branch the region replaced, so its registers are reads there.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_entry_undefined_before_an_if_condition_read_is_dropped():
    hasm = (_DATA / "entry_undefined_read_only_in_if_condition_96_9291.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 9291, strict=False), verbose=False, raw=False)

    assert "r1 = new Map();" in out
    assert 'r1.has("")' in out
    assert "r1 = undefined;" not in out
