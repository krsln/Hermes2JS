from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, STRING_ID, sequence

# Patterns
PUT_BY_ID_PATTERN = sequence(REG, REG, UINT8, STRING_ID)
PUT_NEW_OWN_PATTERN = sequence(REG, REG, STRING_ID)
PUT_GETTER_SETTER_PATTERN = sequence(REG, REG, REG, REG, UINT8)


class PutOwnGetterSetterByVal(OpcodeHandler):
    """Define getter/setter property."""

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = PUT_GETTER_SETTER_PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected 4 Reg + UInt8")

        obj_reg, key_reg, getter_reg, setter_reg, enumerable_flag = map(int, match.groups())

        obj_val = self.get_register_value(analysis, obj_reg) or f"r{obj_reg}"
        key_val = self.get_register_value(analysis, key_reg) or f"r{key_reg}"
        getter_val = self.get_register_value(analysis, getter_reg)
        setter_val = self.get_register_value(analysis, setter_reg)
        enumerable = "true" if enumerable_flag else "false"

        descriptor_parts = []
        if getter_val is not None:
            descriptor_parts.append(f"get: {getter_val}")
        if setter_val is not None:
            descriptor_parts.append(f"set: {setter_val}")
        descriptor_parts.append(f"enumerable: {enumerable}")
        descriptor_parts.append("configurable: true")

        descriptor = "{ " + ", ".join(descriptor_parts) + " }"
        value = f"Object.defineProperty({obj_val}, {key_val}, {descriptor})"

        variable = JSVariable(handler, entry.address, f'r{obj_reg}', value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
