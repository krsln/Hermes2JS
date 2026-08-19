function function_15054(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 3, UInt8: 2>
    // USED → r3 = param2;
    // CODE → addr:  3 | <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → addr:  6 | <JStrictNotEqual>: <Addr8: 46, Reg8: 3, Reg8: 0>  # Address: 00000034
    if (param2 !== 2) goto label_52;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 10 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr: 12 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 18 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 23 | <LoadConstString>: <Reg8: 1, string_id: 4581>  # String: '__BC:ControlFlow/ForEachTests/forEachTest/if-middle' (String)
    // USED → r1 = "__BC:ControlFlow/ForEachTests/forEachTest/if-middle";
    // CODE → addr: 27 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
    console.log("__BC:ControlFlow/ForEachTests/forEachTest/if-middle")
    // CODE → addr: 32 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 38 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 43 | <LoadConstString>: <Reg8: 0, string_id: 8469>  # String: 'middle' (Identifier)
    // USED → r0 = "middle";
    // CODE → addr: 47 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("middle")
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 52 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr: 54 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 60 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 65 | <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → addr: 68 | <Call3>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log(param2, param1)
    // CODE → addr: 74 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 76 | <Ret>: <Reg8: 0>
    return undefined;
}