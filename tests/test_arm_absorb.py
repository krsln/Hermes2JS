"""
`||` / `?:` folds must not lose what the folded arm computed
(`shared/_absorb.py`).
"""

from __future__ import annotations

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.transforms.shared import substitute_register
from hermes_decompiler.ir.expressions import BinaryExpression, Identifier
from hermes_decompiler.ir.Operators import BinaryOperator

from tests.test_repoint_references import LAB_TO_XYZ


def test_substitute_register_replaces_every_use():
    one = Identifier(name="param1")
    expr = BinaryExpression(left=Identifier(name="r7"), operator=BinaryOperator.ADD, right=Identifier(name="r7"))

    out = substitute_register(expr, "r7", one)

    assert out.left is one and out.right is one
    assert substitute_register(expr, "r9", one) is expr


def test_lab_ternary_keeps_the_subtraction_the_arm_computed():
    out = Decompiler.render(Decompiler.build_context(LAB_TO_XYZ, 12962), verbose=False)

    # `r7 = r7 - 0.1379; r2 = r7 / 7.787` used to fold to `r7 / 7.787`.
    assert "(r7 - 0.13793103448275862) / 7.787" in out
    assert "(r6 - 0.13793103448275862) / 7.787" in out
    assert "(r4 - 0.13793103448275862) / 7.787" in out


def test_destructuring_guard_keeps_the_assignment_in_the_arm():
    # hermes-98 `parameterDestructureTest`: `r6 = r4` used to vanish together
    # with the folded `r3 === undefined || r3 === undefined`.
    root = Path(__file__).resolve().parent.parent / "apps/demo/fixtures/98/sections"
    path = root / "function_9488_parameterDestructureTest.hasm"
    out = Decompiler.render(Decompiler.build_context(path.read_text(encoding="utf-8"), 9488, strict=False),
                            verbose=False)

    assert "r6 = r4" in out
    assert "r3 === undefined || r3 === undefined" not in out


