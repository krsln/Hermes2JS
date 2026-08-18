function delay(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 27>  # String: 'Promise' (Identifier)
    // USED → r2 = Promise;
    // CODE → <GetById>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 8040>  # String: 'resolve' (Identifier)
    // USED → r1 = Promise.resolve;
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = Promise.resolve(param1)
    // CODE → <Ret>: <Reg8: 0>
    return r0;
}