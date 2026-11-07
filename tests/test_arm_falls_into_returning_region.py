"""
An arm that falls into the code a test before it skips to, after a test whose taken side is code of its own
(F-222, 98/10919 `onAction`).

    if (a) goto ARM; <mid>; if (r !== null) goto REST; ARM: <code>; return; REST: <rest of the function>; return

`ARM` is entered from the first test and from the end of `<mid>`; `REST` is a whole region that only the second
test reaches and that ends in `return`s. Only a lone `return` counted as such a taken side, so `ARM` stayed the
`then` arm of the first test and the second test printed `if (r !== null) goto L` into `REST`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_arm_follows_the_if_that_runs_into_it():
    hasm = (_DATA / "arm_falls_into_returning_region_98_10919.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 10919, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert 'if (typeof param1.target !== "string" || param1.target === r7.key) {' in code
    assert "if (r8 !== null) {\n                r5 = r7 === r8;" in code
