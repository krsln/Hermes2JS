from hermes_decompiler.analysis.terminators import TerminatorThrow
from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.ir.statements import ThrowStatement
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8 (total size 1)
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

        expression = self.get_register_expression(analysis, value_reg)
        terminator = TerminatorThrow(value=expression)

        # NOTE (fix): same reasoning as Ret.py - `Throw` terminators are
        # never consumed by a structurer, so without an explicit
        # `statement` attached here the `throw ...;` line silently
        # disappears from the output (this is what was happening in the
        # generated `catch` blocks).
        statement = ThrowStatement(argument=expression)

        result = OpcodeResult(
            entry, value=expression, statement=statement, terminator=terminator, dest_reg=None
        )
        analysis.add_result(result)

        return result


from hermes_decompiler.handlers import OpcodeHandler, REG, UINT32, sequence
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(ThrowIfEmpty, Reg8, Reg8)
# Example:
class ThrowIfEmpty(OpcodeHandler):
    """
    Throw if the first register contains Hermes' internal Empty value.

    TODO:
        Requires runtime semantics. This opcode is conditional and
        should eventually emit a conditional terminator rather than a
        plain ThrowStatement.
    """

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis,
                entry,
                "Expected Reg8, Reg8 arguments",
            )

        # value_reg = int(match.group(1))
        # error_reg = int(match.group(2))

        return self.build_exception_result(
            analysis,
            entry,
            "// TODO: ThrowIfEmpty is not implemented",
        )


# UInt32 (string_id) (total size 4)
# DEFINE_OPCODE_1(ThrowIfHasRestrictedGlobalProperty, UInt32)
# Example:
class ThrowIfHasRestrictedGlobalProperty(OpcodeHandler):
    """
    Throw if a restricted global property exists.

    TODO:
        Exact runtime semantics need verification.
    """

    _PATTERN = sequence(UINT32)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis,
                entry,
                "Expected UInt32 argument",
            )

        # string_id = int(match.group(1))

        return self.build_exception_result(
            analysis,
            entry,
            "// TODO: ThrowIfHasRestrictedGlobalProperty is not implemented",
        )


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(ThrowIfUndefined, Reg8, Reg8)
# Example:
class ThrowIfUndefined(OpcodeHandler):
    """
    Throw if the first register contains undefined.

    TODO:
        Conditional runtime check.
    """

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis,
                entry,
                "Expected Reg8, Reg8 arguments",
            )

        # value_reg = int(match.group(1))
        # error_reg = int(match.group(2))

        return self.build_exception_result(
            analysis,
            entry,
            "// TODO: ThrowIfUndefined is not implemented",
        )


# Reg8 (total size 1)
# DEFINE_OPCODE_1(ThrowIfUndefinedInst, Reg8)
# Example:
class ThrowIfUndefinedInst(OpcodeHandler):
    """
    Throw if the given register contains an undefined instance.

    TODO:
        Exact runtime semantics need verification.
    """

    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis,
                entry,
                "Expected Reg8 argument",
            )

        # value_reg = int(match.group(1))

        return self.build_exception_result(
            analysis,
            entry,
            "// TODO: ThrowIfUndefinedInst is not implemented",
        )


# Reg8 (total size 1)
# DEFINE_OPCODE_1(ThrowIfThisInitialized, Reg8)
# Example:
class ThrowIfThisInitialized(OpcodeHandler):
    """
    Throw if 'this' has already been initialized.

    Used by class constructor initialization checks.

    TODO:
        Conditional runtime check.
    """

    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis,
                entry,
                "Expected Reg8 argument",
            )

        this_reg = int(match.group(1))

        this_value = self.get_register_expression(analysis, this_reg)

        # No JS-visible expression on the success path; modeled as an
        # inert pseudo-call so it's still traceable in output rather
        # than silently discarded, consistent with the
        # getParentEnvironment()-style convention used for other
        # no-surface-syntax opcodes.
        expression = CallExpression(
            callee=Identifier(name="__throwIfThisInitialized__"),
            arguments=(this_value,),
        )
        # // TODO: ThrowIfThisInitialized is not implemented

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result
