"""A bottom-tested loop's header branch is an ordinary `if` in the body (F-172).

`labeledBreakTest` (`do { if (r5 === 1 && j === 1) { log; break outer } log } while (...)`) had its header's test
treated as a loop test, so the `&&` was never folded and the output lost the `log` of the `r5 === 1 && j !== 1`
path. A header that branches only inside the loop, of a loop whose latch carries the test, is folded like any
other in-body test, and a crossed fold may end on a latch.

    96/15065  labeledBreakTest
    98/9456   labeledBreakTest
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def _check(out: str, outer: str):
    assert "goto" not in out
    assert f"if ({outer} === 1 && j === 1) {{" in out
    assert "break loop_1;" in out
    # the log after the test runs on every path that did not break
    assert out.index("break loop_1;") < out.index(f"console.log({outer}, j);")


def test_labeled_break_96():
    _check(_render("loop_header_ordinary_if_96_15065.hasm", 15065), "r5")


def test_labeled_break_98():
    _check(_render("loop_header_ordinary_if_98_9456.hasm", 9456), "i")
