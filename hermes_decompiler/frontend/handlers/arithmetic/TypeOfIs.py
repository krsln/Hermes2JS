from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT16
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.frontend.handlers.shared import build_typeof_condition


# Reg8, Reg8, UInt16 (total size 4)
# DEFINE_OPCODE_3(TypeOfIs, Reg8, Reg8, UInt16)
# Example: <TypeOfIs>: <Reg8: 1, Reg8: 4, UInt16: 258>
class TypeOfIs(OpcodeHandler):
    """
    Arg1 = typeof Arg2 is one of the types encoded in the Arg3 bitmask.

    The bit-to-type mapping is the measured one in
    `shared/_typeof_mask.py` (shared with `JmpTypeOfIs`).
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT16), "Reg8, Reg8, UInt16")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, value_reg, type_mask = map(int, match.groups())

        operand = self.get_register_expression(ctx.analysis, value_reg)
        expression = build_typeof_condition(operand, type_mask)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
