"""
An object made by `new` is ONE object, so it is built once and read through its register (F-146, 96/1163
`PlatformColor`).

    r1 = new Array(n)          // CreateThis / Construct / SelectObject
    loop: r1[i] = arguments[i]
    return { resource_paths: r1 }

The value of `SelectObject` is the `NewExpression` itself, and `get_register_expression` inlined it into
every reader: the loop printed `new Array(r5)[r0] = arguments[r0]`, a fresh array on every iteration
that nothing keeps, and the result held a second one. A `new` is now kept in its register like a call
or a literal object, when a read sits in a loop its definition is outside of or when another read
of it does (the scratch pass of `OpcodeDispatcher` says which definitions print).

96/15130 `tag` stores the array in the environment first and fills it in the loop afterwards:
`r0[0] = new Array(n)` stored one array and the loop filled a second one.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def _code() -> str:
    return _render("new_object_identity_96_1163.hasm", 1163)


def test_a_new_object_read_twice_is_built_once():
    code = _code()

    assert code.count("new Array(") == 1


def test_the_loop_fills_the_register_that_is_returned():
    code = _code()

    assert "r1 = new Array(r5);" in code
    assert "r1[r0] = arguments[r0];" in code
    assert '"resource_paths": r1' in code


def test_a_new_object_stored_before_a_loop_fills_the_stored_object():
    code = _render("new_object_stored_then_filled_96_15130.hasm", 15130)

    assert code.count("new Array(") == 1
    assert "r0[0] = r4;" in code
    assert "r4[r9] = arguments[r2];" in code
