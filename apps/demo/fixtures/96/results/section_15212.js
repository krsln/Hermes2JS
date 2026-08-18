function set(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4543>  # String: '__BC:Classes/PrivateStaticTests/Counter/set-value' (String)
    // USED → r0 = "__BC:Classes/PrivateStaticTests/Counter/set-value";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Classes/PrivateStaticTests/Counter/set-value")
    // CODE → <GetEnvironment>: <Reg8: 2, UInt8: 1>
    r2 = getEnvironment(1)
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 2, UInt8: 4>
    // USED → r0 = r2[4];
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 0, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r5 = r2[4].default;
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 5>
    // USED → r4 = r2[5];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 0>
    // USED → r3 = this;
    // CODE → <Call3>: <Reg8: 3, Reg8: 5, Reg8: 0, Reg8: 3, Reg8: 4>
    r3 = r2[4].default.call(undefined, this, r4)
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 5>
    // USED → r2 = r2[5];
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 4, string_id: 21>  # String: 'Math' (Identifier)
    // USED → r6 = Math;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 5, string_id: 113>  # String: 'min' (Identifier)
    // USED → r5 = Math.min;
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 0>
    // USED → r1 = r1[0];
    // CODE → <GetById>: <Reg8: 4, Reg8: 1, UInt8: 6, string_id: 11547>  # String: 'MAX' (Identifier)
    // USED → r4 = r1[0].MAX;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → <Call3>: <Reg8: 1, Reg8: 5, Reg8: 6, Reg8: 1, Reg8: 4>
    r1 = Math.min(param1, r4)
    // CODE → <PutByVal>: <Reg8: 3, Reg8: 2, Reg8: 1>
    r3[r2[5]] = r1
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}