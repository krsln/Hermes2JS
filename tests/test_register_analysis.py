"""Register analysis: staleness, purity, definitions, reads, memory stores.

Merged from: test_call_invalidates_member_reads, test_dangling_tool, test_flow_audit_bare_return, test_global_base_kept_when_the_register_is_overwritten, test_inert_block_printed_definitions, test_memory_store_staleness, test_printed_definition_kept, test_register_read_index_matches_the_plain_scan, test_side_effect_purity, test_side_effecting_arm_value, test_stale_inlined_read.
"""

from __future__ import annotations

import importlib
import importlib.util
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.emit.printer.ExpressionPrinter import ExpressionPrinter
from hermes_decompiler.backend.transforms.StructuralAnalyzer import StructuralAnalyzer
from hermes_decompiler.backend.transforms.shared import _repoint, has_side_effects, substitute_register
from hermes_decompiler.backend.transforms.structurers.if_structurer._predicates import is_inert_block
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.ir.Operators import LogicalOperator
from hermes_decompiler.ir.expressions import (
    BinaryExpression,
    CallExpression,
    FunctionExpression,
    Identifier,
    MemberExpression,
    NumericLiteral,
    UndefinedLiteral,
)


# ----------------------------------------------------------------------------------------------------
# call_invalidates_member_reads
#
# A call may write any property, so a member read loaded before it is not what
# the same expression reads after it (98/11177):
#
#     r8 = r5.params;  r5 = ...;  r9 = r8[k]      (not `r5.params[k]` later)
#
# A load consumed as the callee / `this` of the call being handled is exempt
# (`console.log` fetched before the argument's own call).
# ----------------------------------------------------------------------------------------------------

_HASM = """
=> [Function #11177 "" of 186 bytes]: 2 params, frame size=20, strict=1, exc handler=0, debug info=0  @ offset 0x002252ac

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 5, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 6, UInt8: 1>
==> 00000006: <GetByIdShort>: <Reg8: 8, Reg8: 6, UInt8: 0, string_id: 232>  # String: 'startsWith' (Identifier)
==> 0000000b: <LoadConstString>: <Reg8: 7, string_id: 4447>  # String: '[...' (String)
==> 0000000f: <Call2>: <Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 7>
==> 00000014: <JmpTrue>: <Addr8: 91, Reg8: 7>  # Address: 0000006f
==> 00000017: <GetByIdShort>: <Reg8: 8, Reg8: 6, UInt8: 0, string_id: 232>  # String: 'startsWith' (Identifier)
==> 0000001c: <LoadConstString>: <Reg8: 7, string_id: 1103>  # String: '[' (String)
==> 00000020: <Call2>: <Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 7>
==> 00000025: <JmpFalse>: <Addr8: 20, Reg8: 7>  # Address: 00000039
==> 00000028: <GetByIdShort>: <Reg8: 8, Reg8: 6, UInt8: 1, string_id: 135>  # String: 'endsWith' (Identifier)
==> 0000002d: <LoadConstString>: <Reg8: 7, string_id: 1218>  # String: ']' (String)
==> 00000031: <Call2>: <Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 7>
==> 00000036: <JmpTrue>: <Addr8: 5, Reg8: 7>  # Address: 0000003b
==> 00000039: <Ret>: <Reg8: 6>
==> 0000003b: <LoadFromEnvironment>: <Reg8: 7, Reg8: 5, UInt8: 0>
==> 0000003f: <GetByIdShort>: <Reg8: 9, Reg8: 7, UInt8: 2, string_id: 196>  # String: 'params' (Identifier)
==> 00000044: <LoadConstNull>: <Reg8: 2>
==> 00000046: <Eq>: <Reg8: 2, Reg8: 9, Reg8: 2>
==> 0000004a: <LoadConstUndefined>: <Reg8: 7>
==> 0000004c: <JmpTrue>: <Addr8: 27, Reg8: 2>  # Address: 00000067
==> 0000004f: <GetByIdShort>: <Reg8: 8, Reg8: 6, UInt8: 3, string_id: 120>  # String: 'slice' (Identifier)
==> 00000054: <LoadConstInt>: <Reg8: 0, Imm32: -1>
==> 0000005a: <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
==> 0000005d: <Call3>: <Reg8: 8, Reg8: 8, Reg8: 6, Reg8: 1, Reg8: 0>
==> 00000063: <GetByVal>: <Reg8: 7, Reg8: 9, Reg8: 8>
==> 00000067: <JmpTrue>: <Addr8: 6, Reg8: 7>  # Address: 0000006d
==> 0000006a: <Mov>: <Reg8: 7, Reg8: 6>
==> 0000006d: <Ret>: <Reg8: 7>
==> 0000006f: <LoadFromEnvironment>: <Reg8: 5, Reg8: 5, UInt8: 0>
==> 00000073: <GetByIdShort>: <Reg8: 8, Reg8: 5, UInt8: 2, string_id: 196>  # String: 'params' (Identifier)
==> 00000078: <LoadConstNull>: <Reg8: 2>
==> 0000007a: <Eq>: <Reg8: 4, Reg8: 8, Reg8: 2>
==> 0000007e: <LoadConstUndefined>: <Reg8: 5>
==> 00000080: <JmpTrue>: <Addr8: 50, Reg8: 4>  # Address: 000000b2
==> 00000083: <GetByIdShort>: <Reg8: 7, Reg8: 6, UInt8: 3, string_id: 120>  # String: 'slice' (Identifier)
==> 00000088: <LoadConstInt>: <Reg8: 0, Imm32: -1>
==> 0000008e: <LoadConstUInt8>: <Reg8: 1, UInt8: 4>
==> 00000091: <Call3>: <Reg8: 7, Reg8: 7, Reg8: 6, Reg8: 1, Reg8: 0>
==> 00000097: <GetByVal>: <Reg8: 9, Reg8: 8, Reg8: 7>
==> 0000009b: <Eq>: <Reg8: 2, Reg8: 9, Reg8: 2>
==> 0000009f: <LoadConstUndefined>: <Reg8: 5>
==> 000000a1: <JmpTrue>: <Addr8: 17, Reg8: 2>  # Address: 000000b2
==> 000000a4: <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 4, string_id: 167>  # String: 'join' (Identifier)
==> 000000a9: <LoadConstString>: <Reg8: 7, string_id: 503>  # String: '/' (String)
==> 000000ad: <Call2>: <Reg8: 5, Reg8: 8, Reg8: 9, Reg8: 7>
==> 000000b2: <JmpTrue>: <Addr8: 6, Reg8: 5>  # Address: 000000b8
==> 000000b5: <Mov>: <Reg8: 5, Reg8: 6>
==> 000000b8: <Ret>: <Reg8: 5>


"""


