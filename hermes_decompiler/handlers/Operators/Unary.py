from typing import ClassVar

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


class UnaryOperator(OpcodeHandler):
    """Base class for unary register operations."""

    _PATTERN: ClassVar = sequence(REG, REG)

    def expression(self, value: str) -> str:
        """
        Return the JavaScript expression for the unary operation.
        Subclasses should override this method.
        """
        return value

    def Handle(
            self,
            analysis: HermesAnalysis,
            entry: OpcodeEntry,
    ) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(
                analysis,
                entry,
                "Expected two Reg8 arguments",
            )

        dest_reg, src_reg = map(int, match.groups())

        src_val = (
                self.GetValueByReg(analysis.results, src_reg)
                or f"r{src_reg}"
        )

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", self.expression(src_val), )

        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class Not(UnaryOperator):
    def expression(self, value: str) -> str:
        return f"!{value}"


class TypeOf(UnaryOperator):
    def expression(self, value: str) -> str:
        return f"typeof {value}"


class ToInt32(UnaryOperator):
    def expression(self, value: str) -> str:
        return f"({value} | 0)"


class ToNumeric(UnaryOperator):
    def expression(self, value: str) -> str:
        return f"+{value}"


class ToNumber(UnaryOperator):
    """
    Arg1 = ToNumber(Arg2). Emitted as unary `+`, the same representation
    already used for ToNumeric above. The two opcodes differ in real JS
    semantics (ToNumber rejects BigInt with a TypeError; ToNumeric passes
    BigInt through unchanged) — but `+value` is actually the *spec-accurate*
    source-level operator for ToNumber specifically (unary `+` in real JS
    calls ToNumber, and does throw on BigInt), whereas reusing it for
    ToNumeric is the looser approximation of the two. Both are kept as the
    same textual form here for readability; if BigInt-precision matters for
    your use case, ToNumeric should be distinguished (e.g. wrapped in a
    `/* numeric */` comment) rather than sharing this class.
    """

    def expression(self, value: str) -> str:
        return f"+{value}"


class Inc(UnaryOperator):
    def expression(self, value: str) -> str:
        return f"{value} + 1"


class Dec(UnaryOperator):
    def expression(self, value: str) -> str:
        return f"{value} - 1"


class Negate(UnaryOperator):
    """Arg1 = -Arg2 (unary minus)."""

    def expression(self, value: str) -> str:
        return f"-{value}"


class AddEmptyString(UnaryOperator):
    """Forces a ToString coercion via string concatenation — the idiomatic
    cheap alternative to a full ToString/ToPrimitive call."""

    def expression(self, value: str) -> str:
        return f'"" + {value}'
