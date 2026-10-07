function nestedArrayDestructureTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUndefined>: <Reg8: 3>
    // USED → r3 = undefined;
    // CODE → addr:  8 | <GetGlobalObject>: <Reg8: 10>
    // USED → r10 = globalThis;
    // CODE → addr: 10 | <TryGetById>: <Reg8: 4, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 16 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 21 | <LoadConstString>: <Reg8: 1, string_id: 4967>  # String: '__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start";
    // CODE → addr: 25 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
    console.log("__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start");
    // CODE → addr: 30 | <NewArray>: <Reg8: 2, UInt16: 3>
    r2 = [];
    // CODE → addr: 34 | <NewArrayWithBuffer>: <Reg8: 1, UInt16: 2, UInt16: 2, UInt16: 42665>  # Array: [1, 2]
    r1 = [1, 2];
    // CODE → addr: 42 | <DefineOwnInDenseArray>: <Reg8: 2, Reg8: 1, UInt8: 0>
    r2[0] = r1;
    // CODE → addr: 46 | <NewArrayWithBuffer>: <Reg8: 1, UInt16: 2, UInt16: 2, UInt16: 48477>  # Array: [3, 4]
    r1 = [3, 4];
    // CODE → addr: 54 | <DefineOwnInDenseArray>: <Reg8: 2, Reg8: 1, UInt8: 1>
    r2[1] = r1;
    // CODE → addr: 58 | <NewArrayWithBuffer>: <Reg8: 1, UInt16: 2, UInt16: 2, UInt16: 15101>  # Array: [5, 6]
    r1 = [5, 6];
    // CODE → addr: 66 | <DefineOwnInDenseArray>: <Reg8: 2, Reg8: 1, UInt8: 2>
    r2[2] = r1;
    // CODE → addr: 70 | <Mov>: <Reg8: 6, Reg8: 2>
    r6 = r2;
    // CODE → addr: 73 | <IteratorBegin>: <Reg8: 1, Reg8: 6>
    [[r8, r7], , [, r0]] = r6;
    // CODE → addr:126 | <Mov>: <Reg8: 8, Reg8: 9>
    // CODE → addr:159 | <Mov>: <Reg8: 7, Reg8: 9>
    // CODE → addr:271 | <Mov>: <Reg8: 0, Reg8: 11>
    // ──────────────── Block 21 ──────────────── 
    // CODE → addr:292 | <TryGetById>: <Reg8: 11, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → addr:298 | <GetByIdShort>: <Reg8: 9, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr:303 | <Call4>: <Reg8: 0, Reg8: 9, Reg8: 11, Reg8: 8, Reg8: 7, Reg8: 0>
    console.log(r8, r7, r0);
    // CODE → addr:310 | <NewArrayWithBuffer>: <Reg8: 17, UInt16: 1, UInt16: 1, UInt16: 20024>  # Array: [10]
    r17 = [10];
    // CODE → addr:318 | <IteratorBegin>: <Reg8: 7, Reg8: 17>
    [r15 = 0, r14 = 0, ...r13] = r17;
    // CODE → addr:349 | <Mov>: <Reg8: 15, Reg8: 12>
    // CODE → addr:410 | <Mov>: <Reg8: 14, Reg8: 12>
    // CODE → addr:413 | <NewArray>: <Reg8: 13, UInt16: 0>
    // ──────────────── Block 34 ──────────────── 
    // CODE → addr:462 | <TryGetById>: <Reg8: 12, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r12 = console;
    // CODE → addr:468 | <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r11 = console.log;
    // CODE → addr:473 | <Call4>: <Reg8: 11, Reg8: 11, Reg8: 12, Reg8: 15, Reg8: 14, Reg8: 13>
    console.log(r15, r14, r13);
    // CODE → addr:480 | <TryGetById>: <Reg8: 12, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r12 = console;
    // CODE → addr:486 | <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r11 = console.log;
    // CODE → addr:491 | <LoadConstString>: <Reg8: 10, string_id: 4966>  # String: '__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end' (String)
    // USED → r10 = "__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end";
    // CODE → addr:495 | <Call2>: <Reg8: 10, Reg8: 11, Reg8: 12, Reg8: 10>
    console.log("__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end");
    // CODE → addr:500 | <Ret>: <Reg8: 3>
}