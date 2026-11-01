"""
F-10 (non-return targets): `if (c) continue;` compiled as a branch to a second, empty back edge.

    96/8548  `cloneObjectProperties`: `if (k === "__initData") { v = o.__initData; if (v !== undefined) continue; }`
             then the body. The branch targets an empty latch block, not the loop header, and the
             else arm of the first test also falls into the body.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_a_branch_to_an_empty_latch_is_a_continue_and_the_body_still_follows():
    hasm = (_DATA / "conditional_continue_empty_latch_96_8548.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 8548, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert 'if (r13 === "__initData") {' in out
    assert "continue;" in out
    # the body runs after the guard, not inside an else arm that drops it
    assert out.index("continue;") < out.index("r15[r14] = r13;")
    assert "} else {" not in out
