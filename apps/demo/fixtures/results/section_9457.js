function labeledContinueTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 8>
    // USED → r8 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 11, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r10 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 9, string_id: 4795>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/start' (String)
    // USED → r9 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 9>
    console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
    // USED → r3 = 1;
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 6, UInt8: 3>
    // USED → r6 = 3;
    // CODE → addr: 28 | <LoadConstString>: <Reg8: 10, string_id: 4790>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/continue-outer' (String)
    // USED → r10 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/continue-outer";
    // CODE → addr: 32 | <LoadConstString>: <Reg8: 9, string_id: 4796>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/unreachable-with-j1' (String)
    // USED → r9 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/unreachable-with-j1";
    loop_1:
    // LOOP → START (for)
    for (r4 = 0; r4 < 3; r4 = r4 + 1) {
        // ──────────────── Block 1 ──────────────── 
        // LOOP → START (for)
        for (r0 = 0; r0 < 3; r0 = r0 + 1) {
            // ──────────────── Block 2 ──────────────── 
            if (r0 === 1) {
                // ──────────────── Block 8 ──────────────── 
                // CODE → addr:  0 | ContinueStatement
                continue loop_1;
            }
            // ──────────────── Block 3 ──────────────── 
            // CODE → addr: 50 | <TryGetById>: <Reg8: 12, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r12 = console;
            // CODE → addr: 56 | <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r11 = console.log;
            // CODE → addr: 61 | <Call3>: <Reg8: 11, Reg8: 11, Reg8: 12, Reg8: 2, Reg8: 1>
            console.log(r4, r0)
        }
        // LOOP → END
        // ──────────────── Block 4 ──────────────── 
        // CODE → addr: 75 | <TryGetById>: <Reg8: 12, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r12 = console;
        // CODE → addr: 81 | <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r11 = console.log;
        // CODE → addr: 86 | <Call2>: <Reg8: 11, Reg8: 11, Reg8: 12, Reg8: 9>
        console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/unreachable-with-j1")
        // CODE → addr: 91 | <Jmp>: <Addr8: 18>  # Address: 0000006d
        goto label_109;
        // ──────────────── Block 5 ──────────────── 
        // CODE → addr: 93 | <TryGetById>: <Reg8: 12, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r12 = console;
        // CODE → addr: 99 | <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r11 = console.log;
        // CODE → addr:104 | <Call2>: <Reg8: 11, Reg8: 11, Reg8: 12, Reg8: 10>
        console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/continue-outer")
        // ──────────────── Block 6 ──────────────── 
    }
    // LOOP → END
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:117 | <TryGetById>: <Reg8: 10, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:123 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr:128 | <LoadConstString>: <Reg8: 8, string_id: 4791>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/end' (String)
    // USED → r8 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/end";
    // CODE → addr:132 | <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
    console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/end")
    // CODE → addr:137 | <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → addr:139 | <Ret>: <Reg8: 7>
    return undefined;
}