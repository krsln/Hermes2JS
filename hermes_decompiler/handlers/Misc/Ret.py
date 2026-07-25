from hermes_decompiler.ir import ReturnStatement
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult, ControlFlowType
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


# DEFINE_OPCODE_1(Ret, Reg8)
# Example: <Ret>: <Reg8: 0>
class Ret(OpcodeHandler):
    """
    Return from the current function.

    NOTE (fix): this file previously contained a stray copy of
    `Throw.py` - a `class Throw` (not `Ret`), which meant no handler was
    ever registered for the `Ret` opcode at all (`OpcodeHandler.
    __init_subclass__` keys the registry by class name). Every function
    body was ending with an unhandled `Ret`, and the file's duplicate
    `Throw` class was silently overwriting the real one from Misc/Throw.py
    in the registry, depending on import order.
    """

    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        value_reg = int(match.group(1))
        value = self.get_register_value(analysis, value_reg)

        variable = JSVariable(
            handler,
            entry.address,
            "",
            value,
            statement=ReturnStatement(argument=value),
        )
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable, control_flow=ControlFlowType.RETURN)
