"""
Resolves a function's `DebugOffsets` struct - the 12-byte, 3x uint32_t
structure (`sourceLocations`, `scopeDescData`, `textifiedCallees`) that
`serializeDebugOffsets` writes for any `has_debug_info=True` function,
confirmed against P1sec/hermes-dec's own `hbc_file_parser.py`
(`HBCReader.get_debug_offsets_reader`, fetched via
`vendor/fetch-hermes-dec.sh`) - the same source that uncovered the
`LARGE_HEADER_SIZE` bug this module's own position lookup now depends
on (see `FunctionHeaderOverflow.py`'s module docstring).

This is validation-tooling-adjacent, not a full debug-info parser: the
three fields exposed here are themselves just byte OFFSETS into the
separate debug-info blob (source locations table, scope descriptor
table, textified-callees table) described near the end of
`hermes_disassembler`'s own package docstring's "not covered" list -
resolving what those tables actually contain is out of scope here.
What this module resolves is only WHERE that struct sits and what its
three raw offset values are - matching exactly what real hermes-dec's
own disassembler prints for a `has_debug_info=True` function (a
`[Debug offsets: source_locs=0x..., scope_desc_data=0x...]` line - see
`HasmWriter.py`), which likewise never decodes the tables those
offsets point to.

Location: immediately after `entry`'s exception handler table (if
`entry.has_exception_handler`) or at the same aligned position
`ExceptionHandlerTable._locate_table_start` would use (if not) - see
`ExceptionHandlerTable.locate_after_exception_handlers`, which this
module builds on directly rather than re-deriving.

Validated against apps/testy/96 function index 1791 - the one real
function in either test fixture with BOTH `has_exception_handler=True`
and `has_debug_info=True` (found only after the `LARGE_HEADER_SIZE` fix
corrected its previously-misdetected flags; it used to crash
`ExceptionHandlerTable.resolve_exception_handlers` outright with a
`TruncatedFileError` reading ~2.6MB past a wrong offset) - resolving
cleanly to a `DebugOffsets` struct sitting immediately after that
function's own (now-correctly-located) exception handler table.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass

from hermes_disassembler.core.Exceptions import TruncatedFileError
from hermes_disassembler.format.ExceptionHandlerTable import locate_after_exception_handlers
from hermes_disassembler.format.FunctionHeader import FunctionHeaderEntry

__all__ = ["DebugOffsets", "resolve_debug_offsets"]

_STRUCT_SIZE = 12  # 3x uint32_t: sourceLocations, scopeDescData, textifiedCallees


@dataclass(frozen=True, slots=True)
class DebugOffsets:
    """Raw byte offsets into the separate debug-info tables this package doesn't otherwise parse (see module docstring)."""

    source_locations: int
    scope_desc_data: int
    textified_callees: int


def resolve_debug_offsets(data: bytes, entry: FunctionHeaderEntry, version: int) -> DebugOffsets | None:
    """
    Returns `entry`'s `DebugOffsets` struct, or `None` if
    `entry.has_debug_info` is False.

    `version` is required (threaded through to
    `ExceptionHandlerTable.locate_after_exception_handlers`) to size a
    large-header duplicate correctly when `entry.was_large_header`.

    Raises `HermesBytecodeError`/`TruncatedFileError` under the same
    conditions as `ExceptionHandlerTable.resolve_exception_handlers`
    (bad `info_offset`, unconfirmed large-header size, or a read past
    the end of `data`).
    """
    if not entry.has_debug_info:
        return None

    offset = locate_after_exception_handlers(data, entry, version)
    end = offset + _STRUCT_SIZE
    if len(data) < end:
        raise TruncatedFileError("DebugOffsets", end, len(data))

    source_locations, scope_desc_data, textified_callees = struct.unpack_from("<III", data, offset)
    return DebugOffsets(
        source_locations=source_locations,
        scope_desc_data=scope_desc_data,
        textified_callees=textified_callees,
    )
