import re
from typing import Dict

from hermes_decompiler.ir.Expressions import CallExpression
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, sequence


class CallX(OpcodeHandler):
    # One pattern per arity: dest + closure + N argument registers.
    _PATTERN: Dict[int, "re.Pattern[str]"] = {
        n: sequence(*([REG] * (n + 2))) for n in (1, 2, 3, 4)
    }

    num_args = 1  # to be overridden

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        reg_pattern = self._PATTERN.get(self.num_args)
        if not reg_pattern:
            return self.build_invalid_args_result(analysis, entry)

        match = re.match(reg_pattern, entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, func_reg, *arg_regs = (int(x) for x in match.groups())
        callee = self.get_register_value_new(analysis, func_reg)
        arguments = [
            self.get_register_value_new(analysis, reg)
            for reg in arg_regs
        ]

        value = CallExpression(callee=callee, arguments=arguments)
        variable = JSVariable(handler, entry.address, f"r{dest_reg}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# DEFINE_OPCODE_3(Call, Reg8, Reg8, UInt8)
# Example: <Call>: <Reg8: 4, Reg8: 9, UInt8: 6>
class Call(CallX):
    """The same semantics as CallX but with a runtime-determined argument count
    (UInt8) instead of a fixed arity."""
    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, func_reg, num_args = map(int, match.groups())
        func_name = self.get_register_value_new(analysis, func_reg)

        arg_regs = list(range(func_reg - num_args, func_reg))  # Arguments in reverse order
        arg_list = [f"r{r}" for r in arg_regs]
        args_str = ", ".join(arg_list)

        value = f"{func_name}({args_str})"
        # value = CallExpression(callee=func_name, arguments=arg_list)

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# @formatter:off
class Call1(CallX): num_args = 1
class Call2(CallX): num_args = 2
class Call3(CallX): num_args = 3
class Call4(CallX): num_args = 4
# @formatter:on
