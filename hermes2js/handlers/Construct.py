import re

from hermes2js.models.HermesAnalysis import HermesAnalysis
from hermes2js.models.OpcodeResult import OpcodeResult
from hermes2js.models.JSVariable import JSVariable
from hermes2js.models.OpcodeEntry import OpcodeEntry
from hermes2js.models.OpcodeHandler import OpcodeHandler


# /// Call a constructor, with semantics identical to Call.
# /// Arg1 is the destination of the return value.
# /// Arg2 is the closure to invoke.
# /// Arg3 is the number of arguments, assumed to be found in reverse order
# ///      from the end of the current frame. The first argument 'this'
# ///      is assumed to be created with CreateThis.
# DEFINE_OPCODE_3(Construct, Reg8, Reg8, UInt8)
# DEFINE_RET_TARGET(Construct)
# Example: <Construct>: <Reg8: 2, Reg8: 4, UInt8: 2>
class Construct(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Match: Reg8 (dest), Reg8 (closure to invoke), UInt8 (arg count)
        match = re.match(r'Reg8:\s*(\d+),\s*Reg8:\s*(\d+),\s*UInt8:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, func_reg, arg_count = map(int, match.groups())

        # Reverse-order args: usually preloaded into registers before this
        args = [f"arg{i}" for i in range(arg_count)]
        args_str = ", ".join(args)

        func_name = self.GetValueByReg(analysis.results, func_reg)

        const = f'new {func_name}'
        const_val = f"({args_str})"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{const}{const_val};", const, const_val)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
