import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, STRING_ID, sequence


# /// Get a property by value. Constant string values should instead use GetById.
# /// Arg1 = Arg2[Arg3]
# DEFINE_OPCODE_3(GetByVal, Reg8, Reg8, Reg8)
# Example: <GetByVal>: <Reg8: 3, Reg8: 7, Reg8: 0>
class GetByVal(OpcodeHandler):
    """Get property by dynamic value: obj[key]"""
    _PATTERN = sequence(REG, REG, REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8, Reg8, Reg8 arguments")

        dest_reg, base_reg, prop_reg = map(int, match.groups())

        value = f"r{base_reg}[r{prop_reg}]"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', value)
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
    """Get property by string ID: obj[propName]"""
    _PATTERN = sequence(REG, REG, UINT8, STRING_ID)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, obj_reg, _cache, string_id = map(int, match.groups())

        # Resolve property name
        prop_name = self._get_property_name(analysis, entry, string_id)
        if not prop_name:
            error = f'/* Error: string_id {string_id} not found in stringTable */'
            return self.Exception(analysis, entry, error)

        # Get base object value
        base_value = self.GetValueByReg(analysis, obj_reg)

        # Build property access
        js_expr = f"{base_value}.{prop_name}"

        variable = JSVariable(
            handler,
            entry.address,
            f'r{dest_reg}',
            js_expr,
            base_value,
            f".{prop_name}"
        )
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    def _get_property_name(self, analysis: HermesAnalysis, entry: OpcodeEntry, string_id: int) -> str:
        """Resolve the property name from a string table or comment."""
        # Try the string table first
        prop_name = analysis.stringTable.get(str(string_id))
        if prop_name:
            return prop_name

        # Fallback: try to extract from comment
        comment_match = re.search(r"String:\s*'([^']+)'\s*\(Identifier\)", entry.comment or "")
        if comment_match:
            return comment_match.group(1)

        return f'str_{string_id}'


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
# Example: <TryGetById>: <Reg8: 14, Reg8: 13, UInt8: 8, string_id: 23>  # String: 'Math' (Identifier)
class TryGetById(GetById):
    """TryGetById - similar to GetById, often used with global-object."""
    pass


class TryGetByIdLong(TryGetById):
    pass
