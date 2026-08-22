function labeledBreakTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 8>
    // USED → r8 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 11, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r10 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 9, string_id: 4789>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/start' (String)
    // USED → r9 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 9>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
    // USED → r3 = 1;
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 6, UInt8: 3>
    // USED → r6 = 3;
    loop_1:
    // LOOP → START (for)
    for (r4 = 0; r4 < 3; r4 = r4 + 1) {
        // ──────────────── Block 1 ──────────────── 
        // LOOP → START (for)
        for (r0 = 0; r0 < 3; r0 = r0 + 1) {
            // ──────────────── Block 2 ──────────────── 
            if (r4 !== 1) {
                // ──────────────── Block 4 ──────────────── 
                // CODE → addr: 46 | <TryGetById>: <Reg8: 10, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r10 = console;
                // CODE → addr: 52 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r9 = console.log;
                // CODE → addr: 57 | <Call3>: <Reg8: 9, Reg8: 9, Reg8: 10, Reg8: 2, Reg8: 1>
                console.log(r4, r0)
            } else if (r0 === 1) {
                // ──────────────── Block 7 ──────────────── 
                // CODE → addr: 81 | <TryGetById>: <Reg8: 11, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r11 = console;
                // CODE → addr: 87 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r10 = console.log;
                // CODE → addr: 92 | <LoadConstString>: <Reg8: 9, string_id: 4783>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer' (String)
                // USED → r9 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer";
                // CODE → addr: 96 | <Call2>: <Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 9>
                console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer")
                // ──────────────── Block 9 ──────────────── 
                // CODE → addr:  0 | BreakStatement
                break loop_1;
            }
        }
        // LOOP → END
        // ──────────────── Block 5 ──────────────── 
    }
    // LOOP → END
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:101 | <TryGetById>: <Reg8: 10, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:107 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr:112 | <LoadConstString>: <Reg8: 8, string_id: 4784>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/end' (String)
    // USED → r8 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/end";
    // CODE → addr:116 | <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/end")
    // CODE → addr:121 | <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → addr:123 | <Ret>: <Reg8: 7>
    return undefined;
}