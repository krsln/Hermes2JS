"""
Two `Mov`s in a row each carry a merged value one level on
(`Mov r2, r0` at the end of an arm, then `Mov r1, r2` after it).

`UnfoldedMergeRepairPass` repoints the readers of an arm's value to the
register; the first repair hands the SAME replacement `r0` to both `Mov`s, and the
second repair then took that shared object for an ambiguous constant and gave up,
so `r1` kept an inlined `r5 != null` over a register reassigned on one path only.
"""

from hermes_decompiler.Decompiler import Decompiler

_IS_PUBLIC_INSTANCE_HASM = """
=> [Function #4129 "isPublicInstance" of 91 bytes]: 2 params, frame size=7, strict=1, exc handler=0, debug info=0  @ offset 0x0019b16d

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 5, UInt8: 1>
==> 00000003: <LoadConstNull>: <Reg8: 3>
==> 00000005: <Neq>: <Reg8: 1, Reg8: 5, Reg8: 3>
==> 00000009: <JmpFalse>: <Addr8: 80, Reg8: 1>  # Address: 00000059
==> 0000000c: <GetById>: <Reg8: 6, Reg8: 5, UInt8: 0, string_id: 10143>  # String: '__nativeTag' (Identifier)
==> 00000012: <Neq>: <Reg8: 2, Reg8: 6, Reg8: 3>
==> 00000016: <JmpTrue>: <Addr8: 64, Reg8: 2>  # Address: 00000056
==> 00000019: <Neq>: <Reg8: 0, Reg8: 5, Reg8: 3>
==> 0000001d: <JmpFalse>: <Addr8: 13, Reg8: 0>  # Address: 0000002a
==> 00000020: <GetById>: <Reg8: 6, Reg8: 5, UInt8: 1, string_id: 14991>  # String: '_internalInstanceHandle' (Identifier)
==> 00000026: <Neq>: <Reg8: 0, Reg8: 6, Reg8: 3>
==> 0000002a: <JmpFalse>: <Addr8: 18, Reg8: 0>  # Address: 0000003c
==> 0000002d: <GetById>: <Reg8: 6, Reg8: 5, UInt8: 1, string_id: 14991>  # String: '_internalInstanceHandle' (Identifier)
==> 00000033: <GetByIdShort>: <Reg8: 6, Reg8: 6, UInt8: 2, string_id: 233>  # String: 'stateNode' (Identifier)
==> 00000038: <Neq>: <Reg8: 0, Reg8: 6, Reg8: 3>
==> 0000003c: <JmpFalse>: <Addr8: 23, Reg8: 0>  # Address: 00000053
==> 0000003f: <GetById>: <Reg8: 5, Reg8: 5, UInt8: 1, string_id: 14991>  # String: '_internalInstanceHandle' (Identifier)
==> 00000045: <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 2, string_id: 233>  # String: 'stateNode' (Identifier)
==> 0000004a: <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 3, string_id: 98>  # String: 'canonical' (Identifier)
==> 0000004f: <Neq>: <Reg8: 0, Reg8: 5, Reg8: 3>
==> 00000053: <Mov>: <Reg8: 2, Reg8: 0>
==> 00000056: <Mov>: <Reg8: 1, Reg8: 2>
==> 00000059: <Ret>: <Reg8: 1>
"""


def _code(hasm, function_id):
    out = Decompiler.render(Decompiler.build_context(hasm, function_id), verbose=False)
    return "\n".join(line for line in out.splitlines() if not line.strip().startswith("//"))


def test_chained_movs_of_a_merged_value_name_the_registers_not_the_arm_value():
    # hermes-98 `isPublicInstance`
    code = _code(_IS_PUBLIC_INSTANCE_HASM, 4129)

    assert "r2 = r0;" in code
    assert "r1 = r2;" in code
    assert "r1 = r5 != null" not in code
    # the head definition the skipping path reads
    assert "r2 = param1.__nativeTag != null;" in code
