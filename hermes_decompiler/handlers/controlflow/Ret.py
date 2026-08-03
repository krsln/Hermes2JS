from hermes_decompiler.analysis.terminators import TerminatorReturn
from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.statements import ReturnStatement
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8 (total size 1)
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

        expression = self.get_register_expression(analysis, value_reg)
        terminator = TerminatorReturn(value=expression)

        # NOTE (fix): a `Return` terminator is never "consumed" by any
        # structurer (only `ConditionalBranch` is, when folded into an
        # if/while condition) - so unless this opcode also carries its
        # own renderable `statement`, the `return` disappears from the
        # output entirely once it reaches the printer. Building the
        # `ReturnStatement` right here, at the source of truth for what
        # value is being returned, is the most robust place: it can't
        # get skipped by a structural-analysis pass forgetting about it.
        statement = ReturnStatement(argument=expression)

        result = OpcodeResult(
            entry, value=expression, statement=statement, terminator=terminator, dest_reg=None
        )
        analysis.add_result(result)

        return result
