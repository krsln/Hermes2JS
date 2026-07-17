from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, STRING_ID, sequence
from .PutById import PutById

# Patterns
PUT_BY_ID_PATTERN = sequence(REG, REG, UINT8, STRING_ID)
PUT_NEW_OWN_PATTERN = sequence(REG, REG, STRING_ID)
PUT_GETTER_SETTER_PATTERN = sequence(REG, REG, REG, REG, UINT8)


# DEFINE_OPCODE_3(PutNewOwnByIdShort, Reg8, Reg8, UInt8)
# DEFINE_OPCODE_3(PutNewOwnById, Reg8, Reg8, UInt16)
# DEFINE_OPCODE_3(PutNewOwnByIdLong, Reg8, Reg8, UInt32)
# Example: <PutNewOwnById>: <Reg8: 4, Reg8: 5, string_id: 8626>  # String: 'Authorization' (Identifier)
# Example: <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 6, string_id: 158>  # String: 'method' (Identifier)
class PutNewOwnByIdX(OpcodeHandler):
    """Base class for PutNewOwnById* variants."""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = PUT_NEW_OWN_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, value_reg, string_id = map(int, match.groups())

        prop_name = PutById._extract_property_name(self, analysis, entry, string_id)
        value = PutById._get_register_value(self, analysis, value_reg)

        obj = PutById._parse_existing_object(self, analysis, dest_reg)
        obj[prop_name] = value

        js_obj = PutById._format_object_literal(obj)

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_obj)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class PutNewOwnByIdShort(PutNewOwnByIdX): pass


class PutNewOwnById(PutNewOwnByIdX): pass


class PutNewOwnByIdLong(PutNewOwnByIdX): pass
