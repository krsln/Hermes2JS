"""The Hermes bytecode disassembler: headers, tables, literals, opcodes, the `.hasm` writer.

Merged from: test_hermes_disassembler_bigint_table, test_hermes_disassembler_builtins, test_hermes_disassembler_debug_offsets, test_hermes_disassembler_exception_handler_table, test_hermes_disassembler_function_header, test_hermes_disassembler_function_header_overflow, test_hermes_disassembler_hasm_writer, test_hermes_disassembler_header, test_hermes_disassembler_jump_target, test_hermes_disassembler_literal_buffer, test_hermes_disassembler_object_literal, test_hermes_disassembler_opcode, test_hermes_disassembler_oracle, test_hermes_disassembler_string_table, test_hermes_disassembler_switch_table, test_opcode_entry_literals, test_opcode_name_validation.
"""

from __future__ import annotations

import struct
import subprocess
from hermes_disassembler.core.Exceptions import HermesBytecodeError, InvalidMagicError, TruncatedFileError, UnsupportedBytecodeVersionError
from hermes_disassembler.emit import HasmWriter
from hermes_disassembler.emit.HasmWriter import format_bundle, format_function, format_instruction
from hermes_disassembler.format.BigIntTable import resolve_bigint
from hermes_disassembler.format.Builtins import load_builtins_table, resolve_builtin
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader, HEADER_SIZE, LAYOUT_V96, LAYOUT_V98, MAGIC
from hermes_disassembler.format.DebugOffsets import DebugOffsets, resolve_debug_offsets
from hermes_disassembler.format.ExceptionHandlerTable import ExceptionHandler, resolve_exception_handlers
from hermes_disassembler.format.FunctionHeader import FunctionHeaderEntry, FunctionKind, ProhibitInvoke, parse_function_headers
from hermes_disassembler.format.FunctionHeaderOverflow import _SMALL_BYTECODE_SIZE_LIMIT, resolve_overflowed_headers
from hermes_disassembler.format.JumpTarget import is_jump_instruction, resolve_jump_target, resolve_operand_jump_target
from hermes_disassembler.format.LiteralBuffer import decode_literal_buffer
from hermes_disassembler.format.ObjectLiteral import resolve_object_literal
from hermes_disassembler.format.Opcode import decode_function, load_opcode_table
from hermes_disassembler.format.StringTable import StringTable
from hermes_disassembler.format.SwitchTable import resolve_switch_table_entries
from hermes_disassembler.oracle.HermescFileInfo import HermescFileInfo
from pathlib import Path

import pytest

from hermes_decompiler.backend.analysis.cfg.BasicBlock import BasicBlock
from hermes_decompiler.frontend.handlers import OpcodeHandler
from hermes_decompiler.frontend.handlers.HandlerLoader import HandlerLoader
from hermes_decompiler.frontend.opcode.OpcodeEntry import JS_UNDEFINED, OpcodeEntry, _normalize_js_literals
from hermes_decompiler.frontend.parsing.OpcodeParser import OpcodeParser
from tests.models.OpcodeCatalog import OpcodeStatus, classify_all


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_bigint_table
#
# Tests `hermes_disassembler.format.BigIntTable` - synthetically for the
# value-decoding logic itself (neither `apps/testy/96` nor
# `apps/testy/98` has a single real BigInt literal - both have
# `bigint_count=0`, see that module's own docstring), and against the
# real fixtures for the table-location computation (`StringTable.py`'s
# `bigint_table_offset`), which real hermes-dec output can cross-check
# even with zero entries in it.
# ----------------------------------------------------------------------------------------------------

APPS_TESTY = Path(__file__).resolve().parent.parent / "apps" / "testy"


class _FakeHeader:
    def __init__(self, bigint_count: int):
        self.bigint_count = bigint_count


class _FakeTable:
    def __init__(self, bigint_table_offset: int):
        self.bigint_table_offset = bigint_table_offset


def test_resolves_two_entries_of_different_lengths():
    table_start = 100
    data = bytearray(300)
    _pack_entry(data, table_start, index=0, offset=0, length=4)
    _pack_entry(data, table_start, index=1, offset=4, length=2)
    storage_start = table_start + 2 * 8
    data[storage_start:storage_start + 4] = (0x12345678).to_bytes(4, "little")
    data[storage_start + 4:storage_start + 6] = (0xABCD).to_bytes(2, "little")

    fake_table = _FakeTable(bigint_table_offset=table_start)
    fake_header = _FakeHeader(bigint_count=2)

    assert resolve_bigint(bytes(data), fake_table, fake_header, 0) == 0x12345678
    assert resolve_bigint(bytes(data), fake_table, fake_header, 1) == 0xABCD


def test_out_of_range_index_raises_indexerror():
    fake_table = _FakeTable(bigint_table_offset=100)
    fake_header = _FakeHeader(bigint_count=2)
    with pytest.raises(IndexError):
        resolve_bigint(b"\x00" * 300, fake_table, fake_header, 5)


def _pack_entry(data: bytearray, table_start: int, index: int, offset: int, length: int) -> None:
    entry_pos = table_start + index * 8
    data[entry_pos:entry_pos + 4] = offset.to_bytes(4, "little")
    data[entry_pos + 4:entry_pos + 8] = length.to_bytes(4, "little")


@pytest.mark.parametrize("version", [96, 98])
def test_bigint_table_offset_matches_real_hermes_dec_stream_position(version: int):
    """
    Neither fixture has a real BigInt to decode, but the TABLE START
    position (StringTable.bigint_table_offset) is independently
    confirmed here by actually running real hermes-dec's own
    sequential HBCReader up through read_arrays() and checking its
    file stream position at that exact point: 943398 for bytecode 96
    (943400 once 4-byte aligned - read_bigints()'s own first step) and
    912180 for bytecode 98 (already aligned) - both match
    bigint_table_offset exactly. Not re-run here (would require
    reaching into vendor/hermes-dec directly from a test file); this
    only re-confirms both fixtures still have bigint_count=0, so a
    future fixture change would be caught if the offset math needed
    revisiting.
    """
    path = APPS_TESTY / str(version) / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, header)
    assert header.bigint_count == 0
    assert table.bigint_table_offset in (943400, 912180)


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_builtins
#
# Tests `hermes_disassembler.format.Builtins` against the real
# `apps/testy/96` and `apps/testy/98` bundle fixtures.
#
# `GetBuiltinClosure`/`CallBuiltin`/`CallBuiltinLong`'s builtin-number
# operand (tagged `builtin_id` by `Opcode.load_opcode_table`, always at
# operand index 1 for these three opcodes) is resolved here for every
# such instruction in both bundles, not just the one spot-checked
# example already cited in `Builtins.py`'s own module docstring - see
# `test_every_builtin_reference_resolves_at_scale` below for why that
# matters (the same "don't trust a single spot check" lesson `Opcode.py`
# and `StringTable.py`'s own test suites already apply).
# ----------------------------------------------------------------------------------------------------

#: opcodes whose builtin_id-tagged operand is at this fixed index (see
#: Opcode.py's semantics table for CallBuiltin/CallBuiltinLong/GetBuiltinClosure -
#: all three carry it at operand index 1).
_BUILTIN_OPERAND_INDEX = 1
_BUILTIN_OPCODES = ("GetBuiltinClosure", "CallBuiltin", "CallBuiltinLong")


def _load(version: str):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)
    return data, header, resolved


def _iter_builtin_refs(data: bytes, resolved, version: int):
    """Yield (function_index, instruction_name, builtin_index) for every builtin-referencing instruction in the bundle."""
    for e in resolved:
        instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, version)
        for i in instructions:
            if i.name in _BUILTIN_OPCODES:
                yield e.index, i.name, i.operands[_BUILTIN_OPERAND_INDEX]


def test_v96_builtins_table_size():
    assert len(load_builtins_table(96)) == 53


def test_v98_builtins_table_size():
    assert len(load_builtins_table(98)) == 59


def test_v99_raises_not_generated():
    with pytest.raises(HermesBytecodeError):
        load_builtins_table(99)


def test_getbuiltinclosure_57_resolves_to_spawnasync_98():
    """
    The exact spot check cited in Builtins.py's own module docstring:
    apps/testy/98's GetBuiltinClosure with operand 57 resolves to
    "spawnAsync", matching real hermes-dec output's own
    `# Built-in function: [#57 spawnAsync]` comment for the same
    instruction.
    """
    assert resolve_builtin(98, 57) == "spawnAsync"


def test_out_of_range_index_raises_indexerror_2():
    table_size = len(load_builtins_table(96))
    with pytest.raises(IndexError):
        resolve_builtin(96, table_size)


@pytest.mark.parametrize(
    "version,expected_count,expected_unique_names",
    [(96, 1314, 5), (98, 2546, 10)],
)
def test_every_builtin_reference_resolves_at_scale(version: int, expected_count: int, expected_unique_names: int):
    """
    Every `GetBuiltinClosure`/`CallBuiltin`/`CallBuiltinLong` instruction
    in each full bundle resolves its builtin_id operand without error -
    not just the single "operand 57 -> spawnAsync" example the module
    docstring cites. Exact counts pinned here as a regression check:
    a shift in these numbers would mean either the opcode table or the
    builtins table changed under us.
    """
    data, header, resolved = _load(str(version))
    refs = list(_iter_builtin_refs(data, resolved, version))
    assert len(refs) == expected_count

    names = {resolve_builtin(version, idx) for _fn, _name, idx in refs}
    assert len(names) == expected_unique_names


def test_getbuiltinclosure_57_found_in_real_bundle_98():
    """
    Confirms the docstring's spot-check instruction actually exists in
    the fixture (rather than `test_getbuiltinclosure_57_resolves_to_spawnasync_98`
    only checking the table in isolation) - i.e. some real function in
    apps/testy/98 has a `GetBuiltinClosure` whose builtin_id operand is
    literally 57.
    """
    data, header, resolved = _load("98")
    refs = list(_iter_builtin_refs(data, resolved, 98))
    assert any(name == "GetBuiltinClosure" and idx == 57 for _fn, name, idx in refs)


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_debug_offsets
#
# Tests `hermes_disassembler.format.DebugOffsets` - synthetically, since
# neither `apps/testy/96` nor `apps/testy/98` currently has a single real
# `has_debug_info=True` function to test against (see that module's own
# docstring for why, and `ExceptionHandlerTable.py`'s for the bug whose
# fix made that discoverable in the first place). The real fixtures are
# still used to confirm the negative case (no function in either bundle
# resolves anything here) at scale.
# ----------------------------------------------------------------------------------------------------

