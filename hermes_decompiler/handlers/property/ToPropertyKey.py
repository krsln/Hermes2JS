from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(ToPropertyKey, Reg8, Reg8)
# Example: <ToPropertyKey>: <Reg8: 6, Reg8: 6>
class ToPropertyKey(OpcodeHandler):
    """Arg1 = ToPropertyKey(Arg2) -- coerce a value to a valid property key."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8 arguments")

        dest_reg, value_reg = map(int, match.groups())

        # No-op passthrough at the JS-source level: `obj[key]` already
        # implies ToPropertyKey coercion, so there's nothing additional
        # to render -- just forward the source value to the destination.
        value = self.get_register_value(analysis, value_reg)

        result = OpcodeResult(entry, value=value, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
