from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.expressions import MemberExpression, Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_1(GetNewTarget, Reg8)   [confirmed, facebook/hermes main BytecodeList.def]
#
#   "Obtain the value of NewTarget from the frame.
#    Arg1 = NewTarget"
#
# Backs the `new.target` meta-property. `new.target` isn't a regular
# identifier or member expression in JS grammar terms, but since this
# codebase doesn't have a dedicated MetaProperty IR node (checked: not
# present in Access.py/Literals.py/Operations.py, the files reviewed so
# far), it's rendered as a MemberExpression on the pseudo-receiver
# `new`, matching how `new.target` actually reads as source text.
class GetNewTarget(OpcodeHandler):
    """Arg1 = new.target"""

    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8 argument")

        dest_reg = int(match.group(1))

        expression = MemberExpression(
            receiver=Identifier(name="new"),
            member=Identifier(name="target"),
            computed=False,
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