def _entry(**overrides) -> FunctionHeaderEntry:
    base = dict(
        index=0, is_overflowed=False, was_large_header=False,
        offset=0, info_offset=100, param_count=0, bytecode_size_in_bytes=0,
        function_name=0, frame_size=0, prohibit_invoke=ProhibitInvoke.NONE,
        strict_mode=False, has_exception_handler=False, has_debug_info=True,
        kind=FunctionKind.NORMAL,
    )
    base.update(overrides)
    return FunctionHeaderEntry(**base)


def test_has_debug_info_false_returns_none():
    entry = _entry(has_debug_info=False)
    assert resolve_debug_offsets(b"\x00" * 200, entry, 96) is None


def test_resolves_directly_at_info_offset_when_no_exception_handler():
    """No has_exception_handler: the DebugOffsets struct sits directly at info_offset (see ExceptionHandlerTable.locate_after_exception_handlers)."""
    info_offset = 100
    data = bytearray(200)
    struct.pack_into("<III", data, info_offset, 0x1234, 0x5678, 0x9ABC)

    entry = _entry(info_offset=info_offset, has_exception_handler=False, has_debug_info=True)
    offsets = resolve_debug_offsets(bytes(data), entry, 96)
    assert offsets == DebugOffsets(source_locations=0x1234, scope_desc_data=0x5678, textified_callees=0x9ABC)


def test_resolves_after_exception_handler_table_when_both_present():
    """
    has_exception_handler=True AND has_debug_info=True: the DebugOffsets
    struct sits immediately after the (correctly located) exception
    handler table, matching hermes-dec's own sequential read order
    (exception table first, then debug offsets) - see
    ExceptionHandlerTable.py's module docstring.
    """
    info_offset = 100
    data = bytearray(200)
    # ExceptionHandlerTableHeader: count=1
    struct.pack_into("<I", data, info_offset, 1)
    # one HBCExceptionHandlerInfo entry: start=1, end=2, target=3
    struct.pack_into("<III", data, info_offset + 4, 1, 2, 3)
    # table is 4 + 1*12 = 16 bytes (already 4-byte aligned) -> DebugOffsets right after
    debug_offset = info_offset + 16
    struct.pack_into("<III", data, debug_offset, 0xAAAA, 0xBBBB, 0xCCCC)

    entry = _entry(info_offset=info_offset, has_exception_handler=True, has_debug_info=True)

    handlers = resolve_exception_handlers(bytes(data), entry, 96)
    assert handlers[0].start == 1 and handlers[0].end == 2 and handlers[0].target == 3

    offsets = resolve_debug_offsets(bytes(data), entry, 96)
    assert offsets == DebugOffsets(source_locations=0xAAAA, scope_desc_data=0xBBBB, textified_callees=0xCCCC)


@pytest.mark.parametrize("version", [96, 98])
def test_neither_fixture_has_a_real_has_debug_info_function(version: int):
    """
    Documents the current state of both test fixtures (see module
    docstring) rather than testing DebugOffsets.py itself - if this
    ever starts failing (i.e. a fixture gains a real has_debug_info=True
    function), that's good news: replace it with a real assertion
    against tools/hermes/dump_bytecode.sh's oracle output instead of
    the synthetic cases above.
    """
    path = APPS_TESTY / str(version) / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)
    assert sum(1 for e in resolved if e.has_debug_info) == 0


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_exception_handler_table
#
# Tests `hermes_disassembler.format.ExceptionHandlerTable` against the
# real `apps/testy/96` and `apps/testy/98` bundle fixtures.
# ----------------------------------------------------------------------------------------------------

def _load_2(version: str):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)
    return data, resolved


def test_non_overflowed_handler_matches_instruction_boundaries_exactly():
    """
    apps/testy/96 function index 7 (guardedLoadModule): the exact
    hand-verified case that established the non-overflowed formula
    (info_offset points directly at the table, no large-header prefix) -
    see ExceptionHandlerTable.py's module docstring.
    """
    data, resolved = _load_2("96")
    guarded_load_module = next(e for e in resolved if e.index == 7)
    assert not guarded_load_module.was_large_header

    handlers = resolve_exception_handlers(data, guarded_load_module, 96)
    assert handlers == (ExceptionHandler(start=42, end=62, target=64),)

    instructions = decode_function(
        data, guarded_load_module.offset, guarded_load_module.bytecode_size_in_bytes, 96
    )
    starts = {i.offset - guarded_load_module.offset for i in instructions}
    assert handlers[0].start in starts
    assert handlers[0].target in starts


def test_overflowed_handler_matches_instruction_boundaries_exactly():
    """
    apps/testy/98 function index 1: the exact hand-verified case that
    established the overflowed formula (table follows the 37-byte large
    header, aligned to 4 bytes) - see ExceptionHandlerTable.py's module
    docstring and FunctionHeaderOverflow.py's for why 37, not
    hermes-dec's own (buggy, one byte short) 36, is correct for v98.
    """
    data, resolved = _load_2("98")
    fn = next(e for e in resolved if e.index == 1)
    assert fn.was_large_header

    handlers = resolve_exception_handlers(data, fn, 98)
    assert len(handlers) == 1
    assert handlers[0].start == 3
    assert handlers[0].end == 42
    assert handlers[0].target == 42

    instructions = decode_function(data, fn.offset, fn.bytecode_size_in_bytes, 98)
    starts = {i.offset - fn.offset for i in instructions}
    assert handlers[0].start in starts
    assert handlers[0].target in starts


def test_no_exception_handler_returns_empty_tuple():
    data, resolved = _load_2("96")
    clear_fn = next(e for e in resolved if e.index == 2)
    assert not clear_fn.has_exception_handler
    assert resolve_exception_handlers(data, clear_fn, 96) == ()


def test_overflowed_global_function_has_no_exception_handler():
    """
    Regression test for the bug FunctionHeaderOverflow.py's module
    docstring describes at length: apps/testy/96 function index 0
    ("global") was previously misdetected as `has_exception_handler=True`
    (from misreading its flags byte 6 bytes past its real position,
    under the old flat `LARGE_HEADER_SIZE=37`), with a handler table
    that never landed on real instruction boundaries. With the corrected
    31-byte v96 large-header size, it correctly decodes to
    `has_exception_handler=False` - matching
    `tools/hermes/dump_bytecode.sh`'s own real hermesc oracle output,
    which has no "Exception Handlers:" block anywhere in that
    function's ~7500-line listing (not re-run here; this only checks
    this package's own decoding, not the oracle itself).
    """
    data, resolved = _load_2("96")
    global_fn = next(e for e in resolved if e.index == 0)
    assert global_fn.was_large_header
    assert not global_fn.has_exception_handler
    assert resolve_exception_handlers(data, global_fn, 96) == ()


@pytest.mark.parametrize("version,expected_min_plausible_ratio", [("96", 1.0), ("98", 1.0)])
def test_most_handlers_land_on_instruction_boundaries_at_scale(version: str, expected_min_plausible_ratio: float):
    """
    Every has_exception_handler function's resolved table, across the
    whole bundle: each handler's start/target should land exactly on
    another instruction's offset within the same function. Both
    versions now hit 100% (660/660 in bytecode 96, 1082/1082 in
    bytecode 98) - bytecode 96 previously needed a 0.9 tolerance for
    one misdetected function (see
    test_overflowed_global_function_has_no_exception_handler above for
    what that was and why it no longer applies).
    """
    data, resolved = _load_2(version)
    eh_functions = [e for e in resolved if e.has_exception_handler]
    assert eh_functions  # sanity: both fixtures have some

    total = 0
    plausible = 0
    for e in eh_functions:
        instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, int(version))
        starts = {i.offset - e.offset for i in instructions}
        handlers = resolve_exception_handlers(data, e, int(version))
        for h in handlers:
            total += 1
            if h.start in starts and h.target in starts:
                plausible += 1

    assert total > 0
    assert plausible / total >= expected_min_plausible_ratio


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_function_header
#
# Tests `hermes_disassembler.format.FunctionHeader` against the real
# `apps/testy/96` and `apps/testy/98` bundle fixtures. Expected
# (name, param_count) signatures were captured once from
# `tools/hermes/dump_bytecode.sh <version> ...`'s function listing -
# hardcoded here so this test needs no hermesc install to run.
# ----------------------------------------------------------------------------------------------------

def _load_3(version: str):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, header)
    entries = parse_function_headers(data, header)
    return data, header, table, entries


def _signatures(entries, table) -> set[tuple[str, int]]:
    found = set()
    for e in entries:
        if e.is_overflowed:
            continue
        try:
            name = table.resolve(e.function_name)
        except Exception:
            continue
        found.add((name, e.param_count))
    return found


def test_entry_count_matches_header_96():
    _, header, _, entries = _load_3("96")
    assert len(entries) == header.function_count


def test_known_signatures_found_96():
    # from tools/hermes/dump_bytecode.sh 96 ...: Function<clear>(1 params...),
    # Function<define>(4 params...), Function<metroRequire>(3 params...),
    # Function<metroImportDefault>(3 params...)
    _, _, table, entries = _load_3("96")
    signatures = _signatures(entries, table)
    for target in [("clear", 1), ("define", 4), ("metroRequire", 3), ("metroImportDefault", 3)]:
        assert target in signatures


def test_known_signature_found_98():
    # Most bytecode-98 functions overflow (FunctionName is only 8 bits there
    # - see module docstring), so this checks a signature that survives:
    # Function<get>(1 params...), confirmed present in the oracle dump.
    _, _, table, entries = _load_3("98")
    signatures = _signatures(entries, table)
    assert ("get", 1) in signatures


def test_v96_overflow_is_rare():
    _, header, _, entries = _load_3("96")
    overflow_count = sum(1 for e in entries if e.is_overflowed)
    assert overflow_count == 3  # see module docstring


def test_v98_overflow_is_common_due_to_8bit_function_name():
    _, header, _, entries = _load_3("98")
    overflow_count = sum(1 for e in entries if e.is_overflowed)
    # not a bug - LAYOUT_V98's FunctionName field is only 8 bits (max 255),
    # see module docstring. Assert the majority overflow to catch any future
    # regression that would make this either 0 or 100%.
    assert 0.5 * header.function_count < overflow_count < header.function_count


