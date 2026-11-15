"""Several ways out of one loop onto the same block are all `break`s (F-245, 98/2609 `updateSimpleMemoComponent`).

An inlined `shallowEqual` leaves its `do { ... } while (i < keys.length)` from two tests (`!hasOwnProperty`,
`!Object.is`) onto the code after the loop, where the loop's own completion lands as well. Each exit saw the other as
"some other way onto the block" and none was converted: one stayed a raw `goto`, the other became an
`if (c) { rest of the body }` whose else path fell into the loop test (the loop ran on after a failed test).

Only on the last retry rung (`cfg.sibling_loop_exits`): the same rule on the first attempt structured
98/10170 worse.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_both_exits_are_breaks_and_nothing_else_is_left():
    hasm = (_DATA / "loop_sibling_exits_98_2609.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2609, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (!r20) {\n                                            break;" in out
    assert "if (!r18) {\n                                            break;" in out
    assert "} while (r1 < r15.length);" in out
