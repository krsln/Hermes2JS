function closureLoopTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateFunctionEnvironment>: <Reg8: 2, UInt8: 1>
    // USED → r2 = __environment__;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 0, string_id: 4927>  # String: '__BC:Functions/ClosureTests/closureLoopTest/start' (String)
    // USED → r0 = "__BC:Functions/ClosureTests/closureLoopTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log("__BC:Functions/ClosureTests/closureLoopTest/start")
    // CODE → addr: 25 | <NewArray>: <Reg8: 0, UInt16: 0>
    r0 = []
    // CODE → addr: 29 | <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 0>
    __environment__[0] = r0
    // CODE → addr: 33 | <CreateClosure>: <Reg8: 6, Reg8: 2, function_id: 12480>  # Function: [#12480 _loop of 39 bytes]: 2 params @ offset 0x00243e88
    // USED → r6 = _loop(param1);
    // CODE → addr: 38 | <LoadConstZero>: <Reg8: 5>
    // USED → r5 = 0;
    // CODE → addr: 40 | <LoadConstUInt8>: <Reg8: 4, UInt8: 1>
    // USED → r4 = 1;
    // CODE → addr: 43 | <LoadConstUInt8>: <Reg8: 3, UInt8: 3>
    // USED → r3 = 3;
    // CODE → addr: 46 | <LoadConstZero>: <Reg8: 2>
    r2 = 0
    // LOOP → START (do_while)
    do {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 48 | <Call2>: <Reg8: 7, Reg8: 6, Reg8: 5, Reg8: 2>
        r7 = _loop(param1).call(0, r2)
        // CODE → addr: 53 | <AddN>: <Reg8: 2, Reg8: 2, Reg8: 4>
        r2 = r2 + 1
    // → r2 = r2 + 1
    } while (r2 < 3);
    // LOOP → END
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 61 | <Mov>: <Reg8: 2, Reg8: 0>
    r2 = r0
    // CODE → addr: 64 | <IteratorBegin>: <Reg8: 3, Reg8: 2>
    r3 = GetIterator(r2)
    // CODE → addr: 67 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // LOOP → START (while)
    while (!(r5 === undefined)) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → addr: 72 | <IteratorNext>: <Reg8: 4, Reg8: 3, Reg8: 4>
        r4 = r3.next()
        // ──────────────── Block 4 ──────────────── 
        // CODE → addr: 83 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r6 = console;
        // CODE → addr: 89 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r5 = console.log;
        // CODE → addr: 94 | <Call1>: <Reg8: 4, Reg8: 4, Reg8: 0>
        r4 = r4.call(undefined)
        // CODE → addr: 98 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
        console.log(r4)
    }
    // LOOP → END
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr:105 | <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → addr:107 | <IteratorClose>: <Reg8: 3, UInt8: 1>
    r3.return()
    // CODE → addr:110 | <Throw>: <Reg8: 2>
    throw caughtException;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:112 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:118 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:123 | <LoadConstString>: <Reg8: 1, string_id: 4924>  # String: '__BC:Functions/ClosureTests/closureLoopTest/end' (String)
    // USED → r1 = "__BC:Functions/ClosureTests/closureLoopTest/end";
    // CODE → addr:127 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/ClosureTests/closureLoopTest/end")
    // CODE → addr:132 | <Ret>: <Reg8: 0>
    return undefined;
}