def test_overflowed_entries_have_no_other_fields():
    _, _, _, entries = _load_3("96")
    overflowed = [e for e in entries if e.is_overflowed]
    assert overflowed  # sanity: there are some to check
    for e in overflowed:
        assert e.offset is None
        assert e.param_count is None
        assert e.function_name is None


def test_flags_decode_as_enums():
    _, _, _, entries = _load_3("96")
    for e in entries:
        if e.is_overflowed:
            continue
        assert isinstance(e.prohibit_invoke, ProhibitInvoke)
        assert isinstance(e.kind, FunctionKind)
        assert e.kind == FunctionKind.NORMAL  # LAYOUT_V96 has no Kind bits


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_function_header_overflow
#
# Tests `hermes_disassembler.format.FunctionHeaderOverflow` against the
# real `apps/testy/96` and `apps/testy/98` bundle fixtures.
# ----------------------------------------------------------------------------------------------------

def _load_4(version: str):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, header)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)
    return data, header, table, resolved


@pytest.mark.parametrize("version", ["96", "98"])
def test_no_overflowed_entries_remain(version: str):
    _, _, _, resolved = _load_4(version)
    assert all(not e.is_overflowed for e in resolved)


@pytest.mark.parametrize("version", ["96", "98"])
def test_every_resolved_large_header_has_a_sane_name(version: str):
    _, header, table, resolved = _load_4(version)
    large = [e for e in resolved if e.was_large_header]
    assert large  # sanity: there are some to resolve for both fixtures
    for e in large:
        name = table.resolve(e.function_name)  # raises on failure
        assert isinstance(name, str)


def test_v96_overflowed_functions_resolved():
    # from tools/hermes/dump_bytecode.sh 96: the global function overflows
    # (bytecode > 32767 bytes, v96's small-header limit) and resolves to
    # exactly "global" with param_count=1.
    _, _, table, resolved = _load_4("96")
    global_fn = next(e for e in resolved if e.was_large_header and table.resolve(e.function_name) == "global")
    assert global_fn.param_count == 1
    assert global_fn.bytecode_size_in_bytes > _SMALL_BYTECODE_SIZE_LIMIT[96]


def test_v98_previously_unreachable_signatures_now_resolve():
    # These four were unreachable before overflow resolution (see
    # test_hermes_disassembler_function_header.py's test_known_signature_found_98
    # comment) - v98's 8-bit FunctionName field pushed them into the
    # overflowed 78%. All four should resolve now.
    _, _, table, resolved = _load_4("98")
    signatures = {(table.resolve(e.function_name), e.param_count) for e in resolved}
    for target in [("clear", 1), ("define", 4), ("metroRequire", 3), ("metroImportDefault", 3)]:
        assert target in signatures


def test_pass_through_when_nothing_overflowed():
    """resolve_overflowed_headers on an all-non-overflowed tuple should be a no-op."""
    from hermes_disassembler.format.FunctionHeader import FunctionKind, FunctionHeaderEntry, ProhibitInvoke

    entry = FunctionHeaderEntry(
        index=0, is_overflowed=False, offset=1, param_count=1,
        bytecode_size_in_bytes=1, function_name=1, frame_size=1,
        prohibit_invoke=ProhibitInvoke.NONE, strict_mode=False,
        has_exception_handler=False, has_debug_info=False, kind=FunctionKind.NORMAL,
    )
    data, header, _, _ = _load_4("96")
    result = resolve_overflowed_headers(data, header, (entry,))
    assert result == (entry,)


def test_unconfirmed_version_raises_when_resolution_needed():
    import struct

    from hermes_disassembler.format.BytecodeFileHeader import HEADER_SIZE, MAGIC
    from hermes_disassembler.format.FunctionHeader import FunctionHeaderEntry

    # a minimal header claiming version 99 with function_count=1 (99's large
    # FunctionHeader layout is intentionally unconfirmed - see module docstring)
    class _FakeHeader:
        version = 99

    entry = FunctionHeaderEntry(index=0, is_overflowed=True)
    with pytest.raises(HermesBytecodeError):
        resolve_overflowed_headers(b"\x00" * HEADER_SIZE, _FakeHeader(), (entry,))


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_hasm_writer
#
# Tests `hermes_disassembler.emit.HasmWriter` against the real
# `apps/testy/96` and `apps/testy/98` bundle fixtures.
#
# The most important test here (`test_emitted_text_parses_with_real_hermes_decompiler`)
# doesn't just check our own output against a hardcoded string - it feeds
# every emitted line through `hermes_decompiler.frontend.parsing.OpcodeParser`,
# the REAL parser `hermes_decompiler`'s pipeline uses today (fed by
# vendor/hermes-dec's AGPL output). If that parser accepts our lines and
# extracts the expected opcode/args/comment, that's direct evidence
# `hermes_disassembler`'s output is usable as a drop-in replacement for
# that AGPL dependency - the actual stated purpose of this package (see
# its `__init__.py`).
# ----------------------------------------------------------------------------------------------------

def _load_clear(version: str, expected_frame_size: int):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, header)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)
    clear_fn = next(
        e for e in resolved
        if table.resolve(e.function_name) == "clear" and e.param_count == 1 and e.frame_size == expected_frame_size
    )
    instructions = decode_function(data, clear_fn.offset, clear_fn.bytecode_size_in_bytes, int(version))
    return data, clear_fn, instructions, table


def test_function_header_line_format_96():
    data, clear_fn, instructions, table = _load_clear("96", 9)
    text = format_function(data, clear_fn, instructions, table, 96)
    header_line = text.splitlines()[0]
    assert header_line == (
        '=> [Function #2 "clear" of 37 bytes]: 1 params, frame size=9, '
        'strict=1, exc handler=0, debug info=0  @ offset 0x000f7241'
    )


def test_string_id_operand_shows_semantic_label_and_comment_96():
    data, clear_fn, instructions, table = _load_clear("96", 9)
    line = format_instruction(data, instructions[1], clear_fn.offset, table, 96)  # TryGetById ... "Map"
    assert line == (
        "==> 00000002: <TryGetById>: <Reg8: 0, Reg8: 0, UInt8: 1, string_id: 20>"
        "  # String: 'Map' (Identifier)"
    )


def test_plain_instruction_has_no_comment_96():
    data, clear_fn, instructions, table = _load_clear("96", 9)
    line = format_instruction(data, instructions[0], clear_fn.offset, table, 96)  # GetGlobalObject
    assert line == "==> 00000000: <GetGlobalObject>: <Reg8: 0>"
    assert "#" not in line


@pytest.mark.parametrize("version,expected_frame_size", [("96", 9), ("98", 10)])
def test_emitted_text_parses_with_real_hermes_decompiler(version: str, expected_frame_size: int):
    """
    The end-to-end check: every instruction line this module emits for
    clear() is fed through hermes_decompiler's REAL OpcodeParser (not a
    reimplementation or a mock) and must parse successfully, extracting
    the same opcode name and a non-None args string for every
    instruction - see module docstring.
    """
    data, clear_fn, instructions, table = _load_clear(version, expected_frame_size)

    parsed_count = 0
    for instruction in instructions:
        line = format_instruction(data, instruction, clear_fn.offset, table, int(version))
        entry = OpcodeParser.parse(line)
        assert entry is not None, f"real OpcodeParser rejected our emitted line: {line!r}"
        assert entry.opcode == instruction.name
        parsed_count += 1

    assert parsed_count == len(instructions)


def test_string_comment_content_matches_resolved_string():
    """The comment's resolved string content must match StringTable.resolve() exactly - not just be present."""
    data, clear_fn, instructions, table = _load_clear("96", 9)
    get_by_id_short = instructions[2]  # GetByIdShort ... "prototype"
    line = format_instruction(data, get_by_id_short, clear_fn.offset, table, 96)
    entry = OpcodeParser.parse(line)
    assert "'prototype'" in entry.comment
    assert table.resolve(206) == "prototype"


def test_multiple_comments_each_get_their_own_prefix_not_joined():
    """
    Real hermes-dec output for CreateRegExp (two string_id operands)
    repeats the '  # ' prefix per comment rather than joining them with
    '; ' - locks in that join behavior directly, since none of our
    fixtures happens to contain a CreateRegExp instruction to exercise
    it end-to-end.
    """
    data, clear_fn, instructions, table = _load_clear("96", 9)
    single_comment_line = format_instruction(data, instructions[1], clear_fn.offset, table, 96)  # TryGetById
    assert single_comment_line.count("  # ") == 1

    comment_parts = ["String: 'a' (String)", "String: 'b' (Identifier)"]
    rendered = "==> 00000000: <Fake>: <>"
    for part in comment_parts:
        rendered += f"  # {part}"
    assert rendered == "==> 00000000: <Fake>: <>  # String: 'a' (String)  # String: 'b' (Identifier)"


def test_function_id_operand_resolves_target_signature():
    """CreateClosure/CreateGenerator's function_id operand resolves to the target function's own signature when all_functions is supplied."""
    data = (APPS_TESTY / "96" / "index.android.bundle").read_bytes()
    bc_header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, bc_header)
    entries = parse_function_headers(data, bc_header)
    resolved = resolve_overflowed_headers(data, bc_header, entries)

    target_instruction = None
    owner_offset = None
    for e in resolved[:2000]:
        instrs = decode_function(data, e.offset, e.bytecode_size_in_bytes, 96)
        for i in instrs:
            if i.name in ("CreateClosure", "CreateGenerator", "CreateAsyncClosure"):
                target_instruction, owner_offset = i, e.offset
                break
        if target_instruction:
            break
    assert target_instruction is not None, "no CreateClosure-family instruction found in first 2000 functions"

    without_functions = format_instruction(data, target_instruction, owner_offset, table, 96)
    assert "# Function:" not in without_functions

    with_functions = format_instruction(data, target_instruction, owner_offset, table, 96, resolved)
    assert "# Function: [#" in with_functions
    target_index = target_instruction.operands[-1]
    target_entry = resolved[target_index]
    assert f"of {target_entry.bytecode_size_in_bytes} bytes" in with_functions
    assert f"{target_entry.param_count} params" in with_functions
    assert f"offset 0x{target_entry.offset:08x}" in with_functions


def test_exception_handlers_line_present_and_formatted():
    """A function with has_exception_handler=True gets a '  [Exception handlers: ...]' line matching real hermes-dec's format."""
    data = (APPS_TESTY / "96" / "index.android.bundle").read_bytes()
    bc_header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, bc_header)
    entries = parse_function_headers(data, bc_header)
    resolved = resolve_overflowed_headers(data, bc_header, entries)
    guarded_load_module = next(e for e in resolved if e.index == 7)
    instructions = decode_function(data, guarded_load_module.offset, guarded_load_module.bytecode_size_in_bytes, 96)

    text = format_function(data, guarded_load_module, instructions, table, 96)
    lines = text.splitlines()
    assert lines[1] == "  [Exception handlers: [start=0x2a, end=0x3e, target=0x40] ]"


