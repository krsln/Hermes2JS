function get() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4545>  # String: '__BC:Classes/PrivateStaticTests/Counter/static-get-instanceCount' (String)
    // USED → r0 = "__BC:Classes/PrivateStaticTests/Counter/static-get-instanceCount";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Classes/PrivateStaticTests/Counter/static-get-instanceCount")
    // CODE → addr: 22 | <GetEnvironment>: <Reg8: 0, UInt8: 1>
    r0 = getEnvironment(1)
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 4>
    r1 = r0[4]
    // CODE → addr: 29 | <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r3 = r1.default;
    // CODE → addr: 34 | <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // CODE → addr: 37 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 0>
    r2 = r1[0]
    // CODE → addr: 41 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 6>
    r1 = r0[6]
    // CODE → addr: 45 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr: 47 | <Call3>: <Reg8: 0, Reg8: 3, Reg8: 0, Reg8: 2, Reg8: 1>
    r0 = r1.default.call(r0, r2, r1)
    // CODE → addr: 53 | <GetByVal>: <Reg8: 0, Reg8: 0, Reg8: 1>
    r0 = r0[r1]
    // CODE → addr: 57 | <Ret>: <Reg8: 0>
    return r0;
}