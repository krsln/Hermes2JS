"""
A `catch` that swallows some errors falls out into the code after the `try` (F-213, 98/6705 `getLayoutNode`).

    try { ...; if (r0 == null) r0 = r1; r1 = r0 } catch (e) { if (e instanceof Error && !match) throw e }
    if (r6) { ... }

The `try` body jumps to the same `if (r6)` the catch falls into. Three things were wrong:
the catch's own guard took that code as its `then` arm (the `try` body then needed a `goto` into it),
the catch swallowed it when the `try` was built (it has no post-dominator because the catch can throw),
and `r1 = r0` after the arm `if (r0 == null) r0 = r1` printed `r1 = r1`, which is no statement at all.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _code():
    hasm = (_DATA / "try_exit_catch_fallthrough_98_6705.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 6705, strict=False), verbose=False, raw=False)
    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_try_body_needs_no_goto():
    assert "goto" not in _code()


def test_the_code_after_the_try_follows_the_catch():
    code = _code()

    assert "        }\n        if (r6) {" in code
    assert code.count("if (r6) {") == 1


def test_the_join_copy_is_kept_in_the_try_body():
    assert "            r1 = r0;\n        } catch" in _code()
