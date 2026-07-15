from typing import Tuple, Optional, ClassVar

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from ._shared_patterns import REG, ADDR, sequence

# Updated patterns supporting negative offsets
_JMP_PATTERN = sequence(ADDR)
_JMP_CONDITIONAL_PATTERN = sequence(ADDR, REG)


def _parse_jump_args(entry: OpcodeEntry, is_conditional: bool = False) -> Tuple[int, Optional[int]]:
    """Parse jump arguments, supporting negative address offsets."""
    args = entry.args.strip()
    if not args:
        raise ValueError(f"Empty arguments for {entry.opcode}")

    pattern = _JMP_CONDITIONAL_PATTERN if is_conditional else _JMP_PATTERN
    match = pattern.match(args)

    if not match:
        raise ValueError(f"Invalid {entry.opcode} arguments: {args}")

    addr_offset = int(match.group(1))

    if not is_conditional:
        return addr_offset, None

    reg = int(match.group(2))
    return addr_offset, reg


# Unconditional branch to Arg1.
# Example: <Jmp>: <Addr8: 6>  # Address: 00000013
class Jmp(OpcodeHandler):
    """Unconditional jump."""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        try:
            addr_offset, _ = _parse_jump_args(entry, is_conditional=False)
        except ValueError as e:
            return self.InvalidArgs(analysis, entry, str(e))

        target_addr = entry.address + addr_offset
        analysis.gotoList.append(target_addr)

        value = f"goto label_{target_addr};"

        variable = JSVariable(handler, entry.address, "", value)
        analysis.AddResult(entry, variable, goto=target_addr)

        return OpcodeResult(entry, variable, goto=target_addr)


# Conditional branches to Arg1 based on Arg2.
# Example: <JmpTrue>: <Addr8: 8, Reg8: 9>  # Address: 00000044
class JmpTrue(OpcodeHandler):
    """Jump if true."""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        try:
            addr_offset, reg = _parse_jump_args(entry, is_conditional=True)
        except ValueError as e:
            return self.InvalidArgs(analysis, entry, str(e))

        target_addr = entry.address + addr_offset
        analysis.gotoList.append(target_addr)

        condition = self.GetValueByReg(analysis.results, reg) or f"r{reg}"
        value = f"if ({condition}) {{ /* jump to label_{target_addr} */ }}"

        variable = JSVariable(handler, entry.address, "", value)
        analysis.AddResult(entry, variable, goto=target_addr)

        return OpcodeResult(entry, variable, goto=target_addr)


# Diğer sınıflar (JmpFalse, JmpUndefined, JCompareX vb.) aynı kalabilir.
# Sadece alttaki kısmı da güncelleyelim:

# Conditional branches to Arg1 based on Arg2.
# Example: <JmpFalse>: <Addr8: 40, Reg8: 9>  # Address: 000001ff
class JmpFalse(OpcodeHandler):
    """Jump if false."""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        try:
            addr_offset, reg = _parse_jump_args(entry, is_conditional=True)
        except ValueError as e:
            return self.InvalidArgs(analysis, entry, str(e))

        target_addr = entry.address + addr_offset
        analysis.gotoList.append(target_addr)

        condition = self.GetValueByReg(analysis.results, reg) or f"r{reg}"
        value = f"if (!{condition}) {{ /* jump to label_{target_addr} */ }}"

        variable = JSVariable(handler, entry.address, "", value)
        analysis.AddResult(entry, variable, goto=target_addr)

        return OpcodeResult(entry, variable, goto=target_addr)


# Jump if the value is undefined.
# Example: <JmpUndefined>: <Addr8: 18, Reg8: 0>  # Address: 00000043
class JmpUndefined(OpcodeHandler):
    """Jump if undefined."""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        try:
            addr_offset, reg = _parse_jump_args(entry, is_conditional=True)
        except ValueError as e:
            return self.InvalidArgs(analysis, entry, str(e))

        target_addr = entry.address + addr_offset
        analysis.gotoList.append(target_addr)

        condition = self.GetValueByReg(analysis.results, reg) or f"r{reg}"
        value = f"if ({condition} === undefined) {{ /* jump to label_{target_addr} */ }}"

        variable = JSVariable(handler, entry.address, "", value)
        analysis.AddResult(entry, variable, goto=target_addr)

        return OpcodeResult(entry, variable, goto=target_addr)


class JCompareX(OpcodeHandler):
    """Base class for comparison jumps."""
    _PATTERN = sequence(ADDR, REG, REG)

    operator: ClassVar[str] = "=="

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, f"Expected Addr, Reg, Reg for {handler}")

        addr_offset, lhs_reg, rhs_reg = map(int, match.groups())
        target_addr = entry.address + addr_offset
        analysis.gotoList.append(target_addr)

        lhs_val = self.GetValueByReg(analysis.results, lhs_reg) or f"r{lhs_reg}"
        rhs_val = self.GetValueByReg(analysis.results, rhs_reg) or f"r{rhs_reg}"

        value = f"if ({lhs_val} {self.operator} {rhs_val}) {{ /* jump to label_{target_addr} */ }}"

        variable = JSVariable(handler, entry.address, "", value)
        analysis.AddResult(entry, variable, goto=target_addr)

        return OpcodeResult(entry, variable, goto=target_addr)


# Comparison classes
class JLess(JCompareX): operator = "<"


class JNotLess(JCompareX): operator = ">="


class JEqual(JCompareX): operator = "=="


class JStrictEqual(JCompareX): operator = "==="


class JStrictNotEqual(JCompareX): operator = "!=="


# Long variants
class JmpTrueLong(JmpTrue): pass


class JmpFalseLong(JmpFalse): pass
