function legacyArgumentsTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    // USED → r4 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → <TryGetById>: <Reg8: 9, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 4953>  # String: '__BC:Functions/RestParameterTests/legacyArgumentsTest/start' (String)
    // USED → r6 = "__BC:Functions/RestParameterTests/legacyArgumentsTest/start";
    // CODE → <Call2>: <Reg8: 6, Reg8: 8, Reg8: 9, Reg8: 6>
    console.log("__BC:Functions/RestParameterTests/legacyArgumentsTest/start")
    // CODE → <TryGetById>: <Reg8: 9, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = globalThis.console.log;
    // CODE → <Mov>: <Reg8: 6, Reg8: 7>
    r6 = undefined
    // CODE → <GetArgumentsLength>: <Reg8: 6, Reg8: 6>
    // USED → r6 = arguments.length;
    // CODE → <Call2>: <Reg8: 6, Reg8: 8, Reg8: 9, Reg8: 6>
    console.log(arguments.length)
    // CODE → <Mov>: <Reg8: 6, Reg8: 7>
    r6 = undefined
    // CODE → <GetArgumentsLength>: <Reg8: 6, Reg8: 6>
    // USED → r6 = arguments.length;
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <Less>: <Reg8: 3, Reg8: 0, Reg8: 6>
    // USED → r3 = 0 < arguments.length;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    // USED → r1 = 1;
    // CODE → <JmpFalse>: <Addr8: 37, Reg8: 3>  # Address: 00000064
    if (!(0 < arguments.length)) goto label_100;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 9, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = globalThis.console.log;
    // CODE → <GetArgumentsPropByValStrict>: <Reg8: 6, Reg8: 0, Reg8: 7>
    // USED → r6 = arguments[0];
    // CODE → <Call2>: <Reg8: 6, Reg8: 8, Reg8: 9, Reg8: 6>
    console.log(arguments[0])
    // CODE → <AddN>: <Reg8: 0, Reg8: 0, Reg8: 1>
    // USED → r0 = 0 + 1;
    // CODE → <Mov>: <Reg8: 6, Reg8: 7>
    r6 = undefined
    // CODE → <GetArgumentsLength>: <Reg8: 6, Reg8: 6>
    // USED → r6 = arguments.length;
    // CODE → <JLess>: <Addr8: -30, Reg8: 0, Reg8: 6>  # Address: 00000042
    if (0 + 1 < arguments.length) goto label_66;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4952>  # String: '__BC:Functions/RestParameterTests/legacyArgumentsTest/end' (String)
    // USED → r5 = "__BC:Functions/RestParameterTests/legacyArgumentsTest/end";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Functions/RestParameterTests/legacyArgumentsTest/end")
    // CODE → <Ret>: <Reg8: 4>
    return undefined;
}