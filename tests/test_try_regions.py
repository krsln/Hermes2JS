"""`try`/`catch`/`finally` regions: exits, merges, copies, boundaries.

Merged from: test_catch_merge_if, test_cfg_exception_handler_merge, test_finally_copies_after_an_await, test_merged_try_gap_exits, test_try_boundary_member_read, test_try_exit_catch_fallthrough, test_try_exit_into_switch, test_try_exit_to_emptied_finally_copy, test_try_exit_to_if_join, test_try_finally_reinterpretation, test_try_finally_with_branching_copy, test_try_inside_guard, test_try_return_beside_catch_jump.
"""

from __future__ import annotations

import copy
import itertools
import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.analysis.cfg.CFGBuilder import CFGBuilder


# ----------------------------------------------------------------------------------------------------
# catch_merge_if
#
# A test the try body and the catch both run into ends the catch, it is not part of it (F-188).
#
#     try { r2 = f() } catch (e) { r2 = false }   if (!r2) { g() }   return
#
# The test is the merge block of the handler: the try body reaches it by a `Jmp`, the catch by falling through. Once
# the `IfStructurer` turned it into an `IfRegion` its emptied block was gone from the tree and `_find_catch_boundary`
# (which looks for that block) ran on: the `if` and the `return` were printed inside the catch, and the try body
# kept a `goto` to where the test used to be. `IfRegion.source_block` remembers the block.
#
# Not for a test only the catch reaches (`catch (e) { if (it) it.return(); throw e }`, tests/test_arm_absorb.py).
#
#     98/171 `polyfill`
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_test_after_the_try_catch_is_not_part_of_the_catch():
    out = _render("catch_merge_if_98_171.hasm", 171)

    assert "goto" not in out
    assert "    } catch (caughtException) {\n        r2 = false;\n    }\n    if (!r2) {" in out


# ----------------------------------------------------------------------------------------------------
# cfg_exception_handler_merge
#
# Unit tests for `CFGBuilder._merge_fragmented_handlers`.
#
# Hermes records one try body as SEVERAL exception-table entries whenever
# the body's instruction stream is interrupted by something the handler
# must not cover (a `Jmp` over a conditional throw, a generator/async
# suspend point). `TryStructurer` must see those fragments as ONE handler,
# otherwise it builds a second try/catch against a handler block the first
# one already relocated (scrambled output).
#
# The merge is grouped by TARGET and gated only by "is the gap clear of
# every other handler's boundary" - never by position in the sorted table.
# The tables below are real ones from `apps/demo/fixtures/{96,98}`; the
# function they come from is named in each test.
# ----------------------------------------------------------------------------------------------------

def h(start: int, end: int, target: int) -> dict:
    return {"start": start, "end": end, "target": target}


def merge(*entries: dict) -> list[dict]:
    return CFGBuilder._merge_fragmented_handlers(list(entries))


def triples(handlers: list[dict]) -> list[tuple[int, int, int]]:
    return sorted((x["start"], x["end"], x["target"]) for x in handlers)


def test_empty_table():
    assert CFGBuilder._merge_fragmented_handlers([]) == []


def test_single_handler_untouched():
    assert triples(merge(h(0x16, 0x45, 0x45))) == [(0x16, 0x45, 0x45)]


def test_contiguous_fragments_merge():
    # hbc96 tryCatchInsideLoopTest: `Jmp` over a conditional throw.
    merged = merge(h(0x3A, 0x63, 0x85), h(0x65, 0x85, 0x85))
    assert triples(merged) == [(0x3A, 0x85, 0x85)]


def test_long_fragment_chain_collapses_to_one():
    # hbc98 asyncTryCatchTest: one fragment per await/suspend point.
    merged = merge(
        h(0x4B, 0xD3, 0x1B6),
        h(0xDF, 0x12B, 0x1B6),
        h(0x133, 0x18E, 0x1B6),
        h(0x19A, 0x1A1, 0x1B6),
        h(0x1AD, 0x1B6, 0x1B6),
    )
    assert triples(merged) == [(0x4B, 0x1B6, 0x1B6)]


