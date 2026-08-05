function Counter(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 8, UInt8: 0>
    // USED → r8 = this;
    // CODE → <GetEnvironment>: <Reg8: 3, UInt8: 1>
    // USED → r3 = getEnvironment(1);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = getEnvironment(1)[2];
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r1 = getEnvironment(1)[2].default;
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 0>
    // USED → r2 = getEnvironment(0)[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 0, Reg8: 8, Reg8: 2>
    r1 = getEnvironment(1)[2].default.call(undefined, this, getEnvironment(0)[0])
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 1, UInt8: 2, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r7 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 3, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r6 = globalThis.Object.defineProperty;
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 7>
    // USED → r5 = getEnvironment(1)[7];
    // CODE → <NewObject>: <Reg8: 4>
    // USED → r4 = {  };
    // CODE → <LoadFromEnvironment>: <Reg8: 9, Reg8: 3, UInt8: 11>
    // USED → r9 = getEnvironment(1)[11];
    // CODE → <PutNewOwnByIdShort>: <Reg8: 4, Reg8: 9, string_id: 205>  # String: 'value' (Identifier)
    // USED → r4 = { value: getEnvironment(1)[11] };
    // CODE → <Call4>: <Reg8: 4, Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 5, Reg8: 4>
    r4 = globalThis.Object.defineProperty(this, getEnvironment(1)[7], { value: getEnvironment(1)[11] })
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 1, UInt8: 2, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r7 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 3, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r6 = globalThis.Object.defineProperty;
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 5>
    // USED → r5 = getEnvironment(1)[5];
    // CODE → <NewObjectWithBuffer>: <Reg8: 4, UInt16: 2, UInt16: 2, UInt16: 43, UInt16: 45>  # Object: {'writable': true, 'value': 0}
    // USED → r4 = { "writable": true, "value": 0 };
    // CODE → <Call4>: <Reg8: 4, Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 5, Reg8: 4>
    r4 = globalThis.Object.defineProperty(this, getEnvironment(1)[5], { "writable": true, "value": 0 })
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 4, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 5, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 290>  # String: '__BC:Classes/PrivateStaticTests/Counter/constructor' (String)
    // USED → r1 = "__BC:Classes/PrivateStaticTests/Counter/constructor";
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 5, Reg8: 1>
    r1 = globalThis.console.log("__BC:Classes/PrivateStaticTests/Counter/constructor")
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 3, UInt8: 4>
    // USED → r1 = getEnvironment(1)[4];
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r1 = getEnvironment(1)[4].default;
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 3, UInt8: 6>
    // USED → r3 = getEnvironment(1)[6];
    // CODE → <Call3>: <Reg8: 2, Reg8: 1, Reg8: 0, Reg8: 2, Reg8: 3>
    // USED → r2 = getEnvironment(1)[4].default.call(undefined, getEnvironment(0)[0], getEnvironment(1)[6]);
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 2, Reg8: 3>
    r1 = getEnvironment(1)[4].default.call(undefined, getEnvironment(0)[0], getEnvironment(1)[6])[getEnvironment(1)[6]]
    // CODE → <Inc>: <Reg8: 1, Reg8: 1>
    // USED → r1 = r1 + 1;
    // CODE → <PutByVal>: <Reg8: 2, Reg8: 3, Reg8: 1>
    getEnvironment(1)[4].default.call(undefined, getEnvironment(0)[0], getEnvironment(1)[6])[getEnvironment(1)[6]] = r1 + 1
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}