"""A guard that jumps past a `throw` inside an arm built a moment ago (F-182).

    if (r2) { r9 = r2; if (typeof r9 === "function") goto T; throw ... }   T: if (r9) ...

`if (r2)` came out of folding a residual test, and the `typeof` test inside its arm was never folded: it
printed `if (typeof r2 === "function") goto label_200;`. The arm is folded now, but only when

  - the jump's target is the code BEHIND the enclosing arms (`_target_follows_the_region`: not a `return`
    printed elsewhere, 98/2202 `if (isNaN(x)) goto RETURN_UNDEFINED` inside an arm that goes on into a `switch`),
  - the arm ends in a `throw`/`return` (nothing falls out of it), and
  - nothing outside the arm jumps into it (98/2693: code behind a `throw` that other jumps reach),

and never for a `case` test (98/2211: the chain `SwitchStructurer` reads). The fold stops at a target that sits
later in the region (`if (C) goto T; A; T: B` is `if (!C) { A } B`).

    98/2490  `accumulateDirectDispatchesSingle`   98/2202 `_getFilterAmount`
    98/2211  `processTransformOrigin`            98/2693 `findHostInstance`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_type_check_guards_its_throw():
    out = _render("guard_throw_arm_98_2490.hasm", 2490)

    assert "goto" not in out
    assert 'if (typeof r2 !== "function") {\n' in out
    assert out.index('if (typeof r2 !== "function") {') < out.index("throw r2;")


def test_a_return_printed_elsewhere_is_not_where_the_arm_continues():
    out = _render("guard_throw_arm_98_2202.hasm", 2202)

    assert "if (!r5) {\n            return undefined;\n        }" in out
    assert "if (r7) {\n            return undefined;\n        }" in out


def test_a_case_test_keeps_its_chain():
    out = _render("guard_throw_arm_98_2211.hasm", 2211)

    assert '"left" !== r30 &&' not in out
    assert 'case "left":\n                    case "right":' in out


def test_code_other_jumps_reach_stays_behind_the_throw_guard():
    out = _render("guard_throw_arm_98_2693.hasm", 2693)

    assert "throw r19;\n                    r15" not in out