def test_fragments_separated_by_a_wider_other_target_handler_still_merge():
    # hbc96 asyncTryCatchTest (section 15181). The finally-wrapper
    # [0x20, 0x76)->0xd0 sorts BETWEEN the two 0x8d fragments; an
    # adjacency-based merge never saw them as neighbours and left the
    # catch split in two, scrambling the whole function.
    merged = merge(
        h(0x20, 0x54, 0x8D),
        h(0x56, 0x76, 0x8D),
        h(0x20, 0x76, 0xD0),
        h(0x8D, 0xA3, 0xD0),
    )
    assert triples(merged) == [(0x20, 0x76, 0x8D), (0x20, 0xA3, 0xD0)]


# hbc96 parseBoxShadowString (#1133): a for-of whose body is full of
# `continue`s. BOTH the catch (0x1d2) and its finally-wrapper (0x217) are
# fragmented, and each one's fragment edges fall inside the other's gaps.
# A single merge pass sees the wrapper's edges as "foreign boundaries" in
# the catch's gaps and leaves six catch fragments unmerged (each one then
# silently skipped by `TryStructurer`); the merge has to iterate.
PARSE_BOX_SHADOW = [
    h(0xB5, 0xED, 0x1D2),
    h(0xF9, 0x113, 0x1D2),
    h(0x11F, 0x139, 0x1D2),
    h(0x145, 0x156, 0x1D2),
    h(0x162, 0x16B, 0x1D2),
    h(0x170, 0x18F, 0x1D2),
    h(0x1A0, 0x1C1, 0x1D2),
    h(0x77, 0xF0, 0x217),
    h(0xF9, 0x116, 0x217),
    h(0x11F, 0x13C, 0x217),
    h(0x145, 0x159, 0x217),
    h(0x162, 0x197, 0x217),
    h(0x1A0, 0x1C9, 0x217),
    h(0x1D2, 0x209, 0x217),
]


def test_fragmented_catch_inside_fragmented_finally_wrapper():
    merged = merge(*PARSE_BOX_SHADOW)
    assert triples(merged) == [(0x77, 0x209, 0x217), (0xB5, 0x1C1, 0x1D2)]


def test_nested_try_catch_finally_table_from_15082():
    merged = merge(
        h(0x16, 0x4A, 0x4A),
        h(0x16, 0x60, 0x8A),
        h(0x16, 0x88, 0xA2),
        h(0x8A, 0xA2, 0xA2),
        h(0x16, 0xB8, 0xE4),
    )
    assert triples(merged) == [
        (0x16, 0x4A, 0x4A),
        (0x16, 0x60, 0x8A),
        (0x16, 0xA2, 0xA2),
        (0x16, 0xB8, 0xE4),
    ]


def test_shadowed_duplicate_range_is_folded_into_neighbour():
    # hbc96 tryCatchFinallyImplicitThrowTest: same range, different
    # targets, then a same-target continuation past a clear gap.
    merged = merge(h(0x19, 0x3F, 0x55), h(0x19, 0x3F, 0x87), h(0x55, 0x6B, 0x87))
    assert triples(merged) == [(0x19, 0x3F, 0x55), (0x19, 0x6B, 0x87)]


def test_gap_with_foreign_boundary_is_not_merged():
    # hbc98 nestedArrayDestructureTest: nested handlers sit INSIDE the
    # gap between the two 0x20a fragments; they are two distinct
    # protected regions that merely share a handler.
    table = [
        h(0x62, 0xA8, 0x215),
        h(0xDD, 0x11B, 0x20A),
        h(0x15B, 0x15D, 0x1F6),
        h(0x18F, 0x196, 0x196),
        h(0x1BD, 0x1C1, 0x1C7),
        h(0x203, 0x20A, 0x20A),
    ]
    assert triples(merge(*table)) == triples(table)


def test_other_target_handler_ending_inside_gap_blocks_merge():
    merged = merge(h(0, 10, 100), h(0, 12, 200), h(20, 30, 100))
    assert triples(merged) == [(0, 10, 100), (0, 12, 200), (20, 30, 100)]


def test_other_target_handler_exactly_filling_the_gap_blocks_merge():
    # Both of its boundaries lie ON the gap's edges, so a plain
    # "boundary strictly inside" test cannot see it.
    merged = merge(h(0, 10, 100), h(10, 20, 200), h(20, 30, 100))
    assert triples(merged) == [(0, 10, 100), (10, 20, 200), (20, 30, 100)]


def test_different_targets_never_merge_even_when_adjacent():
    merged = merge(h(0, 10, 100), h(10, 20, 200))
    assert triples(merged) == [(0, 10, 100), (10, 20, 200)]


