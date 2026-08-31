function _privateHelper2() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 4>
    r1 = r0[4]
    // CODE → addr:  7 | <GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r4 = r1.default;
    // CODE → addr: 12 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 0, UInt8: 5>
    r3 = r0[5]
    // CODE → addr: 16 | <LoadConstUndefined>: <Reg8: 2>
    r2 = undefined
    // CODE → addr: 18 | <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this;
    // CODE → addr: 21 | <Call3>: <Reg8: 1, Reg8: 4, Reg8: 2, Reg8: 1, Reg8: 3>
    r1 = r1.default.call(r2, this, r3)
    // CODE → addr: 27 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 5>
    r0 = r0[5]
    // CODE → addr: 31 | <GetByVal>: <Reg8: 2, Reg8: 1, Reg8: 0>
    r2 = r1[r0]
    // CODE → addr: 35 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr: 37 | <TryGetById>: <Reg8: 0, Reg8: 0, UInt8: 2, string_id: 14>  # String: 'HermesInternal' (Identifier)
    // USED → r0 = HermesInternal;
    // CODE → addr: 43 | <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 96>  # String: 'concat' (Identifier)
    // USED → r1 = HermesInternal.concat;
    // CODE → addr: 48 | <LoadConstString>: <Reg8: 0, string_id: 5460>  # String: 'count=' (String)
    // USED → r0 = "count=";
    // CODE → addr: 52 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 0, Reg8: 2>
    r0 = HermesInternal.concat.call("count=", r2)
    // CODE → addr: 57 | <Ret>: <Reg8: 0>
    return r0;
}