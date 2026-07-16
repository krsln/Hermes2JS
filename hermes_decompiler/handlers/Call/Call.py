import re
from typing import Dict

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

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Get precompiled regex for the number of arguments
        reg_pattern = self._PATTERN.get(self.num_args)
        if not reg_pattern:
            return self.InvalidArgs(analysis, entry)

        match = re.match(reg_pattern, entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, func_reg, *arg_regs = (int(x) for x in match.groups())

        func_variable = self.GetVariableByReg(analysis, func_reg)
        func_name = self.GetValueByReg(analysis, func_reg)

        argList = self.GetFuncArgs(analysis, arg_regs)

        # Special handling for HermesInternal.concat
        if func_name == "this.HermesInternal.concat":
            # Skip the first argument if it's an empty string
            checked_args = [arg for arg in argList if arg != '""']
            # Build a template literal
            template_parts = []
            for arg in checked_args:
                # If the argument is a string literal, strip quotes for template literal
                if arg.startswith('"') and arg.endswith('"'):
                    template_parts.append(arg[1:-1])  # Remove quotes
                else:
                    template_parts.append(f"${{{arg}}}")  # Wrap variables/expressions in ${}
            # Combine into a template literal
            template_str = f"`{''.join(template_parts)}`"
            variable = JSVariable(handler, entry.address, f'r{dest_reg}', template_str, func_name, template_str)
            analysis.AddResult(entry, variable)
            return OpcodeResult(entry, variable)

        first_arg = argList[0] if argList else None
        # Extract the base object from function name, e.g., "this.console" from "this.console.log"
        func_parts = func_name.split(".")
        base_object = ".".join(func_parts[:-1]) if len(func_parts) > 1 else None

        explicit_receiver_passed = False
        checked_args = []
        for arg in argList:
            if arg == "undefined" or arg == base_object:
                # If the first arg is "undefined" or it's the same as the function's base (e.g., "this.console")
                explicit_receiver_passed = first_arg in ("undefined", base_object)
                continue
            checked_args.append(arg)

        args_str = ", ".join(r for r in checked_args)
        if self.ShouldUseCall(func_variable) and not explicit_receiver_passed:
            func_val = f".call(this, {args_str})"
        else:
            func_val = f"({args_str})"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{func_name}{func_val}", func_name, func_val)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    @staticmethod
    def ShouldUseCall(variable: JSVariable) -> bool:
        """
        Decide if we should emit `.call(this, ...)` based on the variable info.
        """
        if not variable:
            return True  # fallback safety

        # If it's created by a CreateClosure handler, assume it doesn't need .call
        if variable.handler == 'CreateClosure':
            return False

        if variable.name in ('fetch', 'encodeURIComponent'):  # Known global functions
            return False

        # If func_name starts with "this.", assume it's a method needing `.call(this, ...)`
        if variable.name and variable.name.startswith("this."):
            return True

        # Otherwise, assume it's a property (this.console.log), needs .call
        return True


# DEFINE_OPCODE_3(Call, Reg8, Reg8, UInt8)
# Example: <Call>: <Reg8: 4, Reg8: 9, UInt8: 6>
class Call(CallX):
    """The same semantics as CallX but with a runtime-determined argument count
    (UInt8) instead of a fixed arity."""
    _PATTERN = sequence(REG, REG, UINT8)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, func_reg, num_args = map(int, match.groups())
        func_name = self.GetValueByReg(analysis, func_reg)
        arg_regs = list(range(func_reg - num_args, func_reg))  # Arguments in reverse order
        # argList = [self.GetValueByReg(analysis, r) for r in arg_regs]
        argList = [
            f"r{r}"
            for r in arg_regs
        ]
        args_str = ", ".join(argList)

        func_val = f"({args_str})" if not self.ShouldUseCall(
            self.GetVariableByReg(analysis, func_reg)) else f".call(this, {args_str})"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{func_name}{func_val}", func_name, func_val)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# @formatter:off
class Call1(CallX): num_args = 1
class Call2(CallX): num_args = 2
class Call3(CallX): num_args = 3
class Call4(CallX): num_args = 4
# @formatter:on
