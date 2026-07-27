from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_4(CreateBaseClass, Reg8, Reg8, Reg8, UInt16 function_id)
# DEFINE_OPCODE_4(CreateBaseClassLongIndex, Reg8, Reg8, Reg8, UInt32 function_id)
#   [confirmed, hermes-dec table]
#
#   "Create a base class. Arg1 is the output register for the closure.
#    Arg2 is the output register for the home object. Arg3 is the
#    current environment. Arg4 is index in the function table."
#
# NOTE: this opcode produces TWO results (closure in Arg1, home object
# in Arg2) but OpcodeResult in this codebase only models a single
# dest_reg, matching the pattern used for CreateClosure elsewhere. The
# home-object register (Arg2) is set separately since analysis.add_result
# only tracks one destination per call; if this decompiler's
# OpcodeResult/analysis API supports multiple writes, prefer that
# instead of the two-result-object workaround below.
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


class CreateBaseClassLongIndex(CreateBaseClass):
    pass

# todo CreateDerivedClass
