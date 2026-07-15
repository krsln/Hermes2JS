from typing import ClassVar

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, ADDR, sequence


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


class JStrictEqualLong(JStrictEqual):
    """Jump if operands are strictly equal."""
    pass


class JStrictNotEqualLong(JStrictNotEqual):
    """Jump if operands are not strictly equal."""
    pass
