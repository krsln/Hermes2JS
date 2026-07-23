import re
from typing import ClassVar

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, sequence
from hermes_decompiler.ir.Values import Value, UndefinedValue, EmptyValue, ConstantValue
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult


# ---------------------------------------------------------------------------
# Simple constants
# ---------------------------------------------------------------------------

class LoadSimpleConst(OpcodeHandler):
    """
    Base class for simple constant loaders.

        Reg8
    """

    _PATTERN = sequence(REG)

    VALUE: ClassVar[Value | object]

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8 argument")

        register = int(match.group(1))

        value = self.VALUE

        if not isinstance(value, Value):
            value = ConstantValue(value)

        variable = JSVariable(handler, entry.address, f"r{register}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


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
    VALUE = UndefinedValue()

class LoadConstEmpty(LoadSimpleConst):
    VALUE = EmptyValue()
# @formatter:on

# ---------------------------------------------------------------------------
# Numeric constants
# ---------------------------------------------------------------------------

class LoadConstUInt8(OpcodeHandler):
    _PATTERN = sequence(REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, UInt8")

        register = int(match.group(1))
        value = ConstantValue(int(match.group(2)))

        variable = JSVariable(handler, entry.address, f"r{register}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class LoadConstInt(OpcodeHandler):
    _PATTERN = re.compile(r"^Reg8:\s*(\d+),\s*Imm32:\s*(-?\d+)$")

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Imm32")

        register = int(match.group(1))
        value = ConstantValue(int(match.group(2)))

        variable = JSVariable(handler, entry.address, f"r{register}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class LoadConstDouble(OpcodeHandler):
    _PATTERN = re.compile(r"^Reg8:\s*(\d+),\s*Double:\s*(-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)$")

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Double")

        register = int(match.group(1))
        value = ConstantValue(float(match.group(2)))

        variable = JSVariable(handler, entry.address, f"r{register}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# ---------------------------------------------------------------------------
# String constants
# ---------------------------------------------------------------------------

class LoadConstString(OpcodeHandler):
    _PATTERN = sequence(REG, r"string_id:\s*(\d+)")

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, string_id")

        register = int(match.group(1))
        string_id = match.group(2)

        resolved = entry.string_literal

        if resolved is None:
            resolved = entry.identifier_name

        if resolved is None:
            resolved = f"str_{string_id}"

        variable = JSVariable(handler, entry.address, f"r{register}", ConstantValue(resolved))
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class LoadConstStringLongIndex(LoadConstString):
    """
    UInt32 string index variant.
    """
    pass
