function describe() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 3777>  # String: '__BC:Classes/PrivateStaticTests/Counter/describe' (String)
    // USED → r0 = "__BC:Classes/PrivateStaticTests/Counter/describe";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Classes/PrivateStaticTests/Counter/describe")
    // CODE → addr: 22 | <GetEnvironment>: <Reg8: 0, UInt8: 1>
    r0 = getEnvironment(1)
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 4>
    r1 = r0[4]
    // CODE → addr: 29 | <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r3 = r1.default;
    // CODE → addr: 34 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 7>
    r0 = r0[7]
    // CODE → addr: 38 | <LoadConstUndefined>: <Reg8: 2>
    r2 = undefined
    // CODE → addr: 40 | <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this;
    // CODE → addr: 43 | <Call3>: <Reg8: 1, Reg8: 3, Reg8: 2, Reg8: 1, Reg8: 0>
    r1 = r1.default.call(r2, this, r0)
    // CODE → addr: 49 | <GetByVal>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = r1[r0];
    // CODE → addr: 53 | <Call1>: <Reg8: 0, Reg8: 0, Reg8: 1>
    r0 = r1[r0]()
    // CODE → addr: 57 | <Ret>: <Reg8: 0>
    return r0;
}