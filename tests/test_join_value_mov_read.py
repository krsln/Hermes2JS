"""
A `Mov` that reads a join value reads the register (`retryTimedOutBoundary`,
98/2683):

    r3 = 2; if (c) { r4 = ...; r3 = r4; if (d) { ...; r3 = r4 } }; Mov r8, r3

The arm's `Mov r3, r4` is not printed (inlined), so the reader after the `if`
held the arm's value (`r8 = r4`) and was wrong on the path that skips the arm.
"""

import re

from hermes_decompiler.Decompiler import Decompiler

_HASM = """
=> [Function #2683 "retryTimedOutBoundary" of 261 bytes]: 3 params, frame size=20, strict=1, exc handler=0, debug info=0  @ offset 0x0017b781

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 6, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 9, UInt8: 1>
==> 00000006: <LoadParam>: <Reg8: 8, UInt8: 2>
==> 00000009: <LoadConstZero>: <Reg8: 2>
==> 0000000b: <JStrictNotEqual>: <Addr8: 68, Reg8: 2, Reg8: 8>  # Address: 0000004f
==> 0000000f: <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 0, string_id: 185>  # String: 'mode' (Identifier)
==> 00000014: <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
==> 00000017: <BitAnd>: <Reg8: 1, Reg8: 7, Reg8: 0>
==> 0000001b: <LoadConstUInt8>: <Reg8: 3, UInt8: 2>
==> 0000001e: <JStrictEqual>: <Addr8: 46, Reg8: 2, Reg8: 1>  # Address: 0000004c
==> 00000022: <LoadFromEnvironment>: <Reg8: 4, Reg8: 6, UInt8: 91>
==> 00000026: <LShift>: <Reg8: 1, Reg8: 4, Reg8: 0>
==> 0000002a: <StoreNPToEnvironment>: <Reg8: 6, UInt8: 91, Reg8: 1>
==> 0000002e: <LoadConstInt>: <Reg8: 0, Imm32: 62914560>
==> 00000034: <BitAnd>: <Reg8: 0, Reg8: 1, Reg8: 0>
==> 00000038: <Mov>: <Reg8: 3, Reg8: 4>
==> 0000003b: <JStrictNotEqual>: <Addr8: 17, Reg8: 2, Reg8: 0>  # Address: 0000004c
==> 0000003f: <LoadConstInt>: <Reg8: 0, Imm32: 4194304>
==> 00000045: <StoreNPToEnvironment>: <Reg8: 6, UInt8: 91, Reg8: 0>
==> 00000049: <Mov>: <Reg8: 3, Reg8: 4>
==> 0000004c: <Mov>: <Reg8: 8, Reg8: 3>
==> 0000004f: <LoadFromEnvironment>: <Reg8: 7, Reg8: 6, UInt8: 162>
==> 00000053: <Call3>: <Reg8: 7, Reg8: 7, Reg8: 2, Reg8: 9, Reg8: 8>
==> 00000059: <LoadConstNull>: <Reg8: 3>
==> 0000005b: <JStrictEqualLong>: <Addr32: 166, Reg8: 3, Reg8: 7>  # Address: 00000101
==> 00000062: <GetById>: <Reg8: 9, Reg8: 7, UInt8: 1, string_id: 13574>  # String: 'pendingLanes' (Identifier)
==> 00000068: <BitOr>: <Reg8: 9, Reg8: 9, Reg8: 8>
==> 0000006c: <PutByIdStrict>: <Reg8: 7, Reg8: 9, UInt8: 0, string_id: 13574>  # String: 'pendingLanes' (Identifier)
==> 00000072: <LoadConstInt>: <Reg8: 0, Imm32: 268435456>
==> 00000078: <JStrictEqual>: <Addr8: 22, Reg8: 0, Reg8: 8>  # Address: 0000008e
==> 0000007c: <PutByIdStrict>: <Reg8: 7, Reg8: 2, UInt8: 1, string_id: 13523>  # String: 'suspendedLanes' (Identifier)
==> 00000082: <PutByIdStrict>: <Reg8: 7, Reg8: 2, UInt8: 2, string_id: 15552>  # String: 'pingedLanes' (Identifier)
==> 00000088: <PutByIdStrict>: <Reg8: 7, Reg8: 2, UInt8: 3, string_id: 9441>  # String: 'warmLanes' (Identifier)
==> 0000008e: <LoadFromEnvironment>: <Reg8: 8, Reg8: 6, UInt8: 125>
==> 00000092: <StrictNeq>: <Reg8: 4, Reg8: 7, Reg8: 8>
==> 00000096: <JmpFalse>: <Addr8: 12, Reg8: 4>  # Address: 000000a2
==> 00000099: <GetByIdShort>: <Reg8: 8, Reg8: 7, UInt8: 2, string_id: 62>  # String: 'next' (Identifier)
==> 0000009e: <StrictEq>: <Reg8: 4, Reg8: 3, Reg8: 8>
==> 000000a2: <JmpFalse>: <Addr8: 31, Reg8: 4>  # Address: 000000c1
==> 000000a5: <LoadFromEnvironment>: <Reg8: 8, Reg8: 6, UInt8: 125>
==> 000000a9: <JStrictEqual>: <Addr8: 16, Reg8: 3, Reg8: 8>  # Address: 000000b9
==> 000000ad: <PutByIdStrict>: <Reg8: 8, Reg8: 7, UInt8: 4, string_id: 62>  # String: 'next' (Identifier)
==> 000000b3: <StoreToEnvironment>: <Reg8: 6, UInt8: 125, Reg8: 7>
==> 000000b7: <Jmp>: <Addr8: 10>  # Address: 000000c1
==> 000000b9: <StoreToEnvironment>: <Reg8: 6, UInt8: 125, Reg8: 7>
==> 000000bd: <StoreToEnvironment>: <Reg8: 6, UInt8: 124, Reg8: 7>
==> 000000c1: <LoadConstTrue>: <Reg8: 3>
==> 000000c3: <StoreNPToEnvironment>: <Reg8: 6, UInt8: 127, Reg8: 3>
==> 000000c7: <LoadFromEnvironment>: <Reg8: 4, Reg8: 6, UInt8: 126>
==> 000000cb: <JmpTrue>: <Addr8: 54, Reg8: 4>  # Address: 00000101
==> 000000ce: <StoreNPToEnvironment>: <Reg8: 6, UInt8: 126, Reg8: 3>
==> 000000d2: <LoadFromEnvironmentL>: <Reg8: 3, Reg8: 6, UInt16: 389>
==> 000000d7: <JmpTrue>: <Addr8: 25, Reg8: 3>  # Address: 000000f0
==> 000000da: <LoadFromEnvironment>: <Reg8: 9, Reg8: 6, UInt8: 72>
==> 000000de: <LoadFromEnvironment>: <Reg8: 8, Reg8: 6, UInt8: 77>
==> 000000e2: <LoadFromEnvironment>: <Reg8: 7, Reg8: 6, UInt8: 132>
==> 000000e6: <LoadConstUndefined>: <Reg8: 3>
==> 000000e8: <Call3>: <Reg8: 7, Reg8: 9, Reg8: 3, Reg8: 8, Reg8: 7>
==> 000000ee: <Jmp>: <Addr8: 19>  # Address: 00000101
==> 000000f0: <LoadFromEnvironmentL>: <Reg8: 7, Reg8: 6, UInt16: 390>
==> 000000f5: <LoadConstUndefined>: <Reg8: 3>
==> 000000f7: <CreateClosure>: <Reg8: 6, Reg8: 6, function_id: 9765>  # Function: [#9765  of 222 bytes]: 1 params @ offset 0x002087d0
==> 000000fc: <Call2>: <Reg8: 6, Reg8: 7, Reg8: 3, Reg8: 6>
==> 00000101: <LoadConstUndefined>: <Reg8: 3>
==> 00000103: <Ret>: <Reg8: 3>


"""


def test_mov_after_if_reads_the_merged_register():
    context = Decompiler.build_context(_HASM, 2683, strict=False)
    js = Decompiler.render(context, verbose=False, raw=False)

    assert re.search(r"\br8 = r3;", js)
    assert not re.search(r"\br8 = r4;\n\s*}\n\s*r7 = ", js)
