function closureLoopTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  2 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  4 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 10 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 15 | <LoadConstString>: <Reg8: 2, string_id: 4767>  # String: '__BC:Functions/ClosureTests/closureLoopTest/start' (String)
    // USED → r2 = "__BC:Functions/ClosureTests/closureLoopTest/start";
    // CODE → addr: 19 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/ClosureTests/closureLoopTest/start")
    // CODE → addr: 24 | <NewArray>: <Reg8: 4, UInt16: 0>
    r4 = []
    // CODE → addr: 28 | <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 4>
    r0[0] = r4
    // CODE → addr: 32 | <CreateClosure>: <Reg8: 5, Reg8: 0, function_id: 15151>  # Function: [#15151 _loop of 35 bytes]: 2 params @ offset 0x0026aa27
    // USED → r5 = _loop(param1);
    // CODE → addr: 37 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 39 | <LoadConstUInt8>: <Reg8: 2, UInt8: 3>
    // USED → r2 = 3;
    // CODE → addr: 42 | <LoadConstZero>: <Reg8: 3>
    // USED → r3 = 0;
    // LOOP → START (do_while)
    do {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 44 | <Call2>: <Reg8: 6, Reg8: 5, Reg8: 0, Reg8: 3>
        r6 = _loop(param1).call(undefined, r3)
        // CODE → addr: 49 | <Inc>: <Reg8: 3, Reg8: 3>
        r3 = r3 + 1
    // → r3 = r3 + 1
    } while (r3 < 3);
    // LOOP → END
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 56 | <Mov>: <Reg8: 2, Reg8: 4>
    r2 = r4
    // CODE → addr: 59 | <IteratorBegin>: <Reg8: 3, Reg8: 2>
    r3 = GetIterator(r2)
    // LOOP → START (for_of)
    for (const r4 of r2) {
        // ──────────────── Block 3 ──────────────── 
        // ──────────────── Block 4 ──────────────── 
        // CODE → addr: 73 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r6 = console;
        // CODE → addr: 79 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r5 = console.log;
        // CODE → addr: 84 | <Call1>: <Reg8: 4, Reg8: 4, Reg8: 0>
        // USED → r4 = r4.call(undefined);
        // CODE → addr: 88 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
        console.log(r4)
    }
    // LOOP → END
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:102 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:108 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:113 | <LoadConstString>: <Reg8: 1, string_id: 4766>  # String: '__BC:Functions/ClosureTests/closureLoopTest/end' (String)
    // USED → r1 = "__BC:Functions/ClosureTests/closureLoopTest/end";
    // CODE → addr:117 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/ClosureTests/closureLoopTest/end")
    // CODE → addr:122 | <Ret>: <Reg8: 0>
    return undefined;
}