function forOfTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4804>  # String: '__BC:Iterators/IteratorTests/forOfTest/start' (String)
    // USED → r0 = "__BC:Iterators/IteratorTests/forOfTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Iterators/IteratorTests/forOfTest/start")
    // CODE → <NewArrayWithBuffer>: <Reg8: 2, UInt16: 4, UInt16: 4, UInt16: 20817>  # Array: [1, 2, 3, 4]
    r2 = [1, 2, 3, 4]
    // CODE → <IteratorBegin>: <Reg8: 3, Reg8: 2>
    r3 = GetIterator(r2)
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <IteratorNext>: <Reg8: 6, Reg8: 3, Reg8: 2>
    // USED → r6 = r3.next();
    // CODE → <Mov>: <Reg8: 4, Reg8: 3>
    r4 = r3
    // CODE → <JStrictEqual>: <Addr8: 29, Reg8: 4, Reg8: 0>  # Address: 00000047
    // → r4 = r3
    if (r4 === undefined) goto label_71;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 6>
    console.log(r6)
    // CODE → <Jmp>: <Addr8: -27>  # Address: 00000023
    goto label_35;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → <IteratorClose>: <Reg8: 3, UInt8: 1>
    r3.return()
    // CODE → <Throw>: <Reg8: 2>
    throw caughtException;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4803>  # String: '__BC:Iterators/IteratorTests/forOfTest/end' (String)
    // USED → r1 = "__BC:Iterators/IteratorTests/forOfTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Iterators/IteratorTests/forOfTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}