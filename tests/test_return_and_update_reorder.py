"""
`decode` (96/7575): a `Inc r2, r2` whose result a later `Mov r7, r2` reads, and a
`return r0` that `Mov r0, r9` (inside the loop) and `LoadParam r0` both reach.

* The update was pulled into the `for` header, i.e. moved after the `Mov` that
  stores the incremented value (`r7 = r2` then stored the OLD counter).
* `ReturnValueResolutionPass` walked back from `return r0`, never saw the path
  through the handler (no predecessor edge), found only `Mov r0, r9` and printed
  `return r9`, skipping the zero-iteration path where `r0` is the parameter.
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


def test_update_is_not_moved_past_a_reader_of_the_incremented_value():
    js = _render()

    # The increment stays ahead of the statement that stores it.
    assert js.index("r2 = r2 + 1;") < js.index("r7 = r2;")


def test_return_names_a_register_some_paths_never_rewrote():
    js = _render()

    assert "return r9;" not in js
    assert "return r0;" in js
    assert "r0 = r9;" in js
