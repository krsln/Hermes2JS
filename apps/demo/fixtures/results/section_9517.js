function callRestParameterTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 6, UInt8: 0>
    r6 = getParentEnvironment(0)
    // CODE → <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → <TryGetById>: <Reg8: 9, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 4082>  # String: '__BC:Functions/RestParameterTests/callRestParameterTests/start' (String)
    // USED → r7 = "__BC:Functions/RestParameterTests/callRestParameterTests/start";
    // CODE → <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    console.log("__BC:Functions/RestParameterTests/callRestParameterTests/start")
    // CODE → <LoadFromEnvironment>: <Reg8: 7, Reg8: 6, UInt8: 0>
    // USED → r7 = r6[0];
    // CODE → <LoadConstUndefined>: <Reg8: 3>
    // USED → r3 = undefined;
    // CODE → <Call1>: <Reg8: 4, Reg8: 7, Reg8: 3>
    r4 = r6[0].call(r3)
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
    // USED → r0 = 3;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    // USED → r1 = 2;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → <Call4>: <Reg8: 4, Reg8: 7, Reg8: 3, Reg8: 2, Reg8: 1, Reg8: 0>
    r4 = r6[0].call(r3, 1, 2, 3)
    // CODE → <LoadFromEnvironment>: <Reg8: 11, Reg8: 6, UInt8: 1>
    // USED → r11 = r6[1];
    // CODE → <LoadConstString>: <Reg8: 10, string_id: 36>  # String: 'b' (Identifier)
    // USED → r10 = "b";
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 6471>  # String: 'a' (Identifier)
    // USED → r9 = "a";
    // CODE → <Call3>: <Reg8: 4, Reg8: 11, Reg8: 3, Reg8: 9, Reg8: 10>
    r4 = r6[1].call(r3, "a", "b")
    // CODE → <LoadConstString>: <Reg8: 12, string_id: 6518>  # String: 'd' (Identifier)
    r12 = "d"
    // CODE → <LoadConstString>: <Reg8: 13, string_id: 6562>  # String: 'c' (Identifier)
    r13 = "c"
    // CODE → <LoadConstUndefined>: <Reg8: 16>
    r16 = undefined
    // CODE → <Mov>: <Reg8: 15, Reg8: 9>
    r15 = "a"
    // CODE → <Mov>: <Reg8: 14, Reg8: 10>
    r14 = "b"
    // CODE → <Call>: <Reg8: 4, Reg8: 11, UInt8: 5>
    r4 = r6[1](r16, r15, r14, r13, r12)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 6, UInt8: 2>
    // USED → r6 = r6[2];
    // CODE → <Call1>: <Reg8: 4, Reg8: 6, Reg8: 3>
    r4 = r6[2].call(r3)
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4950>  # String: '__BC:Functions/RestParameterTests/callRestParameterTests/end' (String)
    // USED → r5 = "__BC:Functions/RestParameterTests/callRestParameterTests/end";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Functions/RestParameterTests/callRestParameterTests/end")
    // CODE → <Ret>: <Reg8: 3>
    return undefined;
}