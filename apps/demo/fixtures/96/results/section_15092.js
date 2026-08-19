function forOfTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4804>  # String: '__BC:Iterators/IteratorTests/forOfTest/start' (String)
    // USED → r0 = "__BC:Iterators/IteratorTests/forOfTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Iterators/IteratorTests/forOfTest/start")
    // CODE → addr: 22 | <NewArrayWithBuffer>: <Reg8: 2, UInt16: 4, UInt16: 4, UInt16: 20817>  # Array: [1, 2, 3, 4]
    r2 = [1, 2, 3, 4]
    // CODE → addr: 30 | <IteratorBegin>: <Reg8: 3, Reg8: 2>
    r3 = GetIterator(r2)
    // CODE → addr: 33 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    try {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → addr: 35 | <IteratorNext>: <Reg8: 6, Reg8: 3, Reg8: 2>
            // USED → r6 = r3.next();
            // CODE → addr: 39 | <Mov>: <Reg8: 4, Reg8: 3>
            r4 = r3
            // → r4 = r3
            if (r4 !== undefined) {
                // ──────────────── Block 2 ──────────────── 
                // CODE → addr: 46 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r5 = console;
                // CODE → addr: 52 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r4 = console.log;
                // CODE → addr: 57 | <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 6>
                console.log(r6)
                // CODE → addr: 62 | <Jmp>: <Addr8: -27>  # Address: 00000023
                goto label_35;
            }
        }
        // LOOP → END
    } finally {
        // ──────────────── Block 3 ──────────────── 
        // CODE → addr: 66 | <IteratorClose>: <Reg8: 3, UInt8: 1>
        r3.return()
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 71 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 77 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 82 | <LoadConstString>: <Reg8: 1, string_id: 4803>  # String: '__BC:Iterators/IteratorTests/forOfTest/end' (String)
    // USED → r1 = "__BC:Iterators/IteratorTests/forOfTest/end";
    // CODE → addr: 86 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Iterators/IteratorTests/forOfTest/end")
    // CODE → addr: 91 | <Ret>: <Reg8: 0>
    return undefined;
}