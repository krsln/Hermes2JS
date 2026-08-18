function callGeneratorTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getParentEnvironment(0)
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4939>  # String: '__BC:Functions/GeneratorTests/callGeneratorTests/start' (String)
    // USED → r0 = "__BC:Functions/GeneratorTests/callGeneratorTests/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log("__BC:Functions/GeneratorTests/callGeneratorTests/start")
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 0>
    // USED → r3 = r2[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call1>: <Reg8: 5, Reg8: 3, Reg8: 0>
    r5 = r2[0].call(r0)
    // CODE → <Mov>: <Reg8: 3, Reg8: 5>
    // USED → r3 = r5;
    // CODE → <IteratorBegin>: <Reg8: 4, Reg8: 3>
    r4 = GetIterator(r3)
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Mov>: <Reg8: 5, Reg8: 3>
    r5 = r5
    // CODE → <IteratorNext>: <Reg8: 7, Reg8: 4, Reg8: 5>
    // USED → r7 = r4.next();
    // CODE → <Mov>: <Reg8: 5, Reg8: 4>
    r5 = r4
    // CODE → <JStrictEqual>: <Addr8: 29, Reg8: 5, Reg8: 0>  # Address: 00000050
    // → r5 = r4
    if (r5 === undefined) goto label_80;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
    console.log(r7)
    // CODE → <Jmp>: <Addr8: -30>  # Address: 00000029
    goto label_41;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → <IteratorClose>: <Reg8: 4, UInt8: 1>
    r4.return()
    // CODE → <Throw>: <Reg8: 3>
    throw caughtException;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 1>
    // USED → r4 = r2[1];
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 5>
    // USED → r3 = 5;
    // CODE → <Call2>: <Reg8: 5, Reg8: 4, Reg8: 0, Reg8: 3>
    r5 = r2[1].call(r0, 5)
    // CODE → <Mov>: <Reg8: 3, Reg8: 5>
    // USED → r3 = r5;
    // CODE → <IteratorBegin>: <Reg8: 4, Reg8: 3>
    r4 = GetIterator(r3)
    // ──────────────── Block 5 ──────────────── 
    // CODE → <Mov>: <Reg8: 5, Reg8: 3>
    r5 = r5
    // CODE → <IteratorNext>: <Reg8: 7, Reg8: 4, Reg8: 5>
    // USED → r7 = r4.next();
    // CODE → <Mov>: <Reg8: 5, Reg8: 4>
    r5 = r4
    // CODE → <JStrictEqual>: <Addr8: 29, Reg8: 5, Reg8: 0>  # Address: 00000089
    // → r5 = r4
    if (r5 === undefined) goto label_137;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
    console.log(r7)
    // CODE → <Jmp>: <Addr8: -30>  # Address: 00000062
    goto label_98;
    // ──────────────── Block 7 ──────────────── 
    // CODE → <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → <IteratorClose>: <Reg8: 4, UInt8: 1>
    r4.return()
    // CODE → <Throw>: <Reg8: 3>
    throw caughtException;
    // ──────────────── Block 8 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 2>
    // USED → r2 = r2[2];
    // CODE → <Call1>: <Reg8: 5, Reg8: 2, Reg8: 0>
    r5 = r2[2].call(r0)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 62>  # String: 'next' (Identifier)
    // USED → r2 = r5.next;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = r5.next();
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 136>  # String: 'return' (Identifier)
    // USED → r2 = r5.return;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 0>
    // USED → r2 = r5.return(r0);
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4937>  # String: '__BC:Functions/GeneratorTests/callGeneratorTests/end' (String)
    // USED → r1 = "__BC:Functions/GeneratorTests/callGeneratorTests/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/GeneratorTests/callGeneratorTests/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}