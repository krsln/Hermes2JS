"""
A `try` body that ends by jumping to the function's closing `return` gets its own `return` (F-10(b), 98/14166).

`r0 = undefined` is set once at the entry and the `catch` handler (which has no predecessor) falls into
the same closing `return r0`. `_single_reaching_value` took the handler for a path that never set the
register and refused the copy, so the `try` printed `goto label_N`. A handler now counts as running from
inside its try range, and a copy of a constant return says the value instead of naming the register.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _code() -> str:
    hasm = (_DATA / "shared_return_try_exit_98_14166.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 14166, strict=False), verbose=False, raw=False)


def test_a_try_body_that_ends_the_function_returns_instead_of_jumping():
    code = _code()

    assert "goto" not in code
    assert "return undefined;\n    } catch" in code


def test_the_copied_return_names_no_register_that_prints_nowhere():
    assert "return r0" not in _code()
