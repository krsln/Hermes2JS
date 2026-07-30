import re

from hermes_decompiler.analysis.terminators import TerminatorSwitch
from hermes_decompiler.handlers import OpcodeHandler, REG, ADDR, UINT8, UINT16, sequence
from hermes_decompiler.handlers import OpcodeHandler
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, UInt32, Addr32, UInt32, UInt32 (total size 17)
# DEFINE_OPCODE_5(SwitchImm, Reg8, UInt32, Addr32, UInt32, UInt32)
# Example: <SwitchImm>: <Reg8: 3, UInt32: 970, Addr32: 954, UInt32: 0, UInt32: 27>  # Address: 000003d6  # Jump table: [000003a2, ..., 0000018e]
class SwitchImm(OpcodeHandler):
    """"
    Jump table switch - using a table of offset, jump to the offset of the given
    input or to the default block if out of range (or not right type)
    """

    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        print(entry)

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis,
                entry,
                "Expected a leading Reg selector",
            )

        selector_reg = int(match.group(1))
        selector = self.get_register_value(analysis, selector_reg)

        targets = []

        for offset in sequence(ADDR).findall(entry.args):
            target = entry.address + int(offset)
            analysis.gotoList.append(target)
            targets.append(target)



        terminator = TerminatorSwitch(selector=selector, targets=tuple(targets))

        # NOTE (fix): the original never set `control_flow`, defaulting
        # to NORMAL despite having multiple successors and no
        # fallthrough - same class of bug already fixed for JCompareX.
        # pure control flow: no operand value of its own
        result = OpcodeResult(entry, value=None, terminator=terminator, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, UInt32, Addr32, UInt32, UInt32 (total size 17)
# DEFINE_OPCODE_5(UIntSwitchImm, Reg8, UInt32, Addr32, UInt32, UInt32)
# Example: <UIntSwitchImm>: <Reg8: 17, UInt32: 5474, Addr32: 5320, UInt32: 0, UInt32: 31>  # Address: 00001a74
class UIntSwitchImm(SwitchImm):
    pass


# Reg8, UInt32, UInt32, Addr32, UInt32 (total size 17)
# DEFINE_OPCODE_5(StringSwitchImm, Reg8, UInt32, UInt32, Addr32, UInt32)
# Example: <StringSwitchImm>: <Reg8: 1, UInt32: 3, UInt32: 86, Addr32: 82, UInt32: 12>  # Address: 0000007a
class StringSwitchImm(OpcodeHandler):
    """All-string `switch` statement. Case targets come from an out-of-line table this handler can't yet resolve."""

    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected a leading Reg selector",
            )

        selector_reg = int(match.group(1))
        selector = self.get_register_value(analysis, selector_reg)

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

        terminator = TerminatorSwitch(selector=selector, targets=tuple(targets))

        result = OpcodeResult(entry, value=None, terminator=terminator, dest_reg=None)
        analysis.add_result(result)

        return result
