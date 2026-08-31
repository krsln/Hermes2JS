function restOnlyTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstZero>: <Reg8: 8>
    r8 = 0
    // CODE → addr:  2 | <CallBuiltin>: <Reg8: 6, UInt8: 47, UInt8: 2>  # Built-in function: [#47 copyRestArgs]
    // USED → r6 = copyRestArgs(r8, r7);
    // CODE → addr:  6 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  8 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 14 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 19 | <LoadConstString>: <Reg8: 3, string_id: 4958>  # String: '__BC:Functions/RestParameterTests/restOnlyTest/start' (String)
    // USED → r3 = "__BC:Functions/RestParameterTests/restOnlyTest/start";
    // CODE → addr: 23 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Functions/RestParameterTests/restOnlyTest/start")
    // CODE → addr: 28 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 34 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 39 | <GetByIdShort>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
    // USED → r3 = r6.length;
    // CODE → addr: 44 | <Call3>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 6>
    console.log(r6.length, r6)
    // CODE → addr: 50 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 56 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 61 | <LoadConstString>: <Reg8: 2, string_id: 4957>  # String: '__BC:Functions/RestParameterTests/restOnlyTest/end' (String)
    // USED → r2 = "__BC:Functions/RestParameterTests/restOnlyTest/end";
    // CODE → addr: 65 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/RestParameterTests/restOnlyTest/end")
    // CODE → addr: 70 | <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → addr: 72 | <Ret>: <Reg8: 1>
    return undefined;
}