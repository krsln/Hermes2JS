function describe(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 3777>  # String: '__BC:Classes/PrivateStaticTests/Counter/describe' (String)
    // USED → r0 = "__BC:Classes/PrivateStaticTests/Counter/describe";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Classes/PrivateStaticTests/Counter/describe")
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 1>
    // USED → r0 = getEnvironment(1);
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 4>
    // USED → r1 = getEnvironment(1)[4];
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r3 = getEnvironment(1)[4].default;
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 7>
    // USED → r0 = getEnvironment(1)[7];
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this;
    // CODE → <Call3>: <Reg8: 1, Reg8: 3, Reg8: 2, Reg8: 1, Reg8: 0>
    // USED → r1 = getEnvironment(1)[4].default.call(undefined, this, getEnvironment(1)[7]);
    // CODE → <GetByVal>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = getEnvironment(1)[4].default.call(undefined, this, getEnvironment(1)[7])[getEnvironment(1)[7]];
    // CODE → <Call1>: <Reg8: 0, Reg8: 0, Reg8: 1>
    // USED → r0 = getEnvironment(1)[4].default.call(undefined, this, getEnvironment(1)[7])[getEnvironment(1)[7]]();
    // CODE → <Ret>: <Reg8: 0>
    return getEnvironment(1)[4].default.call(undefined, this, getEnvironment(1)[7])[getEnvironment(1)[7]]();
}