"""
Resolves a `SwitchImm`/`UIntSwitchImm` instruction's jump table - the
separate blob of `(max - min + 1)` relative jump targets its value
register is looked up against once range-checked (values outside
`[min, max]` instead take the instruction's own `Addr32` operand, its
"default case" - an ordinary single jump target, already handled
generically by `JumpTarget.resolve_operand_jump_target`, not by this
module).

Format and exact operand roles, confirmed from P1sec/hermes-dec's own
`hbc_bytecode_parser.py` (`fetched via vendor/fetch-hermes-dec.sh`, not
shipped in this repo) - `SwitchImm`/`UIntSwitchImm` share one operand
layout: `(value_reg: Reg8, table_offset: UInt32, default_target: Addr32,
min: UInt32, max: UInt32)`. `table_offset` is a relative offset from the
instruction's OWN start to the jump table blob (same relative-to-
instruction convention `JumpTarget.py` already uses for its single
targets); seek there, align up to 4 bytes, then read `max - min + 1`
raw `uint32` entries (UNSIGNED - not zigzag/signed-decoded, so a
switch's case bodies must all lie forward of the table itself, which
in practice they always do: a `switch` statement's compiled cases sit
sequentially after the dispatch code, see `resolve_switch_jump_table`'s
own confirmation below), each then added to the instruction's own
offset as this package's usual relative-target convention.

Directly confirmed - not just reasoned from source - by running real
hermes-dec (`hbc-disassembler`, installed from `vendor/hermes-dec` via
`pip install -e .`) against apps/testy/96's actual bundle: its first
`SwitchImm` (function-relative offset `0000000b`, operands `<Reg8: 1,
UInt32: 238, Addr32: 232, UInt32: 0, UInt32: 31>`) printed `# Address:
000000f3  # Jump table: [00000067, 00000031, ...]` - `000000f3` is
exactly `0xb + 232` (the default-case `Addr32` operand, confirmed by
`JumpTarget.py`'s general mechanism, not this module), and `00000067`
is exactly what this module's own formula produces for that same
instruction (verified in
`tests/test_hermes_disassembler_switch_table.py`, which reads that
real value directly from the fixture rather than hardcoding it as a
literal here).

`StringSwitchImm` (bytecode 98/99 only - a distinct opcode from
`UIntSwitchImm`, switching on interned string identity rather than an
integer range) is a DELIBERATE non-feature here, matching a confirmed
quirk of real hermes-dec's own output: its jump-table-comment code
path (`elif self.inst.name == 'SwitchImm':`) checks for the LITERAL
name `"SwitchImm"` only - never `"UIntSwitchImm"` (bytecode 98's own
name for the very same opcode this module handles) and never
`"StringSwitchImm"` - so real hermes-dec's own disassembly NEVER prints
a `# Jump table:` comment for either bytecode 98 opcode, confirmed by
running hermes-dec against apps/testy/98 directly (both
`UIntSwitchImm` and `StringSwitchImm` instances there get only their
`# Address:` comment, nothing else). `resolve_switch_table_entries`
below replicates this exactly: it raises for `StringSwitchImm` rather
than attempting a (currently unconfirmed) decode, and
`HasmWriter.py` only ever calls it for an instruction literally named
`SwitchImm` - so `UIntSwitchImm` is capable of being decoded here
(its binary layout is identical to `SwitchImm`'s) but, matching real
hermes-dec's own output byte-for-byte, never actually is.
"""
from __future__ import annotations

import struct

from hermes_disassembler.core.Exceptions import HermesBytecodeError, TruncatedFileError
from hermes_disassembler.format.Opcode import Instruction

__all__ = ["resolve_switch_table_entries"]

_ENTRY_SIZE = 4  # uint32 per jump table entry
_ALIGNMENT = 4


def _align_up(offset: int, alignment: int = _ALIGNMENT) -> int:
    remainder = offset % alignment
    return offset if remainder == 0 else offset + (alignment - remainder)


def resolve_switch_table_entries(
        data: bytes, instruction: Instruction, table_offset_operand: int,
        min_operand: int, max_operand: int,
) -> tuple[int, ...]:
    """
    Returns the absolute byte offset each of `instruction`'s jump table
    entries resolves to (same `instruction.offset + value` convention
    as `JumpTarget.resolve_operand_jump_target` - callers subtract
    their function's own `offset` to print it relative, as everywhere
    else in this package).

    `table_offset_operand`/`min_operand`/`max_operand` are OPERAND
    INDICES (not values) - `SwitchImm`/`UIntSwitchImm` use (1, 3, 4);
    see module docstring. Raises `HermesBytecodeError` for any other
    instruction name (in particular `StringSwitchImm` - see module
    docstring for why that's deliberate, not a missing case) and
    `TruncatedFileError` if the table would read past the end of `data`.
    """
    if instruction.name not in ("SwitchImm", "UIntSwitchImm"):
        raise HermesBytecodeError(
            f"{instruction.name} jump tables aren't decoded here - only "
            f"SwitchImm/UIntSwitchImm are (see module docstring for why "
            f"StringSwitchImm is deliberately excluded)"
        )

    table_offset = instruction.operands[table_offset_operand]
    min_value = instruction.operands[min_operand]
    max_value = instruction.operands[max_operand]

    start = _align_up(instruction.offset + table_offset)
    count = max_value - min_value + 1
    end = start + count * _ENTRY_SIZE
    if len(data) < end:
        raise TruncatedFileError(f"{instruction.name} jump table", end, len(data))

    return tuple(
        instruction.offset + raw
        for raw in struct.unpack_from(f"<{count}I", data, start)
    )
