function nestedArrayDestructureTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4811>  # String: '__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start' (String)
    // USED → r0 = "__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start")
    // CODE → addr: 22 | <NewArray>: <Reg8: 3, UInt16: 3>
    r3 = []
    // CODE → addr: 26 | <NewArrayWithBuffer>: <Reg8: 0, UInt16: 2, UInt16: 2, UInt16: 23637>  # Array: [1, 2]
    r0 = [1, 2]
    // CODE → addr: 34 | <PutOwnByIndex>: <Reg8: 3, Reg8: 0, UInt8: 0>
    // USED → r3 = r3[0] = r0;
    // CODE → addr: 38 | <NewArrayWithBuffer>: <Reg8: 0, UInt16: 2, UInt16: 2, UInt16: 12324>  # Array: [3, 4]
    r0 = [3, 4]
    // CODE → addr: 46 | <PutOwnByIndex>: <Reg8: 3, Reg8: 0, UInt8: 1>
    // USED → r3 = (r3[0] = r0)[1] = r0;
    // CODE → addr: 50 | <NewArrayWithBuffer>: <Reg8: 0, UInt16: 2, UInt16: 2, UInt16: 23646>  # Array: [5, 6]
    r0 = [5, 6]
    // CODE → addr: 58 | <PutOwnByIndex>: <Reg8: 3, Reg8: 0, UInt8: 2>
    // USED → r3 = ((r3[0] = r0)[1] = r0)[2] = r0;
    // CODE → addr: 62 | <GetEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getEnvironment(0)
    // CODE → addr: 65 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 2, UInt8: 1>
    r0 = r2[1]
    // CODE → addr: 69 | <GetByIdShort>: <Reg8: 7, Reg8: 0, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r7 = r0.default;
    // CODE → addr: 74 | <LoadConstZero>: <Reg8: 6>
    r6 = 0
    // CODE → addr: 76 | <GetByVal>: <Reg8: 5, Reg8: 3, Reg8: 6>
    // USED → r5 = (((r3[0] = r0)[1] = r0)[2] = r0)[r6];
    // CODE → addr: 80 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 82 | <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    // CODE → addr: 85 | <Call3>: <Reg8: 5, Reg8: 7, Reg8: 0, Reg8: 5, Reg8: 4>
    r5 = r0.default(r5, 2)
    // CODE → addr: 91 | <GetByVal>: <Reg8: 10, Reg8: 5, Reg8: 6>
    // USED → r10 = r5[r6];
    // CODE → addr: 95 | <LoadConstUInt8>: <Reg8: 7, UInt8: 1>
    r7 = 1
    // CODE → addr: 98 | <GetByVal>: <Reg8: 9, Reg8: 5, Reg8: 7>
    // USED → r9 = r5[r7];
    // CODE → addr:102 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 2, UInt8: 1>
    r5 = r2[1]
    // CODE → addr:106 | <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r5 = r5.default;
    // CODE → addr:111 | <GetByVal>: <Reg8: 3, Reg8: 3, Reg8: 4>
    // USED → r3 = (((r3[0] = r0)[1] = r0)[2] = r0)[r4];
    // CODE → addr:115 | <Call3>: <Reg8: 3, Reg8: 5, Reg8: 0, Reg8: 3, Reg8: 4>
    r3 = r5.default.call(r0, r3, 2)
    // CODE → addr:121 | <GetByVal>: <Reg8: 8, Reg8: 3, Reg8: 7>
    // USED → r8 = r3[r7];
    // CODE → addr:125 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:131 | <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:136 | <Call4>: <Reg8: 3, Reg8: 3, Reg8: 5, Reg8: 10, Reg8: 9, Reg8: 8>
    console.log(r10, r9, r8)
    // CODE → addr:143 | <NewArrayWithBuffer>: <Reg8: 3, UInt16: 1, UInt16: 1, UInt16: 23655>  # Array: [10]
    // USED → r3 = [10];
    // CODE → addr:151 | <GetByVal>: <Reg8: 8, Reg8: 3, Reg8: 6>
    r8 = r3[r6]
    // CODE → addr:155 | <LoadConstZero>: <Reg8: 5>
    r5 = (r8 === undefined) ? 0 : r3[r6]
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr:164 | <GetByVal>: <Reg8: 7, Reg8: 3, Reg8: 7>
    r7 = r3[r7]
    // CODE → addr:168 | <LoadConstZero>: <Reg8: 6>
    r6 = (r7 === undefined) ? 0 : r3[r7]
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:177 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 0>
    r2 = r2[0]
    // CODE → addr:181 | <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r2 = r2.default;
    // CODE → addr:186 | <Call2>: <Reg8: 3, Reg8: 2, Reg8: 0, Reg8: 3>
    r3 = r2.default.call(r0, r3)
    // CODE → addr:191 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 4, string_id: 227>  # String: 'slice' (Identifier)
    // USED → r2 = r3.slice;
    // CODE → addr:196 | <Call2>: <Reg8: 4, Reg8: 2, Reg8: 3, Reg8: 4>
    // USED → r4 = r3.slice(2);
    // CODE → addr:201 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:207 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:212 | <Call4>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log(r5, r6, r4)
    // CODE → addr:219 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:225 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:230 | <LoadConstString>: <Reg8: 1, string_id: 4808>  # String: '__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end";
    // CODE → addr:234 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end")
    // CODE → addr:239 | <Ret>: <Reg8: 0>
    return undefined;
}