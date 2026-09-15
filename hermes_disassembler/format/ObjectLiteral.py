"""
Decodes a `NewObjectWithBuffer`/`NewObjectWithBufferLong` instruction's
object literal content (keys and values) for a hasm comment.

Layout source: facebook/hermes's own MIT-licensed
`include/hermes/BCGen/ShapeTableEntry.h` (LAYOUT_V98's object-key
indirection - see below) plus the same `SerializedLiteralGenerator`
tag format `LiteralBuffer.py` decodes (for both keys and values, in
both layouts).

Object literal representation genuinely differs between the two
confirmed bytecode versions - not just a renamed field, unlike most of
the rest of this package:

  LAYOUT_V96: `NewObjectWithBuffer(Reg8, UInt16 hint, UInt16 count,
  UInt16 keyBufIdx, UInt16 valBufIdx)` - `keyBufIdx` addresses `count`
  keys DIRECTLY in the object key buffer
  (`StringTable.object_key_buffer_offset`), `valBufIdx` addresses
  `count` values directly in the object value buffer
  (`StringTable.object_value_or_shape_table_offset`, which for this
  layout IS the value buffer, not a shape table - see
  `BytecodeFileHeader`'s LAYOUT_V96: `obj_value_buffer_size`).

  LAYOUT_V98 (and 99): `NewObjectWithBuffer(Reg8, UInt16 shapeTableIdx,
  UInt16 valBufIdx)`. `shapeTableIdx` indexes a
  `ShapeTableEntry { uint32_t keyBufferOffset; uint32_t numProps; }`
  (8 bytes, packed) in the object shape table
  (`StringTable.object_value_or_shape_table_offset`, sized by
  `header.obj_shape_table_count * 8`) - `keyBufferOffset` then
  addresses `numProps` keys in the object key buffer, and `valBufIdx`
  addresses `numProps` values in the SAME literal value buffer arrays
  use (`StringTable.literal_value_buffer_offset` - v98's header has no
  separate object-value-buffer-size field, only
  `literal_value_buffer_size`, shared between arrays and objects).
  Confirmed byte-for-byte against apps/testy/98: shape index 25 decodes
  to `keyBufferOffset=254, numProps=1`, matching
  `tools/hermes/dump_bytecode.sh`'s own "Object Shape Table:" line
  `25[254, 1]` exactly.

History: this module originally rejected bytecode 96 outright. Its
direct `keyBufIdx` decode initially produced garbage for the majority
of objects (only 42% of decoded "keys" came out as strings; the rest
were `undefined`/bool/null, which are never legitimate object literal
keys) - traced to `LiteralBuffer.py`'s tag-6 bug (ByteStringTag,
version < 98, was being decoded as the wrong, version>=98-only
UndefinedTag meaning, silently eating one fewer payload byte than it
should and desynchronizing every subsequent element). Once that was
fixed, bytecode 96 decodes to 99.8% string keys (7680 of 7696 across
every `NewObjectWithBuffer` in apps/testy/96) with zero errors - see
`tests/test_hermes_disassembler_object_literal.py`. Both layouts are
now supported here.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass

from hermes_disassembler.core.Exceptions import HermesBytecodeError, TruncatedFileError
from hermes_disassembler.format.LiteralBuffer import LiteralValue, decode_literal_buffer
from hermes_disassembler.format.StringTable import StringTable

__all__ = ["ObjectLiteral", "resolve_object_literal"]

_SHAPE_TABLE_ENTRY_SIZE = 8  # ShapeTableEntry: uint32_t keyBufferOffset, numProps

#: versions using the direct keyBufIdx/valBufIdx layout (arg2=count,
#: arg3=keyBufIdx, arg4=valBufIdx) vs. the shape-table layout
#: (arg2=shapeTableIdx, arg3=valBufIdx). See module docstring.
#: 99 is deliberately excluded from the shape-table set even though it
#: shares LAYOUT_V98's header/SmallFuncHeader - there is no
#: apps/testy/99 bundle to confirm ShapeTableEntry decoding against,
#: matching this package's don't-guess-an-unvalidated-version discipline
#: (see e.g. FunctionHeaderOverflow.VERSION_TO_LARGE_HEADER_LAYOUT).
_DIRECT_KEY_BUFFER_VERSIONS = {96}
_SHAPE_TABLE_VERSIONS = {98}


@dataclass(frozen=True, slots=True)
class ObjectLiteral:
    keys: tuple[LiteralValue, ...]
    values: tuple[LiteralValue, ...]


def resolve_object_literal(
        data: bytes, table: StringTable, version: int,
        count_or_shape_idx: int, key_or_val_idx: int, val_idx: int | None = None,
) -> ObjectLiteral:
    """
    Resolve a `NewObjectWithBuffer`/`NewObjectWithBufferLong`
    instruction's literal content.

    For LAYOUT_V98/99 (shape table): call with
    `(data, table, version, shapeTableIdx, valBufIdx)` - `val_idx`
    left as `None`.

    For LAYOUT_V96 (direct buffers): call with
    `(data, table, version, count, keyBufIdx, valBufIdx)` - all three
    positional args after `version` are required.

    Raises `HermesBytecodeError` for any version with no confirmed
    layout (see `_DIRECT_KEY_BUFFER_VERSIONS`/`_SHAPE_TABLE_VERSIONS`
    above - don't guess a third version's layout without confirming
    against a real bundle first, per this package's general discipline),
    and `TruncatedFileError` if a shape table entry or buffer read
    would exceed `len(data)`.
    """
    if version in _SHAPE_TABLE_VERSIONS:
        shape_idx, buf_val_idx = count_or_shape_idx, key_or_val_idx
        entry_offset = table.object_value_or_shape_table_offset + shape_idx * _SHAPE_TABLE_ENTRY_SIZE
        entry_end = entry_offset + _SHAPE_TABLE_ENTRY_SIZE
        if len(data) < entry_end:
            raise TruncatedFileError("ShapeTableEntry", entry_end, len(data))
        key_buffer_offset, num_props = struct.unpack_from("<II", data, entry_offset)

        keys = decode_literal_buffer(data, table.object_key_buffer_offset + key_buffer_offset, num_props, version,
                                     table)
        values = decode_literal_buffer(data, table.literal_value_buffer_offset + buf_val_idx, num_props, version, table)
        return ObjectLiteral(keys=keys, values=values)

    if version in _DIRECT_KEY_BUFFER_VERSIONS:
        if val_idx is None:
            raise TypeError("LAYOUT_V96 requires (count, keyBufIdx, valBufIdx) - val_idx must not be None")
        count, key_idx = count_or_shape_idx, key_or_val_idx
        keys = decode_literal_buffer(data, table.object_key_buffer_offset + key_idx, count, version, table)
        values = decode_literal_buffer(data, table.object_value_or_shape_table_offset + val_idx, count, version, table)
        return ObjectLiteral(keys=keys, values=values)

    raise HermesBytecodeError(
        f"object literal decoding is not supported for bytecode {version} - "
        f"see hermes_disassembler.format.ObjectLiteral's module docstring"
    )
