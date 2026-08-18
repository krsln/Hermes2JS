function callRestParameterTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4791>  # String: '__BC:Functions/RestParameterTests/callRestParameterTests/start' (String)
    // USED → r0 = "__BC:Functions/RestParameterTests/callRestParameterTests/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Functions/RestParameterTests/callRestParameterTests/start")
    // CODE → <GetEnvironment>: <Reg8: 2, UInt8: 0>
    // USED → r2 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 2, UInt8: 0>
    // USED → r6 = getEnvironment(0)[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call1>: <Reg8: 3, Reg8: 6, Reg8: 0>
    r3 = getEnvironment(0)[0].call(undefined)
    // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 3>
    // USED → r3 = 3;
    // CODE → <Call4>: <Reg8: 3, Reg8: 6, Reg8: 0, Reg8: 5, Reg8: 4, Reg8: 3>
    r3 = getEnvironment(0)[0].call(undefined, 1, 2, 3)
    // CODE → <LoadFromEnvironment>: <Reg8: 7, Reg8: 2, UInt8: 1>
    // USED → r7 = getEnvironment(0)[1];
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 7189>  # String: 'a' (Identifier)
    // USED → r6 = "a";
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 38>  # String: 'b' (Identifier)
    // USED → r5 = "b";
    // CODE → <Call3>: <Reg8: 3, Reg8: 7, Reg8: 0, Reg8: 6, Reg8: 5>
    r3 = getEnvironment(0)[1].call(undefined, "a", "b")
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 7241>  # String: 'c' (Identifier)
    r9 = "c"
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 7181>  # String: 'd' (Identifier)
    r8 = "d"
    // CODE → <LoadConstUndefined>: <Reg8: 12>
    r12 = undefined
    // CODE → <Mov>: <Reg8: 11, Reg8: 6>
    r11 = "a"
    // CODE → <Mov>: <Reg8: 10, Reg8: 5>
    r10 = "b"
    // CODE → <Call>: <Reg8: 3, Reg8: 7, UInt8: 5>
    r3 = getEnvironment(0)[1](r12, r11, r10, r9, r8)
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 2>
    // USED → r2 = getEnvironment(0)[2];
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 0>
    r2 = getEnvironment(0)[2].call(undefined)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4790>  # String: '__BC:Functions/RestParameterTests/callRestParameterTests/end' (String)
    // USED → r1 = "__BC:Functions/RestParameterTests/callRestParameterTests/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/RestParameterTests/callRestParameterTests/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}