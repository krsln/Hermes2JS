function legacyArgumentsTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4795>  # String: '__BC:Functions/RestParameterTests/legacyArgumentsTest/start' (String)
    // USED → r2 = "__BC:Functions/RestParameterTests/legacyArgumentsTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 2>
    console.log("__BC:Functions/RestParameterTests/legacyArgumentsTest/start")
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetArgumentsLength>: <Reg8: 2, Reg8: 4>
    // USED → r2 = arguments.length;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 2>
    console.log(r2)
    // CODE → <GetArgumentsLength>: <Reg8: 2, Reg8: 4>
    // USED → r2 = arguments.length;
    // CODE → <LoadConstZero>: <Reg8: 3>
    // USED → r3 = 0;
    // CODE → <Less>: <Reg8: 2, Reg8: 3, Reg8: 2>
    // USED → r2 = 0 < arguments.length;
    // CODE → <JmpFalse>: <Addr8: 33, Reg8: 2>  # Address: 00000057
    if (!(0 < arguments.length)) goto label_87;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <GetArgumentsPropByVal>: <Reg8: 2, Reg8: 3, Reg8: 4>
    // USED → r2 = arguments[0];
    // CODE → <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    console.log(r2)
    // CODE → <Inc>: <Reg8: 3, Reg8: 3>
    // USED → r3 = r3 + 1;
    // CODE → <GetArgumentsLength>: <Reg8: 2, Reg8: 4>
    // USED → r2 = arguments.length;
    // CODE → <JLess>: <Addr8: -26, Reg8: 3, Reg8: 2>  # Address: 00000039
    // → r2 = arguments.length; r3 = r3 + 1
    if (r3 < r2) goto label_57;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 2593>  # String: '__BC:Functions/RestParameterTests/legacyArgumentsTest/end' (String)
    // USED → r1 = "__BC:Functions/RestParameterTests/legacyArgumentsTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/RestParameterTests/legacyArgumentsTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}