from hermes_decompiler.analysis.terminators import TerminatorSwitch
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.handlers import OpcodeHandler, REG, ADDR, UINT32, sequence
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis

logger = get_logger(__name__)


# Reg8, UInt32, Addr32, UInt32, UInt32 (total size 17)
# DEFINE_OPCODE_5(SwitchImm, Reg8, UInt32, Addr32, UInt32, UInt32)
# Example: <SwitchImm>: <Reg8: 3, UInt32: 970, Addr32: 954, UInt32: 0, UInt32: 27>  # Address: 000003d6  # Jump table: [000003a2, ..., 0000018e]
class SwitchImm(OpcodeHandler):
    """"
    Jump table switch - using a table of offset, jump to the offset of the given
    input or to the default block if out of range (or not right type)
    """

    _PATTERN = sequence(REG, UINT32, ADDR, UINT32, UINT32)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis,
                entry,
                "Expected a leading Reg selector",
            )

        selector_reg = int(match.group(1))
        selector = self.get_register_expression(analysis, selector_reg)

        # if entry.jump_table:
        #     targets = list(entry.jump_table)
        # else:
        #     targets = []
        # # print("targets",targets)

        case_map = {}

        if entry.jump_table:
            first_case = int(match.group(4))
            last_case = int(match.group(5))

            expected = last_case - first_case + 1

            if len(entry.jump_table) != expected:
                logger.warning("Jump table size mismatch: expected %d entries, got %d", expected, len(entry.jump_table))

            for value, target in zip(
                    range(first_case, first_case + len(entry.jump_table)),
                    entry.jump_table,
            ):
                case_map[value] = target
        # print("case_map",case_map)

        default_target = entry.target_address
        terminator = TerminatorSwitch(selector=selector, case_map=case_map, default_target=default_target)

        result = OpcodeResult(entry, value=None, terminator=terminator, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, UInt32, Addr32, UInt32, UInt32 (total size 17)
# DEFINE_OPCODE_5(UIntSwitchImm, Reg8, UInt32, Addr32, UInt32, UInt32)
# Example: <UIntSwitchImm>: <Reg8: 17, UInt32: 5474, Addr32: 5320, UInt32: 0, UInt32: 31>  # Address: 00001a74
class UIntSwitchImm(SwitchImm):
    # todo: wrong?
    pass


# Reg8, UInt32, UInt32, Addr32, UInt32 (total size 17)
# DEFINE_OPCODE_5(StringSwitchImm, Reg8, UInt32, UInt32, Addr32, UInt32)
# Example: <StringSwitchImm>: <Reg8: 1, UInt32: 3, UInt32: 86, Addr32: 82, UInt32: 12>  # Address: 0000007a
class StringSwitchImm(OpcodeHandler):
    """All-string `switch` statement. Case targets come from an out-of-line table this handler can't yet resolve."""

    _PATTERN = sequence(REG, UINT32, UINT32, ADDR, UINT32)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected a leading Reg selector",
            )

        selector_reg = int(match.group(1))
        selector = self.get_register_expression(analysis, selector_reg)

        # Case targets live in an out-of-line string-switch table (Arg3
        # offset) that this handler does not resolve -- see module
        # comment. Only the default-jump (Addr32, Arg4) is picked up if
        # the disassembler surfaces it as a plain `Addr` token, same as
        # SwitchImm's existing regex.
        targets = []
        for offset in sequence(ADDR).findall(entry.args):
            target = entry.address + int(offset)
            analysis.gotoList.append(target)
            targets.append(target)

        case_map = {}

        default_target = entry.target_address
        terminator = TerminatorSwitch(selector=selector, case_map=case_map, default_target=default_target)

        result = OpcodeResult(entry, value=None, terminator=terminator, dest_reg=None)
        analysis.add_result(result)

        return result
