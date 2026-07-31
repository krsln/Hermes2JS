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

    def resolve_arguments(
            self, analysis: HermesAnalysis, func_reg: int, arg_count: int
    ) -> tuple[Expression, ...]:
        if arg_count <= 0:
            return ()

        # Henüz kullanılmamış register sonuçlarını topla
        # (Construct'tan hemen önceki LoadConst / Mov / CreateThis vb.)
        unused: dict[int, Expression] = {}
        for item in analysis.results:
            if not getattr(item, "used", True) and item.dest_reg is not None:
                unused[item.dest_reg] = item.value

        if not unused:
            # fallback: eski davranış (nadiren gerekir)
            regs = range(func_reg - arg_count, func_reg)
            values = [self.get_register_value(analysis, r) for r in regs]
        else:
            # Frame'in sonu = en yüksek unused register
            end_reg = max(unused.keys())  # örnekte 5
            start_reg = end_reg - arg_count + 1  # örnekte 4

            # reverse order: yüksek → düşük (this önce)
            values = [
                unused.get(reg) or self.get_register_value(analysis, reg)
                for reg in range(end_reg, start_reg - 1, -1)
            ]
            # values = [r5=this, r4="test"]

            # Bu register'ları artık kullandık diye işaretle
            for reg in range(start_reg, end_reg + 1):
                for item in analysis.results:
                    if item.dest_reg == reg:
                        item.used = True

        # Construct'ta ilk slot her zaman CreateThis / this
        if values and self._is_this_value(values[0]):
            values = values[1:]

        return tuple(values)

    def _is_this_value(self, expr: Expression) -> bool:
        if isinstance(expr, Identifier) and expr.name == "this":
            return True
        # CreateThis'i CallExpression(callee=Identifier("createThis"), ...) olarak üretiyorsan:
        if (
                isinstance(expr, CallExpression)
                and isinstance(expr.callee, Identifier)
                and expr.callee.name == "createThis"
        ):
            return True
        return False


# Reg8, Reg8, UInt32 (total size 6)
# DEFINE_OPCODE_3(ConstructLong, Reg8, Reg8, UInt32)
class ConstructLong(Construct):
    """
    Construct using UInt32 argument count.
    """

    _PATTERN = sequence(REG, REG, UINT32)
