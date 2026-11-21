"""An `if/else` inside a loop whose arms leave the loop with `if (c) break;` kept its `goto`s (98/10170
`useAnimatedPropsMemo`).

`LoopBreakStructurer` replaces an exit branch by a block holding a `break`; that block keeps the address of the
branch's block, so `_DominanceIfBuilder._convert` took it for an item of neither arm, ended the arms there and bailed
with an empty `else`: `if (r17 === "style") goto label_259`, `goto label_251`, `goto label_274`. The block now follows
the item before it, as an address-less one does.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_arms_that_break_out_of_the_loop_still_form_an_if_else():
    hasm = (_DATA / "loop_breaks_in_if_arms_98_10170.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 10170, strict=False), verbose=False, raw=False)

    assert "goto label" not in out
    assert 'if (r17 === "style") {' in out
    assert out.count("break;") == 4
    assert "continue;" not in out
