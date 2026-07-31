from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, UINT16, sequence
from hermes_decompiler.ir.expressions import MemberExpression, NumericLiteral
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(LoadFromEnvironment, Reg8, Reg8, UInt8)
# Example: <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 19>
class LoadFromEnvironment(OpcodeHandler):
    """
    Load a value from a lexical environment.

        dst = env[slot]
    """

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, env_reg, slot = map(int, match.groups())
        env = self.get_register_expression(analysis, env_reg)

        expression = MemberExpression(receiver=env, member=NumericLiteral(slot), computed=True)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8, Reg8, UInt16 (total size 4)
# DEFINE_OPCODE_3(LoadFromEnvironmentL, Reg8, Reg8, UInt16)
# Example: <LoadFromEnvironmentL>: <Reg8: 7, Reg8: 5, UInt16: 269>
class LoadFromEnvironmentL(LoadFromEnvironment):
    _PATTERN = sequence(REG, REG, UINT16)
