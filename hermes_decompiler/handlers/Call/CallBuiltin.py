from hermes_decompiler.handlers._shared_patterns import REG, UINT8, sequence
from hermes_decompiler.ir import CallExpression, Identifier
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult


# DEFINE_OPCODE_3(CallBuiltin, Reg8, UInt8, UInt8)
# Example: <CallBuiltin>: <Reg8: 3, UInt8: 12, UInt8: 2>
class CallBuiltin(OpcodeHandler):
    _PATTERN = sequence(REG, UINT8, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, builtin_id, arg_count = map(int, match.groups())

        arguments = tuple(
            Identifier(name=f"r{reg}")
            for reg in range(dest_reg - arg_count, dest_reg)
        )

        expression = CallExpression(
            callee=Identifier(name=f"builtin_{builtin_id}"),
            arguments=arguments,
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