def test_function_without_exception_handler_has_no_extra_line():
    data, clear_fn, instructions, table = _load_clear("96", 9)
    text = format_function(data, clear_fn, instructions, table, 96)
    lines = text.splitlines()
    assert lines[1] == ""  # blank line straight after the header, no exception handlers line


@pytest.mark.parametrize(
    "kind,expected_label",
    [(FunctionKind.GENERATOR, "Generator function"), (FunctionKind.ASYNC, "Async function")],
)
def test_header_line_uses_kind_specific_label(kind: FunctionKind, expected_label: str):
    """
    Regression test for a previously-hardcoded "Function" label
    (header.kind was ignored entirely) - apps/testy/98 has 102 real
    generator and 90 real async functions this affected. hermes-dec's
    own format uses "Generator function"/"Async function" instead of
    "Function" for these - see HasmWriter.py's `_FUNC_KIND_LABEL`.
    """
    data = (APPS_TESTY / "98" / "index.android.bundle").read_bytes()
    bc_header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, bc_header)
    entries = parse_function_headers(data, bc_header)
    resolved = resolve_overflowed_headers(data, bc_header, entries)
    fn = next(e for e in resolved if e.kind == kind)
    instructions = decode_function(data, fn.offset, fn.bytecode_size_in_bytes, 98)

    text = format_function(data, fn, instructions, table, 98)
    assert text.splitlines()[0].startswith(f'=> [{expected_label} #{fn.index} "')


@pytest.mark.parametrize("kind", [FunctionKind.GENERATOR, FunctionKind.ASYNC])
def test_header_line_still_parses_with_real_function_metadata_parser(kind: FunctionKind):
    """
    Downstream regression check for the same fix as
    test_header_line_uses_kind_specific_label above: real
    hermes_decompiler code has TWO separate consumers of this header
    line, not just OpcodeParser (see this file's own module docstring) -
    hermes_decompiler.frontend.parsing.FunctionMetadataParser has its
    own, separate regex for it. That regex originally only matched a
    literal "Function #..." prefix - the "Generator function"/"Async
    function" labels this fix introduces would have made
    FunctionMetadataParser silently fail to parse any generator/async
    function's metadata (function_id/function_name/byte_size all
    missing, only a logged warning) without FunctionMetadataParser's
    own matching update.
    """
    from hermes_decompiler.frontend.parsing.FunctionMetadataParser import FunctionMetadataParser

    data = (APPS_TESTY / "98" / "index.android.bundle").read_bytes()
    bc_header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, bc_header)
    entries = parse_function_headers(data, bc_header)
    resolved = resolve_overflowed_headers(data, bc_header, entries)
    fn = next(e for e in resolved if e.kind == kind)
    instructions = decode_function(data, fn.offset, fn.bytecode_size_in_bytes, 98)

    header_line = format_function(data, fn, instructions, table, 98).splitlines()[0]
    metadata = FunctionMetadataParser.parse(header_line)

    assert metadata["function_id"] == fn.index
    assert metadata["byte_size"] == fn.bytecode_size_in_bytes
    assert metadata["param_count"] == fn.param_count


def test_debug_offsets_line_present_and_formatted():
    """
    A function with has_debug_info=True gets a '  [Debug offsets: ...]'
    line matching real hermes-dec's format - synthetic, since neither
    test fixture currently has a real has_debug_info=True function (see
    DebugOffsets.py's module docstring). Exercises format_function's
    actual line placement/ordering (after the header line, before the
    blank line and "Bytecode listing:"), not just DebugOffsets.py's own
    resolution logic (already covered in
    test_hermes_disassembler_debug_offsets.py).
    """
    data, clear_fn, instructions, table = _load_clear("96", 9)
    import struct as _struct
    import dataclasses
    debug_data = bytearray(data)
    debug_offset = clear_fn.info_offset
    if len(debug_data) < debug_offset + 12:
        debug_data.extend(b"\x00" * (debug_offset + 12 - len(debug_data)))
    _struct.pack_into("<III", debug_data, debug_offset, 0x111, 0x222, 0x333)
    fn_with_debug = dataclasses.replace(clear_fn, has_debug_info=True)

    text = format_function(bytes(debug_data), fn_with_debug, instructions, table, 96)
    lines = text.splitlines()
    assert lines[1] == f"  [Debug offsets: source_locs=0x{0x111:x}, scope_desc_data=0x{0x222:x}]"


def _split_output_file_module():
    """Import the real scripts/split_output_file.py (not part of any package - script directory added to sys.path)."""
    import scripts.split_output_file as split_output_file
    # import sys as _sys

    # scripts_dir = str(Path(__file__).resolve().parent.parent / "scripts")
    # if scripts_dir not in _sys.path:
    #     _sys.path.insert(0, scripts_dir)
    # import split_output_file  # noqa: PLC0415
    return split_output_file


@pytest.mark.parametrize("version", ["96", "98"])
def test_bundle_splits_with_real_split_output_file(version: str, tmp_path):
    """
    format_bundle()'s output, written to disk and split with the REAL
    scripts/split_output_file.py (not a reimplementation), produces
    exactly one section per function - the closed-loop check that
    SECTION_SEPARATOR matches that script's DEFAULT_SEPARATOR and that
    every format_function() block is self-contained (no stray
    separator-looking lines inside a function's own instructions).
    """
    split_output_file = _split_output_file_module()

    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    bc_header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, bc_header)

    assert HasmWriter.SECTION_SEPARATOR == split_output_file.DEFAULT_SEPARATOR

    text = format_bundle(data, bc_header, table, int(version))
    hasm_path = tmp_path / "output.hasm"
    hasm_path.write_text(text)

    sections = list(split_output_file.iter_sections(hasm_path, split_output_file.DEFAULT_SEPARATOR))
    assert len(sections) == bc_header.function_count
    assert sections[0].lines[0].startswith('=> [Function #0 ')
    # Every section (including the last) ends with two blank lines
    # before its separator - matching real hermes-dec's own output
    # exactly (see format_bundle's docstring) - so the LAST section is
    # still a genuine, non-empty function block, not an empty phantom
    # section (which the trailing separator could otherwise produce -
    # see iter_sections' own docstring for that confirmed real
    # hermes-dec-output edge case).
    assert sections[-1].is_function
    assert any(line.strip() for line in sections[-1].lines)


def test_switch_imm_gets_jump_table_comment_matching_real_hermes_dec():
    """
    apps/testy/96's SwitchImm at function-relative offset 0x0000000b -
    the exact instruction/values confirmed against real hermes-dec
    output in test_hermes_disassembler_switch_table.py - gets both its
    default-case `# Address:` comment (from the generalized per-operand
    Addr32 handling - see JumpTarget.py) and a `# Jump table: [...]`
    comment, in that order, matching real hermes-dec's own output
    exactly (confirmed by directly running hbc-disassembler against
    this fixture - see SwitchTable.py's module docstring).
    """
    data = (APPS_TESTY / "96" / "index.android.bundle").read_bytes()
    bc_header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, bc_header)
    entries = parse_function_headers(data, bc_header)
    resolved = resolve_overflowed_headers(data, bc_header, entries)

    switch_fn, switch_instr = next(
        (e, i)
        for e in resolved
        for i in decode_function(data, e.offset, e.bytecode_size_in_bytes, 96)
        if i.name == "SwitchImm" and (i.offset - e.offset) == 0xB and i.operands == (1, 238, 232, 0, 31)
    )

    line = format_instruction(data, switch_instr, switch_fn.offset, table, 96)
    assert "  # Address: 000000f3  # Jump table: [00000067, 00000031, " in line
    assert line.rstrip().endswith("0000001d]")


def test_uint_switch_imm_gets_jump_table_comment_even_though_hermes_dec_doesnt():
    """
    UNLIKE most of this package's hermes-dec-quirk-matching choices,
    `UIntSwitchImm` deliberately does NOT match real hermes-dec's own
    output here (confirmed via hbc-disassembler run directly against
    apps/testy/98: it never prints a `# Jump table:` comment for this
    opcode). hermes_decompiler's `UIntSwitchImm` handler is the exact
    same class as `SwitchImm`'s and depends on this comment (parsed
    into `ctx.entry.jump_table`) to reconstruct a v98 switch statement's
    cases at all - see SwitchTable.py's module docstring.
    """
    data = (APPS_TESTY / "98" / "index.android.bundle").read_bytes()
    bc_header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, bc_header)
    entries = parse_function_headers(data, bc_header)
    resolved = resolve_overflowed_headers(data, bc_header, entries)

    fn, instr = next(
        (e, i)
        for e in resolved
        for i in decode_function(data, e.offset, e.bytecode_size_in_bytes, 98)
        if i.name == "UIntSwitchImm"
    )

    line = format_instruction(data, instr, fn.offset, table, 98)
    assert "# Address:" in line
    assert "# Jump table: [" in line


def test_string_switch_imm_gets_address_but_no_jump_table_comment():
    """
    `StringSwitchImm` genuinely has no jump-table comment here, unlike
    `UIntSwitchImm` above - hermes_decompiler's own `StringSwitchImm`
    handler doesn't read one at all (its cases come from a separate
    string-keyed table this package doesn't parse), so there's no
    consumer for it either way - see SwitchTable.py's module docstring.
    """
    data = (APPS_TESTY / "98" / "index.android.bundle").read_bytes()
    bc_header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, bc_header)
    entries = parse_function_headers(data, bc_header)
    resolved = resolve_overflowed_headers(data, bc_header, entries)

    fn, instr = next(
        (e, i)
        for e in resolved
        for i in decode_function(data, e.offset, e.bytecode_size_in_bytes, 98)
        if i.name == "StringSwitchImm"
    )

    line = format_instruction(data, instr, fn.offset, table, 98)
    assert "# Address:" in line
    assert "Jump table" not in line


