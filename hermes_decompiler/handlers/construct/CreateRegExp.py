import re

from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern
from hermes_decompiler.ir.expressions import RegExpLiteral


# Reg8, UInt32 (string_id), UInt32 (string_id), UInt32 (total size 13)
# DEFINE_OPCODE_4(CreateRegExp, Reg8, UInt32, UInt32, UInt32)
# Example: <CreateRegExp>: <Reg8: 0, UInt32: 12, UInt32: 13, UInt32: 0>  # String: '^\d+$'  String: 'g'
class CreateRegExp(OpcodeHandler):
    """Create a RegExp literal."""

    ARGUMENTS = ArgsPattern(
        re.compile(
            r'^Reg\d+:\s*(\d+),\s*(?:string_id|UInt32):\s*(\d+),\s*(?:string_id|UInt32):\s*(\d+),\s*(?:UInt32|Reg\d+):\s*(\d+)$'
        ), "Reg8, UInt32, UInt32, UInt32"
    )

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, pattern_id, flags_id, _ = map(int, match.groups())

        pattern, flags = ctx.entry.resolve_pattern_and_flags()

        if pattern is None:
            error = f'/* Error: could not resolve RegExp pattern (id {pattern_id}) */'
            return self.build_exception_result(ctx.analysis, ctx.entry, error)

        # expression = f"/{pattern}/{flags or ''}"
        expression = RegExpLiteral(pattern=pattern, flags=flags or "")

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
