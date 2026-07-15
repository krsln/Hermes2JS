import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from ._shared_patterns import REG, sequence

# Pre-compiled patterns
_BINARY_REG_PATTERN = sequence(REG, REG, REG)
_UNARY_REG_PATTERN = sequence(REG, REG)


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


# /// Arg1 = Arg2 + 1 (numeric increment).
# /// Note: like other Hermes bytecode ops, this is a pure "produce a new
# /// value in Arg1" instruction — it does not mutate Arg2 in place. Any
# /// pre/post-increment sugaring (`x++` vs `++x`) is a higher-level pattern
# /// that would need to be reconstructed from surrounding Mov/store
# /// instructions; at the opcode level we can only emit the raw expression.
# DEFINE_OPCODE_2(Inc, Reg8, Reg8)
# Example: <Inc>: <Reg8: 3, Reg8: 3>
class Inc(OpcodeHandler):
    """Arg1 = Arg2 + 1"""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _UNARY_REG_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected two Reg8 arguments")

        dest_reg, src_reg = map(int, match.groups())
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
    """ToNumeric coercion (unary +)"""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _UNARY_REG_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected two Reg8 arguments")

        dest_reg, src_reg = map(int, match.groups())
        src_val = self.GetValueByReg(analysis.results, src_reg) or f"r{src_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"+{src_val}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Arg1 = typeof Arg2.
# DEFINE_OPCODE_2(TypeOf, Reg8, Reg8)
# Example: <TypeOf>: <Reg8: 1, Reg8: 0>
class TypeOf(OpcodeHandler):
    """typeof operator"""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _UNARY_REG_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected two Reg8 arguments")

        dest_reg, src_reg = map(int, match.groups())
        src_val = self.GetValueByReg(analysis.results, src_reg) or f"r{src_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"typeof {src_val}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Arg1 = (Arg2 instanceof Arg3).
# DEFINE_OPCODE_3(InstanceOf, Reg8, Reg8, Reg8)
# Example: <InstanceOf>: <Reg8: 2, Reg8: 0, Reg8: 1>
class InstanceOf(OpcodeHandler):
    """instanceof operator"""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _BINARY_REG_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, lhs_reg, rhs_reg = map(int, match.groups())

        lhs_val = self.GetValueByReg(analysis.results, lhs_reg) or f"r{lhs_reg}"
        rhs_val = self.GetValueByReg(analysis.results, rhs_reg) or f"r{rhs_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{lhs_val} instanceof {rhs_val}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Arg1 = (Arg2 < Arg3), a boolean *value*.
# /// Contrast with JLess in JmpCompare.py: that opcode performs the same
# /// comparison but as a conditional *jump* — no boolean is ever
# /// materialized into a register. This opcode is what backs a plain
# /// expression like `const isSmaller = a < b;`.
# DEFINE_OPCODE_3(Less, Reg8, Reg8, Reg8)
# Example: <Less>: <Reg8: 0, Reg8: 93, Reg8: 0>
class Less(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _BINARY_REG_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, lhs_reg, rhs_reg = (int(x) for x in match.groups())
        lhs_val = self.GetValueByReg(analysis.results, lhs_reg) or f"r{lhs_reg}"
        rhs_val = self.GetValueByReg(analysis.results, rhs_reg) or f"r{rhs_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{lhs_val} < {rhs_val}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)



# /// Arg1 = delete Arg2[Arg3].
# DEFINE_OPCODE_3(DelByVal, Reg8, Reg8, Reg8)
# Example: <DelByVal>: <Reg8: 2, Reg8: 0, Reg8: 1>
class DelByVal(OpcodeHandler):
    """delete obj[prop]"""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _BINARY_REG_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, obj_reg, prop_reg = map(int, match.groups())

        obj_val = self.GetValueByReg(analysis.results, obj_reg) or f"r{obj_reg}"
        prop_val = self.GetValueByReg(analysis.results, prop_reg) or f"r{prop_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"delete {obj_val}[{prop_val}]")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)