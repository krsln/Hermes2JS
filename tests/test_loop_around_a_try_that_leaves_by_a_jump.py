"""The body of `while (true) { try { ... } catch { ... } }` stays inside the loop and leaves it by `break` (96/2139).

The edge from a protected block to the `catch` is implicit, so the natural loop was only the header and the catch's
back edge: the rest of the `try` body was printed behind the loop (an exception in it was not caught) and the arms
that left the body kept `goto`s. `LoopAnalysis.include_protected_blocks` adds the protected blocks to the loop and
`LoopExitBreakRegionPass` turns the ways out into `break` (copying the small shared exit block into each arm).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "loop_around_a_try_that_leaves_by_a_jump_96_2139.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_goto_is_left():
    assert "goto" not in _render()


def test_the_body_is_inside_the_try_inside_the_loop():
    out = _render()
    loop = out.index("while (true)")
    try_at = out.index("try {", loop)
    catch_at = out.index("} catch", try_at)

    assert "break;" in out[try_at:catch_at]
