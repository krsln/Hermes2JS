from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, UINT32, sequence
from hermes_decompiler.ir.expressions import Expression, Identifier, NewExpression, CallExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(Construct, Reg8, Reg8, UInt8)
# Example: <Construct>: <Reg8: 2, Reg8: 4, UInt8: 2>
class Construct(OpcodeHandler):
    """
    Construct using UInt8 argument count.
    """

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, ArgCount")

        dest_reg, ctor_reg, arg_count = map(int, match.groups())

        constructor = self.get_register_expression(analysis, ctor_reg)
        arguments: list[OpcodeResult] = []

        for result in reversed(analysis.results):
            if result.used:
                continue
            if result.dest_reg is None:
                continue
            if result.opcode.address >= entry.address:
                continue

            arguments.append(result)

            if len(arguments) == arg_count:
                break

        # Register frame order
        arguments.sort(key=lambda r: r.dest_reg)

        # Son register CreateThis ise kaldır
        if arguments and self._is_this_value(arguments[-1].value):
            arguments.pop()

        # Kullanıldı olarak işaretle
        for arg in arguments:
            arg.used = True

        values = tuple(arg.value for arg in arguments)
        expression = NewExpression(callee=constructor, arguments=values)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result

    @staticmethod
    def _is_this_value(expr: Expression) -> bool:
        """
        Return True if the expression represents the synthetic CreateThis value
        produced by the Hermes CreateThis opcode.
        """

        return (
                isinstance(expr, CallExpression)
                and isinstance(expr.callee, Identifier)
                and expr.callee.name == "createThis"
        )


# Reg8, Reg8, UInt32 (total size 6)
# DEFINE_OPCODE_3(ConstructLong, Reg8, Reg8, UInt32)
class ConstructLong(Construct):
    """
    Construct using UInt32 argument count.
    """

    _PATTERN = sequence(REG, REG, UINT32)
