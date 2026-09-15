"""
Resolves a `bigint_id` operand (`LoadConstBigInt`/`LoadConstBigIntLongIndex`
- see `Opcode.py`'s opcode tables, `operand_meaning`) to its actual
arbitrary-precision integer value.

Table format, confirmed from P1sec/hermes-dec's own `hbc_file_parser.py`
(`HBCReader.read_bigints`/`get_offset_length_pair_reader`, fetched via
`vendor/fetch-hermes-dec.sh`, not shipped in this repo): `header.bigint_count`
`BigIntTableEntry` structs (`offset: uint32, length: uint32`, 8 bytes each,
facebook/hermes's `include/hermes/Support/BigIntSupport.h`), followed by
`header.bigint_storage_size` bytes of raw little-endian value storage -
each entry's value is `int.from_bytes(storage[offset:offset+length], 'little')`
(unsigned - this package, like hermes-dec's own disassembler, doesn't
attempt to recover the original source's sign or literal suffix, just
the raw stored magnitude - see `resolve_bigint`).

Location: `table.bigint_table_offset` (see `StringTable.py`, which
computes it as part of the same section-offset chain array/object
buffer parsing already needs - Hermes's bytecode format gives no
standalone absolute offset field for this section, only a count and a
storage size, so its start has to be derived from what precedes it,
the same way every `read_*` step in hermes-dec's own sequential reader
does). Confirmed correct independently of trusting hermes-dec's
byte-level struct definitions (which, per `FunctionHeaderOverflow.py`'s
own history, aren't always right): by actually RUNNING hermes-dec's
`HBCReader` against both apps/testy/96 and apps/testy/98 up through
`read_arrays()` and checking its own file stream's position at that
point - 943398 for bytecode 96 (943400 once aligned to 4 bytes, which
`read_bigints()` does as its own first step - matching
`table.bigint_table_offset` exactly) and 912180 for bytecode 98
(already aligned, no adjustment needed - also matching exactly).

Both apps/testy/96 and apps/testy/98 have `bigint_count=0` - neither
has a single real BigInt literal to decode, so `resolve_bigint` below
is validated only by the table-location cross-check above and a
synthetic test, not a real end-to-end example - see
`tests/test_hermes_disassembler_bigint_table.py`.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass

from hermes_disassembler.core.Exceptions import HermesBytecodeError, TruncatedFileError
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.StringTable import StringTable

__all__ = ["resolve_bigint"]

_ENTRY_SIZE = 8  # BigIntTableEntry: uint32 offset, uint32 length


@dataclass(frozen=True, slots=True)
class _BigIntTableEntry:
    offset: int
    length: int


def _read_entry(data: bytes, table_start: int, index: int) -> _BigIntTableEntry:
    entry_offset = table_start + index * _ENTRY_SIZE
    if len(data) < entry_offset + _ENTRY_SIZE:
        raise TruncatedFileError("BigIntTableEntry", entry_offset + _ENTRY_SIZE, len(data))
    offset, length = struct.unpack_from("<II", data, entry_offset)
    return _BigIntTableEntry(offset=offset, length=length)


def resolve_bigint(data: bytes, table: StringTable, header: BytecodeFileHeader, index: int) -> int:
    """
    Returns the arbitrary-precision integer value of BigInt table entry
    `index` (a `bigint_id` operand's value).

    Raises `IndexError` if `index` is out of range (matching
    `Builtins.resolve_builtin`'s convention for the same kind of
    operand-value-out-of-range mistake) and `TruncatedFileError` if the
    entry or the storage bytes it points to would read past the end of
    `data`.
    """
    if not (0 <= index < header.bigint_count):
        raise IndexError(f"bigint index {index} out of range (table has {header.bigint_count} entries)")

    table_start = table.bigint_table_offset
    entry = _read_entry(data, table_start, index)

    storage_start = table_start + header.bigint_count * _ENTRY_SIZE
    value_start = storage_start + entry.offset
    value_end = value_start + entry.length
    if len(data) < value_end:
        raise TruncatedFileError("BigInt value bytes", value_end, len(data))

    return int.from_bytes(data[value_start:value_end], "little")
