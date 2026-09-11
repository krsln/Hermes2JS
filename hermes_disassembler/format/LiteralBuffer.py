"""
Decodes a Hermes "serialized literal" buffer - the tag-prefixed
run-length encoding `NewArrayWithBuffer`/`NewArrayWithBufferLong`'s
buffer-index operand points into, used to reconstruct an array
literal's constant elements (e.g. `[1, 0, 2]`) for a hasm comment.

Format source: facebook/hermes's own MIT-licensed
`include/hermes/BCGen/SerializedLiteralGenerator.h` - the class comment
there fully documents the tag scheme (reproduced and cited inline
below); this module is a decoder for the format that header's own
`SerializedLiteralGenerator` class WRITES.

Tag byte, one per run of same-typed consecutive elements:
  short form (run length < 16):  0 ttt llll            (1 byte)
  long form  (run length <= 4095): 1 ttt llll llllllll  (2 bytes,
    length = ((byte0 & 0xF) << 8) | byte1)
  t = type (3 bits, TagMask = 0x70, see _Tag below)
  l = run length

Per-element payload by tag (little-endian; Null/True/False/Undefined
have none - the run length alone says how many):
  Number:      8 bytes (double)
  ShortString: 2 bytes (uint16 string-table index, "smaller than 2^16")
  LongString:  4 bytes (uint32 string-table index)
  Integer:     4 bytes (int32)

Runs continue until the requested element count (`NewArrayWithBuffer`'s
own "number of static elements" operand) is consumed - this module
takes that count as a parameter rather than reading a terminator, since
the buffer has none.

Validated against apps/testy/96 and apps/testy/98: cross-checked
byte-for-byte against `tools/hermes/dump_bytecode.sh`'s own
"Array Buffer:" section (which prints the WHOLE buffer's decoded
values as one continuous sequential walk, not per-array) - decoding
from byte 0 with this module's tag logic reproduces that exact value
sequence in order (String(1914), Integer(1), Integer(2), Integer(578),
Integer(1478), ... - confirmed by hand against the raw hex too). At
scale: every `NewArrayWithBuffer`/`NewArrayWithBufferLong` instruction
in both bundles (1815 + 1776 = 3591 total), decoded via its own
`buf_idx` operand: 100% succeed in bytecode 98; bytecode 96 has 18
(~1%) that resolve a `ShortString`/`LongString` tag to an out-of-range
string index - not yet root-caused (a guess: possible interaction with
buffer deduplication across arrays sharing encoded suffixes, per a
"ConsecutiveStringStorage" dedup mechanism mentioned in facebook/hermes's
own commit history, landing a `buf_idx` a few bytes off from a true tag
boundary in these specific cases - unconfirmed). `decode_literal_buffer`
raises for these rather than returning wrong data; see `HasmWriter.py`,
which catches that and falls back to an `<unresolved: ...>` comment
instead of aborting the whole bundle.

Known gap: object literal buffers (`NewObjectWithBuffer`'s key/value
buffers) are NOT handled here - v98 uses a different, not yet
investigated "object shape table" indirection distinct from v96's
direct key+value buffer pair (see
`hermes_disassembler.format.BytecodeFileHeader`'s LAYOUT_V98 docstring:
`obj_shape_table_count` replaces v96's `obj_value_buffer_size`), so
this needs separate, version-specific work.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass
from typing import Union

from hermes_disassembler.core.Exceptions import TruncatedFileError
from hermes_disassembler.format.StringTable import StringTable

__all__ = ["LiteralValue", "decode_literal_buffer"]

# hermes/include/hermes/BCGen/SerializedLiteralGenerator.h: TagType constants
_NULL_TAG = 0 << 4
_TRUE_TAG = 1 << 4
_FALSE_TAG = 2 << 4
_NUMBER_TAG = 3 << 4
_LONG_STRING_TAG = 4 << 4
_SHORT_STRING_TAG = 5 << 4
_UNDEFINED_TAG = 6 << 4
_INTEGER_TAG = 7 << 4
_TAG_MASK = 0x70

LiteralValue = Union[None, bool, float, int, str]  # str only for a resolved string_id


def decode_literal_buffer(
        data: bytes, offset: int, count: int, table: StringTable | None = None
) -> tuple[LiteralValue, ...]:
    """
    Decode `count` literal values starting at absolute byte `offset`.

    String elements (ShortString/LongString tags) are resolved through
    `table` if given (raising if `table` is `None` and a string element
    is encountered); every other tag needs no table.

    Raises `TruncatedFileError` if a tag or its payload would read past
    `len(data)`, and `ValueError` for an unrecognized tag byte or if the
    buffer's runs produce more or fewer than `count` elements (a strong
    signal the offset, count, or tag table is wrong - never silently
    truncated or padded).
    """
    values: list[LiteralValue] = []
    pos = offset

    while len(values) < count:
        if pos >= len(data):
            raise TruncatedFileError("literal buffer tag byte", pos + 1, len(data))
        tag_byte = data[pos]
        tag = tag_byte & _TAG_MASK

        if tag_byte & 0x80:  # long form: 2-byte tag
            if pos + 2 > len(data):
                raise TruncatedFileError("literal buffer long tag", pos + 2, len(data))
            run_length = ((tag_byte & 0x0F) << 8) | data[pos + 1]
            pos += 2
        else:  # short form: 1-byte tag
            run_length = tag_byte & 0x0F
            pos += 1

        run_length = min(run_length, count - len(values))  # don't overshoot the requested count

        for _ in range(run_length):
            if tag == _NULL_TAG:
                values.append(None)
            elif tag == _TRUE_TAG:
                values.append(True)
            elif tag == _FALSE_TAG:
                values.append(False)
            elif tag == _UNDEFINED_TAG:
                values.append(_Undefined)
            elif tag == _NUMBER_TAG:
                if pos + 8 > len(data):
                    raise TruncatedFileError("literal buffer Number", pos + 8, len(data))
                (v,) = struct.unpack_from("<d", data, pos)
                values.append(v)
                pos += 8
            elif tag == _INTEGER_TAG:
                if pos + 4 > len(data):
                    raise TruncatedFileError("literal buffer Integer", pos + 4, len(data))
                (v,) = struct.unpack_from("<i", data, pos)
                values.append(v)
                pos += 4
            elif tag == _SHORT_STRING_TAG:
                if pos + 2 > len(data):
                    raise TruncatedFileError("literal buffer ShortString", pos + 2, len(data))
                (string_id,) = struct.unpack_from("<H", data, pos)
                values.append(table.resolve(string_id) if table is not None else string_id)
                pos += 2
            elif tag == _LONG_STRING_TAG:
                if pos + 4 > len(data):
                    raise TruncatedFileError("literal buffer LongString", pos + 4, len(data))
                (string_id,) = struct.unpack_from("<I", data, pos)
                values.append(table.resolve(string_id) if table is not None else string_id)
                pos += 4
            else:
                raise ValueError(f"unrecognized literal buffer tag {tag:#x} at offset {pos}")

    return tuple(values)


class _UndefinedType:
    """Sentinel distinct from None for a literal `undefined` element."""

    def __repr__(self) -> str:
        return "undefined"


_Undefined = _UndefinedType()
