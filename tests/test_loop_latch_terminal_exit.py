"""
A bottom-tested loop whose way out ends in a `return`/`throw` of its own, with another exit elsewhere (F-149).

    do {                                    // 96/11086 `useHandler`
        r4 = it.next();
        if (r4 === undefined) break;        // -> the code after the throw
        ...
    } while (isWorklet(...));
    throw new ReanimatedError(...);         // the latch's exit

`LoopConditionRegionPass` made the latch the loop's `while (c)` and left the `throw` behind the loop, so
the bare `break` on `undefined` ran the `throw` too: every function that found only worklets threw.
The latch's exit is now moved into the loop (`if (!c) { throw }`, Shape B) and the loop keeps its one
real way out, the `break`. A bare `break` also needs the loop's own completion to reach the same block.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _code(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_a_throw_behind_the_loop_moves_into_it_and_the_loop_is_a_for_in():
    code = _code("loop_latch_throw_exit_96_11086.hasm", 11086)

    assert "for (const r4 in r10) {" in code
    assert "if (!r2) {" in code
    assert code.index("throw new r8(") < code.index("r4 = r2.buildDependencies")
    assert "HermesPropertyIterator" not in code
    assert "do {" not in code
    assert "goto" not in code


def test_the_code_after_the_loop_is_reached_by_the_break_only():
    """98/9880 `finish`: the search loop `break`s on a match; running out returns `undefined`."""
    code = _code("loop_latch_return_exit_98_9880.hasm", 9880)

    assert "goto" not in code
    assert "break;" in code
    assert code.count("return undefined;") == 2
