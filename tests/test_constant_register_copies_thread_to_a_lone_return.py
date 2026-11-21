"""`r0 = r4; if (c) goto J` with `J: if (r0) return r0` kept two `goto`s (98/5730 `sortRoutes`).

`ConstantEdgeThreadingCfgPass` (F-289) only threaded a literal load; here the edge carries a COPY of a register that
holds one constant for the whole function (`r4 = 1` before the loop), and the side `J` decides is a lone `return r0`.
The constant is looked up through its single definition, and the edge gets a return block of its own that returns it.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_edge_returns_the_constant_without_a_goto():
    hasm = (_DATA / "ternary_values_through_a_constant_register_98_5730.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out
    assert "return r0;" in out  # the join that still computes the value
    assert out.count("return 1;") >= 3
    assert "return r1;" in out
