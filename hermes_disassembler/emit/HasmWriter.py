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
- `bigint_id` operand comments (no BigInt table parser in this package yet).
- Multiple string_id operands on one instruction (e.g. `CreateRegExp`
  has two) - each gets its own `  # ` segment, per hermes-dec's real
  output for that exact case (confirmed, not guessed).
- Exact `Double` operand text formatting (no fixture example with one).
- `NewArrayWithBuffer`/`NewObjectWithBuffer`/`NewArrayWithBufferLong`/etc.
  literal-content comments (e.g. `# Array: [1, 0, 2]`, `# Object: {'a': 1}`) -
  real hermes-dec output includes these; this module doesn't yet parse
  the literal value buffer / object key-value buffers needed to
  reconstruct them. Confirmed missing by direct comparison against real
  hermes-dec output, not just inferred.
- Exception handler resolution (`format_function`'s
  `  [Exception handlers: ...]` line) has one known-bad case: a
  function that is BOTH overflowed (`was_large_header=True`) AND has
  `has_exception_handler=True` in bytecode 96 specifically. Validated
  at scale otherwise - 1082/1082 in bytecode 98 (where every
  exception-handler function overflows) and 660/660 non-overflowed
  bytecode-96 cases - but apps/testy/96's own "global" function (the
  huge bundle-init function, index 0) is exactly this combination and
  its handler offsets don't land on real instruction boundaries with
  the same formula that works everywhere else. See
  `hermes_disassembler.format.ExceptionHandlerTable`'s module docstring
  for the full validation story and this gap's details. Functions with
  `has_debug_info=True` are also unvalidated (see that same module).

