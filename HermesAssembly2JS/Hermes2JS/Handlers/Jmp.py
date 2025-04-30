import re

from Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from Hermes2JS.Models.OpcodeResult import OpcodeResult
from Hermes2JS.Models.JSVariable import JSVariable
from Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from Hermes2JS.Models.OpcodeHandler import OpcodeHandler

"""
Handlers for Hermes bytecode jump opcodes.

This module defines handlers for jump-related opcodes (Jmp, JmpTrue, JmpFalse, JmpUndefined)
used in the Hermes bytecode to JavaScript converter. The handlers parse opcode arguments,
track jump targets, and emit temporary control flow statements for post-processing.

Regex Patterns:
    _REGEX_PATTERNS: Precompiled regexes for parsing jump opcode arguments.
        - 'Jmp': Matches 'Addr8: <offset>' for unconditional jumps.
        - 'Conditional': Matches 'Addr8: <offset>, Reg8: <reg>' for conditional jumps.
"""

_REGEX_PATTERNS = {
    "Jmp": re.compile(r'^Addr\d+:\s*(\d+)$'),
    "Conditional": re.compile(r'^Addr\d+:\s*(\d+),\s*Reg\d+:\s*(\d+)$')
}

from typing import Tuple, Optional


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
        """
        Handle an unconditional jump opcode (Jmp).

        Args:
            analysis (HermesAnalysis): The analysis context.
            entry (OpcodeEntry): The opcode entry with args 'Addr8: <offset>'.

        Returns:
            OpcodeResult: Result with a goto statement and target address.

        Example:
            <Jmp>: <Addr8: 6>  # Jumps to address = current address + 6
        """
        try:
            addr_offset, _ = _parse_jump_args(entry, "Jmp")
        except ValueError as e:
            return self.InvalidArgs(entry, str(e))

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
        """
        Handle a conditional jump if true opcode (JmpTrue).

        Args:
            analysis (HermesAnalysis): The analysis context.
            entry (OpcodeEntry): The opcode entry with args 'Addr8: <offset>, Reg8: <reg>'.

        Returns:
            OpcodeResult: Result with an if statement and target address.

        Example:
            <JmpTrue>: <Addr8: 8, Reg8: 9>  # If r9, jump to address + 8
        """
        try:
            addr_offset, reg = _parse_jump_args(entry, "Conditional")
        except ValueError as e:
            return self.InvalidArgs(entry, str(e))

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
        """
        Handle a conditional jump if false opcode (JmpFalse).

        Args:
            analysis (HermesAnalysis): The analysis context.
            entry (OpcodeEntry): The opcode entry with args 'Addr8: <offset>, Reg8: <reg>'.

        Returns:
            OpcodeResult: Result with an if statement and target address.

        Example:
            <JmpFalse>: <Addr8: 40, Reg8: 9>  # If !r9, jump to address + 40
        """
        try:
            addr_offset, reg = _parse_jump_args(entry, "Conditional")
        except ValueError as e:
            return self.InvalidArgs(entry, str(e))

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
        """
        Handle a conditional jump if undefined opcode (JmpUndefined).

        Args:
            analysis (HermesAnalysis): The analysis context.
            entry (OpcodeEntry): The opcode entry with args 'Addr8: <offset>, Reg8: <reg>'.

        Returns:
            OpcodeResult: Result with an if statement and target address.

        Example:
            <JmpUndefined>: <Addr8: 18, Reg8: 0>  # If r0 is undefined, jump to address + 18
        """
        try:
            addr_offset, reg = _parse_jump_args(entry, "Conditional")
        except ValueError as e:
            return self.InvalidArgs(entry, str(e))

        target_addr = entry.address + addr_offset
        analysis.gotoList.append(target_addr)

        condition = self.GetValueByReg(analysis.results, reg)
        value = f"if ({condition} === undefined) {{ /* jump to label_{target_addr} */ }}"

        variable = JSVariable(self.__class__.__name__, entry.address, "", value)
        analysis.AddResult(entry, variable, goto=target_addr)

        return OpcodeResult(entry, variable, goto=target_addr)
