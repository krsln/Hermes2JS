"""
Tests `hermes_disassembler.format.FunctionHeaderOverflow` against the
real `apps/testy/96` and `apps/testy/98` bundle fixtures.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from hermes_disassembler.core.Exceptions import HermesBytecodeError
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.FunctionHeader import parse_function_headers
from hermes_disassembler.format.FunctionHeaderOverflow import (
    _SMALL_BYTECODE_SIZE_LIMIT,
    resolve_overflowed_headers,
)
from hermes_disassembler.format.StringTable import StringTable

APPS_TESTY = Path(__file__).resolve().parent.parent / "apps" / "testy"


def _load(version: str):
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
    _, _, _, resolved = _load(version)
    assert all(not e.is_overflowed for e in resolved)


@pytest.mark.parametrize("version", ["96", "98"])
def test_every_resolved_large_header_has_a_sane_name(version: str):
    _, header, table, resolved = _load(version)
    large = [e for e in resolved if e.was_large_header]
    assert large  # sanity: there are some to resolve for both fixtures
    for e in large:
        name = table.resolve(e.function_name)  # raises on failure
        assert isinstance(name, str)


def test_v96_overflowed_functions_resolved():
    # from tools/hermes/dump_bytecode.sh 96: the global function overflows
    # (bytecode > 32767 bytes, v96's small-header limit) and resolves to
    # exactly "global" with param_count=1.
    _, _, table, resolved = _load("96")
    global_fn = next(e for e in resolved if e.was_large_header and table.resolve(e.function_name) == "global")
    assert global_fn.param_count == 1
    assert global_fn.bytecode_size_in_bytes > _SMALL_BYTECODE_SIZE_LIMIT[96]


def test_v98_previously_unreachable_signatures_now_resolve():
    # These four were unreachable before overflow resolution (see
    # test_hermes_disassembler_function_header.py's test_known_signature_found_98
    # comment) - v98's 8-bit FunctionName field pushed them into the
    # overflowed 78%. All four should resolve now.
    _, _, table, resolved = _load("98")
    signatures = {(table.resolve(e.function_name), e.param_count) for e in resolved}
    for target in [("clear", 1), ("define", 4), ("metroRequire", 3), ("metroImportDefault", 3)]:
        assert target in signatures


def test_pass_through_when_nothing_overflowed():
    """resolve_overflowed_headers on an all-non-overflowed tuple should be a no-op."""
    from hermes_disassembler.format.FunctionHeader import FuncKind, FunctionHeaderEntry, ProhibitInvoke

    entry = FunctionHeaderEntry(
        index=0, is_overflowed=False, offset=1, param_count=1,
        bytecode_size_in_bytes=1, function_name=1, frame_size=1,
        prohibit_invoke=ProhibitInvoke.NONE, strict_mode=False,
        has_exception_handler=False, has_debug_info=False, kind=FuncKind.NORMAL,
    )
    data, header, _, _ = _load("96")
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
