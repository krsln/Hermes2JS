"""
An arm that throws unless its test jumps to the body the guard skips to (F-212, 98/9633 `Tr`).

    if (signal !== undefined) { ...; if (!isAbortSignal(signal)) throw new TypeError(...); }  <build and return the object>

The object-building body ends in a `return` of its own and is entered by the guard and by the arm's test. With no
post-dominator, the body became the `then` arm of the guard and the arm's test a `goto` into it. The body follows
the `if` now.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_body_follows_the_signal_check():
    hasm = (_DATA / "arm_throw_then_body_98_9633.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 9633, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "if (undefined !== r5) {" in code
    assert code.count("return r4;") == 1
