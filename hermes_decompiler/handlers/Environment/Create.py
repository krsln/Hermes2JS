from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


class CreateEnvironment(OpcodeHandler):
    """
    Allocate a new lexical environment.

    Hermes uses environment objects to store variables
    captured by nested closures.
    """

    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg = int(match.group(1))

        expression = CallExpression(callee=Identifier(name="createEnvironment"), arguments=())

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
