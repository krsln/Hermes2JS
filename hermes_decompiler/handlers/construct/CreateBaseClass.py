from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT16, UINT32
from hermes_decompiler.ir.expressions import Identifier


# Reg8, Reg8, Reg8, UInt16 (total size 5)
# DEFINE_OPCODE_4(CreateBaseClass, Reg8, Reg8, Reg8, UInt16)
# Example: <CreateBaseClass>: <Reg8: 1, Reg8: 3, Reg8: 2, UInt16: 8197>
class CreateBaseClass(OpcodeHandler):
    """Create a base (non-derived) ES6 class closure."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, UINT16), "Reg8, Reg8, Reg8, UInt16")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        closure_reg, home_object_reg, _env_reg, function_id = map(int, match.groups())

        func_name = (
            ctx.entry.function.name
            if ctx.entry.function and ctx.entry.function.name
            else f"function_{function_id}"
        )
        class_name = f"function_{function_id}"
        expression = Identifier(name=func_name)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=closure_reg)
        ctx.analysis.add_result(result)

        # Home object (used to resolve `super` inside methods) has no
        # direct JS-visible expression of its own.
        home_object_expr = Identifier(name=f"{class_name}.prototype")
        home_result = OpcodeResult(ctx.entry, value=home_object_expr, dest_reg=home_object_reg)
        ctx.analysis.add_result(home_result)

        return result


# Reg8, Reg8, Reg8, UInt32 (total size 7)
# DEFINE_OPCODE_4(CreateBaseClassLongIndex, Reg8, Reg8, Reg8, UInt32)
class CreateBaseClassLongIndex(CreateBaseClass):
    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, UINT32), "Reg8, Reg8, Reg8, UInt32")


# Reg8, Reg8, Reg8, Reg8, UInt16 (total size 6)
# DEFINE_OPCODE_5(CreateDerivedClass, Reg8, Reg8, Reg8, Reg8, UInt16)
# Example: <CreateDerivedClass>: <Reg8: 1, Reg8: 3, Reg8: 2, Reg8: 1, UInt16: 2363>
class CreateDerivedClass(OpcodeHandler):
    """Create a derived (extends ...) ES6 class closure."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, REG, UINT16), "Reg8, Reg8, Reg8, Reg8, UInt16")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        closure_reg, home_object_reg, _env_reg, _super_class_reg, function_id = map(int, match.groups())

        func_name = (
            ctx.entry.function.name
            if ctx.entry.function and ctx.entry.function.name
            else f"function_{function_id}"
        )
        class_name = f"function_{function_id}"
        expression = Identifier(name=func_name)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=closure_reg)
        ctx.analysis.add_result(result)

        home_object_expr = Identifier(name=f"{class_name}.prototype")
        home_result = OpcodeResult(ctx.entry, value=home_object_expr, dest_reg=home_object_reg)
        ctx.analysis.add_result(home_result)

        return result


# Reg8, Reg8, Reg8, Reg8, UInt32 (total size 8)
# DEFINE_OPCODE_5(CreateDerivedClassLongIndex, Reg8, Reg8, Reg8, Reg8, UInt32)
class CreateDerivedClassLongIndex(CreateDerivedClass):
    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, REG, UINT32), "Reg8, Reg8, Reg8, Reg8, UInt32")
