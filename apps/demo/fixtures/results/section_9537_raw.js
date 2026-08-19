function value() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 316>  # String: '__BC:Classes/PrivateStaticTests/Counter/get-value' (String)
    // USED → r0 = "__BC:Classes/PrivateStaticTests/Counter/get-value";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Classes/PrivateStaticTests/Counter/get-value")
    // CODE → addr: 22 | <GetParentEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getParentEnvironment(0)
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 6>
    r1 = r0[6]
    // CODE → addr: 29 | <LoadParam>: <Reg8: 0, UInt8: 0>
    // USED → r0 = this;
    // CODE → addr: 32 | <GetOwnPrivateBySym>: <Reg8: 0, Reg8: 0, UInt8: 0, Reg8: 1>
    // USED → r0 = this.#__private_1__;
    // CODE → addr: 37 | <Ret>: <Reg8: 0>
    return this.#__private_1__;
}