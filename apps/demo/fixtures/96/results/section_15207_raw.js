function _privateHelper2(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 4>
    // USED → r1 = getEnvironment(0)[4];
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r4 = getEnvironment(0)[4].default;
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 0, UInt8: 5>
    // USED → r3 = getEnvironment(0)[5];
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this;
    // CODE → <Call3>: <Reg8: 1, Reg8: 4, Reg8: 2, Reg8: 1, Reg8: 3>
    // USED → r1 = getEnvironment(0)[4].default.call(undefined, r1, r3);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 5>
    // USED → r0 = getEnvironment(0)[5];
    // CODE → <GetByVal>: <Reg8: 2, Reg8: 1, Reg8: 0>
    // USED → r2 = getEnvironment(0)[4].default.call(undefined, r1, r3)[getEnvironment(0)[5]];
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 0, Reg8: 0, UInt8: 2, string_id: 14>  # String: 'HermesInternal' (Identifier)
    // USED → r0 = globalThis.HermesInternal;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 96>  # String: 'concat' (Identifier)
    // USED → r1 = globalThis.HermesInternal.concat;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 5460>  # String: 'count=' (String)
    // USED → r0 = "count=";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 0, Reg8: 2>
    // USED → r0 = globalThis.HermesInternal.concat.call("count=", r2);
    // CODE → <Ret>: <Reg8: 0>
    return globalThis.HermesInternal.concat.call("count=", r2);
}