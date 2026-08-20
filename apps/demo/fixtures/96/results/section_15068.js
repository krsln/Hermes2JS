function tripleNestedLabeledTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4622>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 6, UInt8: 3>
    // USED → r6 = 3;
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 5, UInt8: 2>
    // USED → r5 = 2;
    // CODE → addr: 28 | <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
    // USED → r3 = 1;
    // CODE → addr: 31 | <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    loop_1:
    // LOOP → START (for)
    for (r1 = 0; r1 < 3; r1 = r1 + 1) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 35 | <Mov>: <Reg8: 10, Reg8: 2>
        // USED → r10 = 0;
        loop_2:
        // LOOP → START (for)
        for (r9 = 0; r9 < 3; r9 = r9 + 1) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 43 | <Mov>: <Reg8: 13, Reg8: 10>
            r13 = 0
            // LOOP → START (for)
            for (r12 = 0; r12 < 3; r12 = r12 + 1) {
                // ──────────────── Block 3 ──────────────── 
                // CODE → addr: 51 | <Inc>: <Reg8: 4, Reg8: 13>
                // USED → r4 = r13 + 1;
                if (r12 === 1) {
                    // ──────────────── Block 10 ──────────────── 
                    // CODE → addr:  0 | ContinueStatement
                    continue loop_2;
                }
                if (r1 === 2) {
                    if (r9 === 2) {
                        // ──────────────── Block 11 ──────────────── 
                        // CODE → addr:  0 | BreakStatement
                        break loop_1;
                    }
                    // ──────────────── Block 6 ──────────────── 
                    // CODE → addr: 72 | <Mov>: <Reg8: 13, Reg8: 4>
                    r13 = r13 + 1
                }
            }
            // LOOP → END
            // ──────────────── Block 7 ──────────────── 
            // CODE → addr: 82 | <Mov>: <Reg8: 10, Reg8: 4>
            r10 = r13 + 1
        }
        // LOOP → END
        // ──────────────── Block 8 ──────────────── 
        // CODE → addr: 92 | <Mov>: <Reg8: 2, Reg8: 4>
        r2 = r13 + 1
    }
    // LOOP → END
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr: 99 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:105 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:110 | <LoadConstString>: <Reg8: 1, string_id: 4620>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits";
    // CODE → addr:114 | <Call3>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1, Reg8: 4>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits", r4)
    // CODE → addr:120 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:126 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:131 | <LoadConstString>: <Reg8: 0, string_id: 4284>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end";
    // CODE → addr:135 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end")
    // CODE → addr:140 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:142 | <Ret>: <Reg8: 0>
    return undefined;
}