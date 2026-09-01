function whileTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4647>  # String: '__BC:ControlFlow/WhileTests/whileTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/WhileTests/whileTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/WhileTests/whileTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 4, UInt8: 5>
    // USED → r4 = 5;
    // CODE → addr: 25 | <LoadConstString>: <Reg8: 3, string_id: 4131>  # String: '__BC:ControlFlow/WhileTests/whileTest/if-continue' (String)
    // USED → r3 = "__BC:ControlFlow/WhileTests/whileTest/if-continue";
    // CODE → addr: 29 | <LoadConstString>: <Reg8: 2, string_id: 2406>  # String: 'while' (String)
    // USED → r2 = "while";
    // CODE → addr: 33 | <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    // USED → r1 = 2;
    // LOOP → START (for)
    for (r5 = 0; r5 < 5; r5 = r5 + 1) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 38 | <TryGetById>: <Reg8: 7, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r7 = console;
        // CODE → addr: 44 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r6 = console.log;
        // CODE → addr: 49 | <Call3>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 2, Reg8: 5>
        console.log("while", r5)
        if (r5 === 2) {
            // ──────────────── Block 3 ──────────────── 
            // CODE → addr: 67 | <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r9 = console;
            // CODE → addr: 73 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r8 = console.log;
            // CODE → addr: 78 | <Call2>: <Reg8: 8, Reg8: 8, Reg8: 9, Reg8: 3>
            console.log("__BC:ControlFlow/WhileTests/whileTest/if-continue")
            // CODE → addr: 83 | <Inc>: <Reg8: 6, Reg8: 7>
            // USED → r6 = r5 + 1;
        } else {
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 62 | <Inc>: <Reg8: 6, Reg8: 7>
            r6 = r5 + 1
        }
        // ──────────────── Block 4 ──────────────── 
    }
    // LOOP → END
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 93 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 99 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:104 | <LoadConstString>: <Reg8: 0, string_id: 4644>  # String: '__BC:ControlFlow/WhileTests/whileTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/WhileTests/whileTest/end";
    // CODE → addr:108 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/WhileTests/whileTest/end")
    // CODE → addr:113 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:115 | <Ret>: <Reg8: 0>
    return undefined;
}