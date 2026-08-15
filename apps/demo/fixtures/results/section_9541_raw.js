function instanceCount() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getParentEnvironment(0);
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 3596>  # String: '__BC:Classes/PrivateStaticTests/Counter/static-get-instanceCount' (String)
    // USED → r1 = "__BC:Classes/PrivateStaticTests/Counter/static-get-instanceCount";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/PrivateStaticTests/Counter/static-get-instanceCount")
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 2>
    // USED → r1 = getParentEnvironment(0)[2];
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 4>
    r0 = getParentEnvironment(0)[4]
    // CODE → <GetOwnPrivateBySym>: <Reg8: 0, Reg8: 1, UInt8: 0, Reg8: 0>
    // USED → r0 = getParentEnvironment(0)[2].#__private_0__;
    // CODE → <Ret>: <Reg8: 0>
    return getParentEnvironment(0)[2].#__private_0__;
}