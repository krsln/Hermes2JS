from hermes_decompiler.ir.Expressions import IndexExpression, AssignmentExpression
from hermes_decompiler.ir.Values import ConstantValue
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult

from hermes_decompiler.handlers._shared_patterns import (
    REG,
    UINT8,
    UINT16,
    sequence,
)


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

        # expression = f"{env}[{slot}] = {value};"
        left = IndexExpression(object=env, index=ConstantValue(slot))
        expression = AssignmentExpression(left=left, operator="=", right=value)

        variable = JSVariable(self.__class__.__name__, entry.address, "", expression)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class StoreToEnvironmentL(StoreToEnvironment):
    _PATTERN = sequence(REG, UINT16, REG, )


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
