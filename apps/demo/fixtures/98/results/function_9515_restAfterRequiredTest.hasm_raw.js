function restAfterRequiredTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUInt8>: <Reg8: 10, UInt8: 2>
    r10 = 2
    // CODE → addr:  3 | <CallBuiltin>: <Reg8: 7, UInt8: 47, UInt8: 2>  # Built-in function: [#47 copyRestArgs]
    r7 = copyRestArgs(r10, r9)
    // CODE → addr:  7 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  9 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 15 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 20 | <LoadConstString>: <Reg8: 3, string_id: 4955>  # String: '__BC:Functions/RestParameterTests/restAfterRequiredTest/start' (String)
    // USED → r3 = "__BC:Functions/RestParameterTests/restAfterRequiredTest/start";
    // CODE → addr: 24 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Functions/RestParameterTests/restAfterRequiredTest/start")
    // CODE → addr: 29 | <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 35 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 40 | <LoadParam>: <Reg8: 4, UInt8: 2>
    // USED → r4 = param2;
    // CODE → addr: 43 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr: 46 | <Call4>: <Reg8: 3, Reg8: 5, Reg8: 6, Reg8: 3, Reg8: 4, Reg8: 7>
    console.log(param1, param2, r7)
    // CODE → addr: 53 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 59 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 64 | <LoadConstString>: <Reg8: 2, string_id: 4954>  # String: '__BC:Functions/RestParameterTests/restAfterRequiredTest/end' (String)
    // USED → r2 = "__BC:Functions/RestParameterTests/restAfterRequiredTest/end";
    // CODE → addr: 68 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/RestParameterTests/restAfterRequiredTest/end")
    // CODE → addr: 73 | <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → addr: 75 | <Ret>: <Reg8: 1>
    return r1;
}