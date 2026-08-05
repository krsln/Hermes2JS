function increment(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 0>
    // USED → r2 = this;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4729>  # String: '__BC:Classes/PrivateStaticTests/Counter/increment' (String)
    // USED → r0 = "__BC:Classes/PrivateStaticTests/Counter/increment";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Classes/PrivateStaticTests/Counter/increment")
    // CODE → <GetParentEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getParentEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 6>
    r1 = getParentEnvironment(0)[6]
    // CODE → <GetOwnPrivateBySym>: <Reg8: 0, Reg8: 2, UInt8: 0, Reg8: 1>
    r0 = this.#__private_1__
    // CODE → <Inc>: <Reg8: 0, Reg8: 0>
    // USED → r0 = r0 + 1;
    // CODE → <PutOwnPrivateBySym>: <Reg8: 2, Reg8: 0, UInt8: 0, Reg8: 1>
    this.#__private_1__ = r0 + 1
    // CODE → <Ret>: <Reg8: 0>
    return r0 + 1;
}