import re
from abc import ABC

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, sequence


# /// Load common constants.
# DEFINE_OPCODE_1(LoadConstEmpty, Reg8)
# DEFINE_OPCODE_1(LoadConstUndefined, Reg8)
# DEFINE_OPCODE_1(LoadConstNull, Reg8)
# DEFINE_OPCODE_1(LoadConstTrue, Reg8)
# DEFINE_OPCODE_1(LoadConstFalse, Reg8)
# DEFINE_OPCODE_1(LoadConstZero, Reg8)
# Shared logic via Mixin or base method
class LoadConstX(OpcodeHandler, ABC):
    """Base class for simple constant loaders."""
    _PATTERN = sequence(REG)

    def _handle_const(self, analysis: HermesAnalysis, entry: OpcodeEntry, const_value: str) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8 argument")

        dest_reg = int(match.group(1))

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', const_value)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# Example: <LoadConstZero>: <Reg8: 0>
class LoadConstZero(LoadConstX):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return self._handle_const(analysis, entry, "0")


class LoadConstUndefined(LoadConstX):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return self._handle_const(analysis, entry, "undefined")


class LoadConstNull(LoadConstX):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return self._handle_const(analysis, entry, "null")


# Example: <LoadConstTrue>: <Reg8: 3>
class LoadConstTrue(LoadConstX):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return self._handle_const(analysis, entry, "true")


class LoadConstFalse(LoadConstX):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return self._handle_const(analysis, entry, "false")


class LoadConstEmpty(LoadConstX):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return self._handle_const(analysis, entry, "empty")


# /// Load a constant integer value.
# DEFINE_OPCODE_2(LoadConstUInt8, Reg8, UInt8)
# DEFINE_OPCODE_2(LoadConstInt, Reg8, Imm32)
# Example: <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
class LoadConstUInt8(OpcodeHandler):
    """Load a small unsigned integer constant."""
    _PATTERN = sequence(REG, UINT8)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, value = map(int, match.groups())

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', str(value))
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class LoadConstInt(OpcodeHandler):
    """Load integer constant (Imm32)."""
    _PATTERN = re.compile(r'^Reg8:\s*(\d+),\s*Imm32:\s*(-?\d+)$')

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8 and Imm32 arguments")

        dest_reg, value = map(int, match.groups())

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', str(value))
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Load a constant string value by string table index.
# DEFINE_OPCODE_2(LoadConstString, Reg8, UInt16)
# DEFINE_OPCODE_2(LoadConstStringLongIndex, Reg8, UInt32)
# OPERAND_STRING_ID(LoadConstString, 2)
# OPERAND_STRING_ID(LoadConstStringLongIndex, 2)
# Example: <LoadConstString>: <Reg8: 6, string_id: 4098>  # String: 'application/json' (String)
class LoadConstString(OpcodeHandler):
    """Load constant string from the string table."""
    _PATTERN = sequence(REG, r'string_id:\s*(\d+)')

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, string_id = match.groups()

        # Resolve string from table
        const_value = analysis.stringTable.get(string_id, f'str_{string_id}')

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f'"{const_value}"')
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class LoadConstStringLongIndex(LoadConstString):
    """Long index variant."""
    pass


class LoadConstDouble(OpcodeHandler):
    """Load a floating-point constant."""

    _PATTERN = re.compile(
        r"^Reg8:\s*(\d+),\s*Double:\s*(-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)$"
    )

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
                "Expected Reg8 and Double arguments",
            )

        dest_reg = int(match.group(1))
        value = match.group(2)

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", value, )
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
