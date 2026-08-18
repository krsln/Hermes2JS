function restAfterRequiredTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUInt8>: <Reg8: 10, UInt8: 2>
    r10 = 2
    // CODE → <CallBuiltin>: <Reg8: 7, UInt8: 47, UInt8: 2>  # Built-in function: [#47 copyRestArgs]
    // USED → r7 = copyRestArgs(r5, r6);
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4955>  # String: '__BC:Functions/RestParameterTests/restAfterRequiredTest/start' (String)
    // USED → r3 = "__BC:Functions/RestParameterTests/restAfterRequiredTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Functions/RestParameterTests/restAfterRequiredTest/start")
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 2>
    // USED → r4 = param2;
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → <Call4>: <Reg8: 3, Reg8: 5, Reg8: 6, Reg8: 3, Reg8: 4, Reg8: 7>
    console.log(param1, param2, r7)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4954>  # String: '__BC:Functions/RestParameterTests/restAfterRequiredTest/end' (String)
    // USED → r2 = "__BC:Functions/RestParameterTests/restAfterRequiredTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/RestParameterTests/restAfterRequiredTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}