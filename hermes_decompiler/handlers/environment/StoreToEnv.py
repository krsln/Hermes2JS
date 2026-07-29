from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, UINT16, sequence
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression, MemberExpression, NumericLiteral
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, UInt8, Reg8 (total size 3)
# DEFINE_OPCODE_3(StoreToEnvironment, Reg8, UInt8, Reg8)
# Example: <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 4>
class StoreToEnvironment(OpcodeHandler):
    """
    Store a value into a lexical environment.

        env[slot] = value
    """

    _PATTERN = sequence(REG, UINT8, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        env_reg, slot, value_reg = map(int, match.groups())
        env = self.get_register_value(analysis, env_reg)
        value = self.get_register_value(analysis, value_reg)

        left = MemberExpression(receiver=env, member=NumericLiteral(slot), computed=True)
        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=value)

        # No destination register (name=""): OpcodeResult/JSRenderer
        # already render a name-less Expression as a bare statement
        # (`env[17] = r5;`), so no extra ExpressionStatement wrapper
        # is needed here.
        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, UInt16, Reg8 (total size 4)
# DEFINE_OPCODE_3(StoreToEnvironmentL, Reg8, UInt16, Reg8)
# Example: <StoreToEnvironmentL>: <Reg8: 5, UInt16: 385, Reg8: 4>
class StoreToEnvironmentL(StoreToEnvironment):
    _PATTERN = sequence(REG, UINT16, REG)


# Reg8, UInt8, Reg8 (total size 3)
# DEFINE_OPCODE_3(StoreNPToEnvironment, Reg8, UInt8, Reg8)
# Example: <StoreNPToEnvironment>: <Reg8: 3, UInt8: 13, Reg8: 0>
class StoreNPToEnvironment(StoreToEnvironment):
    """
    Non-pointer variant.

    Semantically identical during decompilation.
    """

    pass


# Reg8, UInt16, Reg8 (total size 4)
# DEFINE_OPCODE_3(StoreNPToEnvironmentL, Reg8, UInt16, Reg8)
# Example: <StoreNPToEnvironmentL>: <Reg8: 0, UInt16: 264, Reg8: 11>
class StoreNPToEnvironmentL(StoreToEnvironmentL):
    """
    Long non-pointer variant.
    """
    _PATTERN = sequence(REG, UINT16, REG)

    pass
