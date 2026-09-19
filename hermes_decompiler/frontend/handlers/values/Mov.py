from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.frontend.opcode import OpcodeResult


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

        # Carry env_source forward (see OpcodeResult's own docstring) -
        # a private-field/class-reference opcode several Movs downstream
        # from the GetEnvironment/GetParentEnvironment/LoadFromEnvironment
        # that actually set it still needs to trace back to it (see
        # CreateThis.py's own Mov of a placeholder for the same reasoning
        # applied to a different kind of value).
        src_state = ctx.analysis.get_register_state(src_reg)
        env_source = src_state.definition.env_source if src_state is not None else None

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg, env_source=env_source)
        ctx.analysis.add_result(result)

        return result


# Reg32, Reg32 (total size 8)
# DEFINE_OPCODE_2(MovLong, Reg32, Reg32)
# Example:
class MovLong(Mov):
    pass