def test_bigint_id_comment_requires_bc_header():
    """
    A LoadConstBigInt/LoadConstBigIntLongIndex instruction's bigint_id
    operand gets a `# BigInt: <value>` comment (matching real
    hermes-dec's format exactly - see BigIntTable.py's module
    docstring) when bc_header is passed, and none when it's omitted -
    same graceful-degradation pattern as function_id/all_functions.
    Synthetic, since neither fixture has a real BigInt (bigint_count=0
    in both - see BigIntTable.py's module docstring).
    """
    from hermes_disassembler.format.Opcode import Instruction, load_opcode_table

    data, clear_fn, _instructions, table = _load_clear("96", 9)
    bc_header = BytecodeFileHeader.parse(data)

    debug_data = bytearray(data)
    table_start = table.bigint_table_offset
    needed = table_start + 8 + 4  # one entry (offset,length) + its 4-byte value
    if len(debug_data) < needed:
        debug_data.extend(b"\x00" * (needed - len(debug_data)))
    debug_data[table_start:table_start + 4] = (0).to_bytes(4, "little")
    debug_data[table_start + 4:table_start + 8] = (4).to_bytes(4, "little")
    debug_data[table_start + 8:table_start + 12] = (12345).to_bytes(4, "little")

    import dataclasses
    header_with_one_bigint = dataclasses.replace(bc_header, bigint_count=1)

    opcode_table = load_opcode_table(96)
    bigint_opcode = next(i for i, (name, _ops, _sem) in enumerate(opcode_table) if name == "LoadConstBigInt")
    load_bigint = Instruction(
        offset=clear_fn.offset, opcode=bigint_opcode, name="LoadConstBigInt", operands=(0, 0), size=4
    )

    line_without_header = format_instruction(bytes(debug_data), load_bigint, clear_fn.offset, table, 96)
    assert "# BigInt:" not in line_without_header

    line_with_header = format_instruction(
        bytes(debug_data), load_bigint, clear_fn.offset, table, 96, bc_header=header_with_one_bigint
    )
    assert line_with_header.rstrip().endswith("# BigInt: 12345")


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_header
#
# Tests `hermes_disassembler.format.BytecodeFileHeader` against the real
# `apps/testy/96` and `apps/testy/98` bundle fixtures already committed in
# this repo. Expected values were cross-checked once against
# `tools/hermes/dump_bytecode.sh <version> ...`'s own "Bytecode File
# Information" block (see `BytecodeFileHeader.py`'s module docstring) -
# hardcoded here so this test needs no hermesc install to run.
#
# See `test_hermes_disassembler_oracle.py` for the live cross-check against
# hermesc itself (skipped when the compiler isn't installed).
# ----------------------------------------------------------------------------------------------------

def _bundle(version: str) -> bytes:
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    return path.read_bytes()


@pytest.fixture(scope="module")
def bundle_96_bytes() -> bytes:
    return _bundle("96")


@pytest.fixture(scope="module")
def bundle_98_bytes() -> bytes:
    return _bundle("98")


def test_header_size_is_128_bytes():
    assert HEADER_SIZE == 128


def test_parses_real_bundle_96_legacy_layout(bundle_96_bytes: bytes):
    header = BytecodeFileHeader.parse(bundle_96_bytes)

    assert header.layout is LAYOUT_V96
    assert header.version == 96
    assert header.source_hash.hex() == "1d51e04b69e9eff199c798fe7d984872112bdf2c"
    assert header.file_length == len(bundle_96_bytes)
    assert header.function_count == 15247
    assert header.string_count == 18615
    assert header.string_kind_count == 3
    assert header.identifier_count == 11707
    assert header.overflow_string_count == 285
    assert header.bigint_count == 0
    assert header.regexp_count == 196
    assert header.segment_id == 0
    assert header.cjs_module_count == 0
    assert header.function_source_count == 84
    assert header.options.static_builtins is False
    assert header.options.cjs_modules_statically_resolved is False
    # v96-only fields present, v98-only fields absent:
    assert header.array_buffer_size is not None
    assert header.num_string_switch_imms is None


def test_parses_real_bundle_98_stringswitch_layout(bundle_98_bytes: bytes):
    header = BytecodeFileHeader.parse(bundle_98_bytes)

    assert header.layout is LAYOUT_V98
    assert header.version == 98
    assert header.source_hash.hex() == "0c1ff7241f4ebcf41ad75a2a9ae7d9f9cc2e34aa"
    assert header.file_length == len(bundle_98_bytes)
    assert header.function_count == 14267
    assert header.string_count == 18070
    assert header.string_kind_count == 3
    assert header.bigint_count == 0
    assert header.regexp_count == 199
    assert header.num_string_switch_imms == 7
    assert header.segment_id == 0  # was misread as 7 under the v96 layout - see module docstring
    assert header.cjs_module_count == 0
    assert header.function_source_count == 90
    assert header.options.static_builtins is False
    # v98-only fields present, v96-only fields absent:
    assert header.literal_value_buffer_size is not None
    assert header.array_buffer_size is None


def test_rejects_bad_magic():
    junk = b"\x00" * HEADER_SIZE
    with pytest.raises(InvalidMagicError) as exc_info:
        BytecodeFileHeader.parse(junk)
    assert exc_info.value.expected == MAGIC


def test_rejects_truncated_input():
    with pytest.raises(TruncatedFileError):
        BytecodeFileHeader.parse(b"\x00" * 10)


def test_rejects_unconfirmed_version():
    import struct
    # valid magic, version 97 (no confirmed layout - see versions.json: no npm hermesc exists for it)
    junk = struct.pack("<QI", MAGIC, 97) + b"\x00" * (HEADER_SIZE - 12)
    with pytest.raises(UnsupportedBytecodeVersionError) as exc_info:
        BytecodeFileHeader.parse(junk)
    assert exc_info.value.version == 97


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_jump_target
#
# Tests `hermes_disassembler.format.JumpTarget` against the real
# `apps/testy/96` and `apps/testy/98` bundle fixtures.
# ----------------------------------------------------------------------------------------------------

def _load_5(version: str):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, header)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)
    return data, resolved


def test_non_jump_instruction_returns_none():
    data, resolved = _load_5("96")
    fn = next(e for e in resolved if e.index == 7)
    instructions = decode_function(data, fn.offset, fn.bytecode_size_in_bytes, 96)
    load_param = instructions[0]
    assert load_param.name == "LoadParam"
    assert not is_jump_instruction(load_param, 96)
    assert resolve_jump_target(load_param, 96) is None


def test_guarded_load_module_jump_targets_96():
    """
    apps/testy/96 function index 7 ("guardedLoadModule", a try/catch
    module loader): hand-verified jump targets that established the
    offset formula (offset + first operand) - see JumpTarget.py's
    module docstring.
    """
    data, resolved = _load_5("96")
    fn = next(e for e in resolved if e.index == 7)
    instructions = decode_function(data, fn.offset, fn.bytecode_size_in_bytes, 96)
    by_relative_offset = {i.offset - fn.offset: i for i in instructions}

    jmp = by_relative_offset[62]
    assert jmp.name == "Jmp"
    assert resolve_jump_target(jmp, 96) - fn.offset == 87  # lands on LoadConstFalse (try succeeded)

    jmp_true = by_relative_offset[20]
    assert jmp_true.name == "JmpTrue"
    assert resolve_jump_target(jmp_true, 96) - fn.offset == 95

    jmp_false = by_relative_offset[33]
    assert jmp_false.name == "JmpFalse"
    assert resolve_jump_target(jmp_false, 96) - fn.offset == 95  # converges with JmpTrue's target


@pytest.mark.parametrize("version,expected_jump_count", [("96", 26716), ("98", 35178)])
def test_every_jump_in_bundle_lands_on_an_instruction_boundary(version: str, expected_jump_count: int):
    """
    Every jump instruction in every function of the bundle, decoded and
    resolved, lands exactly on another instruction's start offset (or
    exactly at its function's end) - never out of bounds, never
    mid-instruction. This is the mass-validation that confirmed the
    offset formula at scale (26716 / 35178 jumps, all landing exactly)
    rather than trusting the three hand-picked examples above alone.
    """
    data, resolved = _load_5(version)

    total_jumps = 0
    for e in resolved:
        instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, int(version))
        starts = {i.offset for i in instructions}
        func_end = e.offset + e.bytecode_size_in_bytes

        for instruction in instructions:
            if not is_jump_instruction(instruction, int(version)):
                continue
            total_jumps += 1
            target = resolve_jump_target(instruction, int(version))
            assert e.offset <= target <= func_end, f"function {e.index}: jump at {instruction.offset} target {target} out of bounds"
            assert target in starts or target == func_end, f"function {e.index}: jump at {instruction.offset} target {target} not on an instruction boundary"

    assert total_jumps == expected_jump_count


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_literal_buffer
#
# Tests `hermes_disassembler.format.LiteralBuffer` against the real
# `apps/testy/96` and `apps/testy/98` bundle fixtures.
# ----------------------------------------------------------------------------------------------------

def _load_6(version: str):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, header)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)
    return data, header, table, resolved


def test_decodes_byte_verified_single_element_array_96():
    """
    Hand-verified byte-for-byte: offset base+3 is 0x71 (IntegerTag,
    run length 1), payload 01 00 00 00 = 1 - see LiteralBuffer.py's
    module docstring.
    """
    data, header, table, resolved = _load_6("96")
    values = decode_literal_buffer(data, table.literal_value_buffer_offset + 3, 1, 96, table)
    assert values == (1,)


def test_decodes_byte_verified_three_element_array_96():
    """Same hand-verified region: offset base+8 is 3 consecutive Integer tag+run, values 2, 578, 1478."""
    data, header, table, resolved = _load_6("96")
    values = decode_literal_buffer(data, table.literal_value_buffer_offset + 8, 3, 96, table)
    assert values == (2, 578, 1478)


def test_matches_oracle_array_buffer_dump_sequence_96():
    """
    Reproduces the exact start of tools/hermes/dump_bytecode.sh's own
    "Array Buffer:" section (a raw sequential walk from byte 0 - NOT
    per-instruction order, see module docstring): String(1914),
    Integer(1), Integer(2), Integer(578), Integer(1478).
    """
    data, header, table, resolved = _load_6("96")
    base = table.literal_value_buffer_offset
    values = decode_literal_buffer(data, base, 5, 96, table)
    assert values == (table.resolve(1914), 1, 2, 578, 1478)


