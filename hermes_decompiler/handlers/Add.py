import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

_BINARY_REG_PATTERN = re.compile(r'^Reg\d+:\s*(\d+),\s*Reg\d+:\s*(\d+),\s*Reg\d+:\s*(\d+)$')
_UNARY_REG_PATTERN = re.compile(r'^Reg\d+:\s*(\d+),\s*Reg\d+:\s*(\d+)$')


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
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _BINARY_REG_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, lhs_reg, rhs_reg = (int(x) for x in match.groups())

        lhs_val = self.GetValueByReg(analysis.results, lhs_reg) or f"r{lhs_reg}"
        rhs_val = self.GetValueByReg(analysis.results, rhs_reg) or f"r{rhs_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{lhs_val} + {rhs_val}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class AddN(Add):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return super().Handle(analysis, entry)


# /// Arg1 = Arg2 + 1 (numeric increment).
# /// Note: like other Hermes bytecode ops, this is a pure "produce a new
# /// value in Arg1" instruction — it does not mutate Arg2 in place. Any
# /// pre/post-increment sugaring (`x++` vs `++x`) is a higher-level pattern
# /// that would need to be reconstructed from surrounding Mov/store
# /// instructions; at the opcode level we can only emit the raw expression.
# DEFINE_OPCODE_2(Inc, Reg8, Reg8)
# Example: <Inc>: <Reg8: 3, Reg8: 3>
class Inc(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _UNARY_REG_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected two Reg8 arguments")

        dest_reg, src_reg = (int(x) for x in match.groups())
        src_val = self.GetValueByReg(analysis.results, src_reg) or f"r{src_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{src_val} + 1")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Arg1 = ToNumeric(Arg2), i.e. coerce the operand to a Number or BigInt
# /// following the JS ToNumeric abstract operation. Emitted as a unary `+`
# /// coercion, the idiomatic JS shorthand for ToNumber (BigInt operands pass
# /// through the runtime's own coercion regardless of the emitted syntax).
# DEFINE_OPCODE_2(ToNumeric, Reg8, Reg8)
# Example: <ToNumeric>: <Reg8: 1, Reg8: 0>
class ToNumeric(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _UNARY_REG_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected two Reg8 arguments")

        dest_reg, src_reg = (int(x) for x in match.groups())
        src_val = self.GetValueByReg(analysis.results, src_reg) or f"r{src_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"+{src_val}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)