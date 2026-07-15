from typing import ClassVar

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


class UnaryOperator(OpcodeHandler):
    """Base class for unary register operations."""

    _PATTERN = sequence(REG, REG)

    prefix: ClassVar[str] = ""
    suffix: ClassVar[str] = ""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(
                analysis,
                entry,
                "Expected two Reg8 arguments",
            )

        dest_reg, src_reg = map(int, match.groups())

        src_val = self.GetValueByReg(
            analysis.results,
            src_reg,
        ) or f"r{src_reg}"

        variable = JSVariable(
            handler,
            entry.address,
            f"r{dest_reg}",
            f"{self.prefix}{src_val}{self.suffix}",
        )

        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# @formatter:off
class Not(UnaryOperator): prefix = "!"
class TypeOf(UnaryOperator): prefix = "typeof "
class ToNumeric(UnaryOperator): prefix = "+"

class Inc(UnaryOperator): suffix = " + 1"
class Dec(UnaryOperator): suffix = " - 1"
# @formatter:on
