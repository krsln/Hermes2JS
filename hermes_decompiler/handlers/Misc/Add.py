from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence

_BINARY_REG_PATTERN = sequence(REG, REG, REG)


# /// Arg1 = Arg2 + Arg3.
# /// Add performs both numeric addition and string concatenation, mirroring
# /// JS `+` semantics; AddN is the numeric-only fast-path variant emitted by
# /// the compiler when both operands are statically known to be numbers —
# /// the *decompiled* JS output is identical either way, so AddN subclasses
# /// Add directly.
# DEFINE_OPCODE_3(Add, Reg8, Reg8, Reg8)
# DEFINE_OPCODE_3(AddN, Reg8, Reg8, Reg8)
# Example: <Add>: <Reg8: 2, Reg8: 0, Reg8: 1>
class Add(OpcodeHandler):
    """Arg1 = Arg2 + Arg3 (numeric or string concatenation)"""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _BINARY_REG_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, lhs_reg, rhs_reg = map(int, match.groups())

        lhs_val = self.GetValueByReg(analysis.results, lhs_reg) or f"r{lhs_reg}"
        rhs_val = self.GetValueByReg(analysis.results, rhs_reg) or f"r{rhs_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{lhs_val} + {rhs_val}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class AddN(Add):
    """Numeric-only add (fast path). Same JS output as Add."""
    pass