Pre-existing, separate gap worth knowing about here:
`scripts/split_output_file.py`'s `FUNCTION_HEADER_RE` required a
function-header line to start with `[Function` and didn't match the
`=> [Function...` prefix this module (and real hermes-dec output)
actually produces - already fixed (see that script's own history), so
`format_bundle()`'s output now splits into descriptive `function_N_name`
filenames, not anonymous `section_N` ones.
"""
from __future__ import annotations

from hermes_disassembler.core.Exceptions import HermesBytecodeError
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.ExceptionHandlerTable import resolve_exception_handlers
from hermes_disassembler.format.FunctionHeader import FunctionHeaderEntry
from hermes_disassembler.format.FunctionHeaderOverflow import resolve_overflowed_headers
from hermes_disassembler.format.JumpTarget import is_jump_instruction, resolve_jump_target
from hermes_disassembler.format.Opcode import Instruction, decode_function, load_opcode_table
from hermes_disassembler.format.StringTable import StringTable

#: scripts/split_output_file.py's own separator constant, duplicated
#: here rather than imported (that script isn't part of this package
#: and sits outside hermes_disassembler/hermes_decompiler's own
#: dependency graph) - keep in sync if that script's DEFAULT_SEPARATOR
#: ever changes.
SECTION_SEPARATOR = "==============="

__all__ = ["format_instruction", "format_function", "format_bundle", "SECTION_SEPARATOR"]


def _format_operand(operand_type: str, value: int | float, semantic: str | None) -> str:
    label = semantic if semantic is not None else operand_type
    return f"{label}: {value}"


def format_instruction(
        instruction: Instruction,
        function_offset: int,
        table: StringTable,
        version: int,
        all_functions: tuple[FunctionHeaderEntry, ...] | None = None,
) -> str:
    """
    Format one instruction as a `==> <rel_offset>: <Name>: <operands>`
    line, with a trailing `  # ...` comment (one per commented operand,
    each with its own `  # ` prefix - see module docstring) for string
    references, function references, and jump targets where applicable.
    `function_offset` is the owning function's `FunctionHeaderEntry.offset`
    (needed to print the instruction's offset relative to its function,
    matching hermes-dec's `==> 00000000:`-from-zero convention - see
    module docstring).

    `all_functions` - the full, overflow-resolved function list for this
    bundle (e.g. from `format_bundle`, or
    `FunctionHeaderOverflow.resolve_overflowed_headers`'s return value) -
    is needed to resolve `function_id` operands (e.g. `CreateGenerator`,
    `CreateClosure`) to their target function's own signature. Omit it
    (the default) to format a single function in isolation - `function_id`
    operands are then left without a comment rather than raising, since
    the target function's info genuinely isn't available.
    """
    _name, operand_types, semantics = load_opcode_table(version)[instruction.opcode]

    operand_strs = [
        _format_operand(operand_types[i], value, semantics.get(i))
        for i, value in enumerate(instruction.operands)
    ]

    comment_parts: list[str] = []
    for i, value in enumerate(instruction.operands):
        tag = semantics.get(i)
        if tag == "string_id":
            string_value = table.resolve(value)
            kind = "Identifier" if table.is_identifier(value) else "String"
            comment_parts.append(f"String: {string_value!r} ({kind})")
        elif tag == "function_id" and all_functions is not None:
            comment_parts.append(_format_function_reference(all_functions[value], table))
        # function_id with all_functions=None, and bigint_id always: no comment yet, see module docstring

    if is_jump_instruction(instruction, version):
        absolute_target = resolve_jump_target(instruction, version)
        relative_target = absolute_target - function_offset
        comment_parts.append(f"Address: {relative_target:08x}")

    rel_offset = instruction.offset - function_offset
    line = f"==> {rel_offset:08x}: <{instruction.name}>: <{', '.join(operand_strs)}>"
    for part in comment_parts:
        line += f"  # {part}"
    return line


def _format_function_reference(target: FunctionHeaderEntry, table: StringTable) -> str:
    """
    `# Function: [#N name of B bytes]: P params @ offset 0xHEX` for a
    `function_id` operand's comment.

    Known gap: hermes-dec shows a synthesized `?anon_<n>_<description>`
    name for functions it considers anonymous (observed in real output,
    e.g. `?anon_0_generatorWithLoopTest`), not the plain string-table
    name this uses - that heuristic isn't reverse-engineered here (it
    likely depends on debug info this package doesn't parse yet - see
    `hermes_disassembler`'s package docstring). Index, byte size, param
    count, and offset are the real, structurally-verified fields here;
    only the cosmetic name may not match hermes-dec byte-for-byte for
    an anonymous function.
    """
    name = table.resolve(target.function_name)
    return (
        f"Function: [#{target.index} {name} of {target.bytecode_size_in_bytes} bytes]: "
        f"{target.param_count} params @ offset 0x{target.offset:08x}"
    )


def format_function(
        data: bytes,
        header: FunctionHeaderEntry,
        instructions: tuple[Instruction, ...],
        table: StringTable,
        version: int,
        all_functions: tuple[FunctionHeaderEntry, ...] | None = None,
) -> str:
    """
    Format a complete function block matching hermes-dec's shape:
    the `=> [Function #N "name" of B bytes]: ...` header line (plus a
    `  [Exception handlers: ...]` line when `header.has_exception_handler`
    - see `ExceptionHandlerTable`'s module docstring for the one known-bad
    case), a `Bytecode listing:` label, then one `format_instruction()`
    line per instruction - see module docstring for the exact fixture
    this reproduces. `data` is the full bundle bytes (needed to resolve
    the exception handler table). `all_functions` is passed through to
    `format_instruction` for `function_id` resolution.
    """
    name = table.resolve(header.function_name)
    header_line = (
        f'=> [Function #{header.index} "{name}" of {header.bytecode_size_in_bytes} bytes]: '
        f"{header.param_count} params, frame size={header.frame_size}, "
        f"strict={int(header.strict_mode)}, exc handler={int(header.has_exception_handler)}, "
        f"debug info={int(header.has_debug_info)}  @ offset 0x{header.offset:08x}"
    )

    lines = [header_line]
    if header.has_exception_handler:
        lines.append(_format_exception_handlers_line(data, header))
    lines += ["", "Bytecode listing:", ""]
    lines.extend(
        format_instruction(i, header.offset, table, version, all_functions) for i in instructions
    )

    return "\n".join(lines)


def _format_exception_handlers_line(data: bytes, header: FunctionHeaderEntry) -> str:
    """
    `  [Exception handlers: [start=0xHEX, end=0xHEX, target=0xHEX] ...]`
    - confirmed format for a single handler against real hermes-dec
    output; the separator between multiple handlers is NOT confirmed
    (no multi-handler real example seen) - space-separated here as a
    reasonable guess.

    Falls back to a clearly-marked `<unresolved: ...>` placeholder
    instead of raising when resolution fails - see module docstring's
    "Known gaps" for the specific cases this covers (bytecode 96,
    overflowed AND has_exception_handler; any has_debug_info=True
    function) - so that one function's unresolved edge case doesn't
    abort `format_bundle()` for an entire otherwise-healthy bundle.
    """
    try:
        handlers = resolve_exception_handlers(data, header)
    except HermesBytecodeError as exc:
        return f"  [Exception handlers: <unresolved: {exc}>]"

    entries = " ".join(
        f"[start=0x{h.start:x}, end=0x{h.end:x}, target=0x{h.target:x}]" for h in handlers
    )
    return f"  [Exception handlers: {entries} ]"


def format_bundle(data: bytes, bc_header: BytecodeFileHeader, table: StringTable, version: int) -> str:
    """
    Decode and format every function in `data` into one hermes-dec-style
    multi-function `.hasm` text: each function's `format_function()`
    block, separated by `SECTION_SEPARATOR` on its own line - the exact
    boundary `scripts/split_output_file.py`'s `iter_sections()` scans
    for (see module docstring's "Pre-existing, separate gap" note re:
    function-name extraction specifically, which is unaffected here).

    This resolves overflowed function headers itself (via
    `FunctionHeaderOverflow.resolve_overflowed_headers`) - callers don't
    need to do that step separately first.
    """
    from hermes_disassembler.format.FunctionHeader import parse_function_headers

    entries = parse_function_headers(data, bc_header)
    resolved = resolve_overflowed_headers(data, bc_header, entries)

    blocks = []
    for entry in resolved:
        instructions = decode_function(data, entry.offset, entry.bytecode_size_in_bytes, version)
        blocks.append(format_function(data, entry, instructions, table, version, resolved))

    return f"\n\n\n{SECTION_SEPARATOR}\n\n".join(blocks)
