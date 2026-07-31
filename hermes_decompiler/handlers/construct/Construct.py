from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, UINT32, sequence
from hermes_decompiler.ir.expressions import Expression, Identifier, NewExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(Construct, Reg8, Reg8, UInt8)
# Example: <Construct>: <Reg8: 2, Reg8: 4, UInt8: 2>
class Construct(OpcodeHandler):
    """
    Construct using UInt8 argument count.

    TODO
    """

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, ArgCount")

        dest_reg, func_reg, arg_count = map(int, match.groups())

        constructor = self.get_register_value(analysis, func_reg)
        arguments = self.resolve_arguments(analysis, func_reg, arg_count)

        # `ir.NewExpression` names this field `callee` (not `constructor`),
        # matching CallExpression's naming for consistency.
        expression = NewExpression(callee=constructor, arguments=arguments)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result

    def resolve_arguments(self, analysis: HermesAnalysis, func_reg: int, arg_count: int) -> tuple[Expression, ...]:
        values = [
            self.get_register_value(analysis, reg)
            for reg in range(func_reg - arg_count, func_reg)
        ]

        # Hermes CreateThis inserts an implicit "this" as the first
        # constructor argument slot; `ThisValue` no longer exists as a
        # distinct type (see decision on RegisterValue/ThisValue ->
        # Identifier), so the check becomes a name comparison.
        if values and isinstance(values[0], Identifier) and values[0].name == "this":
            values = values[1:]

        return tuple(values)


# Reg8, Reg8, UInt32 (total size 6)
# DEFINE_OPCODE_3(ConstructLong, Reg8, Reg8, UInt32)
class ConstructLong(Construct):
    """
    Construct using UInt32 argument count.
    """

    _PATTERN = sequence(REG, REG, UINT32)
