"""
`if (r5 !== "object") { <typeof checks> } else { ...; if (r2 != null) return r2; }` where the else arm's test falls
into the very `typeof` checks the branch jumps to (F-210, 96/1139 `processColor`).

`r5 = typeof r6` stays in a register (the target tests `r5 !== "number"` again), so the branch condition was no
`typeof x` test and `_arm_retests_constant` did not see that the arm's other test runs on into the branch
target. The target was printed as the `then` arm, the arm's test as `if (r2 != null) goto L; return r2`
(the fall-through into the checks lost). The target is now the join after `if (r5 === "object") { ... }`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _code() -> str:
    hasm = (_DATA / "typeof_register_join_96_1139.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 1139, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_typeof_checks_follow_the_object_branch():
    code = _code()

    assert "goto" not in code
    assert 'if (r5 === "object") {' in code
    assert "if (r2 != null) {\n                    return r2;\n                }\n            }\n            if (r5 !== \"number\") {" in code
