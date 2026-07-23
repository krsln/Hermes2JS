from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult

from hermes_decompiler.handlers._shared_patterns import REG, sequence


# DEFINE_OPCODE_3(CreateThis, Reg8, Reg8, Reg8)
# Example: <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 2>
class CreateThis(OpcodeHandler):
    """Represents `this` object allocation prior to a constructor call."""

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        dest, func, new_target = (int(x) for x in match.groups())

        func_name = self.get_register_value(analysis, func) or f"r{func}"
        new_target_name = self.get_register_value(analysis, new_target) or f"r{new_target}"

        variable = JSVariable(
            handler, entry.address,
            f'r{dest}', f"createThis(prototype={func_name}, constructor={new_target_name})",
        )

        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
