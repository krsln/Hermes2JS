"""
Readers after an `if` of the alias an arm's `Mov` made read the register
(`useReducer`, 96/2215):

    r2 = param2 (else) | r4 (then, and a nested `if`); store(r0, r2); store(r0, r2)

Both `PutById`s held the arm's alias `r4`, which is not what `r2` holds on the
path through the `else`. `UnfoldedMergeRepairPass` only repointed `Mov`
readers; any other reader kept the copy, and a second read got a fresh copy
the repair could not find.
"""

import re

from hermes_decompiler.Decompiler import Decompiler

_USE_REDUCER = r"""

=> [Function #2215 "useReducer" of 187 bytes]: 4 params, frame size=19, strict=1, exc handler=1, debug info=0  @ offset 0x0013333d
  [Exception handlers: [start=0x40, end=0x45, target=0xac] ]

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 2, UInt8: 3>
==> 00000003: <LoadParam>: <Reg8: 5, UInt8: 2>
==> 00000006: <Mov>: <Reg8: 6, Reg8: 2>
==> 00000009: <GetEnvironment>: <Reg8: 1, UInt8: 0>
==> 0000000c: <LoadFromEnvironmentL>: <Reg8: 0, Reg8: 1, UInt16: 331>
==> 00000011: <LoadConstUndefined>: <Reg8: 3>
==> 00000013: <Call1>: <Reg8: 0, Reg8: 0, Reg8: 3>
==> 00000017: <JStrictNotEqual>: <Addr8: 9, Reg8: 3, Reg8: 2>  # Address: 00000020
==> 0000001b: <Mov>: <Reg8: 2, Reg8: 5>
==> 0000001e: <Jmp>: <Addr8: 53>  # Address: 00000053
==> 00000020: <Mov>: <Reg8: 7, Reg8: 6>
==> 00000023: <Mov>: <Reg8: 4, Reg8: 5>
==> 00000026: <Call2>: <Reg8: 4, Reg8: 7, Reg8: 3, Reg8: 4>
==> 0000002b: <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 122>
==> 0000002f: <Mov>: <Reg8: 2, Reg8: 4>
==> 00000032: <JmpFalse>: <Addr8: 33, Reg8: 7>  # Address: 00000053
==> 00000035: <LoadFromEnvironment>: <Reg8: 8, Reg8: 1, UInt8: 237>
==> 00000039: <LoadConstTrue>: <Reg8: 7>
==> 0000003b: <Call2>: <Reg8: 7, Reg8: 8, Reg8: 3, Reg8: 7>
==> 00000040: <Call2>: <Reg8: 5, Reg8: 6, Reg8: 3, Reg8: 5>
==> 00000045: <LoadFromEnvironment>: <Reg8: 6, Reg8: 1, UInt8: 237>
==> 00000049: <LoadConstFalse>: <Reg8: 5>
==> 0000004b: <Call2>: <Reg8: 5, Reg8: 6, Reg8: 3, Reg8: 5>
==> 00000050: <Mov>: <Reg8: 2, Reg8: 4>
==> 00000053: <PutById>: <Reg8: 0, Reg8: 2, UInt8: 1, string_id: 70>  # String: 'baseState' (Identifier)
==> 00000059: <PutById>: <Reg8: 0, Reg8: 2, UInt8: 2, string_id: 173>  # String: 'memoizedState' (Identifier)
==> 0000005f: <NewObjectWithBuffer>: <Reg8: 4, UInt16: 5, UInt16: 3, UInt16: 647, UInt16: 28>  # Object: {'pending': null, 'lanes': 0, 'dispatch': null}
==> 00000069: <LoadConstNull>: <Reg8: 7>
==> 0000006b: <LoadParam>: <Reg8: 5, UInt8: 1>
==> 0000006e: <PutNewOwnById>: <Reg8: 4, Reg8: 5, string_id: 12727>  # String: 'lastRenderedReducer' (Identifier)
==> 00000073: <PutNewOwnById>: <Reg8: 4, Reg8: 2, string_id: 13876>  # String: 'lastRenderedState' (Identifier)
==> 00000078: <PutById>: <Reg8: 0, Reg8: 4, UInt8: 3, string_id: 208>  # String: 'queue' (Identifier)
==> 0000007e: <LoadFromEnvironmentL>: <Reg8: 6, Reg8: 1, UInt16: 366>
==> 00000083: <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 71>  # String: 'bind' (Identifier)
==> 00000088: <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 117>
==> 0000008c: <Call4>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 2, Reg8: 4>
==> 00000093: <PutById>: <Reg8: 4, Reg8: 2, UInt8: 4, string_id: 119>  # String: 'dispatch' (Identifier)
==> 00000099: <GetByIdShort>: <Reg8: 4, Reg8: 0, UInt8: 2, string_id: 173>  # String: 'memoizedState' (Identifier)
==> 0000009e: <NewArray>: <Reg8: 0, UInt16: 2>
==> 000000a2: <PutOwnByIndex>: <Reg8: 0, Reg8: 4, UInt8: 0>
==> 000000a6: <PutOwnByIndex>: <Reg8: 0, Reg8: 2, UInt8: 1>
==> 000000aa: <Ret>: <Reg8: 0>
==> 000000ac: <Catch>: <Reg8: 0>
==> 000000ae: <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 237>
==> 000000b2: <LoadConstFalse>: <Reg8: 1>
==> 000000b4: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
==> 000000b9: <Throw>: <Reg8: 0>
"""


def _render(hasm: str, function_id: int) -> str:
    context = Decompiler.build_context(hasm, function_id, strict=False)

    return Decompiler.render(context, verbose=False, raw=False)


def test_stores_after_the_merge_read_the_merged_register():
    js = _render(_USE_REDUCER, 2215)

    assert re.search(r"\br0\.baseState = r2;", js)
    assert re.search(r"\br0\.memoizedState = r2;", js)
