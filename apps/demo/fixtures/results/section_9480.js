function forInTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 4, string_id: 4960>  # String: '__BC:Iterators/IteratorTests/forInTest/start' (String)
    // USED → r4 = "__BC:Iterators/IteratorTests/forInTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Iterators/IteratorTests/forInTest/start")
    // CODE → addr: 22 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1912, UInt16: 19164>  # Object: {'a': 1, 'b': 2, 'c': 3}
    r7 = { "a": 1, "b": 2, "c": 3 }
    // CODE → addr: 28 | <Mov>: <Reg8: 5, Reg8: 7>
    r5 = r7
    // CODE → addr: 31 | <GetPNameList>: <Reg8: 6, Reg8: 5, Reg8: 0, Reg8: 1>
    r6 = HermesPropertyIterator(r5)
    // → r6 = HermesPropertyIterator(r5)
    if (r6 !== undefined) {
        // LOOP → START (while)
        // → r4 = r6.next()
        while (!(r4 === undefined)) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → addr: 39 | <GetNextPName>: <Reg8: 4, Reg8: 6, Reg8: 5, Reg8: 0, Reg8: 1>
            r4 = r6.next()
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 48 | <Mov>: <Reg8: 11, Reg8: 4>
            // USED → r11 = r4;
            // CODE → addr: 51 | <TryGetById>: <Reg8: 10, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r10 = console;
            // CODE → addr: 57 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r9 = console.log;
            // CODE → addr: 62 | <GetByVal>: <Reg8: 8, Reg8: 7, Reg8: 11>
            // USED → r8 = r7[r11];
            // CODE → addr: 66 | <Call3>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 8>
            console.log(r11, r8)
            // CODE → addr: 72 | <Jmp>: <Addr8: -33>  # Address: 00000027
            goto label_39;
        }
        // LOOP → END
    }
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 74 | <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 80 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 85 | <LoadConstString>: <Reg8: 3, string_id: 4959>  # String: '__BC:Iterators/IteratorTests/forInTest/end' (String)
    // USED → r3 = "__BC:Iterators/IteratorTests/forInTest/end";
    // CODE → addr: 89 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Iterators/IteratorTests/forInTest/end")
    // CODE → addr: 94 | <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → addr: 96 | <Ret>: <Reg8: 2>
    return undefined;
}