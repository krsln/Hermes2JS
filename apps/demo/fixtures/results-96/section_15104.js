function callDefaultParameterTests(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4596>  # String: '__BC:Functions/DefaultParameterTests/callDefaultParameterTests/start' (String)
    // USED → r0 = "__BC:Functions/DefaultParameterTests/callDefaultParameterTests/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Functions/DefaultParameterTests/callDefaultParameterTests/start")
    // CODE → <GetEnvironment>: <Reg8: 2, UInt8: 0>
    // USED → r2 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 2, UInt8: 0>
    // USED → r6 = getEnvironment(0)[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 5>
    // USED → r5 = 5;
    // CODE → <Call2>: <Reg8: 3, Reg8: 6, Reg8: 0, Reg8: 5>
    r3 = getEnvironment(0)[0].call(undefined, 5)
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 20>
    // USED → r4 = 20;
    // CODE → <Call3>: <Reg8: 3, Reg8: 6, Reg8: 0, Reg8: 5, Reg8: 4>
    r3 = getEnvironment(0)[0].call(undefined, 5, 20)
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 1224>  # String: 'sum' (String)
    // USED → r3 = "sum";
    // CODE → <Call4>: <Reg8: 3, Reg8: 6, Reg8: 0, Reg8: 5, Reg8: 4, Reg8: 3>
    r3 = getEnvironment(0)[0].call(undefined, 5, 20, "sum")
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 2, UInt8: 1>
    // USED → r5 = getEnvironment(0)[1];
    // CODE → <Call1>: <Reg8: 2, Reg8: 5, Reg8: 0>
    r2 = getEnvironment(0)[1].call(undefined)
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 3>
    // USED → r3 = 3;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 4>
    // USED → r2 = 4;
    // CODE → <Call4>: <Reg8: 2, Reg8: 5, Reg8: 0, Reg8: 4, Reg8: 3, Reg8: 2>
    r2 = getEnvironment(0)[1].call(undefined, 2, 3, 4)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4594>  # String: '__BC:Functions/DefaultParameterTests/callDefaultParameterTests/end' (String)
    // USED → r1 = "__BC:Functions/DefaultParameterTests/callDefaultParameterTests/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Functions/DefaultParameterTests/callDefaultParameterTests/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}