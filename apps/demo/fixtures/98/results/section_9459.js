function tripleNestedLabeledTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 15>
    // USED → r15 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 18, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r18 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 17, Reg8: 18, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r17 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 16, string_id: 4804>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start' (String)
    // USED → r16 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 16, Reg8: 17, Reg8: 18, Reg8: 16>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 12, UInt8: 3>
    // USED → r12 = 3;
    // CODE → addr: 28 | <LoadConstUInt8>: <Reg8: 13, UInt8: 2>
    // USED → r13 = 2;
    // CODE → addr: 33 | <LoadConstZero>: <Reg8: 10>
    r10 = 0
    loop_1:
    // LOOP → START (for)
    for (r9 = 0; r9 < 3; r9 = r11 + 1) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 35 | <Mov>: <Reg8: 11, Reg8: 9>
        r11 = r9
        // CODE → addr: 38 | <Mov>: <Reg8: 5, Reg8: 10>
        r5 = r10
        loop_2:
        // LOOP → START (for)
        for (r6 = 0; r6 < 3; r6 = r7 + 1) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 43 | <Mov>: <Reg8: 7, Reg8: 6>
            r7 = r6
            // CODE → addr: 46 | <Mov>: <Reg8: 0, Reg8: 5>
            r0 = r5
            // LOOP → START (for)
            for (r1 = 0; r1 < 3; r1 = r4 + 1) {
                // ──────────────── Block 3 ──────────────── 
                // CODE → addr: 51 | <AddN>: <Reg8: 3, Reg8: 0, Reg8: 2>
                r3 = r0 + 1
                // CODE → addr: 55 | <Mov>: <Reg8: 4, Reg8: 1>
                r4 = r1
                // → r4 = r1
                if (r4 === 1) {
                    // ──────────────── Block 10 ──────────────── 
                    // CODE → addr:  0 | ContinueStatement
                    continue loop_2;
                }
                if (r11 === 2) {
                    if (r7 === 2) {
                        // ──────────────── Block 11 ──────────────── 
                        // CODE → addr:  0 | BreakStatement
                        break loop_1;
                    }
                    // ──────────────── Block 6 ──────────────── 
                    // CODE → addr: 74 | <Mov>: <Reg8: 0, Reg8: 3>
                    r0 = r3
                }
            }
            // LOOP → END
            // ──────────────── Block 7 ──────────────── 
            // CODE → addr: 85 | <Mov>: <Reg8: 5, Reg8: 3>
            r5 = r3
        }
        // LOOP → END
        // ──────────────── Block 8 ──────────────── 
        // CODE → addr: 96 | <Mov>: <Reg8: 10, Reg8: 3>
        r10 = r3
    }
    // LOOP → END
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:103 | <TryGetById>: <Reg8: 18, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r18 = console;
    // CODE → addr:109 | <GetByIdShort>: <Reg8: 17, Reg8: 18, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r17 = console.log;
    // CODE → addr:114 | <LoadConstString>: <Reg8: 16, string_id: 4801>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits' (String)
    // USED → r16 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits";
    // CODE → addr:118 | <Call3>: <Reg8: 16, Reg8: 17, Reg8: 18, Reg8: 16, Reg8: 3>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits", r3)
    // CODE → addr:124 | <TryGetById>: <Reg8: 17, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r17 = console;
    // CODE → addr:130 | <GetByIdShort>: <Reg8: 16, Reg8: 17, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r16 = console.log;
    // CODE → addr:135 | <LoadConstString>: <Reg8: 15, string_id: 4798>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end' (String)
    // USED → r15 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end";
    // CODE → addr:139 | <Call2>: <Reg8: 15, Reg8: 16, Reg8: 17, Reg8: 15>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end")
    // CODE → addr:144 | <LoadConstUndefined>: <Reg8: 14>
    // USED → r14 = undefined;
    // CODE → addr:146 | <Ret>: <Reg8: 14>
    return undefined;
}