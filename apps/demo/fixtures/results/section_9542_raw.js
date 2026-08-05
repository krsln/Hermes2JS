function reset(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
    // USED → r2 = getParentEnvironment(0);
    // CODE → <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4732>  # String: '__BC:Classes/PrivateStaticTests/Counter/static-reset' (String)
    // USED → r3 = "__BC:Classes/PrivateStaticTests/Counter/static-reset";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:Classes/PrivateStaticTests/Counter/static-reset")
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 2>
    // USED → r3 = getParentEnvironment(0)[2];
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 4>
    r2 = getParentEnvironment(0)[4]
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <PutOwnPrivateBySym>: <Reg8: 3, Reg8: 0, UInt8: 0, Reg8: 2>
    getParentEnvironment(0)[2].#__private_2__ = 0
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}