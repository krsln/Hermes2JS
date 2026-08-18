function callMapSetTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4555>  # String: '__BC:Collections/MapSetTests/callMapSetTests/start' (String)
    // USED → r0 = "__BC:Collections/MapSetTests/callMapSetTests/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Collections/MapSetTests/callMapSetTests/start")
    // CODE → <GetEnvironment>: <Reg8: 2, UInt8: 0>
    // USED → r2 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 1>
    // USED → r3 = getEnvironment(0)[1];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    getEnvironment(0)[1].call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 2>
    // USED → r3 = getEnvironment(0)[2];
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    getEnvironment(0)[2].call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 3>
    // USED → r2 = getEnvironment(0)[3];
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 0>
    getEnvironment(0)[3].call(undefined)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 317>  # String: '__BC:Collections/MapSetTests/callMapSetTests/end' (String)
    // USED → r1 = "__BC:Collections/MapSetTests/callMapSetTests/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Collections/MapSetTests/callMapSetTests/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}