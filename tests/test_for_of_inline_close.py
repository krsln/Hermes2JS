"""The iterator close Hermes copies onto a for-of's exits is dropped (F-167).

`for (x of xs)` already closes the iterator on `break` and `return`, so

    r2.return(); break;           r1.return(); return true;

only repeat what the loop says. Left behind they also kept the `GetIterator` setup alive.

    96/13887  `matchAgainstConfigs`  (break)
    96/10836  `inlinePropsHasChanged`  (return)
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_close_before_a_break_is_dropped():
    out = _render("for_of_inline_close_break_96_13887.hasm", 13887)

    assert "for (const r10 of r5) {" in out
    assert ".return()" not in out and "GetIterator" not in out
    assert "if (r9 === 1) {\n                break;" in out


def test_a_close_before_a_return_is_dropped():
    out = _render("for_of_inline_close_return_96_10836.hasm", 10836)

    assert "for (const r7 of r2) {" in out
    assert ".return()" not in out and "GetIterator" not in out
    assert "if (r6 !== r5) {\n                return true;" in out
