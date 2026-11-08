"""A shared tail inside a `try` range is copied for the test that skips it, when its ways in are inside too (F-195).

    try { ...; if (A) goto T; r = f(x); if (!r) goto END; T: push(x); END: }        (a for-of body)

F-193 let the copy pass work in functions with a handler when nothing it touches is protected. A for-of's whole
body is the protected range, so every tail in it was left alone (`goto label_128` in 98/1738 `getChildNodes`, the
filter result decided whether `push` ran and the output ran it on both paths). The copy sits right in front of the
tail, inside the same range, so a tail and every way into it under the SAME handlers are copied; a tail something
outside the range jumps to, or a handler's entry, is not.

The copy is the block the test FALLS into, so `LoopStructurer` lays it out right behind that test (`follows`);
by id it came last in the loop body, after the latch.

    98/1738 `getChildNodes`   98/8837 `getInlineStyle`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_filter_result_decides_the_push():
    out = _render("shared_tail_inside_try_98_1738.hasm", 1738)

    assert "goto" not in out
    # the tests now fold into one condition (F-216), so nothing needs the tail twice
    assert "if (r8 != null && (param2 == null || param2(r6))) {" in out
    assert out.count("r0.push(") == 1


def test_the_transform_check_that_fails_keeps_the_plain_assignment():
    out = _render("shared_tail_inside_try_98_8837.hasm", 8837)

    assert "goto" not in out
    assert out.count("r3[r11] = r10;") == 1
    # the copy of the first test's operand folds into the condition (F-225)
    assert 'if (!r10 && (r9 !== "transform" || !r0[5].call(0, r8))) {' in out
