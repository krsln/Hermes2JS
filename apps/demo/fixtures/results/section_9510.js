function closureLoopTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateFunctionEnvironment>: <Reg8: 2, UInt8: 1>
    // USED → r2 = __environment__;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4927>  # String: '__BC:Functions/ClosureTests/closureLoopTest/start' (String)
    // USED → r0 = "__BC:Functions/ClosureTests/closureLoopTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log("__BC:Functions/ClosureTests/closureLoopTest/start")
    // CODE → <NewArray>: <Reg8: 0, UInt16: 0>
    r0 = []
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 0>
    __environment__[0] = r0
    // CODE → <CreateClosure>: <Reg8: 6, Reg8: 2, function_id: 12480>  # Function: [#12480 _loop of 39 bytes]: 2 params @ offset 0x00243e88
    // USED → r6 = _loop;
    // CODE → <LoadConstZero>: <Reg8: 5>
    // USED → r5 = 0;
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 1>
    // USED → r4 = 1;
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 3>
    // USED → r3 = 3;
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    // LOOP → START (do_while)
    do {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Call2>: <Reg8: 7, Reg8: 6, Reg8: 5, Reg8: 2>
        r7 = _loop.call(0, 0)
        // CODE → <AddN>: <Reg8: 2, Reg8: 2, Reg8: 4>
        // USED → r2 = 0 + 1;
    } while (0 + 1 < 3);
    // LOOP → END
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Mov>: <Reg8: 2, Reg8: 0>
    // USED → r2 = r0;
    // CODE → <IteratorBegin>: <Reg8: 3, Reg8: 2>
    // USED → r3 = GetIterator(r2);
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <Mov>: <Reg8: 4, Reg8: 2>
        r4 = r0
        // CODE → <IteratorNext>: <Reg8: 4, Reg8: 3, Reg8: 4>
        // USED → r4 = GetIterator(r2).next();
        // CODE → <Mov>: <Reg8: 5, Reg8: 3>
        // USED → r5 = GetIterator(r2);
        if (GetIterator(r2) !== undefined) {
            // ──────────────── Block 4 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r6 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r5 = globalThis.console.log;
            // CODE → <Call1>: <Reg8: 4, Reg8: 4, Reg8: 0>
            // USED → r4 = GetIterator(r2).next().call(undefined);
            // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
            console.log(GetIterator(r2).next().call(undefined))
            // CODE → <Jmp>: <Addr8: -34>  # Address: 00000045
            goto label_69;
        }
    }
    // LOOP → END
    // ──────────────── Block 5 ──────────────── 
    // CODE → <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → <IteratorClose>: <Reg8: 3, UInt8: 1>
    GetIterator(r2).return()
    // CODE → <Throw>: <Reg8: 2>
    throw caughtException;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4924>  # String: '__BC:Functions/ClosureTests/closureLoopTest/end' (String)
    // USED → r1 = "__BC:Functions/ClosureTests/closureLoopTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/ClosureTests/closureLoopTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}