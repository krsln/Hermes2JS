from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8, UINT16
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import Identifier, MemberExpression, NumericLiteral


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(LoadFromEnvironment, Reg8, Reg8, UInt8)
# Example: <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 19>
class LoadFromEnvironment(OpcodeHandler):
    """
    Load a value from a lexical environment.

        dst = env[slot]

    When `env`'s own depth is known (it was itself produced by
    GetEnvironment/GetParentEnvironment, or by a chain of Movs tracing
    back to one - see OpcodeResult.env_source) and this function's own id
    is known, ClassEnvironmentTable gets one eager attempt at resolving
    (this function, depth, slot) to a real class name (`Animal`, `Dog`,
    ...) - if it succeeds, that becomes the value here directly instead
    of the raw `env[slot]`, so every later use of this register (a `new`
    call, an instanceof check, ...) already sees the resolved name
    through the ordinary register-inlining every other opcode already
    gets, with no further wiring needed downstream.

    A private field's *symbol* has no such standalone printable form
    (see AddOwnPrivateBySym.py/PrivateProperty.py) - it only means
    anything as the `#fieldName` a later AddOwnPrivateBySym/
    GetOwnPrivateBySym/PutOwnPrivateBySym turns it into - so unlike the
    class case, this only carries `env_source=(depth, slot)` forward
    (through any Mov - see Mov.py) rather than trying to resolve
    PrivateNameTable eagerly here; that opcode is where the actual lookup
    happens.
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT8), "Reg8, Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, env_reg, slot = map(int, match.groups())

        env = self.get_register_expression(ctx.analysis, env_reg)

        env_state = ctx.analysis.get_register_state(env_reg)
        depth = env_state.definition.env_source[0] if env_state and env_state.definition.env_source else None

        class_name = None
        if depth is not None and ctx.function_id is not None and ctx.batch_tables is not None:
            class_name = ctx.batch_tables.class_environment_table.name_for(ctx.function_id, depth, slot)

        if class_name is not None:
            expression = Identifier(name=class_name)
            env_source = None
        else:
            expression = MemberExpression(obj=env, prop=NumericLiteral(slot), computed=True)
            env_source = (depth, slot) if depth is not None else None

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg, env_source=env_source)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt16 (total size 4)
# DEFINE_OPCODE_3(LoadFromEnvironmentL, Reg8, Reg8, UInt16)
# Example: <LoadFromEnvironmentL>: <Reg8: 7, Reg8: 5, UInt16: 269>
class LoadFromEnvironmentL(LoadFromEnvironment):
    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT16), "Reg8, Reg8, UInt16")
