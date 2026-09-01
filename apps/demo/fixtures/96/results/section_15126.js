function callMapSetTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4555>  # String: '__BC:Collections/MapSetTests/callMapSetTests/start' (String)
    // USED → r0 = "__BC:Collections/MapSetTests/callMapSetTests/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Collections/MapSetTests/callMapSetTests/start")
    // CODE → addr: 22 | <GetEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getEnvironment(0)
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 1>
    // USED → r3 = r2[1];
    // CODE → addr: 29 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 31 | <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = r2[1].call(r0)
    // CODE → addr: 35 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 2>
    // USED → r3 = r2[2];
    // CODE → addr: 39 | <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = r2[2].call(r0)
    // CODE → addr: 43 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 3>
    // USED → r2 = r2[3];
    // CODE → addr: 47 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 0>
    r2 = r2[3].call(r0)
    // CODE → addr: 51 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 57 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 62 | <LoadConstString>: <Reg8: 1, string_id: 317>  # String: '__BC:Collections/MapSetTests/callMapSetTests/end' (String)
    // USED → r1 = "__BC:Collections/MapSetTests/callMapSetTests/end";
    // CODE → addr: 66 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Collections/MapSetTests/callMapSetTests/end")
    // CODE → addr: 71 | <Ret>: <Reg8: 0>
    return undefined;
}