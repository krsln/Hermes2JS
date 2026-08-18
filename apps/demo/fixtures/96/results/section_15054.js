function function_15054(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 2>
    // USED → r3 = param2;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    if (param2 === 2) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetGlobalObject>: <Reg8: 0>
        // USED → r0 = globalThis;
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4581>  # String: '__BC:ControlFlow/ForEachTests/forEachTest/if-middle' (String)
        // USED → r1 = "__BC:ControlFlow/ForEachTests/forEachTest/if-middle";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
        console.log("__BC:ControlFlow/ForEachTests/forEachTest/if-middle")
        // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r2 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r1 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 0, string_id: 8469>  # String: 'middle' (Identifier)
        // USED → r0 = "middle";
        // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
        console.log("middle")
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → <Call3>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log(param2, param1)
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}