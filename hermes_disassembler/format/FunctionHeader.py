"""
Decodes the `SmallFuncHeader` array - the "function headers" segment that
comes right after the 128-byte file header (see `StringTable.py`'s
module docstring for the full segment order).

Layout source: facebook/hermes's own MIT-licensed
`include/hermes/BCGen/HBC/BytecodeFileFormat.h`, same two commits as
`BytecodeFileHeader.py`/`StringTable.py`. `SmallFuncHeader`'s *size*
differs by version (16 vs 12 bytes - see `StringTable.VERSION_TO_SMALL_FUNC_HEADER_SIZE`);
its *field layout* differs too, more substantially than the header
struct did:

  LAYOUT_V96: native C bitfields (`store_type name : bits;`), three
  uint32_t "words" + three separate uint8_t bytes + a 1-byte
  `FunctionHeaderFlag` with NO `Kind` field (no generator/async
  distinction - that concept didn't exist in the format yet):
  https://github.com/facebook/hermes/blob/v0.12.0/include/hermes/BCGen/HBC/BytecodeFileFormat.h
  Fields: offset(25) paramCount(7) | bytecodeSizeInBytes(15) functionName(17)
  | infoOffset(25) frameSize(7) | environmentSize(8) highestReadCacheIndex(8)
  highestWriteCacheIndex(8) | flags(8, no Kind bits).

  LAYOUT_V98: `BitField<>` template, two uint32_t words + three uint8_t
  bytes + a 1-byte `FunctionHeaderFlag` that DOES have a 2-bit `Kind`
  field (Normal/Generator/Async - added later, see FunctionInfo.h):
  https://github.com/facebook/hermes/blob/cb5bb3342f43d378cc2653e2ac9077a282b97637/include/hermes/BCGen/HBC/BytecodeFileFormat.h
  Fields: Offset(25) ParamCount(5) LoopDepth(2) | BytecodeSizeInBytes(14)
  FunctionName(8) NumberRegCount(5) NonPtrRegCount(5) | FrameSize(8)
  ReadCacheSize(8) WriteCacheSize(6) NumCacheNewObject(1)
  PrivateNameCacheSize(1) | flags(8, with Kind).

Both confirmed LSB-first bit packing (bit 0 = first-declared field), the
same convention already empirically validated for `BytecodeOptions` in
BytecodeFileHeader.py and `SmallStringTableEntry` in StringTable.py.

`ProhibitInvoke`/`FuncKind` enum values: facebook/hermes's
`include/hermes/BCGen/FunctionInfo.h` (Call=0/Construct=1/None=2 and
Normal=0/Generator=1/Async=2 respectively - LAYOUT_V96 predates this
file and its `ProhibitInvoke` enum has the same values under different
names: ProhibitCall=0/ProhibitConstruct=1/ProhibitNone=2, no Kind at all).

Known gap - overflowed headers: a `SmallFuncHeader` whose fields don't
fit its bit widths sets `flags.overflowed` and repurposes `offset` +
`function_name` (v96) or `offset` + a second field (v98) to encode a
byte offset to a full-size `FunctionHeader` elsewhere in the file
(`getLargeHeaderOffset()`). This module detects and flags overflowed
entries (`is_overflowed=True`, all other fields `None`) but does not
yet resolve them. The overflow rate differs sharply by version and
this is confirmed, not a decoding bug: LAYOUT_V96's `FunctionName` is
17 bits (fits any string index up to 131071) so overflow is rare there
(3 of 15247 functions in apps/testy/96 - a giant bundle-init function
among them); LAYOUT_V98's `FunctionName` is only 8 bits (max 255), so
in apps/testy/98 the *majority* of functions overflow (11155 of
14267) purely because their name's string-table index exceeds 255 -
nothing to do with bytecode size. The non-overflowed ~22% were enough
to validate this module (see below), but resolving `FunctionHeader`
(the full-size struct overflow points to) is needed before most v98
functions' metadata - offset, bytecode size, everything - is reachable
at all; see `hermes_disassembler`'s package docstring for what's next.

Validated against apps/testy/96 and apps/testy/98: for each bundle,
decoding every non-overflowed function header and resolving
`function_name` through `StringTable` reproduces the exact
(name, param_count) pairs `tools/hermes/dump_bytecode.sh` shows -
clear/1, define/4, metroRequire/3, metroImportDefault/3 for 96 (all
four found); get/1 with 1-byte-ish bytecode sizes for 98 (96's targets
mostly fall in 98's overflowed 78%, consistent with the FunctionName
explanation above, so this test uses a different, non-overflowed
signature for 98) - see
`tests/test_hermes_disassembler_function_header.py`.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass
from enum import IntEnum
from typing import Optional

from hermes_disassembler.core.Exceptions import HermesBytecodeError, TruncatedFileError
from hermes_disassembler.format.BytecodeFileHeader import HEADER_SIZE, BytecodeFileHeader
from hermes_disassembler.format.StringTable import VERSION_TO_SMALL_FUNC_HEADER_SIZE

__all__ = [
    "FunctionHeaderEntry", "ProhibitInvoke", "FuncKind",
    "parse_function_headers",
]


class ProhibitInvoke(IntEnum):
    """hermes/include/hermes/BCGen/FunctionInfo.h (LAYOUT_V96 used the same values under ProhibitCall/ProhibitConstruct/ProhibitNone)."""

    CALL = 0
    CONSTRUCT = 1
    NONE = 2


class FuncKind(IntEnum):
    """hermes/include/hermes/BCGen/FunctionInfo.h. Not representable under LAYOUT_V96 (no Kind bits) - always NORMAL there."""

    NORMAL = 0
    GENERATOR = 1
    ASYNC = 2


@dataclass(frozen=True, slots=True)
class FunctionHeaderEntry:
    """
    One decoded `SmallFuncHeader`. If `is_overflowed` is True, every
    other field is `None` - see module docstring's "Known gap" section.
    """

    index: int
    is_overflowed: bool
    offset: Optional[int] = None  # byte offset of this function's bytecode
    bytecode_size_in_bytes: Optional[int] = None
    param_count: Optional[int] = None
    frame_size: Optional[int] = None
    function_name: Optional[int] = None  # string table index; resolve via StringTable
    prohibit_invoke: Optional[ProhibitInvoke] = None
    strict_mode: Optional[bool] = None
    has_exception_handler: Optional[bool] = None
    has_debug_info: Optional[bool] = None
    kind: Optional[FuncKind] = None  # always NORMAL under LAYOUT_V96 (no Kind bits there)


def parse_function_headers(
        data: bytes, header: BytecodeFileHeader
) -> tuple[FunctionHeaderEntry, ...]:
    """
    Decode the `function_count`-entry `SmallFuncHeader` array right
    after the 128-byte file header, dispatching to the right bit layout
    for `header.version` (see module docstring).
    """
    if header.version not in _VERSION_TO_DECODER:
        raise HermesBytecodeError(
            f"no confirmed SmallFuncHeader field layout for bytecode version "
            f"{header.version} (known: {sorted(_VERSION_TO_DECODER)}) - don't "
            f"guess, confirm against a real bundle first (see module docstring)"
        )
    decode_one = _VERSION_TO_DECODER[header.version]
    entry_size = VERSION_TO_SMALL_FUNC_HEADER_SIZE[header.version]

    end = HEADER_SIZE + header.function_count * entry_size
    if len(data) < end:
        raise TruncatedFileError("function headers table", end, len(data))

    return tuple(
        decode_one(i, data[HEADER_SIZE + i * entry_size: HEADER_SIZE + (i + 1) * entry_size])
        for i in range(header.function_count)
    )


def _decode_v96(index: int, raw: bytes) -> FunctionHeaderEntry:
    w1, w2, w3 = struct.unpack_from("<III", raw, 0)
    flags = raw[15]

    if (flags >> 5) & 1:  # overflowed
        return FunctionHeaderEntry(index=index, is_overflowed=True)

    return FunctionHeaderEntry(
        index=index,
        is_overflowed=False,
        offset=w1 & 0x1FF_FFFF,  # 25 bits
        param_count=(w1 >> 25) & 0x7F,  # 7 bits
        bytecode_size_in_bytes=w2 & 0x7FFF,  # 15 bits
        function_name=(w2 >> 15) & 0x1_FFFF,  # 17 bits
        frame_size=(w3 >> 25) & 0x7F,  # 7 bits (infoOffset, bits 0-24, unused here)
        prohibit_invoke=ProhibitInvoke(flags & 0b11),
        strict_mode=bool((flags >> 2) & 1),
        has_exception_handler=bool((flags >> 3) & 1),
        has_debug_info=bool((flags >> 4) & 1),
        kind=FuncKind.NORMAL,  # LAYOUT_V96 has no Kind bits
    )


def _decode_v98(index: int, raw: bytes) -> FunctionHeaderEntry:
    w1, w2 = struct.unpack_from("<II", raw, 0)
    b1, b2, b3 = raw[8], raw[9], raw[10]
    flags = raw[11]

    if (flags >> 5) & 1:  # overflowed
        return FunctionHeaderEntry(index=index, is_overflowed=True)

    return FunctionHeaderEntry(
        index=index,
        is_overflowed=False,
        offset=w1 & 0x1FF_FFFF,  # 25 bits
        param_count=(w1 >> 25) & 0x1F,  # 5 bits (+ LoopDepth:2 above, unused here)
        bytecode_size_in_bytes=w2 & 0x3FFF,  # 14 bits
        function_name=(w2 >> 14) & 0xFF,  # 8 bits
        frame_size=b1,  # full byte
        prohibit_invoke=ProhibitInvoke(flags & 0b11),
        strict_mode=bool((flags >> 2) & 1),
        has_exception_handler=bool((flags >> 3) & 1),
        has_debug_info=bool((flags >> 4) & 1),
        kind=FuncKind((flags >> 6) & 0b11),
    )


_VERSION_TO_DECODER = {96: _decode_v96, 98: _decode_v98, 99: _decode_v98}
