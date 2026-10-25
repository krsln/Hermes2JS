"""
A member read made inside a `try` stays there (F-33, 98/13768).

    try { x = param1.aborted } catch { return false }
    return typeof x === "boolean"

compiles to a `GetById` inside the handler's range and a `TypeOfIs` after it. The read was folded into
the `TypeOfIs`, which printed `typeof param1.aborted` OUTSIDE the `try` and left `try { } catch` empty: a
getter (or `undefined`) that throws would no longer reach the `catch`. A read that can throw is now
named by its register where the reader stands outside the range.

Generator/async bodies are exempt: their state machine wraps the body in one synthetic `try`, and
the golden outputs of `generatorWithLoopTest` / `simpleAsyncTest` / `asyncLoopTest` (98) guard that.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _code() -> str:
    hasm = (_DATA / "try_member_read_98_13768.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 13768, strict=False), verbose=False, raw=False)


def test_the_read_that_can_throw_is_inside_the_try():
    code = _code()

    assert "try {\n            r0 = param1.aborted;\n        } catch" in code


def test_the_reader_outside_the_try_names_the_register():
    code = _code()

    assert 'r0 = typeof r0 === "boolean";' in code
    assert "typeof param1.aborted" not in code
