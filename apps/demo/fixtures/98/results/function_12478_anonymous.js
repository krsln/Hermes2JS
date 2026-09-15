function function_12478(param1, param2, param3) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 5, UInt8: 3>
    r5 = param3
    // CODE → addr:  3 | <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED → r2 = param2;
    // CODE → addr:  6 | <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → addr:  9 | <Add>: <Reg8: 2, Reg8: 1, Reg8: 2>
    // USED → r2 = param1 + param2;
    // CODE → addr: 13 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → addr: 16 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 1, UInt8: 0>
    // USED → r3 = r1[0];
    // CODE → addr: 20 | <GetByVal>: <Reg8: 4, Reg8: 3, Reg8: 5>
    r4 = r1[0][param3]
    // CODE → addr: 24 | <LoadConstString>: <Reg8: 1, string_id: 6457>  # String: '' (Identifier)
    r1 = ""
    // CODE → addr: 28 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    if (r4 !== undefined) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 34 | <GetGlobalObject>: <Reg8: 4>
        // USED → r4 = globalThis;
        // CODE → addr: 36 | <TryGetById>: <Reg8: 4, Reg8: 4, UInt8: 0, string_id: 33>  # String: 'String' (Identifier)
        // USED → r4 = String;
        // CODE → addr: 42 | <GetByVal>: <Reg8: 3, Reg8: 3, Reg8: 5>
        r3 = r1[0][param3]
        // CODE → addr: 46 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 3>
        r1 = String.call(r0, r3)
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 51 | <Add>: <Reg8: 1, Reg8: 2, Reg8: 1>
    // USED → r1 = param1 + param2 + r1;
    // CODE → addr: 55 | <Ret>: <Reg8: 1>
    return param1 + param2 + r1;
}