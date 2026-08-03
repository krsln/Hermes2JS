from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, STRING_ID, sequence
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression, Identifier, MemberExpression
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt8, UInt16 (string_id) (total size 5)
# Example: <PutById>: <Reg8: 10, Reg8: 2, UInt8: 3, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
class PutById(OpcodeHandler):
    """
    Put object property by identifier.

    Hermes:
        PutById rObj, rValue, cache, string_id

    JavaScript:
        rObj.foo = rValue;
    """

    _PATTERN = sequence(REG, REG, UINT8, STRING_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        obj_reg, value_reg, _cache, string_id = map(int, match.groups())

        property_name = (entry.identifier_name or f"string_{string_id}")

        left = MemberExpression(
            receiver=self.get_register_expression(analysis, obj_reg),
            member=Identifier(name=property_name),
            computed=False,
        )

        right = self.get_register_expression(analysis, value_reg)

        # No destination register (name=""): OpcodeResult/JSRenderer
        # already render a name-less Expression as a bare statement
        # (`obj.foo = value;`), same pattern as StoreToEnvironment.
        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, Reg8, UInt8, UInt32 (string_id) (total size 7)
# Example:
class PutByIdLong(PutById):
    pass


# Reg8, Reg8, UInt8, UInt16 (string_id) (total size 5)
# DEFINE_OPCODE_4(PutByIdStrict, Reg8, Reg8, UInt8, UInt16)
# Example: <PutByIdStrict>: <Reg8: 0, Reg8: 1, UInt8: 0, string_id: 186>  # String: 'name' (Identifier)
class PutByIdStrict(PutById):
    pass


# Reg8, Reg8, UInt8, UInt32 (string_id) (total size 7)
# DEFINE_OPCODE_4(PutByIdStrictLong, Reg8, Reg8, UInt8, UInt32)
# Example:
class PutByIdStrictLong(PutByIdStrict):
    pass


# Reg8, Reg8, UInt8, UInt16 (string_id) (total size 5)
# DEFINE_OPCODE_4(PutByIdLoose, Reg8, Reg8, UInt8, UInt16)
# Example: <PutByIdLoose>: <Reg8: 1, Reg8: 2, UInt8: 0, string_id: 140>  # String: 'exports' (Identifier)
class PutByIdLoose(PutById):
    pass


# Reg8, Reg8, UInt8, UInt32 (string_id) (total size 7)
# DEFINE_OPCODE_4(PutByIdLooseLong, Reg8, Reg8, UInt8, UInt32)
# Example:
class PutByIdLooseLong(PutByIdLoose):
    pass

# TryPutById
# TryPutByIdLong
# TryPutByIdLoose
# TryPutByIdLooseLong
# TryPutByIdStrict
# TryPutByIdStrictLong
