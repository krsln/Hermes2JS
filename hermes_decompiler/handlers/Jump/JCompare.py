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


# @formatter:off
# Equality
# ---------
class JEqual(JCompareX): operator = "=="
class JEqualLong(JEqual):  pass

class JNotEqual(JCompareX):  operator = "!="
class JNotEqualLong(JNotEqual):  pass

class JStrictEqual(JCompareX): operator = "==="
class JStrictEqualLong(JStrictEqual):  pass

class JStrictNotEqual(JCompareX): operator = "!=="
class JStrictNotEqualLong(JStrictNotEqual):  pass

# Less
# ----
class JLess(JCompareX): operator = "<"
class JLessN(JLess): pass
class JLessLong(JLess): pass

class JLessEqual(JCompareX): operator = "<="
class JLessEqualN(JLessEqual): pass
class JLessEqualLong(JLessEqual):  pass

class JNotLess(JCompareX): operator = ">="
class JNotLessN(JNotLess): pass
class JNotLessNLong(JNotLess): pass
class JNotLessLong(JNotLess): pass

class JNotLessEqual(JCompareX):  operator = ">"
class JNotLessEqualN(JNotLessEqual): pass
class JNotLessEqualLong(JNotLessEqual): pass
class JNotLessEqualNLong(JNotLessEqual): pass

# Greater
# -------
class JGreater(JCompareX): operator = ">"
class JGreaterN(JGreater): pass
class JGreaterLong(JGreater): pass

class JGreaterEqual(JCompareX): operator = ">="
class JGreaterEqualN(JGreaterEqual): pass
class JGreaterEqualLong(JGreaterEqual): pass

class JNotGreater(JCompareX): operator = "<="
class JNotGreaterN(JNotGreater): pass
class JNotGreaterLong(JNotGreater): pass

class JNotGreaterEqual(JCompareX): operator = "<"
class JNotGreaterEqualN(JNotGreaterEqual):  pass
class JNotGreaterEqualNLong(JNotGreaterEqual): pass
class JNotGreaterEqualLong(JNotGreaterEqual): pass
# @formatter:on
