from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.expressions import Identifier, MemberExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_1(ReifyArguments, Reg8)
# Example: <ReifyArguments>: <Reg8: 0>
class ReifyArguments(OpcodeHandler):
    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8 argument")

        dest_reg = int(match.group(1))

        expression = Identifier(name="arguments")

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# DEFINE_OPCODE_1(ReifyArgumentsStrict, Reg8)
# DEFINE_OPCODE_1(ReifyArgumentsLoose, Reg8)
#
# NOT independently confirmed for this specific pair, but following the
# exact same pattern already established elsewhere in this codebase for
# every other strict/loose opcode split (PutById -> PutByIdStrict/
# PutByIdLoose, PutByVal -> PutByValStrict/PutByValLoose, DelByVal ->
# DelByValStrict/DelByValLoose): same Reg8 operand as the unsuffixed
# opcode, with the mode baked into the name rather than an operand.
# The strict/loose distinction affects how the reified `arguments`
# object interacts with mapped parameters at runtime (strict-mode
# `arguments` never maps to named parameters; loose/sloppy-mode
# `arguments` does) -- an ES-spec-level behavioral difference with no
# separate JS *syntax* of its own, so both render identically to
# ReifyArguments: `arguments`.
class ReifyArgumentsStrict(ReifyArguments):
    pass


class ReifyArgumentsLoose(ReifyArguments):
    pass


# DEFINE_OPCODE_2(GetArgumentsLength, Reg8, Reg8)
# Example: <GetArgumentsLength>: <Reg8: 1, Reg8: 0>
class GetArgumentsLength(OpcodeHandler):
    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected two Reg8 arguments")

        dest_reg, _lazy_reg = map(int, match.groups())

        expression = MemberExpression(receiver=Identifier(name="arguments"), member=Identifier(name="length"))

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# DEFINE_OPCODE_3(GetArgumentsPropByVal, Reg8, Reg8, Reg8)
# Example: <GetArgumentsPropByVal>: <Reg8: 2, Reg8: 1, Reg8: 0>
class GetArgumentsPropByVal(OpcodeHandler):
    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, index_reg, _lazy_reg = map(int, match.groups())
        index_value = self.get_register_value(analysis, index_reg)

        # `ComputedMemberExpression` was a separate legacy class for
        # `obj[x]`; the new IR unifies dot/bracket access into one
        # `MemberExpression` via `computed=`.
        expression = MemberExpression(receiver=Identifier(name="arguments"), member=index_value, computed=True)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
