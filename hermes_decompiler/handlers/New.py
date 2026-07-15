import json
import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler


# Create an object from a static map of values, as for var={'a': 3}.
# Any non-constant elements can be set afterwards with PutOwnByInd.
# Arg1 is the destination.
# Arg2 is a preallocation size hint.
# Arg3 is the number of static elements.
# Arg4 is the index in the object key buffer table.
# Arg5 is the index in the object val buffer table.
# DEFINE_OPCODE_5(NewObjectWithBuffer, Reg8, UInt16, UInt16, UInt16, UInt16)
# Example: < NewObjectWithBuffer >: < Reg8: 2, UInt16: 2, UInt16: 2, UInt16: 4743, UInt16: 24182 >  # Object: {'message': 'You have joined the list', 'type': 'success'}
class NewObjectWithBuffer(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(
            r'Reg8:\s*(\d+),\s*UInt16:\s*\d+,\s*UInt16:\s*\d+,\s*UInt16:\s*\d+,\s*UInt16:\s*\d+',
            entry.args.strip()
        )

        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg = int(match.group(1))

        # Extract all Object: {...} comments
        object_matches = re.findall(r"Object:\s*(\{[^}]+})", entry.comment)
        parsed_obj = {}

        for obj_str in object_matches:
            try:
                # Convert single quotes to double quotes and remove trailing commas
                clean_str = obj_str.replace("'", '"').rstrip(",")
                parsed = json.loads(clean_str)
                parsed_obj = parsed
                break  # take the first valid parsed object
            except json.JSONDecodeError:
                print(f"Failed to parse: {obj_str}")

        if not parsed_obj:
            error = f'// Warning: No valid object parsed from comment: {entry.comment}'
            return self.Exception(analysis, entry, error)

        js_obj = "{ " + ", ".join(f'{k}: "{v}"' for k, v in parsed_obj.items()) + " }"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{js_obj}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# DEFINE_OPCODE_5(NewObjectWithBufferLong, Reg8, UInt16, UInt16, UInt32, UInt32)
class NewObjectWithBufferLong(NewObjectWithBuffer):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return super().Handle(analysis, entry)


# Create a new, empty Object using the built-in constructor (regardless of
# whether it was overridden).
# Arg1 = {}
# DEFINE_OPCODE_1(NewObject, Reg8)
# Example: <NewObject>: <Reg8: 3>
class NewObject(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Parse the Reg8 argument (e.g., "Reg8: 3")
        match = re.match(r'Reg8:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg = int(match.group(1))

        # Create an empty JavaScript object
        js_obj = "{}"

        # Create a JSVariable for the new object
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_obj)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
