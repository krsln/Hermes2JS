"""
`if (a === undefined) goto T; r0 = null; if (a === null) goto T;` where T is `return r0`
(98/7358 `collectSpans`).

The `null` test is followed by an unrelated comparison (`length === 0`) that jumps to the same
kind of exit. That one used to count as a second `case` body, so the shared target was left to
`SwitchStructurer` and the jump was dropped: `null` fell off the end and returned `undefined`
instead of `null`. Only tests on the SAME value make a `case` chain.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_a_null_argument_still_returns_null():
    out = _render("null_test_after_undefined_test_98_7358.hasm", 7358)

    assert "goto" not in out
    assert out.count("return null;") >= 2
    assert "case null:\n            return null;" in out or "param1 === null" in out
