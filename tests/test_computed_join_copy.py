"""
A computed value written on ONE arm must not be inlined into a copy read on another (F-138, 96/1801
`getComponentNameFromType`).

`r3` is last written (in address order) by the `ForwardRef(...)` arm, and every other arm ends in
`Mov r1, r3` reading `param1`. The join guard in `get_register_expression` only covered a bare register
alias, so the arm's string concatenation was inlined into each of them
(`r1 = r2 + (r2.displayName || r1.name || "") + ")"`). A join of three or more paths now keeps the
register for a binary expression too.

Not fixed (still open under F-138):
- inside the `ForwardRef` arm itself, `BooleanChainRegionPass` copies `r2.displayName || r1.name || ""`
  into a test that stands after `r1`/`r2` were redefined, so two such lines remain;
- the last `Mov r1, r3; Ret r1` of that arm is a join of two paths, which the guard deliberately leaves
  to the ternary fold (widening it to two paths broke 17 other tests).

Other value shapes keep inlining on purpose: a constant or an environment value would leave a read of a
register that prints nowhere (`reject.call(r0, ...)`, 96/2999), and a member read is left to the ternary
fold (`tests/test_default_parameter_merge.py`).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"

_GARBAGE = 'r2 + (r2.displayName || r1.name || "") + ")"'


def _code() -> str:
    hasm = (_DATA / "computed_join_copy_96_1801.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 1801, strict=False), verbose=False, raw=False)


def test_a_copy_on_another_arm_reads_the_register_not_the_forward_ref_string():
    code = _code()

    # Seven arms read it before the fix; only the two inside the `ForwardRef` arm are left.
    assert code.count(_GARBAGE) <= 2
    assert code.count("r1 = r3;") >= 4
