from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, UINT32, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt32, UInt8 (total size 7)
# DEFINE_OPCODE_4(CacheNewObject, Reg8, Reg8, UInt32, UInt8)
# Example: <CacheNewObject>: <Reg8: 4, Reg8: 5, UInt32: 2297, UInt8: 0>
class CacheNewObject(OpcodeHandler):
    """Runtime hint: look up/cache the hidden-class shape for a `this`/new.target pair. No JS-visible effect."""

    _PATTERN = sequence(REG, REG, UINT32, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected Reg8, Reg8, UInt32, UInt8 arguments"
            )

        this_reg, new_target_reg, _shape_idx, _cache_idx = map(int, match.groups())

        this_value = self.get_register_expression(analysis, this_reg)
        new_target = self.get_register_expression(analysis, new_target_reg)

        expression = CallExpression(
            callee=Identifier(name="__cacheNewObject__"),
            arguments=(this_value, new_target),
        )

        # No destination register -- this opcode doesn't produce a value.
        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result
