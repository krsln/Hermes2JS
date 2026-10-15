"""
A register a loop overwrites and the code after the loop reads by name
(`makeSafeRegex`, 96/9342):

    r0 = param1;  for (const x of xs) { r0 = r17.join(...); }  return r0;

The `LoadParam` alias was folded into its readers and never printed, so when the
loop ran zero times (or skipped the write) `return r0` read a register nothing
had assigned. `LoopCarriedDefinitionPass` prints the pre-loop definition.
"""

from hermes_decompiler.Decompiler import Decompiler

_MAKE_SAFE_REGEX = r"""

=> [Function #9342 "makeSafeRegex" of 232 bytes]: 2 params, frame size=31, strict=1, exc handler=1, debug info=0  @ offset 0x001dc3c3
  [Exception handlers: [start=0x42, end=0xda, target=0xdf] ]

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 0, UInt8: 1>
==> 00000003: <GetEnvironment>: <Reg8: 14, UInt8: 0>
==> 00000006: <LoadFromEnvironment>: <Reg8: 1, Reg8: 14, UInt8: 8>
==> 0000000a: <Mov>: <Reg8: 13, Reg8: 1>
==> 0000000d: <IteratorBegin>: <Reg8: 2, Reg8: 13>
==> 00000010: <LoadConstUndefined>: <Reg8: 12>
==> 00000012: <LoadConstUInt8>: <Reg8: 11, UInt8: 2>
==> 00000015: <LoadConstZero>: <Reg8: 10>
==> 00000017: <LoadConstUInt8>: <Reg8: 9, UInt8: 1>
==> 0000001a: <GetGlobalObject>: <Reg8: 8>
==> 0000001c: <LoadConstString>: <Reg8: 7, string_id: 7163>  # String: '' (Identifier)
==> 00000020: <LoadConstString>: <Reg8: 6, string_id: 1490>  # String: '*' (String)
==> 00000024: <LoadConstString>: <Reg8: 5, string_id: 4455>  # String: '{0,' (String)
==> 00000028: <LoadConstString>: <Reg8: 4, string_id: 599>  # String: '}' (String)
==> 0000002c: <LoadConstString>: <Reg8: 3, string_id: 316>  # String: '+' (String)
==> 00000030: <LoadConstString>: <Reg8: 1, string_id: 1924>  # String: '{1,' (String)
==> 00000034: <IteratorNext>: <Reg8: 16, Reg8: 2, Reg8: 13>
==> 00000038: <Mov>: <Reg8: 15, Reg8: 2>
==> 0000003b: <JStrictEqualLong>: <Addr32: 171, Reg8: 15, Reg8: 12>  # Address: 000000e6
==> 00000042: <LoadFromEnvironment>: <Reg8: 15, Reg8: 14, UInt8: 0>
==> 00000046: <Call3>: <Reg8: 15, Reg8: 15, Reg8: 12, Reg8: 16, Reg8: 11>
==> 0000004c: <GetByVal>: <Reg8: 19, Reg8: 15, Reg8: 10>
==> 00000050: <GetByVal>: <Reg8: 18, Reg8: 15, Reg8: 9>
==> 00000054: <Mov>: <Reg8: 17, Reg8: 0>
==> 00000057: <GetByIdShort>: <Reg8: 16, Reg8: 17, UInt8: 1, string_id: 229>  # String: 'split' (Identifier)
==> 0000005c: <TryGetById>: <Reg8: 15, Reg8: 8, UInt8: 2, string_id: 14>  # String: 'HermesInternal' (Identifier)
==> 00000062: <GetByIdShort>: <Reg8: 15, Reg8: 15, UInt8: 3, string_id: 96>  # String: 'concat' (Identifier)
==> 00000067: <Call3>: <Reg8: 15, Reg8: 15, Reg8: 7, Reg8: 19, Reg8: 6>
==> 0000006d: <Call2>: <Reg8: 17, Reg8: 16, Reg8: 17, Reg8: 15>
==> 00000072: <GetByIdShort>: <Reg8: 16, Reg8: 17, UInt8: 4, string_id: 165>  # String: 'join' (Identifier)
==> 00000077: <TryGetById>: <Reg8: 15, Reg8: 8, UInt8: 2, string_id: 14>  # String: 'HermesInternal' (Identifier)
==> 0000007d: <GetByIdShort>: <Reg8: 15, Reg8: 15, UInt8: 3, string_id: 96>  # String: 'concat' (Identifier)
==> 00000082: <Mov>: <Reg8: 24, Reg8: 7>
==> 00000085: <Mov>: <Reg8: 23, Reg8: 19>
==> 00000088: <Mov>: <Reg8: 22, Reg8: 5>
==> 0000008b: <Mov>: <Reg8: 21, Reg8: 18>
==> 0000008e: <Mov>: <Reg8: 20, Reg8: 4>
==> 00000091: <Call>: <Reg8: 15, Reg8: 15, UInt8: 5>
==> 00000095: <Call2>: <Reg8: 17, Reg8: 16, Reg8: 17, Reg8: 15>
==> 0000009a: <GetByIdShort>: <Reg8: 16, Reg8: 17, UInt8: 1, string_id: 229>  # String: 'split' (Identifier)
==> 0000009f: <TryGetById>: <Reg8: 15, Reg8: 8, UInt8: 2, string_id: 14>  # String: 'HermesInternal' (Identifier)
==> 000000a5: <GetByIdShort>: <Reg8: 15, Reg8: 15, UInt8: 3, string_id: 96>  # String: 'concat' (Identifier)
==> 000000aa: <Call3>: <Reg8: 15, Reg8: 15, Reg8: 7, Reg8: 19, Reg8: 3>
==> 000000b0: <Call2>: <Reg8: 17, Reg8: 16, Reg8: 17, Reg8: 15>
==> 000000b5: <GetByIdShort>: <Reg8: 16, Reg8: 17, UInt8: 4, string_id: 165>  # String: 'join' (Identifier)
==> 000000ba: <TryGetById>: <Reg8: 15, Reg8: 8, UInt8: 2, string_id: 14>  # String: 'HermesInternal' (Identifier)
==> 000000c0: <GetByIdShort>: <Reg8: 15, Reg8: 15, UInt8: 3, string_id: 96>  # String: 'concat' (Identifier)
==> 000000c5: <Mov>: <Reg8: 24, Reg8: 7>
==> 000000c8: <Mov>: <Reg8: 23, Reg8: 19>
==> 000000cb: <Mov>: <Reg8: 22, Reg8: 1>
==> 000000ce: <Mov>: <Reg8: 21, Reg8: 18>
==> 000000d1: <Call>: <Reg8: 15, Reg8: 15, UInt8: 5>
==> 000000d5: <Call2>: <Reg8: 0, Reg8: 16, Reg8: 17, Reg8: 15>
==> 000000da: <JmpLong>: <Addr32: -166>  # Address: 00000034
==> 000000df: <Catch>: <Reg8: 1>
==> 000000e1: <IteratorClose>: <Reg8: 2, UInt8: 1>
==> 000000e4: <Throw>: <Reg8: 1>
==> 000000e6: <Ret>: <Reg8: 0>
"""


def test_definition_before_a_loop_prints_when_read_after_it():
    context = Decompiler.build_context(_MAKE_SAFE_REGEX, 9342, strict=False)
    js = Decompiler.render(context, verbose=False, raw=False)

    assert "r0 = param1;" in js
    assert js.index("r0 = param1;") < js.index("return r0;")
