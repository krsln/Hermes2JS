import dataclasses

from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(Mov, Reg8, Reg8)
# Example: <Mov>: <Reg8: 1, Reg8: 6>
class Mov(OpcodeHandler):
    """Move value between registers: rX = rY"""

    ARGUMENTS = ArgsPattern(sequence(REG, REG), "Reg8, Reg8 (total size 2)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, src_reg = map(int, match.groups())

        expression = self.get_register_expression(ctx.analysis, src_reg)
        # `expression` is the SAME object currently backing src_reg's
        # own definition (get_register_expression returns the live
        # shared node, not a copy - see its docstring). Storing it
        # unchanged as dest_reg's value would make dest_reg and
        # src_reg's definitions alias the same Expression identity
        # from this point on, so any later fold (e.g.
        # BooleanChainFolder._repoint_references, which matches by
        # `is`, not structural equality) targeting one register's
        # read would silently also rewrite the other, unrelated
        # register's value. A Mov is a NEW definition - give it a
        # distinct top-level identity via a shallow copy so the two
        # registers' definitions can be independently repointed from
        # here on, while still sharing the same nested structure.
        # expression = dataclasses.replace(expression)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg32, Reg32 (total size 8)
# DEFINE_OPCODE_2(MovLong, Reg32, Reg32)
# Example:
class MovLong(Mov):
    pass
