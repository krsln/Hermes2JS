"""A try body's jump to a join that is itself an `if` is dropped (F-165).

    if (a) { if (b) { try { ...; jmp JOIN } catch { ... } } }   JOIN: if (r0) ... else ...

`_next_fallthrough_address` only resolved a plain block as the next sibling and gave up when the try sat in an
`if` arm or the join was an `if`, so the jump printed as `goto label_56`. Arms resume where their `if` does, and
an `if` sibling starts at the test block its condition swallowed.

    96/331  `function_331`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_try_body_ends_without_a_goto():
    hasm = (_DATA / "try_exit_to_if_join_96_331.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 331, strict=False), verbose=False, raw=False)
    out = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in out
    assert out.index("r0 = r2;") < out.index("} catch")
    assert out.index("} catch") < out.index("if (r0) {")
