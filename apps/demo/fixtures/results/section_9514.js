function restOnlyTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstZero>: <Reg8: 8>
    r8 = 0
    // CODE → <CallBuiltin>: <Reg8: 6, UInt8: 47, UInt8: 2>  # Built-in function: [#47 copyRestArgs]
    // USED → r6 = copyRestArgs(r4, r5);
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4958>  # String: '__BC:Functions/RestParameterTests/restOnlyTest/start' (String)
    // USED → r3 = "__BC:Functions/RestParameterTests/restOnlyTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Functions/RestParameterTests/restOnlyTest/start")
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
    // USED → r3 = r6.length;
    // CODE → <Call3>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 6>
    console.log(r3, r6)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4957>  # String: '__BC:Functions/RestParameterTests/restOnlyTest/end' (String)
    // USED → r2 = "__BC:Functions/RestParameterTests/restOnlyTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/RestParameterTests/restOnlyTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}