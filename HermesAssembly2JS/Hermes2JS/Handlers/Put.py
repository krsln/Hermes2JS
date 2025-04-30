import json
import re

from Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from Hermes2JS.Models.OpcodeResult import OpcodeResult
from Hermes2JS.Models.JSVariable import JSVariable
from Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from Hermes2JS.Models.OpcodeHandler import OpcodeHandler

# /// Create a new own property on an object. This is similar to PutById, but
# /// the destination must be an object, it only deals with own properties,
# /// ignoring the prototype chain, and the property must not already be defined.
# /// Similarly to PutById, the property name cannot be a valid array index.
# /// Arg1 is the destination object, which is known to be an object.
# /// Arg2 is the value to write.
# /// Arg3 is the string table ID of the property name.
# /// Arg1[stringTable[Arg3]] = Arg2
# DEFINE_OPCODE_3(PutNewOwnByIdShort, Reg8, Reg8, UInt8)
# DEFINE_OPCODE_3(PutNewOwnById, Reg8, Reg8, UInt16)
# DEFINE_OPCODE_3(PutNewOwnByIdLong, Reg8, Reg8, UInt32)
# OPERAND_STRING_ID(PutNewOwnByIdShort, 3)
# OPERAND_STRING_ID(PutNewOwnById, 3)
# OPERAND_STRING_ID(PutNewOwnByIdLong, 3)
# Example: <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 6, string_id: 158>  # String: 'method' (Identifier)
class PutNewOwnByIdShort(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Parse arguments: Reg8 (dest), Reg8 (value), string_id
        match = re.match(r'Reg8:\s*(\d+),\s*Reg8:\s*(\d+),\s*string_id:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(entry)

        dest_reg = int(match.group(1))
        value_reg = int(match.group(2))
        string_id = int(match.group(3))

        # Extract property name from comment (e.g., String: 'method')
        prop_name = None
        comment_match = re.search(r"String:\s*'([^']+)'\s*\(Identifier\)", entry.comment)
        if comment_match:
            prop_name = comment_match.group(1)
        else:
            # Fallback to string table lookup
            try:
                prop_name = analysis.stringTable.get(str(string_id))
            except (AttributeError, KeyError):
                prop_name = f'string_{string_id}'  # Fallback if lookup fails

        # Retrieve the destination object from the analysis context
        dest_var = self.GetVariableByReg(analysis.results, dest_reg)

        if not dest_var or not dest_var.value:
            return OpcodeResult(entry, JSVariable(handler, entry.address, f'r{dest_reg}',
                                                 f'// Error: No valid object found in r{dest_reg}'))

        # Retrieve the value from the analysis context
        value_var = self.GetVariableByReg(analysis.results, value_reg)
        value = value_var.value if value_var and value_var.value else 'undefined'

        # Parse the destination object’s value as a JSON-like object
        try:
            obj = json.loads(dest_var.value.replace("'", '"')) if dest_var.value != '{}' else {}
        except json.JSONDecodeError:
            return OpcodeResult(entry, JSVariable(handler, entry.address, f'r{dest_reg}',
                                                 f'// Error: Invalid object format in r{dest_reg}: {dest_var.value}'))

        # Add the new property
        obj[prop_name] = value
        # print(obj.items())

        # Convert back to a JSON-like string
        js_obj = "{ " + ", ".join(f'"{k}": "{v}"' for k, v in obj.items()) + " }"
        js_obj = "{ " + ", ".join(f'"{k}": {v}' for k, v in obj.items()) + " }"

        # Update the JSVariable for the destination object
        updated_var = JSVariable(handler, entry.address, f'r{dest_reg}', js_obj)
        analysis.AddResult(entry, updated_var)

        return OpcodeResult(entry, updated_var)