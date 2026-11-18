"""A crossed `||` whose second test's setup is overwritten by a dead copy stays one condition (F-275).

`if (typeof c.diff === "function" || typeof c.process === "function") { body }` compiles to a second test block
`r19 = c.process; r22 = typeof r19; r19 = r20` (the last write is a loop-carried copy nobody reads) that jumps to END
and falls into the shared body; the exits read `r19`, which the block overwrites, so the fold refused the setup and the
second test stayed a `goto` (96/2339 `restoreDeletedValuesInNestedArray`).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_second_typeof_test_joins_the_first_with_or():
    hasm = (_DATA / "crossed_or_with_overwritten_setup_96_2339.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2339, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert '|| "function" === typeof r18.process' in out
