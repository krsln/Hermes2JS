"""
Resolves an overflowed `SmallFuncHeader` (see `FunctionHeader.py`'s
"Known gap" section) to the full-size `FunctionHeader` struct its
`getLargeHeaderOffset()` points to.

`getLargeHeaderOffset()`'s encoding, confirmed from facebook/hermes's
MIT-licensed `include/hermes/BCGen/HBC/BytecodeFileFormat.h` at the same
two commits used throughout this package:

  LAYOUT_V96 (v0.12.0): `getLargeHeaderOffset() = (infoOffset << 16) |
  offset` (both taken from the *small* header's own 25-bit fields, which
  is why they're all that's meaningful once overflowed - see
  `SmallFuncHeader::setLargeHeaderOffset`).
  https://github.com/facebook/hermes/blob/v0.12.0/include/hermes/BCGen/HBC/BytecodeFileFormat.h

  LAYOUT_V98 (cb5bb334...): `getLargeHeaderOffset() = (functionName <<
  24) | (offset & 0xffffff)` - a different encoding than v96's (uses
  FunctionName's 8 bits as the high byte, not a dedicated infoOffset
  field - v98's SmallFuncHeader has no infoOffset at all, see
  `FunctionHeader.py`).
  https://github.com/facebook/hermes/blob/cb5bb3342f43d378cc2653e2ac9077a282b97637/include/hermes/BCGen/HBC/BytecodeFileFormat.h

The large struct's own BYTE SIZE, `VERSION_TO_LARGE_HEADER_SIZE` below,
was originally guessed at a flat 37 bytes for BOTH versions (every
sub-field read as full-width, 4 bytes each, regardless of its real
width). That guess turned out to be wrong for v96 and - despite
looking wrong by the same reasoning - actually RIGHT for v98, for two
unrelated reasons uncovered separately:

  LAYOUT_V96: confirmed WRONG. offset, paramCount, bytecodeSizeInBytes,
  functionName, infoOffset, frameSize, environmentSize (7 x uint32_t =
  28 bytes) + highestReadCacheIndex, highestWriteCacheIndex (2 x
  uint8_t, NOT uint32_t = 2 bytes) + 1-byte `FunctionHeaderFlag` = 31
  bytes, not 37 - confirmed two independent ways: (1) diffing against
  P1sec/hermes-dec's own `hbc_file_parser.py`
  (`HBCReader.get_large_func_header_reader()`, fetched via
  `vendor/fetch-hermes-dec.sh`, not shipped in this repo - its ctypes
  struct definition is unambiguous that these trailing fields are
  `c_uint8`, not `c_uint32`), and (2) independently, by brute-force
  testing every candidate struct size from 24 to 41 bytes against every
  overflowed, `has_exception_handler=True` function in apps/testy/96
  and keeping the one whose resulting exception handler table entries
  land on real instruction boundaries - only 31 does (2/2 functions,
  the only two that exist in this fixture; every other candidate size
  gives 0/2).

  LAYOUT_V98: confirmed RIGHT, but not for the reason originally
  assumed (matching v96's byte-width mistake) - 37 genuinely is this
  struct's real size. hermes-dec's OWN size for this layout (36 bytes -
  Offset, ParamCount, LoopDepth, BytecodeSizeInBytes, FunctionName,
  NumberRegCount, NonPtrRegCount, FrameSize as 8 x uint32_t, +
  ReadCacheSize, WriteCacheSize, PrivateNameCacheSize as 3 x uint8_t, +
  1-byte flags) is ITSELF WRONG - one byte short, most likely a field
  hermes-dec's reader omits entirely between PrivateNameCacheSize and
  the flags byte. This was NOT caught by diffing against hermes-dec (its
  own output looked internally consistent) but by the same brute-force
  method used for v96 above, applied across the first 3000 overflowed
  functions in apps/testy/98: hermes-dec's own 36-byte size resolves
  a `has_exception_handler=True` table that lands cleanly on real
  instruction boundaries for 0 of the functions it flags as having one;
  37 bytes resolves 109/109 cleanly. This matches what's already been
  independently reported about hermes-dec's own disassembler output for
  bytecode 98: it fails to surface exception handlers there at all -
  consistent with its large-header reader silently misreading every
  v98 overflowed function's flags byte (from one byte before its real
  position), including `hasExceptionHandler` itself.

Consequences of the old, wrong FLAT 37-for-both guess: for v96 only,
the flags byte was read 6 bytes past its real position, corrupting
every flag the large header carries (`has_exception_handler`,
`has_debug_info`, `strict_mode`, `kind`, `prohibit_invoke`) for every
`was_large_header=True` entry in that version - not just downstream
consumers that use `LARGE_HEADER_SIZE` to locate data *after* the
struct (see `ExceptionHandlerTable.py`). Concretely, in apps/testy/96:
the "global" function (index 0) - previously documented here and in
`ExceptionHandlerTable.py` as a confirmed `has_exception_handler=True`
"known-bad" case whose handler table formula mysteriously didn't line
up - was a MISDETECTION: with the corrected 31-byte size its flags
byte decodes to `has_exception_handler=False`, matching
`tools/hermes/dump_bytecode.sh`'s own real hermesc oracle dump exactly
(no "Exception Handlers:" block anywhere in its ~7500-line listing).
At scale, every `has_exception_handler=True` function in apps/testy/96
now resolves cleanly (398 functions, 660 handler entries, 660/660
landing on real instruction boundaries - up from the 0.9-ratio
tolerance the "known-bad" case previously required). v98 was already
correct at this same flat value by coincidence, so it was already at
660/660-equivalent 1082/1082 before this fix and remains so after -
see `tests/test_hermes_disassembler_exception_handler_table.py`.

  bytecode 99: intentionally UNSUPPORTED here (see
  `VERSION_TO_LARGE_HEADER_LAYOUT` below). Given how easy both
  known-version sizes above turned out to be to get wrong even with a
  real bundle to test against, guessing 99's size from its shared
  *compact* SmallFuncHeader layout (see StringTable.py) without an
  apps/testy/99 fixture to brute-force against would be exactly the
  mistake this module's own history warns against - so it still
  doesn't.

Validated against every overflowed function in apps/testy/96 and
apps/testy/98: `function_name` resolves to a non-empty, plausible
identifier through `StringTable.resolve()` for all of them, and
`bytecode_size_in_bytes` exceeds the corresponding version's small-header
limit (32767 for v96, 16383 for v98) - the two facts our earlier
manual inspection of function 0 relied on, now checked against every
overflowed entry rather than just one; see
`tests/test_hermes_disassembler_function_header_overflow.py`.
"""
from __future__ import annotations

