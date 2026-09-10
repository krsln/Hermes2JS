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
  immediately after that 37-byte (`LARGE_HEADER_SIZE`) struct, padded
  up to the next 4-byte boundary. Confirmed against apps/testy/98
  function index 1: `info_offset + 37` landed 3 bytes before a valid
  table (37+3=40, a multiple of 4 - the missing alignment step), whose
  single entry `(start=3, end=42, target=42)` again lines up exactly:
  `start=3` is that function's `GetGlobalObject`, `target=42` is its
  `Catch`.

Why this needed empirical confirmation rather than reading
`lib/BCGen/HBC/BytecodeStream.cpp`'s `serializeFunctionInfo` alone: that
writer function's code reads as if it unconditionally writes a 37-byte
large-header duplicate before the exception table for ANY function
needing one (exception handler OR debug info OR doesn't fit small) -
but the non-overflowed case above has no such duplicate. Either the
reading missed a condition, or the comment ("write large header if it
doesn't fit in a small") was accurate and the surrounding code review
mis-traced control flow - either way, the two real, cross-validated
data points above are the actual ground truth this module relies on,
not the source reading alone.

Known gap: `has_debug_info` functions (0 in apps/testy/96, 0 in
apps/testy/98 per FunctionHeaderOverflow's own mass counts) aren't
covered - `serializeDebugOffsets` writes its own data after the
exception handler table (or in its place, if there's no exception
handler), and this module doesn't account for that offset shift. Every
function in both test fixtures has `has_debug_info=False`, so this has
had no real bundle to validate against; don't trust this module for a
`has_debug_info=True` function without checking that first.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass

from hermes_disassembler.core.Exceptions import HermesBytecodeError, TruncatedFileError
from hermes_disassembler.format.FunctionHeader import FunctionHeaderEntry
from hermes_disassembler.format.FunctionHeaderOverflow import LARGE_HEADER_SIZE

__all__ = ["ExceptionHandler", "resolve_exception_handlers", "INFO_ALIGNMENT"]

#: hermes/lib/BCGen/HBC/BytecodeStream.cpp: INFO_ALIGNMENT (same value as
#: BYTECODE_ALIGNMENT elsewhere in this package - confirmed empirically
#: here via the 37+3=40 alignment gap described in the module docstring,
#: not independently verified against the source's own constant value).
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


def resolve_exception_handlers(
        data: bytes, entry: FunctionHeaderEntry
) -> tuple[ExceptionHandler, ...]:
    """
    Read `entry`'s exception handler table (see module docstring for
    the two location rules). Returns an empty tuple if
    `entry.has_exception_handler` is False.

    Raises `HermesBytecodeError` if `has_exception_handler` is True but
    `entry.info_offset` is `None` (shouldn't happen for a correctly
    resolved entry - see `FunctionHeader.parse_function_headers` and
    `FunctionHeaderOverflow.resolve_overflowed_headers`) and
    `TruncatedFileError` if the table would read past the end of `data`.
    """
    if not entry.has_exception_handler:
        return ()

    if entry.info_offset is None:
        raise HermesBytecodeError(
            f"function {entry.index} has has_exception_handler=True but no "
            f"info_offset - can't locate its exception handler table"
        )

    table_start = (
        _align_up(entry.info_offset + LARGE_HEADER_SIZE)
        if entry.was_large_header
        else entry.info_offset
    )

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
