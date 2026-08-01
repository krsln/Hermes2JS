function callGeneratorTests(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4776>  # String: '__BC:Functions/GeneratorTests/callGeneratorTests/start' (String)
    // USED → r0 = "__BC:Functions/GeneratorTests/callGeneratorTests/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Functions/GeneratorTests/callGeneratorTests/start")
    // CODE → <GetEnvironment>: <Reg8: 2, UInt8: 0>
    // USED → r2 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 0>
    // USED → r3 = getEnvironment(0)[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call1>: <Reg8: 5, Reg8: 3, Reg8: 0>
    // USED → r5 = getEnvironment(0)[0].call(undefined);
    // CODE → <Mov>: <Reg8: 3, Reg8: 5>
    r3 = getEnvironment(0)[0].call(undefined)
    // CODE → <IteratorBegin>: <Reg8: 4, Reg8: 3>
    // USED → r4 = GetIterator(r3);
    // LOOP → START (for_of)
    for (const r7 of r3) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 5, Reg8: 4>
        // USED → r5 = GetIterator(r3);
        // CODE → <JStrictEqual>: <Addr8: 29, Reg8: 5, Reg8: 0>  # Address: 0000004d
        if (GetIterator(r3) === undefined) goto label_77;
        // ──────────────── Block 2 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r6 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r5 = globalThis.console.log;
        // CODE → <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
        r5 = globalThis.console.log(GetIterator(r3).next())
        // CODE → <Jmp>: <Addr8: -27>  # Address: 00000029
        goto label_41;
    }
    // LOOP → END
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 1>
    // USED → r4 = getEnvironment(0)[1];
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 5>
    // USED → r3 = 5;
    // CODE → <Call2>: <Reg8: 5, Reg8: 4, Reg8: 0, Reg8: 3>
    // USED → r5 = getEnvironment(0)[1].call(undefined, 5);
    // CODE → <Mov>: <Reg8: 3, Reg8: 5>
    r3 = getEnvironment(0)[1].call(undefined, 5)
    // CODE → <IteratorBegin>: <Reg8: 4, Reg8: 3>
    // USED → r4 = GetIterator(r3);
    // LOOP → START (for_of)
    for (const r7 of r3) {
        // ──────────────── Block 5 ──────────────── 
        // CODE → <Mov>: <Reg8: 5, Reg8: 4>
        // USED → r5 = GetIterator(r3);
        // CODE → <JStrictEqual>: <Addr8: 29, Reg8: 5, Reg8: 0>  # Address: 00000083
        if (GetIterator(r3) === undefined) goto label_131;
        // ──────────────── Block 6 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r6 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r5 = globalThis.console.log;
        // CODE → <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
        r5 = globalThis.console.log(GetIterator(r3).next())
        // CODE → <Jmp>: <Addr8: -27>  # Address: 0000005f
        goto label_95;
    }
    // LOOP → END
    // ──────────────── Block 8 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 2>
    // USED → r2 = getEnvironment(0)[2];
    // CODE → <Call1>: <Reg8: 5, Reg8: 2, Reg8: 0>
    // USED → r5 = getEnvironment(0)[2].call(undefined);
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 182>  # String: 'next' (Identifier)
    // USED → r2 = getEnvironment(0)[2].call(undefined).next;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = getEnvironment(0)[2].call(undefined).next();
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log(getEnvironment(0)[2].call(undefined).next())
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 4, string_id: 214>  # String: 'return' (Identifier)
    // USED → r2 = getEnvironment(0)[2].call(undefined).return;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 0>
    // USED → r2 = getEnvironment(0)[2].call(undefined).return(undefined);
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log(getEnvironment(0)[2].call(undefined).return(undefined))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4775>  # String: '__BC:Functions/GeneratorTests/callGeneratorTests/end' (String)
    // USED → r1 = "__BC:Functions/GeneratorTests/callGeneratorTests/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Functions/GeneratorTests/callGeneratorTests/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}