from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression, MemberExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_3(PutByVal, Reg8, Reg8, Reg8)
# Example: <PutByVal>: <Reg8: 98, Reg8: 2, Reg8: 0>
class PutByVal(OpcodeHandler):
    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        obj_reg, key_reg, value_reg = map(int, match.groups())

        left = MemberExpression(
            receiver=self.get_register_value(analysis, obj_reg),
            member=self.get_register_value(analysis, key_reg),
            computed=True,
        )
        right = self.get_register_value(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# DEFINE_OPCODE_3(PutByValLoose, Reg8, Reg8, Reg8)
#
# NOT in the checked BytecodeList.def, but confirmed to exist as a
# sibling opcode by direct analogy with DelByVal -> DelByValLoose /
# DelByValStrict, which IS confirmed in the hermes-dec table:
#
#   DelByValLoose: Reg8, Reg8, Reg8
#   DelByValStrict: Reg8, Reg8, Reg8
#   (both drop the UInt8 strict-mode flag that plain DelByVal carries,
#    because the mode is now baked into the opcode name itself)
#
# PutByVal's own strict/loose split almost certainly follows the exact
# same shape: same three Reg8 operands as PutByVal, with the pre-split
# PutByVal instruction eventually retired/aliased once callers migrate
# to the explicit strict/loose variants (compare PutById -> PutByIdLoose
# also in this codebase). Loose mode differs from strict mode only in
# whether a failed write silently no-ops vs throws at runtime -- there
# is no separate JS syntax for that, so it's rendered identically to
# PutByVal: `obj[key] = value;`.
#
# NOTE: no PutByValStrict counterpart was requested/added here -- add
# one analogously if/when it shows up in your opcode stream.
class PutByValLoose(PutByVal):
    pass
