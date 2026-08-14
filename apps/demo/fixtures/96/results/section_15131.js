function function_15131(param1, param2, param3) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 3>
    // USED → r5 = param3;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 2>
    // USED → r0 = param2;
    // CODE → <Add>: <Reg8: 1, Reg8: 1, Reg8: 0>
    // USED → r1 = param1 + param2;
    // CODE → <GetEnvironment>: <Reg8: 2, UInt8: 0>
    // USED → r2 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 2, UInt8: 0>
    // USED → r0 = getEnvironment(0)[0];
    // CODE → <GetByVal>: <Reg8: 3, Reg8: 0, Reg8: 5>
    // USED → r3 = getEnvironment(0)[0][param3];
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 7163>  # String: '' (Identifier)
    r0 = (r3 === undefined) ? "" : globalThis.String.call(undefined, r2)
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    // USED → r4 = undefined;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Add>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = param1 + param2 + ((r3 === undefined) ? "" : globalThis.String.call(undefined, r2));
    // CODE → <Ret>: <Reg8: 0>
    return param1 + param2 + ((r3 === undefined) ? "" : globalThis.String.call(undefined, r2));
}