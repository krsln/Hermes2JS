"""A for-of whose iterator-close handler covers only the body, or none at all (96/5140 `anonymous`).

`IteratorNext; Mov; JStrictEqual it undefined -> exit` heads the loop and the handler range (0x1c-0x24) starts at
the `if` that is the body: the `if`'s test block was no longer a child of any sequence, so
`RegionGraph.lowest_common_sequence` found no common sequence with the handler's block, the `try` was never built
and the loop stayed `while (!(r5 === undefined)) { r4 = r2.next(); r5 = r2; ... }` (the test reads a register the
body sets AFTER the test) with the close handler left as dead `r2.return(); throw caughtException;` behind it.
Without any handler the loop was left the same way: `ForEachRegionPass` only recognized a loop inside a `try`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name):
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 5140, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_handler_over_the_body_only_is_a_for_of():
    code = _render("for_of_inner_try_96_5140.hasm")

    assert "for (let r4 of r3)" in code
    assert "next()" not in code
    assert "caughtException" not in code


def test_for_of_without_a_handler_is_a_for_of():
    code = _render("for_of_no_handler_96_5140.hasm")

    assert "for (let r4 of r3)" in code
    assert "next()" not in code
    assert "undefined" not in code
