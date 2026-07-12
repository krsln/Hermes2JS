import re
from typing import Dict

from conversion.hermes2js.models.HermesAnalysis import HermesAnalysis
from conversion.hermes2js.models.OpcodeResult import OpcodeResult
from conversion.hermes2js.models.JSVariable import JSVariable
from conversion.hermes2js.models.OpcodeEntry import OpcodeEntry
from conversion.hermes2js.models.OpcodeHandler import OpcodeHandler


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
            return self.InvalidArgs(analysis, entry)

        match = re.match(reg_pattern, entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        # Strip commas and convert to integers
        regs = [int(x.split(":")[1].strip()) for x in match.groups()]
        dest_reg, func_reg, *args = regs

        func_variable = self.GetVariableByReg(analysis.results, func_reg)
        func_name = self.GetValueByReg(analysis.results, func_reg)

        argList = self.GetFuncArgs(analysis.results, args)

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


# /// Call a function with one arg.
# /// Arg1 is the destination of the return value.
# /// Arg2 is the closure to invoke.
# /// Arg3 is the first argument.
# DEFINE_OPCODE_3(Call1, Reg8, Reg8, Reg8)
# DEFINE_RET_TARGET(Call1)
class Call1(CallX):
    num_args = 1


# /// Call a function directly without a closure.
# /// Arg1 is the destination of the return value.
# /// Arg2 is the number of arguments, assumed to be found in reverse order
# ///      from the end of the current frame. The first argument 'this'
# ///      is assumed to be created with CreateThis.
# /// Arg3 is index in the function table.
# /// Note that we expect the variable-sized argument to be last.
# DEFINE_OPCODE_3(CallDirect, Reg8, UInt8, UInt16)
# OPERAND_FUNCTION_ID(CallDirect, 3)
# DEFINE_RET_TARGET(CallDirect)
class CallDirect(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Parse args: Reg8, UInt8, UInt16
        match = re.match(r'^Reg(\d+):\s*(\d+),\s*UInt8:\s*(\d+),\s*UInt16:\s*(\d+)$', entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg = int(match.group(2))
        arg_count = int(match.group(3))
        func_index = int(match.group(4))

        # Lookup the function name from function index table, assume it's stored in analysis context
        func_name = analysis.functionTable.get(str(func_index), f"function_{func_index}")

        # Get arguments from the frame, assume `GetArgsFromFrame` helper exists or can be implemented
        args = [f"arg{i}" for i in range(arg_count)]
        args_str = ", ".join(args)

        func_val = f"{func_name}({args_str})"
        variable = JSVariable(handler, entry.address, f"r{dest_reg}", func_val, func_name, func_val)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Call a function.
# /// Arg1 is the destination of the return value.
# /// Arg2 is the closure to invoke.
# /// Arg3 is the number of arguments, assumed to be found in reverse order
# ///      from the end of the current frame.
# DEFINE_OPCODE_3(Call, Reg8, Reg8, UInt8)
# DEFINE_RET_TARGET(Call)
# Example: <Call>: <Reg8: 4, Reg8: 9, UInt8: 6>
class Call(CallX):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'^Reg8:\s*(\d+)\s*,\s*Reg8:\s*(\d+)\s*,\s*UInt8:\s*(\d+)$', entry.args.strip())

        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, func_reg, num_args = map(int, match.groups())
        func_name = self.GetValueByReg(analysis.results, func_reg)
        arg_regs = list(range(func_reg - num_args, func_reg))  # Arguments in reverse order
        argList = [self.GetValueByReg(analysis.results, r) for r in arg_regs]
        args_str = ", ".join(argList)
        func_val = f"({args_str})" if not self.ShouldUseCall(self.GetVariableByReg(analysis.results, func_reg)) else f".call(this, {args_str})"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{func_name}{func_val}", func_name, func_val)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

# /// Call a function with two args.
# /// Arg1 is the destination of the return value.
# /// Arg2 is the closure to invoke.
# /// Arg3 is the first argument.
# /// Arg4 is the second argument.
# DEFINE_OPCODE_4(Call2, Reg8, Reg8, Reg8, Reg8)
# DEFINE_RET_TARGET(Call2)
class Call2(CallX):
    num_args = 2


# /// Call a function with three args.
# /// Arg1 is the destination of the return value.
# /// Arg2 is the closure to invoke.
# /// Arg3 is the first argument.
# /// Arg4 is the second argument.
# /// Arg5 is the third argument.
# DEFINE_OPCODE_5(Call3, Reg8, Reg8, Reg8, Reg8, Reg8)
# DEFINE_RET_TARGET(Call3)
class Call3(CallX):
    num_args = 3


# /// Call a function with four args.
# /// Arg1 is the destination of the return value.
# /// Arg2 is the closure to invoke.
# /// Arg3 is the first argument.
# /// Arg4 is the second argument.
# /// Arg5 is the third argument.
# /// Arg6 is the fourth argument.
# DEFINE_OPCODE_6(Call4, Reg8, Reg8, Reg8, Reg8, Reg8, Reg8)
# DEFINE_RET_TARGET(Call4)
class Call4(CallX):
    num_args = 4
