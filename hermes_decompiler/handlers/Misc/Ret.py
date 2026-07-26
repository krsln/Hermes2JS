from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.statements import ReturnStatement
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult, ControlFlowType
from hermes_decompiler.runtime import HermesAnalysis


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
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        value_reg = int(match.group(1))

        expression = self.get_register_value(analysis, value_reg)
        statement = ReturnStatement(argument=expression)
        flow = ControlFlowType.RETURN

        result = OpcodeResult(entry, value=expression, statement=statement, dest_reg=None, control_flow=flow)
        analysis.add_result(result)

        return result
