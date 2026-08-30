function callGeneratorTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getParentEnvironment(0)
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 0, string_id: 4939>  # String: '__BC:Functions/GeneratorTests/callGeneratorTests/start' (String)
    // USED → r0 = "__BC:Functions/GeneratorTests/callGeneratorTests/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log("__BC:Functions/GeneratorTests/callGeneratorTests/start")
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
    // LOOP → START (while)
    // → r5 = r4
    while (!(r5 === undefined)) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 41 | <Mov>: <Reg8: 5, Reg8: 3>
        r5 = r5
        // CODE → addr: 44 | <IteratorNext>: <Reg8: 7, Reg8: 4, Reg8: 5>
        // USED → r7 = r4.next();
        // CODE → addr: 48 | <Mov>: <Reg8: 5, Reg8: 4>
        r5 = r4
        // ──────────────── Block 2 ──────────────── 
        // CODE → addr: 55 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r6 = console;
        // CODE → addr: 61 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r5 = console.log;
        // CODE → addr: 66 | <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
        console.log(r7)
    }
    // LOOP → END
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 73 | <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → addr: 75 | <IteratorClose>: <Reg8: 4, UInt8: 1>
    r4.return()
    // CODE → addr: 78 | <Throw>: <Reg8: 3>
    throw caughtException;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 80 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 1>
    // USED → r4 = r2[1];
    // CODE → addr: 84 | <LoadConstUInt8>: <Reg8: 3, UInt8: 5>
    // USED → r3 = 5;
    // CODE → addr: 87 | <Call2>: <Reg8: 5, Reg8: 4, Reg8: 0, Reg8: 3>
    r5 = r2[1].call(r0, 5)
    // CODE → addr: 92 | <Mov>: <Reg8: 3, Reg8: 5>
    r3 = r5
    // CODE → addr: 95 | <IteratorBegin>: <Reg8: 4, Reg8: 3>
    r4 = GetIterator(r3)
    // LOOP → START (while)
    // → r5 = r4
    while (!(r5 === undefined)) {
        // ──────────────── Block 5 ──────────────── 
        // CODE → addr: 98 | <Mov>: <Reg8: 5, Reg8: 3>
        r5 = r5
        // CODE → addr:101 | <IteratorNext>: <Reg8: 7, Reg8: 4, Reg8: 5>
        // USED → r7 = r4.next();
        // CODE → addr:105 | <Mov>: <Reg8: 5, Reg8: 4>
        r5 = r4
        // ──────────────── Block 6 ──────────────── 
        // CODE → addr:112 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r6 = console;
        // CODE → addr:118 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r5 = console.log;
        // CODE → addr:123 | <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
        console.log(r7)
    }
    // LOOP → END
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:130 | <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → addr:132 | <IteratorClose>: <Reg8: 4, UInt8: 1>
    r4.return()
    // CODE → addr:135 | <Throw>: <Reg8: 3>
    throw caughtException;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:137 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 2>
    // USED → r2 = r2[2];
    // CODE → addr:141 | <Call1>: <Reg8: 5, Reg8: 2, Reg8: 0>
    r5 = r2[2].call(r0)
    // CODE → addr:145 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:151 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:156 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 62>  # String: 'next' (Identifier)
    // USED → r2 = r5.next;
    // CODE → addr:161 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = r5.next();
    // CODE → addr:165 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:170 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:176 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:181 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 136>  # String: 'return' (Identifier)
    // USED → r2 = r5.return;
    // CODE → addr:186 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 0>
    // USED → r2 = r5.return(r0);
    // CODE → addr:191 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:196 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:202 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:207 | <LoadConstString>: <Reg8: 1, string_id: 4937>  # String: '__BC:Functions/GeneratorTests/callGeneratorTests/end' (String)
    // USED → r1 = "__BC:Functions/GeneratorTests/callGeneratorTests/end";
    // CODE → addr:211 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/GeneratorTests/callGeneratorTests/end")
    // CODE → addr:216 | <Ret>: <Reg8: 0>
    return undefined;
}