function tripleNestedLabeledTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4622>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 6, UInt8: 3>
    // USED → r6 = 3;
    // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 2>
    // USED → r5 = 2;
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
    // USED → r3 = 1;
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    // CODE → <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    loop_1:
    // LOOP → START (do_while)
    do {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 10, Reg8: 2>
        // USED → r10 = 0;
        // CODE → <Mov>: <Reg8: 8, Reg8: 1>
        // USED → r8 = 0;
        // CODE → <LoadConstZero>: <Reg8: 9>
        // USED → r9 = 0;
        loop_2:
        // LOOP → START (do_while)
        do {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <Mov>: <Reg8: 13, Reg8: 10>
            r13 = 0
            // CODE → <Mov>: <Reg8: 11, Reg8: 9>
            // USED → r11 = 0;
            // CODE → <LoadConstZero>: <Reg8: 12>
            // USED → r12 = 0;
            // LOOP → START (do_while)
            do {
                // ──────────────── Block 3 ──────────────── 
                // CODE → <Inc>: <Reg8: 4, Reg8: 13>
                // USED → r4 = r13 + 1;
                // CODE → <Mov>: <Reg8: 14, Reg8: 12>
                // USED → r14 = 0;
                if (0 === 1) {
                    // ──────────────── Block 10 ──────────────── 
                    // CODE → ContinueStatement
                    continue loop_2;
                }
                if (0 === 2) {
                    if (0 === 2) {
                        // ──────────────── Block 11 ──────────────── 
                        // CODE → BreakStatement
                        break loop_1;
                    }
                    // ──────────────── Block 6 ──────────────── 
                    // CODE → <Inc>: <Reg8: 12, Reg8: 14>
                    // USED → r12 = r14 + 1;
                    // CODE → <Mov>: <Reg8: 13, Reg8: 4>
                    r13 = r13 + 1
                }
            } while (r14 + 1 < 3);
            // LOOP → END
            // ──────────────── Block 7 ──────────────── 
            // CODE → <Inc>: <Reg8: 9, Reg8: 11>
            // USED → r9 = r11 + 1;
            // CODE → <Mov>: <Reg8: 10, Reg8: 4>
            r10 = r13 + 1
        } while (r11 + 1 < 3);
        // LOOP → END
        // ──────────────── Block 8 ──────────────── 
        // CODE → <Inc>: <Reg8: 1, Reg8: 8>
        // USED → r1 = r8 + 1;
        // CODE → <Mov>: <Reg8: 2, Reg8: 4>
        r2 = r13 + 1
    } while (r8 + 1 < 3);
    // LOOP → END
    // ──────────────── Block 9 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4620>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits";
    // CODE → <Call3>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1, Reg8: 4>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits", r13 + 1)
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4284>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}