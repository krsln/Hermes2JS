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
    r1 = globalThis.console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start")
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
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 10, Reg8: 2>
        // USED → r10 = 0;
        // CODE → <Mov>: <Reg8: 8, Reg8: 1>
        // USED → r8 = 0;
        // CODE → <LoadConstZero>: <Reg8: 9>
        // USED → r9 = 0;
        // ──────────────── Block 8 ──────────────── 
        // CODE → <Inc>: <Reg8: 1, Reg8: 8>
        // USED → r1 = 0 + 1;
        // CODE → <Mov>: <Reg8: 2, Reg8: 4>
        r2 = 0 + 1
        // CODE → <JLess>: <Addr8: -60, Reg8: 1, Reg8: 6>  # Address: 00000023
        if (0 + 1 < 3) goto label_35;
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <Mov>: <Reg8: 13, Reg8: 10>
            // USED → r13 = 0;
            // CODE → <Mov>: <Reg8: 11, Reg8: 9>
            // USED → r11 = 0;
            // CODE → <LoadConstZero>: <Reg8: 12>
            // USED → r12 = 0;
            // ──────────────── Block 7 ──────────────── 
            // CODE → <Inc>: <Reg8: 9, Reg8: 11>
            // USED → r9 = 0 + 1;
            // CODE → <Mov>: <Reg8: 10, Reg8: 4>
            r10 = 0 + 1
            // CODE → <JLess>: <Addr8: -42, Reg8: 9, Reg8: 6>  # Address: 0000002b
            if (0 + 1 < 3) goto label_43;
            // LOOP → START (while)
            while (0 === 1) {
                // ──────────────── Block 3 ──────────────── 
                // CODE → <Inc>: <Reg8: 4, Reg8: 13>
                // USED → r4 = 0 + 1;
                // CODE → <Mov>: <Reg8: 14, Reg8: 12>
                // USED → r14 = 0;
                if (0 !== 2) {
                    // ──────────────── Block 6 ──────────────── 
                    // CODE → <Inc>: <Reg8: 12, Reg8: 14>
                    // USED → r12 = 0 + 1;
                    // CODE → <Mov>: <Reg8: 13, Reg8: 4>
                    r13 = 0 + 1
                    // CODE → <JLess>: <Addr8: -24, Reg8: 12, Reg8: 6>  # Address: 00000033
                    if (0 + 1 < 3) goto label_51;
                } else {
                    // ──────────────── Block 5 ──────────────── 
                    // CODE → <JStrictEqual>: <Addr8: 34, Reg8: 11, Reg8: 5>  # Address: 00000063
                    if (0 === 2) goto label_99;
                }
            }
            // LOOP → END
        }
        // LOOP → END
    }
    // LOOP → END
    // ──────────────── Block 9 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4620>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits";
    // CODE → <Call3>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1, Reg8: 4>
    r1 = globalThis.console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits", 0 + 1)
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4284>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}