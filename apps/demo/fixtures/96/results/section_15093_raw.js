function forInTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4802>  # String: '__BC:Iterators/IteratorTests/forInTest/start' (String)
    // USED → r1 = "__BC:Iterators/IteratorTests/forInTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Iterators/IteratorTests/forInTest/start")
    // CODE → addr: 22 | <NewObjectWithBuffer>: <Reg8: 6, UInt16: 3, UInt16: 3, UInt16: 1155, UInt16: 1179>  # Object: {'a': 1, 'b': 2, 'c': 3}
    r6 = { "a": 1, "b": 2, "c": 3 }
    // CODE → addr: 32 | <Mov>: <Reg8: 4, Reg8: 6>
    r4 = r6
    // CODE → addr: 35 | <GetPNameList>: <Reg8: 5, Reg8: 4, Reg8: 3, Reg8: 2>
    r5 = HermesPropertyIterator(r4)
    // CODE → addr: 40 | <JmpUndefined>: <Addr8: 38, Reg8: 5>  # Address: 0000004e
    // → r5 = HermesPropertyIterator(r4)
    if (r5 === undefined) goto label_78;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 43 | <GetNextPName>: <Reg8: 1, Reg8: 5, Reg8: 4, Reg8: 3, Reg8: 2>
    r1 = r5.next()
    // CODE → addr: 49 | <JmpUndefined>: <Addr8: 29, Reg8: 1>  # Address: 0000004e
    // → r1 = r5.next()
    if (r1 === undefined) goto label_78;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 52 | <Mov>: <Reg8: 10, Reg8: 1>
    // USED → r10 = r1;
    // CODE → addr: 55 | <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → addr: 61 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr: 66 | <GetByVal>: <Reg8: 7, Reg8: 6, Reg8: 10>
    // USED → r7 = r6[r10];
    // CODE → addr: 70 | <Call3>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 7>
    console.log(r10, r7)
    // CODE → addr: 76 | <Jmp>: <Addr8: -33>  # Address: 0000002b
    goto label_43;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 78 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 84 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 89 | <LoadConstString>: <Reg8: 0, string_id: 4800>  # String: '__BC:Iterators/IteratorTests/forInTest/end' (String)
    // USED → r0 = "__BC:Iterators/IteratorTests/forInTest/end";
    // CODE → addr: 93 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Iterators/IteratorTests/forInTest/end")
    // CODE → addr: 98 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:100 | <Ret>: <Reg8: 0>
    return r0;
}