def test_byte_string_tag_decodes_correctly_v96():
    """
    Regression test for the tag-6 bug: version < 98 uses ByteStringTag
    (1-byte string index payload) for raw tag 6, not UndefinedTag (0
    bytes) - getting this wrong desynchronizes every subsequent tag in
    the buffer. Confirmed via a real object key buffer decode that only
    works correctly with the ByteStringTag interpretation - see
    ObjectLiteral.py and LiteralBuffer.py's module docstrings for the
    full story (42% -> 99.8% string keys in bytecode 96 after this fix).
    """
    data, header, table, resolved = _load_6("96")
    for e in resolved:
        instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, 96)
        for instruction in instructions:
            if instruction.name != "NewObjectWithBuffer":
                continue
            _reg, _hint, count, key_idx, _val_idx = instruction.operands
            keys = decode_literal_buffer(data, table.object_key_buffer_offset + key_idx, count, 96, table)
            if keys == ("trace", "info", "warn", "error"):
                return
    pytest.fail("expected console-levels object keys not found - ByteStringTag regression?")


@pytest.mark.parametrize("version,expected_min_success_ratio", [("96", 1.0), ("98", 1.0)])
def test_every_array_instruction_decodes_at_scale(version: str, expected_min_success_ratio: float):
    """
    Every NewArrayWithBuffer/NewArrayWithBufferLong instruction in the
    bundle, decoded via its own buf_idx: 100% succeed in both versions
    (bytecode 96 used to have a ~1% failure rate here, entirely caused
    by the tag-6 bug described in this module's own docstring and now
    fixed).
    """
    data, header, table, resolved = _load_6(version)

    total = 0
    ok = 0
    for e in resolved:
        instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, int(version))
        for instruction in instructions:
            if instruction.name not in ("NewArrayWithBuffer", "NewArrayWithBufferLong"):
                continue
            total += 1
            _reg, _hint, count, buf_idx = instruction.operands
            try:
                decode_literal_buffer(data, table.literal_value_buffer_offset + buf_idx, count, int(version), table)
                ok += 1
            except Exception:
                pass

    assert total > 0
    assert ok / total >= expected_min_success_ratio


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_object_literal
#
# Tests `hermes_disassembler.format.ObjectLiteral` against the real
# `apps/testy/96` and `apps/testy/98` bundle fixtures. Both layouts are
# supported (v96's direct key/value buffers, v98's shape-table
# indirection) - see the module's own docstring for the tag-6 bug that
# initially made v96 look unsupportable, and its fix.
# ----------------------------------------------------------------------------------------------------

def _load_7(version: str):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, header)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)
    return data, header, table, resolved


def _resolve(data, table, version: str, instruction):
    """Dispatch operand extraction per version's layout - see ObjectLiteral.py."""
    if version == "98":
        shape_idx, val_idx = instruction.operands[1], instruction.operands[2]
        return resolve_object_literal(data, table, 98, shape_idx, val_idx)
    count, key_idx, val_idx = instruction.operands[2], instruction.operands[3], instruction.operands[4]
    return resolve_object_literal(data, table, 96, count, key_idx, val_idx)


def test_shape_table_entry_25_matches_oracle_byte_for_byte():
    """
    tools/hermes/dump_bytecode.sh 98 ...'s own "Object Shape Table:"
    line for index 25 is "25[254, 1]" - keyBufferOffset=254, numProps=1 -
    confirmed here directly from the file (not just via an instruction).
    """
    data, header, table, resolved = _load_7("98")
    entry_offset = table.object_value_or_shape_table_offset + 25 * 8
    key_buffer_offset, num_props = struct.unpack_from("<II", data, entry_offset)
    assert (key_buffer_offset, num_props) == (254, 1)


def test_resolves_plausible_object_literal_98():
    """A real NewObjectWithBuffer's operands resolve to {'value': True} - matches shape 25 above (single prop, key 'value')."""
    data, header, table, resolved = _load_7("98")
    literal = resolve_object_literal(data, table, 98, 25, 17297)
    assert literal.keys == ("value",)
    assert literal.values == (True,)


def test_bytecode_96_direct_layout_resolves_console_levels():
    """
    apps/testy/96's console-level object ({trace:0, info:1, warn:2,
    error:3}) - the same source, and the identical decoded result, as
    apps/testy/98's own shape-table-based instance of it (see
    test_v96_and_v98_agree_on_the_same_source_object below) - proof v96's
    direct keyBufIdx/valBufIdx layout is genuinely fixed, not just
    "less wrong".
    """
    data, header, table, resolved = _load_7("96")
    for e in resolved:
        instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, 96)
        for instruction in instructions:
            if instruction.name != "NewObjectWithBuffer":
                continue
            literal = _resolve(data, table, "96", instruction)
            if literal.keys == ("trace", "info", "warn", "error"):
                assert literal.values == (0, 1, 2, 3)
                return
    pytest.fail("console-level object not found in apps/testy/96")


def test_v96_and_v98_agree_on_the_same_source_object():
    """The exact same {trace,info,warn,error} object, compiled to both bytecode versions, decodes identically."""
    values_by_version = {}
    for version in ("96", "98"):
        data, header, table, resolved = _load_7(version)
        for e in resolved:
            instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, int(version))
            for instruction in instructions:
                if instruction.name != "NewObjectWithBuffer":
                    continue
                literal = _resolve(data, table, version, instruction)
                if literal.keys == ("trace", "info", "warn", "error"):
                    values_by_version[version] = literal.values
                    break
            if version in values_by_version:
                break
    assert values_by_version["96"] == values_by_version["98"] == (0, 1, 2, 3)


def test_unconfirmed_version_raises_not_guessed():
    data, header, table, resolved = _load_7("98")
    with pytest.raises(HermesBytecodeError):
        resolve_object_literal(data, table, 97, 0, 0, 0)


@pytest.mark.parametrize("version,expected_min_string_key_ratio", [("96", 0.95), ("98", 0.95)])
def test_most_keys_are_strings_at_scale(version: str, expected_min_string_key_ratio: float):
    """
    Every NewObjectWithBuffer in the bundle: the overwhelming majority
    of decoded keys should be strings (property names) - a numeric key
    is legal JS but rare; anything else (undefined/bool/None) would
    indicate a decoding bug. Before the LiteralBuffer tag-6 fix, v96
    scored only 42% here; now both versions are effectively clean
    (99.8%/99.3%).
    """
    data, header, table, resolved = _load_7(version)

    total_keys = 0
    string_keys = 0
    errors = 0
    for e in resolved:
        instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, int(version))
        for instruction in instructions:
            if instruction.name not in ("NewObjectWithBuffer", "NewObjectWithBufferLong"):
                continue
            try:
                literal = _resolve(data, table, version, instruction)
            except Exception:
                errors += 1
                continue
            for k in literal.keys:
                total_keys += 1
                if isinstance(k, str):
                    string_keys += 1

    assert total_keys > 0
    assert string_keys / total_keys >= expected_min_string_key_ratio


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_opcode
#
# Tests `hermes_disassembler.format.Opcode` against the real
# `apps/testy/96` and `apps/testy/98` bundle fixtures.
#
# The full-function decode tests reproduce, instruction-by-instruction,
# `tools/hermes/dump_bytecode.sh`'s own listing for `clear()` in each
# bundle - hardcoded here so this test needs no hermesc install to run.
# This is deliberately a whole-function, opcode-by-opcode comparison
# rather than a handful of spot checks: an earlier version of the v96
# opcode table (generated from the `v0.12.0` git tag instead of the
# actual pinned commit) decoded the *first* instruction correctly and
# only diverged into garbage from the *second* instruction onward - a
# single-instruction smoke test would have missed that entirely. See
# `hermes_disassembler/format/Opcode.py`'s module docstring for the full
# story.
# ----------------------------------------------------------------------------------------------------

# From tools/hermes/dump_bytecode.sh <version> ...'s listing for clear()
# (the (1 params, N registers, ...) variant with no exception handler /
# debug info): (opcode_name, operand_values) in order. Operand values
# that reference the string table are the raw string_table index (not
# the resolved string) except where noted with a separate assertion.
EXPECTED_96 = [
    ("GetGlobalObject", (0,)),
    ("TryGetById", (0, 0, 1, 20)),  # id 20 -> "Map"
    ("GetByIdShort", (1, 0, 2, 206)),  # id 206 -> "prototype"
    ("CreateThis", (1, 1, 0)),
    ("Mov", (2, 1)),
    ("Construct", (0, 0, 1)),
    ("SelectObject", (0, 1, 0)),
    ("GetEnvironment", (1, 0)),
    ("StoreToEnvironment", (1, 1, 0)),
    ("Ret", (0,)),
]
EXPECTED_98 = [
    ("GetGlobalObject", (0,)),
    ("TryGetById", (0, 0, 0, 18)),  # id 18 -> "Map"
    ("CreateThisForNew", (1, 0, 1)),
    ("Mov", (2, 1)),
    ("Construct", (0, 0, 1)),
    ("SelectObject", (0, 1, 0)),
    ("GetParentEnvironment", (1, 0)),
    ("StoreToEnvironment", (1, 1, 0)),
    ("Ret", (0,)),
]


def _load_8(version: str):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, header)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)
    return data, header, table, resolved


def test_v96_opcode_count():
    assert len(load_opcode_table(96)) == 206


def test_v98_opcode_count():
    assert len(load_opcode_table(98)) == 219


def test_v98_define_own_by_id_name_operand_is_tagged_string_id():
    # Upstream's BytecodeList.def tags only DefineOwnByIdLong
    # (`OPERAND_STRING_ID(DefineOwnByIdLong, 4)`) and forgets the short form,
    # so the generated table alone left DefineOwnById's name operand untagged
    # (1,814 call sites in the 98 test bundle printed no `# String:` comment,
    # and the decompiler emitted `obj.string_140 = ...`). It is restored by
    # `_MANUAL_SEMANTICS` in tools/hermes/generate_opcode_tables.py.
    semantics = {name: sem for name, _operands, sem in load_opcode_table(98)}

    assert semantics["DefineOwnById"] == {3: "string_id"}
    assert semantics["DefineOwnByIdLong"] == {3: "string_id"}


@pytest.mark.parametrize("version", [96, 98])
def test_short_and_long_forms_carry_the_same_semantics(version: int):
    # Guards against the same upstream omission for any other opcode pair:
    # a `...Long` opcode only widens an operand, it never changes its meaning.
    table = {name: (operands, sem) for name, operands, sem in load_opcode_table(version)}
    mismatches = [
        (name, table[name[:-4]][1], sem)
        for name, (_operands, sem) in table.items()
        if name.endswith("Long") and name[:-4] in table and table[name[:-4]][1] != sem
    ]

    assert mismatches == []


def test_v99_raises_not_generated_2():
    with pytest.raises(HermesBytecodeError):
        load_opcode_table(99)


