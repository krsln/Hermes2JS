from hermes_decompiler.handlers._shared_patterns import (
    REG,
    UINT8,
    UINT16,
    sequence,
)
from hermes_decompiler.ir import MemberExpression, NumericLiteral
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult


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
        env = self.get_register_value(analysis, env_reg)

        expression = MemberExpression(receiver=env, member=NumericLiteral(slot), computed=True)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


class LoadFromEnvironmentL(LoadFromEnvironment):
    _PATTERN = sequence(REG, REG, UINT16)
