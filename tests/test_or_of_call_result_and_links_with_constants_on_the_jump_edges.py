"""`(f1(x) && a(x) > 0) || (f2(x) && b(x) > 0) || h(x) > 0` as a condition kept `r0 = true; if (c) goto J;` (96/155 `Pe`).

The bytecode loads `true` into the join's register before each `&&` link's jump and `J` tests that register
(`if (!r0)`), while the last link sets it to its own comparison. The constant edge goes straight to the decided side of
`J` (`ConstantEdgeThreadingCfgPass`) and the three links fold into one `||` condition, calls in evaluation order.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_three_links_are_one_condition():
    hasm = (_DATA / "call_result_and_chain_with_constant_edges_96_155.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 155, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out
    assert out.count("||") == 2
    assert "[115].call(undefined, param1) > 0)" in out
