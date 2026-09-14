"""
Resolves a function's exception handler table: `[start, end)` try-block
byte ranges (relative to the function's own start, same convention as
`Instruction.offset` minus the function offset) and the `target` byte
offset of each range's `catch` handler.

Two different locations, confirmed empirically against real bundles
(not derived from source alone - see the discrepancy this resolved,
below):

  Non-overflowed function (`was_large_header=False`) with
  `has_exception_handler=True`: the table sits DIRECTLY at
  `entry.info_offset` (a field in the *small* `SmallFuncHeader` itself -
  see `FunctionHeader.py`'s `_decode_v96`). No large-header duplicate
  precedes it. Confirmed against apps/testy/96 function index 7
  (`guardedLoadModule`): `info_offset` decoded to a `count=1` entry
  `(start=42, end=62, target=64)` that lines up EXACTLY with that
  function's own decoded instructions - `start=42` is precisely where
  its try-guarded `Call4` sequence begins, `end=62` is precisely its
  `Jmp` out of the try block (confirming `end` is exclusive, per
  facebook/hermes's own `HBCExceptionHandlerInfo` doc comment: "End
  offset of the try, exclusive"), and `target=64` is precisely its
  `Catch` instruction.

  Overflowed function (`was_large_header=True`): `entry.info_offset`
  is the byte offset of that function's own *large* `FunctionHeader`
  (see `FunctionHeaderOverflow.py`, which sets `info_offset` to the
  same `large_offset` it resolves the header from) - the table follows
  immediately after that struct (`VERSION_TO_LARGE_HEADER_SIZE[version]`
  bytes - 31 for v96, 36 for v98; NOT a flat 37 for both, see that
  module's docstring for why), padded up to the next 4-byte boundary.
  Confirmed against apps/testy/98 function index 1: `info_offset + 36`
  landed 2 bytes before a valid table (36+2=38, a multiple of 4 - the
  missing alignment step), whose single entry `(start=3, end=42,
  target=42)` again lines up exactly: `start=3` is that function's
  `GetGlobalObject`, `target=42` is its `Catch`.

Why this needed empirical confirmation rather than reading
`lib/BCGen/HBC/BytecodeStream.cpp`'s `serializeFunctionInfo` alone: that
writer function's code reads as if it unconditionally writes a
large-header duplicate before the exception table for ANY function
needing one (exception handler OR debug info OR doesn't fit small) -
but the non-overflowed case above has no such duplicate. Either the
reading missed a condition, or the comment ("write large header if it
doesn't fit in a small") was accurate and the surrounding code review
mis-traced control flow - either way, the two real, cross-validated
data points above are the actual ground truth this module relies on,
not the source reading alone.

`has_debug_info` functions: `serializeDebugOffsets` writes its own
12-byte `DebugOffsets` struct (see `DebugOffsets.py`) after the
exception handler table - or in its place, at the same aligned
position, if the function has no exception handler at all - confirmed
against P1sec/hermes-dec's own `hbc_file_parser.py` (`read_functions`:
exception handler read, THEN debug info read, both gated
independently, both preceded by their own alignment step). This module
only ever needs to know WHERE that table starts, which is unaffected
by whether debug info follows it - `_locate_table_start` below is also
reused by `DebugOffsets.py` to find where the exception table (if
any) ENDS, since that's where the `DebugOffsets` struct begins.

Previously documented here as an unvalidated/known-bad case: apps/testy/96
function index 0 ("global"), believed to be simultaneously
`was_large_header=True` and `has_exception_handler=True` with a
handler table that didn't land on real instruction boundaries. That
belief was itself downstream of a bug in `FunctionHeaderOverflow.py`
(the old, wrong `LARGE_HEADER_SIZE=37` misread that function's flags
byte from 6 bytes past its real position). With that fixed,
"global"'s real flags decode to `has_exception_handler=False` -
confirmed against `tools/hermes/dump_bytecode.sh`'s own oracle output,
which has no "Exception Handlers:" block anywhere in that function's
listing. See `tests/test_hermes_disassembler_exception_handler_table.py`.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass

from hermes_disassembler.core.Exceptions import HermesBytecodeError, TruncatedFileError
from hermes_disassembler.format.FunctionHeader import FunctionHeaderEntry
from hermes_disassembler.format.FunctionHeaderOverflow import VERSION_TO_LARGE_HEADER_SIZE

__all__ = ["ExceptionHandler", "resolve_exception_handlers", "INFO_ALIGNMENT"]

#: hermes/lib/BCGen/HBC/BytecodeStream.cpp: INFO_ALIGNMENT (same value as
#: BYTECODE_ALIGNMENT elsewhere in this package - confirmed empirically
#: here via the alignment gap described in the module docstring, not
#: independently verified against the source's own constant value).
INFO_ALIGNMENT = 4

_TABLE_HEADER_SIZE = 4  # ExceptionHandlerTableHeader: uint32_t count
_ENTRY_SIZE = 12  # HBCExceptionHandlerInfo: uint32_t start, end, target


def _align_up(offset: int, alignment: int = INFO_ALIGNMENT) -> int:
    remainder = offset % alignment
    return offset if remainder == 0 else offset + (alignment - remainder)


@dataclass(frozen=True, slots=True)
class ExceptionHandler:
    """One `HBCExceptionHandlerInfo` entry, offsets relative to the owning function's start (same convention as `Instruction.offset - function.offset`)."""

    start: int  # inclusive
    end: int  # exclusive
    target: int  # the `catch` handler's instruction offset


