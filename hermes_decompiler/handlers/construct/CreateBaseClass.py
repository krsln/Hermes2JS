from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import sequence, REG, UINT8, UINT16, UINT32
from hermes_decompiler.handlers.OpcodeHandler import OpcodeHandler
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, Reg8, UInt16 (total size 5)
# DEFINE_OPCODE_4(CreateBaseClass, Reg8, Reg8, Reg8, UInt16)
# Example: <CreateBaseClass>: <Reg8: 1, Reg8: 3, Reg8: 2, UInt16: 8197>
class CreateBaseClass(OpcodeHandler):
    """Create a base (non-derived) ES6 class closure."""

    _PATTERN = sequence(REG, REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected Reg8, Reg8, Reg8, function_id arguments"
            )

        closure_reg, home_object_reg, _env_reg, function_id = map(int, match.groups())

        func_name = (
            entry.function.name
            if entry.function and entry.function.name
            else f"function_{function_id}"
        )
        class_name = f"function_{function_id}"
        expression = Identifier(name=func_name)

        result = OpcodeResult(entry, value=expression, dest_reg=closure_reg)
        analysis.add_result(result)

        # Home object (used to resolve `super` inside methods) has no
        # direct JS-visible expression of its own.
        home_object_expr = Identifier(name=f"{class_name}.prototype")
        home_result = OpcodeResult(entry, value=home_object_expr, dest_reg=home_object_reg)
        analysis.add_result(home_result)

        return result


# Reg8, Reg8, Reg8, UInt32 (total size 7)
# DEFINE_OPCODE_4(CreateBaseClassLongIndex, Reg8, Reg8, Reg8, UInt32)
class CreateBaseClassLongIndex(CreateBaseClass):
    _PATTERN = sequence(REG, REG, REG, UINT32)


# Reg8, Reg8, Reg8, Reg8, UInt16 (total size 6)
# DEFINE_OPCODE_5(CreateDerivedClass, Reg8, Reg8, Reg8, Reg8, UInt16)
# Example: <CreateDerivedClass>: <Reg8: 1, Reg8: 3, Reg8: 2, Reg8: 1, UInt16: 2363>
class CreateDerivedClass(OpcodeHandler):
    """Create a derived (extends ...) ES6 class closure."""

    _PATTERN = sequence(REG, REG, REG, REG, UINT16)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected Reg8, Reg8, Reg8, Reg8, function_id arguments"
            )

        closure_reg, home_object_reg, _env_reg, _super_class_reg, function_id = map(int, match.groups())

        func_name = (
            entry.function.name
            if entry.function and entry.function.name
            else f"function_{function_id}"
        )
        class_name = f"function_{function_id}"
        expression = Identifier(name=func_name)

        result = OpcodeResult(entry, value=expression, dest_reg=closure_reg)
        analysis.add_result(result)

        home_object_expr = Identifier(name=f"{class_name}.prototype")
        home_result = OpcodeResult(entry, value=home_object_expr, dest_reg=home_object_reg)
        analysis.add_result(home_result)

        return result


# Reg8, Reg8, Reg8, Reg8, UInt32 (total size 8)
# DEFINE_OPCODE_5(CreateDerivedClassLongIndex, Reg8, Reg8, Reg8, Reg8, UInt32)
class CreateDerivedClassLongIndex(CreateDerivedClass):
    _PATTERN = sequence(REG, REG, REG, REG, UINT32)
