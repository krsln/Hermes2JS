function callDefaultParameterTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4771>  # String: '__BC:Functions/DefaultParameterTests/callDefaultParameterTests/start' (String)
    // USED → r0 = "__BC:Functions/DefaultParameterTests/callDefaultParameterTests/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Functions/DefaultParameterTests/callDefaultParameterTests/start")
    // CODE → addr: 22 | <GetEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getEnvironment(0)
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 6, Reg8: 2, UInt8: 0>
    // USED → r6 = r2[0];
    // CODE → addr: 29 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr: 31 | <LoadConstUInt8>: <Reg8: 5, UInt8: 5>
    // USED → r5 = 5;
    // CODE → addr: 34 | <Call2>: <Reg8: 3, Reg8: 6, Reg8: 0, Reg8: 5>
    r3 = r2[0].call(r0, 5)
    // CODE → addr: 39 | <LoadConstUInt8>: <Reg8: 4, UInt8: 20>
    // USED → r4 = 20;
    // CODE → addr: 42 | <Call3>: <Reg8: 3, Reg8: 6, Reg8: 0, Reg8: 5, Reg8: 4>
    r3 = r2[0].call(r0, 5, 20)
    // CODE → addr: 48 | <LoadConstString>: <Reg8: 3, string_id: 1248>  # String: 'sum' (String)
    // USED → r3 = "sum";
    // CODE → addr: 52 | <Call4>: <Reg8: 3, Reg8: 6, Reg8: 0, Reg8: 5, Reg8: 4, Reg8: 3>
    r3 = r2[0].call(r0, 5, 20, "sum")
    // CODE → addr: 59 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 2, UInt8: 1>
    // USED → r5 = r2[1];
    // CODE → addr: 63 | <Call1>: <Reg8: 2, Reg8: 5, Reg8: 0>
    r2 = r2[1].call(r0)
    // CODE → addr: 67 | <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    // CODE → addr: 70 | <LoadConstUInt8>: <Reg8: 3, UInt8: 3>
    // USED → r3 = 3;
    // CODE → addr: 73 | <LoadConstUInt8>: <Reg8: 2, UInt8: 4>
    // USED → r2 = 4;
    // CODE → addr: 76 | <Call4>: <Reg8: 2, Reg8: 5, Reg8: 0, Reg8: 4, Reg8: 3, Reg8: 2>
    r2 = r2[1].call(r0, 2, 3, 4)
    // CODE → addr: 83 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 89 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 94 | <LoadConstString>: <Reg8: 1, string_id: 4770>  # String: '__BC:Functions/DefaultParameterTests/callDefaultParameterTests/end' (String)
    // USED → r1 = "__BC:Functions/DefaultParameterTests/callDefaultParameterTests/end";
    // CODE → addr: 98 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/DefaultParameterTests/callDefaultParameterTests/end")
    // CODE → addr:103 | <Ret>: <Reg8: 0>
    return r0;
}