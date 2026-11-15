"""
An arm that leaves only through `return`s of its own and falls into the code its (constant) test skips to
(F-220, 98/13851: the second iterator element).

    if (r6 === undefined) { if (!x) return null; ...; if (optional) return null; }  <code both paths run>

The test compares with `undefined`, which the arm-falls-into rule left to chains of case tests, so the code after
the arm was printed as the `then` arm and the arm's last test became `if (r5) goto L; return null;`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_code_after_the_arm_follows_the_if():
    hasm = (_DATA / "arm_guard_constant_test_98_13851.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 13851, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "if (r6 === undefined) {" in code
    assert "if (r5) {\n                return null;\n            }" in code
    assert code.rindex("r4 = r4[0];") > code.index("if (r5) {")
