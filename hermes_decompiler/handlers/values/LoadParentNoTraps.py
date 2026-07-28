from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.expressions import CallExpression, Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# LoadParentNoTraps -- ***SIGNATURE NOT CONFIRMED***
#
# Not found in either source consulted. Inferred from its name: JS
# engines distinguish between `Object.getPrototypeOf(obj)` (which, for
# a Proxy, invokes the Proxy's `getPrototypeOf` trap) and internal
# engine operations that need the "real" underlying prototype without
# triggering user-defined trap code (used internally for e.g. property
# lookup chains, instanceof checks against exotic objects, or spec
# algorithms that explicitly call the *ordinary* [[GetPrototypeOf]]
# rather than the object's possibly-overridden one). "NoTraps" strongly
# suggests this is that internal/ordinary variant.
#
# Guessed shape: Reg8 dest, Reg8 obj -- same two-register shape as most
# other simple accessor opcodes (compare GetParentEnvironment's
# Reg8+immediate vs. this being Reg8+Reg8 since the source object is
# data-dependent, not statically known).
#
# Rendered as a named pseudo-call (no real single-expression JS syntax
# distinguishes "ordinary [[GetPrototypeOf]], bypassing Proxy traps"
# from `Object.getPrototypeOf(obj)` at the source level -- they only
# differ for Proxy objects), following the same convention used for
# other opaque/internal-only opcodes in this codebase (createThis(),
# getParentEnvironment(), etc).
#
# VERIFY operand count and register roles against your actual
# disassembler output before trusting this.
class LoadParentNoTraps(OpcodeHandler):
    """Get an object's ordinary [[GetPrototypeOf]], bypassing Proxy traps."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8 arguments")

        dest_reg, obj_reg = map(int, match.groups())

        obj = self.get_register_value(analysis, obj_reg)

        expression = CallExpression(
            callee=Identifier(name="__getPrototypeOfNoTraps__"),
            arguments=(obj,),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
