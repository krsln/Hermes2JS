"""
Decodes a `NewObjectWithBuffer`/`NewObjectWithBufferLong` instruction's
object literal content (keys and values) for a hasm comment.

Layout source: facebook/hermes's own MIT-licensed
`include/hermes/BCGen/ShapeTableEntry.h` (LAYOUT_V98's object-key
indirection - see below) plus the same `SerializedLiteralGenerator`
tag format `LiteralBuffer.py` already decodes (for both keys and
values).

Object literal representation is genuinely different between the two
confirmed bytecode versions - not just a renamed field, unlike most of
the rest of this package:

  LAYOUT_V98 (bytecode 98/99): `NewObjectWithBuffer(Reg8, UInt16
  shapeTableIdx, UInt16 valBufIdx)`. `shapeTableIdx` indexes a
  `ShapeTableEntry { uint32_t keyBufferOffset; uint32_t numProps; }`
  (8 bytes, packed) in the "object shape table" segment
  (`StringTable.object_value_or_shape_table_offset`, sized by
  `header.obj_shape_table_count * 8`) - `keyBufferOffset` then
  addresses `numProps` keys in the object key buffer
  (`StringTable.object_key_buffer_offset`), and `valBufIdx` addresses
  `numProps` values in the SAME literal value buffer arrays use
  (`StringTable.literal_value_buffer_offset` - confirmed: v98's header
  has no separate object-value-buffer-size field, only
  `literal_value_buffer_size`, shared between arrays and objects).
  Confirmed byte-for-byte against apps/testy/98: shape index 25 decodes
  to `keyBufferOffset=254, numProps=1`, matching
  `tools/hermes/dump_bytecode.sh`'s own "Object Shape Table:" line
  `25[254, 1]` exactly; the resulting key/value pair
  (`'value'`/`True`) is a plausible object literal, and at scale across
  every `NewObjectWithBuffer` in the bundle (12247 total), 99.3% of
  decoded keys are strings (30660 of 30884, the rest small integers) -
  essentially clean.

  LAYOUT_V96 (bytecode 96): `NewObjectWithBuffer(Reg8, UInt16 hint,
  UInt16 count, UInt16 keyBufIdx, UInt16 valBufIdx)` - `keyBufIdx`
  addresses the object key buffer DIRECTLY (no shape-table
  indirection), the same way `NewArrayWithBuffer`'s `buf_idx` works.
  This module does NOT support this path yet: decoding `count` keys
  from `keyBufIdx` this way produces plausible results for some
  instructions (e.g. `{trace: 0, info: 1, ...}`) but garbage - tags
  decoding as `undefined`/`bool`/`null` where a property key can never
  legitimately be one - for the majority of them: across every
  bytecode-96 `NewObjectWithBuffer` (863 total), only 42% of decoded
  "keys" come out as strings. v98's shape-table approach, decoding the
  SAME kind of tagged buffer, is 99.3% clean, so the tag-decoding logic
  itself (`LiteralBuffer.decode_literal_buffer`) is not in question -
  something about how v96 computes or shares `keyBufIdx` across
  objects isn't understood yet (a guess: heavier key-sequence
  deduplication landing `keyBufIdx` mid-run for many objects, unlike
  v98's explicit per-shape `keyBufferOffset` - unconfirmed). Rather
  than emit wrong data most of the time, `resolve_object_literal`
  raises `HermesBytecodeError` unconditionally for bytecode 96.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass

from hermes_disassembler.core.Exceptions import HermesBytecodeError, TruncatedFileError
from hermes_disassembler.format.LiteralBuffer import LiteralValue, decode_literal_buffer
from hermes_disassembler.format.StringTable import StringTable

__all__ = ["ObjectLiteral", "resolve_object_literal"]

_SHAPE_TABLE_ENTRY_SIZE = 8  # ShapeTableEntry: uint32_t keyBufferOffset, numProps


@dataclass(frozen=True, slots=True)
class ObjectLiteral:
    keys: tuple[LiteralValue, ...]
    values: tuple[LiteralValue, ...]


def resolve_object_literal(
        data: bytes, table: StringTable, version: int, shape_or_key_idx: int, val_idx: int
) -> ObjectLiteral:
    """
    Resolve a `NewObjectWithBuffer`/`NewObjectWithBufferLong`
    instruction's literal content. `shape_or_key_idx` is its shape-table
    operand (v98) - v96 is not supported yet, see module docstring.

    Raises `HermesBytecodeError` for bytecode 96 (unconditionally - not
    yet understood well enough to trust, see module docstring) and any
    version with no confirmed shape-table layout, and `TruncatedFileError`
    if the shape table entry or buffer reads would exceed `len(data)`.
    """
    if version != 98 and version != 99:
        raise HermesBytecodeError(
            f"object literal decoding is not supported for bytecode {version} - "
            f"see hermes_disassembler.format.ObjectLiteral's module docstring"
        )

    entry_offset = table.object_value_or_shape_table_offset + shape_or_key_idx * _SHAPE_TABLE_ENTRY_SIZE
    entry_end = entry_offset + _SHAPE_TABLE_ENTRY_SIZE
    if len(data) < entry_end:
        raise TruncatedFileError("ShapeTableEntry", entry_end, len(data))
    key_buffer_offset, num_props = struct.unpack_from("<II", data, entry_offset)

    keys = decode_literal_buffer(data, table.object_key_buffer_offset + key_buffer_offset, num_props, table)
    values = decode_literal_buffer(data, table.literal_value_buffer_offset + val_idx, num_props, table)

    return ObjectLiteral(keys=keys, values=values)
