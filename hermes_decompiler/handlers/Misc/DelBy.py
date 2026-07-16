import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, STRING_ID, sequence

_IDENTIFIER_COMMENT_PATTERN = re.compile(r"String:\s*'([^']+)'\s*\(Identifier\)")


# /// Delete an object property by string index.
# /// Arg1 = delete Arg2[stringtable[Arg4]]
# /// Arg3 is a cache index used to speed up the above operation (unused
# /// here — decompilation only needs the resolved property name).
# DEFINE_OPCODE_4(DelById, Reg8, Reg8, UInt8, UInt16)
# OPERAND_STRING_ID(DelById, 4)
# Example: <DelById>: <Reg8: 2, Reg8: 1, UInt8: 0, string_id: 158>  # String: 'cache' (Identifier)
class DelById(OpcodeHandler):
    _PATTERN = sequence(REG, REG, UINT8, STRING_ID)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8, Reg8, UInt8, string_id arguments")

        dest_reg, obj_reg, _cache, string_id = map(int, match.groups())

        prop_name = self._resolve_property_name(analysis, entry, string_id)
        if prop_name is None:
            error = f'/* Error: string_id {string_id} not found in stringTable */ undefined'
            return self.Exception(analysis, entry, error)

        obj_val = self.GetValueByReg(analysis, obj_reg)

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"delete {obj_val}.{prop_name}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    @staticmethod
    def _resolve_property_name(analysis: HermesAnalysis, entry: OpcodeEntry, string_id: int):
        comment_match = _IDENTIFIER_COMMENT_PATTERN.search(entry.comment or "")
        if comment_match:
            return comment_match.group(1)
        string_table = getattr(analysis, "stringTable", None)
        if string_table is None:
            return None
        return string_table.get(str(string_id))


# /// Arg1 = delete Arg2[Arg3].
# DEFINE_OPCODE_3(DelByVal, Reg8, Reg8, Reg8)
# Example: <DelByVal>: <Reg8: 2, Reg8: 0, Reg8: 1>
class DelByVal(OpcodeHandler):
    """delete obj[prop]"""
    _PATTERN = sequence(REG, REG, REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, obj_reg, prop_reg = map(int, match.groups())

        obj_val = self.GetValueByReg(analysis, obj_reg)
        prop_val = self.GetValueByReg(analysis, prop_reg)

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"delete {obj_val}[{prop_val}]")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
