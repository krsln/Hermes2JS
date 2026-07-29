from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier, NumericLiteral
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(GetEnvironment, Reg8, Reg8, UInt8)
# Example: <GetEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 1>
class GetEnvironment(OpcodeHandler):
    """
    Resolve an environment from the lexical scope chain.

    level = 0  -> current environment
    level = 1  -> parent environment
    level = 2  -> grandparent
    ...
    """

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, level = map(int, match.groups())

        expression = CallExpression(
            callee=Identifier(name="getEnvironment"),
            arguments=(NumericLiteral(level),),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
