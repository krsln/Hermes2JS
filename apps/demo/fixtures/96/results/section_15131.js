function function_15131(param1, param2, param3) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 3>
    r5 = param3
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 2>
    // USED → r0 = param2;
    // CODE → <Add>: <Reg8: 1, Reg8: 1, Reg8: 0>
    // USED → r1 = param1 + param2;
    // CODE → <GetEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getEnvironment(0)
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 2, UInt8: 0>
    // USED → r0 = r2[0];
    // CODE → <GetByVal>: <Reg8: 3, Reg8: 0, Reg8: 5>
    r3 = r2[0][r5]
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 7163>  # String: '' (Identifier)
    r0 = ""
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    // USED → r4 = undefined;
    // → r3 = r2[0][r5]
    if (r3 !== undefined) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetGlobalObject>: <Reg8: 3>
        // USED → r3 = globalThis;
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 3, UInt8: 1, string_id: 34>  # String: 'String' (Identifier)
        // USED → r3 = String;
        // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 0>
        // USED → r2 = r2[0];
        // CODE → <GetByVal>: <Reg8: 2, Reg8: 2, Reg8: 5>
        // USED → r2 = r2[0][r5];
        // CODE → <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 2>
        r0 = String.call(r4, r2)
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Add>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = param1 + param2 + r0;
    // CODE → <Ret>: <Reg8: 0>
    return param1 + param2 + r0;
}