function nestedLoopTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4627>  # String: '__BC:ControlFlow/NestedTests/nestedLoopTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/NestedTests/nestedLoopTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 7, UInt8: 3>
    // USED → r7 = 3;
    // CODE → <LoadConstUInt8>: <Reg8: 6, UInt8: 4>
    // USED → r6 = 4;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4623>  # String: '__BC:ControlFlow/NestedTests/nestedLoopTest/deep-if' (String)
    // USED → r5 = "__BC:ControlFlow/NestedTests/nestedLoopTest/deep-if";
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 1516>  # String: 'nested' (String)
    // USED → r4 = "nested";
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 2>
    // USED → r3 = 2;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // LOOP → START (do_while)
    do {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 9, Reg8: 1>
        // USED → r9 = 0;
        // CODE → <LoadConstZero>: <Reg8: 10>
        // USED → r10 = 0;
        // LOOP → START (do_while)
        do {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <Mov>: <Reg8: 11, Reg8: 10>
            // USED → r11 = 0;
            if (0 === 1 && 0 === 2) {
                // ──────────────── Block 4 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 13, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r13 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r12 = globalThis.console.log;
                // CODE → <Call2>: <Reg8: 12, Reg8: 12, Reg8: 13, Reg8: 5>
                console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/deep-if")
                // CODE → <TryGetById>: <Reg8: 13, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r13 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r12 = globalThis.console.log;
                // CODE → <Call2>: <Reg8: 12, Reg8: 12, Reg8: 13, Reg8: 4>
                console.log("nested")
            }
            // ──────────────── Block 5 ──────────────── 
            // CODE → <Inc>: <Reg8: 10, Reg8: 11>
            // USED → r10 = r11 + 1;
        } while (r11 + 1 < 4);
        // LOOP → END
        // ──────────────── Block 6 ──────────────── 
        // CODE → <Inc>: <Reg8: 1, Reg8: 9>
        // USED → r1 = r9 + 1;
    } while (r9 + 1 < 3);
    // LOOP → END
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4625>  # String: '__BC:ControlFlow/NestedTests/nestedLoopTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/NestedTests/nestedLoopTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}