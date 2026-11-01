"""
An arm that runs on into the branch target leaves the target AFTER the `if` (a retry with copied returns).

    if (c) goto T;  <arm: ...; if (x) return ...; ...>  T: <tail>

The first attempt took `T` for the `else` arm: the arm's own flow into it was dropped, or a `goto` stayed.
With the shared returns copied, the arm's other exits are real `return`s, so `T` follows the `if`.

    96/842    `handleException`: `if (handler) { if (handler(...)) return; }` then the rest.
    96/10211  `isAnimationTerminatingCalculation`: the clamped branch returns `true` out of range and
              otherwise runs on into the spring energy test.
    96/11046  `areDependenciesEqual`: see `test_shared_return_widened.py` (the loop tail).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_code_after_an_early_return_arm_follows_the_if():
    out = _render("arm_runs_into_tail_96_842.hasm", 842)

    assert "goto" not in out
    assert out.count("try {") == 1
    assert out.index("return undefined;") < out.index("try {")


def test_a_clamped_branch_runs_on_into_the_energy_test():
    out = _render("arm_runs_into_tail_96_10211.hasm", 10211)

    assert "goto" not in out
    # both clamp tests leave for the same `return true`: one `||` (F-170), not two copies
    assert out.count("return true;") == 1
    assert "if (r0 < r5 || r0 > r4) {\n            return true;" in out
    assert out.index("return true;") < out.index("r4[0](")


def test_the_first_attempt_keeps_the_code_an_arm_falls_into():
    """96/890 `requireModule`: `if (a == null) goto T; r0 = f(); if (r0 != null) return r0; T: ...`.

    No return copies are needed: the arm's test leaves through a lone `return`, and its fall-through
    is the branch target, which therefore follows the `if` (it was dropped before)."""
    out = _render("arm_runs_into_tail_first_attempt_96_890.hasm", 890)

    assert "goto" not in out
    assert out.index("r1[2].call(") < out.index("r1[1][param1]")
    assert out.count("return r0;") == 1


def test_a_last_test_that_jumps_onto_the_tail_and_falls_into_a_return_leaves_the_tail_after_the_if():
    """96/8976 `processColorInitially`: `if (typeof p === "number") goto T; r = f(p); if (typeof r === "number")
    goto T; return r; T: <number code>; return`. The tail follows the `if` (it stayed a `goto`)."""
    out = _render("arm_tests_into_tail_past_return_96_8976.hasm", 8976)

    assert "goto" not in out
    assert out.count(">>> 0") == 1
    assert out.index("return r1;") < out.index(">>> 0")
