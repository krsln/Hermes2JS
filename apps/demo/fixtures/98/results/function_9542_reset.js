function reset() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getParentEnvironment(0)
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 3, string_id: 4732>  # String: '__BC:Classes/PrivateStaticTests/Counter/static-reset' (String)
    // USED → r3 = "__BC:Classes/PrivateStaticTests/Counter/static-reset";
    // CODE → addr: 20 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Classes/PrivateStaticTests/Counter/static-reset")
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 2>
    // USED → r3 = r2[2];
    // CODE → addr: 29 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 4>
    r2 = r2[4]
    // CODE → addr: 33 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr: 35 | <PutOwnPrivateBySym>: <Reg8: 3, Reg8: 0, UInt8: 0, Reg8: 2>
    r2[2].#__private_2__ = 0
    // CODE → addr: 40 | <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → addr: 42 | <Ret>: <Reg8: 1>
    return undefined;
}