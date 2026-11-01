"""A test the arm repeats on a recomputed value is not a `case` label (F-181).

    if (0 !== r6) goto T;                 // T: the code after the `if`
    if (a) { ...; r6 = f(); if (0 === r6) return x; }  falls into T
    T: ...

The branch compares a value with a constant, which `_DominanceIfBuilder` left to the `switch` builders: the
arm's own test of the SAME constant, reached by falling into `T`, never made `T` the join. `T` was printed in
the `if (0 !== r6) {..}` arm only, so the path of the second test that runs `T` returned `null` instead
(`goto label_269`, a `return` printed nowhere).

    98/2618  `bailoutOnAlreadyFinishedWork`
    96/141   `fe`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_rest_follows_the_if_of_the_retested_value():
    out = _render("retested_constant_98_2618.hasm", 2618)

    assert "goto" not in out
    assert "if (0 === r6) {\n                return null;\n            }" in out
    # the code both tests reach is printed once, after the outer `if`
    assert out.count("Resuming work not yet implemented.") == 1
    assert out.index("if (0 === r6) {") < out.index("Resuming work not yet implemented.")
    assert "if (0 !== r6)" not in out


def test_a_second_function_of_the_shape_has_no_goto():
    out = _render("retested_constant_96_141.hasm", 141)

    assert "goto" not in out
