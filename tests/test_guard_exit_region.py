"""
F-10 (non-return targets): `if (a) { ...; if (c) return x; } TAIL`, with the exit laid out after TAIL.

    98/3552  `canParse`: when a base is given it is parsed first and `null == base` returns false;
             both paths then run the same code that parses the url. The exit block lies after that
             shared code, so the guard stayed `if (null == r5) goto label` and the tail was
             duplicated into an else arm that dropped the fall-through.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_a_guard_whose_exit_follows_the_shared_tail_returns_inside_the_if():
    hasm = (_DATA / "guard_exit_after_tail_98_3552.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 3552, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (null == r5) {\n            return false;\n        }" in out
    # the url is parsed once, after the guard, for both paths
    assert out.count("r3[22](") == 2
    assert "} else {" not in out


def test_a_loops_exit_to_a_shared_return_is_not_absorbed_into_a_guarded_body():
    """98/8982 `checkEqual`: `do { r9 = it.next(); if (r9 === undefined) goto RETURN_TRUE; ...} while (r4)`.
    The residual branch was folded into `if (r9 !== undefined) { body }`, which dropped the exit:
    `return true` ended up after the loop where the walk never reaches it. The first attempt only
    looked fine because another goto in the function forced a retry that hid it."""
    hasm = (_DATA / "loop_exit_return_98_8982.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 8982, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (r9 === undefined) {\n                        return true;\n                    }" in out
    assert "if (r9 !== undefined)" not in out


def test_a_loop_break_to_a_function_ending_region_runs_that_region_inside_the_if():
    """96/2026 `refreshCache`: `for (n = fiber.return; n !== null; n = n.return) { if (tag === 24 || tag === 3) { ...; return } }`.

    The two tests jump out of the loop to the same code, which was printed after the loop's own
    `return undefined` (dead): a fiber with tag 24 never ran it, and tag 3 only by accident.
    The tests are one `||` condition and the code that follows ends the function, so it sits in the `if`.
    The loop counter register is reused for `getEnvironment(0)` inside it: it must keep its `rN` name.
    """
    hasm = (_DATA / "loop_two_exits_found_region_96_2026.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2026, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (24 === r4 || 3 === r4) {\n            r3 = getEnvironment(0);" in out
    assert "r3[458].call(undefined, r6)" in out
    assert "i[458]" not in out
    assert out.index("r2.payload = r1;") < out.index("return undefined;")
