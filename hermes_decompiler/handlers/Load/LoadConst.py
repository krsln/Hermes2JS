import re
from typing import ClassVar

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, sequence
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
    CONSTANT: ClassVar[str]

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8 argument")

        register = int(match.group(1))

        variable = JSVariable(handler, entry.address, f"r{register}", self.CONSTANT)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# @formatter:off
class LoadConstZero(LoadSimpleConst): CONSTANT = "0"
class LoadConstUndefined(LoadSimpleConst): CONSTANT = "undefined"
class LoadConstNull(LoadSimpleConst): CONSTANT = "null"
class LoadConstTrue(LoadSimpleConst): CONSTANT = "true"
class LoadConstFalse(LoadSimpleConst): CONSTANT = "false"
class LoadConstEmpty(LoadSimpleConst): CONSTANT = "empty"
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
        value = match.group(2)

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
        value = match.group(2)

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
        value = match.group(2)

        variable = JSVariable(handler, entry.address, f"r{register}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# ---------------------------------------------------------------------------
# String constants
# ---------------------------------------------------------------------------

class LoadConstString(OpcodeHandler):
    _PATTERN = sequence(REG, r"string_id:\s*(\d+)")

    @staticmethod
    def ResolveString(analysis: HermesAnalysis, string_id: str) -> str:
        return analysis.stringTable.get(string_id, f"str_{string_id}")

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, string_id")

        register = int(match.group(1))
        string_id = match.group(2)

        value = f'"{self.ResolveString(analysis, string_id)}"'

        variable = JSVariable(handler, entry.address, f"r{register}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class LoadConstStringLongIndex(LoadConstString):
    """
    UInt32 string index variant.
    """
    pass
