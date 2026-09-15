function increment() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 2, UInt8: 0>
    // USED → r2 = this;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 1, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 0, string_id: 4729>  # String: '__BC:Classes/PrivateStaticTests/Counter/increment' (String)
    // USED → r0 = "__BC:Classes/PrivateStaticTests/Counter/increment";
    // CODE → addr: 20 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 3, Reg8: 0>
    console.log("__BC:Classes/PrivateStaticTests/Counter/increment")
    // CODE → addr: 25 | <GetParentEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getParentEnvironment(0)
    // CODE → addr: 28 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 6>
    r1 = r0[6]
    // CODE → addr: 32 | <GetOwnPrivateBySym>: <Reg8: 0, Reg8: 2, UInt8: 0, Reg8: 1>
    r0 = this.#__private_1__
    // CODE → addr: 37 | <Inc>: <Reg8: 0, Reg8: 0>
    // USED → r0 = r0 + 1;
    // CODE → addr: 40 | <PutOwnPrivateBySym>: <Reg8: 2, Reg8: 0, UInt8: 0, Reg8: 1>
    this.#__private_1__ = r0 + 1
    // CODE → addr: 45 | <Ret>: <Reg8: 0>
    return r0;
}