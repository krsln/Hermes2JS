function function_15131(param1, param2, param3) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 5, UInt8: 3>
    r5 = param3
    // CODE → addr:  3 | <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → addr:  6 | <LoadParam>: <Reg8: 0, UInt8: 2>
    // USED → r0 = param2;
    // CODE → addr:  9 | <Add>: <Reg8: 1, Reg8: 1, Reg8: 0>
    // USED → r1 = param1 + param2;
    // CODE → addr: 13 | <GetEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getEnvironment(0)
    // CODE → addr: 16 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 2, UInt8: 0>
    // USED → r0 = r2[0];
    // CODE → addr: 20 | <GetByVal>: <Reg8: 3, Reg8: 0, Reg8: 5>
    r3 = r2[0][r5]
    // CODE → addr: 24 | <LoadConstString>: <Reg8: 0, string_id: 7163>  # String: '' (Identifier)
    r0 = ""
    // CODE → addr: 28 | <LoadConstUndefined>: <Reg8: 4>
    // USED → r4 = undefined;
    // CODE → addr: 30 | <JStrictEqual>: <Addr8: 25, Reg8: 3, Reg8: 4>  # Address: 00000037
    // → r3 = r2[0][r5]
    if (r3 === undefined) goto label_55;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 34 | <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → addr: 36 | <TryGetById>: <Reg8: 3, Reg8: 3, UInt8: 1, string_id: 34>  # String: 'String' (Identifier)
    // USED → r3 = String;
    // CODE → addr: 42 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 0>
    // USED → r2 = r2[0];
    // CODE → addr: 46 | <GetByVal>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = r2[0][r5];
    // CODE → addr: 50 | <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 2>
    r0 = String.call(r4, r2)
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 55 | <Add>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = param1 + param2 + r0;
    // CODE → addr: 59 | <Ret>: <Reg8: 0>
    return param1 + param2 + r0;
}