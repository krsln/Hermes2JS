function callGeneratorTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4776>  # String: '__BC:Functions/GeneratorTests/callGeneratorTests/start' (String)
    // USED → r0 = "__BC:Functions/GeneratorTests/callGeneratorTests/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Functions/GeneratorTests/callGeneratorTests/start")
    // CODE → addr: 22 | <GetEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getEnvironment(0)
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 0>
    // USED → r3 = r2[0];
    // CODE → addr: 29 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 31 | <Call1>: <Reg8: 5, Reg8: 3, Reg8: 0>
    r5 = r2[0].call(r0)
    // CODE → addr: 35 | <Mov>: <Reg8: 3, Reg8: 5>
    r3 = r5
    // CODE → addr: 38 | <IteratorBegin>: <Reg8: 4, Reg8: 3>
    r4 = GetIterator(r3)
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 41 | <IteratorNext>: <Reg8: 7, Reg8: 4, Reg8: 3>
    r7 = r4.next()
    // CODE → addr: 45 | <Mov>: <Reg8: 5, Reg8: 4>
    r5 = r4
    // CODE → addr: 48 | <JStrictEqual>: <Addr8: 29, Reg8: 5, Reg8: 0>  # Address: 0000004d
    // → r5 = r4
    if (r5 === undefined) goto label_77;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 52 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 58 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 63 | <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
    console.log(r7)
    // CODE → addr: 68 | <Jmp>: <Addr8: -27>  # Address: 00000029
    goto label_41;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 70 | <Catch>: <Reg8: 3>
    r3 = caughtException
    // CODE → addr: 72 | <IteratorClose>: <Reg8: 4, UInt8: 1>
    r4.return()
    // CODE → addr: 75 | <Throw>: <Reg8: 3>
    throw r3;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 77 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 1>
    // USED → r4 = r2[1];
    // CODE → addr: 81 | <LoadConstUInt8>: <Reg8: 3, UInt8: 5>
    // USED → r3 = 5;
    // CODE → addr: 84 | <Call2>: <Reg8: 5, Reg8: 4, Reg8: 0, Reg8: 3>
    r5 = r2[1].call(r0, 5)
    // CODE → addr: 89 | <Mov>: <Reg8: 3, Reg8: 5>
    r3 = r5
    // CODE → addr: 92 | <IteratorBegin>: <Reg8: 4, Reg8: 3>
    r4 = GetIterator(r3)
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 95 | <IteratorNext>: <Reg8: 7, Reg8: 4, Reg8: 3>
    r7 = r4.next()
    // CODE → addr: 99 | <Mov>: <Reg8: 5, Reg8: 4>
    r5 = r4
    // CODE → addr:102 | <JStrictEqual>: <Addr8: 29, Reg8: 5, Reg8: 0>  # Address: 00000083
    // → r5 = r4
    if (r5 === undefined) goto label_131;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:106 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:112 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr:117 | <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
    console.log(r7)
    // CODE → addr:122 | <Jmp>: <Addr8: -27>  # Address: 0000005f
    goto label_95;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:124 | <Catch>: <Reg8: 3>
    r3 = caughtException
    // CODE → addr:126 | <IteratorClose>: <Reg8: 4, UInt8: 1>
    r4.return()
    // CODE → addr:129 | <Throw>: <Reg8: 3>
    throw r3;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:131 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 2>
    // USED → r2 = r2[2];
    // CODE → addr:135 | <Call1>: <Reg8: 5, Reg8: 2, Reg8: 0>
    r5 = r2[2].call(r0)
    // CODE → addr:139 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:145 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:150 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 182>  # String: 'next' (Identifier)
    // USED → r2 = r5.next;
    // CODE → addr:155 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = r5.next()
    // CODE → addr:159 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:164 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:170 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:175 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 4, string_id: 214>  # String: 'return' (Identifier)
    // USED → r2 = r5.return;
    // CODE → addr:180 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 0>
    r2 = r5.return(r0)
    // CODE → addr:185 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:190 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:196 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:201 | <LoadConstString>: <Reg8: 1, string_id: 4775>  # String: '__BC:Functions/GeneratorTests/callGeneratorTests/end' (String)
    // USED → r1 = "__BC:Functions/GeneratorTests/callGeneratorTests/end";
    // CODE → addr:205 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/GeneratorTests/callGeneratorTests/end")
    // CODE → addr:210 | <Ret>: <Reg8: 0>
    return r0;
}