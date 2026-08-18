function reset() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4548>  # String: '__BC:Classes/PrivateStaticTests/Counter/static-reset' (String)
    // USED → r0 = "__BC:Classes/PrivateStaticTests/Counter/static-reset";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Classes/PrivateStaticTests/Counter/static-reset")
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 1>
    // USED → r0 = getEnvironment(1);
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 4>
    // USED → r1 = getEnvironment(1)[4];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r2 = getEnvironment(1)[4].default;
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0)[0];
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 0, UInt8: 6>
    // USED → r3 = getEnvironment(1)[6];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call3>: <Reg8: 2, Reg8: 2, Reg8: 0, Reg8: 1, Reg8: 3>
    // USED → r2 = getEnvironment(1)[4].default.call(undefined, r1, r3);
    // CODE → <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // CODE → <PutByVal>: <Reg8: 2, Reg8: 3, Reg8: 1>
    getEnvironment(1)[4].default.call(undefined, r1, r3)[getEnvironment(1)[6]] = 0
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}