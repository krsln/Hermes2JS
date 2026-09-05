from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, ADDR, UINT32
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.terminators import TerminatorSwitch

logger = get_logger(__name__)


# Reg8, UInt32, Addr32, UInt32, UInt32 (total size 17)
# DEFINE_OPCODE_5(SwitchImm, Reg8, UInt32, Addr32, UInt32, UInt32)
# Example: <SwitchImm>: <Reg8: 3, UInt32: 970, Addr32: 954, UInt32: 0, UInt32: 27>  # Address: 000003d6  # Jump table: [000003a2, ..., 0000018e]
class SwitchImm(OpcodeHandler):
    """"
    Jump table switch - using a table of offset, jump to the offset of the given
    input or to the default block if out of range (or not right type)
    """

    ARGUMENTS = ArgsPattern(sequence(REG, UINT32, ADDR, UINT32, UINT32), "Reg8, UInt32, Addr32, UInt32, UInt32")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        selector_reg = int(match.group(1))
        selector = self.get_register_expression(ctx.analysis, selector_reg)

        case_map = {}

        if ctx.entry.jump_table:
            first_case = int(match.group(4))
            last_case = int(match.group(5))

            expected = last_case - first_case + 1

            if len(ctx.entry.jump_table) != expected:
                logger.warning("Jump table size mismatch: expected %d entries, got %d", expected,
                               len(ctx.entry.jump_table))

            for value, target in zip(
                    range(first_case, first_case + len(ctx.entry.jump_table)),
                    ctx.entry.jump_table,
            ):
                case_map[value] = target

        default_target = ctx.entry.target_address
        terminator = TerminatorSwitch(selector=selector, case_map=case_map, default_target=default_target)

        result = OpcodeResult(ctx.entry, value=None, terminator=terminator, dest_reg=None)
        ctx.analysis.add_result(result)

        return result


# Reg8, UInt32, Addr32, UInt32, UInt32 (total size 17)
# DEFINE_OPCODE_5(UIntSwitchImm, Reg8, UInt32, Addr32, UInt32, UInt32)
# Example: <UIntSwitchImm>: <Reg8: 17, UInt32: 5474, Addr32: 5320, UInt32: 0, UInt32: 31>  # Address: 00001a74
class UIntSwitchImm(SwitchImm):
    """
    Same operand layout as `SwitchImm` (`Reg8, UInt32, Addr32, UInt32,
    UInt32`) - verified against hbc98 and hbc99's instruction definitions,
    where it replaces `SwitchImm` (their version ranges don't overlap:
    `SwitchImm` up to hbc97, `UIntSwitchImm` from hbc98 on). Only
    difference is that the selector is compared as an unsigned integer;
    that distinction doesn't affect this handler, which only reads the
    jump table and case range, not the selector's signedness.
    """

    pass


# Reg8, UInt32, UInt32, Addr32, UInt32 (total size 17)
# DEFINE_OPCODE_5(StringSwitchImm, Reg8, UInt32, UInt32, Addr32, UInt32)
# Example: <StringSwitchImm>: <Reg8: 1, UInt32: 3, UInt32: 86, Addr32: 82, UInt32: 12>  # Address: 0000007a
class StringSwitchImm(OpcodeHandler):
    """All-string `switch` statement. Case targets come from an out-of-line table this handler can't yet resolve."""

    ARGUMENTS = ArgsPattern(sequence(REG, UINT32, UINT32, ADDR, UINT32), "Reg8, UInt32, UInt32, Addr32, UInt32")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        selector_reg = int(match.group(1))
        selector = self.get_register_expression(ctx.analysis, selector_reg)

        # Case targets live in an out-of-line string-switch table (Arg3
        # offset) that this handler does not resolve -- see module
        # comment. Only the default-jump (Addr32, Arg4) is picked up if
        # the disassembler surfaces it as a plain `Addr` token, same as
        # SwitchImm's existing regex.
        targets = []
        for offset in sequence(ADDR).findall(ctx.entry.args):
            target = ctx.entry.address + int(offset)
            ctx.analysis.gotoList.append(target)
            targets.append(target)

        case_map = {}

        default_target = ctx.entry.target_address
        terminator = TerminatorSwitch(selector=selector, case_map=case_map, default_target=default_target)

        result = OpcodeResult(ctx.entry, value=None, terminator=terminator, dest_reg=None)
        ctx.analysis.add_result(result)

        return result
