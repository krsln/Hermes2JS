import re
from typing import Dict

from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


class CallX(OpcodeHandler):
    # One pattern per arity: dest + closure + N argument registers.
    _PATTERN: Dict[int, "re.Pattern[str]"] = {
        n: sequence(*([REG] * (n + 2))) for n in (1, 2, 3, 4)
    }

    num_args = 1  # to be overridden

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        reg_pattern = self._PATTERN.get(self.num_args)
        if not reg_pattern:
            return self.build_invalid_args_result(analysis, entry)

        match = re.match(reg_pattern, entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, func_reg, *arg_regs = (int(x) for x in match.groups())
        callee = self.get_register_value(analysis, func_reg)
        arguments = tuple(
            self.get_register_value(analysis, reg)
            for reg in arg_regs
        )

        expression = CallExpression(callee=callee, arguments=arguments)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# DEFINE_OPCODE_3(Call, Reg8, Reg8, UInt8)
# Example: <Call>: <Reg8: 4, Reg8: 9, UInt8: 6>
class Call(CallX):
    """
    Runtime argument count variant.

    Hermes layout:

        [arg1][arg2]...[argN][callee]

    Example:

        Call r4, r9, 6

    means

        r4 = r9(r3, r4, r5, r6, r7, r8)
    """

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, func_reg, num_args = map(int, match.groups())

        callee = self.get_register_value(analysis, func_reg)
        arg_regs = list(range(func_reg - num_args, func_reg))  # Arguments in reverse order

        # NOTE: kept as bare register references (not resolved via
        # get_register_value), same as the original - the argument slots
        # here are a contiguous stack range that doesn't necessarily
        # correspond to individually tracked register assignments.
        arguments = tuple(
            Identifier(name=f"r{r}")
            for r in arg_regs
        )

        expression = CallExpression(callee=callee, arguments=arguments)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# @formatter:off
class Call1(CallX): num_args = 1
class Call2(CallX): num_args = 2
class Call3(CallX): num_args = 3
class Call4(CallX): num_args = 4
# @formatter:on