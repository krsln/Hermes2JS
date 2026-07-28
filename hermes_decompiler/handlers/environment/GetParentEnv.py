from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier, NumericLiteral
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# NOTE: `UINT32` is imported here on the assumption it exists as a
# pattern token in hermes_decompiler.handlers, by analogy with UINT8/
# UINT16 (UINT16 is confirmed in use in NewObjectWithBuffer.py). I have
# not actually seen it used anywhere in the files shared so far --
# if the import fails, either the token has a different name or
# CreateTopLevelEnvironment's UInt32 operand needs a different
# handling path (e.g. reusing STRING_ID's width or a raw regex).


# DEFINE_OPCODE_2(GetParentEnvironment, Reg8, UInt8)   [confirmed, hermes-dec table]
#
#   "Get an environment (scope) from N levels up relative to the
#    current function's enclosing environment. 0 retrieves the
#    environment from the closure, 1 retrieves its parent, etc."
#
# Same "no direct JS surface syntax" situation as CreateFunctionEnvironment
# earlier -- purely internal scope-chain traversal that backs closures'
# access to outer-scope `let`/`const` bindings. Modeled the same way:
# a named pseudo-call rather than emitting nothing, consistent with the
# convention already used for CreateThis's createThis() placeholder.
class GetParentEnvironment(OpcodeHandler):
    """Fetch an environment N levels up the *enclosing* scope chain."""

    _PATTERN = sequence(REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, UInt8 arguments")

        dest_reg, levels = map(int, match.groups())

        expression = CallExpression(
            callee=Identifier(name="getParentEnvironment"),
            arguments=(NumericLiteral(value=levels),),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