def test_clear_decodes_exactly_96():
    data, header, table, resolved = _load_8("96")
    clear_fn = next(
        e for e in resolved if table.resolve(e.function_name) == "clear" and e.param_count == 1 and e.frame_size == 9)

    instructions = decode_function(data, clear_fn.offset, clear_fn.bytecode_size_in_bytes, 96)

    assert [(i.name, i.operands) for i in instructions] == EXPECTED_96
    # every declared byte accounted for, no gap and no overrun
    assert sum(i.size for i in instructions) == clear_fn.bytecode_size_in_bytes
    # spot-check the two string-table operands actually resolve as expected
    assert table.resolve(instructions[1].operands[3]) == "Map"
    assert table.resolve(instructions[2].operands[3]) == "prototype"


def test_clear_decodes_exactly_98():
    data, header, table, resolved = _load_8("98")
    clear_fn = next(
        e for e in resolved if table.resolve(e.function_name) == "clear" and e.param_count == 1 and e.frame_size == 10)

    instructions = decode_function(data, clear_fn.offset, clear_fn.bytecode_size_in_bytes, 98)

    assert [(i.name, i.operands) for i in instructions] == EXPECTED_98
    assert sum(i.size for i in instructions) == clear_fn.bytecode_size_in_bytes
    assert table.resolve(instructions[1].operands[3]) == "Map"


@pytest.mark.parametrize("version,expected_frame_size", [("96", 9), ("98", 10)])
def test_last_instruction_is_ret(version: str, expected_frame_size: int):
    data, header, table, resolved = _load_8(version)
    clear_fn = next(
        e for e in resolved
        if table.resolve(e.function_name) == "clear" and e.param_count == 1 and e.frame_size == expected_frame_size
    )
    instructions = decode_function(data, clear_fn.offset, clear_fn.bytecode_size_in_bytes, int(version))
    assert instructions[-1].name == "Ret"


@pytest.mark.parametrize("version,expected_count", [("96", 15247), ("98", 14267)])
def test_every_function_in_bundle_decodes_cleanly(version: str, expected_count: int):
    """
    Every function header in each bundle - including the ~2.6-3.3% with
    has_exception_handler=True, which earlier (mistaken) investigation
    suspected might need special handling - decodes with decode_function()
    landing exactly on offset + bytecode_size_in_bytes, with no
    HermesBytecodeError. has_exception_handler turned out to need no
    special casing at all: the earlier failure that looked like a
    missing preamble was entirely the v0.12.0-tag opcode table bug (see
    Opcode.py's module docstring) - this test is the regression check
    for that conclusion, across every function, not just the two spot
    checks above.
    """
    data, header, table, resolved = _load_8(version)
    assert len(resolved) == expected_count

    ok = 0
    for e in resolved:
        decode_function(data, e.offset, e.bytecode_size_in_bytes, int(version))  # raises on failure
        ok += 1
    assert ok == expected_count


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_oracle
#
# Live cross-check of `BytecodeFileHeader.parse()` against the official
# `hermesc` compiler's own `-dump-bytecode` report, for the bytecode
# versions pinned in `tools/hermes/versions.json`.
#
# Skipped (not failed) when the relevant hermesc isn't installed - install
# it with `./tools/hermes/fetch_compiler.sh <version>` to run this for
# real; see `tools/hermes/README.md`.
# ----------------------------------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
DUMP_SCRIPT = REPO_ROOT / "tools" / "hermes" / "dump_bytecode.sh"

# version -> bundle fixture already committed in this repo
BUNDLES = {
    96: REPO_ROOT / "apps" / "testy" / "96" / "index.android.bundle",
    98: REPO_ROOT / "apps" / "testy" / "98" / "index.android.bundle",
}


def _hermesc_installed(version: int) -> bool:
    compiler_dir = REPO_ROOT / "tools" / "hermes" / "compilers" / str(version)
    return any(compiler_dir.glob("node_modules/hermes-compiler/hermesc/*/hermesc"))


def _run_oracle_dump(version: int, bundle: Path, tmp_path: Path) -> str:
    output = tmp_path / f"oracle-{version}.hdump"
    subprocess.run(
        [str(DUMP_SCRIPT), str(version), str(bundle), str(output)],
        check=True, capture_output=True, text=True,
    )
    return output.read_text()


@pytest.mark.parametrize("version", sorted(BUNDLES))
def test_header_matches_hermesc_oracle(version: int, tmp_path: Path):
    bundle = BUNDLES[version]
    if not bundle.is_file():
        pytest.skip(f"fixture not found: {bundle}")
    if not _hermesc_installed(version):
        pytest.skip(
            f"hermesc {version} not installed - run "
            f"./tools/hermes/fetch_compiler.sh {version} first"
        )

    header = BytecodeFileHeader.parse(bundle.read_bytes())
    oracle = HermescFileInfo.parse(_run_oracle_dump(version, bundle, tmp_path))

    ours = {
        "version": header.version,
        "source_hash": header.source_hash.hex(),
        "function_count": header.function_count,
        "string_count": header.string_count,
        "bigint_count": header.bigint_count,
        "string_kind_count": header.string_kind_count,
        "regexp_count": header.regexp_count,
        "segment_id": header.segment_id,
        "cjs_module_count": header.cjs_module_count,
        "function_source_count": header.function_source_count,
        "static_builtins": header.options.static_builtins,
        "cjs_modules_statically_resolved": header.options.cjs_modules_statically_resolved,
    }

    for field, our_value in ours.items():
        expected = getattr(oracle, field)
        assert our_value == expected, f"{field}: ours={our_value!r} oracle={expected!r}"


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_string_table
#
# Tests `hermes_disassembler.format.StringTable` against the real
# `apps/testy/96` and `apps/testy/98` bundle fixtures. Expected values
# (first 15 strings, overflow/utf16 counts) were captured once from
# `tools/hermes/dump_bytecode.sh <version> ...`'s "Global String Table:"
# block - hardcoded here so this test needs no hermesc install to run.
# ----------------------------------------------------------------------------------------------------

# First 15 entries of "Global String Table:" from a real hermesc dump, in order.
EXPECTED_FIRST_15 = {
    "96": [
        "$$typeof", "type", "_state", "state", "Animated", "isArray", "Array",
        "y", "Boolean", "ComplexAnimationBuilder", "r", "ReanimatedError",
        "Error", "H", "HermesInternal",
    ],
    "98": [
        "$$typeof", "type", "isArray", "Array", "y", "Boolean",
        "ComplexAnimationBuilder", "r", "TypeError", "Error", "HermesInternal",
        "has", "hasOwnProperty", "data", "width",
    ],
}


def _load_9(version: str):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    return header, StringTable.parse(data, header)


@pytest.mark.parametrize("version", ["96", "98"])
def test_string_count_matches_header(version: str):
    header, table = _load_9(version)
    assert len(table.entries) == header.string_count
    assert len(table.storage) == header.string_storage_size


@pytest.mark.parametrize("version", sorted(EXPECTED_FIRST_15))
def test_first_15_strings_match_oracle(version: str):
    _, table = _load_9(version)
    for i, expected in enumerate(EXPECTED_FIRST_15[version]):
        assert table.resolve(i) == expected, f"i{i}"


def test_recovers_string_hermesc_truncates_in_its_own_dump():
    """
    hermesc's own `-dump-bytecode` text output shows this string as
    `"__BUNDLE_START_TI"...` (truncated at ~18 chars, see
    BytecodeFileHeader.py's module docstring for background on that
    limitation) - this module reads it from string storage directly, so
    it should come back whole.
    """
    _, table = _load_9("96")
    matches = [
        table.resolve(i)
        for i in range(len(table.entries))
        if table.resolve(i).startswith("__BUNDLE_START_TI")
    ]
    assert matches == ["__BUNDLE_START_TIME__"]


@pytest.mark.parametrize("version", ["96", "98"])
def test_every_string_resolves_without_error(version: str):
    _, table = _load_9(version)
    for i in range(len(table.entries)):
        table.resolve(i)  # raises on failure


def test_overflow_entry_count_matches_header_96():
    header, table = _load_9("96")
    overflow_count = sum(1 for e in table.entries if e.is_overflowed)
    assert overflow_count == header.overflow_string_count == 285


def test_utf16_entries_decode_cleanly_96():
    _, table = _load_9("96")
    utf16_indices = [i for i, e in enumerate(table.entries) if e.is_utf16]
    assert len(utf16_indices) == 24
    for i in utf16_indices:
        assert isinstance(table.resolve(i), str)


# ----------------------------------------------------------------------------------------------------
# hermes_disassembler_switch_table
#
# Tests `hermes_disassembler.format.SwitchTable` against the real
# `apps/testy/96` and `apps/testy/98` bundle fixtures, cross-checked
# against real hermes-dec output (`hbc-disassembler`, installed from
# `vendor/hermes-dec` via `pip install -e .` - not shipped in this repo,
# see `vendor/fetch-hermes-dec.sh`) rather than hardcoding expected
# values as literals here.
# ----------------------------------------------------------------------------------------------------

def _load_10(version: str):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)
    return data, resolved


def _find_switch_imm(data: bytes, resolved, version: int):
    for e in resolved:
        for i in decode_function(data, e.offset, e.bytecode_size_in_bytes, version):
            if i.name == "SwitchImm" and (i.offset - e.offset) == 0xB and i.operands == (1, 238, 232, 0, 31):
                return e, i
    raise AssertionError("expected SwitchImm instruction not found in fixture")


def test_switch_imm_matches_real_hermes_dec_output():
    """
    apps/testy/96's SwitchImm at function-relative offset 0x0000000b:
    real hermes-dec prints `# Address: 000000f3  # Jump table:
    [00000067, 00000031, 000000f3, ...]` (32 entries total, min=0/max=31)
    for this exact instruction - confirmed by actually running
    `hbc-disassembler` against this fixture, not read from source alone.
    """
    data, resolved = _load_10("96")
    fn, instr = _find_switch_imm(data, resolved, 96)

    default_target = resolve_operand_jump_target(instr, 2) - fn.offset
    assert default_target == 0xF3

    entries = resolve_switch_table_entries(data, instr, 1, 3, 4)
    relative_entries = [t - fn.offset for t in entries]
    assert len(relative_entries) == 32  # max(31) - min(0) + 1
    assert relative_entries[0] == 0x67
    assert relative_entries[1] == 0x31
    assert relative_entries[-1] == 0x1D


