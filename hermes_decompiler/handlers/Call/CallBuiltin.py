from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, sequence


# /// Call one of the VM's built-in functions directly by index, bypassing
# /// normal property lookup (a fast path for common calls like
# /// Array.prototype.push, Object.keys, etc.).
# /// Arg1 is the destination of the return value.
# /// Arg2 is the builtin function's index into Hermes's internal builtin
# ///      table (not a string_id — a fixed enum baked into the VM/compiler,
# ///      see Hermes's BuiltinFunctions.def).
# /// Arg3 is the number of arguments, found in the registers immediately
# ///      preceding `dest_reg` — same best-effort, frame-position heuristic
# ///      CallDirect uses (see Call/CallDirect.py); real layout depends on
# ///      the stack frame pointer, which isn't tracked here.
# DEFINE_OPCODE_3(CallBuiltin, Reg8, UInt8, UInt8)
# Example: <CallBuiltin>: <Reg8: 3, UInt8: 12, UInt8: 2>
class CallBuiltin(OpcodeHandler):
    """
    ⚠️ Builtin-index -> name resolution needs a lookup table this codebase
    doesn't define yet. Falls back to `builtin_<id>` if
    `analysis.builtinTable` isn't populated — populate it (id -> qualified
    name, e.g. "Array.prototype.push") to get real output instead of
    placeholders. Hermes's own `BuiltinFunctions.def` is the source of
    truth for what each index means.
    """

    _PATTERN = sequence(REG, UINT8, UINT8)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8, UInt8, UInt8 arguments")

        dest_reg, builtin_id, arg_count = map(int, match.groups())

        builtin_table = getattr(analysis, "builtinTable", None) or {}
        func_name = builtin_table.get(str(builtin_id), f"builtin_{builtin_id}")

        arg_start = dest_reg - arg_count
        args = []
        for offset, reg in enumerate(range(arg_start, dest_reg)):
            value = self.GetValueByReg(analysis.results, reg)
            args.append(value if value is not None else f"arg{offset}")

        args_str = ", ".join(args)
        func_val = f"({args_str})"

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", f"{func_name}{func_val}", func_name, func_val)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)