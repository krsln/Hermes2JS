import re
from typing import Dict

from HermesAssembly2JS.Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from HermesAssembly2JS.Hermes2JS.Models.OpcodeResult import OpcodeResult
from HermesAssembly2JS.Hermes2JS.Models.JSVariable import JSVariable
from HermesAssembly2JS.Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from HermesAssembly2JS.Hermes2JS.Models.OpcodeHandler import OpcodeHandler


# Note:
# If you want to support both .call() and direct call, you could check the previous instruction context
# (e.g., if the function was fetched via .log, you may want to emit .call()).

# “The difference [between direct and indirect call] is whether the function is a reference or a closure...
# closures are typically created via a CreateClosure opcode...”


class CallX(OpcodeHandler):
    # Precompiled regex patterns for each number of arguments
    _REGEX_PATTERNS: Dict[int, re.Pattern] = {
        1: re.compile(r'^(Reg\d+:\s*\d+)\s*,\s*(Reg\d+:\s*\d+)\s*,\s*(Reg\d+:\s*\d+)$'),
        2: re.compile(r'^(Reg\d+:\s*\d+)\s*,\s*(Reg\d+:\s*\d+)\s*,\s*(Reg\d+:\s*\d+)\s*,\s*(Reg\d+:\s*\d+)$'),
        3: re.compile(
            r'^(Reg\d+:\s*\d+)\s*,\s*(Reg\d+:\s*\d+)\s*,\s*(Reg\d+:\s*\d+)\s*,\s*(Reg\d+:\s*\d+)\s*,\s*(Reg\d+:\s*\d+)$'),
        4: re.compile(
            r'^(Reg\d+:\s*\d+)\s*,\s*(Reg\d+:\s*\d+)\s*,\s*(Reg\d+:\s*\d+)\s*,\s*(Reg\d+:\s*\d+)\s*,\s*(Reg\d+:\s*\d+)\s*,\s*(Reg\d+:\s*\d+)$')
    }

    num_args = 1  # to be overridden

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Get precompiled regex for the number of arguments
        reg_pattern = self._REGEX_PATTERNS.get(self.num_args)
        if not reg_pattern:
            return self.InvalidArgs(entry)

        match = re.match(reg_pattern, entry.args.strip())
        if not match:
            return self.InvalidArgs(entry)

        # Strip commas and convert to integers
        regs = [int(x.split(":")[1].strip()) for x in match.groups()]
        dest_reg, func_reg, *args = regs

        func_variable = self.GetVariableByReg(analysis.results, func_reg)
        func_name = self.GetValueByReg(analysis.results, func_reg)

        argList = self.GetFuncArgs(analysis.results, args)

        checked_args = []
        use_call = True
        for arg in argList:
            if arg.startswith("this."):
                # print(arg)
                use_call = False
            else:
                checked_args.append(arg)

        args_str = ", ".join(r for r in checked_args)
        if self.ShouldUseCall(func_variable) and use_call:
            # Default behavior: use .call(this, ...)
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

        # Otherwise, assume it's a property (this.console.log), needs .call
        return True


# # Call a function with one arg.
# # Arg1 is the destination of the return value.
# # Arg2 is the closure to invoke.
# # Arg3 is the first argument.
# Example: <Call1>: <Reg8: 8, Reg8: 6, Reg8: 7>
class Call1(CallX):
    num_args = 1


# Call a function with two args.
# Arg1 is the destination of the return value.
# Arg2 is the closure to invoke.
# Arg3 is the first argument.
# Arg4 is the second argument.
# Example: <Call2>: <Reg8: 6, Reg8: 4, Reg8: 0, Reg8: 3>
class Call2(CallX):
    num_args = 2


# Call a function with three args.
# Arg1 is the destination of the return value.
# Arg2 is the closure to invoke.
# Arg3 is the first argument.
# Arg4 is the second argument.
# Arg5 is the third argument.
# Example: <Call3>: <Reg8: 14, Reg8: 21, Reg8: 3, Reg8: 20, Reg8: 14>
class Call3(CallX):
    num_args = 3


# Call a function with four args.
# Arg1 is the destination of the return value.
# Arg2 is the closure to invoke.
# Arg3 is the first argument.
# Arg4 is the second argument.
# Arg5 is the third argument.
# Arg6 is the fourth argument.
# Example: <Call4>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 5, Reg8: 2>
class Call4(CallX):
    num_args = 4