import struct

from hermes_disassembler.core.Exceptions import HermesBytecodeError, TruncatedFileError
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.FunctionHeader import (
    FuncKind,
    FunctionHeaderEntry,
    ProhibitInvoke,
)

__all__ = [
    "resolve_overflowed_headers", "VERSION_TO_LARGE_HEADER_LAYOUT",
    "VERSION_TO_LARGE_HEADER_SIZE",
]

# Small-header limits each version's large-header path exists to work
# around - the field width in SmallFuncHeader that most commonly
# overflows in practice. Exposed for tests/diagnostics, not load-bearing.
_SMALL_BYTECODE_SIZE_LIMIT = {96: (1 << 15) - 1, 98: (1 << 14) - 1, 99: (1 << 14) - 1}

#: Size in bytes of the "large" FunctionHeader struct, per version - the
#: two layouts are NOT the same size (31 vs 37 bytes; see module
#: docstring for the field-by-field breakdown and the bug this corrects).
#: Exported for ExceptionHandlerTable.py, which reads the exception
#: handler table (and DebugOffsets.py, which reads the debug offsets
#: struct) immediately after this struct for an overflowed function. 99
#: is intentionally absent - see module docstring.
VERSION_TO_LARGE_HEADER_SIZE: dict[int, int] = {96: 31, 98: 37}


def _large_offset_v96(small: bytes) -> int:
    w1, _w2, w3 = struct.unpack_from("<III", small, 0)
    offset = w1 & 0x1FF_FFFF
    info_offset = w3 & 0x1FF_FFFF
    return (info_offset << 16) | offset


def _large_offset_v98(small: bytes) -> int:
    w1, w2 = struct.unpack_from("<II", small, 0)
    offset = w1 & 0x1FF_FFFF
    function_name = (w2 >> 14) & 0xFF
    return (function_name << 24) | (offset & 0xFF_FFFF)


def _decode_large_v96(data: bytes, large_offset: int, index: int) -> FunctionHeaderEntry:
    size = VERSION_TO_LARGE_HEADER_SIZE[96]
    if large_offset + size > len(data):
        raise TruncatedFileError(f"large FunctionHeader for function {index}", large_offset + size, len(data))
    (offset, param_count, bytecode_size, function_name, _info_offset, frame_size,
     _env_size) = struct.unpack_from("<7I", data, large_offset)
    # highestReadCacheIndex/highestWriteCacheIndex: 1 byte each (not 4 -
    # see module docstring), at offsets 28/29; unused here, so skipped
    # rather than unpacked.
    flags = data[large_offset + 30]
    return FunctionHeaderEntry(
        index=index, is_overflowed=False, was_large_header=True,
        offset=offset, info_offset=large_offset, param_count=param_count,
        bytecode_size_in_bytes=bytecode_size,
        function_name=function_name, frame_size=frame_size,
        prohibit_invoke=ProhibitInvoke(flags & 0b11),
        strict_mode=bool((flags >> 2) & 1),
        has_exception_handler=bool((flags >> 3) & 1),
        has_debug_info=bool((flags >> 4) & 1),
        kind=FuncKind.NORMAL,  # v96's kind bits are always 0 in practice - see FunctionHeader.py
    )


