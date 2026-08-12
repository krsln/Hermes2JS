function closureLoopTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    // USED → r0 = createEnvironment();
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4767>  # String: '__BC:Functions/ClosureTests/closureLoopTest/start' (String)
    // USED → r2 = "__BC:Functions/ClosureTests/closureLoopTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/ClosureTests/closureLoopTest/start")
    // CODE → <NewArray>: <Reg8: 4, UInt16: 0>
    r4 = []
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 4>
    createEnvironment()[0] = r4
    // CODE → <CreateClosure>: <Reg8: 5, Reg8: 0, function_id: 15151>  # Function: [#15151 _loop of 35 bytes]: 2 params @ offset 0x0026aa27
    // USED → r5 = _loop;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 3>
    // USED → r2 = 3;
    // CODE → <LoadConstZero>: <Reg8: 3>
    // USED → r3 = 0;
    // LOOP → START (do_while)
    do {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Call2>: <Reg8: 6, Reg8: 5, Reg8: 0, Reg8: 3>
        r6 = _loop.call(undefined, 0)
        // CODE → <Inc>: <Reg8: 3, Reg8: 3>
        // USED → r3 = r3 + 1;
    } while (r3 + 1 < 3);
    // LOOP → END
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Mov>: <Reg8: 2, Reg8: 4>
    r2 = r4
    // CODE → <IteratorBegin>: <Reg8: 3, Reg8: 2>
    // USED → r3 = GetIterator(r2);
    // LOOP → START (for_of)
    for (const r4 of r2) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <Mov>: <Reg8: 5, Reg8: 3>
        // USED → r5 = GetIterator(r2);
        if (GetIterator(r2) !== undefined) {
            // ──────────────── Block 4 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r6 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r5 = globalThis.console.log;
            // CODE → <Call1>: <Reg8: 4, Reg8: 4, Reg8: 0>
            // USED → r4 = GetIterator(r2).next().call(undefined);
            // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
            console.log(GetIterator(r2).next().call(undefined))
            // CODE → <Jmp>: <Addr8: -31>  # Address: 0000003e
            goto label_62;
        }
    }
    // LOOP → END
    // ──────────────── Block 6 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4766>  # String: '__BC:Functions/ClosureTests/closureLoopTest/end' (String)
    // USED → r1 = "__BC:Functions/ClosureTests/closureLoopTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/ClosureTests/closureLoopTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}