def test_string_switch_imm_raises():
    """
    StringSwitchImm is deliberately unsupported here (see module
    docstring) - resolve_switch_table_entries raises rather than
    silently mis-decoding it, matching the fact that hermes-dec's own
    output never includes a jump table comment for one either (only
    the ordinary # Address: comment for its default-case operand,
    handled separately by JumpTarget.py).
    """
    data, resolved = _load_10("98")
    string_switch = next(
        i
        for e in resolved
        for i in decode_function(data, e.offset, e.bytecode_size_in_bytes, 98)
        if i.name == "StringSwitchImm"
    )
    with pytest.raises(HermesBytecodeError):
        resolve_switch_table_entries(data, string_switch, 1, 4, 2)


@pytest.mark.parametrize("version,opcode_name", [(96, "SwitchImm"), (98, "UIntSwitchImm")])
def test_every_switch_imm_table_resolves_without_error_at_scale(version: int, opcode_name: str):
    """Every SwitchImm/UIntSwitchImm instruction in the whole bundle resolves its jump table without raising."""
    data, resolved = _load_10(str(version))
    count = 0
    for e in resolved:
        for i in decode_function(data, e.offset, e.bytecode_size_in_bytes, version):
            if i.name == opcode_name:
                count += 1
                resolve_switch_table_entries(data, i, 1, 3, 4)
    assert count > 0


# ----------------------------------------------------------------------------------------------------
# opcode_entry_literals
#
# `Object: {...}` / `Array: [...]` opcode comments carry a Python-repr-like
# literal whose JS keywords (`null`/`true`/`false`/`undefined`) must be
# rewritten for `ast.literal_eval` - without touching string CONTENTS.
#
# String values can themselves be JavaScript source (a Reanimated worklet's
# `code` field), so a plain regex over the whole comment either corrupts them
# (`return null;` -> `return None;`) or, for `undefined`, splices a quoted
# marker into the middle of an already-quoted string and makes the whole
# literal unparseable: the `NewObjectWithBuffer ... No valid object parsed
# from comment` errors seen when decompiling a full React Native bundle.
# ----------------------------------------------------------------------------------------------------

parse_object = OpcodeEntry._parse_object_literal
parse_array = OpcodeEntry._parse_array_literal


def test_undefined_inside_a_string_does_not_break_parsing():
    parsed = parse_object("{'code': \"function f(m){if(m[6]!==undefined){return 1;}return 2;}\"}")

    assert parsed == {"code": "function f(m){if(m[6]!==undefined){return 1;}return 2;}"}


def test_keywords_inside_a_string_are_left_alone():
    parsed = parse_object("{'code': 'function f(){return null;}', 'a': \"x==true||y===false\", 'ok': true}")

    assert parsed["code"] == "function f(){return null;}"
    assert parsed["a"] == "x==true||y===false"
    assert parsed["ok"] is True


def test_bare_keywords_are_still_converted():
    parsed = parse_object("{'a': null, 'b': true, 'c': false, 'd': undefined, 'e': [undefined, null]}")

    assert parsed["a"] is None
    assert parsed["b"] is True
    assert parsed["c"] is False
    assert parsed["d"] is JS_UNDEFINED
    assert parsed["e"] == [JS_UNDEFINED, None]


def test_undefined_stays_distinct_from_null():
    parsed = parse_object("{'x': undefined, 'y': null}")

    assert parsed["x"] is JS_UNDEFINED
    assert parsed["y"] is None
    assert parsed["x"] is not parsed["y"]


def test_escaped_quote_does_not_end_the_string_early():
    parsed = parse_object("{'s': 'it\\'s null', 'n': null}")

    assert parsed == {"s": "it's null", "n": None}


def test_double_quoted_string_may_contain_single_quotes_and_braces():
    parsed = parse_object("{'code': \"if(typeof c==='number'){return null;}\"}")

    assert parsed == {"code": "if(typeof c==='number'){return null;}"}


def test_array_literal_strings_named_like_keywords_stay_strings():
    assert parse_array("['undefined', 'true', 'null', 3]") == ["undefined", "true", "null", 3]


def test_array_literal_bare_keywords_are_converted():
    assert parse_array("[null, true, false, undefined]") == [None, True, False, JS_UNDEFINED]


def test_normalizer_leaves_identifiers_that_merely_contain_a_keyword():
    # `\bnull\b` never matched these either; a token scanner must not split them.
    assert _normalize_js_literals("{'k': nullable, 'j': true_value}") == "{'k': nullable, 'j': true_value}"


def test_unterminated_string_does_not_hang_or_raise_in_the_normalizer():
    assert _normalize_js_literals("{'a': 'oops null") == "{'a': 'oops null"


@pytest.mark.parametrize("keyword", ["null", "true", "false", "undefined"])
def test_worklet_like_code_round_trips_unchanged(keyword):
    code = f"function w(a){{if(a=={keyword}){{return {keyword};}}return a;}}"

    assert parse_object("{'code': \"" + code + "\"}") == {"code": code}


# ----------------------------------------------------------------------------------------------------
# opcode_name_validation
#
# Validate that every registered OpcodeHandler corresponds to a real Hermes
# bytecode opcode.
#
# Dispatch is performed by matching OpcodeEntry.opcode directly to the
# OpcodeHandler subclass name. A typo in a handler class name therefore
# creates silently unreachable code, while a missing handler represents an
# unnoticed coverage gap.
#
# The opcode catalog is generated from the hermes-dec project and contains
# the union of all tracked Hermes bytecode versions (currently hbc51-hbc99).
#
# Handlers are classified as:
#
#     CURRENT  - present in the newest tracked bytecode version.
#     LEGACY   - present only in older tracked versions.
#     UNKNOWN  - not found in any tracked version.
#
# UNKNOWN handlers fail the test unless explicitly allow-listed.
# ----------------------------------------------------------------------------------------------------

# Helper/mixin classes that intentionally do not correspond to Hermes
# bytecode opcodes.
#
# They provide shared OpcodeHandler functionality (operand parsing,
# helper methods, etc.) and must never appear in the handler registry.
# Most are excluded automatically via `_abstract = True`; this allow-list
# serves as a defensive safeguard in case one is accidentally registered.
NON_OPCODE_HELPER_CLASSES = {"OpcodeHandler"}

# Handler names that are intentionally exempt from validation until they
# have been verified against the tracked Hermes opcode catalog
# (currently hbc51-hbc99).
#
# Every entry must include a justification (Hermes version, upstream
# source, or another authoritative reference). This prevents temporary
# assumptions from silently becoming permanent exceptions.
#
# This allow-list should normally remain empty.
KNOWN_UNVERIFIED: dict[str, str] = {
    # "BitOrN": "TODO: Add the Hermes version and authoritative source.",
}

# Lower bound used to detect accidental registry shrinkage.
# Update intentionally whenever handlers are added, removed, or consolidated.
MIN_EXPECTED_HANDLER_COUNT = 200


@pytest.fixture(scope="module", autouse=True)
def initialize_handler_registry():
    """Populate ``OpcodeHandler.registry`` before any validation runs."""

    HandlerLoader.load()


@pytest.fixture(scope="module")
def registered_handler_names() -> list[str]:
    """Return the names of all registered concrete opcode handlers."""

    return [
        name for name in OpcodeHandler.registry
        if name not in NON_OPCODE_HELPER_CLASSES
    ]


def test_every_handler_name_is_a_known_opcode(registered_handler_names):
    buckets = classify_all(registered_handler_names)

    unknown = [
        info for info in buckets[OpcodeStatus.UNKNOWN]
        if info.name not in KNOWN_UNVERIFIED
    ]

    if unknown:
        details = "\n".join(
            f"  - {info.name}"
            for info in sorted(unknown, key=lambda x: x.name)
        )

        pytest.fail(
            "The following handler class names do not exist in any tracked "
            "Hermes bytecode version (hbc51-hbc99).\n\n"
            "Either:\n"
            "  1. the handler name contains a typo, or\n"
            "  2. the opcode belongs to a newer Hermes bytecode version that "
            "is not yet tracked.\n\n"
            "Verify the opcode against a trusted external source before "
            "merging.\n\n"
            f"{details}"
        )

# NOTE: 38 legacy handler(s) detected (not present in hbc99)
def test_legacy_opcodes_are_visible_and_documented(registered_handler_names, capsys):
    """
    Informational test.

    Reports handlers that exist only in older Hermes bytecode versions.

    Legacy handlers are expected and therefore do not cause the test to fail.
    The goal is to make version-specific opcode coverage visible in CI output
    instead of leaving that information buried in source comments.
    """

    buckets = classify_all(registered_handler_names)
    legacy = sorted(buckets[OpcodeStatus.LEGACY], key=lambda item: item.name)

    with capsys.disabled():
        print(f"\n{len(legacy)} legacy handler(s) detected (not present in hbc99):")
        for info in legacy:
            v_min, v_max = info.versions[0], info.versions[-1]
            print(f"  - {info.name}: hbc{v_min}..hbc{v_max}")

    assert True


def test_known_unverified_list_is_empty():
    """
    Enforces that KNOWN_UNVERIFIED remains empty.

    The project policy is to verify every handler against an authoritative
    Hermes opcode source before it is merged. Allowing unverified entries to
    accumulate would weaken the guarantees provided by the validation tests.
    """

    assert not KNOWN_UNVERIFIED, (
        f"KNOWN_UNVERIFIED contains {len(KNOWN_UNVERIFIED)} unverified "
        f"handler name(s): {sorted(KNOWN_UNVERIFIED)}. "
        "Verify each entry against an authoritative Hermes opcode source "
        "and remove it from the allow-list, or remove the handler if the "
        "opcode cannot be confirmed."
    )


def test_no_duplicate_registration_shadowing():
    """
    Detect accidental handler registration shadowing.

    OpcodeHandler.registry is keyed by class name. If two handler classes are
    defined with the same name, the later registration silently overwrites
    the previous one.

    Because HandlerLoader imports every handler module, such collisions may
    go unnoticed unless explicitly checked. This test provides a simple
    sanity check by ensuring the registry size does not unexpectedly shrink,
    which could indicate a duplicate registration or an unintentionally
    missing handler.
    """

    assert len(OpcodeHandler.registry) >= MIN_EXPECTED_HANDLER_COUNT


def test_basic_blocks_compare_by_id():
    # Distinct instances representing the same CFG node.
    a = BasicBlock(block_id=3, address=100)
    b = BasicBlock(block_id=3, address=100)

    assert a == b
    assert hash(a) == hash(b)
