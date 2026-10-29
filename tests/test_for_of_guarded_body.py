"""A `for-of` whose try covers only the loop body (F-166).

    while (!done) { r = it.next(); try { body } finally { it.return() } }

Two things kept it a `while`/`try` pile, or a `goto`:

  * `LoopBreakStructurer` found the loop's merge only through the latches. A top-tested loop's latch just
    jumps back, so `if (c) { r0 = x; it.return(); break; }` stayed outside the loop behind `goto label_67`.
    The header's own exit now counts when the header is the guard.
  * `ForEachRegionPass._try_recognize_for_of_with_inner_try` refused a `finally`, which is how the close
    scaffold looks once a `break`/`return` copied it. It only needs to be the iterator close.

    96/10789  `checkIfScreenWasChanged`
    96/13412  `findInMenu`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_break_out_of_a_guarded_body_stays_in_the_for_of():
    out = _render("for_of_break_in_guarded_try_96_10789.hasm", 10789)

    assert "goto" not in out
    assert "for (const r8 of r5) {" in out
    assert "r0 = r8;\n            break;" in out
    assert "finally" not in out and "while" not in out


def test_a_return_in_a_guarded_body_leaves_no_finally_close():
    out = _render("for_of_return_in_guarded_try_96_13412.hasm", 13412)

    assert "for (const r9 of r6) {" in out
    assert "finally" not in out and "GetIterator" not in out and ".return()" not in out