def test_member_read_before_a_call_is_named_not_reread_after_it():
    js = Decompiler.render(Decompiler.build_context(_HASM, 11177, strict=False), verbose=False, raw=False)

    assert "r8 = r5.params;" in js
    assert "r9 = r8[r7];" in js
    assert "r9 = r5.params[r7];" not in js


# ----------------------------------------------------------------------------------------------------
# dangling_tool
#
# Tests for `tests/tools/dangling.py`'s text analysis (`analyze`).
#
# The tool is a correctness proxy for decompiler output, so a bug in it shows up
# as a phantom regression (or hides a real one) in every measurement. These tests
# pin its comment/string stripping.
# ----------------------------------------------------------------------------------------------------

_TOOL = Path(__file__).resolve().parent / "tools" / "dangling.py"


@pytest.fixture(scope="module")
def dangling():
    # dangling.py reads sys.argv at import time (output path / repo root) and
    # inserts the repo root into sys.path; give it a clean argv so pytest's own
    # arguments are not mistaken for a repo path.
    saved = sys.argv
    sys.argv = ["dangling.py"]
    try:
        spec = importlib.util.spec_from_file_location("dangling_under_test", _TOOL)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    finally:
        sys.argv = saved

    return module


def test_double_slash_inside_a_string_is_not_a_comment(dangling):
    # The `//` in the URL used to be stripped as a line comment first. That
    # deleted the closing quote, and the orphaned `"` then swallowed the code
    # up to the next quote - including the real definition of r2.
    js = (
        "function f() {\n"
        '    r1 = "see https://example.com/x";\n'
        "    r2 = { a: 1 };\n"
        '    r3 = "b";\n'
        "    return r2 + r3 + r1;\n"
        "}\n"
    )

    never_defined, read_before_def = dangling.analyze(js)

    assert never_defined == set()
    assert read_before_def == set()


def test_quote_inside_a_comment_does_not_open_a_string(dangling):
    js = (
        "function f() {\n"
        "    // it's a note\n"
        "    r1 = 1;\n"
        '    r2 = "x";\n'
        "    return r1 + r2;\n"
        "}\n"
    )

    never_defined, read_before_def = dangling.analyze(js)

    assert never_defined == set()
    assert read_before_def == set()


def test_registers_mentioned_only_in_comments_are_ignored(dangling):
    js = (
        "function f() {\n"
        "    // r9 = 1;\n"
        "    /* r8 */\n"
        "    r1 = 1;\n"
        "    return r1;\n"
        "}\n"
    )

    never_defined, read_before_def = dangling.analyze(js)

    assert never_defined == set()
    assert read_before_def == set()


def test_registers_inside_strings_are_ignored(dangling):
    js = 'function f() {\n    r1 = "r7 = r8";\n    return r1;\n}\n'

    never_defined, _ = dangling.analyze(js)

    assert never_defined == set()


def test_a_genuinely_undefined_register_is_still_reported(dangling):
    # The fix must not make the tool blind: a read with no definition anywhere
    # (even next to a URL string) is still a finding.
    js = (
        "function f() {\n"
        '    r1 = "https://example.com";\n'
        "    return r1 + r5;\n"
        "}\n"
    )

    never_defined, _ = dangling.analyze(js)

    assert never_defined == {"r5"}


def test_a_read_before_its_definition_is_still_reported(dangling):
    js = "function f() {\n    r1 = r2;\n    r2 = 1;\n    return r1;\n}\n"

    never_defined, read_before_def = dangling.analyze(js)

    assert never_defined == set()
    assert read_before_def == {"r2"}


@pytest.mark.parametrize("pattern", [
    "[r8, r7, r0] = r6;",
    "[[r8, r7], , [, r0]] = r6;",
    "[r8 = 0, r7 = 0, ...r0] = r6;",
    "{ a: r8, b: r7, c: r0 } = r6;",
])
def test_destructuring_assignment_targets_count_as_definitions(dangling, pattern):
    # Nested / holey / defaulted / rest forms used to stop at the first inner
    # `]`, so their targets (r8, r7, r0) looked read-but-never-defined.
    js = f"function f() {{\n    r6 = [1];\n    {pattern}\n    console.log(r8, r7, r0);\n}}\n"

    never_defined, read_before_def = dangling.analyze(js)

    assert never_defined == set()
    assert read_before_def == set()