def _render_fixture(version: str, index: int, name: str) -> str:
    root = Path(__file__).resolve().parent.parent / "apps/demo/fixtures" / version / "sections"
    text = (root / f"function_{index}_{name}.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(text, index, strict=False), verbose=False)


def test_flattening_does_not_look_past_a_printed_definition():
    # hermes-96 `defaultWithRestTest`: `r1 = arguments[0]` sits in front of the
    # nested `if (r1 !== undefined)`. Flattening to `length > 0 && r1 !== undefined`
    # read r1 before the only statement that sets it.
    out = _render_fixture("96", 15155, "defaultWithRestTest")

    assert "arguments.length > 0 && r1 !== undefined" not in out
    assert "r1 = arguments[0]" in out


# hermes-98 `getDevServer`: `if (r3 == null) r3 = env[3]` merges with the
# earlier `r3`; the object literal below it reads r3 after the merge.
_GET_DEV_SERVER = (
    "00000000|<GetParentEnvironment>: <Reg8: 2, UInt8: 0>",
    "00000003|<LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 1>",
    "00000007|<LoadConstUndefined>: <Reg8: 0>",
    "00000009|<JStrictNotEqual>: <Addr8: 80, Reg8: 3, Reg8: 0>",
    "0000000d|<LoadFromEnvironment>: <Reg8: 1, Reg8: 2, UInt8: 0>",
    "00000011|<GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 115>",
    "00000016|<GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 1, string_id: 150>",
    "0000001b|<Call1>: <Reg8: 1, Reg8: 1, Reg8: 4>",
    "0000001f|<GetById>: <Reg8: 5, Reg8: 1, UInt8: 2, string_id: 13447>",
    "00000025|<GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 3, string_id: 180>",
    "0000002a|<CreateRegExp>: <Reg8: 1, string_id: 2089, string_id: 6457, UInt32: 52>",
    "00000038|<Call2>: <Reg8: 6, Reg8: 4, Reg8: 5, Reg8: 1>",
    "0000003d|<LoadConstNull>: <Reg8: 1>",
    "0000003f|<JmpFalse>: <Addr8: 7, Reg8: 6>",
    "00000042|<GetByIndex>: <Reg8: 1, Reg8: 6, UInt8: 0>",
    "00000046|<StoreToEnvironment>: <Reg8: 2, UInt8: 1, Reg8: 1>",
    "0000004a|<LoadConstNull>: <Reg8: 4>",
    "0000004c|<JmpFalse>: <Addr8: 6, Reg8: 6>",
    "0000004f|<Mov>: <Reg8: 4, Reg8: 5>",
    "00000052|<StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 4>",
    "00000056|<Mov>: <Reg8: 3, Reg8: 1>",
    "00000059|<LoadConstNull>: <Reg8: 0>",
    "0000005b|<JNotEqual>: <Addr8: 8, Reg8: 3, Reg8: 0>",
    "0000005f|<LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 3>",
    "00000063|<NewObjectWithBuffer>: <Reg8: 1, UInt16: 1241, UInt16: 17424>",
    "00000069|<PutOwnBySlotIdx>: <Reg8: 1, Reg8: 3, UInt8: 0>",
    "0000006d|<LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 2>",
    "00000071|<PutOwnBySlotIdx>: <Reg8: 1, Reg8: 3, UInt8: 1>",
    "00000075|<LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 1>",
    "00000079|<StrictNeq>: <Reg8: 0, Reg8: 2, Reg8: 0>",
    "0000007d|<PutOwnBySlotIdx>: <Reg8: 1, Reg8: 0, UInt8: 2>",
    "00000081|<Ret>: <Reg8: 1>",
)


def _render_listing(entries) -> str:
    body = "\n".join(f"==> {addr}: {text}" for addr, text in (e.split("|", 1) for e in entries))

    return (
            '\n=> [Function #1 "f" of 131 bytes]: 1 params, frame size=17, strict=1, exc handler=0, '
            "debug info=0  @ offset 0x00000000\n\nBytecode listing:\n\n" + body + "\n\n"
    )


def test_a_write_in_one_arm_is_not_inlined_into_a_read_after_the_merge():
    out = Decompiler.render(Decompiler.build_context(_render_listing(_GET_DEV_SERVER), 1), verbose=False)

    # Before: `if (r3 == null) { }` and `"url": r2[3]` - the arm printed
    # nothing and the object claimed the arm's value unconditionally.
    assert "if (r3 == null) {\n        r3 = r2[3]\n    }" in out
    assert "= r3\n" in out  # the object slot reads r3, not the arm's `r2[3]`
    assert "slot_0 = r2[3]" not in out


def _render_98(index: int, name: str) -> str:
    # With the set's batch tables: without them the generator dispatch is not detected.
    from tests.test_register_semantics import decompile

    return decompile("98", index)


def test_generator_keeps_the_environment_register_its_body_reads():
    # hermes-98 `generatorWithLoopTest`: the dispatch prologue that defined
    # `r1 = getParentEnvironment(0)` is deleted, the body still reads `r1[0]`.
    out = _render_98(12483, "generatorWithLoopTest")

    assert "r1 = getParentEnvironment(0)" in out
    assert out.index("r1 = getParentEnvironment(0)") < out.index("r1[0]")


def test_generator_state_machine_bookkeeping_is_not_printed():
    out = _render_98(12483, "generatorWithLoopTest")

    # `env[resume_slot] = k; env[state_slot] = SUSPENDED` before every yield,
    # the register mirror of the state, and the COMPLETED write in `finally`.
    assert "r1[2] = r8" not in out and "r1[3] = r8" not in out
    assert "r2 = 3" not in out and "finally" not in out


def test_a_catch_that_only_rethrows_is_not_printed():
    out = _render_98(12482, "simpleGeneratorTest")

    assert "catch" not in out and "r1[0]" not in out and "r1[1]" not in out
    assert out.count("yield") == 3
