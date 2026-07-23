from hermes_decompiler.ir.Expressions import IndexExpression, CallExpression
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


class LoadFromEnvironment(OpcodeHandler):
    """
    Load a value from a lexical environment.

        dst = env[slot]
    """

    _PATTERN = sequence(REG, REG, UINT8, )

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, env_reg, slot = map(int, match.groups())
        reg_value = self.get_register_value(analysis, env_reg)

        value = f"{reg_value}[{slot}]"
        # value = IndexExpression(CallExpression(reg_value,), ConstantValue(slot))

        variable = JSVariable(self.__class__.__name__, entry.address, f"r{dest_reg}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class LoadFromEnvironmentL(LoadFromEnvironment):
    _PATTERN = sequence(REG, REG, UINT16)
