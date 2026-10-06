"""
`||` / `?:` folds must not lose what the folded arm computed
(`shared/_absorb.py`).
"""

from __future__ import annotations

import sys
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

    # The element writes (`r6 = r4` used to vanish with the folded guard) are
    # now part of the destructuring pattern itself.
    assert "[r7, r6] = param2" in out
    assert "r3 === undefined || r3 === undefined" not in out
    assert "GetIterator" not in out and ".next()" not in out


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


def test_generator_body_is_printed_in_control_flow_order():
    # hermes-98 `simpleGeneratorTest`: the resume continuations sit at LOWER
    # addresses than the code that reaches them, so address order printed
    # `end` + `return` first and the `start` log last.
    out = _render_98(12482, "simpleGeneratorTest")

    order = [out.index(marker) for marker in ("/start", "yield 1", "yield 2", "yield 3", "/end", "return r7")]

    assert order == sorted(order)


def test_async_environment_prologue_precedes_the_code_that_reads_it():
    # hermes-98 `simpleAsyncTest`: `r1 = getParentEnvironment(0)` was printed
    # below the post-await body that reads `r1[0][0]`.
    out = _render_98(13742, "simpleAsyncTest")

    assert out.index("r1 = getParentEnvironment(0)") < out.index("await") < out.index("r1[0][0] = param2")
    assert out.index("r1[0][0] = param2") < out.index("return r5")


def test_flat_array_destructuring_is_one_statement():
    # hermes-98 `swapViaDestructureTest`: `[a, b] = [2, 1]` compiled to
    # IteratorBegin/Next/Close diamonds; every guard was printed.
    out = _render_98(9489, "swapViaDestructureTest")

    assert "[r8, r7] = r6" in out
    assert "GetIterator" not in out and ".next()" not in out and ".return()" not in out
    assert "console.log(r8, r7)" in out


def test_destructuring_statement_cannot_glue_onto_the_previous_line():
    # No statement terminators are printed, so `r6 = r7\n[r8, r7] = r6` would
    # parse as `r6 = r7[r8, r7] = r6`.
    out = _render_98(9489, "swapViaDestructureTest")

    assert "\n[" not in out


def test_default_value_ternary_does_not_read_its_own_target_before_it_is_set():
    # hermes-98 `parameterDestructureTest`: `{ name = "anon" } = param1` folded to
    # `r8 = (r8 !== undefined) ? param1.name : "anon"`. The default (`r8 =
    # param1.name`) moved inside the ternary, so the test read `r8` before
    # anything defined it.
    out = _render_98(9488, "parameterDestructureTest")

    assert 'r8 = (param1.name !== undefined) ? param1.name : "anon"' in out
    assert "(r8 !== undefined)" not in out


def test_default_value_ternary_test_names_the_default_in_every_destructuring_form():
    for index, name in ((9485, "nestedObjectDestructureTest"), (9486, "renamedDefaultDestructureTest")):
        out = _render_98(index, name)

        assert "(r5 !== undefined) ?" not in out
        assert ".page !== undefined) ?" in out or ".retries !== undefined) ?" in out


def test_for_of_does_not_leave_its_iterator_setup_behind():
    # hermes-98 `forOfTest`: `for (const r6 of r2)` stands for the iterator, but
    # `r3 = GetIterator(r2)` was still printed in front of it.
    out = _render_98(9479, "forOfTest")

    assert "for (const r6 of r2)" in out
    assert "GetIterator" not in out


def test_iterator_setup_is_kept_when_the_register_is_still_read():
    # hermes-96 `asyncLoopTest`: the for-of body still calls `r4.return()` (the
    # generator-return path), so the iterator register must stay defined.
    from tests.test_register_semantics import decompile

    out = decompile("96", 15185)

    assert "r4 = GetIterator(param1)" in out
    assert "r4.return()" in out


def test_nested_pattern_with_holes_is_one_statement():
    # `const [[a, b], , [, d]] = matrix` is three iterators (outer + one per nested
    # pattern), a hole each, and an iterator-close cleanup handler around each
    # nested pattern. It is ONE destructuring statement.
    out = _render_98(9487, "nestedArrayDestructureTest")

    assert "[[r8, r7], , [, r0]] = r6" in out
    assert "GetIterator(r6)" not in out
    assert "r1.next()" not in out and "r1.return()" not in out
    assert "label_544" not in out


def test_array_pattern_defaults_and_rest_are_one_statement():
    # `const [first = 0, second = 0, ...remaining] = [10]`: each default is a
    # compare-and-assign diamond (the done path jumps straight to the default),
    # the default evaluation and the rest loop sit under iterator cleanup handlers.
    out = _render_98(9487, "nestedArrayDestructureTest")

    assert "[r15 = 0, r14 = 0, ...r13] = r17" in out
    assert "GetIterator" not in out and ".return()" not in out and "goto" not in out
    assert "console.log(r15, r14, r13)" in out


