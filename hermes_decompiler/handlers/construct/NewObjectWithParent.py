from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.expressions import (
    CallExpression,
    Identifier,
    MemberExpression,
)
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(NewObjectWithParent, Reg8, Reg8)
# Example: <NewObjectWithParent>: <Reg8: 1, Reg8: 14>
class NewObjectWithParent(OpcodeHandler):
    """Create a new object with the specified prototype."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, parent_reg = map(int, match.groups())

        parent = self.get_register_expression(analysis, parent_reg)

        expression = CallExpression(
            callee=MemberExpression(
                Identifier(name="Object"),
                Identifier(name="create"),
            ),
            arguments=(parent,),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
