from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression, MemberExpression, Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(AddOwnPrivateBySym, Reg8, Reg8, Reg8)
# Example: <AddOwnPrivateBySym>: <Reg8: 4, Reg8: 3, Reg8: 7>
class AddOwnPrivateBySym(OpcodeHandler):
    """Initialize a private class field on a fresh instance: obj.#field = value."""

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, Reg8 arguments")

        obj_reg, private_name_reg, value_reg = map(int, match.groups())

        field_name = entry.identifier_name or f"__private_{private_name_reg}__"

        left = MemberExpression(
            receiver=self.get_register_value(analysis, obj_reg),
            member=Identifier(name=f"#{field_name}"),
            computed=False,
        )
        right = self.get_register_value(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, Reg8, UInt8, Reg8 (total size 4)
# DEFINE_OPCODE_4(GetOwnPrivateBySym, Reg8, Reg8, UInt8, Reg8)
# <GetOwnPrivateBySym>: <Reg8: 7, Reg8: 5, UInt8: 0, Reg8: 4>
class GetOwnPrivateBySym(OpcodeHandler):
    """Read a private class field: obj.#field"""

    _PATTERN = sequence(REG, REG, UINT8, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected Reg8, Reg8, UInt8, Reg8 arguments"
            )

        dest_reg, obj_reg, _cache, private_name_reg = map(int, match.groups())

        field_name = entry.identifier_name or f"__private_{private_name_reg}__"

        expression = MemberExpression(
            receiver=self.get_register_value(analysis, obj_reg),
            member=Identifier(name=f"#{field_name}"),
            computed=False,
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8, Reg8, UInt8, Reg8 (total size 4)
# DEFINE_OPCODE_4(PutOwnPrivateBySym, Reg8, Reg8, UInt8, Reg8)
# <PutOwnPrivateBySym>: <Reg8: 4, Reg8: 5, UInt8: 1, Reg8: 6>
class PutOwnPrivateBySym(OpcodeHandler):
    """Write a private class field on an already-initialized instance: obj.#field = value"""

    _PATTERN = sequence(REG, REG, UINT8, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected Reg8, Reg8, UInt8, Reg8 arguments"
            )

        obj_reg, value_reg, _cache, private_name_reg = map(int, match.groups())

        field_name = entry.identifier_name or f"__private_{private_name_reg}__"

        left = MemberExpression(
            receiver=self.get_register_value(analysis, obj_reg),
            member=Identifier(name=f"#{field_name}"),
            computed=False,
        )
        right = self.get_register_value(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result
