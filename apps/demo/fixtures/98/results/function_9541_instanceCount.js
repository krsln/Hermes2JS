function instanceCount() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getParentEnvironment(0)
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 1, string_id: 3596>  # String: '__BC:Classes/PrivateStaticTests/Counter/static-get-instanceCount' (String)
    // USED → r1 = "__BC:Classes/PrivateStaticTests/Counter/static-get-instanceCount";
    // CODE → addr: 20 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/PrivateStaticTests/Counter/static-get-instanceCount")
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 2>
    // USED → r1 = r0[2];
    // CODE → addr: 29 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 4>
    r0 = r0[4]
    // CODE → addr: 33 | <GetOwnPrivateBySym>: <Reg8: 0, Reg8: 1, UInt8: 0, Reg8: 0>
    // USED → r0 = r0[2].#__private_0__;
    // CODE → addr: 38 | <Ret>: <Reg8: 0>
    return r0[2].#__private_0__;
}