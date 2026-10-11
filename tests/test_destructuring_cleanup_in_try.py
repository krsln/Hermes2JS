"""
`ArrayDestructuringCfgPass` collapses a destructuring pattern and removes its
iterator-cleanup blocks from the CFG. A surrounding `try` (here the `for...of`
over the iterator) lists those blocks in its range too; they were only
removed from the handlers that guard the pattern itself, so the surrounding
handler kept CFG-less blocks, and the dominator analysis died with a
`KeyError` (98/5649 `extractPathFromURL`: "Code generation failed").
"""

from hermes_decompiler.Decompiler import Decompiler

_HASM = """
=> [Function #5649 "extractPathFromURL" of 548 bytes]: 3 params, frame size=39, strict=1, exc handler=1, debug info=0  @ offset 0x001b9054
  [Exception handlers: [start=0x188, end=0x18c, target=0x192] [start=0x4c, end=0x213, target=0x21b] ]

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 20, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 16, UInt8: 2>
==> 00000006: <LoadConstUndefined>: <Reg8: 0>
==> 00000008: <LoadConstUndefined>: <Reg8: 19>
==> 0000000a: <LoadConstUndefined>: <Reg8: 1>
==> 0000000c: <LoadConstUndefined>: <Reg8: 18>
==> 0000000e: <LoadConstUndefined>: <Reg8: 17>
==> 00000010: <LoadConstUndefined>: <Reg8: 3>
==> 00000012: <LoadParam>: <Reg8: 15, UInt8: 1>
==> 00000015: <IteratorBegin>: <Reg8: 2, Reg8: 15>
==> 00000018: <LoadConstString>: <Reg8: 14, string_id: 1865>  # String: '?' (String)
==> 0000001c: <GetGlobalObject>: <Reg8: 13>
==> 0000001e: <LoadConstString>: <Reg8: 12, string_id: 503>  # String: '/' (String)
==> 00000022: <LoadConstString>: <Reg8: 5, string_id: 6457>  # String: '' (Identifier)
==> 00000026: <LoadConstUInt8>: <Reg8: 10, UInt8: 1>
==> 00000029: <LoadConstString>: <Reg8: 9, string_id: 1693>  # String: '^' (String)
==> 0000002d: <LoadConstString>: <Reg8: 8, string_id: 840>  # String: '.' (String)
==> 00000031: <LoadConstString>: <Reg8: 7, string_id: 1900>  # String: '\\.' (String)
==> 00000035: <LoadConstString>: <Reg8: 6, string_id: 1168>  # String: '(/)*' (String)
==> 00000039: <LoadConstNull>: <Reg8: 4>
==> 0000003b: <Mov>: <Reg8: 21, Reg8: 15>
==> 0000003e: <IteratorNext>: <Reg8: 23, Reg8: 2, Reg8: 21>
==> 00000042: <Mov>: <Reg8: 21, Reg8: 2>
==> 00000045: <JStrictEqualLong>: <Addr32: 477, Reg8: 21, Reg8: 0>  # Address: 00000222
==> 0000004c: <Mov>: <Reg8: 19, Reg8: 23>
==> 0000004f: <GetByIdShort>: <Reg8: 22, Reg8: 23, UInt8: 0, string_id: 180>  # String: 'match' (Identifier)
==> 00000054: <CreateRegExp>: <Reg8: 21, string_id: 4591, string_id: 6457, UInt32: 90>  # String: '^[^:]+:' (String)  # String: '' (Identifier)
==> 00000062: <Call2>: <Reg8: 21, Reg8: 22, Reg8: 23, Reg8: 21>
==> 00000067: <Eq>: <Reg8: 22, Reg8: 21, Reg8: 4>
==> 0000006b: <LoadConstUndefined>: <Reg8: 24>
==> 0000006d: <JmpTrue>: <Addr8: 7, Reg8: 22>  # Address: 00000074
==> 00000070: <GetByIndex>: <Reg8: 24, Reg8: 21, UInt8: 0>
==> 00000074: <JNotEqual>: <Addr8: 7, Reg8: 24, Reg8: 4>  # Address: 0000007b
==> 00000078: <Mov>: <Reg8: 24, Reg8: 5>
==> 0000007b: <Mov>: <Reg8: 25, Reg8: 19>
==> 0000007e: <GetByIdShort>: <Reg8: 23, Reg8: 25, UInt8: 1, string_id: 217>  # String: 'replace' (Identifier)
==> 00000083: <TryGetById>: <Reg8: 27, Reg8: 13, UInt8: 2, string_id: 29>  # String: 'RegExp' (Identifier)
==> 00000089: <LoadFromEnvironment>: <Reg8: 21, Reg8: 20, UInt8: 0>
==> 0000008d: <GetByIdShort>: <Reg8: 22, Reg8: 21, UInt8: 3, string_id: 115>  # String: 'default' (Identifier)
==> 00000092: <Call2>: <Reg8: 26, Reg8: 22, Reg8: 0, Reg8: 24>
==> 00000097: <TryGetById>: <Reg8: 22, Reg8: 13, UInt8: 4, string_id: 10>  # String: 'HermesInternal' (Identifier)
==> 0000009d: <GetByIdShort>: <Reg8: 22, Reg8: 22, UInt8: 5, string_id: 105>  # String: 'concat' (Identifier)
==> 000000a2: <Call2>: <Reg8: 30, Reg8: 22, Reg8: 9, Reg8: 26>
==> 000000a7: <CreateThisForNew>: <Reg8: 26, Reg8: 27, UInt8: 6>
==> 000000ab: <Mov>: <Reg8: 31, Reg8: 26>
==> 000000ae: <Construct>: <Reg8: 22, Reg8: 27, UInt8: 2>
==> 000000b2: <SelectObject>: <Reg8: 22, Reg8: 26, Reg8: 22>
==> 000000b6: <Call3>: <Reg8: 25, Reg8: 23, Reg8: 25, Reg8: 22, Reg8: 5>
==> 000000bc: <GetByIdShort>: <Reg8: 23, Reg8: 25, UInt8: 1, string_id: 217>  # String: 'replace' (Identifier)
==> 000000c1: <CreateRegExp>: <Reg8: 22, string_id: 1678, string_id: 6578, UInt32: 11>  # String: '\\/+' (String)  # String: 'g' (Identifier)
==> 000000cf: <Call3>: <Reg8: 25, Reg8: 23, Reg8: 25, Reg8: 22, Reg8: 12>
==> 000000d5: <GetByIdShort>: <Reg8: 23, Reg8: 25, UInt8: 1, string_id: 217>  # String: 'replace' (Identifier)
==> 000000da: <CreateRegExp>: <Reg8: 22, string_id: 1676, string_id: 6457, UInt32: 86>  # String: '^\\/' (String)  # String: '' (Identifier)
==> 000000e8: <Call3>: <Reg8: 22, Reg8: 23, Reg8: 25, Reg8: 22, Reg8: 5>
==> 000000ee: <TryGetById>: <Reg8: 23, Reg8: 13, UInt8: 2, string_id: 29>  # String: 'RegExp' (Identifier)
==> 000000f4: <GetByIdShort>: <Reg8: 21, Reg8: 21, UInt8: 3, string_id: 115>  # String: 'default' (Identifier)
==> 000000f9: <Call2>: <Reg8: 24, Reg8: 21, Reg8: 0, Reg8: 24>
==> 000000fe: <GetByIdShort>: <Reg8: 21, Reg8: 22, UInt8: 7, string_id: 230>  # String: 'split' (Identifier)
==> 00000103: <Call2>: <Reg8: 25, Reg8: 21, Reg8: 22, Reg8: 8>
==> 00000108: <GetByIdShort>: <Reg8: 22, Reg8: 25, UInt8: 8, string_id: 126>  # String: 'map' (Identifier)
==> 0000010d: <CreateClosure>: <Reg8: 21, Reg8: 20, function_id: 10986>  # Function: [#10986  of 36 bytes]: 2 params @ offset 0x002215b5
==> 00000112: <Call2>: <Reg8: 22, Reg8: 22, Reg8: 25, Reg8: 21>
==> 00000117: <GetByIdShort>: <Reg8: 21, Reg8: 22, UInt8: 9, string_id: 167>  # String: 'join' (Identifier)
==> 0000011c: <Call2>: <Reg8: 22, Reg8: 21, Reg8: 22, Reg8: 7>
==> 00000121: <TryGetById>: <Reg8: 21, Reg8: 13, UInt8: 4, string_id: 10>  # String: 'HermesInternal' (Identifier)
==> 00000127: <GetByIdShort>: <Reg8: 21, Reg8: 21, UInt8: 5, string_id: 105>  # String: 'concat' (Identifier)
==> 0000012c: <Call4>: <Reg8: 30, Reg8: 21, Reg8: 9, Reg8: 24, Reg8: 6, Reg8: 22>
==> 00000133: <CreateThisForNew>: <Reg8: 22, Reg8: 23, UInt8: 6>
==> 00000137: <Mov>: <Reg8: 31, Reg8: 22>
==> 0000013a: <Construct>: <Reg8: 21, Reg8: 23, UInt8: 2>
==> 0000013e: <SelectObject>: <Reg8: 1, Reg8: 22, Reg8: 21>
==> 00000142: <GetByIdShort>: <Reg8: 21, Reg8: 16, UInt8: 7, string_id: 230>  # String: 'split' (Identifier)
==> 00000147: <Call2>: <Reg8: 21, Reg8: 21, Reg8: 16, Reg8: 14>
==> 0000014c: <Mov>: <Reg8: 25, Reg8: 21>
==> 0000014f: <IteratorBegin>: <Reg8: 23, Reg8: 25>
==> 00000152: <Mov>: <Reg8: 21, Reg8: 25>
==> 00000155: <IteratorNext>: <Reg8: 22, Reg8: 23, Reg8: 21>
==> 00000159: <Mov>: <Reg8: 21, Reg8: 23>
==> 0000015c: <StrictEq>: <Reg8: 24, Reg8: 21, Reg8: 0>
==> 00000160: <LoadConstUndefined>: <Reg8: 21>
==> 00000162: <JmpTrue>: <Addr8: 6, Reg8: 24>  # Address: 00000168
==> 00000165: <Mov>: <Reg8: 21, Reg8: 22>
==> 00000168: <Mov>: <Reg8: 18, Reg8: 21>
==> 0000016b: <NewArray>: <Reg8: 21, UInt16: 0>
==> 0000016f: <LoadConstZero>: <Reg8: 22>
==> 00000171: <JmpTrue>: <Addr8: 43, Reg8: 24>  # Address: 0000019c
==> 00000174: <Mov>: <Reg8: 24, Reg8: 25>
==> 00000177: <IteratorNext>: <Reg8: 27, Reg8: 23, Reg8: 24>
==> 0000017b: <Mov>: <Reg8: 24, Reg8: 23>
==> 0000017e: <StrictEq>: <Reg8: 24, Reg8: 24, Reg8: 0>
==> 00000182: <Mov>: <Reg8: 26, Reg8: 22>
==> 00000185: <JmpTrue>: <Addr8: 23, Reg8: 24>  # Address: 0000019c
==> 00000188: <PutByValStrict>: <Reg8: 21, Reg8: 26, Reg8: 27>
==> 0000018c: <AddN>: <Reg8: 22, Reg8: 26, Reg8: 10>
==> 00000190: <Jmp>: <Addr8: -28>  # Address: 00000174
==> 00000192: <Catch>: <Reg8: 22>
==> 00000194: <JmpTrue>: <Addr8: 6, Reg8: 24>  # Address: 0000019a
==> 00000197: <IteratorClose>: <Reg8: 23, UInt8: 1>
==> 0000019a: <Throw>: <Reg8: 22>
==> 0000019c: <Mov>: <Reg8: 17, Reg8: 21>
==> 0000019f: <Mov>: <Reg8: 24, Reg8: 18>
==> 000001a2: <GetByIdShort>: <Reg8: 23, Reg8: 24, UInt8: 1, string_id: 217>  # String: 'replace' (Identifier)
==> 000001a7: <CreateRegExp>: <Reg8: 22, string_id: 1678, string_id: 6578, UInt32: 11>  # String: '\\/+' (String)  # String: 'g' (Identifier)
==> 000001b5: <Call3>: <Reg8: 23, Reg8: 23, Reg8: 24, Reg8: 22, Reg8: 12>
==> 000001bb: <GetByIdShort>: <Reg8: 22, Reg8: 23, UInt8: 5, string_id: 105>  # String: 'concat' (Identifier)
==> 000001c0: <GetByIdShort>: <Reg8: 24, Reg8: 21, UInt8: 10, string_id: 177>  # String: 'length' (Identifier)
==> 000001c5: <Mov>: <Reg8: 21, Reg8: 5>
==> 000001c8: <JmpFalse>: <Addr8: 32, Reg8: 24>  # Address: 000001e8
==> 000001cb: <Mov>: <Reg8: 25, Reg8: 17>
==> 000001ce: <GetByIdShort>: <Reg8: 24, Reg8: 25, UInt8: 9, string_id: 167>  # String: 'join' (Identifier)
==> 000001d3: <Call2>: <Reg8: 25, Reg8: 24, Reg8: 25, Reg8: 14>
==> 000001d8: <TryGetById>: <Reg8: 24, Reg8: 13, UInt8: 4, string_id: 10>  # String: 'HermesInternal' (Identifier)
==> 000001de: <GetByIdShort>: <Reg8: 24, Reg8: 24, UInt8: 5, string_id: 105>  # String: 'concat' (Identifier)
==> 000001e3: <Call2>: <Reg8: 21, Reg8: 24, Reg8: 14, Reg8: 25>
==> 000001e8: <Call2>: <Reg8: 23, Reg8: 22, Reg8: 23, Reg8: 21>
==> 000001ed: <Mov>: <Reg8: 3, Reg8: 23>
==> 000001f0: <Mov>: <Reg8: 22, Reg8: 1>
==> 000001f3: <GetByIdShort>: <Reg8: 21, Reg8: 22, UInt8: 11, string_id: 47>  # String: 'test' (Identifier)
==> 000001f8: <Call2>: <Reg8: 21, Reg8: 21, Reg8: 22, Reg8: 23>
==> 000001fd: <JmpTrue>: <Addr8: 8, Reg8: 21>  # Address: 00000205
==> 00000200: <JmpLong>: <Addr32: -453>  # Address: 0000003b
==> 00000205: <Mov>: <Reg8: 4, Reg8: 3>
==> 00000208: <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 217>  # String: 'replace' (Identifier)
==> 0000020d: <Call3>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 5>
==> 00000213: <Mov>: <Reg8: 3, Reg8: 2>
==> 00000216: <IteratorClose>: <Reg8: 3, UInt8: 0>
==> 00000219: <Ret>: <Reg8: 1>
==> 0000021b: <Catch>: <Reg8: 1>
==> 0000021d: <IteratorClose>: <Reg8: 2, UInt8: 1>
==> 00000220: <Throw>: <Reg8: 1>
==> 00000222: <Ret>: <Reg8: 0>
"""


def test_a_surrounding_try_does_not_keep_the_removed_cleanup_blocks():
    out = Decompiler.render(Decompiler.build_context(_HASM, 5649), verbose=False)

    assert "function extractPathFromURL(" in out
