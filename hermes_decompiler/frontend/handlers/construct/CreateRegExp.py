import re

from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern
from hermes_decompiler.frontend.opcode import OpcodeResult
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

        # The disassembler's comment text backslash-escapes the pattern
        # for its own display (a real `\d` in the regex source shows up
        # as `\\d` in the comment, e.g. `# String: '^\\d+$' (String)`
        # for the true pattern `^\d+$`). resolve_pattern_and_flags()
        # returns that comment text verbatim, so undo that one level of
        # escaping here - otherwise every backslash in the pattern is
        # doubled in the emitted regex literal, silently changing its
        # meaning (`\d` becomes a literal backslash followed by `d`).
        pattern = pattern.replace("\\\\", "\\")

        # expression = f"/{pattern}/{flags or ''}"
        expression = RegExpLiteral(pattern=pattern, flags=flags or "")

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
