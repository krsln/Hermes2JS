function nestedArrayDestructureTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4811>  # String: '__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start' (String)
    // USED → r0 = "__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start")
    // CODE → <NewArray>: <Reg8: 3, UInt16: 3>
    r3 = []
    // CODE → <NewArrayWithBuffer>: <Reg8: 0, UInt16: 2, UInt16: 2, UInt16: 23637>  # Array: [1, 2]
    r0 = [1, 2]
    // CODE → <PutOwnByIndex>: <Reg8: 3, Reg8: 0, UInt8: 0>
    // USED → r3 = r3[0] = r0;
    // CODE → <NewArrayWithBuffer>: <Reg8: 0, UInt16: 2, UInt16: 2, UInt16: 12324>  # Array: [3, 4]
    r0 = [3, 4]
    // CODE → <PutOwnByIndex>: <Reg8: 3, Reg8: 0, UInt8: 1>
    // USED → r3 = (r3[0] = r0)[1] = r0;
    // CODE → <NewArrayWithBuffer>: <Reg8: 0, UInt16: 2, UInt16: 2, UInt16: 23646>  # Array: [5, 6]
    r0 = [5, 6]
    // CODE → <PutOwnByIndex>: <Reg8: 3, Reg8: 0, UInt8: 2>
    // USED → r3 = ((r3[0] = r0)[1] = r0)[2] = r0;
    // CODE → <GetEnvironment>: <Reg8: 2, UInt8: 0>
    // USED → r2 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 2, UInt8: 1>
    // USED → r0 = getEnvironment(0)[1];
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 0, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r7 = getEnvironment(0)[1].default;
    // CODE → <LoadConstZero>: <Reg8: 6>
    // USED → r6 = 0;
    // CODE → <GetByVal>: <Reg8: 5, Reg8: 3, Reg8: 6>
    // USED → r5 = (((r3[0] = r0)[1] = r0)[2] = r0)[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    // CODE → <Call3>: <Reg8: 5, Reg8: 7, Reg8: 0, Reg8: 5, Reg8: 4>
    // USED → r5 = getEnvironment(0)[1].default.call(undefined, (((r3[0] = r0)[1] = r0)[2] = r0)[0], 2);
    // CODE → <GetByVal>: <Reg8: 10, Reg8: 5, Reg8: 6>
    // USED → r10 = getEnvironment(0)[1].default.call(undefined, (((r3[0] = r0)[1] = r0)[2] = r0)[0], 2)[0];
    // CODE → <LoadConstUInt8>: <Reg8: 7, UInt8: 1>
    // USED → r7 = 1;
    // CODE → <GetByVal>: <Reg8: 9, Reg8: 5, Reg8: 7>
    // USED → r9 = getEnvironment(0)[1].default.call(undefined, (((r3[0] = r0)[1] = r0)[2] = r0)[0], 2)[1];
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 2, UInt8: 1>
    // USED → r5 = getEnvironment(0)[1];
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r5 = getEnvironment(0)[1].default;
    // CODE → <GetByVal>: <Reg8: 3, Reg8: 3, Reg8: 4>
    // USED → r3 = (((r3[0] = r0)[1] = r0)[2] = r0)[2];
    // CODE → <Call3>: <Reg8: 3, Reg8: 5, Reg8: 0, Reg8: 3, Reg8: 4>
    // USED → r3 = getEnvironment(0)[1].default.call(undefined, (((r3[0] = r0)[1] = r0)[2] = r0)[2], 2);
    // CODE → <GetByVal>: <Reg8: 8, Reg8: 3, Reg8: 7>
    // USED → r8 = getEnvironment(0)[1].default.call(undefined, (((r3[0] = r0)[1] = r0)[2] = r0)[2], 2)[1];
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <Call4>: <Reg8: 3, Reg8: 3, Reg8: 5, Reg8: 10, Reg8: 9, Reg8: 8>
    console.log(getEnvironment(0)[1].default.call(undefined, (((r3[0] = r0)[1] = r0)[2] = r0)[0], 2)[0], getEnvironment(0)[1].default.call(undefined, (((r3[0] = r0)[1] = r0)[2] = r0)[0], 2)[1], getEnvironment(0)[1].default.call(undefined, (((r3[0] = r0)[1] = r0)[2] = r0)[2], 2)[1])
    // CODE → <NewArrayWithBuffer>: <Reg8: 3, UInt16: 1, UInt16: 1, UInt16: 23655>  # Array: [10]
    r3 = [10]
    // CODE → <GetByVal>: <Reg8: 8, Reg8: 3, Reg8: 6>
    // USED → r8 = r3[0];
    // CODE → <LoadConstZero>: <Reg8: 5>
    r5 = (r8 === r0) ? 0 : r3[0]
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetByVal>: <Reg8: 7, Reg8: 3, Reg8: 7>
    // USED → r7 = r3[1];
    // CODE → <LoadConstZero>: <Reg8: 6>
    r6 = (r7 === r0) ? 0 : r3[1]
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 0>
    // USED → r2 = getEnvironment(0)[0];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r2 = getEnvironment(0)[0].default;
    // CODE → <Call2>: <Reg8: 3, Reg8: 2, Reg8: 0, Reg8: 3>
    // USED → r3 = getEnvironment(0)[0].default.call(undefined, r3);
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 4, string_id: 227>  # String: 'slice' (Identifier)
    // USED → r2 = getEnvironment(0)[0].default.call(undefined, r3).slice;
    // CODE → <Call2>: <Reg8: 4, Reg8: 2, Reg8: 3, Reg8: 4>
    // USED → r4 = getEnvironment(0)[0].default.call(undefined, r3).slice(2);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call4>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log((r8 === r0) ? 0 : r3[0], (r7 === r0) ? 0 : r3[1], getEnvironment(0)[0].default.call(undefined, r3).slice(2))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4808>  # String: '__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}