from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, STRING_ID, sequence
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
#
# NOTE: `ObjectExpression`/`Property` names are inferred from common
# ESTree-style IR conventions used elsewhere in this codebase (e.g.
# MemberExpression, AssignmentExpression). Verify these exact class
# names/constructor kwargs exist in hermes_decompiler.ir.expressions
# before relying on this -- if they're named differently (or don't
# exist yet), this is the piece to adjust. Unlike Literal/UnaryExpression
# (which I could check against the files you attached), I have not seen
# the source for these two classes, so they're still unverified.
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
                    value=self.get_register_value(analysis, getter_reg),
                    shorthand=False,
                    computed=False,
                ),
                ObjectProperty(
                    key=Identifier(name="set"),
                    value=self.get_register_value(analysis, setter_reg),
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
                self.get_register_value(analysis, obj_reg),
                self.get_register_value(analysis, key_reg),
                descriptor,
            ),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# DEFINE_OPCODE_3(DefineOwnByIndex, Reg8, Reg8, UInt8)   [confirmed, hermes-dec table]
# DEFINE_OPCODE_3(DefineOwnByIndexL, Reg8, Reg8, UInt32)
#
#   "Assign a value to a constant integer own property which will be
#    created as enumerable. This is used (potentially in conjunction
#    with NewArrayWithBuffer) for arr=[foo,bar] initializations.
#    Arg1[Arg3] = Arg2;"
#
# Note the args are: Arg1 = destination array/object, Arg2 = value,
# Arg3 = the (immediate) integer index -- i.e. the *index* is baked
# into the bytecode as UInt8/UInt32, not read from a register, unlike
# DefineOwnByVal above. This is essentially the "own" counterpart to
# PutOwnByIndex, used when populating array-literal elements that
# couldn't be captured statically in the array buffer table.
#
# FIX vs. earlier draft: `Literal` (in Literals.py) is declared
# `class Literal(Expression, ABC)` -- it's an abstract base class with
# no `value` field of its own, so `Literal(value=index)` can't be
# instantiated at all. The concrete subclass for a plain JS number is
# `NumericLiteral(value=...)`.
class DefineOwnByIndex(OpcodeHandler):
    """Define an own indexed property: arr[N] = value (N is an immediate index)."""

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, UInt8 arguments")

        obj_reg, value_reg, index = map(int, match.groups())

        left = MemberExpression(
            receiver=self.get_register_value(analysis, obj_reg),
            member=NumericLiteral(value=index),
            computed=True,
        )
        right = self.get_register_value(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


class DefineOwnByIndexL(DefineOwnByIndex):
    pass


# DEFINE_OPCODE_3(DefineOwnInDenseArray, Reg8, Reg8, UInt8)   [confirmed, hermes-dec table]
# DEFINE_OPCODE_4(DefineOwnInDenseArrayL, Reg8, Reg8, UInt16)
#
#   "Define an own property in a dense JavaScript array at a specific
#    index. Requires that the array is dense and that the ArrayStorage
#    underlying it has a size which is greater than the arrayIndex
#    operand. Arg1[Arg3] = Arg2; Arg1 is the dense array object where
#    the property will be defined. Arg2 is the value to be stored.
#    Arg3 is the array index where the property will be stored. NOTE:
#    the 'L' version only goes up to 16-bit array indices, because
#    NewArray only takes UInt16 argument."
#
# Functionally identical rendering to DefineOwnByIndex (`arr[N] =
# value`) -- the distinction (dense-array-storage fast path vs. generic
# own-property definition) is a Hermes runtime optimization detail with
# no separate JS syntax.
#
# Same `Literal` -> `NumericLiteral` fix as DefineOwnByIndex above.
#
# NOTE: per the doc comment, the "L" (long) variant here is UInt16, not
# UInt32 like most other *L/*Long opcodes in this file -- verify that
# matches your actual bytecode stream before assuming the same UINT8
# token width works; may need a UInt16-specific pattern token.
class DefineOwnInDenseArray(OpcodeHandler):
    """Define an own property directly in dense array storage: arr[N] = value."""

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, UInt8 arguments")

        obj_reg, value_reg, index = map(int, match.groups())

        left = MemberExpression(
            receiver=self.get_register_value(analysis, obj_reg),
            member=NumericLiteral(value=index),
            computed=True,
        )
        right = self.get_register_value(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


class DefineOwnInDenseArrayL(DefineOwnInDenseArray):
    pass
