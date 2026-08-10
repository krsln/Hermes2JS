function callGeneratorTests(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
    // USED → r2 = getParentEnvironment(0);
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4939>  # String: '__BC:Functions/GeneratorTests/callGeneratorTests/start' (String)
    // USED → r0 = "__BC:Functions/GeneratorTests/callGeneratorTests/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log("__BC:Functions/GeneratorTests/callGeneratorTests/start")
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 0>
    // USED → r3 = getParentEnvironment(0)[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call1>: <Reg8: 5, Reg8: 3, Reg8: 0>
    // USED → r5 = getParentEnvironment(0)[0].call(undefined);
    // CODE → <Mov>: <Reg8: 3, Reg8: 5>
    // USED → r3 = getParentEnvironment(0)[0].call(undefined);
    // CODE → <IteratorBegin>: <Reg8: 4, Reg8: 3>
    // USED → r4 = GetIterator(r3);
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 5, Reg8: 3>
        r5 = getParentEnvironment(0)[0].call(undefined)
        // CODE → <IteratorNext>: <Reg8: 7, Reg8: 4, Reg8: 5>
        // USED → r7 = GetIterator(r3).next();
        // CODE → <Mov>: <Reg8: 5, Reg8: 4>
        // USED → r5 = GetIterator(r3);
        if (GetIterator(r3) !== undefined) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r6 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r5 = globalThis.console.log;
            // CODE → <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
            console.log(GetIterator(r3).next())
            // CODE → <Jmp>: <Addr8: -30>  # Address: 00000029
            goto label_41;
        }
    }
    // LOOP → END
    // ──────────────── Block 3 ──────────────── 
    // CODE → <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → <IteratorClose>: <Reg8: 4, UInt8: 1>
    GetIterator(r3).return()
    // CODE → <Throw>: <Reg8: 3>
    throw caughtException;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 1>
    // USED → r4 = getParentEnvironment(0)[1];
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 5>
    // USED → r3 = 5;
    // CODE → <Call2>: <Reg8: 5, Reg8: 4, Reg8: 0, Reg8: 3>
    // USED → r5 = getParentEnvironment(0)[1].call(undefined, 5);
    // CODE → <Mov>: <Reg8: 3, Reg8: 5>
    // USED → r3 = getParentEnvironment(0)[1].call(undefined, 5);
    // CODE → <IteratorBegin>: <Reg8: 4, Reg8: 3>
    // USED → r4 = GetIterator(r3);
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 5 ──────────────── 
        // CODE → <Mov>: <Reg8: 5, Reg8: 3>
        r5 = getParentEnvironment(0)[1].call(undefined, 5)
        // CODE → <IteratorNext>: <Reg8: 7, Reg8: 4, Reg8: 5>
        // USED → r7 = GetIterator(r3).next();
        // CODE → <Mov>: <Reg8: 5, Reg8: 4>
        // USED → r5 = GetIterator(r3);
        if (GetIterator(r3) !== undefined) {
            // ──────────────── Block 6 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r6 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r5 = globalThis.console.log;
            // CODE → <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
            console.log(GetIterator(r3).next())
            // CODE → <Jmp>: <Addr8: -30>  # Address: 00000062
            goto label_98;
        }
    }
    // LOOP → END
    // ──────────────── Block 7 ──────────────── 
    // CODE → <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → <IteratorClose>: <Reg8: 4, UInt8: 1>
    GetIterator(r3).return()
    // CODE → <Throw>: <Reg8: 3>
    throw caughtException;
    // ──────────────── Block 8 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 2>
    // USED → r2 = getParentEnvironment(0)[2];
    // CODE → <Call1>: <Reg8: 5, Reg8: 2, Reg8: 0>
    // USED → r5 = getParentEnvironment(0)[2].call(undefined);
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 62>  # String: 'next' (Identifier)
    // USED → r2 = getParentEnvironment(0)[2].call(undefined).next;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = getParentEnvironment(0)[2].call(undefined).next();
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(getParentEnvironment(0)[2].call(undefined).next())
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 136>  # String: 'return' (Identifier)
    // USED → r2 = getParentEnvironment(0)[2].call(undefined).return;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 0>
    // USED → r2 = getParentEnvironment(0)[2].call(undefined).return(undefined);
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(getParentEnvironment(0)[2].call(undefined).return(undefined))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4937>  # String: '__BC:Functions/GeneratorTests/callGeneratorTests/end' (String)
    // USED → r1 = "__BC:Functions/GeneratorTests/callGeneratorTests/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/GeneratorTests/callGeneratorTests/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}