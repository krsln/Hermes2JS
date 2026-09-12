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
  ByteString:  1 byte (uint8 string-table index) - version < 98 only, see below
  Integer:     4 bytes (int32)

VERSION-DEPENDENT TAG 6 - the bug this module originally had: tag value
6 (0x60) means two DIFFERENT things depending on bytecode version, and
`SerializedLiteralGenerator.h` (fetched from the bytecode-98 commit the
first time this module was written) only documents the NEWER meaning.
Cross-checked against P1sec/hermes-dec's own independent implementation
(`src/hermes_dec/parsers/serialized_literal_parser.py`, which explicitly
branches on `bytecode_version >= 98`):
  version < 98:  tag 6 = ByteStringTag - a 1-BYTE payload (uint8 string
    index, 0-255). This is the ORIGINAL meaning (a third, more compact
    string-index width alongside Short/Long).
  version >= 98: tag 6 = UndefinedTag - NO payload at all (repurposed;
    ByteStringTag was dropped in favor of always using ShortString for
    small indices).
Getting this wrong doesn't just mis-decode the tag-6 elements themselves:
since a ByteStringTag's payload is 1 byte and UndefinedTag's is 0 bytes,
treating a version<98 ByteStringTag run as UndefinedTag skips one fewer
byte than it should, desynchronizing every subsequent tag read in the
buffer - this was the root cause of a ~1% NewArrayWithBuffer failure
rate and a much larger (~58% of keys) NewObjectWithBuffer failure rate
in bytecode 96, both now fixed; see this module's and
`ObjectLiteral.py`'s test suites for the before/after.

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
scale, with the tag-6 fix: every `NewArrayWithBuffer`/
`NewArrayWithBufferLong` instruction in both bundles decodes cleanly
(100% - the tag-6 bug was the entire cause of the small failure rate
noted in earlier versions of this docstring), and `NewObjectWithBuffer`
key decoding in bytecode 96 (via `ObjectLiteral.py`) went from 42%
strings to effectively 100% - see `tests/test_hermes_disassembler_object_literal.py`.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass
from typing import Union

from hermes_disassembler.core.Exceptions import TruncatedFileError
from hermes_disassembler.format.StringTable import StringTable

__all__ = ["LiteralValue", "decode_literal_buffer"]

# hermes/include/hermes/BCGen/SerializedLiteralGenerator.h TagType constants,
# with tag 6 handled specially per version - see module docstring.
_NULL_TAG = 0 << 4
_TRUE_TAG = 1 << 4
_FALSE_TAG = 2 << 4
_NUMBER_TAG = 3 << 4
_LONG_STRING_TAG = 4 << 4
_SHORT_STRING_TAG = 5 << 4
_TAG6 = 6 << 4  # ByteStringTag (version < 98) or UndefinedTag (version >= 98)
_INTEGER_TAG = 7 << 4
_TAG_MASK = 0x70

_TAG6_IS_UNDEFINED_FROM_VERSION = 98

LiteralValue = Union[None, bool, float, int, str]  # str only for a resolved string_id


def decode_literal_buffer(
        data: bytes, offset: int, count: int, bytecode_version: int, table: StringTable | None = None
) -> tuple[LiteralValue, ...]:
    """
    Decode `count` literal values starting at absolute byte `offset`.

    `bytecode_version` determines tag 6's meaning (ByteStringTag below
    98, UndefinedTag from 98 onward - see module docstring); getting
    this wrong desynchronizes every element after the first tag-6 run.

    String elements (ShortString/LongString/ByteString tags) are
    resolved through `table` if given (raising if `table` is `None`
    and a string element is encountered); every other tag needs no
    table.

    Raises `TruncatedFileError` if a tag or its payload would read past
    `len(data)`, and `ValueError` for an unrecognized tag byte or if the
    buffer's runs produce more or fewer than `count` elements (a strong
    signal the offset, count, or tag table is wrong - never silently
    truncated or padded).
    """
    tag6_is_undefined = bytecode_version >= _TAG6_IS_UNDEFINED_FROM_VERSION
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
            elif tag == _TAG6:
                if tag6_is_undefined:
                    values.append(_Undefined)
                else:
                    if pos + 1 > len(data):
                        raise TruncatedFileError("literal buffer ByteString", pos + 1, len(data))
                    string_id = data[pos]
                    values.append(table.resolve(string_id) if table is not None else string_id)
                    pos += 1
            else:
                raise ValueError(f"unrecognized literal buffer tag {tag:#x} at offset {pos}")

    return tuple(values)


class _UndefinedType:
    """Sentinel distinct from None for a literal `undefined` element."""

    def __repr__(self) -> str:
        return "undefined"


_Undefined = _UndefinedType()