def test_a_register_missing_from_a_destructuring_pattern_is_still_reported(dangling):
    js = "function f() {\n    r6 = [1];\n    [[r8, r7]] = r6;\n    console.log(r8, r7, r0);\n}\n"

    never_defined, _ = dangling.analyze(js)

    assert never_defined == {"r0"}


# ----------------------------------------------------------------------------------------------------
# flow_audit_bare_return
#
# A `return undefined` block that carries its own `ReturnStatement` is still falling off the end (F-178).
#
# `flow_audit._bare_undefined_return` demanded that no instruction of the block print a statement, but the `Ret`
# instruction carries the `ReturnStatement` itself, so no `return undefined` block ever qualified and every
# `switch` whose `default` runs on into one (96/2103 `commitDeletionEffectsOnFiber`) counted a lost path. The count
# sends a function through the retries, which may then adopt a worse tree for a loss that was never one.
#
#     96/2103  the `default` body falls into the closing `return undefined`
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"


def test_falling_into_the_closing_return_is_not_a_lost_path():
    counts = []
    original = StructuralAnalyzer.build

    def build(self):
        root = original(self)
        counts.append(getattr(self.cfg, "lost_edges", None))
        return root

    StructuralAnalyzer.build = build

    try:
        hasm = (_DATA / "switch_case_fallthrough_96_2103.hasm").read_text(encoding="utf-8")
        Decompiler.render(Decompiler.build_context(hasm, 2103, strict=False), verbose=False, raw=False)
    finally:
        StructuralAnalyzer.build = original

    # every attempt, the retries too: the one that was adopted lost a path that was never lost
    assert counts and max(counts) == 0


# ----------------------------------------------------------------------------------------------------
# global_base_kept_when_the_register_is_overwritten
#
# A member of the global object keeps `globalThis` as its base (98/11768 `anonymous`).
#
# `r4 = globalThis; r8 = r4.Object; r7 = r8.entries; <r4 = default | r4 = parse(...)>; r4 = r7(r8, r4)`: the member's base
# was the very node of the printed `r4 = globalThis`, a pass that repoints the readers of that node made it `r4`, and
# the call printed `r4.Object.entries(r4)` after the arms had overwritten `r4`.
# ----------------------------------------------------------------------------------------------------

