function labeledBreakTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4615>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 3, UInt8: 3>
    // USED → r3 = 3;
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    loop_1:
    // LOOP → START (for)
    for (r1 = 0; r1 < 3; r1 = r5 + 1) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 30 | <Mov>: <Reg8: 5, Reg8: 1>
        r5 = r1
        // LOOP → START (for)
        for (r6 = 0; r6 < 3; r6 = r7 + 1) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 35 | <Mov>: <Reg8: 7, Reg8: 6>
            r7 = r6
            if (r5 !== 1) {
                // ──────────────── Block 4 ──────────────── 
                // CODE → addr: 46 | <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r9 = console;
                // CODE → addr: 52 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r8 = console.log;
                // CODE → addr: 57 | <Call3>: <Reg8: 8, Reg8: 8, Reg8: 9, Reg8: 5, Reg8: 7>
                console.log(r5, r7)
            } else if (r7 === 1) {
                // ──────────────── Block 7 ──────────────── 
                // CODE → addr: 79 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r3 = console;
                // CODE → addr: 85 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r2 = console.log;
                // CODE → addr: 90 | <LoadConstString>: <Reg8: 1, string_id: 4608>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer' (String)
                // USED → r1 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer";
                // CODE → addr: 94 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
                console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer")
                // ──────────────── Block 9 ──────────────── 
                // CODE → addr:  0 | BreakStatement
                break loop_1;
            }
        }
        // LOOP → END
    }
    // LOOP → END
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr: 99 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:105 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:110 | <LoadConstString>: <Reg8: 0, string_id: 4610>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/end";
    // CODE → addr:114 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/end")
    // CODE → addr:119 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:121 | <Ret>: <Reg8: 0>
    return undefined;
}