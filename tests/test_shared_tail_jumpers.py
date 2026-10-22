"""
F-127: a jump into the other arm of an enclosing `if` must stay.

    96/273 `q`: `if (state !== "writable" || isX(...)) n(); else schedule(n)`. Both tests
    jump to the `n()` block and nothing falls into it. The second test's jump used to be
    folded away (`if (!isX) { schedule }`), so `n()` never ran for it.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_both_tests_that_jump_to_the_tail_reach_it():
    out = _render("or_condition_calls_shared_tail_96_273.hasm", 273)

    assert "goto" not in out
    # `n()` runs when the state is not writable AND when the second test holds
    assert out.count("r0 = n();") == 1
    assert 'if ("writable" === r3)' in out
    assert "if (!r2) {" in out
    assert out.index("r0 = r2(r0, n);") < out.index("r0 = n();")
