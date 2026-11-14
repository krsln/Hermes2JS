"""An `||` of two tests whose second jumps away, with a constant the join reads set in between (96/474).

`typeof D === "function" || typeof D === "object"` guards a block that sets `r2 = false` itself and runs a `try`;
the second test block also loads `r2 = false` for the join (`if (r2)` after both paths). The crossed fold of
`ShortCircuitConditionCfgPass` moves such a constant onto the edge into the join, but refused a function with an
exception handler or a join with other ways in; both only matter when the test, the join or the arm lie inside a
protected range. The printed `if (c) goto label;` jumped to the very code below it.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name, index):
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)


def test_the_two_tests_become_one_condition_with_an_else():
    out = _render("or_chain_shared_target_96_474.hasm", 474)

    assert "goto label" not in out
    assert 'if ("function" !== r2 && "object" !== typeof r4) {\n        r2 = false;\n    } else {' in out
