function delay(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 0, string_id: 26>  # String: 'Promise' (Identifier)
    // USED → r2 = globalThis.Promise;
    // CODE → <GetById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 7302>  # String: 'resolve' (Identifier)
    // USED → r1 = globalThis.Promise.resolve;
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    // USED → r0 = globalThis.Promise.resolve(r0);
    // CODE → <Ret>: <Reg8: 0>
    return globalThis.Promise.resolve(r0);
}