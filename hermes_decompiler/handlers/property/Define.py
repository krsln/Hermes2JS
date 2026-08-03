from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence, UINT32, UINT16
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import (
    AssignmentExpression,
    BooleanLiteral,
    CallExpression,
    Identifier,
    MemberExpression,
    NumericLiteral,
    ObjectExpression, ObjectProperty,
)
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt8, UInt16 (total size 5)
# DEFINE_OPCODE_4(DefineOwnById, Reg8, Reg8, UInt8, UInt16)
# Example: <DefineOwnById>: <Reg8: 2, Reg8: 5, UInt8: 1, UInt16: 160>
class DefineOwnById(OpcodeHandler):
    """Define an own object property by string ID: obj.foo = value (fresh property)."""

    _PATTERN = sequence(REG, REG, UINT8, UINT16)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        obj_reg, value_reg, _cache, string_id = map(int, match.groups())

        property_name = entry.identifier_name or f"string_{string_id}"

        left = MemberExpression(
            receiver=self.get_register_expression(analysis, obj_reg),
            member=Identifier(name=property_name),
            computed=False,
        )
        right = self.get_register_expression(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, Reg8, UInt8, UInt32 (string_id) (total size 7)
# DEFINE_OPCODE_4(DefineOwnByIdLong, Reg8, Reg8, UInt8, UInt32)
# Example:
class DefineOwnByIdLong(DefineOwnById):
    pass


# Reg8, Reg8, Reg8, UInt8 (total size 4)
# DEFINE_OPCODE_4(DefineOwnByVal, Reg8, Reg8, Reg8, UInt8)
# Example: <DefineOwnByVal>: <Reg8: 4, Reg8: 7, Reg8: 5, UInt8: 0>
class DefineOwnByVal(OpcodeHandler):
    """Define an own object property by computed value: obj[key] = value (fresh property)."""

    _PATTERN = sequence(REG, REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected Reg8, Reg8, Reg8, UInt8 arguments"
            )

        obj_reg, value_reg, key_reg, _enumerable = map(int, match.groups())

        left = MemberExpression(
            receiver=self.get_register_expression(analysis, obj_reg),
            member=self.get_register_expression(analysis, key_reg),
            computed=True,
        )
        right = self.get_register_expression(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8, Reg8, UInt8 (total size 5)
# DEFINE_OPCODE_5(DefineOwnGetterSetterByVal, Reg8, Reg8, Reg8, Reg8, UInt8)
# Example: <DefineOwnGetterSetterByVal>: <Reg8: 6, Reg8: 7, Reg8: 5, Reg8: 0, UInt8: 0>
class DefineOwnGetterSetterByVal(OpcodeHandler):
    """Object.defineProperty(obj, key, { get, set, enumerable })."""

    _PATTERN = sequence(REG, REG, REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected Reg8, Reg8, Reg8, Reg8, UInt8 arguments"
            )

        obj_reg, key_reg, getter_reg, setter_reg, enumerable = map(int, match.groups())

        callee = MemberExpression(
            receiver=Identifier(name="Object"),
            member=Identifier(name="defineProperty"),
            computed=False,
        )

        descriptor = ObjectExpression(
            properties=(
                ObjectProperty(
                    key=Identifier(name="get"),
                    value=self.get_register_expression(analysis, getter_reg),
                    shorthand=False,
                    computed=False,
                ),
                ObjectProperty(
                    key=Identifier(name="set"),
                    value=self.get_register_expression(analysis, setter_reg),
                    shorthand=False,
                    computed=False,
                ),
                ObjectProperty(
                    key=Identifier(name="enumerable"),
                    value=BooleanLiteral(value=bool(enumerable)),
                    shorthand=False,
                    computed=False,
                ),
            )
        )

        expression = CallExpression(
            callee=callee,
            arguments=(
                self.get_register_expression(analysis, obj_reg),
                self.get_register_expression(analysis, key_reg),
                descriptor,
            ),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(DefineOwnByIndex, Reg8, Reg8, UInt8)
# Example: <DefineOwnByIndex>: <Reg8: 3, Reg8: 4, UInt8: 70>
class DefineOwnByIndex(OpcodeHandler):
    """Define an own indexed property: arr[N] = value (N is an immediate index)."""

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, UInt8 arguments")

        obj_reg, value_reg, index = map(int, match.groups())

        left = MemberExpression(
            receiver=self.get_register_expression(analysis, obj_reg),
            member=NumericLiteral(value=index),
            computed=True,
        )
        right = self.get_register_expression(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, Reg8, UInt32 (total size 6)
# DEFINE_OPCODE_3(DefineOwnByIndexL, Reg8, Reg8, UInt32)
class DefineOwnByIndexL(DefineOwnByIndex):
    _PATTERN = sequence(REG, REG, UINT32)


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(DefineOwnInDenseArray, Reg8, Reg8, UInt8)
# Example: <DefineOwnInDenseArray>: <Reg8: 4, Reg8: 3, UInt8: 2>
class DefineOwnInDenseArray(OpcodeHandler):
    """Define an own property directly in dense array storage: arr[N] = value."""

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, UInt8 arguments")

        obj_reg, value_reg, index = map(int, match.groups())

        left = MemberExpression(
            receiver=self.get_register_expression(analysis, obj_reg),
            member=NumericLiteral(value=index),
            computed=True,
        )
        right = self.get_register_expression(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, Reg8, UInt16 (total size 4)
# DEFINE_OPCODE_3(DefineOwnInDenseArrayL, Reg8, Reg8, UInt16)
class DefineOwnInDenseArrayL(DefineOwnInDenseArray):
    _PATTERN = sequence(REG, REG, UINT16)
