from hermes_decompiler.handlers import OpcodeHandler, REG, UINT32, sequence
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# NOTE: `UINT32` is imported here on the assumption it exists as a
# pattern token in hermes_decompiler.handlers, by analogy with UINT8/
# UINT16 (UINT16 is confirmed in use in NewObjectWithBuffer.py). I have
# not actually seen it used anywhere in the files shared so far --
# if the import fails, either the token has a different name or
# CreateTopLevelEnvironment's UInt32 operand needs a different
# handling path (e.g. reusing STRING_ID's width or a raw regex).


# DEFINE_OPCODE_2(CreateTopLevelEnvironment, Reg8, UInt32)   [confirmed, hermes-dec table]
#
#   "Create a top level environment, without a parent. TODO: Consider
#    removing this in favor of using CreateEnvironment by using a
#    different scheme for encoding the top level environment. Arg1 is
#    the destination. Arg2 is the size of the new environment."
#
# Same treatment as CreateFunctionEnvironment/CreateEnvironment: opaque
# scope allocation, no JS-visible expression of its own.
class CreateTopLevelEnvironment(OpcodeHandler):
    """Allocate the parentless module/global-level environment record."""

    _PATTERN = sequence(REG, UINT32)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, UInt32 arguments")

        dest_reg, _size = map(int, match.groups())

        expression = Identifier(name="__environment__")

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