def test_overlapping_same_target_ranges_union():
    merged = merge(h(0, 10, 100), h(5, 20, 100))
    assert triples(merged) == [(0, 20, 100)]


def test_input_is_not_mutated():
    table = [h(0x20, 0x54, 0x8D), h(0x56, 0x76, 0x8D), h(0x20, 0x76, 0xD0)]
    snapshot = copy.deepcopy(table)
    CFGBuilder._merge_fragmented_handlers(table)
    assert table == snapshot


@pytest.mark.parametrize(
    "table",
    [
        [h(0x20, 0x54, 0x8D), h(0x56, 0x76, 0x8D), h(0x20, 0x76, 0xD0), h(0x8D, 0xA3, 0xD0)],
        [h(0x16, 0x4A, 0x4A), h(0x16, 0x60, 0x8A), h(0x16, 0x88, 0xA2), h(0x8A, 0xA2, 0xA2), h(0x16, 0xB8, 0xE4)],
    ],
    ids=["asyncTryCatch-15181", "nestedTryCatchFinally-15082"],
)
def test_result_is_independent_of_input_order(table):
    expected = triples(CFGBuilder._merge_fragmented_handlers(list(table)))

    for perm in itertools.permutations(table):
        assert triples(CFGBuilder._merge_fragmented_handlers(list(perm))) == expected


def test_large_table_is_independent_of_input_order():
    # Too big to permute exhaustively; a fixed set of shuffles is enough.
    import random

    expected = triples(CFGBuilder._merge_fragmented_handlers(list(PARSE_BOX_SHADOW)))
    rng = random.Random(1133)

    for _ in range(50):
        shuffled = list(PARSE_BOX_SHADOW)
        rng.shuffle(shuffled)
        assert triples(CFGBuilder._merge_fragmented_handlers(shuffled)) == expected


def test_identical_ranges_keep_table_order():
    # Hermes matches entries in listed order, so of two identical ranges
    # the first-listed is the one that ever fires. TryStructurer's dedup
    # keeps the first it sees - the merge must not reorder them.
    merged = merge(h(0, 10, 200), h(0, 10, 100))
    assert [(x["start"], x["end"], x["target"]) for x in merged] == [(0, 10, 200), (0, 10, 100)]

    merged = merge(h(0, 10, 100), h(0, 10, 200))
    assert [(x["start"], x["end"], x["target"]) for x in merged] == [(0, 10, 100), (0, 10, 200)]


@pytest.mark.parametrize(
    "table",
    [
        PARSE_BOX_SHADOW,
        [h(0x20, 0x54, 0x8D), h(0x56, 0x76, 0x8D), h(0x20, 0x76, 0xD0), h(0x8D, 0xA3, 0xD0)],
        [h(0x62, 0xA8, 0x215), h(0xDD, 0x11B, 0x20A), h(0x15B, 0x15D, 0x1F6),
         h(0x18F, 0x196, 0x196), h(0x1BD, 0x1C1, 0x1C7), h(0x203, 0x20A, 0x20A)],
    ],
    ids=["parseBoxShadow-1133", "asyncTryCatch-15181", "nestedArrayDestructure-9487"],
)
def test_merge_never_loses_protection_and_never_grows_the_table(table):
    merged = CFGBuilder._merge_fragmented_handlers(list(table))

    assert len(merged) <= len(table)

    # Every original range is still covered by a merged range that has
    # the same target: merging may only widen protection, never drop it.
    for raw in table:
        assert any(
            m["target"] == raw["target"] and m["start"] <= raw["start"] and m["end"] >= raw["end"]
            for m in merged
        ), raw

    # Idempotent: merging an already-merged table changes nothing.
    assert triples(CFGBuilder._merge_fragmented_handlers(merged)) == triples(merged)


# ----------------------------------------------------------------------------------------------------
# finally_copies_after_an_await
#
# `try { return await x; } finally { cleanup }` in an async function prints without the resume placeholders (F-312,
# 96/14945).
#
# Two things were left behind: (1) the entry resume's guard came as `if (!__resumeIsReturn) { body } else { return r0 }`
# (the structurer made the larger arm the `then`), the state-machine pass only knew the pad as the `then` arm, so
# `r0 = await yield;` stayed on top; (2) behind the `try` the guard of the second suspend has two arms that both run
# the copy of the `finally` body and `return r1;`, so the placeholder `r1 = await yield;` stayed in the `try`. The arms
# are the same code, so one copy stays behind the `try`.
# ----------------------------------------------------------------------------------------------------

