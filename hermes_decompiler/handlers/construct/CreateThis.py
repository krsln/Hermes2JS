from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG, UINT8
from hermes_decompiler.ir.expressions import CallExpression, Identifier


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(CreateThis, Reg8, Reg8, Reg8)
# Example: <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 2>
class CreateThis(OpcodeHandler):
    """Represents `this` object allocation prior to a constructor call."""

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry, "Expected three Reg8 arguments")

        dest_reg, func, new_target = (int(x) for x in match.groups())

        prototype = self.get_register_expression(ctx.analysis, func)
        constructor = self.get_register_expression(ctx.analysis, new_target)

        # `CreateThisExpression` had no JS equivalent and isn't part of
        # the new `ir` package; represented as a named pseudo-call,
        # matching the same convention already used for
        # getEnvironment()/HermesPropertyIterator() elsewhere.
        expression = CallExpression(
            callee=Identifier(name="createThis"),
            arguments=(prototype, constructor),
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(CreateThisForNew, Reg8, Reg8, UInt8)
# Example: <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
class CreateThisForNew(OpcodeHandler):
    """Allocate the uninitialized `this` object ahead of a `new` call."""

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry, "Expected Reg8, Reg8, UInt8 arguments")

        dest_reg, constructor_reg, _cache = map(int, match.groups())

        constructor = self.get_register_expression(ctx.analysis, constructor_reg)

        expression = Identifier(name="__uninitialized_this_for_new__")

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8, UInt8 (total size 4)
# DEFINE_OPCODE_4(CreateThisForSuper, Reg8, Reg8, Reg8, UInt8)
# Example: <CreateThis>: <CreateThisForSuper>: <Reg8: 4, Reg8: 2, Reg8: 1, UInt8: 0>
class CreateThisForSuper(OpcodeHandler):
    """Allocate the uninitialized `this` object ahead of a `super(...)` call."""

    _PATTERN = sequence(REG, REG, REG, UINT8)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                ctx.analysis, ctx.entry, "Expected Reg8, Reg8, Reg8, UInt8 arguments"
            )

        dest_reg, constructor_reg, new_target_reg, _cache = map(int, match.groups())

        constructor = self.get_register_expression(ctx.analysis, constructor_reg)
        new_target = self.get_register_expression(ctx.analysis, new_target_reg)

        expression = Identifier(name="__uninitialized_this_for_super__")

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