def _locate_table_start(entry: FunctionHeaderEntry, version: int) -> int:
    """
    Byte offset where `entry`'s exception handler table would start (or
    would have started, if it had one) - i.e. `entry.info_offset`
    itself for a non-overflowed function, or the aligned position right
    after its large-header duplicate for an overflowed one. Shared by
    `resolve_exception_handlers` below and `DebugOffsets.py`, which
    needs this same position as its own search's starting point.

    Raises `HermesBytecodeError` if `entry.was_large_header` but
    `version` has no confirmed large-header size (see
    `FunctionHeaderOverflow.VERSION_TO_LARGE_HEADER_SIZE`).
    """
    if entry.info_offset is None:
        raise HermesBytecodeError(
            f"function {entry.index} has no info_offset - can't locate its "
            f"exception handler table / debug offsets position"
        )

    if not entry.was_large_header:
        return entry.info_offset

    if version not in VERSION_TO_LARGE_HEADER_SIZE:
        raise HermesBytecodeError(
            f"no confirmed large FunctionHeader size for bytecode version "
            f"{version} (known: {sorted(VERSION_TO_LARGE_HEADER_SIZE)}) - "
            f"can't locate function {entry.index}'s exception handler table"
        )
    return _align_up(entry.info_offset + VERSION_TO_LARGE_HEADER_SIZE[version])


def locate_after_exception_handlers(data: bytes, entry: FunctionHeaderEntry, version: int) -> int:
    """
    Byte offset immediately after `entry`'s exception handler table
    (aligned to `INFO_ALIGNMENT`) - or, if `entry.has_exception_handler`
    is False, the same position `_locate_table_start` would return
    (there's no table to skip past). This is where `DebugOffsets.py`
    looks for a `has_debug_info=True` function's `DebugOffsets` struct,
    matching hermes-dec's own sequential read order (exception table
    first, if present, then debug offsets - see module docstring).

    Raises the same errors as `resolve_exception_handlers` for a
    genuinely-present table that can't be located or read.
    """
    table_start = _locate_table_start(entry, version)
    if not entry.has_exception_handler:
        return table_start

    count_end = table_start + _TABLE_HEADER_SIZE
    if len(data) < count_end:
        raise TruncatedFileError("ExceptionHandlerTableHeader", count_end, len(data))
    (count,) = struct.unpack_from("<I", data, table_start)

    entries_end = count_end + count * _ENTRY_SIZE
    if len(data) < entries_end:
        raise TruncatedFileError("exception handler entries", entries_end, len(data))

    # The exception table's own byte length (4 + count*12) is always a
    # multiple of 4, so this align-up is a no-op in practice - kept for
    # symmetry with hermes-dec's own unconditional align-before-each-read.
    return _align_up(entries_end)


def resolve_exception_handlers(
        data: bytes, entry: FunctionHeaderEntry, version: int
) -> tuple[ExceptionHandler, ...]:
    """
    Read `entry`'s exception handler table (see module docstring for
    the two location rules). Returns an empty tuple if
    `entry.has_exception_handler` is False.

    `version` is required to size a large-header duplicate correctly
    when `entry.was_large_header` (see `FunctionHeaderOverflow.py`'s
    `VERSION_TO_LARGE_HEADER_SIZE`) - unused otherwise.

    Raises `HermesBytecodeError` if `has_exception_handler` is True but
    `entry.info_offset` is `None` (shouldn't happen for a correctly
    resolved entry - see `FunctionHeader.parse_function_headers` and
    `FunctionHeaderOverflow.resolve_overflowed_headers`) and
    `TruncatedFileError` if the table would read past the end of `data`.
    """
    if not entry.has_exception_handler:
        return ()

    table_start = _locate_table_start(entry, version)

    count_end = table_start + _TABLE_HEADER_SIZE
    if len(data) < count_end:
        raise TruncatedFileError("ExceptionHandlerTableHeader", count_end, len(data))
    (count,) = struct.unpack_from("<I", data, table_start)

    entries_end = count_end + count * _ENTRY_SIZE
    if len(data) < entries_end:
        raise TruncatedFileError("exception handler entries", entries_end, len(data))

    return tuple(
        ExceptionHandler(*struct.unpack_from("<III", data, count_end + i * _ENTRY_SIZE))
        for i in range(count)
    )
