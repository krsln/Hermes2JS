function callRestParameterTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4791>  # String: '__BC:Functions/RestParameterTests/callRestParameterTests/start' (String)
    // USED → r0 = "__BC:Functions/RestParameterTests/callRestParameterTests/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Functions/RestParameterTests/callRestParameterTests/start")
    // CODE → addr: 22 | <GetEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getEnvironment(0)
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 6, Reg8: 2, UInt8: 0>
    // USED → r6 = r2[0];
    // CODE → addr: 29 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr: 31 | <Call1>: <Reg8: 3, Reg8: 6, Reg8: 0>
    r3 = r2[0].call(r0)
    // CODE → addr: 35 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr: 38 | <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    // CODE → addr: 41 | <LoadConstUInt8>: <Reg8: 3, UInt8: 3>
    // USED → r3 = 3;
    // CODE → addr: 44 | <Call4>: <Reg8: 3, Reg8: 6, Reg8: 0, Reg8: 5, Reg8: 4, Reg8: 3>
    r3 = r2[0].call(r0, 1, 2, 3)
    // CODE → addr: 51 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 2, UInt8: 1>
    // USED → r7 = r2[1];
    // CODE → addr: 55 | <LoadConstString>: <Reg8: 6, string_id: 7189>  # String: 'a' (Identifier)
    // USED → r6 = "a";
    // CODE → addr: 59 | <LoadConstString>: <Reg8: 5, string_id: 38>  # String: 'b' (Identifier)
    // USED → r5 = "b";
    // CODE → addr: 63 | <Call3>: <Reg8: 3, Reg8: 7, Reg8: 0, Reg8: 6, Reg8: 5>
    r3 = r2[1].call(r0, "a", "b")
    // CODE → addr: 69 | <LoadConstString>: <Reg8: 9, string_id: 7241>  # String: 'c' (Identifier)
    r9 = "c"
    // CODE → addr: 73 | <LoadConstString>: <Reg8: 8, string_id: 7181>  # String: 'd' (Identifier)
    r8 = "d"
    // CODE → addr: 77 | <LoadConstUndefined>: <Reg8: 12>
    r12 = undefined
    // CODE → addr: 79 | <Mov>: <Reg8: 11, Reg8: 6>
    r11 = "a"
    // CODE → addr: 82 | <Mov>: <Reg8: 10, Reg8: 5>
    r10 = "b"
    // CODE → addr: 85 | <Call>: <Reg8: 3, Reg8: 7, UInt8: 5>
    r3 = r2[1](r12, r11, r10, r9, r8)
    // CODE → addr: 89 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 2>
    // USED → r2 = r2[2];
    // CODE → addr: 93 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 0>
    r2 = r2[2].call(r0)
    // CODE → addr: 97 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:103 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:108 | <LoadConstString>: <Reg8: 1, string_id: 4790>  # String: '__BC:Functions/RestParameterTests/callRestParameterTests/end' (String)
    // USED → r1 = "__BC:Functions/RestParameterTests/callRestParameterTests/end";
    // CODE → addr:112 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/RestParameterTests/callRestParameterTests/end")
    // CODE → addr:117 | <Ret>: <Reg8: 0>
    return r0;
}