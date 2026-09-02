function labeledContinueTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4618>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 5, UInt8: 3>
    // USED → r5 = 3;
    // CODE → addr: 25 | <LoadConstString>: <Reg8: 4, string_id: 4616>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/continue-outer' (String)
    // USED → r4 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/continue-outer";
    // CODE → addr: 29 | <LoadConstString>: <Reg8: 3, string_id: 4619>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/unreachable-with-j1' (String)
    // USED → r3 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/unreachable-with-j1";
    // CODE → addr: 33 | <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    loop_1:
    // LOOP → START (for)
    for (r1 = 0; r1 < 3; r1 = r1 + 1) {
        // LOOP → START (for)
        for (r8 = 0; r8 < 3; r8 = r9 + 1) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 43 | <Mov>: <Reg8: 9, Reg8: 8>
            r9 = 0
            // → r9 = 0
            if (r9 === 1) {
                // ──────────────── Block 5 ──────────────── 
                // CODE → addr: 92 | <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r9 = console;
                // CODE → addr: 98 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r8 = console.log;
                // CODE → addr:103 | <Call2>: <Reg8: 8, Reg8: 8, Reg8: 9, Reg8: 4>
                console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/continue-outer")
                // ──────────────── Block 8 ──────────────── 
                // CODE → addr:  0 | ContinueStatement
                continue loop_1;
            }
            // ──────────────── Block 3 ──────────────── 
            // CODE → addr: 50 | <TryGetById>: <Reg8: 11, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r11 = console;
            // CODE → addr: 56 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r10 = console.log;
            // CODE → addr: 61 | <Call3>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 7, Reg8: 9>
            console.log(r1, r9)
        }
        // LOOP → END
        // ──────────────── Block 4 ──────────────── 
        // CODE → addr: 74 | <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r9 = console;
        // CODE → addr: 80 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r8 = console.log;
        // CODE → addr: 85 | <Call2>: <Reg8: 8, Reg8: 8, Reg8: 9, Reg8: 3>
        console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/unreachable-with-j1")
        // CODE → addr: 90 | <Jmp>: <Addr8: 18>  # Address: 0000006c
        goto label_108;
    }
    // LOOP → END
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:115 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:121 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:126 | <LoadConstString>: <Reg8: 0, string_id: 2050>  # String: '__BC:ControlFlow/LabeledTests/labeledContinueTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/LabeledTests/labeledContinueTest/end";
    // CODE → addr:130 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/end")
    // CODE → addr:135 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:137 | <Ret>: <Reg8: 0>
    return undefined;
}