from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.ir.statements import ThrowStatement
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult, ControlFlowType
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_1(Throw, Reg8)
# Example: <Throw>: <Reg8: 2>
class Throw(OpcodeHandler):
    """Throw an exception."""

    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        value_reg = int(match.group(1))

        expression = self.get_register_value(analysis, value_reg)
        statement = ThrowStatement(argument=expression)
        flow = ControlFlowType.THROW

        result = OpcodeResult(entry, value=expression, statement=statement, dest_reg=None, control_flow=flow)
        analysis.add_result(result)

        return result


# ThrowIfThisInitialized -- ***SIGNATURE NOT CONFIRMED***
#
# Not found in either source consulted. Inferred from its name and JS
# semantics: derived class constructors must call `super()` before
# touching `this`, and calling `super()` a second time (or touching
# `this` before the first `super()` call completes) is a runtime error
# ("must call super constructor... before accessing 'this'" /
# "super constructor may only be called once"). This opcode is
# presumably the compiler-inserted guard for that check, emitted right
# before/around a `super()` call site or a `this` access.
#
# Guessed shape: Reg8 (the `this` slot being checked) -- no destination
# register, since like Throw this is a control-flow guard, not a value-
# producing instruction. It only actually throws if the check fails;
# on success it's effectively a no-op at the JS-source level (the
# language-level guarantee it enforces is invisible in valid,
# non-buggy compiled output), so unlike Throw there's no unconditional
# ThrowStatement here -- it's rendered as an inert marker/no-op rather
# than a guaranteed throw.
#
# VERIFY: operand count (could plausibly be 0-arg if it always checks
# an implicit fixed `this` slot rather than an explicit register) and
# whether your disassembler actually surfaces this opcode with an
# operand at all before trusting the REG pattern below.
class ThrowIfThisInitialized(OpcodeHandler):
    """Guard: throws if `this` was already initialized (double `super()` call)."""

    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8 argument")

        this_reg = int(match.group(1))

        this_value = self.get_register_value(analysis, this_reg)

        # No JS-visible expression on the success path; modeled as an
        # inert pseudo-call so it's still traceable in output rather
        # than silently discarded, consistent with the
        # getParentEnvironment()-style convention used for other
        # no-surface-syntax opcodes.
        expression = CallExpression(
            callee=Identifier(name="__throwIfThisInitialized__"),
            arguments=(this_value,),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result
