"""
Resolves an overflowed `SmallFuncHeader` (see `FunctionHeader.py`'s
"Known gap" section) to the full-size `FunctionHeader` struct its
`getLargeHeaderOffset()` points to.

`getLargeHeaderOffset()`'s encoding and the large struct's own field
layout, both confirmed from facebook/hermes's MIT-licensed
`include/hermes/BCGen/HBC/BytecodeFileFormat.h` at the same two commits
used throughout this package:

  LAYOUT_V96 (v0.12.0): `getLargeHeaderOffset() = (infoOffset << 16) |
  offset` (both taken from the *small* header's own 25-bit fields, which
  is why they're all that's meaningful once overflowed - see
  `SmallFuncHeader::setLargeHeaderOffset`). The struct at that offset:
  9 full-width uint32_t fields (offset, paramCount, bytecodeSizeInBytes,
  functionName, infoOffset, frameSize, environmentSize,
  highestReadCacheIndex, highestWriteCacheIndex) + 1-byte
  `FunctionHeaderFlag` = 37 bytes, confirmed an ABSOLUTE file offset by
  decoding it for a real overflowed function (index 0, "global", in
  apps/testy/96) and getting back paramCount=1 (already known) and a
  functionName that resolves through StringTable to literally "global".
  https://github.com/facebook/hermes/blob/v0.12.0/include/hermes/BCGen/HBC/BytecodeFileFormat.h

  LAYOUT_V98 (cb5bb334...): `getLargeHeaderOffset() = (functionName <<
  24) | (offset & 0xffffff)` - a different encoding than v96's (uses
  FunctionName's 8 bits as the high byte, not a dedicated infoOffset
  field - v98's SmallFuncHeader has no infoOffset at all, see
  `FunctionHeader.py`). The struct at that offset: 8 full-width
  uint32_t fields (Offset, ParamCount, LoopDepth, BytecodeSizeInBytes,
  FunctionName, NumberRegCount, NonPtrRegCount, FrameSize) + 4
  full-width uint8_t fields (ReadCacheSize, WriteCacheSize,
  NumCacheNewObject, PrivateNameCacheSize) + 1-byte
  `FunctionHeaderFlag` = 37 bytes.
  https://github.com/facebook/hermes/blob/cb5bb3342f43d378cc2653e2ac9077a282b97637/include/hermes/BCGen/HBC/BytecodeFileFormat.h

  bytecode 99: intentionally UNSUPPORTED here (see
  `VERSION_TO_LARGE_HEADER_LAYOUT` below), even though it shares
  LAYOUT_V98's *compact* SmallFuncHeader size (confirmed in
  StringTable.py). Its FUNC_HEADER_FIELDS macro drops the
  NumCacheNewObject sub-field entirely (WriteCacheSize grows from 6 to
  7 bits to absorb the freed bit - see diff noted in
  BytecodeFileHeader.py's history). Because DECLARE_FIELD gives each
  named sub-field its own full-width member in the *large* struct
  (unlike the compact one, where bit-packing absorbs such changes for
  free), removing NumCacheNewObject shrinks the large FunctionHeader by
  a whole byte (36, not 37) for 99 - and there's no apps/testy/99
  bundle fixture to confirm that against, so guessing here would repeat
  the exact mistake BytecodeFileHeader.py's module docstring describes.

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

__all__ = ["resolve_overflowed_headers", "VERSION_TO_LARGE_HEADER_LAYOUT", "LARGE_HEADER_SIZE"]

# Small-header limits each version's large-header path exists to work
# around - the field width in SmallFuncHeader that most commonly
# overflows in practice. Exposed for tests/diagnostics, not load-bearing.
_SMALL_BYTECODE_SIZE_LIMIT = {96: (1 << 15) - 1, 98: (1 << 14) - 1, 99: (1 << 14) - 1}

#: Size in bytes of the "large" FunctionHeader struct (both v96 and v98/99
#: layouts happen to be 37 bytes, though their field composition differs -
#: see the per-layout _decode_large_* functions). Exported for
#: ExceptionHandlerTable.py, which reads the exception handler table
#: immediately after this struct for an overflowed function.
LARGE_HEADER_SIZE = 37


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
    size = LARGE_HEADER_SIZE
    if large_offset + size > len(data):
        raise TruncatedFileError(f"large FunctionHeader for function {index}", large_offset + size, len(data))
    (offset, param_count, bytecode_size, function_name, _info_offset, frame_size,
     _env_size, _hi_rd, _hi_wr) = struct.unpack_from("<9I", data, large_offset)
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
        kind=FuncKind.NORMAL,  # LAYOUT_V96 FunctionHeaderFlag has no Kind bits
    )


def _decode_large_v98(data: bytes, large_offset: int, index: int) -> FunctionHeaderEntry:
    size = LARGE_HEADER_SIZE
    if large_offset + size > len(data):
        raise TruncatedFileError(f"large FunctionHeader for function {index}", large_offset + size, len(data))
    (offset, param_count, _loop_depth, bytecode_size, function_name,
     _number_reg, _non_ptr_reg, frame_size) = struct.unpack_from("<8I", data, large_offset)
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
