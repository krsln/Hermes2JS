function legacyArgumentsTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:  2 | <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → addr:  4 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  6 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 12 | <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 17 | <LoadConstString>: <Reg8: 2, string_id: 4795>  # String: '__BC:Functions/RestParameterTests/legacyArgumentsTest/start' (String)
    // USED → r2 = "__BC:Functions/RestParameterTests/legacyArgumentsTest/start";
    // CODE → addr: 21 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 2>
    console.log("__BC:Functions/RestParameterTests/legacyArgumentsTest/start")
    // CODE → addr: 26 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 32 | <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 37 | <GetArgumentsLength>: <Reg8: 2, Reg8: 4>
    // USED → r2 = arguments.length;
    // CODE → addr: 40 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 2>
    console.log(r2)
    // CODE → addr: 45 | <GetArgumentsLength>: <Reg8: 2, Reg8: 4>
    // USED → r2 = arguments.length;
    // CODE → addr: 48 | <LoadConstZero>: <Reg8: 3>
    // USED → r3 = 0;
    // CODE → addr: 50 | <Less>: <Reg8: 2, Reg8: 3, Reg8: 2>
    // USED → r2 = 0 < arguments.length;
    // CODE → addr: 54 | <JmpFalse>: <Addr8: 33, Reg8: 2>  # Address: 00000057
    if (!(0 < arguments.length)) goto label_87;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 57 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 63 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 68 | <GetArgumentsPropByVal>: <Reg8: 2, Reg8: 3, Reg8: 4>
    // USED → r2 = arguments[0];
    // CODE → addr: 72 | <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    console.log(r2)
    // CODE → addr: 77 | <Inc>: <Reg8: 3, Reg8: 3>
    r3 = r3 + 1
    // CODE → addr: 80 | <GetArgumentsLength>: <Reg8: 2, Reg8: 4>
    r2 = arguments.length
    // CODE → addr: 83 | <JLess>: <Addr8: -26, Reg8: 3, Reg8: 2>  # Address: 00000039
    // → r2 = arguments.length; r3 = r3 + 1
    if (r3 < r2) goto label_57;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 87 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 93 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 98 | <LoadConstString>: <Reg8: 1, string_id: 2593>  # String: '__BC:Functions/RestParameterTests/legacyArgumentsTest/end' (String)
    // USED → r1 = "__BC:Functions/RestParameterTests/legacyArgumentsTest/end";
    // CODE → addr:102 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/RestParameterTests/legacyArgumentsTest/end")
    // CODE → addr:107 | <Ret>: <Reg8: 0>
    return r0;
}