def _render_2() -> str:
    hasm = (_DATA / "finally_copies_after_an_await_96_14945.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_resume_placeholder_or_guard_is_left():
    out = _render_2()

    assert "await yield" not in out
    assert "__resumeIsReturn" not in out
    assert out.count("return r1;") == 2  # the `finally` body ends in an `if`, each of its arms returns


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_2(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# merged_try_gap_exits
#
# Exits that sit in the gaps of a merged try range are not protected (F-168).
#
# A `for-of` body is protected by several table entries; between them lie the exits (`it.return();
# r0 = []; return r0`), which Hermes keeps OUT of the range. `CFGBuilder` merges the pieces into one range
# spanning the gaps, so `SharedReturnDuplicationCfgPass` treated the exits as inside a try and left the shared
# ones alone: every jump to them printed as `goto label_N` and the exit bodies were printed after the loop,
# where normal completion falls into them. The merged entry now keeps its `fragments`, and only a block that
# overlaps one of them is protected.
#
#     96/1324  `parseBackgroundRepeatCSSString`
#     96/1330  `parseBackgroundSizeCSSString`
# ----------------------------------------------------------------------------------------------------

def test_the_shared_exits_are_copied_into_their_branches():
    out = _render("merged_try_gap_exits_96_1324.hasm", 1324)

    assert "goto" not in out
    assert out.count("return r24;") == 5 and out.count("return r1;") == 2
    assert out.rstrip().endswith("return r0;\n}")


def test_nothing_exits_after_the_loop_but_the_normal_return():
    out = _render("merged_try_gap_exits_96_1330.hasm", 1330)

    assert "goto" not in out
    assert ".return()" not in out and "GetIterator" not in out
    assert out.rstrip().split("\n")[-2].strip().startswith("return")


# ----------------------------------------------------------------------------------------------------
# try_boundary_member_read
#
# A member read made inside a `try` stays there (F-33, 98/13768).
#
#     try { x = param1.aborted } catch { return false }
#     return typeof x === "boolean"
#
# compiles to a `GetById` inside the handler's range and a `TypeOfIs` after it. The read was folded into
# the `TypeOfIs`, which printed `typeof param1.aborted` OUTSIDE the `try` and left `try { } catch` empty: a
# getter (or `undefined`) that throws would no longer reach the `catch`. A read that can throw is now
# named by its register where the reader stands outside the range.
#
# Generator/async bodies are exempt: their state machine wraps the body in one synthetic `try`, and
# the golden outputs of `generatorWithLoopTest` / `simpleAsyncTest` / `asyncLoopTest` (98) guard that.
# ----------------------------------------------------------------------------------------------------

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


# ----------------------------------------------------------------------------------------------------
# try_exit_catch_fallthrough
#
# A `catch` that swallows some errors falls out into the code after the `try` (F-213, 98/6705 `getLayoutNode`).
#
#     try { ...; if (r0 == null) r0 = r1; r1 = r0 } catch (e) { if (e instanceof Error && !match) throw e }
#     if (r6) { ... }
#
# The `try` body jumps to the same `if (r6)` the catch falls into. Three things were wrong:
# the catch's own guard took that code as its `then` arm (the `try` body then needed a `goto` into it),
# the catch swallowed it when the `try` was built (it has no post-dominator because the catch can throw),
# and `r1 = r0` after the arm `if (r0 == null) r0 = r1` printed `r1 = r1`, which is no statement at all.
# ----------------------------------------------------------------------------------------------------

def _code_2():
    hasm = (_DATA / "try_exit_catch_fallthrough_98_6705.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 6705, strict=False), verbose=False, raw=False)
    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_try_body_needs_no_goto():
    assert "goto" not in _code_2()


def test_the_code_after_the_try_follows_the_catch():
    code = _code_2()

    assert "        }\n        if (r6) {" in code
    assert code.count("if (r6) {") == 1


def test_the_join_copy_is_kept_in_the_try_body():
    assert "            r1 = r0;\n        } catch" in _code_2()


# ----------------------------------------------------------------------------------------------------
# try_exit_into_switch
#
# `try { ...; } catch {}` at the end of an `if`, with a `switch` behind it: the try's own jump is no `goto` (98/2636).
#
# `commitDeletionEffectsOnFiber`: `if (hook && typeof hook.onCommitFiberUnmount === "function") { try { ... } catch {} }`
# and then `switch (param3.tag)`. The try body ends in a jump over the handler to the switch's header block. The next
# statement being a `switch` (a compound region whose header block the tree no longer holds), `RedundantJumpRegionPass`
# could not say where control resumes and left `goto label_47`.
# ----------------------------------------------------------------------------------------------------

def test_the_jump_over_the_handler_into_the_switch_is_dropped():
    hasm = (_DATA / "try_exit_into_switch_98_2636.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2636, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "} catch (caughtException) {\n        }\n    }\n    switch (param3.tag) {" in code


# ----------------------------------------------------------------------------------------------------
# try_exit_to_emptied_finally_copy
#
# A try body's jump to the finally copy it ends in is dropped once the copy is gone (F-164).
#
#     try { ...; jmp COPY } catch { ... }   COPY: <finally copy>; ret
#
# `_FinallyAttacher` strips the copy and the emptied block is pruned, so the jump named an address no sibling had
# any more and printed as `goto label_66` right before the `catch`. A target that is an emptied block running on
# into the exit address is the exit.
#
#     96/4085  `flush`
# ----------------------------------------------------------------------------------------------------

def test_the_try_body_ends_without_a_goto():
    hasm = (_DATA / "try_exit_to_emptied_finally_copy_96_4085.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 4085, strict=False), verbose=False, raw=False)
    out = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in out
    assert out.count("finally {") == 1
    assert out.index("r3 = r5.enqueue(r3);") < out.index("} catch")


# ----------------------------------------------------------------------------------------------------
# try_exit_to_if_join
#
# A try body's jump to a join that is itself an `if` is dropped (F-165).
#
#     if (a) { if (b) { try { ...; jmp JOIN } catch { ... } } }   JOIN: if (r0) ... else ...
#
# `_next_fallthrough_address` only resolved a plain block as the next sibling and gave up when the try sat in an
# `if` arm or the join was an `if`, so the jump printed as `goto label_56`. Arms resume where their `if` does, and
# an `if` sibling starts at the test block its condition swallowed.
#
#     96/331  `function_331`
# ----------------------------------------------------------------------------------------------------

def test_the_try_body_ends_without_a_goto_2():
    hasm = (_DATA / "try_exit_to_if_join_96_331.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 331, strict=False), verbose=False, raw=False)
    out = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in out
    assert out.index("r0 = r2;") < out.index("} catch")
    assert out.index("} catch") < out.index("if (r0) {")


# ----------------------------------------------------------------------------------------------------
# try_finally_reinterpretation
#
# Tests for `_FinallyAttacher.maybe_reinterpret_as_finally` and the
# `ForEachRegionPass` iterator-close recognition that depends on it.
#
# A handler `catch (e) { B; throw e }` and a `finally { B }` compile to the
# same handler table and handler block; only the try body differs (Hermes
# inlines a copy of a `finally` body at every normal exit). Rewriting a real
# catch-and-rethrow as `finally` runs B on the success path - it must only
# happen with evidence that the source was a `finally`.
# ----------------------------------------------------------------------------------------------------

FIXTURES = Path(__file__).resolve().parents[1] / "apps" / "demo" / "fixtures"

# hermesc 250829098.0.14 (bytecode 98), compiled from:
#
#   function rethrowWithLog(x) {
#     try { console.log("try-body"); mayThrow(x); }
#     catch (e) { console.log("caught-and-logged"); throw e; }
#     console.log("after");
#   }
RETHROW_WITH_LOG = r"""
=> [Function #2 "rethrowWithLog" of 85 bytes]: 2 params, frame size=14, strict=0, exc handler=1, debug info=1  @ offset 0x000001d1
  [Exception handlers: [start=0x0, end=0x25, target=0x3b] ]
  [Debug offsets: source_locs=0x38, scope_desc_data=0x226]

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 3, UInt8: 1>
==> 00000003: <GetGlobalObject>: <Reg8: 1>
==> 00000005: <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 9>  # String: 'console' (Identifier)
==> 0000000b: <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 7>  # String: 'log' (Identifier)
==> 00000010: <LoadConstString>: <Reg8: 0, string_id: 5>  # String: 'try-body' (String)
==> 00000014: <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
==> 00000019: <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 10>  # String: 'mayThrow' (Identifier)
==> 0000001e: <LoadConstUndefined>: <Reg8: 0>
==> 00000020: <Call2>: <Reg8: 2, Reg8: 2, Reg8: 0, Reg8: 3>
==> 00000025: <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 9>  # String: 'console' (Identifier)
==> 0000002b: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 7>  # String: 'log' (Identifier)
==> 00000030: <LoadConstString>: <Reg8: 1, string_id: 0>  # String: 'after' (String)
==> 00000034: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
==> 00000039: <Ret>: <Reg8: 0>
==> 0000003b: <Catch>: <Reg8: 0>
==> 0000003d: <GetGlobalObject>: <Reg8: 1>
==> 0000003f: <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 9>  # String: 'console' (Identifier)
==> 00000045: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 7>  # String: 'log' (Identifier)
==> 0000004a: <LoadConstString>: <Reg8: 1, string_id: 1>  # String: 'caught-and-logged' (String)
==> 0000004e: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
==> 00000053: <Throw>: <Reg8: 0>


"""


def render(hasm: str, index: int) -> str:
    context = Decompiler.build_context(hasm, index)
    out = Decompiler.render(context, verbose=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def render_fixture(version: str, index: int, name: str) -> str:
    hasm = (FIXTURES / version / "sections" / f"function_{index}_{name}.hasm").read_text()

    return render(hasm, index)


def test_catch_that_logs_and_rethrows_is_not_rewritten_as_finally():
    out = render(RETHROW_WITH_LOG, 2)

    assert "finally" not in out
    assert "catch" in out

    lines = [line.strip() for line in out.split("\n")]
    catch_at = next(i for i, line in enumerate(lines) if line.startswith("} catch"))

    # The logging belongs to the catch, not to the try body.
    assert any("caught-and-logged" in line for line in lines[catch_at:])
    assert not any("caught-and-logged" in line for line in lines[:catch_at])

    # KNOWN LIMITATION, deliberately not asserted either way: the code
    # after the try statement ("after") currently lands INSIDE the try
    # body, because the last protected block also holds unprotected
    # instructions and only LEADING unprotected content is split off.


def test_real_try_finally_with_inlined_copy_still_becomes_finally():
    out = render_fixture("98", 9466, "tryFinallyNormalCompletionTest")

    assert "} finally {" in out
    assert "catch" not in out
    # The inlined normal-exit copy was stripped: the finally body appears once.
    assert out.count("finally-block") == 1


def test_try_body_with_no_normal_exit_still_becomes_finally():
    # try always throws, catch always throws: no copy can exist, and
    # `catch { B; throw e }` is equivalent to `finally { B }` here.
    out = render_fixture("96", 15079, "tryCatchRethrowDifferentTest")

    assert "} finally {" in out


def test_for_of_iterator_close_catch_is_unwrapped_into_plain_for_of():
    # The iterator close reaches the structurer as a catch-and-rethrow;
    # ForEachRegionPass recognises that shape and drops the scaffolding.
    out = render_fixture("96", 15092, "forOfTest")

    assert "for (const" in out
    assert "try" not in out
    assert ".return()" not in out


# ---------------------------------------------------------------------------
# Inlined copy placed AFTER the try (a loop's `break` and its normal end
# converge on one block, so Hermes emits the finally body once, there).
# ---------------------------------------------------------------------------


def test_finally_copy_after_the_try_is_recovered_as_a_real_finally():
    # try { for (...) { if (items[i] === 0) break; ... } } finally { F }
    out = render_fixture("98", 9472, "tryFinallyLoopBreakTest")

    assert "} finally {" in out
    assert "catch" not in out

    # F runs once, in the finally clause - the copy after the try is gone -
    # and the code that followed it is still there, after the try.
    assert out.count("finally-block") == 1
    assert out.index("finally-block") < out.index("/end")


# hermesc 250829098.0.14 (bytecode 98), compiled from:
#
#   function sharedTail(x, y) {
#     if (y) {
#       try { console.log("a"); mayThrow(x); }
#       catch (e) { console.log("dup"); throw e; }
#     }
#     console.log("dup");
#     console.log("rest");
#   }
#
# The code after the try starts with the same statement as the catch body,
# but that block is also reachable when `y` is false, i.e. without passing
# through the try: its first statement is not a finally copy.
SHARED_TAIL = r"""
=> [Function #2 "sharedTail" of 115 bytes]: 3 params, frame size=14, strict=0, exc handler=1, debug info=1  @ offset 0x000001f2
  [Exception handlers: [start=0x6, end=0x2b, target=0x59] ]
  [Debug offsets: source_locs=0x44, scope_desc_data=0x265]

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 0, UInt8: 2>
==> 00000003: <JmpFalse>: <Addr8: 40, Reg8: 0>  # Address: 0000002b
==> 00000006: <LoadParam>: <Reg8: 2, UInt8: 1>
==> 00000009: <GetGlobalObject>: <Reg8: 0>
==> 0000000b: <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 00000011: <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 00000016: <LoadConstString>: <Reg8: 1, string_id: 2>  # String: 'a' (String)
==> 0000001a: <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
==> 0000001f: <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 2, string_id: 9>  # String: 'mayThrow' (Identifier)
==> 00000024: <LoadConstUndefined>: <Reg8: 0>
==> 00000026: <Call2>: <Reg8: 0, Reg8: 1, Reg8: 0, Reg8: 2>
==> 0000002b: <GetGlobalObject>: <Reg8: 0>
==> 0000002d: <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 00000033: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 00000038: <LoadConstString>: <Reg8: 1, string_id: 3>  # String: 'dup' (String)
==> 0000003c: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
==> 00000041: <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 00000047: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 0000004c: <LoadConstString>: <Reg8: 0, string_id: 4>  # String: 'rest' (String)
==> 00000050: <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
==> 00000055: <LoadConstUndefined>: <Reg8: 0>
==> 00000057: <Ret>: <Reg8: 0>
==> 00000059: <Catch>: <Reg8: 0>
==> 0000005b: <GetGlobalObject>: <Reg8: 1>
==> 0000005d: <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 00000063: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 00000068: <LoadConstString>: <Reg8: 1, string_id: 3>  # String: 'dup' (String)
==> 0000006c: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
==> 00000071: <Throw>: <Reg8: 0>


"""

# ... and:
#
#   function returnInside(x) {
#     try { if (x) { return 1; } console.log("a"); mayThrow(x); }
#     catch (e) { console.log("dup"); throw e; }
#     console.log("dup");
#     console.log("rest");
#   }
#
# A `return` in the try body carries its own inlined copy inside the try;
# the trailing-copy rule does not model that and must decline.
RETURN_INSIDE = r"""
=> [Function #3 "returnInside" of 113 bytes]: 2 params, frame size=14, strict=0, exc handler=1, debug info=1  @ offset 0x00000265
  [Exception handlers: [start=0x0, end=0x28, target=0x57] ]
  [Debug offsets: source_locs=0x7f, scope_desc_data=0x2d6]

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 3, UInt8: 1>
==> 00000003: <JmpTrue>: <Addr8: 79, Reg8: 3>  # Address: 00000052
==> 00000006: <GetGlobalObject>: <Reg8: 1>
==> 00000008: <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 0000000e: <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 00000013: <LoadConstString>: <Reg8: 0, string_id: 2>  # String: 'a' (String)
==> 00000017: <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
==> 0000001c: <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 9>  # String: 'mayThrow' (Identifier)
==> 00000021: <LoadConstUndefined>: <Reg8: 0>
==> 00000023: <Call2>: <Reg8: 2, Reg8: 2, Reg8: 0, Reg8: 3>
==> 00000028: <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 0000002e: <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 00000033: <LoadConstString>: <Reg8: 2, string_id: 3>  # String: 'dup' (String)
==> 00000037: <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
==> 0000003c: <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 00000042: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 00000047: <LoadConstString>: <Reg8: 1, string_id: 4>  # String: 'rest' (String)
==> 0000004b: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
==> 00000050: <Ret>: <Reg8: 0>
==> 00000052: <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
==> 00000055: <Ret>: <Reg8: 0>
==> 00000057: <Catch>: <Reg8: 0>
==> 00000059: <GetGlobalObject>: <Reg8: 1>
==> 0000005b: <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 00000061: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 00000066: <LoadConstString>: <Reg8: 1, string_id: 3>  # String: 'dup' (String)
==> 0000006a: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
==> 0000006f: <Throw>: <Reg8: 0>


"""


def test_trailing_copy_is_not_stripped_when_the_block_is_reachable_from_outside_the_try():
    out = render(SHARED_TAIL, 2)

    assert "finally" not in out
    assert "} catch" in out
    # Both statements survive: the one in the catch and the one after.
    assert out.count('"dup"') == 2


def test_trailing_copy_rule_declines_a_try_body_containing_a_return():
    out = render(RETURN_INSIDE, 3)

    assert "finally" not in out
    assert "} catch" in out


# ----------------------------------------------------------------------------------------------------
# try_finally_with_branching_copy
#
# A `finally` whose body branches is one `finally`, with no second copy after the try (F-274).
#
# `try { cb() } catch (e) { report(e) } finally { restore; if (a && b) { a.types = b.types } restore }` compiles
# to a handler copy that ends in a rethrow and a normal-path copy after the try. The handler's last `if` tests the
# merge block, so the span used to stop before it (a `goto` into the copy), and the copy after the try keeps its own
# temporaries (`r4 = r3; r4.types`), so it was not recognised as the same code (96/1030 `startTransition`).
# ----------------------------------------------------------------------------------------------------

def test_the_branching_finally_is_whole_and_not_repeated_after_the_try():
    hasm = (_DATA / "try_finally_branching_copy_96_1030.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 1030, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "} finally {" in out
    assert out.count("r1.types") == 1
    assert out.count(".T = r1") == 1
    assert out.rstrip().endswith("}\n}")


def test_the_try_body_does_not_jump_into_the_stripped_copy():
    """98/2068: the try body's `Jmp` names the first block of the copy that was stripped, not the block left behind."""
    hasm = (_DATA / "try_finally_branching_copy_jump_into_stripped_98_2068.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2068, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "} finally {" in out
    assert out.count(".T = r1") == 1


# ----------------------------------------------------------------------------------------------------
# try_inside_guard
#
# A `try` whose range starts behind a null guard and its setup belongs INSIDE the guard (98/2676 `flushSpawnedWork`).
#
# Bytecode: `if (r9 === null) goto END; r4 = env[2].T; r1 = env[385]; env[385] = 2; r5.T = null; <range starts> ... finally`.
# `TryStructurer` built the `try` around the whole guard `if`, so the `finally` also ran when `r9` was null and read `r4` and
# `r1`, which the setup never set. The guard's test is not protected: the `try` goes into its `then` arm, behind the setup.
# ----------------------------------------------------------------------------------------------------

def test_the_try_sits_inside_the_null_guard():
    hasm = (_DATA / "try_after_guard_setup_98_2676.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2676, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "        try {\n            if (null !== r9) {" not in code
    assert "        if (null !== r9) {\n            r5 = r2[2];\n            r4 = r5.T;" in code
    assert "            try {\n                r10 = 0;" in code


def test_default_of_a_register_written_in_a_try_inside_the_arm_still_prints():
    """96/9338 `test`: `r1 = param1; ...; if (typeof param1 === "string") { try { r1 = new SemVer(...) } catch { return false } }; r11 = r1`.

    With the `try` inside the arm, its `catch` block lies at a higher address than the `r11 = r1` read behind the
    `if`, so the repair pass took the read for one BEFORE the arm's end and dropped `r1 = param1`: the path that skips
    the arm read an `r1` nothing assigned."""
    hasm = (_DATA / "try_in_arm_keeps_default_96_9338.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 9338, strict=False), verbose=False, raw=False)

    assert "    r1 = param1;\n" in out
    assert 'if (r4 === "string") {\n            try {' in out


# ----------------------------------------------------------------------------------------------------
# try_return_beside_catch_jump
#
# A try body that ends in its own `return` keeps it when the catch ends in a jump (F-156).
#
#     try { ...; return r1; } catch { ...; goto T } finally { r3[9] = false; }
#
# `_FinallyAttacher` relocates the tail after the finally copy out of the try and keeps ONE of
# the two (catch first). The try's `return r1` was dropped, so the call result was never returned.
#
#     96/840  `preprocessException`
# ----------------------------------------------------------------------------------------------------

def test_the_try_body_still_returns_its_value():
    hasm = (_DATA / "try_return_beside_catch_jump_96_840.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 840, strict=False), verbose=False, raw=False)
    out = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    try_part = out[out.index("try {"):out.index("} catch")]

    assert "return r1;" in try_part
