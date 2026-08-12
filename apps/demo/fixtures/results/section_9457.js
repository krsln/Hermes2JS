function labeledContinueTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 8>
    // USED → r8 = globalThis;
    // CODE → <TryGetById>: <Reg8: 11, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r10 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 4795>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/start' (String)
    // USED → r9 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/start";
    // CODE → <Call2>: <Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 9>
    console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
    // USED → r3 = 1;
    // CODE → <LoadConstUInt8>: <Reg8: 6, UInt8: 3>
    // USED → r6 = 3;
    // CODE → <LoadConstString>: <Reg8: 10, string_id: 4790>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/continue-outer' (String)
    // USED → r10 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/continue-outer";
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 4796>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/unreachable-with-j1' (String)
    // USED → r9 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/unreachable-with-j1";
    // CODE → <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0;
    loop_1:
    // LOOP → START (do_while)
    do {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 2, Reg8: 4>
        // USED → r2 = 0;
        // CODE → <LoadConstZero>: <Reg8: 0>
        // USED → r0 = 0;
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <Mov>: <Reg8: 1, Reg8: 0>
            // USED → r1 = 0;
            if (0 === 1) {
                // ──────────────── Block 5 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 12, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r12 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r11 = globalThis.console.log;
                // CODE → <Call2>: <Reg8: 11, Reg8: 11, Reg8: 12, Reg8: 10>
                console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/continue-outer")
                // CODE → ContinueStatement
                continue loop_1;
            }
            // ──────────────── Block 3 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 12, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r12 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r11 = globalThis.console.log;
            // CODE → <Call3>: <Reg8: 11, Reg8: 11, Reg8: 12, Reg8: 2, Reg8: 1>
            console.log(0, 0)
            // CODE → <AddN>: <Reg8: 0, Reg8: 1, Reg8: 3>
            // USED → r0 = 0 + 1;
            if (0 + 1 >= 3) {
                // ──────────────── Block 4 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 12, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r12 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r11 = globalThis.console.log;
                // CODE → <Call2>: <Reg8: 11, Reg8: 11, Reg8: 12, Reg8: 9>
                console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/unreachable-with-j1")
                // CODE → ContinueStatement
                continue loop_1;
            }
        }
        // LOOP → END
        // ──────────────── Block 6 ──────────────── 
        // CODE → <AddN>: <Reg8: 4, Reg8: 2, Reg8: 3>
        // USED → r4 = 0 + 1;
    } while (0 + 1 < 3);
    // LOOP → END
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 10, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 4791>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/end' (String)
    // USED → r8 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/end";
    // CODE → <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
    console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → <Ret>: <Reg8: 7>
    return undefined;
}