def test_for_condition_reads_the_bound_the_latch_recomputes():
    # hermes-98 `complexTest`: `for (let i = 0; i < numbers.length; i++)` reloads
    # the bound right before the compare (`r7 = r14.length; if (r0 < r7) goto body`).
    # The header used to read `r7` before the first iteration - where nothing
    # printed defines it (the entry guard inlined the value) - and the reload
    # stayed behind as the last statement of the body.
    out = _render_98(9453, "complexTest")

    assert "for (i = 0; i < r14.length; i = r1 + 1) {" in out
    assert "r7 = r14.length" not in out


def test_bound_stays_in_the_body_when_the_loop_is_not_a_for():
    # hermes-98 `generatorWithLoopTest`: the entry value of the register the
    # condition reads is NOT the loop variable (the guard compares the other
    # way round), so a `for` header would test the wrong thing first. It stays a
    # `do { } while` and keeps the bound reload.
    out = _render_98(12483, "generatorWithLoopTest")

    assert "do {" in out and "r5 = r1[1][0]" in out and "} while (r7 < r5);" in out


def test_array_hole_prints_its_comma():
    from hermes_decompiler.backend.emit.printer.ExpressionPrinter import ExpressionPrinter
    from hermes_decompiler.ir.expressions import ArrayExpression, ArrayHole, Identifier

    printer = ExpressionPrinter()
    a, b = Identifier(name="a"), Identifier(name="b")

    assert printer.visit(ArrayExpression(elements=(a, ArrayHole(), b))) == "[a, , b]"
    assert printer.visit(ArrayExpression(elements=(ArrayHole(), b))) == "[, b]"
    # `[a, ]` would be a single element.
    assert printer.visit(ArrayExpression(elements=(a, ArrayHole()))) == "[a, ,]"


def test_for_of_with_destructured_element_is_recognized():
    # hermes-98 `mapTest`: `for (const [k, v] of map)` keeps its close scaffold
    # INSIDE the loop (the try covers the body only). It used to print as
    # `while (!(r8 === undefined)) { ...; try { ... } catch { r5.return(); throw } }`.
    out = _render_98(9495, "mapTest")

    # The element is destructured by the loop head itself, not by a first
    # statement through two registers (`r11 = r9; [r7, r6] = r11`).
    assert "for (const [r7, r6] of r3) {" in out
    assert "r11" not in out and "[r7, r6] =" not in out
    assert "while" not in out and "caughtException" not in out and ".return()" not in out and "GetIterator" not in out


def _render_98_unfolded(monkeypatch, index: int, name: str) -> str:
    # The destructuring pass folds the iterator protocol away; switch it off to
    # keep exercising the try/catch structuring it used to leave behind.
    from hermes_decompiler.backend.transforms.cfg_passes import ArrayDestructuringCfgPass

    monkeypatch.setattr(sys.modules[ArrayDestructuringCfgPass.__module__].ArrayDestructuringCfgPass, "run",
                        lambda self: 0)

    return _render_98(index, name)


def test_catch_keeps_the_rethrow_that_closes_it(monkeypatch):
    # hermes-98 `nestedArrayDestructureTest` (unfolded): `catch (e) { if (it) it.return(); throw e }`.
    # The catch body stopped at the post-dominator, which is the catch's OWN
    # `throw` block, so the rethrow used to be printed after the try.
    import re

    out = _render_98_unfolded(monkeypatch, 9487, "nestedArrayDestructureTest")

    catch = re.search(r"catch \(caughtException\) \{\n        if \(r7 !== undefined\) \{(.*?)\n    \}\n", out, re.S)

    assert catch is not None, out
    assert "throw caughtException;" in catch.group(1)


def test_rethrow_names_the_catch_parameter(monkeypatch):
    # `Catch` is folded into the catch parameter, so nothing in the CFG defined
    # `r0` any more and `throw r0` stayed bare.
    out = _render_98_unfolded(monkeypatch, 9487, "nestedArrayDestructureTest")

    assert "throw r0" not in out


def test_rest_element_is_part_of_the_destructuring_pattern():
    # hermes-98 `spreadArrayTest`: `const [first, ...rest] = arr` compiled to
    # IteratorNext for `first`, then a NewArray + for-of-like loop for `rest`
    # with a cleanup handler. The loop was even misread as a for-of over `arr`.
    out = _render_98(9492, "spreadArrayTest")

    assert "[r5, ...r4] = r7" in out
    assert "GetIterator" not in out and "for (const" not in out and "caughtException" not in out
