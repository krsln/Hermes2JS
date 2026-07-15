import re
from typing import Tuple, Optional

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

_REGEX_PATTERNS = {
    "Jmp": re.compile(r'^Addr\d+:\s*(\d+)$'),
    "Conditional": re.compile(r'^Addr\d+:\s*(\d+),\s*Reg\d+:\s*(\d+)$')
}


def _parse_jump_args(line: OpcodeEntry, pattern_key: str) -> Tuple[int, Optional[int]]:
    """
    Parse jump opcode arguments.

    Args:
        line (OpcodeEntry): The opcode entry.
        pattern_key (str): The regex pattern key ('Jmp' or 'Conditional').

    Returns:
        Tuple[int, Optional[int]]: Address offset and optional register number.

    Raises:
        ValueError: If arguments are invalid.
    """
    args = line.args.strip()
    if not args:
        raise ValueError(f"Empty arguments for {line.opcode}")

    match = _REGEX_PATTERNS[pattern_key].match(args)
    if not match:
        raise ValueError(f"Invalid {line.opcode} args: {args}")

    addr = int(match.group(1))
    if addr < 0:
        raise ValueError(f"Negative address offset: {addr}")

    if pattern_key == "Jmp":
        return addr, None
    reg = int(match.group(2))
    return addr, reg


# Unconditional branch to Arg1.
# Example: <Jmp>: <Addr8: 6>  # Address: 00000013
class Jmp(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        try:
            addr_offset, _ = _parse_jump_args(entry, "Jmp")
        except ValueError as e:
            return self.InvalidArgs(analysis, entry, str(e))

        target_addr = entry.address + addr_offset
        analysis.gotoList.append(target_addr)
        value = f"goto label_{target_addr};"

        variable = JSVariable(self.__class__.__name__, entry.address, "", value)
        analysis.AddResult(entry, variable, goto=target_addr)

        return OpcodeResult(entry, variable, goto=target_addr)


# Conditional branches to Arg1 based on Arg2.
# Example: <JmpTrue>: <Addr8: 8, Reg8: 9>  # Address: 00000044
class JmpTrue(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        try:
            addr_offset, reg = _parse_jump_args(entry, "Conditional")
        except ValueError as e:
            return self.InvalidArgs(analysis, entry, str(e))

        target_addr = entry.address + addr_offset
        analysis.gotoList.append(target_addr)

        condition = self.GetValueByReg(analysis.results, reg)
        value = f"if ({condition}) {{ /* jump to label_{target_addr} */ }}"

        variable = JSVariable(self.__class__.__name__, entry.address, "", value)
        analysis.AddResult(entry, variable, goto=target_addr)

        return OpcodeResult(entry, variable, goto=target_addr)


class JmpTrueLong(JmpTrue):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return super().Handle(analysis, entry)


# Conditional branches to Arg1 based on Arg2.
# Example: <JmpFalse>: <Addr8: 40, Reg8: 9>  # Address: 000001ff
class JmpFalse(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        try:
            addr_offset, reg = _parse_jump_args(entry, "Conditional")
        except ValueError as e:
            return self.InvalidArgs(analysis, entry, str(e))

        target_addr = entry.address + addr_offset
        analysis.gotoList.append(target_addr)

        condition = self.GetValueByReg(analysis.results, reg)
        value = f"if (!{condition}) {{ /* jump to label_{target_addr} */ }}"

        variable = JSVariable(self.__class__.__name__, entry.address, "", value)
        analysis.AddResult(entry, variable, goto=target_addr)

        return OpcodeResult(entry, variable, goto=target_addr)


# Jump if the value is undefined.
# Example: <JmpUndefined>: <Addr8: 18, Reg8: 0>  # Address: 00000043
class JmpUndefined(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        try:
            addr_offset, reg = _parse_jump_args(entry, "Conditional")
        except ValueError as e:
            return self.InvalidArgs(analysis, entry, str(e))

        target_addr = entry.address + addr_offset
        analysis.gotoList.append(target_addr)

        condition = self.GetValueByReg(analysis.results, reg)
        value = f"if ({condition} === undefined) {{ /* jump to label_{target_addr} */ }}"

        variable = JSVariable(self.__class__.__name__, entry.address, "", value)
        analysis.AddResult(entry, variable, goto=target_addr)

        return OpcodeResult(entry, variable, goto=target_addr)
