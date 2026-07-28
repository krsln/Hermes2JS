function forInTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4769>  # String: '__BC:Iterators/IteratorTests/forInTest/start' (String)
    // USED → r4 = "__BC:Iterators/IteratorTests/forInTest/start";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    r4 = globalThis.console.log("__BC:Iterators/IteratorTests/forInTest/start");
    // CODE → <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1912, UInt16: 19164>  # Object: {'a': 1, 'b': 2, 'c': 3}
    // Error: NewObjectWithBuffer at address 22: Invalid arguments: Reg8: 7, UInt16: 1912, UInt16: 19164;
    // CODE → <Mov>: <Reg8: 5, Reg8: 7>
    // USED → r5 = r7;
    // CODE → <GetPNameList>: <Reg8: 6, Reg8: 5, Reg8: 0, Reg8: 1>
    // USED → r6 = HermesPropertyIterator(r7);
    if (HermesPropertyIterator(r7) !== undefined) {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → <GetNextPName>: <Reg8: 4, Reg8: 6, Reg8: 5, Reg8: 0, Reg8: 1>
            // USED → r4 = HermesPropertyIterator(r7).next();
            // CODE → <JmpUndefined>: <Addr8: 29, Reg8: 4>  # Address: 0000004a
            if (HermesPropertyIterator(r7).next() === undefined) goto label_74;
            // ──────────────── Block 2 ──────────────── 
            // CODE → <Mov>: <Reg8: 11, Reg8: 4>
            // USED → r11 = HermesPropertyIterator(r7).next();
            // CODE → <TryGetById>: <Reg8: 10, Reg8: 3, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
            // USED → r10 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
            // USED → r9 = globalThis.console.log;
            // CODE → <GetByVal>: <Reg8: 8, Reg8: 7, Reg8: 11>
            // USED → r8 = r7[HermesPropertyIterator(r7).next()];
            // CODE → <Call3>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 8>
            r8 = globalThis.console.log(HermesPropertyIterator(r7).next(), r7[HermesPropertyIterator(r7).next()]);
            // CODE → <Jmp>: <Addr8: -33>  # Address: 00000027
            goto label_39;
        }
        // LOOP → END
    }
    // ──────────────── Block 3 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4766>  # String: '__BC:Iterators/IteratorTests/forInTest/end' (String)
    // USED → r3 = "__BC:Iterators/IteratorTests/forInTest/end";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:Iterators/IteratorTests/forInTest/end");
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → <Ret>: <Reg8: 2>
    return undefined;
}