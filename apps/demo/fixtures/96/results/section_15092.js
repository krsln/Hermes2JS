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
    console.log("__BC:Iterators/IteratorTests/forOfTest/start")
    // CODE → <NewArrayWithBuffer>: <Reg8: 2, UInt16: 4, UInt16: 4, UInt16: 20817>  # Array: [1, 2, 3, 4]
    r2 = [1, 2, 3, 4]
    // CODE → <IteratorBegin>: <Reg8: 3, Reg8: 2>
    // USED → r3 = GetIterator(r2);
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // LOOP → START (for_of)
    for (const r6 of r2) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 4, Reg8: 3>
        r4 = GetIterator(r2)
        if (r4 !== undefined) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r5 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r4 = globalThis.console.log;
            // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 6>
            console.log(GetIterator(r2).next())
            // CODE → <Jmp>: <Addr8: -27>  # Address: 00000023
            goto label_35;
        }
    }
    // LOOP → END
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4803>  # String: '__BC:Iterators/IteratorTests/forOfTest/end' (String)
    // USED → r1 = "__BC:Iterators/IteratorTests/forOfTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Iterators/IteratorTests/forOfTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}