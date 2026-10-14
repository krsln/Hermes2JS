"""
A `for` header runs before the first iteration (`decode`, 96/7575):

    r1 = r1.length; if (1 < r1) { for (...; r2 < r1.length; ) { ...; r1 = r1.length } }

The bottom-tested loop reloads its bound (`r1 = r1.length`) right before the
compare, and the bound was folded into the condition. But the entry guard had
already replaced `r1` by that same length, so the header's first test read
`r1.length` of a NUMBER (`undefined`) and the loop never ran. The reload stays
a statement and the condition reads the register.
"""

from hermes_decompiler.Decompiler import Decompiler

_DECODE = r"""

=> [Function #7575 "decode" of 157 bytes]: 2 params, frame size=19, strict=1, exc handler=1, debug info=0  @ offset 0x001b4c67
  [Exception handlers: [start=0x9, end=0x19, target=0x1b] ]

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 0, UInt8: 1>
==> 00000003: <LoadConstUndefined>: <Reg8: 5>
==> 00000005: <LoadConstUndefined>: <Reg8: 6>
==> 00000007: <LoadConstUndefined>: <Reg8: 7>
==> 00000009: <GetGlobalObject>: <Reg8: 1>
==> 0000000b: <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 10229>  # String: 'decodeURIComponent' (Identifier)
==> 00000011: <Mov>: <Reg8: 1, Reg8: 0>
==> 00000014: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 1>
==> 00000019: <Ret>: <Reg8: 1>
==> 0000001b: <Catch>: <Reg8: 1>
==> 0000001d: <Mov>: <Reg8: 8, Reg8: 0>
==> 00000020: <GetByIdShort>: <Reg8: 3, Reg8: 8, UInt8: 2, string_id: 171>  # String: 'match' (Identifier)
==> 00000025: <GetEnvironment>: <Reg8: 4, UInt8: 0>
==> 00000028: <LoadFromEnvironment>: <Reg8: 2, Reg8: 4, UInt8: 0>
==> 0000002c: <Call2>: <Reg8: 2, Reg8: 3, Reg8: 8, Reg8: 2>
==> 00000031: <Mov>: <Reg8: 1, Reg8: 2>
==> 00000034: <JmpTrue>: <Addr8: 7, Reg8: 2>  # Address: 0000003b
==> 00000037: <NewArray>: <Reg8: 1, UInt16: 0>
==> 0000003b: <Mov>: <Reg8: 6, Reg8: 1>
==> 0000003e: <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
==> 00000041: <Mov>: <Reg8: 7, Reg8: 2>
==> 00000044: <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
==> 00000049: <LoadConstString>: <Reg8: 3, string_id: 7163>  # String: '' (Identifier)
==> 0000004d: <JNotLess>: <Addr8: 78, Reg8: 2, Reg8: 1>  # Address: 0000009b
==> 00000051: <LoadFromEnvironment>: <Reg8: 8, Reg8: 4, UInt8: 2>
==> 00000055: <Mov>: <Reg8: 2, Reg8: 6>
==> 00000058: <Mov>: <Reg8: 1, Reg8: 7>
==> 0000005b: <Call3>: <Reg8: 2, Reg8: 8, Reg8: 5, Reg8: 2, Reg8: 1>
==> 00000061: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 165>  # String: 'join' (Identifier)
==> 00000066: <Call2>: <Reg8: 9, Reg8: 1, Reg8: 2, Reg8: 3>
==> 0000006b: <Mov>: <Reg8: 0, Reg8: 9>
==> 0000006e: <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 171>  # String: 'match' (Identifier)
==> 00000073: <LoadFromEnvironment>: <Reg8: 2, Reg8: 4, UInt8: 0>
==> 00000077: <Call2>: <Reg8: 2, Reg8: 8, Reg8: 9, Reg8: 2>
==> 0000007c: <Mov>: <Reg8: 1, Reg8: 2>
==> 0000007f: <JmpTrue>: <Addr8: 7, Reg8: 2>  # Address: 00000086
==> 00000082: <NewArray>: <Reg8: 1, UInt16: 0>
==> 00000086: <Mov>: <Reg8: 6, Reg8: 1>
==> 00000089: <Mov>: <Reg8: 2, Reg8: 7>
==> 0000008c: <Inc>: <Reg8: 2, Reg8: 2>
==> 0000008f: <Mov>: <Reg8: 7, Reg8: 2>
==> 00000092: <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
==> 00000097: <JLess>: <Addr8: -70, Reg8: 2, Reg8: 1>  # Address: 00000051
==> 0000009b: <Ret>: <Reg8: 0>
"""


def _render() -> str:
    context = Decompiler.build_context(_DECODE, 7575, strict=False)

    return Decompiler.render(context, verbose=False, raw=False)


def test_header_does_not_read_length_of_a_length():
    js = _render()

    assert "r2 < r1.length" not in js
    assert "r2 < r1;" in js
    assert js.index("r1 = r1.length;\n        }") > js.index("r7 = r2;")

