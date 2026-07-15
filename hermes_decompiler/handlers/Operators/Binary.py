from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


class BinaryOperator(OpcodeHandler):
    """Base class for binary register operations."""

    _PATTERN = sequence(REG, REG, REG)

    operator = "+"

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(
                analysis,
                entry,
                "Expected three Reg8 arguments"
            )

        dest, lhs, rhs = map(int, match.groups())

        lhs_val = self.GetValueByReg(analysis.results, lhs) or f"r{lhs}"
        rhs_val = self.GetValueByReg(analysis.results, rhs) or f"r{rhs}"

        variable = JSVariable(handler, entry.address, f"r{dest}", f"{lhs_val} {self.operator} {rhs_val}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# @formatter:off
class Mul(BinaryOperator): operator = "*"
class Sub(BinaryOperator): operator = "-"
class Mod(BinaryOperator): operator = "%"
class BitAnd(BinaryOperator): operator = "&"
class BitOr(BinaryOperator): operator = "|"
class LShift(BinaryOperator): operator = "<<"
class RShift(BinaryOperator): operator = ">>"
class URShift(BinaryOperator): operator = ">>>"
class Less(BinaryOperator): operator = "<"
class LessEq(BinaryOperator): operator = "<="

class Eq(BinaryOperator): operator = "=="
class Neq(BinaryOperator): operator = "!="
class StrictEq(BinaryOperator): operator = "==="
class StrictNeq(BinaryOperator): operator = "!=="
# @formatter:on
