"""A source expression that occurs twice does not double its head in a chain (F-151).

`a || b` appearing in two statements folds twice, and the second fold's structural match found the first
fold's right operand and wrapped it again: `x = a || (a || b)`. For an operand without effects the repeat adds
nothing, so a repoint that builds `A op (A op B)` leaves `A op B`.

    98/2487   `recordTouchMove`: `previousTimeStamp = t || (t || (t || u))`
    98/12615  `close`: `!this._closeRequested && (!this._closeRequested && ...)`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_repeated_or_head_is_dropped():
    out = _render("doubled_operand_98_2487.hasm", 2487)

    assert "param1.timeStamp || param1.timestamp" in out
    assert "param1.timeStamp || (param1.timeStamp" not in out


def test_a_repeated_and_head_is_dropped():
    out = _render("doubled_operand_98_12615.hasm", 12615)

    assert '!this._closeRequested && "readable" === r4._state' in out
    assert "(!this._closeRequested &&" not in out
