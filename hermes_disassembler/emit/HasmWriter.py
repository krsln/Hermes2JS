"""
Formats decoded functions/instructions into hermes-dec-compatible
`.hasm` text - the format `vendor/hermes-dec` (AGPL, fetched
separately, see `scripts/fetch-hermes-dec.sh`) produces today, and
that `hermes_decompiler`'s frontend (`OpcodeParser`, `OperandPatterns`)
already parses. This is the module that lets `hermes_disassembler`
actually replace that AGPL dependency, per the package docstring's
stated purpose.

Format ground truth: a REAL hermes-dec output fixture already
committed in this repo,
`apps/demo/fixtures/96/sections/section_15042.hasm` - not a guess, not
derived from OpcodeParser's regexes alone (those only constrain the
grammar, not every literal detail like spacing or hex digit count):

    => [Function #15042 "runAllTests" of 30 bytes]: 1 params, frame size=13, strict=1, exc handler=0, debug info=0  @ offset 0x0026772c

    Bytecode listing:

    ==> 00000000: <LoadConstUndefined>: <Reg8: 0>
    ==> 00000002: <GetEnvironment>: <Reg8: 1, UInt8: 0>
    ==> 00000009: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 65>  # String: 'apply' (Identifier)
    ==> 0000001c: <Ret>: <Reg8: 0>

Every formatting decision below traces to that example: 8-hex-digit
lowercase addresses (both the function's absolute file offset and each
instruction's offset RELATIVE TO THE FUNCTION START, matching
`==> 00000000:` starting at zero); the function header's exact field
order, labels, and the double space before `@ offset`; operand labels
using the *semantic* tag (`string_id`) instead of the raw encoded type
(`UInt8`) wherever `hermes_disassembler.format.Opcode`'s table carries
one (see `tools/hermes/generate_opcode_tables.py`'s `OPERAND_STRING_ID`
handling); and the string comment's exact shape, including which of
`(Identifier)`/`(String)` to use (from
`StringTable.is_identifier()`).

Confirmed but NOT from that one fixture - separately validated in this
package's own test suite before being relied on here: the jump-target
`# Address: <hex>` comment format is inferred from hermes-dec's general
convention (not present in the one fixture line quoted above, which
has no jump instruction) and given in the SAME relative-to-function
addressing as `==>` lines, per `JumpTarget.py`'s absolute-offset
convention converted back to relative here.

Known gaps, not yet implemented:
- `function_id`/`bigint_id` operand comments (only `string_id` is
  handled - the fixture only demonstrates that one, and there's no
  BigInt table in this package yet to resolve a bigint_id against
  anyway).
- Multiple string_id operands on one instruction (e.g. `CreateRegExp`
  has two, per `tools/hermes/generate_opcode_tables.py`'s survey) -
  untested; this module joins multiple comments with "; " as a
  reasonable guess, not a confirmed hermes-dec convention.
- Exact `Double` operand text formatting (no fixture example with one).
"""
from __future__ import annotations

from hermes_disassembler.format.FunctionHeader import FunctionHeaderEntry
from hermes_disassembler.format.JumpTarget import is_jump_instruction, resolve_jump_target
from hermes_disassembler.format.Opcode import Instruction, load_opcode_table
from hermes_disassembler.format.StringTable import StringTable

__all__ = ["format_instruction", "format_function"]


def _format_operand(operand_type: str, value: int | float, semantic: str | None) -> str:
    label = semantic if semantic is not None else operand_type
    return f"{label}: {value}"


def format_instruction(
        instruction: Instruction,
        function_offset: int,
        table: StringTable,
        version: int,
) -> str:
    """
    Format one instruction as a `==> <rel_offset>: <Name>: <operands>`
    line, with a trailing `  # ...` comment for string references and
    jump targets where applicable. `function_offset` is the owning
    function's `FunctionHeaderEntry.offset` (needed to print the
    instruction's offset relative to its function, matching hermes-dec's
    `==> 00000000:`-from-zero convention - see module docstring).
    """
    _name, operand_types, semantics = load_opcode_table(version)[instruction.opcode]

    operand_strs = [
        _format_operand(operand_types[i], value, semantics.get(i))
        for i, value in enumerate(instruction.operands)
    ]

    comment_parts: list[str] = []
    for i, value in enumerate(instruction.operands):
        if semantics.get(i) == "string_id":
            string_value = table.resolve(value)
            kind = "Identifier" if table.is_identifier(value) else "String"
            comment_parts.append(f"String: {string_value!r} ({kind})")
        # function_id / bigint_id comments: not yet implemented, see module docstring

    if is_jump_instruction(instruction, version):
        absolute_target = resolve_jump_target(instruction, version)
        relative_target = absolute_target - function_offset
        comment_parts.append(f"Address: {relative_target:08x}")

    rel_offset = instruction.offset - function_offset
    line = f"==> {rel_offset:08x}: <{instruction.name}>: <{', '.join(operand_strs)}>"
    if comment_parts:
        line += f"  # {'; '.join(comment_parts)}"
    return line


def format_function(
        header: FunctionHeaderEntry,
        instructions: tuple[Instruction, ...],
        table: StringTable,
        version: int,
) -> str:
    """
    Format a complete function block matching hermes-dec's shape:
    the `=> [Function #N "name" of B bytes]: ...` header line, a
    `Bytecode listing:` label, then one `format_instruction()` line per
    instruction - see module docstring for the exact fixture this
    reproduces.
    """
    name = table.resolve(header.function_name)
    header_line = (
        f'=> [Function #{header.index} "{name}" of {header.bytecode_size_in_bytes} bytes]: '
        f"{header.param_count} params, frame size={header.frame_size}, "
        f"strict={int(header.strict_mode)}, exc handler={int(header.has_exception_handler)}, "
        f"debug info={int(header.has_debug_info)}  @ offset 0x{header.offset:08x}"
    )

    lines = [header_line, "", "Bytecode listing:", ""]
    lines.extend(format_instruction(i, header.offset, table, version) for i in instructions)

    return "\n".join(lines)
