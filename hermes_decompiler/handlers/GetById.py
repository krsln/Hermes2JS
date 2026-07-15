import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

arg_regex = r'Reg8:\s*(\d+),\s*Reg8:\s*(\d+),\s*UInt8:\s*(\d+),\s*string_id:\s*(\d+)'


# /// Get a property by value. Constants string values should instead use GetById.
# /// Arg1 = Arg2[Arg3]
# DEFINE_OPCODE_3(GetByVal, Reg8, Reg8, Reg8)
# Example: <GetByVal>: <Reg8: 3, Reg8: 7, Reg8: 0>
class GetByVal(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'^Reg8:\s*(\d+),\s*Reg8:\s*(\d+),\s*Reg8:\s*(\d+)$', entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8, Reg8, Reg8 arguments")

        dest, base, prop = map(int, match.groups())

        value = f"r{base}[r{prop}]"
        variable = JSVariable(handler, entry.address, f'r{dest}', value)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Get an object property by string table index.
# /// Arg1 = Arg2[stringtable[Arg4]]
# /// Arg3 is a cache index used to speed up the above operation.
# DEFINE_OPCODE_4(GetByIdShort, Reg8, Reg8, UInt8, UInt8)
# DEFINE_OPCODE_4(GetById, Reg8, Reg8, UInt8, UInt16)
# DEFINE_OPCODE_4(GetByIdLong, Reg8, Reg8, UInt8, UInt32)
# OPERAND_STRING_ID(GetByIdShort, 4)
# OPERAND_STRING_ID(GetById, 4)
# OPERAND_STRING_ID(GetByIdLong, 4)
# Example: <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 158>  # String: 'prototype' (Identifier)
# Example: <GetById>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 21914>  # String: 'trackJoinCompetitionList' (Identifier)
class GetById(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        arg_match = re.match(arg_regex, entry.args.strip())

        if not arg_match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, obj_reg, _cache, string_id = map(int, arg_match.groups())
        prop_name = analysis.stringTable.get(str(string_id))

        if not prop_name:
            error = f'/* Error: string_id {string_id} not found in stringTable'
            return self.Exception(analysis, entry, error)

        func_name = self.GetValueByReg(analysis.results, obj_reg)
        # obj_var = 'this' if analysis.globalObjects is not None and obj_reg == analysis.globalObjects else func_name

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{func_name}.{prop_name}",
                              f"{func_name}", f".{prop_name}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class GetByIdShort(GetById): pass


class GetByIdLong(GetById): pass


# /// This is similar to GetById, but intended for use with global variables
# /// where Arg2 = GetGlobalObject.
# DEFINE_OPCODE_4(TryGetById, Reg8, Reg8, UInt8, UInt16)
# DEFINE_OPCODE_4(TryGetByIdLong, Reg8, Reg8, UInt8, UInt32)
# OPERAND_STRING_ID(TryGetById, 4)
# OPERAND_STRING_ID(TryGetByIdLong, 4)
# Example: <TryGetById>: <Reg8: 14, Reg8: 13, UInt8: 8, string_id: 23>  # String: 'Math' (Identifier)
class TryGetById(GetById):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return super().Handle(analysis, entry)


class TryGetByIdLong(TryGetById): pass
