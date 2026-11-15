"""
Both arms of a test run on into one block although an arm also leaves through a `throw` (F-223, 98/8536
`normalizeCSSTransitionProperties`).

    if (a.length) { ...; if (some) throw ...; r12 = !r6 } else { r12 = values.some(f) }  if (r12) { ... }

The post-dominator of the test is empty because of the `throw`, so the `else` arm ended in a `goto` to the `if (r12)`
that follows the `if`. The block whose immediate dominator is the test and that both arms enter is the merge.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_join_after_a_throwing_arm_follows_the_if():
    hasm = (_DATA / "arm_join_after_throw_98_8536.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 8536, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "r12 = r16.some(function_12106);\n    }\n    if (r12) {" in code
