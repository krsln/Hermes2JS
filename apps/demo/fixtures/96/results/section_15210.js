function Counter() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 8, UInt8: 0>
    // USED → r8 = this;
    // CODE → addr:  3 | <GetEnvironment>: <Reg8: 3, UInt8: 1>
    r3 = getEnvironment(1)
    // CODE → addr:  6 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 3, UInt8: 2>
    r0 = r3[2]
    // CODE → addr: 10 | <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r1 = r0.default;
    // CODE → addr: 15 | <GetEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getEnvironment(0)
    // CODE → addr: 18 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 0>
    // USED → r2 = r0[0];
    // CODE → addr: 22 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 24 | <Call3>: <Reg8: 1, Reg8: 1, Reg8: 0, Reg8: 8, Reg8: 2>
    r1 = r0.default(this, r2)
    // CODE → addr: 30 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr: 32 | <TryGetById>: <Reg8: 7, Reg8: 1, UInt8: 2, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r7 = Object;
    // CODE → addr: 38 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 3, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r6 = Object.defineProperty;
    // CODE → addr: 43 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 7>
    // USED → r5 = r3[7];
    // CODE → addr: 47 | <NewObject>: <Reg8: 4>
    // USED → r4 = {  };
    // CODE → addr: 49 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 3, UInt8: 11>
    // USED → r9 = r3[11];
    // CODE → addr: 53 | <PutNewOwnByIdShort>: <Reg8: 4, Reg8: 9, string_id: 205>  # String: 'value' (Identifier)
    r4.value = r3[11]
    // CODE → addr: 57 | <Call4>: <Reg8: 4, Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 5, Reg8: 4>
    r4 = Object.defineProperty(this, r5, r4)
    // CODE → addr: 64 | <TryGetById>: <Reg8: 7, Reg8: 1, UInt8: 2, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r7 = Object;
    // CODE → addr: 70 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 3, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r6 = Object.defineProperty;
    // CODE → addr: 75 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 5>
    // USED → r5 = r3[5];
    // CODE → addr: 79 | <NewObjectWithBuffer>: <Reg8: 4, UInt16: 2, UInt16: 2, UInt16: 43, UInt16: 45>  # Object: {'writable': true, 'value': 0}
    // USED → r4 = { "writable": true, "value": 0 };
    // CODE → addr: 89 | <Call4>: <Reg8: 4, Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 5, Reg8: 4>
    r4 = Object.defineProperty(this, r5, r4)
    // CODE → addr: 96 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 4, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:102 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 5, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:107 | <LoadConstString>: <Reg8: 1, string_id: 290>  # String: '__BC:Classes/PrivateStaticTests/Counter/constructor' (String)
    // USED → r1 = "__BC:Classes/PrivateStaticTests/Counter/constructor";
    // CODE → addr:111 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 5, Reg8: 1>
    console.log("__BC:Classes/PrivateStaticTests/Counter/constructor")
    // CODE → addr:116 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 3, UInt8: 4>
    r1 = r3[4]
    // CODE → addr:120 | <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r1 = r1.default;
    // CODE → addr:125 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 3, UInt8: 6>
    // USED → r3 = r3[6];
    // CODE → addr:129 | <Call3>: <Reg8: 2, Reg8: 1, Reg8: 0, Reg8: 2, Reg8: 3>
    r2 = r1.default.call(r0, r2, r3)
    // CODE → addr:135 | <GetByVal>: <Reg8: 1, Reg8: 2, Reg8: 3>
    r1 = r2[r3]
    // CODE → addr:139 | <Inc>: <Reg8: 1, Reg8: 1>
    // USED → r1 = r1 + 1;
    // CODE → addr:142 | <PutByVal>: <Reg8: 2, Reg8: 3, Reg8: 1>
    r2[r3[6]] = r1 + 1
    // CODE → addr:146 | <Ret>: <Reg8: 0>
    return undefined;
}