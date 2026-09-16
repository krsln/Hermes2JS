"""
Tests `hermes_disassembler.format.DebugOffsets` - synthetically, since
neither `apps/testy/96` nor `apps/testy/98` currently has a single real
`has_debug_info=True` function to test against (see that module's own
docstring for why, and `ExceptionHandlerTable.py`'s for the bug whose
fix made that discoverable in the first place). The real fixtures are
still used to confirm the negative case (no function in either bundle
resolves anything here) at scale.
"""
from __future__ import annotations

import struct
from pathlib import Path

import pytest

from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.DebugOffsets import DebugOffsets, resolve_debug_offsets
from hermes_disassembler.format.ExceptionHandlerTable import resolve_exception_handlers
from hermes_disassembler.format.FunctionHeader import (
    FunctionKind,
    FunctionHeaderEntry,
    ProhibitInvoke,
    parse_function_headers,
)
from hermes_disassembler.format.FunctionHeaderOverflow import resolve_overflowed_headers

APPS_TESTY = Path(__file__).resolve().parent.parent / "apps" / "testy"


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
