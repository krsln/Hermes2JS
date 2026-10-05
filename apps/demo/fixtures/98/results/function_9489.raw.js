function swapViaDestructureTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 5, string_id: 4986>  # String: '__BC:Objects/DestructuringTests/swapViaDestructureTest/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/swapViaDestructureTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/start")
    // CODE → addr: 22 | <NewArray>: <Reg8: 7, UInt16: 2>
    // USED → r7 = [];
    // CODE → addr: 26 | <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → addr: 29 | <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 0, UInt8: 0>
    // USED → r7 = [2];
    // CODE → addr: 33 | <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → addr: 36 | <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 0, UInt8: 1>
    r7 = [2, 1]
    // CODE → addr: 40 | <Mov>: <Reg8: 6, Reg8: 7>
    r6 = r7
    // CODE → addr: 43 | <IteratorBegin>: <Reg8: 5, Reg8: 6>
    ;[r8, r7] = r6
    // CODE → addr: 56 | <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → addr: 67 | <Mov>: <Reg8: 8, Reg8: 7>
    // CODE → addr: 94 | <Mov>: <Reg8: 7, Reg8: 6>
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:106 | <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:112 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr:117 | <Call3>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 8, Reg8: 7>
    console.log(r8, r7)
    // CODE → addr:123 | <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:129 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr:134 | <LoadConstString>: <Reg8: 4, string_id: 4984>  # String: '__BC:Objects/DestructuringTests/swapViaDestructureTest/end' (String)
    // USED → r4 = "__BC:Objects/DestructuringTests/swapViaDestructureTest/end";
    // CODE → addr:138 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/end")
    // CODE → addr:143 | <Ret>: <Reg8: 2>
    return r2;
}