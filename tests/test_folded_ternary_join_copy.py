"""
A ternary folded inside the arm of an outer `if` must not turn the join's
copy (`Mov r0, r1`, read after the `if`) into a copy of the ternary: on the
path that skips the arm `r1` still holds its earlier value (96/1853):

    r1 = 8;  if (8 < r3) { ... r1 = c ? a : b; }  r0 = r1;
"""

from hermes_decompiler.Decompiler import Decompiler

_HASM = r"""
=> [Function #1853 "lanesToEventPriority" of 57 bytes]: 2 params, frame size=5, strict=1, exc handler=0, debug info=0  @ offset 0x001228e0

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <Negate>: <Reg8: 0, Reg8: 1>
==> 00000006: <BitAnd>: <Reg8: 3, Reg8: 1, Reg8: 0>
==> 0000000a: <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
==> 0000000d: <JNotLess>: <Addr8: 42, Reg8: 0, Reg8: 3>  # Address: 00000037
==> 00000011: <LoadConstUInt8>: <Reg8: 1, UInt8: 8>
==> 00000014: <JNotLess>: <Addr8: 32, Reg8: 1, Reg8: 3>  # Address: 00000034
==> 00000018: <LoadConstInt>: <Reg8: 2, Imm32: 134217727>
==> 0000001e: <BitAnd>: <Reg8: 4, Reg8: 3, Reg8: 2>
==> 00000022: <LoadConstInt>: <Reg8: 2, Imm32: 268435456>
==> 00000028: <LoadConstZero>: <Reg8: 3>
==> 0000002a: <JStrictEqual>: <Addr8: 7, Reg8: 3, Reg8: 4>  # Address: 00000031
==> 0000002e: <LoadConstUInt8>: <Reg8: 2, UInt8: 32>
==> 00000031: <Mov>: <Reg8: 1, Reg8: 2>
==> 00000034: <Mov>: <Reg8: 0, Reg8: 1>
==> 00000037: <Ret>: <Reg8: 0>
"""


def test_join_copy_after_a_folded_ternary_still_reads_the_register():
    js = Decompiler.render(Decompiler.build_context(_HASM, 1853, strict=False), verbose=False, raw=False)

    assert "r1 = 8;" in js
    assert "r0 = r1;" in js
    assert "r0 = (r3 === r4)" not in js
