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
    r7 = []
    // CODE → addr: 26 | <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → addr: 29 | <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 0, UInt8: 0>
    r7[0] = 2
    // CODE → addr: 33 | <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → addr: 36 | <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 0, UInt8: 1>
    r7[1] = 1
    // CODE → addr: 40 | <Mov>: <Reg8: 6, Reg8: 7>
    r6 = r7
    // CODE → addr: 43 | <IteratorBegin>: <Reg8: 5, Reg8: 6>
    r5 = GetIterator(r6)
    // CODE → addr: 49 | <IteratorNext>: <Reg8: 7, Reg8: 5, Reg8: 7>
    r7 = r5.next()
    // CODE → addr: 56 | <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → addr: 58 | <StrictEq>: <Reg8: 1, Reg8: 8, Reg8: 2>
    // USED → r1 = r5 === undefined;
    // CODE → addr: 62 | <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // → r5 = GetIterator(r6)
    if (r5 !== undefined) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 67 | <Mov>: <Reg8: 8, Reg8: 7>
        r8 = r7
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 70 | <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    if (r5 !== undefined) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → addr: 75 | <IteratorNext>: <Reg8: 6, Reg8: 5, Reg8: 6>
        r6 = r5.next()
        // CODE → addr: 79 | <Mov>: <Reg8: 9, Reg8: 5>
        // USED → r9 = r5;
        // CODE → addr: 82 | <StrictEq>: <Reg8: 3, Reg8: 9, Reg8: 2>
        // USED → r3 = r5 === undefined;
        // CODE → addr: 86 | <LoadConstUndefined>: <Reg8: 7>
        r7 = undefined
        // CODE → addr: 88 | <Mov>: <Reg8: 1, Reg8: 3>
        r1 = r5 === undefined || r5 === undefined
    }
    if (r5 !== undefined) {
        // ──────────────── Block 6 ──────────────── 
        // CODE → addr:103 | <IteratorClose>: <Reg8: 5, UInt8: 0>
        r5.return()
    }
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
    return undefined;
}