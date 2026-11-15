"""
Two tests that copy their operand into one register fold into `a || b` (F-225, 98/11466).

    r12 = r18; r18 = r13; if (r18) goto BODY;  r18 = r12; if (r18) goto BODY;  <else arm>

The second block is a copy and its branch. A copy is not folded in general (the exits may read the register through
another register's inlined value), but here the test before it reads the same register, so the copy exists to be
tested; it took `_fold_pure_setup` out of the pair and left `if (r18) goto L` in the `else` arm of a `for...of` body.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_two_tests_of_one_register_are_one_condition():
    hasm = (_DATA / "dead_mov_raw_branch_98_11466.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 11466, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "r12 = r18;\n        r18 = r13;\n        if (r18 || r12) {" in code
