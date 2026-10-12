"""
A counting-down loop's entry guard repeats the loop's own test, so the
counter's first value (`r0 = n - 1`) sits in front of the guard and the loop
used to print `for (; 0 <= i; ...)` with `i` never assigned
(`_ensureClosestStickyHeader`, 98/4260).
`LoopGuardInitializerPass` moves it into the header and drops the guard.
"""

import re

from hermes_decompiler.Decompiler import Decompiler

_HASM = """
=> [Function #4260 "_ensureClosestStickyHeader" of 98 bytes]: 5 params, frame size=19, strict=1, exc handler=0, debug info=0  @ offset 0x0019de06

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 7, UInt8: 2>
==> 00000003: <LoadParam>: <Reg8: 8, UInt8: 1>
==> 00000006: <GetById>: <Reg8: 8, Reg8: 8, UInt8: 0, string_id: 11193>  # String: 'ListHeaderComponent' (Identifier)
==> 0000000c: <LoadConstZero>: <Reg8: 4>
==> 0000000e: <LoadConstZero>: <Reg8: 2>
==> 00000010: <JmpFalse>: <Addr8: 6, Reg8: 8>  # Address: 00000016
==> 00000013: <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
==> 00000016: <LoadParam>: <Reg8: 8, UInt8: 4>
==> 00000019: <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
==> 0000001c: <Sub>: <Reg8: 0, Reg8: 8, Reg8: 3>
==> 00000020: <JNotLessEqualN>: <Addr8: 62, Reg8: 4, Reg8: 0>  # Address: 0000005e
==> 00000024: <GetByIdShort>: <Reg8: 8, Reg8: 7, UInt8: 1, string_id: 11>  # String: 'has' (Identifier)
==> 00000029: <AddN>: <Reg8: 1, Reg8: 0, Reg8: 2>
==> 0000002d: <Call2>: <Reg8: 8, Reg8: 8, Reg8: 7, Reg8: 1>
==> 00000032: <Mov>: <Reg8: 1, Reg8: 0>
==> 00000035: <JmpTrue>: <Addr8: 13, Reg8: 8>  # Address: 00000042
==> 00000038: <SubN>: <Reg8: 0, Reg8: 1, Reg8: 3>
==> 0000003c: <JLessEqualN>: <Addr8: -24, Reg8: 4, Reg8: 0>  # Address: 00000024
==> 00000040: <Jmp>: <Addr8: 30>  # Address: 0000005e
==> 00000042: <LoadParam>: <Reg8: 9, UInt8: 3>
==> 00000045: <GetById>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 8963>  # String: 'addCells' (Identifier)
==> 0000004b: <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1108, UInt16: 17356>  # Object: {'first': null, 'last': null}
==> 00000051: <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 1, UInt8: 0>
==> 00000055: <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 1, UInt8: 1>
==> 00000059: <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
==> 0000005e: <LoadConstUndefined>: <Reg8: 6>
==> 00000060: <Ret>: <Reg8: 6>


"""


def test_guarded_countdown_loop_gets_its_initializer():
    js = Decompiler.render(Decompiler.build_context(_HASM, 4260, strict=False), verbose=False, raw=False)

    assert "for (i = param4 - 1; 0 <= i; i--) {" in js
    assert "if (0 <= r0)" not in js
    assert not re.search(r"\br0\b", js)
    assert not re.search(r"\br1 = i;", js)
