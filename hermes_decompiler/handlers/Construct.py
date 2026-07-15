from typing import List

from hermes_decompiler.Logger import logger
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from ._shared_patterns import REG, UINT8, sequence


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
    _PATTERN = sequence(REG, REG, UINT8)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Match: Reg8 (dest), Reg8 (closure to invoke), UInt8 (arg count)
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8, Reg8, UInt8 arguments")

        dest_reg, func_reg, arg_count = (int(x) for x in match.groups())

        func_name = self.GetValueByReg(analysis.results, func_reg)
        if func_name is None:
            logger.warning(f"{handler} at address {entry.address}: unresolved constructor register r{func_reg}")
            func_name = f"r{func_reg}"

        # Reverse-order args: usually preloaded into registers before this
        args = self._resolve_args(analysis, entry, handler, func_reg, arg_count)
        args_str = ", ".join(args)

        const = f"new {func_name}"
        const_val = f"({args_str})"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{const}{const_val};", const, const_val)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    def _resolve_args(self, analysis: HermesAnalysis, entry: OpcodeEntry, handler: str,
                      func_reg: int, arg_count: int) -> List[str]:
        arg_regs = range(func_reg - arg_count, func_reg)
        args = []
        for offset, reg in enumerate(arg_regs):
            value = self.GetValueByReg(analysis.results, reg)
            if value is None:
                logger.warning(
                    f"{handler} at address {entry.address}: unresolved argument register r{reg}; "
                    f"using placeholder arg{offset}"
                )
                value = f"arg{offset}"
            args.append(value)

        if args and args[0] == "this":
            args = args[1:]

        return args
