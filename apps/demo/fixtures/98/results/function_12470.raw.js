function function_12470(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 5, UInt8: 2>
    // USED → r5 = param2;
    // CODE → addr:  3 | <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → addr:  6 | <JStrictNotEqual>: <Addr8: 46, Reg8: 5, Reg8: 0>  # Address: 00000034
    if (param2 !== 2) goto label_52;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 10 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr: 12 | <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 18 | <GetByIdShort>: <Reg8: 4, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 23 | <LoadConstString>: <Reg8: 3, string_id: 4758>  # String: '__BC:ControlFlow/ForEachTests/forEachTest/if-middle' (String)
    // USED → r3 = "__BC:ControlFlow/ForEachTests/forEachTest/if-middle";
    // CODE → addr: 27 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 6, Reg8: 3>
    console.log("__BC:ControlFlow/ForEachTests/forEachTest/if-middle")
    // CODE → addr: 32 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 38 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 43 | <LoadConstString>: <Reg8: 2, string_id: 7929>  # String: 'middle' (Identifier)
    // USED → r2 = "middle";
    // CODE → addr: 47 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("middle")
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 52 | <LoadParam>: <Reg8: 4, UInt8: 1>
    // USED → r4 = param1;
    // CODE → addr: 55 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr: 57 | <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 63 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 68 | <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4>
    console.log(param2, param1)
    // CODE → addr: 74 | <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → addr: 76 | <Ret>: <Reg8: 1>
    return r1;
}