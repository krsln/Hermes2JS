function forOfTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4963>  # String: '__BC:Iterators/IteratorTests/forOfTest/start' (String)
    // USED → r0 = "__BC:Iterators/IteratorTests/forOfTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Iterators/IteratorTests/forOfTest/start")
    // CODE → addr: 22 | <NewArrayWithBuffer>: <Reg8: 2, UInt16: 4, UInt16: 4, UInt16: 37098>  # Array: [1, 2, 3, 4]
    r2 = [1, 2, 3, 4]
    // CODE → addr: 30 | <IteratorBegin>: <Reg8: 3, Reg8: 2>
    r3 = GetIterator(r2)
    // CODE → addr: 33 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 35 | <Mov>: <Reg8: 4, Reg8: 2>
        r4 = r2
        // CODE → addr: 38 | <IteratorNext>: <Reg8: 6, Reg8: 3, Reg8: 4>
        // USED → r6 = r3.next();
        // CODE → addr: 42 | <Mov>: <Reg8: 4, Reg8: 3>
        r4 = r3
        // → r4 = r3
        if (r4 !== undefined) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 49 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r5 = console;
            // CODE → addr: 55 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r4 = console.log;
            // CODE → addr: 60 | <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 6>
            console.log(r6)
            // CODE → addr: 65 | <Jmp>: <Addr8: -30>  # Address: 00000023
            goto label_35;
        }
    }
    // LOOP → END
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 67 | <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → addr: 69 | <IteratorClose>: <Reg8: 3, UInt8: 1>
    r3.return()
    // CODE → addr: 72 | <Throw>: <Reg8: 2>
    throw caughtException;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 74 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 80 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 85 | <LoadConstString>: <Reg8: 1, string_id: 4961>  # String: '__BC:Iterators/IteratorTests/forOfTest/end' (String)
    // USED → r1 = "__BC:Iterators/IteratorTests/forOfTest/end";
    // CODE → addr: 89 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Iterators/IteratorTests/forOfTest/end")
    // CODE → addr: 94 | <Ret>: <Reg8: 0>
    return undefined;
}