function forOfTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4804>  # String: '__BC:Iterators/IteratorTests/forOfTest/start' (String)
    // USED → r0 = "__BC:Iterators/IteratorTests/forOfTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Iterators/IteratorTests/forOfTest/start")
    // CODE → <NewArrayWithBuffer>: <Reg8: 2, UInt16: 4, UInt16: 4, UInt16: 20817>  # Array: [1, 2, 3, 4]
    // USED → r2 = [1, 2, 3, 4];
    // CODE → <IteratorBegin>: <Reg8: 3, Reg8: 2>
    // USED → r3 = GetIterator([1, 2, 3, 4]);
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    try {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → <IteratorNext>: <Reg8: 6, Reg8: 3, Reg8: 2>
            // USED → r6 = GetIterator([1, 2, 3, 4]).next();
            // CODE → <Mov>: <Reg8: 4, Reg8: 3>
            // USED → r4 = GetIterator([1, 2, 3, 4]);
            // CODE → <JStrictEqual>: <Addr8: 29, Reg8: 4, Reg8: 0>  # Address: 00000047
            if (GetIterator([1, 2, 3, 4]) === undefined) goto label_71;
            // ──────────────── Block 2 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r5 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r4 = globalThis.console.log;
            // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 6>
            r4 = globalThis.console.log(GetIterator([1, 2, 3, 4]).next())
            // CODE → <Jmp>: <Addr8: -27>  # Address: 00000023
            goto label_35;
        }
        // LOOP → END
    } finally {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <IteratorClose>: <Reg8: 3, UInt8: 1>
        GetIterator([1, 2, 3, 4]).return()
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4803>  # String: '__BC:Iterators/IteratorTests/forOfTest/end' (String)
    // USED → r1 = "__BC:Iterators/IteratorTests/forOfTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Iterators/IteratorTests/forOfTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}