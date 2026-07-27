from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, STRING_ID, sequence
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import AssignmentExpression, Identifier, MemberExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


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
            receiver=self.get_register_value(analysis, obj_reg),
            member=Identifier(name=property_name),
            computed=False,
        )

        right = self.get_register_value(analysis, value_reg)

        # No destination register (name=""): OpcodeResult/JSRenderer
        # already render a name-less Expression as a bare statement
        # (`obj.foo = value;`), same pattern as StoreToEnvironment.
        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


class PutByIdLong(PutById):
    pass


# PutByIdStrict / PutByIdLoose
#
# These are not present in the upstream facebook/hermes BytecodeList.def
# (they are variants that appear in some newer/forked Hermes bytecode
# versions, analogous to how DelById gained DelByIdStrict/DelByIdLoose
# and DelByVal gained DelByValStrict/DelByValLoose). Layout is assumed
# identical to PutById -- Reg8 obj, Reg8 value, UInt8 cache, UInt16/32
# string_id -- with the only difference being whether the runtime throws
# on a failed assignment (strict mode) or silently ignores it (loose
# mode). That distinction is a runtime semantic, not something that
# changes the decompiled JS source (`obj.foo = value;` either way), so
# both simply reuse PutById's handling.
class PutByIdStrict(PutById):
    pass


class PutByIdStrictLong(PutByIdStrict):
    pass


class PutByIdLoose(PutById):
    pass


class PutByIdLooseLong(PutByIdLoose):
    pass
