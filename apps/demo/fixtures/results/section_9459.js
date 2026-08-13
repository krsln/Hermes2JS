function tripleNestedLabeledTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 15>
    // USED → r15 = globalThis;
    // CODE → <TryGetById>: <Reg8: 18, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r18 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 17, Reg8: 18, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r17 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 16, string_id: 4804>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start' (String)
    // USED → r16 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start";
    // CODE → <Call2>: <Reg8: 16, Reg8: 17, Reg8: 18, Reg8: 16>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → <LoadConstUInt8>: <Reg8: 12, UInt8: 3>
    // USED → r12 = 3;
    // CODE → <LoadConstUInt8>: <Reg8: 13, UInt8: 2>
    // USED → r13 = 2;
    // CODE → <LoadConstZero>: <Reg8: 10>
    // USED → r10 = 0;
    loop_1:
    // LOOP → START (for)
    for (r9 = 0; r9 < 3; r10 = 0 + 1) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 11, Reg8: 9>
        // USED → r11 = 0;
        // CODE → <Mov>: <Reg8: 5, Reg8: 10>
        // USED → r5 = 0;
        loop_2:
        // LOOP → START (for)
        for (r6 = 0; r6 < 3; r5 = 0 + 1) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <Mov>: <Reg8: 7, Reg8: 6>
            // USED → r7 = 0;
            // CODE → <Mov>: <Reg8: 0, Reg8: 5>
            // USED → r0 = 0;
            // LOOP → START (for)
            for (r1 = 0; r1 < 3; r0 = 0 + 1) {
                // ──────────────── Block 3 ──────────────── 
                // CODE → <AddN>: <Reg8: 3, Reg8: 0, Reg8: 2>
                // USED → r3 = 0 + 1;
                // CODE → <Mov>: <Reg8: 4, Reg8: 1>
                // USED → r4 = 0;
                // → r4 = 0
                if (r4 === 1) {
                    // ──────────────── Block 10 ──────────────── 
                    // CODE → ContinueStatement
                    continue loop_2;
                }
                if (r11 === 2) {
                    if (r7 === 2) {
                        // ──────────────── Block 11 ──────────────── 
                        // CODE → BreakStatement
                        break loop_1;
                    }
                    // ──────────────── Block 6 ──────────────── 
                    // CODE → <AddN>: <Reg8: 1, Reg8: 4, Reg8: 2>
                    // USED → r1 = 0 + 1;
                }
            }
            // LOOP → END
            // ──────────────── Block 7 ──────────────── 
            // CODE → <AddN>: <Reg8: 6, Reg8: 7, Reg8: 2>
            // USED → r6 = 0 + 1;
        }
        // LOOP → END
        // ──────────────── Block 8 ──────────────── 
        // CODE → <AddN>: <Reg8: 9, Reg8: 11, Reg8: 2>
        // USED → r9 = 0 + 1;
    }
    // LOOP → END
    // ──────────────── Block 9 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 18, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r18 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 17, Reg8: 18, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r17 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 16, string_id: 4801>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits' (String)
    // USED → r16 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits";
    // CODE → <Call3>: <Reg8: 16, Reg8: 17, Reg8: 18, Reg8: 16, Reg8: 3>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits", r3)
    // CODE → <TryGetById>: <Reg8: 17, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r17 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 16, Reg8: 17, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r16 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 15, string_id: 4798>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end' (String)
    // USED → r15 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end";
    // CODE → <Call2>: <Reg8: 15, Reg8: 16, Reg8: 17, Reg8: 15>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 14>
    // USED → r14 = undefined;
    // CODE → <Ret>: <Reg8: 14>
    return undefined;
}