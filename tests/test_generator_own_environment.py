"""
The generator entry block holds the body's own environment next to the resume
pair (96/14490):

    StartGenerator; r8 = param1; r5 = param2; r2 = createEnvironment(); ResumeGenerator …

Folding the resume pair away used to clear the whole block, so `r2[0] = …`
afterwards stored into an environment nothing defined.
"""

from hermes_decompiler.Decompiler import Decompiler

_HASM = r"""
=> [Function #14490 "?anon_0_" of 261 bytes]: 3 params, frame size=19, strict=1, exc handler=0, debug info=0  @ offset 0x0025af0f

Bytecode listing:

==> 00000000: <StartGenerator>: <>
==> 00000001: <LoadParam>: <Reg8: 8, UInt8: 1>
==> 00000004: <LoadParam>: <Reg8: 5, UInt8: 2>
==> 00000007: <CreateEnvironment>: <Reg8: 2>
==> 00000009: <ResumeGenerator>: <Reg8: 0, Reg8: 1>
==> 0000000c: <JmpTrueLong>: <Addr32: 246, Reg8: 1>  # Address: 00000102
==> 00000012: <LoadConstUndefined>: <Reg8: 3>
==> 00000014: <StoreNPToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 3>
==> 00000018: <GetEnvironment>: <Reg8: 1, UInt8: 2>
==> 0000001b: <LoadFromEnvironment>: <Reg8: 4, Reg8: 1, UInt8: 2>
==> 0000001f: <GetByIdShort>: <Reg8: 4, Reg8: 4, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
==> 00000024: <GetById>: <Reg8: 4, Reg8: 4, UInt8: 2, string_id: 8650>  # String: 'unloadAsync' (Identifier)
==> 0000002a: <JmpTrue>: <Addr8: 43, Reg8: 4>  # Address: 00000055
==> 0000002d: <LoadFromEnvironment>: <Reg8: 4, Reg8: 1, UInt8: 1>
==> 00000031: <GetById>: <Reg8: 9, Reg8: 4, UInt8: 3, string_id: 13024>  # String: 'UnavailabilityError' (Identifier)
==> 00000037: <GetByIdShort>: <Reg8: 4, Reg8: 9, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
==> 0000003c: <CreateThis>: <Reg8: 6, Reg8: 4, Reg8: 9>
==> 00000040: <LoadConstString>: <Reg8: 11, string_id: 9595>  # String: 'expo-font' (Identifier)
==> 00000044: <LoadConstString>: <Reg8: 10, string_id: 8650>  # String: 'unloadAsync' (Identifier)
==> 00000048: <Mov>: <Reg8: 12, Reg8: 6>
==> 0000004b: <Construct>: <Reg8: 4, Reg8: 9, UInt8: 3>
==> 0000004f: <SelectObject>: <Reg8: 4, Reg8: 6, Reg8: 4>
==> 00000053: <Throw>: <Reg8: 4>
==> 00000055: <TypeOf>: <Reg8: 6, Reg8: 8>
==> 00000058: <LoadConstString>: <Reg8: 4, string_id: 7532>  # String: 'object' (Identifier)
==> 0000005c: <JStrictEqual>: <Addr8: 30, Reg8: 6, Reg8: 4>  # Address: 0000007a
==> 00000060: <LoadFromEnvironment>: <Reg8: 4, Reg8: 1, UInt8: 11>
==> 00000064: <Call3>: <Reg8: 4, Reg8: 4, Reg8: 3, Reg8: 8, Reg8: 5>
==> 0000006a: <SaveGenerator>: <Addr8: 4>  # Address: 0000006e
==> 0000006c: <Ret>: <Reg8: 4>
==> 0000006e: <ResumeGenerator>: <Reg8: 4, Reg8: 6>
==> 00000071: <JmpTrue>: <Addr8: 6, Reg8: 6>  # Address: 00000077
==> 00000074: <CompleteGenerator>: <>
==> 00000075: <Ret>: <Reg8: 4>
==> 00000077: <CompleteGenerator>: <>
==> 00000078: <Ret>: <Reg8: 4>
==> 0000007a: <JmpTrue>: <Addr8: 73, Reg8: 5>  # Address: 000000c3
==> 0000007d: <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 8>
==> 00000081: <GetGlobalObject>: <Reg8: 4>
==> 00000083: <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 5, string_id: 24>  # String: 'Object' (Identifier)
==> 00000089: <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 6, string_id: 118>  # String: 'keys' (Identifier)
==> 0000008e: <Call2>: <Reg8: 8, Reg8: 6, Reg8: 7, Reg8: 8>
==> 00000093: <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 7, string_id: 27>  # String: 'Promise' (Identifier)
==> 00000099: <GetById>: <Reg8: 4, Reg8: 6, UInt8: 8, string_id: 7443>  # String: 'all' (Identifier)
==> 0000009f: <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 9, string_id: 170>  # String: 'map' (Identifier)
==> 000000a4: <CreateClosure>: <Reg8: 2, Reg8: 2, function_id: 14491>  # Function: [#14491  of 31 bytes]: 2 params @ offset 0x0025b014
==> 000000a9: <Call2>: <Reg8: 2, Reg8: 7, Reg8: 8, Reg8: 2>
==> 000000ae: <Call2>: <Reg8: 2, Reg8: 4, Reg8: 6, Reg8: 2>
==> 000000b3: <SaveGenerator>: <Addr8: 4>  # Address: 000000b7
==> 000000b5: <Ret>: <Reg8: 2>
==> 000000b7: <ResumeGenerator>: <Reg8: 2, Reg8: 4>
==> 000000ba: <JmpTrue>: <Addr8: 6, Reg8: 4>  # Address: 000000c0
==> 000000bd: <CompleteGenerator>: <>
==> 000000be: <Ret>: <Reg8: 3>
==> 000000c0: <CompleteGenerator>: <>
==> 000000c1: <Ret>: <Reg8: 2>
==> 000000c3: <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 1>
==> 000000c7: <GetById>: <Reg8: 4, Reg8: 1, UInt8: 10, string_id: 9531>  # String: 'CodedError' (Identifier)
==> 000000cd: <GetGlobalObject>: <Reg8: 1>
==> 000000cf: <TryGetById>: <Reg8: 1, Reg8: 1, UInt8: 11, string_id: 14>  # String: 'HermesInternal' (Identifier)
==> 000000d5: <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 12, string_id: 96>  # String: 'concat' (Identifier)
==> 000000da: <LoadConstString>: <Reg8: 2, string_id: 3637>  # String: 'No fontFamily can be used for the provided options: ' (String)
==> 000000de: <LoadConstString>: <Reg8: 1, string_id: 2093>  # String: '. The second argument of `unloadAsync()` can only be used with a `string` value as the first argument.' (String)
==> 000000e2: <Call3>: <Reg8: 10, Reg8: 3, Reg8: 2, Reg8: 5, Reg8: 1>
==> 000000e8: <GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
==> 000000ed: <CreateThis>: <Reg8: 2, Reg8: 1, Reg8: 4>
==> 000000f1: <LoadConstString>: <Reg8: 11, string_id: 2414>  # String: 'ERR_FONT_API' (String)
==> 000000f5: <Mov>: <Reg8: 12, Reg8: 2>
==> 000000f8: <Construct>: <Reg8: 1, Reg8: 4, UInt8: 3>
==> 000000fc: <SelectObject>: <Reg8: 1, Reg8: 2, Reg8: 1>
==> 00000100: <Throw>: <Reg8: 1>
==> 00000102: <CompleteGenerator>: <>
==> 00000103: <Ret>: <Reg8: 0>
"""


def test_generator_keeps_its_own_environment_definition():
    js = Decompiler.render(Decompiler.build_context(_HASM, 14490, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in js.splitlines() if not line.strip().startswith("//"))

    assert "r2 = createEnvironment();" in code
    assert code.index("r2 = createEnvironment();") < code.index("r2[0] = undefined;")
