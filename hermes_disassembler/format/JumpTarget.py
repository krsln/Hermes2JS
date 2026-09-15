"""
Resolves a jump instruction's absolute byte-offset target.

Every jump-family opcode (`Jmp`, `JmpTrue`, `JmpFalseLong`, `JLess`, the
`SaveGenerator` family, etc. - anything DEFINE_JUMP_1/2/3 in
BytecodeList.def expanded, see `tools/hermes/generate_opcode_tables.py`)
takes an `Addr8` or `Addr32` as its FIRST operand: a signed byte offset
relative to the jump instruction's OWN start address (not the end of
the instruction, not the start of its operand) - confirmed against a
real bundle, not assumed: apps/testy/96 function index 7
(`guardedLoadModule`, a try/catch-guarded module loader - picked
because it has multiple jumps with different, cross-checkable targets)
has a `Jmp` at relative offset 62 with operand 25; 62+25=87 lands
exactly on the `LoadConstFalse` instruction that begins the
"try succeeded" epilogue, skipping over the `Catch` block entirely -
exactly the control flow a guarded loader should have. A `JmpTrue` at
relative offset 20 (operand 75) and a `JmpFalse` at relative offset 33
(operand 62) both resolve to relative offset 95 - two different
early-exit conditions converging on the same cleanup code, which is
equally plausible and further confirms the formula rather than being
a coincidence of one lucky number. See
`tests/test_hermes_disassembler_jump_target.py`.

`is_jump_instruction`/`resolve_jump_target` below only ever look at
operand INDEX 0 - accurate for every DEFINE_JUMP_N opcode, but NOT a
complete inventory of where `Addr8`/`Addr32` can appear: the
`SwitchImm`/`UIntSwitchImm`/`StringSwitchImm` family also carries one,
at a LATER operand index, as its "value out of range" default-case
target (confirmed against real hermes-dec output - `hbc-disassembler`
run directly against apps/testy/96 and apps/testy/98, not just its
source read - see `SwitchTable.py`, which uses
`resolve_operand_jump_target` below for that operand specifically,
rather than this module's own `is_jump_instruction`/
`resolve_jump_target`, since those two are intentionally scoped to the
"single jump target as operand 0" case their own callers (and
`tests/test_hermes_disassembler_jump_target.py`'s pinned counts) rely
on.
"""
from __future__ import annotations

from hermes_disassembler.format.Opcode import Instruction, load_opcode_table

__all__ = ["is_jump_instruction", "resolve_jump_target", "resolve_operand_jump_target"]

_JUMP_OPERAND_TYPES = frozenset({"Addr8", "Addr32"})


def is_jump_instruction(instruction: Instruction, version: int) -> bool:
    """
    True if `instruction`'s opcode takes a relative jump target as its
    first operand (see module docstring). `SwitchImm`/`UIntSwitchImm`/
    `StringSwitchImm` are deliberately NOT considered jump instructions
    here (their Addr8/Addr32 operand isn't at index 0) - see
    `resolve_operand_jump_target` below for those.
    """
    _name, operand_types, _semantics = load_opcode_table(version)[instruction.opcode]
    return bool(operand_types) and operand_types[0] in _JUMP_OPERAND_TYPES


def resolve_jump_target(instruction: Instruction, version: int) -> int | None:
    """
    Return the absolute byte offset `instruction` jumps to, or `None`
    if it isn't a jump instruction (see `is_jump_instruction`).

    The target is `instruction.offset + <first operand>` - relative to
    where the jump instruction itself starts, not where its operand
    bytes start or where the instruction ends (confirmed against real
    data, see module docstring). The first operand is signed
    (`Addr8`/`Addr32`), so backward jumps produce a smaller offset than
    `instruction.offset` - callers should not assume the result is
    always >= instruction.offset.
    """
    if not is_jump_instruction(instruction, version):
        return None
    return instruction.offset + instruction.operands[0]


def resolve_operand_jump_target(instruction: Instruction, operand_index: int) -> int:
    """
    Return the absolute byte offset `instruction.operands[operand_index]`
    resolves to, treating it as a relative `Addr8`/`Addr32` jump target
    (same `instruction.offset + value` convention as `resolve_jump_target`,
    generalized to any operand index rather than only index 0). Callers
    are responsible for confirming the operand at that index is actually
    an `Addr8`/`Addr32` type - this function doesn't check.
    """
    return instruction.offset + instruction.operands[operand_index]
