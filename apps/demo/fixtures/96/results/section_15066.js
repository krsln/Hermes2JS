function labeledContinueTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4618>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 3>
    // USED → r5 = 3;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4616>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/continue-outer' (String)
    // USED → r4 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/continue-outer";
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4619>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/unreachable-with-j1' (String)
    // USED → r3 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/unreachable-with-j1";
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // LOOP → START (do_while)
    do {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 7, Reg8: 1>
        // USED → r7 = 0;
        // CODE → <LoadConstZero>: <Reg8: 8>
        // USED → r8 = 0;
        // ──────────────── Block 4 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r9 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r8 = globalThis.console.log;
        // CODE → <Call2>: <Reg8: 8, Reg8: 8, Reg8: 9, Reg8: 3>
        console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/unreachable-with-j1")
        // CODE → <Jmp>: <Addr8: 18>  # Address: 0000006c
        continue;
        // ──────────────── Block 5 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r9 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r8 = globalThis.console.log;
        // CODE → <Call2>: <Reg8: 8, Reg8: 8, Reg8: 9, Reg8: 4>
        console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/continue-outer")
        // ──────────────── Block 6 ──────────────── 
        // CODE → <Inc>: <Reg8: 1, Reg8: 7>
        // USED → r1 = 0 + 1;
        // LOOP → START (do_while)
        do {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <Mov>: <Reg8: 9, Reg8: 8>
            // USED → r9 = 0;
            if (0 !== 1) {
                // ──────────────── Block 3 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 11, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r11 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r10 = globalThis.console.log;
                // CODE → <Call3>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 7, Reg8: 9>
                console.log(0, 0)
                // CODE → <Inc>: <Reg8: 8, Reg8: 9>
                // USED → r8 = 0 + 1;
            }
        } while (0 + 1 < 3);
        // LOOP → END
    } while (0 + 1 < 3);
    // LOOP → END
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 2050>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}