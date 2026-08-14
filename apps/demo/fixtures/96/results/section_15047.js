function whileTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4647>  # String: '__BC:ControlFlow/WhileTests/whileTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/WhileTests/whileTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/WhileTests/whileTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 5>
    // USED → r4 = 5;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4131>  # String: '__BC:ControlFlow/WhileTests/whileTest/if-continue' (String)
    // USED → r3 = "__BC:ControlFlow/WhileTests/whileTest/if-continue";
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 2406>  # String: 'while' (String)
    // USED → r2 = "while";
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    // USED → r1 = 2;
    // LOOP → START (for)
    for (r5 = 0; r5 < 5; r5 = r7 + 1) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 7, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r7 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r6 = globalThis.console.log;
        // CODE → <Call3>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 2, Reg8: 5>
        console.log("while", r5)
        // CODE → <Mov>: <Reg8: 7, Reg8: 5>
        // USED → r7 = 0;
        // → r7 = 0
        if (r7 === 2) {
            // ──────────────── Block 3 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r9 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r8 = globalThis.console.log;
            // CODE → <Call2>: <Reg8: 8, Reg8: 8, Reg8: 9, Reg8: 3>
            console.log("__BC:ControlFlow/WhileTests/whileTest/if-continue")
            // CODE → <Inc>: <Reg8: 6, Reg8: 7>
            // USED → r6 = r7 + 1;
        } else {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <Inc>: <Reg8: 6, Reg8: 7>
            r6 = r7 + 1
        }
        // ──────────────── Block 4 ──────────────── 
    }
    // LOOP → END
    // ──────────────── Block 5 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4644>  # String: '__BC:ControlFlow/WhileTests/whileTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/WhileTests/whileTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/WhileTests/whileTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}