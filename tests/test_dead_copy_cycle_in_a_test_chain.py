"""A loop-carried cycle of copies does not keep `&&` from folding, and the folded `if` keeps its tail (96/12510).

`r11 = r3` (setup of the second test) only feeds `r6 = r11` -> `r3 = r6` -> `r11 = r3`, a cycle nothing
reads before it is written again, so `if (A) { if (B) { call; if (r11) return } }` is one test. Once it is one
test the arm's guard `if (r11) return r2` is already a loop exit, and the arm still runs on into the code after the
`if` (the `r7 = r5 + 1` step); before the structurer knew that, the tail landed in an `else`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name, index):
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_tests_fold_and_the_tail_follows_the_if():
    code = _render("dead_copy_cycle_and_loop_guard_96_12510.hasm", 12510)

    assert "goto" not in code
    assert "if (r12.notFound && r10.notFound) {" in code
    assert "} else {\n                                r2 =" not in code
    assert "r7 = r5 + 1;" in code


def test_an_arm_with_a_stripped_guard_runs_into_the_target():
    code = _render("arm_with_stripped_guard_runs_into_target_96_2148.hasm", 2148)

    # the target is reached by `param2` and by a null sibling: it follows the `if`
    assert "if (!param2) {" in code
    assert "} else {" not in code.split("if (!param2) {")[1].split("} while")[0]
    assert code.index("r2[143] = r9;") > code.index("if (!param2) {")
