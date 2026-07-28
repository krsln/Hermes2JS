from hermes_decompiler.handlers import OpcodeHandler, REG, sequence, UINT8
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_3(CreateThis, Reg8, Reg8, Reg8)
# Example: <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 2>
class CreateThis(OpcodeHandler):
    """Represents `this` object allocation prior to a constructor call."""

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, func, new_target = (int(x) for x in match.groups())

        prototype = self.get_register_value(analysis, func)
        constructor = self.get_register_value(analysis, new_target)

        # `CreateThisExpression` had no JS equivalent and isn't part of
        # the new `ir` package; represented as a named pseudo-call,
        # matching the same convention already used for
        # getEnvironment()/HermesPropertyIterator() elsewhere.
        expression = CallExpression(
            callee=Identifier(name="createThis"),
            arguments=(prototype, constructor),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# DEFINE_OPCODE_3(CreateThisForNew, Reg8, Reg8, UInt8)   [confirmed, hermes-dec table]
#
#   "Allocate an empty, uninitialized object to be used as the `this`
#    parameter in a `new` expression. Some closures are responsible for
#    making their own `this`, so in these cases this instruction will
#    simply return undefined. Arg1 is the destination register. Arg2 is
#    the constructor closure that will be invoked. Arg3 is a cache
#    index used to speed up fetching the new target prototype property."
#
# Newer replacement for CreateThis (which takes an explicit prototype
# register instead of deriving it from the constructor). No independent
# JS expression -- like CreateThis, it's implicit machinery behind a
# `new Ctor(...)` call, so it's modeled the same way (an opaque
# placeholder value that later gets replaced/selected by SelectObject).
class CreateThisForNew(OpcodeHandler):
    """Allocate the uninitialized `this` object ahead of a `new` call."""

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, UInt8 arguments")

        dest_reg, constructor_reg, _cache = map(int, match.groups())

        constructor = self.get_register_value(analysis, constructor_reg)

        expression = Identifier(name="__uninitialized_this__")

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# DEFINE_OPCODE_4(CreateThisForSuper, Reg8, Reg8, Reg8, UInt8)   [confirmed, hermes-dec table]
#
#   "Allocate an empty, uninitialized object to be used as the `this`
#    parameter for the current function when calling `super()`. Arg1 is
#    the destination register. Arg2 is the constructor closure that
#    will be invoked as `super()`. Arg3 is the value of new.target.
#    Arg4 is a cache index used to speed up fetching the new target
#    prototype property."
#
# Same "no JS-visible expression, opaque placeholder" treatment as
# CreateThisForNew -- this is the derived-class-constructor sibling
# (used right before a CallWithNewTarget that implements the actual
# `super(...)` call), carrying an extra explicit new.target register
# that CreateThisForNew derives implicitly instead.
class CreateThisForSuper(OpcodeHandler):
    """Allocate the uninitialized `this` object ahead of a `super(...)` call."""

    _PATTERN = sequence(REG, REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected Reg8, Reg8, Reg8, UInt8 arguments"
            )

        dest_reg, constructor_reg, new_target_reg, _cache = map(int, match.groups())

        constructor = self.get_register_value(analysis, constructor_reg)
        new_target = self.get_register_value(analysis, new_target_reg)

        expression = Identifier(name="__uninitialized_this__")

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
