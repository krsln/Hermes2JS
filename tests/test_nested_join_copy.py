"""
A copy read after a join of three paths must read the register (96/4775 `interpolate`).

    r1 = param1;  if (r1 < min) { ...; r1 = min; if (mode !== "clamp") r1 = param1 }  r6 = r1;

The last definition in address order is the inner `r1 = param1`, so `r6 = r1` printed
`r6 = param1` (and every later `r6` read `param1`), although a clamped `r1 = min`
reaches that read too. A join of two paths still folds into a `?:`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_a_copy_read_after_a_three_path_join_keeps_the_register():
    hasm = (_DATA / "nested_join_copy_96_4775.hasm").read_text(encoding="utf-8")

    out = Decompiler.render(Decompiler.build_context(hasm, 4775, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "r6 = r1;" in out
    assert "r8 = -r6;" in out
    assert "r8 = r6 - param2;" in out
    assert "-param1" not in out
