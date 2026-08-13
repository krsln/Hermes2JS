function forInTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4802>  # String: '__BC:Iterators/IteratorTests/forInTest/start' (String)
    // USED → r1 = "__BC:Iterators/IteratorTests/forInTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Iterators/IteratorTests/forInTest/start")
    // CODE → <NewObjectWithBuffer>: <Reg8: 6, UInt16: 3, UInt16: 3, UInt16: 1155, UInt16: 1179>  # Object: {'a': 1, 'b': 2, 'c': 3}
    r6 = { "a": 1, "b": 2, "c": 3 }
    // CODE → <Mov>: <Reg8: 4, Reg8: 6>
    r4 = r6
    // CODE → <GetPNameList>: <Reg8: 5, Reg8: 4, Reg8: 3, Reg8: 2>
    // USED → r5 = HermesPropertyIterator(r4);
    // → r4 = r6
    if (HermesPropertyIterator(r4) !== undefined) {
        // LOOP → START (for_in)
        for (const r1 in r4) {
            // ──────────────── Block 1 ──────────────── 
            if (r5.next() !== undefined) {
                // ──────────────── Block 2 ──────────────── 
                // CODE → <Mov>: <Reg8: 10, Reg8: 1>
                // USED → r10 = r5.next();
                // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r9 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r8 = globalThis.console.log;
                // CODE → <GetByVal>: <Reg8: 7, Reg8: 6, Reg8: 10>
                // USED → r7 = r6[r5.next()];
                // CODE → <Call3>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 7>
                console.log(r10, r7)
                // CODE → <Jmp>: <Addr8: -33>  # Address: 0000002b
                goto label_43;
            }
        }
        // LOOP → END
    }
    // ──────────────── Block 3 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4800>  # String: '__BC:Iterators/IteratorTests/forInTest/end' (String)
    // USED → r0 = "__BC:Iterators/IteratorTests/forInTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Iterators/IteratorTests/forInTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}