def _decode_large_v98(data: bytes, large_offset: int, index: int) -> FunctionHeaderEntry:
    size = VERSION_TO_LARGE_HEADER_SIZE[98]
    if large_offset + size > len(data):
        raise TruncatedFileError(f"large FunctionHeader for function {index}", large_offset + size, len(data))
    (offset, param_count, _loop_depth, bytecode_size, function_name,
     _number_reg, _non_ptr_reg, frame_size) = struct.unpack_from("<8I", data, large_offset)
    # readCacheSize, writeCacheSize, privateNameCacheSize: 3 separate
    # FULL bytes at offsets 32/33/34, none used here, so skipped rather
    # than unpacked. A 4th byte (offset 35, also unused/unnamed here)
    # precedes the flags byte - P1sec/hermes-dec's own reader omits it
    # entirely (see module docstring: this is a confirmed bug in
    # hermes-dec's v98 large-header reader, independently determined by
    # brute-force testing every plausible struct size against apps/testy/98's
    # exception handler tables, NOT by trusting hermes-dec's source - it
    # empirically decodes 0 functions correctly at hermes-dec's own
    # 36-byte size vs. 109/109 at 37).
    flags = data[large_offset + 36]
    return FunctionHeaderEntry(
        index=index, is_overflowed=False, was_large_header=True,
        offset=offset, info_offset=large_offset, param_count=param_count,
        bytecode_size_in_bytes=bytecode_size,
        function_name=function_name, frame_size=frame_size,
        prohibit_invoke=ProhibitInvoke(flags & 0b11),
        strict_mode=bool((flags >> 2) & 1),
        has_exception_handler=bool((flags >> 3) & 1),
        has_debug_info=bool((flags >> 4) & 1),
        kind=FuncKind((flags >> 6) & 0b11),
    )


#: version -> (large_offset_fn, decode_large_fn). 99 intentionally absent
#: (see module docstring).
VERSION_TO_LARGE_HEADER_LAYOUT = {
    96: (_large_offset_v96, _decode_large_v96),
    98: (_large_offset_v98, _decode_large_v98),
}


def resolve_overflowed_headers(
        data: bytes, header: BytecodeFileHeader, entries: tuple[FunctionHeaderEntry, ...]
) -> tuple[FunctionHeaderEntry, ...]:
    """
    Given the `FunctionHeaderEntry` tuple `FunctionHeader.parse_function_headers()`
    produced, return a new tuple with every `is_overflowed=True` entry
    replaced by its fully-resolved large `FunctionHeader` (marked
    `was_large_header=True`). Entries that weren't overflowed pass
    through unchanged.

    Raises `HermesBytecodeError` if `header.version` has no confirmed
    large-header layout (see `VERSION_TO_LARGE_HEADER_LAYOUT` and the
    module docstring's bytecode-99 note) and at least one entry needs
    resolving.
    """
    if not any(e.is_overflowed for e in entries):
        return entries

    if header.version not in VERSION_TO_LARGE_HEADER_LAYOUT:
        raise HermesBytecodeError(
            f"no confirmed large FunctionHeader layout for bytecode version "
            f"{header.version} (known: {sorted(VERSION_TO_LARGE_HEADER_LAYOUT)}) - "
            f"can't resolve this bundle's overflowed function headers; "
            f"don't guess, confirm against a real bundle first (see module docstring)"
        )
    small_entry_size = _small_entry_size(header)
    large_offset_fn, decode_large_fn = VERSION_TO_LARGE_HEADER_LAYOUT[header.version]

    resolved = []
    for e in entries:
        if not e.is_overflowed:
            resolved.append(e)
            continue
        from hermes_disassembler.format.BytecodeFileHeader import HEADER_SIZE
        raw = data[HEADER_SIZE + e.index * small_entry_size: HEADER_SIZE + (e.index + 1) * small_entry_size]
        large_offset = large_offset_fn(raw)
        resolved.append(decode_large_fn(data, large_offset, e.index))

    return tuple(resolved)


def _small_entry_size(header: BytecodeFileHeader) -> int:
    from hermes_disassembler.format.StringTable import VERSION_TO_SMALL_FUNC_HEADER_SIZE
    return VERSION_TO_SMALL_FUNC_HEADER_SIZE[header.version]
