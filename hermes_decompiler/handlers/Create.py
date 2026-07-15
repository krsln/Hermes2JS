import re

from hermes_decompiler.Logger import logger
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from ._shared_patterns import REG, FUNCTION_ID, sequence


# /// Allocate the `this` object for a constructor call, ahead of the actual
# /// Construct/CallDirect invocation that follows.
# /// Arg1 is the destination register.
# /// Arg2 is the closure (used to look up its .prototype).
# /// Arg3 is the `new.target` (the constructor actually being `new`'d, which
# ///      may differ from Arg2 in a derived-class / Reflect.construct call).
# DEFINE_OPCODE_3(CreateThis, Reg8, Reg8, Reg8)
# Example: <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 2>
class CreateThis(OpcodeHandler):
    """Represents `this` object allocation prior to a constructor call."""

    _PATTERN = sequence(REG, REG, REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected three Reg8 arguments")

        dest, func, new_target = (int(x) for x in match.groups())

        func_name = self.GetValueByReg(analysis.results, func) or f"r{func}"
        new_target_name = self.GetValueByReg(analysis.results, new_target) or f"r{new_target}"

        variable = JSVariable(
            handler,
            entry.address,
            f'r{dest}',
            f"createThis(prototype={func_name}, constructor={new_target_name})",
        )

        # variable = JSVariable(handler, entry.address, f'r{dest}', f"createThis({func_name}, {new_target_name});")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Create a closure.
# /// Arg1 is the register in which to store the closure.
# /// Arg2 is the current environment as loaded by GetEnvironment 0.
# /// Arg3 is index in the function table.
# DEFINE_OPCODE_3(CreateClosure, Reg8, Reg8, UInt16)
# DEFINE_OPCODE_3(CreateClosureLongIndex, Reg8, Reg8, UInt32)
# OPERAND_FUNCTION_ID(CreateClosure, 3)
# OPERAND_FUNCTION_ID(CreateClosureLongIndex, 3)
# Example: <CreateClosure>: <Reg8: 3, Reg8: 1, function_id: 11944>  # Function: [#11944  of 37 bytes]: 1 params @ offset 0x0021917e
# Example: <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 11947>  # Function: [#11947 fetchMovies of 29 bytes]: 2 params @ offset 0x00150430
class CreateClosure(OpcodeHandler):
    """Creates a closure bound to the given environment register, resolving
    its display name from the function table (or a `function_N` fallback
    if the id isn't in the table)."""

    _PATTERN = sequence(REG, REG, FUNCTION_ID)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8, Reg8 and function_id arguments")

        dest, env, func_id = (int(x) for x in match.groups())

        func_name = analysis.functionTable.get(str(func_id), f"function_{func_id}")

        env_var = self.GetVariableByReg(analysis.results, env)
        env_value = env_var.value if env_var and env_var.value else 'undefined'
        # print(env, env_value)

        # Simplified closure representation
        variable = JSVariable(
            handler,
            entry.address,
            f'r{dest}',
            f"{func_name} /* Closure with env r{env} = {env_value} */",
        )
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# The long-index variant only differs in the function_id operand's on-disk
# width (UInt32 instead of UInt16); the disassembler still labels it
# `function_id:` either way, so the shared FUNCTION_ID pattern already
# covers both and no logic needs to change.
#
# NOTE: this class was documented in the header comment above but never
# actually defined/registered in the original file — CreateClosureLongIndex
# opcodes would have silently fallen through to "no handler found" during
# dispatch. Added here to close that gap.
class CreateClosureLongIndex(CreateClosure):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return super().Handle(analysis, entry)


# /// Create a RegExp literal.
# /// Arg1 is the destination.
# /// Arg2 is the string_id of the pattern.
# /// Arg3 is the string_id of the flags.
# /// Arg4 is an index into the regexp bytecode table (compiled matcher; not
# ///      needed to reconstruct the source-level literal).
# DEFINE_OPCODE_4(CreateRegExp, Reg8, UInt32, UInt32, UInt32)
# Example: <CreateRegExp>: <Reg8: 0, UInt32: 12, UInt32: 13, UInt32: 0>  # String: '^\d+$'  String: 'g'
class CreateRegExp(OpcodeHandler):
    _PATTERN = re.compile(
        r'^Reg\d+:\s*(\d+),\s*UInt32:\s*(\d+),\s*UInt32:\s*(\d+),\s*UInt32:\s*(\d+)$'
    )

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8 and three UInt32 arguments")

        dest_reg, pattern_id, flags_id = (int(match.group(i)) for i in (1, 2, 3))

        pattern, flags = self._resolve_pattern_and_flags(analysis, entry, pattern_id, flags_id)
        if pattern is None:
            error = f'/* Error: could not resolve RegExp pattern (string_id {pattern_id}) */ undefined'
            return self.Exception(analysis, entry, error)

        js_regex = f"/{pattern}/{flags or ''}"
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_regex)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    @staticmethod
    def _resolve_pattern_and_flags(analysis, entry, pattern_id: int, flags_id: int):
        """
        Prefer the disassembler's own `String: '...'` comment annotations
        (present on real Hermes dumps for CreateRegExp), falling back to a
        stringTable lookup by id. Returns (pattern, flags), with either
        element possibly None if it could not be resolved.
        """
        comment_matches = re.compile(r"String:\s*'([^']*)'").findall(entry.comment or "")
        if len(comment_matches) >= 2:
            return comment_matches[0], comment_matches[1]

        pattern = analysis.stringTable.get(str(pattern_id))
        flags = analysis.stringTable.get(str(flags_id))
        if pattern is None:
            logger.warning(
                f"CreateRegExp at address {entry.address}: unresolved pattern string_id {pattern_id}"
            )
        return pattern, flags
