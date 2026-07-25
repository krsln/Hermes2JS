from hermes_decompiler.handlers._shared_patterns import (
    REG,
    UINT8,
    UINT16,
    sequence,
)
from hermes_decompiler.ir import AssignmentExpression, MemberExpression, NumericLiteral
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult


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


class StoreToEnvironmentL(StoreToEnvironment):
    _PATTERN = sequence(REG, UINT16, REG)


class StoreNPToEnvironment(StoreToEnvironment):
    """
    Non-pointer variant.

    Semantically identical during decompilation.
    """

    pass


class StoreNPToEnvironmentL(StoreToEnvironmentL):
    """
    Long non-pointer variant.
    """

    pass