def _render() -> str:
    hasm = (_DATA / "global_base_kept_when_the_register_is_overwritten_98_11768.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_call_reads_the_global():
    out = _render()

    assert "r4 = Object.entries(r4);" in out
    assert "r4.Object" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0


# ----------------------------------------------------------------------------------------------------
# inert_block_printed_definitions
#
# `is_inert_block` lets IfStructurer look past clutter when deciding whether an
# `if` is the sole meaningful content of an arm (`a && b`, `a || b` folds). A
# definition that still PRINTS (`r2 = 1`, `r6 = r4`) is a statement later code
# may read by name, so a block holding one is not clutter: folding past it
# deletes its only definition (reverting this adds 19 path-flagged functions
# over the 96/98 bundles).
# ----------------------------------------------------------------------------------------------------

def _block_with(definition_used: bool) -> BasicBlock:
    entry = OpcodeEntry("LoadConstUInt8", "0x0", opcode="LoadConstUInt8", args="Reg8: 2, UInt8: 1")
    result = OpcodeResult(entry, value=NumericLiteral(value=1), dest_reg=2)
    result.definition_used = definition_used

    block = BasicBlock(1, 0)
    block.instructions.append(result)

    return block


def test_block_without_instructions_is_inert():
    assert is_inert_block(BasicBlock(1, 0))


def test_block_with_a_printed_definition_is_not_inert():
    assert not is_inert_block(_block_with(definition_used=False))


# ----------------------------------------------------------------------------------------------------
# memory_store_staleness
#
# A value loaded from memory is stale once a store to that location ran.
#
#     r0 = param1.x;      // load
#     param1.x = null;    // store to the same location
#     return r0;          // must still be the OLD value
#
# `ReturnValueResolutionPass` folded `return r0` back into `param1.x`, and
# `get_register_expression` inlined it into a later reader, so both read the
# value AFTER the store (the `throw r3[25]` of `processEventQueue`).
# A store to a different property, or to a deeper chain, leaves it valid.
# ----------------------------------------------------------------------------------------------------

_HEADER = """
=> [Function #1 "f" of 40 bytes]: 2 params, frame size=4, strict=1, exc handler=0, debug info=0  @ offset 0x00000000

Bytecode listing:

"""

_X = "string_id: 10143>  # String: 'x' (Identifier)"
_Y = "string_id: 10144>  # String: 'y' (Identifier)"


def _render_2(body: str) -> str:
    return Decompiler.render(Decompiler.build_context(_HEADER + body, 1), verbose=False)


def test_return_does_not_read_through_a_store_to_the_same_property():
    out = _render_2(f"""
==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <GetById>: <Reg8: 0, Reg8: 1, UInt8: 0, {_X}
==> 00000009: <LoadConstNull>: <Reg8: 2>
==> 0000000b: <PutById>: <Reg8: 1, Reg8: 2, UInt8: 0, {_X}
==> 00000011: <Ret>: <Reg8: 0>
""")

    assert "r0 = param1.x;" in out, out
    assert "return r0;" in out, out


def test_return_still_folds_across_a_store_to_another_property():
    out = _render_2(f"""
==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <GetById>: <Reg8: 0, Reg8: 1, UInt8: 0, {_X}
==> 00000009: <LoadConstNull>: <Reg8: 2>
==> 0000000b: <PutById>: <Reg8: 1, Reg8: 2, UInt8: 0, {_Y}
==> 00000011: <Ret>: <Reg8: 0>
""")

    assert "return param1.x;" in out, out


def test_a_later_reader_does_not_inline_a_load_across_the_store():
    out = _render_2(f"""
==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <GetById>: <Reg8: 0, Reg8: 1, UInt8: 0, {_X}
==> 00000009: <LoadConstNull>: <Reg8: 2>
==> 0000000b: <PutById>: <Reg8: 1, Reg8: 2, UInt8: 0, {_X}
==> 00000011: <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
==> 00000014: <Add>: <Reg8: 3, Reg8: 0, Reg8: 3>
==> 00000018: <Ret>: <Reg8: 3>
""")

    assert "r0 = param1.x;" in out, out
    assert "r0 + 1" in out, out


# ----------------------------------------------------------------------------------------------------
# printed_definition_kept
#
# A definition that PRINTS is a statement later code reads by name; nothing may
# look past it as clutter.
#
# - the printer's else-if flattening skipped a block of constant loads
#   (`r5 = undefined`) that a later `if (!r5)` reads by name;
# - `UnfoldedMergeRepairPass` refused to repair an arm write whose value object a
#   READER (`Mov r11, r5`) also held, as if it were a second definer;
# - the default `r1 = param1` an `if` condition consumed inline has to print when
#   the arm that overwrites it is skipped.
# ----------------------------------------------------------------------------------------------------

_SCROLL_TO_HASM = """
=> [Function #5704 "" of 159 bytes]: 4 params, frame size=20, strict=1, exc handler=0, debug info=0  @ offset 0x0018cc8e

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <LoadParam>: <Reg8: 2, UInt8: 2>
==> 00000006: <LoadParam>: <Reg8: 0, UInt8: 3>
==> 00000009: <TypeOf>: <Reg8: 4, Reg8: 1>
==> 0000000c: <LoadConstString>: <Reg8: 3, string_id: 7552>  # String: 'number' (Identifier)
==> 00000010: <JStrictEqual>: <Addr8: 31, Reg8: 4, Reg8: 3>  # Address: 0000002f
==> 00000014: <LoadConstUndefined>: <Reg8: 5>
==> 00000016: <LoadConstUndefined>: <Reg8: 4>
==> 00000018: <LoadConstUndefined>: <Reg8: 6>
==> 0000001a: <JmpFalse>: <Addr8: 52, Reg8: 1>  # Address: 0000004e
==> 0000001d: <GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 7>  # String: 'y' (Identifier)
==> 00000022: <GetByIdShort>: <Reg8: 5, Reg8: 1, UInt8: 2, string_id: 41>  # String: 'x' (Identifier)
==> 00000027: <GetById>: <Reg8: 6, Reg8: 1, UInt8: 3, string_id: 7210>  # String: 'animated' (Identifier)
==> 0000002d: <Jmp>: <Addr8: 33>  # Address: 0000004e
==> 0000002f: <GetGlobalObject>: <Reg8: 3>
==> 00000031: <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 4, string_id: 99>  # String: 'console' (Identifier)
==> 00000037: <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 5, string_id: 131>  # String: 'warn' (Identifier)
==> 0000003c: <LoadConstString>: <Reg8: 3, string_id: 5061>  # String: '`scrollTo(y, x, animated)` is deprecated. Use `scrollTo({x: 5, y: 5, animated: true})` instead.' (String)
==> 00000040: <Call2>: <Reg8: 3, Reg8: 7, Reg8: 8, Reg8: 3>
==> 00000045: <Mov>: <Reg8: 5, Reg8: 2>
==> 00000048: <Mov>: <Reg8: 4, Reg8: 1>
==> 0000004b: <Mov>: <Reg8: 6, Reg8: 0>
==> 0000004e: <GetEnvironment>: <Reg8: 0, UInt8: 0>
==> 00000051: <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 0>
==> 00000055: <GetById>: <Reg8: 0, Reg8: 1, UInt8: 6, string_id: 9729>  # String: 'getNativeScrollRef' (Identifier)
==> 0000005b: <Call1>: <Reg8: 3, Reg8: 0, Reg8: 1>
==> 0000005f: <LoadConstNull>: <Reg8: 0>
==> 00000061: <JEqual>: <Addr8: 58, Reg8: 3, Reg8: 0>  # Address: 0000009b
==> 00000065: <GetEnvironment>: <Reg8: 0, UInt8: 2>
==> 00000068: <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 24>
==> 0000006c: <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 7, string_id: 107>  # String: 'default' (Identifier)
==> 00000071: <GetById>: <Reg8: 1, Reg8: 2, UInt8: 8, string_id: 10037>  # String: 'scrollTo' (Identifier)
==> 00000077: <JmpTrue>: <Addr8: 5, Reg8: 5>  # Address: 0000007c
==> 0000007a: <LoadConstZero>: <Reg8: 5>
==> 0000007c: <JmpTrue>: <Addr8: 5, Reg8: 4>  # Address: 00000081
==> 0000007f: <LoadConstZero>: <Reg8: 4>
==> 00000081: <LoadConstFalse>: <Reg8: 0>
==> 00000083: <StrictNeq>: <Reg8: 9, Reg8: 6, Reg8: 0>
==> 00000087: <Mov>: <Reg8: 13, Reg8: 2>
==> 0000008a: <Mov>: <Reg8: 12, Reg8: 3>
==> 0000008d: <Mov>: <Reg8: 11, Reg8: 5>
==> 00000090: <Mov>: <Reg8: 10, Reg8: 4>
==> 00000093: <Call>: <Reg8: 0, Reg8: 1, UInt8: 5>
==> 00000097: <LoadConstUndefined>: <Reg8: 0>
==> 00000099: <Ret>: <Reg8: 0>
==> 0000009b: <LoadConstUndefined>: <Reg8: 0>
==> 0000009d: <Ret>: <Reg8: 0>
"""

_SINGLE_TOUCH_HASM = """
=> [Function #6221 "extractSingleTouch" of 77 bytes]: 2 params, frame size=7, strict=1, exc handler=0, debug info=0  @ offset 0x00198775

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <GetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 12462>  # String: 'touches' (Identifier)
==> 00000009: <GetById>: <Reg8: 4, Reg8: 1, UInt8: 2, string_id: 16944>  # String: 'changedTouches' (Identifier)
==> 0000000f: <Mov>: <Reg8: 2, Reg8: 3>
==> 00000012: <JmpFalse>: <Addr8: 14, Reg8: 2>  # Address: 00000020
==> 00000015: <GetByIdShort>: <Reg8: 5, Reg8: 3, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
==> 0000001a: <LoadConstZero>: <Reg8: 0>
==> 0000001c: <Greater>: <Reg8: 2, Reg8: 5, Reg8: 0>
==> 00000020: <Mov>: <Reg8: 0, Reg8: 4>
==> 00000023: <JmpFalse>: <Addr8: 14, Reg8: 0>  # Address: 00000031
==> 00000026: <GetByIdShort>: <Reg8: 6, Reg8: 4, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
==> 0000002b: <LoadConstZero>: <Reg8: 5>
==> 0000002d: <Greater>: <Reg8: 0, Reg8: 6, Reg8: 5>
==> 00000031: <JmpTrue>: <Addr8: 14, Reg8: 2>  # Address: 0000003f
==> 00000034: <JmpFalse>: <Addr8: 11, Reg8: 0>  # Address: 0000003f
==> 00000037: <LoadConstZero>: <Reg8: 0>
==> 00000039: <GetByVal>: <Reg8: 0, Reg8: 4, Reg8: 0>
==> 0000003d: <Jmp>: <Addr8: 14>  # Address: 0000004b
==> 0000003f: <JmpFalse>: <Addr8: 9, Reg8: 2>  # Address: 00000048
==> 00000042: <LoadConstZero>: <Reg8: 2>
==> 00000044: <GetByVal>: <Reg8: 1, Reg8: 3, Reg8: 2>
==> 00000048: <Mov>: <Reg8: 0, Reg8: 1>
==> 0000004b: <Ret>: <Reg8: 0>
"""


def _code(hasm, function_id):
    out = Decompiler.render(Decompiler.build_context(hasm, function_id), verbose=False)
    return "\n".join(line for line in out.splitlines() if not line.strip().startswith("//"))


def test_else_if_flattening_keeps_the_defaults_in_front_of_the_nested_if():
    # hermes-96 `scrollTo`: `else { r5 = undefined; r4 = undefined; r6 = undefined; if (param1) {...} }`
    code = _code(_SCROLL_TO_HASM, 5704)

    assert "} else {\n        r5 = undefined;\n        r4 = undefined;\n        r6 = undefined;\n        if (param1) {" in code


def test_arm_write_read_by_a_mov_is_printed_and_the_reader_names_the_register():
    # `if (!r5) { r5 = 0 }` then `Mov r11, r5`: the 0 used to be inlined into the
    # Mov and the arm left empty (`if (!r5) { }`).
    code = _code(_SCROLL_TO_HASM, 5704)

    assert "if (!r5) {\n            r5 = 0;\n        }" in code
    assert "r11 = r5;" in code
    assert "if (!r5) {\n        }" not in code


def test_parameter_default_printed_when_the_overwriting_arm_is_skipped():
    # hermes-96 `extractSingleTouch`: `r0 = r1` after `if (..) { r1 = r3[r2] }`
    # reads the parameter when the `if` is skipped.
    code = _code(_SINGLE_TOUCH_HASM, 6221)

    assert "r1 = param1;" in code
    assert code.index("r1 = param1;") < code.index("r0 = r1;")


# ----------------------------------------------------------------------------------------------------
# register_read_index_matches_the_plain_scan
#
# `RegisterReadIndex` answers exactly what the plain `_reads_register_by_name` scan answers.
#
# `UnfoldedMergeRepairPass` asks "does code after this `if` read the register by name?" for every write it looks at, and
# the plain scan walks the whole function each time (98/3523 `parseURL` spent 230 s of its render there). The pass now
# asks an index built once; this renders functions with the pass's question answered BOTH ways and compares each answer.
# ----------------------------------------------------------------------------------------------------

pass_module = importlib.import_module(
    "hermes_decompiler.backend.transforms.region_passes.UnfoldedMergeRepairPass"
)
_FIXTURES = (
    "folded_value_test_inside_a_loop_96_1927.hasm",
    "resumed_value_copied_into_an_object_literal_96_12207.hasm",
)


def test_every_answer_of_the_index_is_the_plain_scans(monkeypatch):
    compared = []
    original = pass_module.UnfoldedMergeRepairPass._named_after_the_if

    real_reads = _repoint.RegisterReadIndex.reads

    def recording(index, register, after_address, ignore_blocks=()):
        state.append((after_address, ignore_blocks))

        return real_reads(index, register, after_address, ignore_blocks)

    state = []

    def run(self, write, region_blocks):
        answer = original(self, write, region_blocks)
        after_address, ignored = state[-1]
        plain = _repoint._reads_register_by_name(
            self.cfg, write.dest_reg, after_address, root=self.graph.root, ignore_blocks=ignored
        )
        compared.append((answer, plain))

        return answer

    monkeypatch.setattr(_repoint.RegisterReadIndex, "reads", recording)
    monkeypatch.setattr(pass_module.UnfoldedMergeRepairPass, "_named_after_the_if", run)

    for name in _FIXTURES:
        hasm = (_DATA / name).read_text(encoding="utf-8")
        Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert compared, "the pass never asked the question"
    assert all(answer == plain for answer, plain in compared)


# ----------------------------------------------------------------------------------------------------
# side_effect_purity
#
# `has_side_effects` decides whether a fold may drop, move or make conditional
# an expression. It is deep, and it knows a few calls that are not effects.
# ----------------------------------------------------------------------------------------------------

def call(name: str, *arguments) -> CallExpression:
    return CallExpression(callee=Identifier(name=name), arguments=tuple(arguments))


def user_call(name: str, *arguments) -> CallExpression:
    # A user function is called as `f.call(this, ...)`: a member callee.
    return CallExpression(
        callee=MemberExpression(obj=Identifier(name=name), prop=Identifier(name="call")),
        arguments=tuple(arguments),
    )


def test_reads_and_literals_have_no_side_effects():
    assert not has_side_effects(Identifier(name="r1"))
    assert not has_side_effects(NumericLiteral(value=3))


def test_a_user_call_has_side_effects():
    assert has_side_effects(user_call("f", Identifier(name="r1")))


def test_environment_plumbing_and_exponentiation_are_not_effects():
    assert not has_side_effects(call("getEnvironment", NumericLiteral(value=0)))
    assert not has_side_effects(call("getParentEnvironment", NumericLiteral(value=1)))
    assert not has_side_effects(call("createEnvironment"))
    assert not has_side_effects(call("exponentiationOperator", Identifier(name="r9"), Identifier(name="r8")))


def test_a_pure_callee_is_still_an_effect_if_an_argument_is():
    assert has_side_effects(call("exponentiationOperator", user_call("f"), NumericLiteral(value=3)))


def test_other_builtins_are_effects():
    # They mutate their arguments or run user code.
    for name in ("copyDataProperties", "arraySpread", "apply", "iteratorNext"):
        assert has_side_effects(call(name, Identifier(name="r1"))), name


def test_the_check_is_deep():
    nested = BinaryExpression(
        left=Identifier(name="r1"), operator=LogicalOperator.OR, right=user_call("f")
    )

    assert has_side_effects(nested)


def test_a_function_expression_only_creates_a_value():
    fn = FunctionExpression(name="g", parameters=(), body=user_call("f"))

    assert not has_side_effects(fn)


# hbc96 function #12962 of apps/testy/96 (color-convert's Lab -> XYZ). Hermes
# computes the three `x ** 3` calls BEFORE the conditionals that use them:
#
#   r2 = exponentiationOperator(...)                 // unconditional
#   if (!(r2 > 0.008856)) r2 = (r7 - 0.138) / 7.787
#
# which is the source's `x > 0.008856 ? x ** 3 : (x - 16/116) / 7.787`. The
# call has no effect, so ConditionalExpressionRegionPass may fold it back.
LAB_TO_XYZ = r"""
=> [Function #12962 "" of 248 bytes]: 2 params, frame size=17, strict=0, exc handler=0, debug info=0  @ offset 0x002348c2

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <LoadConstZero>: <Reg8: 0>
==> 00000005: <GetByVal>: <Reg8: 3, Reg8: 1, Reg8: 0>
==> 00000009: <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
==> 0000000c: <GetByVal>: <Reg8: 2, Reg8: 1, Reg8: 0>
==> 00000010: <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
==> 00000013: <GetByVal>: <Reg8: 1, Reg8: 1, Reg8: 0>
==> 00000017: <LoadConstUInt8>: <Reg8: 0, UInt8: 16>
==> 0000001a: <Add>: <Reg8: 3, Reg8: 3, Reg8: 0>
==> 0000001e: <LoadConstUInt8>: <Reg8: 0, UInt8: 116>
==> 00000021: <Div>: <Reg8: 7, Reg8: 3, Reg8: 0>
==> 00000025: <LoadConstInt>: <Reg8: 0, Imm32: 500>
==> 0000002b: <Div>: <Reg8: 0, Reg8: 2, Reg8: 0>
==> 0000002f: <AddN>: <Reg8: 6, Reg8: 0, Reg8: 7>
==> 00000033: <LoadConstUInt8>: <Reg8: 0, UInt8: 200>
==> 00000036: <Div>: <Reg8: 0, Reg8: 1, Reg8: 0>
==> 0000003a: <SubN>: <Reg8: 4, Reg8: 7, Reg8: 0>
==> 0000003e: <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
==> 00000041: <Mov>: <Reg8: 9, Reg8: 7>
==> 00000044: <Mov>: <Reg8: 8, Reg8: 0>
==> 00000047: <CallBuiltin>: <Reg8: 2, UInt8: 49, UInt8: 3>  # Built-in function: [#49 exponentiationOperator]
==> 0000004b: <Mov>: <Reg8: 9, Reg8: 6>
==> 0000004e: <CallBuiltin>: <Reg8: 3, UInt8: 49, UInt8: 3>  # Built-in function: [#49 exponentiationOperator]
==> 00000052: <Mov>: <Reg8: 9, Reg8: 4>
==> 00000055: <CallBuiltin>: <Reg8: 1, UInt8: 49, UInt8: 3>  # Built-in function: [#49 exponentiationOperator]
==> 00000059: <LoadConstDouble>: <Reg8: 0, Double: 0.008856>
==> 00000063: <JGreater>: <Addr8: 32, Reg8: 2, Reg8: 0>  # Address: 00000083
==> 00000067: <LoadConstDouble>: <Reg8: 5, Double: 0.13793103448275862>
==> 00000071: <SubN>: <Reg8: 7, Reg8: 7, Reg8: 5>
==> 00000075: <LoadConstDouble>: <Reg8: 5, Double: 7.787>
==> 0000007f: <DivN>: <Reg8: 2, Reg8: 7, Reg8: 5>
==> 00000083: <JGreater>: <Addr8: 32, Reg8: 3, Reg8: 0>  # Address: 000000a3
==> 00000087: <LoadConstDouble>: <Reg8: 5, Double: 0.13793103448275862>
==> 00000091: <SubN>: <Reg8: 6, Reg8: 6, Reg8: 5>
==> 00000095: <LoadConstDouble>: <Reg8: 5, Double: 7.787>
==> 0000009f: <DivN>: <Reg8: 3, Reg8: 6, Reg8: 5>
==> 000000a3: <JGreater>: <Addr8: 32, Reg8: 1, Reg8: 0>  # Address: 000000c3
==> 000000a7: <LoadConstDouble>: <Reg8: 0, Double: 0.13793103448275862>
==> 000000b1: <SubN>: <Reg8: 4, Reg8: 4, Reg8: 0>
==> 000000b5: <LoadConstDouble>: <Reg8: 0, Double: 7.787>
==> 000000bf: <DivN>: <Reg8: 1, Reg8: 4, Reg8: 0>
==> 000000c3: <LoadConstDouble>: <Reg8: 0, Double: 95.047>
==> 000000cd: <Mul>: <Reg8: 3, Reg8: 3, Reg8: 0>
==> 000000d1: <LoadConstUInt8>: <Reg8: 0, UInt8: 100>
==> 000000d4: <Mul>: <Reg8: 2, Reg8: 2, Reg8: 0>
==> 000000d8: <LoadConstDouble>: <Reg8: 0, Double: 108.883>
==> 000000e2: <Mul>: <Reg8: 1, Reg8: 1, Reg8: 0>
==> 000000e6: <NewArray>: <Reg8: 0, UInt16: 3>
==> 000000ea: <PutOwnByIndex>: <Reg8: 0, Reg8: 3, UInt8: 0>
==> 000000ee: <PutOwnByIndex>: <Reg8: 0, Reg8: 2, UInt8: 1>
==> 000000f2: <PutOwnByIndex>: <Reg8: 0, Reg8: 1, UInt8: 2>
==> 000000f6: <Ret>: <Reg8: 0>


"""


def test_hoisted_exponentiation_is_folded_back_into_the_source_ternary():
    out = Decompiler.render(Decompiler.build_context(LAB_TO_XYZ, 12962), verbose=False)

    # The three assignments, one per Lab channel. (The `return` line repeats
    # the same expressions, which is why this matches assignments only.)
    assignments = [
        line
        for line in out.split("\n")
        if re.match(r"\s*r\d+ = exponentiationOperator\(r9, r8\) > 0\.008856 \? exponentiationOperator\(", line)
    ]

    assert len(assignments) == 3, out


# ----------------------------------------------------------------------------------------------------
# side_effecting_arm_value
#
# A constructor call in one arm of an `if`, read after it (`AnimatedAddition`,
# 96/5146):
#
#     this._a = typeof a === "number" ? new AnimatedValue(a) : a
#
# The arm's `SelectObject` result held the `Construct`, which the reader after the
# `if` inlined: `r0._a = new r3(r11)` ran the constructor on BOTH paths (and
# with `r3`/`r11`, set inside the arm, unassigned on the path that skips it).
# `UnfoldedMergeRepairPass` refused every side-effecting arm value for fear of
# running it twice; repointing the reader MOVES the effect instead.
# ----------------------------------------------------------------------------------------------------

_ANIMATED_ADDITION = r"""

=> [Function #5146 "AnimatedAddition" of 165 bytes]: 4 params, frame size=19, strict=1, exc handler=0, debug info=0  @ offset 0x0017e712

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 7, UInt8: 1>
==> 00000003: <LoadParam>: <Reg8: 4, UInt8: 2>
==> 00000006: <LoadParam>: <Reg8: 6, UInt8: 0>
==> 00000009: <GetEnvironment>: <Reg8: 2, UInt8: 1>
==> 0000000c: <LoadFromEnvironment>: <Reg8: 0, Reg8: 2, UInt8: 0>
==> 00000010: <GetByIdShort>: <Reg8: 0, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
==> 00000015: <GetEnvironment>: <Reg8: 1, UInt8: 0>
==> 00000018: <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 0>
==> 0000001c: <LoadConstUndefined>: <Reg8: 3>
==> 0000001e: <Call3>: <Reg8: 0, Reg8: 0, Reg8: 3, Reg8: 6, Reg8: 5>
==> 00000024: <LoadFromEnvironment>: <Reg8: 0, Reg8: 2, UInt8: 2>
==> 00000028: <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
==> 0000002d: <NewArray>: <Reg8: 0, UInt16: 1>
==> 00000031: <LoadParam>: <Reg8: 8, UInt8: 3>
==> 00000034: <PutOwnByIndex>: <Reg8: 0, Reg8: 8, UInt8: 0>
==> 00000038: <Call4>: <Reg8: 0, Reg8: 1, Reg8: 3, Reg8: 6, Reg8: 5, Reg8: 0>
==> 0000003f: <TypeOf>: <Reg8: 3, Reg8: 7>
==> 00000042: <LoadConstString>: <Reg8: 5, string_id: 7552>  # String: 'number' (Identifier)
==> 00000046: <Mov>: <Reg8: 1, Reg8: 7>
==> 00000049: <JStrictNotEqual>: <Addr8: 36, Reg8: 3, Reg8: 5>  # Address: 0000006d
==> 0000004d: <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 6>
==> 00000051: <GetByIdShort>: <Reg8: 3, Reg8: 3, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
==> 00000056: <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 2, string_id: 206>  # String: 'prototype' (Identifier)
==> 0000005b: <CreateThis>: <Reg8: 6, Reg8: 6, Reg8: 3>
==> 0000005f: <Mov>: <Reg8: 12, Reg8: 6>
==> 00000062: <Mov>: <Reg8: 11, Reg8: 7>
==> 00000065: <Construct>: <Reg8: 3, Reg8: 3, UInt8: 2>
==> 00000069: <SelectObject>: <Reg8: 1, Reg8: 6, Reg8: 3>
==> 0000006d: <PutById>: <Reg8: 0, Reg8: 1, UInt8: 1, string_id: 7361>  # String: '_a' (Identifier)
==> 00000073: <TypeOf>: <Reg8: 3, Reg8: 4>
==> 00000076: <Mov>: <Reg8: 1, Reg8: 4>
==> 00000079: <JStrictNotEqual>: <Addr8: 36, Reg8: 3, Reg8: 5>  # Address: 0000009d
==> 0000007d: <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 6>
==> 00000081: <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
==> 00000086: <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 206>  # String: 'prototype' (Identifier)
==> 0000008b: <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 2>
==> 0000008f: <Mov>: <Reg8: 12, Reg8: 3>
==> 00000092: <Mov>: <Reg8: 11, Reg8: 4>
==> 00000095: <Construct>: <Reg8: 2, Reg8: 2, UInt8: 2>
==> 00000099: <SelectObject>: <Reg8: 1, Reg8: 3, Reg8: 2>
==> 0000009d: <PutById>: <Reg8: 0, Reg8: 1, UInt8: 2, string_id: 11393>  # String: '_b' (Identifier)
==> 000000a3: <Ret>: <Reg8: 0>
"""


def _render_3() -> str:
    context = Decompiler.build_context(_ANIMATED_ADDITION, 5146, strict=False)

    return Decompiler.render(context, verbose=False, raw=False)


def test_constructor_runs_only_in_the_arm_that_takes_it():
    js = _render_3()

    assert "r0._a = new" not in js
    assert "r0._b = new" not in js
    assert js.count("new r") == 2  # one per arm, nowhere else


def test_the_join_value_is_named_after_the_if():
    js = _render_3()

    assert "r1 = new r3(r11);" in js
    assert "r0._a = r1;" in js
    assert "r0._b = r1;" in js


# ----------------------------------------------------------------------------------------------------
# stale_inlined_read
#
# A value built from a register (`r1 = r0[0]`, an environment slot) that is read
# after that register was overwritten must not be inlined: the register in it
# would then name the NEW value (F-01, F-04).
#
# The frontend inlines a load into its reader and cannot yet know whether a
# LATER definition of the register it mentions will end up printed. A scratch
# pass (`OpcodeDispatcher.dispatch_all`) now tells the real pass which
# definitions print - pinned by a bare read, or never folded into a reader.
#
#     96/4456  r1 = r0[0]; r0 = {...}; r1._responderRegion = r0
#              printed `r0[0]._responderRegion = r0`: `r0[0]` of the new object.
#     96/9118  r4 = r0[0]; r0 = undefined; r0 = r4(r2)
#              printed `r0 = undefined; r0 = r0[0](r2)`.
#
# Also covered: when a fold swaps a register callee for a member expression, the
# call keeps `this = undefined` (`env[1].call(undefined, x)`, not `env[1](x)`,
# which would pass `env` as `this`).
# ----------------------------------------------------------------------------------------------------

def _render_4(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_environment_load_is_kept_when_the_register_is_overwritten_by_a_literal():
    """96/4456: the literal that overwrites `r0` is printed, so `r1` keeps its own statement."""
    out = _render_4("any_of_params_96_4456.hasm", 4456)

    assert "r1 = r0[0];" in out
    assert "r1._responderRegion = r0;" in out
    assert "r0[0]._responderRegion" not in out


def test_callee_load_is_kept_when_the_register_is_overwritten_before_the_call():
    """96/9118: `r4 = r0[0]` ... `r0 = undefined` ... `r4(r0)`. The call folds into
    the test (`r1 === 1 && env[0].call(undefined, param1[0])`): its callee comes from
    the environment load, not from `r0` as it is by then, and `this` is undefined."""
    out = _render_4("parseScaleX_stale_callee_96_9118.hasm", 9118)

    assert "goto" not in out
    assert "getEnvironment(0)[0].call(undefined, param1[0])" in out
    assert "r0[0](" not in out
    assert "undefined[0]" not in out


def test_a_register_callee_replaced_by_a_member_keeps_this_undefined():
    call = CallExpression(callee=Identifier("r4"), arguments=(Identifier("x"),))
    member = MemberExpression(obj=Identifier("env"), prop=NumericLiteral(1), computed=True)

    folded = substitute_register(call, "r4", member)

    assert ExpressionPrinter().visit(folded) == "env[1].call(undefined, x)"
    assert isinstance(folded.arguments[0], UndefinedLiteral)


def test_a_register_callee_replaced_by_another_register_stays_a_plain_call():
    call = CallExpression(callee=Identifier("r4"), arguments=(Identifier("x"),))

    folded = substitute_register(call, "r4", Identifier("r7"))

    assert ExpressionPrinter().visit(folded) == "r7(x)"
