from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression, MemberExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# All three confirmed directly from facebook/hermes BytecodeList.def,
# tag hermes-v260318099.0.1 (newer than any version indexed by the
# hermes-dec table or hermes_rs's v76-v96 defs used earlier in this
# session).
#
# All three operate on private class fields (`#x`), where the property
# key is a Symbol value sitting in a register (produced earlier by
# CreatePrivateName) rather than a compile-time string_id -- that's why
# these take a Reg8 "symbol value" operand instead of the
# UInt8+string_id pair GetById/PutById use. Since `#x` syntax is only
# valid inside the class body it was declared in and always resolves
# to a fixed textual name, all three render as plain
# `obj.#fieldName` member access/assignment -- the same simplification
# already applied to DefineOwnById vs. PutById (fresh-property vs.
# through-prototype-chain is a runtime distinction with no separate JS
# surface syntax).
#
# The private-name Symbol register's origin (a CreatePrivateName result
# for a class field named e.g. "x") would need to be traced back for a
# fully accurate `#x` label; `entry.identifier_name` is used as a
# best-effort resolution consistent with how other opcodes in this
# codebase (GetById, PutById, DefineOwnById) resolve their `string_id`/
# name operands, with a placeholder fallback.


# DEFINE_OPCODE_3(AddOwnPrivateBySym, Reg8, Reg8, Reg8)
#
#   "Add a private property to an object. This must be a new property.
#    The property will be added with the privateName flag set on the
#    PropertyFlags.
#    Arg1[Arg2] = Arg3"
#
# NOTE the operand order here is (obj, private_name_symbol, value) --
# different from GetOwnPrivateBySym/PutOwnPrivateBySym below, which
# both put the private-name symbol register *last*. This one puts it
# in Arg2, matching field-initialization call sites where the object
# and the about-to-be-added field are adjacent.
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
            member=RawPrivateName(field_name),
            computed=False,
        )
        right = self.get_register_value(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# DEFINE_OPCODE_4(GetOwnPrivateBySym, Reg8, Reg8, UInt8, Reg8)
#
#   "Get a private property from an object.
#    Arg1 = Arg2[Arg4]
#    Arg1 is the result.
#    Arg2 is the object to read from.
#    Arg3 is a private name cache index used to speed up the above operation.
#    Arg4 is the symbol value of the private name."
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
            member=RawPrivateName(field_name),
            computed=False,
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# DEFINE_OPCODE_4(PutOwnPrivateBySym, Reg8, Reg8, UInt8, Reg8)
#
#   "Store a private property to an object.
#    Arg1[Arg4] = Arg2
#    Arg1 is the object to store to.
#    Arg2 is the value to store.
#    Arg3 is a private name cache index used to speed up the above operation.
#    Arg4 is the symbol value of the private name."
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
            member=RawPrivateName(field_name),
            computed=False,
        )
        right = self.get_register_value(analysis, value_reg)

        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# NOTE: `RawPrivateName` is used above as a placeholder for rendering
# `#fieldName` as the member of a MemberExpression -- `Identifier` in
# this codebase's IR presumably renders as a bare identifier
# (`fieldName`), not one prefixed with `#`. Neither Access.py,
# Literals.py, nor Operations.py (the three IR files reviewed earlier
# in this session) define a private-name-aware node. If no such class
# exists yet in ir/expressions, this needs one of:
#   (a) a new `PrivateName(name: str)` IR node that the renderer prints
#       as `#name`, or
#   (b) reusing `Identifier(name=f"#{field_name}")` directly if the
#       renderer doesn't validate identifier characters.
# Using (b) inline below to avoid inventing an unconfirmed class name;
# swap for a dedicated node if this codebase adds one.
def RawPrivateName(name: str):
    from hermes_decompiler.ir.expressions import Identifier

    return Identifier(name=f"#{name}")
