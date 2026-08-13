function labeledBreakTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 8>
    // USED → r8 = globalThis;
    // CODE → <TryGetById>: <Reg8: 11, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r10 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 4789>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/start' (String)
    // USED → r9 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/start";
    // CODE → <Call2>: <Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 9>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
    // USED → r3 = 1;
    // CODE → <LoadConstUInt8>: <Reg8: 6, UInt8: 3>
    // USED → r6 = 3;
    // LOOP → START (for)
    for (r4 = 0; r4 < 3; r4 = 0 + 1) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 2, Reg8: 4>
        // USED → r2 = 0;
        // LOOP → START (for)
        for (r0 = 0; r0 < 3; r0 = 0 + 1) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <Mov>: <Reg8: 1, Reg8: 0>
            // USED → r1 = 0;
            if (r2 !== 1) {
                // ──────────────── Block 4 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 10, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r10 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r9 = globalThis.console.log;
                // CODE → <Call3>: <Reg8: 9, Reg8: 9, Reg8: 10, Reg8: 2, Reg8: 1>
                console.log(r2, r1)
            } else {
                // ──────────────── Block 3 ──────────────── 
                // CODE → <JStrictEqual>: <Addr8: 39, Reg8: 1, Reg8: 3>  # Address: 00000051
                if (r1 === 1) goto label_81;
            }
        }
        // LOOP → END
        // ──────────────── Block 5 ──────────────── 
    }
    // LOOP → END
    // ──────────────── Block 6 ──────────────── 
    // CODE → <Jmp>: <Addr8: 22>  # Address: 00000065
    goto label_101;
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 11, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r10 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 4783>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer' (String)
    // USED → r9 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer";
    // CODE → <Call2>: <Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 9>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer")
    // ──────────────── Block 8 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 10, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 4784>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/end' (String)
    // USED → r8 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/end";
    // CODE → <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → <Ret>: <Reg8: 7>
    return undefined;
}