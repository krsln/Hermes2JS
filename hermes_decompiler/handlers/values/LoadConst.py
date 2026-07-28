import re
from typing import ClassVar

from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence, STRING_ID
from hermes_decompiler.ir.expressions import (
    Expression,
    UndefinedLiteral,
    StringLiteral,
    RawExpression,
    python_literal,
)
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# ---------------------------------------------------------------------------
# Simple constants
# ---------------------------------------------------------------------------

class LoadSimpleConst(OpcodeHandler):
    """
    Base class for simple constant loaders.

        Reg8
    """

    _PATTERN = sequence(REG)

    VALUE: ClassVar[Expression | object]

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8 argument")

        dest_reg = int(match.group(1))

        value = self.VALUE

        if not isinstance(value, Expression):
            value = python_literal(value)

        result = OpcodeResult(entry, value=value, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# @formatter:off
class LoadConstZero(LoadSimpleConst):
    VALUE = 0

class LoadConstTrue(LoadSimpleConst):
    VALUE = True

class LoadConstFalse(LoadSimpleConst):
    VALUE = False

class LoadConstNull(LoadSimpleConst):
    VALUE = None

class LoadConstUndefined(LoadSimpleConst):
    VALUE = UndefinedLiteral()

class LoadConstEmpty(LoadSimpleConst):
    # Hermes' internal "empty" sentinel (e.g. an array hole) has no real
    # JS literal - it isn't `undefined` at the engine level, even though
    # source-visible reads of it usually coerce to `undefined`. Kept as
    # an explicit marker rather than silently lying with UndefinedLiteral.
    VALUE = RawExpression(source="/* empty */")
# @formatter:on


# ---------------------------------------------------------------------------
# Numeric constants
# ---------------------------------------------------------------------------

class LoadConstUInt8(OpcodeHandler):
    _PATTERN = sequence(REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, UInt8")

        dest_reg = int(match.group(1))
        value = python_literal(int(match.group(2)))

        result = OpcodeResult(entry, value=value, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


class LoadConstInt(OpcodeHandler):
    _PATTERN = re.compile(r"^Reg8:\s*(\d+),\s*Imm32:\s*(-?\d+)$")

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Imm32")

        dest_reg = int(match.group(1))
        value = python_literal(int(match.group(2)))

        result = OpcodeResult(entry, value=value, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


class LoadConstDouble(OpcodeHandler):
    _PATTERN = re.compile(r"^Reg8:\s*(\d+),\s*Double:\s*(-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)$")

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Double")

        dest_reg = int(match.group(1))
        value = python_literal(float(match.group(2)))

        result = OpcodeResult(entry, value=value, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# ---------------------------------------------------------------------------
# String constants
# ---------------------------------------------------------------------------

class LoadConstString(OpcodeHandler):
    _PATTERN = sequence(REG, STRING_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, string_id")

        dest_reg = int(match.group(1))
        string_id = match.group(2)

        resolved = entry.string_literal

        if resolved is None:
            resolved = entry.identifier_name

        if resolved is None:
            resolved = f"str_{string_id}"

        result = OpcodeResult(entry, value=StringLiteral(resolved), dest_reg=dest_reg)
        analysis.add_result(result)

        return result


class LoadConstStringLongIndex(LoadConstString):
    """
    UInt32 string index variant.
    """

    pass
