from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, STRING_ID, sequence
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import (
    AssignmentExpression,
    CallExpression,
    Identifier,
    Literal,
    MemberExpression, BooleanLiteral,
)
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_5(DefineOwnById, Reg8, Reg8, UInt8, UInt16 string_id)   [confirmed, hermes-dec table]
# DEFINE_OPCODE_5(DefineOwnByIdLong, Reg8, Reg8, UInt8, UInt32 string_id)
#
#   "Define an object own property by string index.
#    Arg1[stringtable[Arg4]] = Arg2. Arg3 is a cache index."
#
# Semantically almost identical to PutById, except the property is
# guaranteed to not exist yet and is being *defined* rather than
# assigned through the prototype chain. Hermes emits this instead of
# PutById for property definitions inside object literals / class
# bodies where the compiler already knows the property is fresh.
# The resulting JS is indistinguishable from a normal assignment, so we
# render it the same way PutById does.
class DefineOwnById(OpcodeHandler):
    """Define an own object property by string ID: obj.foo = value (fresh property)."""

    _PATTERN = sequence(REG, REG, UINT8, STRING_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        obj_reg, value_reg, _cache, string_id = map(int, match.groups())

        property_name = entry.identifier_name or f"string_{string_id}"

        left = MemberExpression(
            receiver=self.get_register_value(analysis, obj_reg),
            member=Identifier(name=property_name),
            computed=False,
        )
        right = self.get_register_value(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


class DefineOwnByIdLong(DefineOwnById):
    pass


# DEFINE_OPCODE_4(DefineOwnByVal, Reg8, Reg8, Reg8, UInt8 enumerable)   [confirmed, hermes-dec table]
#
#   "Set an own property identified by value.
#    Arg1 is the destination object. Arg2 is the value to write.
#    Arg3 is the property name. Arg4: bool -> enumerable.
#    Arg1[Arg3] = Arg2;"
#
# Same shape as PutOwnByVal (which this codebase presumably already
# handles); the enumerable flag (Arg4) only affects the resulting
# property descriptor at runtime and has no separate JS surface syntax
# distinct from a computed assignment, so it's rendered as obj[key] = value.
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
            receiver=self.get_register_value(analysis, obj_reg),
            member=self.get_register_value(analysis, key_reg),
            computed=True,
        )
        right = self.get_register_value(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# DEFINE_OPCODE_5(DefineOwnGetterSetterByVal, Reg8, Reg8, Reg8, Reg8, UInt8)
#   [confirmed, hermes-dec table]
#
#   "Add a getter and a setter for a property by value.
#    Object.defineProperty(Arg1, Arg2, { get: Arg3, set: Arg4 }).
#    Arg1 is the target object. Arg2 is the property name.
#    Arg3 is the getter closure or undefined. Arg4 is the setter
#    closure or undefined. Arg5: boolean, enumerable."
#
# Rendered as an explicit Object.defineProperty(...) call, since there's
# no single JS literal syntax that captures "getter OR setter may be
# undefined" the way object literal get/set shorthand does.
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

        descriptor_props = {
            "get": self.get_register_value(analysis, getter_reg),
            "set": self.get_register_value(analysis, setter_reg),
            "enumerable": BooleanLiteral(value=bool(enumerable)),
        }

        # Expected type 'tuple[Expression | SpreadElement, ...]', got 'list[Expression | dict[str, Expression | BooleanLiteral]]' instead
        expression = CallExpression(
            callee=callee,
            arguments=[
                self.get_register_value(analysis, obj_reg),
                self.get_register_value(analysis, key_reg),
                descriptor_props,
            ],
        )

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# todo
# DefineOwnByIndex
# DefineOwnInDenseArray
