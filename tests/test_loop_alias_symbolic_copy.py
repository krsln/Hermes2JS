"""
The per-iteration copy of a `for` loop's counter (`Mov r1, r0` ... `i = r1 + 1`)
is merged into the counter even when loop-safety kept its read symbolic, so
the Mov carries `r0` itself rather than the initializer's literal
(`areInputsEqual`, 98/4378).
"""

import re

from hermes_decompiler.Decompiler import Decompiler

_HASM = """
=> [Function #4378 "areInputsEqual" of 113 bytes]: 3 params, frame size=22, strict=1, exc handler=0, debug info=0  @ offset 0x001a1d77

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 10, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 9, UInt8: 1>
==> 00000006: <LoadParam>: <Reg8: 8, UInt8: 2>
==> 00000009: <GetByIdShort>: <Reg8: 11, Reg8: 9, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 0000000e: <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 00000013: <JStrictNotEqual>: <Addr8: 90, Reg8: 11, Reg8: 7>  # Address: 0000006d
==> 00000017: <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 0000001c: <LoadConstZero>: <Reg8: 0>
==> 0000001e: <Less>: <Reg8: 3, Reg8: 0, Reg8: 7>
==> 00000022: <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
==> 00000025: <LoadConstTrue>: <Reg8: 4>
==> 00000027: <LoadConstUndefined>: <Reg8: 5>
==> 00000029: <LoadConstFalse>: <Reg8: 6>
==> 0000002b: <JmpFalse>: <Addr8: 64, Reg8: 3>  # Address: 0000006b
==> 0000002e: <GetByVal>: <Reg8: 12, Reg8: 9, Reg8: 0>
==> 00000032: <GetByVal>: <Reg8: 11, Reg8: 8, Reg8: 0>
==> 00000036: <Mov>: <Reg8: 1, Reg8: 0>
==> 00000039: <LoadConstTrue>: <Reg8: 3>
==> 0000003b: <JStrictEqual>: <Addr8: 30, Reg8: 12, Reg8: 11>  # Address: 00000059
==> 0000003f: <LoadFromEnvironment>: <Reg8: 7, Reg8: 10, UInt8: 0>
==> 00000043: <Call2>: <Reg8: 12, Reg8: 7, Reg8: 5, Reg8: 12>
==> 00000048: <LoadConstFalse>: <Reg8: 3>
==> 0000004a: <JmpFalse>: <Addr8: 15, Reg8: 12>  # Address: 00000059
==> 0000004d: <Call2>: <Reg8: 7, Reg8: 7, Reg8: 5, Reg8: 11>
==> 00000052: <LoadConstFalse>: <Reg8: 3>
==> 00000054: <JmpFalse>: <Addr8: 5, Reg8: 7>  # Address: 00000059
==> 00000057: <LoadConstTrue>: <Reg8: 3>
==> 00000059: <JmpTrue>: <Addr8: 5, Reg8: 3>  # Address: 0000005e
==> 0000005c: <Ret>: <Reg8: 6>
==> 0000005e: <AddN>: <Reg8: 0, Reg8: 1, Reg8: 2>
==> 00000062: <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 00000067: <JLess>: <Addr8: -57, Reg8: 0, Reg8: 7>  # Address: 0000002e
==> 0000006b: <Ret>: <Reg8: 4>
==> 0000006d: <LoadConstFalse>: <Reg8: 4>
==> 0000006f: <Ret>: <Reg8: 4>


"""


def test_symbolic_counter_copy_is_merged_into_the_counter():
    js = Decompiler.render(Decompiler.build_context(_HASM, 4378, strict=False), verbose=False, raw=False)

    assert "for (i = 0; i < param1.length; i++) {" in js
    assert "r1 = i;" not in js
    assert not re.search(r"\br1\b", js)
