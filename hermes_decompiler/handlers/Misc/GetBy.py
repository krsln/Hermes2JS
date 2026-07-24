from hermes_decompiler.ir.Expressions import IndexExpression, MemberExpression
from hermes_decompiler.ir.Values import IdentifierValue
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, STRING_ID, sequence


# DEFINE_OPCODE_3(GetByVal, Reg8, Reg8, Reg8)
# Example: <GetByVal>: <Reg8: 3, Reg8: 7, Reg8: 0>
class GetByVal(OpcodeHandler):
    """Get property by dynamic value: obj[key]"""
    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, Reg8 arguments")

        dest_reg, base_reg, prop_reg = map(int, match.groups())

        # value = f"r{base_reg}[r{prop_reg}]"
        value_object = self.get_register_value(analysis, base_reg)
        value_index = self.get_register_value(analysis, prop_reg)
        value = IndexExpression(object=value_object, index=value_index)

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# DEFINE_OPCODE_4(GetByIdShort, Reg8, Reg8, UInt8, UInt8)
# DEFINE_OPCODE_4(GetById, Reg8, Reg8, UInt8, UInt16)
# DEFINE_OPCODE_4(GetByIdLong, Reg8, Reg8, UInt8, UInt32)
# Example: <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 158>  # String: 'prototype' (Identifier)
# Example: <GetById>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 21914>  # String: 'trackJoinCompetitionList' (Identifier)
class GetById(OpcodeHandler):
    """Get property by string ID: obj[propName]"""
    _PATTERN = sequence(REG, REG, UINT8, STRING_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, obj_reg, _cache, string_id = map(int, match.groups())

        prop_name = entry.identifier_name or f"string_{string_id}"
        value_object = self.get_register_value(analysis, obj_reg)
        # function_base = str(value_object)

        # Build property access
        # value = f"{base_value}.{prop_name}"
        value = MemberExpression(object=value_object, property=IdentifierValue(prop_name))

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class GetByIdShort(GetById):
    pass


class GetByIdLong(GetById):
    pass


# /// This is similar to GetById, but intended for use with global variables
# /// where Arg2 = GetGlobalObject.
# DEFINE_OPCODE_4(TryGetById, Reg8, Reg8, UInt8, UInt16)
# DEFINE_OPCODE_4(TryGetByIdLong, Reg8, Reg8, UInt8, UInt32)
# OPERAND_STRING_ID(TryGetById, 4)
# OPERAND_STRING_ID(TryGetByIdLong, 4)
# Example: <TryGetById>: <Reg8: 14, Reg8: 13, UInt8: 8, string_id: 23> # String: 'Math' (Identifier)
class TryGetById(GetById):
    """TryGetById - similar to GetById, often used with global-object."""
    pass


class TryGetByIdLong(TryGetById):
    pass
