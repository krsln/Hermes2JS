"""Generators, `yield`, `await`: resumed values, cleanup copies, loops.

Merged from: test_await_with_cleanup_return_arm, test_generator_await_joined_value, test_generator_catch_reentry, test_generator_loop_yield, test_generator_no_suspend, test_generator_own_environment, test_generator_resume_copies, test_generator_yield_array, test_generator_yield_in_loop_entry, test_inlined_resume_value_after_an_await, test_resumed_value_copied_into_an_object_literal, test_return_await_inside_a_try, test_test_before_await_suspend, test_yield_in_try_with_finally_copy, test_yield_value_earlier_block.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from test_register_semantics import decompile

import pytest

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.frontend.batch_pipeline import BatchContext, BatchPipeline
from hermes_decompiler.frontend.batch_pipeline.stages import (
    ClassEnvironmentTableStage,
    CreatorTableStage,
    EnvironmentOriginTableStage,
    PrivateNameTableStage,
)


# ----------------------------------------------------------------------------------------------------
# await_with_cleanup_return_arm
#
# An `await` whose resume guard's return arm holds cleanup code folds anyway (96/14482, 14867, 8059 `_anon_0`).
#
#     try { await loadSingleFontAsync(a, b); markLoaded(a); } finally { delete loadPromises[a]; }
#
# The `finally` is copied onto the `.return()` path, so the guard `if (resumeIsReturn)` after the suspend does not
# end in a lone `Ret`. An `await` never resumes with the return flag set, so that arm is dead and the guard folds;
# before, the save stayed a `goto label_46` and a second `await yield` was printed.
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"


def test_the_await_folds_and_the_dead_return_arm_is_dropped():
    hasm = (_DATA / "await_with_cleanup_return_arm_96_14482.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 14482, strict=False), verbose=False, raw=False)

    assert "goto label" not in out
    assert "await yield" not in out
    assert "__resumeIsReturn" not in out
    assert "await r6(r5, r1);\n        r5 = r3[5];" in out


# ----------------------------------------------------------------------------------------------------
# generator_await_joined_value
#
# `await ref?.f()` (`yield` here) folds although the suspend block holds only protocol (F-12, 98/13533 `startAnimating`).
#
#     r7 = undefined; if (r8) skip; r7 = r9.f();     // the value joins two paths
#     join:  env[2] = r5; env[1] = r5; {value: r7, done: false}; ret
#
# The resume point's number (`r5 = 1`) was loaded in the dispatch chain, so the suspend block has no leading constant
# load and was declined as "could not find the yielded value". It also needs a suspend that does not borrow the
# protocol store's identity: the protocol strip removed the suspend together with the store it was taken from.
# ----------------------------------------------------------------------------------------------------

def _render() -> str:
    sections = [
        (11786, (_DATA / "generator_await_joined_value_98_13533_creator.hasm").read_text(encoding="utf-8")),
        (13533, (_DATA / "generator_await_joined_value_98_13533.hasm").read_text(encoding="utf-8")),
    ]
    tables = BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()

    return Decompiler.render(Decompiler.build_context(sections[1][1], 13533, batch_tables=tables), verbose=False)


def test_the_awaited_joined_value_is_kept():
    code = _render()

    assert "goto" not in code
    assert "may not be called on executing" not in code
    # the section pair alone does not say whether the wrapper is async, so the suspend prints as `yield`
    assert "yield r7;" in code or "await r7;" in code
    assert code.index("r7 = r9.startAnimating();") < code.index("r7;", code.index("r7 = r9.startAnimating();") + 30)


# ----------------------------------------------------------------------------------------------------
# generator_catch_reentry
#
# A `catch` that resumes a generator/async state by re-entering the dispatch chain is folded (F-12, F-239).
#
# The body's `try` has one exception handler: `catch (e) { env[5] = e; if (env[6] === 0) throw e;
# env[4] = <state>; jmp <dispatch head> }`. The state is a constant the chain maps to a block (the cleanup / the
# `catch` clause), so the jump is a jump to that block; the chain no longer stays reachable and the function folds.
#
#     98/12484 `generatorTryFinallyTest`, 98/13743 `asyncTryCatchTest`, 98/13744 `asyncLoopTest`, 98/12918 and more
#
# Three things have to hold together: the re-entry gets its OWN copy of the target's code (an edge from the `catch` into
# the protected range would put the handler in front of the `try`), `try_blocks` is ordered by the folded layout (the
# `try` starts at the first protected block, not at the resume code that has the lowest address), and the prologue's
# other definitions the body reads (`r9 = getParentEnvironment(1)`, 98/13744; 98/13832 and 98/14155 too) are defined again.
# ----------------------------------------------------------------------------------------------------

def test_generator_try_finally_folds_into_a_try_with_the_cleanup_in_the_catch():
    out = decompile("98", 12484)

    assert "goto" not in out
    assert "NOT valid JavaScript" not in out
    assert "} catch (caughtException) {" in out
    # The try starts at the function body, not after the first `yield`.
    assert out.index("try {") < out.index('yield "a"')
    # The cleanup is reachable from the catch as its own copy.
    assert out.count("generatorTryFinallyTest/cleanup") == 2


def test_async_try_catch_keeps_the_await_inside_the_try():
    out = decompile("98", 13743)

    assert "goto" not in out
    assert out.index("try {") < out.index("await ")


def test_prologue_environment_the_body_reads_is_defined_again():
    # 98/13744 `asyncLoopTest`: `r1[5] = r9` where `r9 = getParentEnvironment(1)` sat in the folded prologue.
    out = decompile("98", 13744)

    assert "r9 = getParentEnvironment(1);" in out
    assert out.index("r9 = getParentEnvironment(1);") < out.index("r1[5] = r9;")


# ----------------------------------------------------------------------------------------------------
# generator_loop_yield
#
# A `yield` in the body of a `do { } while` (96/718 `createValueIterator`, 96/720
# `createKeyIterator`): the resume guard has no `else`, the loop's `i++` is a sibling
# behind it, and the register the suspend point yields is not the one written right
# before the `SaveGenerator`:
#
#     r1 = param1[r3]
#     Mov r2, r3                  (the counter, read again behind the guard)
#     SaveGenerator -> R ; Ret r1  (the `Ret` is never reached; it yields r1)
#     R: ResumeGenerator r1, r5 ; JmpTrue r5, <return>
#     Inc r3, r2                  (reads the copy)
#
# The fold used to bail out on a guard with siblings behind it and left
# `r1 = await yield; if (__resumeIsReturn) { return r1; }` and a `return r2;` after the
# loop (the unreachable `Ret`). Folding it must yield what the `Ret` returns (not the
# instruction before the save) and must not hide a write the code behind the guard reads.
# ----------------------------------------------------------------------------------------------------

_HASM_718 = r"""
=> [Function #718 "?anon_0_createValueIterator" of 64 bytes]: 2 params, frame size=6, strict=1, exc handler=0, debug info=0  @ offset 0x00106368

Bytecode listing:

==> 00000000: <StartGenerator>: <>
==> 00000001: <LoadParam>: <Reg8: 4, UInt8: 1>
==> 00000004: <ResumeGenerator>: <Reg8: 0, Reg8: 1>
==> 00000007: <JmpTrue>: <Addr8: 54, Reg8: 1>  # Address: 0000003d
==> 0000000a: <GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 1, string_id: 169>  # String: 'length' (Identifier)
==> 0000000f: <LoadConstZero>: <Reg8: 3>
==> 00000011: <Less>: <Reg8: 1, Reg8: 3, Reg8: 1>
==> 00000015: <JmpFalse>: <Addr8: 32, Reg8: 1>  # Address: 00000035
==> 00000018: <GetByVal>: <Reg8: 1, Reg8: 4, Reg8: 3>
==> 0000001c: <Mov>: <Reg8: 2, Reg8: 3>
==> 0000001f: <SaveGenerator>: <Addr8: 4>  # Address: 00000023
==> 00000021: <Ret>: <Reg8: 1>
==> 00000023: <ResumeGenerator>: <Reg8: 1, Reg8: 5>
==> 00000026: <JmpTrue>: <Addr8: 20, Reg8: 5>  # Address: 0000003a
==> 00000029: <Inc>: <Reg8: 3, Reg8: 2>
==> 0000002c: <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 169>  # String: 'length' (Identifier)
==> 00000031: <JLess>: <Addr8: -25, Reg8: 3, Reg8: 2>  # Address: 00000018
==> 00000035: <LoadConstUndefined>: <Reg8: 2>
==> 00000037: <CompleteGenerator>: <>
==> 00000038: <Ret>: <Reg8: 2>
==> 0000003a: <CompleteGenerator>: <>
==> 0000003b: <Ret>: <Reg8: 1>
==> 0000003d: <CompleteGenerator>: <>
==> 0000003e: <Ret>: <Reg8: 0>
"""

_HASM_720 = r"""
=> [Function #720 "?anon_0_createKeyIterator" of 60 bytes]: 2 params, frame size=6, strict=1, exc handler=0, debug info=0  @ offset 0x001063b1

Bytecode listing:

==> 00000000: <StartGenerator>: <>
==> 00000001: <LoadParam>: <Reg8: 4, UInt8: 1>
==> 00000004: <ResumeGenerator>: <Reg8: 0, Reg8: 1>
==> 00000007: <JmpTrue>: <Addr8: 50, Reg8: 1>  # Address: 00000039
==> 0000000a: <GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 1, string_id: 169>  # String: 'length' (Identifier)
==> 0000000f: <LoadConstZero>: <Reg8: 3>
==> 00000011: <Less>: <Reg8: 1, Reg8: 3, Reg8: 1>
==> 00000015: <JmpFalse>: <Addr8: 28, Reg8: 1>  # Address: 00000031
==> 00000018: <Mov>: <Reg8: 2, Reg8: 3>
==> 0000001b: <SaveGenerator>: <Addr8: 4>  # Address: 0000001f
==> 0000001d: <Ret>: <Reg8: 2>
==> 0000001f: <ResumeGenerator>: <Reg8: 1, Reg8: 5>
==> 00000022: <JmpTrue>: <Addr8: 20, Reg8: 5>  # Address: 00000036
==> 00000025: <Inc>: <Reg8: 3, Reg8: 2>
==> 00000028: <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 169>  # String: 'length' (Identifier)
==> 0000002d: <JLess>: <Addr8: -21, Reg8: 3, Reg8: 2>  # Address: 00000018
==> 00000031: <LoadConstUndefined>: <Reg8: 2>
==> 00000033: <CompleteGenerator>: <>
==> 00000034: <Ret>: <Reg8: 2>
==> 00000036: <CompleteGenerator>: <>
==> 00000037: <Ret>: <Reg8: 1>
==> 00000039: <CompleteGenerator>: <>
==> 0000003a: <Ret>: <Reg8: 0>
"""


def _code(hasm: str, index: int) -> str:
    js = Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in js.splitlines() if not line.strip().startswith("//"))


def test_yield_in_do_while_yields_what_the_ret_returns():
    code = _code(_HASM_718, 718)

    assert "__resumeIsReturn" not in code
    assert "await yield" not in code
    assert "yield param1[r3];" in code
    assert "return" not in code


def test_copy_made_before_the_save_stays_defined_for_the_code_behind_the_guard():
    code = _code(_HASM_718, 718)

    assert "r2 = r3;" in code
    assert code.index("r2 = r3;") < code.index("r3 = r2 + 1;")


def test_yielded_register_read_behind_the_guard_is_not_hidden():
    code = _code(_HASM_720, 720)

    assert "__resumeIsReturn" not in code
    assert "return" not in code
    # `Mov r2, r3; Save; Ret r2` and `Inc r3, r2` behind the guard reads r2.
    assert code.index("r2 = r3;") < code.index("yield r2;") < code.index("r3 = r2 + 1;")


# ----------------------------------------------------------------------------------------------------
# generator_no_suspend
#
# An async function that never awaits folds into its body (F-12, 98/12831 `queryCache`).
#
#     async queryCache(key) { return default.queryCache(key); }
#
# has a state machine with no suspend site: no resume slot, only the running/exhausted guards on the state and the
# `.throw()`/`.return()` tests on the action in front of the body. With no site, `detect` returned None and the whole
# machine stayed (17 files in 98). The body is what the first `.next()` runs, found by walking the guards and the
# action tests.
# ----------------------------------------------------------------------------------------------------

def _render_2() -> str:
    sections = [
        (10269, (_DATA / "generator_no_suspend_98_12831_creator.hasm").read_text(encoding="utf-8")),
        (12831, (_DATA / "generator_no_suspend_98_12831.hasm").read_text(encoding="utf-8")),
    ]
    tables = BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()

    return Decompiler.render(Decompiler.build_context(sections[1][1], 12831, batch_tables=tables), verbose=False)


def test_the_body_is_all_that_is_left():
    code = _render_2()

    assert "goto" not in code
    assert "may not be called on executing" not in code
    assert "switch" not in code
    assert "r7 = r7.queryCache(r8);" in code
    assert '{ "value": r7, "done": true }' in code


# ----------------------------------------------------------------------------------------------------
# generator_own_environment
#
# The generator entry block holds the body's own environment next to the resume
# pair (96/14490):
#
#     StartGenerator; r8 = param1; r5 = param2; r2 = createEnvironment(); ResumeGenerator …
#
# Folding the resume pair away used to clear the whole block, so `r2[0] = …`
# afterwards stored into an environment nothing defined.
# ----------------------------------------------------------------------------------------------------

_HASM = r"""
=> [Function #14490 "?anon_0_" of 261 bytes]: 3 params, frame size=19, strict=1, exc handler=0, debug info=0  @ offset 0x0025af0f

Bytecode listing:

==> 00000000: <StartGenerator>: <>
==> 00000001: <LoadParam>: <Reg8: 8, UInt8: 1>
==> 00000004: <LoadParam>: <Reg8: 5, UInt8: 2>
==> 00000007: <CreateEnvironment>: <Reg8: 2>
==> 00000009: <ResumeGenerator>: <Reg8: 0, Reg8: 1>
==> 0000000c: <JmpTrueLong>: <Addr32: 246, Reg8: 1>  # Address: 00000102
==> 00000012: <LoadConstUndefined>: <Reg8: 3>
==> 00000014: <StoreNPToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 3>
==> 00000018: <GetEnvironment>: <Reg8: 1, UInt8: 2>
==> 0000001b: <LoadFromEnvironment>: <Reg8: 4, Reg8: 1, UInt8: 2>
==> 0000001f: <GetByIdShort>: <Reg8: 4, Reg8: 4, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
==> 00000024: <GetById>: <Reg8: 4, Reg8: 4, UInt8: 2, string_id: 8650>  # String: 'unloadAsync' (Identifier)
==> 0000002a: <JmpTrue>: <Addr8: 43, Reg8: 4>  # Address: 00000055
==> 0000002d: <LoadFromEnvironment>: <Reg8: 4, Reg8: 1, UInt8: 1>
==> 00000031: <GetById>: <Reg8: 9, Reg8: 4, UInt8: 3, string_id: 13024>  # String: 'UnavailabilityError' (Identifier)
==> 00000037: <GetByIdShort>: <Reg8: 4, Reg8: 9, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
==> 0000003c: <CreateThis>: <Reg8: 6, Reg8: 4, Reg8: 9>
==> 00000040: <LoadConstString>: <Reg8: 11, string_id: 9595>  # String: 'expo-font' (Identifier)
==> 00000044: <LoadConstString>: <Reg8: 10, string_id: 8650>  # String: 'unloadAsync' (Identifier)
==> 00000048: <Mov>: <Reg8: 12, Reg8: 6>
==> 0000004b: <Construct>: <Reg8: 4, Reg8: 9, UInt8: 3>
==> 0000004f: <SelectObject>: <Reg8: 4, Reg8: 6, Reg8: 4>
==> 00000053: <Throw>: <Reg8: 4>
==> 00000055: <TypeOf>: <Reg8: 6, Reg8: 8>
==> 00000058: <LoadConstString>: <Reg8: 4, string_id: 7532>  # String: 'object' (Identifier)
==> 0000005c: <JStrictEqual>: <Addr8: 30, Reg8: 6, Reg8: 4>  # Address: 0000007a
==> 00000060: <LoadFromEnvironment>: <Reg8: 4, Reg8: 1, UInt8: 11>
==> 00000064: <Call3>: <Reg8: 4, Reg8: 4, Reg8: 3, Reg8: 8, Reg8: 5>
==> 0000006a: <SaveGenerator>: <Addr8: 4>  # Address: 0000006e
==> 0000006c: <Ret>: <Reg8: 4>
==> 0000006e: <ResumeGenerator>: <Reg8: 4, Reg8: 6>
==> 00000071: <JmpTrue>: <Addr8: 6, Reg8: 6>  # Address: 00000077
==> 00000074: <CompleteGenerator>: <>
==> 00000075: <Ret>: <Reg8: 4>
==> 00000077: <CompleteGenerator>: <>
==> 00000078: <Ret>: <Reg8: 4>
==> 0000007a: <JmpTrue>: <Addr8: 73, Reg8: 5>  # Address: 000000c3
==> 0000007d: <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 8>
==> 00000081: <GetGlobalObject>: <Reg8: 4>
==> 00000083: <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 5, string_id: 24>  # String: 'Object' (Identifier)
==> 00000089: <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 6, string_id: 118>  # String: 'keys' (Identifier)
==> 0000008e: <Call2>: <Reg8: 8, Reg8: 6, Reg8: 7, Reg8: 8>
==> 00000093: <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 7, string_id: 27>  # String: 'Promise' (Identifier)
==> 00000099: <GetById>: <Reg8: 4, Reg8: 6, UInt8: 8, string_id: 7443>  # String: 'all' (Identifier)
==> 0000009f: <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 9, string_id: 170>  # String: 'map' (Identifier)
==> 000000a4: <CreateClosure>: <Reg8: 2, Reg8: 2, function_id: 14491>  # Function: [#14491  of 31 bytes]: 2 params @ offset 0x0025b014
==> 000000a9: <Call2>: <Reg8: 2, Reg8: 7, Reg8: 8, Reg8: 2>
==> 000000ae: <Call2>: <Reg8: 2, Reg8: 4, Reg8: 6, Reg8: 2>
==> 000000b3: <SaveGenerator>: <Addr8: 4>  # Address: 000000b7
==> 000000b5: <Ret>: <Reg8: 2>
==> 000000b7: <ResumeGenerator>: <Reg8: 2, Reg8: 4>
==> 000000ba: <JmpTrue>: <Addr8: 6, Reg8: 4>  # Address: 000000c0
==> 000000bd: <CompleteGenerator>: <>
==> 000000be: <Ret>: <Reg8: 3>
==> 000000c0: <CompleteGenerator>: <>
==> 000000c1: <Ret>: <Reg8: 2>
==> 000000c3: <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 1>
==> 000000c7: <GetById>: <Reg8: 4, Reg8: 1, UInt8: 10, string_id: 9531>  # String: 'CodedError' (Identifier)
==> 000000cd: <GetGlobalObject>: <Reg8: 1>
==> 000000cf: <TryGetById>: <Reg8: 1, Reg8: 1, UInt8: 11, string_id: 14>  # String: 'HermesInternal' (Identifier)
==> 000000d5: <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 12, string_id: 96>  # String: 'concat' (Identifier)
==> 000000da: <LoadConstString>: <Reg8: 2, string_id: 3637>  # String: 'No fontFamily can be used for the provided options: ' (String)
==> 000000de: <LoadConstString>: <Reg8: 1, string_id: 2093>  # String: '. The second argument of `unloadAsync()` can only be used with a `string` value as the first argument.' (String)
==> 000000e2: <Call3>: <Reg8: 10, Reg8: 3, Reg8: 2, Reg8: 5, Reg8: 1>
==> 000000e8: <GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
==> 000000ed: <CreateThis>: <Reg8: 2, Reg8: 1, Reg8: 4>
==> 000000f1: <LoadConstString>: <Reg8: 11, string_id: 2414>  # String: 'ERR_FONT_API' (String)
==> 000000f5: <Mov>: <Reg8: 12, Reg8: 2>
==> 000000f8: <Construct>: <Reg8: 1, Reg8: 4, UInt8: 3>
==> 000000fc: <SelectObject>: <Reg8: 1, Reg8: 2, Reg8: 1>
==> 00000100: <Throw>: <Reg8: 1>
==> 00000102: <CompleteGenerator>: <>
==> 00000103: <Ret>: <Reg8: 0>
"""


def test_generator_keeps_its_own_environment_definition():
    js = Decompiler.render(Decompiler.build_context(_HASM, 14490, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in js.splitlines() if not line.strip().startswith("//"))

    assert "r2 = createEnvironment();" in code
    assert code.index("r2 = createEnvironment();") < code.index("r2[0] = undefined;")


# ----------------------------------------------------------------------------------------------------
# generator_resume_copies
#
# A suspend point whose resume pair is followed by `Mov`s, and a `SaveGenerator` that
# falls into its own resume address (96/6777, an `async` body):
#
#     r1 = await getMethod(...)
#     SaveGenerator -> R ; Ret r1            (the `Ret` is never reached)
#     R: ResumeGenerator r1, r2
#        Mov r4, r2                          (the return flag the guard tests)
#        Mov r2, r1                          (the resumed value, read behind the guard)
#        JmpFalse r4, ...
#
# Three things went wrong, each leaving a raw `goto label_64` and `r2 = await yield;`:
#
# 1. `RedundantJumpRegionPass` took the `SaveGenerator` of the first arm for a bare jump
#    to the next block and dropped the instruction with its jump;
# 2. `GeneratorStateMachineRegionPass` only knew a resume block that ENDS with the pair,
#    so the `Mov`s hid it;
# 3. the unreachable `Ret` behind the first arm's save landed in the `then` arm of the
#    SECOND arm's resume guard, so that guard held two `Ret`s and was not recognized.
# ----------------------------------------------------------------------------------------------------

_HASM_2 = r"""
=> [Function #6777 "?anon_0_" of 143 bytes]: 1 params, frame size=14, strict=1, exc handler=0, debug info=0  @ offset 0x001a3763

Bytecode listing:

==> 00000000: <StartGenerator>: <>
==> 00000001: <ResumeGenerator>: <Reg8: 0, Reg8: 1>
==> 00000004: <JmpTrueLong>: <Addr32: 136, Reg8: 1>  # Address: 0000008c
==> 0000000a: <GetGlobalObject>: <Reg8: 1>
==> 0000000c: <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
==> 00000012: <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 118>  # String: 'keys' (Identifier)
==> 00000017: <GetEnvironment>: <Reg8: 3, UInt8: 1>
==> 0000001a: <LoadFromEnvironment>: <Reg8: 1, Reg8: 3, UInt8: 5>
==> 0000001e: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
==> 00000023: <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
==> 00000028: <LoadConstZero>: <Reg8: 1>
==> 0000002a: <JGreater>: <Addr8: 37, Reg8: 2, Reg8: 1>  # Address: 0000004f
==> 0000002e: <LoadFromEnvironment>: <Reg8: 2, Reg8: 3, UInt8: 0>
==> 00000032: <GetById>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 17625>  # String: 'getMethod' (Identifier)
==> 00000038: <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
==> 0000003c: <SaveGenerator>: <Addr8: 4>  # Address: 00000040
==> 0000003e: <Ret>: <Reg8: 1>
==> 00000040: <ResumeGenerator>: <Reg8: 1, Reg8: 2>
==> 00000043: <Mov>: <Reg8: 4, Reg8: 2>
==> 00000046: <Mov>: <Reg8: 2, Reg8: 1>
==> 00000049: <JmpFalse>: <Addr8: 38, Reg8: 4>  # Address: 0000006f
==> 0000004c: <CompleteGenerator>: <>
==> 0000004d: <Ret>: <Reg8: 1>
==> 0000004f: <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 0>
==> 00000053: <GetById>: <Reg8: 4, Reg8: 5, UInt8: 4, string_id: 17625>  # String: 'getMethod' (Identifier)
==> 00000059: <LoadFromEnvironment>: <Reg8: 1, Reg8: 3, UInt8: 5>
==> 0000005d: <Call2>: <Reg8: 1, Reg8: 4, Reg8: 5, Reg8: 1>
==> 00000062: <SaveGenerator>: <Addr8: 4>  # Address: 00000066
==> 00000064: <Ret>: <Reg8: 1>
==> 00000066: <ResumeGenerator>: <Reg8: 1, Reg8: 4>
==> 00000069: <Mov>: <Reg8: 2, Reg8: 1>
==> 0000006c: <JmpTrue>: <Addr8: 29, Reg8: 4>  # Address: 00000089
==> 0000006f: <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 1>
==> 00000073: <GetByIdShort>: <Reg8: 4, Reg8: 4, UInt8: 5, string_id: 93>  # String: 'current' (Identifier)
==> 00000078: <JmpFalse>: <Addr8: 14, Reg8: 4>  # Address: 00000086
==> 0000007b: <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 2>
==> 0000007f: <LoadConstUndefined>: <Reg8: 3>
==> 00000081: <Call2>: <Reg8: 3, Reg8: 4, Reg8: 3, Reg8: 2>
==> 00000086: <CompleteGenerator>: <>
==> 00000087: <Ret>: <Reg8: 2>
==> 00000089: <CompleteGenerator>: <>
==> 0000008a: <Ret>: <Reg8: 1>
==> 0000008c: <CompleteGenerator>: <>
==> 0000008d: <Ret>: <Reg8: 0>
"""


def _code_2() -> str:
    js = Decompiler.render(Decompiler.build_context(_HASM_2, 6777, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in js.splitlines() if not line.strip().startswith("//"))


def test_resume_pair_followed_by_copies_is_folded_away():
    code = _code_2()

    assert "goto" not in code
    assert "__resumeIsReturn" not in code
    assert "await yield" not in code


def test_each_arm_binds_the_resumed_value_to_the_register_the_rest_reads():
    code = _code_2()

    # The `Mov r2, r1` copy is folded into the await that produced the value.
    assert "r2 = await r5.getMethod(r1);" in code
    assert "r2 = await r2.getMethod();" in code
    assert code.rstrip().endswith("return r2;\n}")


# ----------------------------------------------------------------------------------------------------
# generator_yield_array
#
# `yield [key, value]` folds: the array is filled after it is created, the cut moves behind the last store (F-12, 98/9674).
#
#     r7 = [env[1][1]]              // NewArray + DefineOwnInDenseArray
#     r5 = env[1][0][env[1][1]]     // the element's own computation sits between the stores
#     r7[1] = r5                    // DefineOwnInDenseArray
#     r5 = 1; env[2] = r5           // protocol
#
# The cut was put at the `NewArray`, so the stores and loads behind it counted as unrecognized protocol and the
# whole dispatch stayed raw.
# ----------------------------------------------------------------------------------------------------

def _render_3() -> str:
    sections = [
        (1720, (_DATA / "generator_yield_array_98_9674_creator.hasm").read_text(encoding="utf-8")),
        (9674, (_DATA / "generator_yield_array_98_9674.hasm").read_text(encoding="utf-8")),
    ]
    tables = BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()

    return Decompiler.render(Decompiler.build_context(sections[1][1], 9674, batch_tables=tables), verbose=False)


def test_the_array_is_built_and_yielded():
    code = _render_3()

    assert "goto" not in code
    assert "yield r7;" in code
    assert "r7[1] = r5;" in code
    assert code.index("r7[1] = r5;") < code.index("yield r7;")
    assert "for (; r7 < r5; )" in code


# ----------------------------------------------------------------------------------------------------
# generator_yield_in_loop_entry
#
# A generator whose `yield` sits in a loop entered by two tests folds into a `for` (F-12, 98/9673 `createKeyIterator`).
#
#     r7 = env[1][1]            // the yielded value, computed BEFORE the resume point's constant load
#     r5 = 1                    // resume point
#     env[2] = r5               // protocol
#
# The constant load between the value and the suspend was an "unrecognized instruction" and the whole dispatch
# stayed raw. Folded, the loop body (entered by the first test and by the latch) has to precede the `return` the
# first test falls into; without a bridge block behind the branch the structurer read the wrong arm and printed
# `if (r7 >= r5) { for ... }` around the loop (the loop never ran).
# ----------------------------------------------------------------------------------------------------

def _render_4() -> str:
    sections = [
        (1719, (_DATA / "generator_loop_yield_98_9673_creator.hasm").read_text(encoding="utf-8")),
        (9673, (_DATA / "generator_loop_yield_98_9673.hasm").read_text(encoding="utf-8")),
    ]
    tables = BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()

    return Decompiler.render(Decompiler.build_context(sections[1][1], 9673, batch_tables=tables), verbose=False)


def test_the_loop_runs_and_yields():
    code = _render_4()

    assert "goto" not in code
    assert "yield r1[1][1];" in code
    assert "if (r7 >= r5)" not in code
    assert "for (; r7 < r5; )" in code
    # the exhausted result comes after the loop, not inside the `if`
    assert code.index("for (") < code.index('"done": true')


# ----------------------------------------------------------------------------------------------------
# inlined_resume_value_after_an_await
#
# A resumed value read by a consumer that inlined it keeps its binding (96/6672, `Asset.downloadAsync`).
#
# `this.localUri = await downloadAsync(...)`: the compiler stores the resumed register straight into the property, so
# the consumer's value was the resume placeholder (`await yield`, not valid JavaScript) and nothing named the
# register, which made the fold believe the resumed value was never read and print `await call();` + `await yield`.
# ----------------------------------------------------------------------------------------------------

def _render_5() -> str:
    hasm = (_DATA / "inlined_resume_value_read_after_an_await_96_6672.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_placeholder_is_printed():
    assert "await yield" not in _render_5()


def test_the_awaited_value_is_bound_and_stored():
    out = _render_5()

    assert "r3 = await r8(this.uri, this.hash, this.type);\n            this.localUri = r3;" in out


# ----------------------------------------------------------------------------------------------------
# resumed_value_copied_into_an_object_literal
#
# A resumed value that an object literal copied keeps its binding (96/12207, a lazy image `{ src: <resumed> }`).
#
# The literal is built from the resume placeholder (`await yield`, not valid JavaScript); the fold only rewrote the
# placeholder object itself, not the copy inside the literal. Every placeholder now carries the address of its own
# `ResumeGenerator`, so a copy is found without reaching the placeholder of the next resume point.
# ----------------------------------------------------------------------------------------------------

def _render_6() -> str:
    hasm = (_DATA / "resumed_value_copied_into_an_object_literal_96_12207.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_placeholder_is_printed_2():
    assert "await yield" not in _render_6()


def test_the_literal_reads_the_bound_register():
    out = _render_6()

    assert "r1 = yield r2[1];" in out
    assert '{ "src": r1 }' in out


# ----------------------------------------------------------------------------------------------------
# return_await_inside_a_try
#
# `return await x;` inside a `try` of an async function prints without the second suspend (F-312, 96/12653).
#
# The function suspends twice: once for `await r4.json()` and once more before it leaves the `try` with the value. The
# second pair left the resume placeholder (`r3 = await yield;`, not valid JavaScript) in the `try` and an `if
# (__resumeIsReturn) { return r3; } else { return r3; }` behind it. Both arms return the same register, so the guard
# decides nothing: the placeholder, the flag and the guard go and `return r3;` stands behind the `try`.
# ----------------------------------------------------------------------------------------------------

def _render_7() -> str:
    hasm = (_DATA / "return_await_inside_a_try_96_12653.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_second_suspend_and_its_guard_are_gone():
    out = _render_7()

    assert "await yield" not in out
    assert "__resumeIsReturn" not in out
    assert "r3 = await r4.json();\n        } catch (caughtException) {" in out
    assert "        }\n        return r3;\n    } else {" in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_7(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    # `getEnvironment`-style helper names are plain identifiers, the file only has to parse
    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# test_before_await_suspend
#
# The `Ret` behind a `SaveGenerator` is not a handler for the register guard of a test chain (96/6029 `_anon_0`).
#
#     if (prev && prev.height === this._frame.height) skip;   // the second test's setup reads/writes r1
#     await this._updateBottomIfNecessary();                   // SaveGenerator; Ret r1  (no CFG predecessor)
#
# `_handlers()` took every block without a predecessor for a handler that may read any register, and the
# suspend's `Ret r1` read `r1`, which the test also writes, so the fold of the second test gave up and left a `goto`.
# That `Ret` runs right after the save and reads what the call before it computed.
# ----------------------------------------------------------------------------------------------------

def test_the_height_test_is_one_condition_before_the_await():
    hasm = (_DATA / "test_before_await_suspend_96_6029.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 6029, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (!r1 || r1.height !== r2[0]._frame.height) {" in out
    assert out.index("await r3._updateBottomIfNecessary();") > out.index("if (!r1 || r1.height")


# ----------------------------------------------------------------------------------------------------
# yield_in_try_with_finally_copy
#
# A `yield` inside a `try` whose `finally` is copied onto the return and the throw paths prints as a `yield`, with the
# right value in each copy (F-312, 96/8059).
#
# `Save/Ret` then `ResumeGenerator` and `JmpTrue <isReturn>`: the guard's return arm is not just a `Ret`, it runs the
# copy of the cleanup first, so the state-machine pass did not fold the pair and `await yield` was left behind (invalid
# JavaScript). The test of the flag stays, the yield folds.
#
# Two reads were wrong behind that:
# - `Mov r2, r1` (the resumed value) sits in the arm the jump falls into, which ends in a `Ret`; the arm the jump goes
#   to (and the `catch`) read `r2` as it was before, `undefined`, not the resumed value;
# - the `Mov r6, r2` copy of that `undefined` shared the literal node of `r4 = undefined`, so the merge repair followed
#   it by identity and made `return undefined` read `r6`.
# ----------------------------------------------------------------------------------------------------

def _render_8() -> str:
    hasm = (_DATA / "yield_in_try_with_finally_copy_96_8059.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_yield_is_folded():
    out = _render_8()

    assert "await yield" not in out
    assert "r1 = yield r3[0];" in out


def test_each_copy_reads_its_own_value():
    out = _render_8()

    # the return arm and the catch hold `undefined`; only the arm the jump falls into holds the resumed value
    assert out.count("[true, undefined]") == 2
    assert out.count("[true, r1]") == 1
    assert "return undefined;" in out
    assert "return r6" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_2(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_8(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# yield_value_earlier_block
#
# The yielded value may be computed in an earlier block than the suspend (F-231, 98/14158 `loadIcon`).
#
#     r7 = env[1];  if (!r7) goto DONE;  r5 = r7 instanceof Promise;  if (r5) goto SUSPEND;  ...
#     SUSPEND: r5 = 1; env[2] = r5; env[3] = r5; r5 = { value: null, done: false }; r5.value = r7; return r5
#
# `GeneratorStateDispatchCfgPass` looked for the definition of the value register inside the suspend block only,
# found none, and left the raw state machine (reentrancy guard, mode switch and all). A block that is nothing but
# the protocol (constant loads, stores, the result object) now suspends on the register by name (`await r7`; `yield r7` when only the creator is in the set, as here).
# ----------------------------------------------------------------------------------------------------

def _render_9() -> str:
    sections = [
        (13879, (_DATA / "yield_value_earlier_block_98_13879_creator.hasm").read_text(encoding="utf-8")),
        (14158, (_DATA / "yield_value_earlier_block_98_14158.hasm").read_text(encoding="utf-8")),
    ]
    tables = BatchPipeline([
        CreatorTableStage(), EnvironmentOriginTableStage(), PrivateNameTableStage(), ClassEnvironmentTableStage(),
    ]).run(BatchContext(sections=sections)).to_batch_tables()
    out = Decompiler.render(Decompiler.build_context(sections[1][1], 14158, batch_tables=tables), verbose=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_state_machine_becomes_a_suspend():
    code = _render_9()

    assert "goto" not in code
    assert "yield r7;" in code or "await r7;" in code
    assert "throwTypeError" not in code
