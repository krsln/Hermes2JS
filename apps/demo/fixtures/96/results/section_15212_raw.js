function set(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4543>  # String: '__BC:Classes/PrivateStaticTests/Counter/set-value' (String)
    // USED → r0 = "__BC:Classes/PrivateStaticTests/Counter/set-value";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Classes/PrivateStaticTests/Counter/set-value")
    // CODE → addr: 22 | <GetEnvironment>: <Reg8: 2, UInt8: 1>
    r2 = getEnvironment(1)
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 2, UInt8: 4>
    r0 = r2[4]
    // CODE → addr: 29 | <GetByIdShort>: <Reg8: 5, Reg8: 0, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r5 = r0.default;
    // CODE → addr: 34 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 5>
    r4 = r2[5]
    // CODE → addr: 38 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr: 40 | <LoadParam>: <Reg8: 3, UInt8: 0>
    // USED → r3 = this;
    // CODE → addr: 43 | <Call3>: <Reg8: 3, Reg8: 5, Reg8: 0, Reg8: 3, Reg8: 4>
    r3 = r0.default(this, r4)
    // CODE → addr: 49 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 5>
    // USED → r2 = r2[5];
    // CODE → addr: 53 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 4, string_id: 21>  # String: 'Math' (Identifier)
    // USED → r6 = Math;
    // CODE → addr: 59 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 5, string_id: 113>  # String: 'min' (Identifier)
    // USED → r5 = Math.min;
    // CODE → addr: 64 | <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // CODE → addr: 67 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 0>
    r1 = r1[0]
    // CODE → addr: 71 | <GetById>: <Reg8: 4, Reg8: 1, UInt8: 6, string_id: 11547>  # String: 'MAX' (Identifier)
    // USED → r4 = r1.MAX;
    // CODE → addr: 77 | <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → addr: 80 | <Call3>: <Reg8: 1, Reg8: 5, Reg8: 6, Reg8: 1, Reg8: 4>
    r1 = Math.min(param1, r1.MAX)
    // CODE → addr: 86 | <PutByVal>: <Reg8: 3, Reg8: 2, Reg8: 1>
    r3[r2[5]] = r1
    // CODE → addr: 90 | <Ret>: <Reg8: 0>
    return r0;
}