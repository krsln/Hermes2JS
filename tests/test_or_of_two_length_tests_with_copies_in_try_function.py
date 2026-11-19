"""`a === x.length || b === y.length` whose second test re-copies the registers of the first (F-263, 98/2474).

    r9 = r5; r8 = r7.length; if (r9 === r8) goto BODY; r9 = r12; r8 = r11.length; if (r9 !== r8) goto END; BODY:

The `Mov r9 <- r12` copy of the second test is dead once the test is over, on both exits and in the
`finally` handler, but the fold only trusted the copies a loop-free, handler-free function showed to be dead, so the
`||` stayed a `goto label_573`. Folding it changes the layout of the loop behind it, and the break of a loop test whose
block holds only copies (`r8 = r12` ahead of `if (!(0 <= r8)) break;`) shadowed that block's address: the first
test then guarded the copy alone and the break ran on its own, outside it.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "loop_latch_inside_if_98_2474.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 2474, strict=False), verbose=False, raw=False)


def test_the_or_of_the_two_length_tests_is_one_condition():
    out = _render()

    assert "if (r9 === r8 || r12 === r11.length) {" in out
    assert "goto label_573" not in out


def test_the_first_test_of_the_loop_guards_the_whole_body():
    out = _render()

    assert "if (1 <= r8) {\n                                        r8 = r12;\n                                    }\n" not in out
    assert "if (1 <= r8) {\n                                        r8 = r12;\n                                        if (!(0 <= r8)) {" in out
