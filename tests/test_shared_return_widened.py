"""
F-10: an `if (c) goto sonReturn` is gone when the shared exit can be copied
without changing what it returns.

    96/10518  `r1[param1] = r0` jumps to the function's closing `return` while
              the other arm falls into it: the closing `return` is copied for
              the jumper instead of leaving `goto label_91`.
    96/11046  the closing `return r0` follows `r0 = true` on one path and
              `r0 = false` on another. One copy per jumper would be exact, but
              the final one then reads as a single value: the output returned
              `false` for equal lists. It must stay as it was (a visible goto),
              never silently wrong.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_closing_return_is_copied_for_a_jump_into_it():
    out = _render("shared_return_throw_exit_96_10518.hasm", 10518)

    assert "goto" not in out
    assert out.count("return undefined;") == 3


def test_a_return_whose_register_has_different_values_per_path_is_not_copied():
    out = _render("shared_return_phi_96_11046.hasm", 11046)

    # Either still a visible goto, or - if a later pass structures it exactly -
    # both constants must survive.
    assert "goto" in out or ("return true" in out and "return false" in out)


def test_a_two_block_tail_with_an_inner_test_is_copied_for_the_test_that_skips_it():
    """98/1871 `get`: `f != null ? f(p) : null` then `?? (m[p] != null ? m[p] : null)`.
    The second operand is a tail of two blocks (it holds its own test) that one
    test jumps onto and another falls into."""
    out = _render("shared_tail_region_98_1871.hasm", 1871)

    assert "goto" not in out
    assert out.count("r3 = r3[1][param1];") == 2
    assert out.count("r2 = null;") == 2


def test_a_copy_written_in_one_arm_is_not_taken_for_the_whole_merge():
    """96/4846 `binarySubdivide`: `r14 = r0; if (c) { r15 = r0; r14 = param3 }`,
    read after the `if` as `r10 = r14`. The arm's write (a copy of `param3`
    that `Mov r13, r10` also holds) was folded into the reader, which printed
    `r10 = param3` on the path that skips the arm too."""
    out = _render("loop_carried_arm_copy_96_4846.hasm", 4846)

    assert "r14 = param3;" in out
    assert "r10 = r14;" in out
    assert "r10 = param3;" not in out
