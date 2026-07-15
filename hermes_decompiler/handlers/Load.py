import re
from abc import ABC

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler


# Load a function parameter by index. Starts at 0 with 'this'.
# Arg1 = Arg2 == 0 ? this : arguments[Arg2 - 1];
# DEFINE_OPCODE_2(LoadParam, Reg8, UInt8)
# Example: <LoadParam>: <Reg8: 1, UInt8: 1>
class LoadParam(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'Reg8:\s*(\d+),\s*UInt8:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, param_index = map(int, match.groups())

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"param{param_index}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Load a constant string value by string table index.
# DEFINE_OPCODE_2(LoadConstString, Reg8, UInt16)
# DEFINE_OPCODE_2(LoadConstStringLongIndex, Reg8, UInt32)
# OPERAND_STRING_ID(LoadConstString, 2)
# OPERAND_STRING_ID(LoadConstStringLongIndex, 2)
# Example: <LoadConstString>: <Reg8: 6, string_id: 4098>  # String: 'application/json' (String)
class LoadConstString(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'Reg8:\s*(\d+),\s*string_id:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg = int(match.group(1))
        string_id = match.group(2)

        # Try to resolve the actual string from analysis.stringMap
        const_value = analysis.stringTable.get(string_id, f'str_{string_id}')

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f'"{const_value}"')
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class LoadConstStringLongIndex(LoadConstString): pass


# /// Load common constants.
# DEFINE_OPCODE_1(LoadConstEmpty, Reg8)
# DEFINE_OPCODE_1(LoadConstUndefined, Reg8)
# DEFINE_OPCODE_1(LoadConstNull, Reg8)
# DEFINE_OPCODE_1(LoadConstTrue, Reg8)
# DEFINE_OPCODE_1(LoadConstFalse, Reg8)
# DEFINE_OPCODE_1(LoadConstZero, Reg8)
# Shared logic via Mixin or base method
class LoadConstX(OpcodeHandler, ABC):
    def _handle_const(self, analysis: HermesAnalysis, entry: OpcodeEntry, const_value: str) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'^Reg8:\s*(\d+)$', entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8 argument")

        dest = int(match.group(1))

        variable = JSVariable(handler, entry.address, f'r{dest}', const_value)
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
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'^Reg8:\s*(\d+),\s*UInt8:\s*(\d+)$', entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8 and UInt8 arguments")

        dest_reg, value = map(int, match.groups())
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', str(value))
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class LoadConstInt(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'^Reg8:\s*(\d+),\s*Imm32:\s*(-?\d+)$', entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8 and Imm32 arguments")

        dest_reg, value = map(int, match.groups())
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', str(value))
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

# /// Obtain the raw \c this value and coerce it to an object. Equivalent to:
# /// \code
# ///     LoadParam    Arg1, #0
# ///     CoerceThisNS Arg1, Arg1
# /// \endcode
# DEFINE_OPCODE_1(LoadThisNS, Reg8)
# Example: <LoadThisNS>: <Reg8: 4>
class LoadThisNS(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__
        match = re.match(r'^Reg8:\s*(\d+)$', entry.args.strip())

        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg = int(match.group(1))
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', 'this')
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
