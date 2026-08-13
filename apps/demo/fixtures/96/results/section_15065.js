function labeledBreakTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4615>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 3>
    // USED → r3 = 3;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // LOOP → START (do_while)
    do {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 5, Reg8: 1>
        // USED → r5 = 0;
        // CODE → <LoadConstZero>: <Reg8: 6>
        // USED → r6 = 0;
        // LOOP → START (do_while)
        do {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <Mov>: <Reg8: 7, Reg8: 6>
            // USED → r7 = 0;
            if (r5 !== 1) {
                // ──────────────── Block 4 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r9 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r8 = globalThis.console.log;
                // CODE → <Call3>: <Reg8: 8, Reg8: 8, Reg8: 9, Reg8: 5, Reg8: 7>
                console.log(0, 0)
                // CODE → <Inc>: <Reg8: 6, Reg8: 7>
                r6 = r7 + 1
            } else {
                // ──────────────── Block 3 ──────────────── 
                // CODE → <JStrictEqual>: <Addr8: 37, Reg8: 7, Reg8: 2>  # Address: 0000004f
                if (r7 === 1) goto label_79;
            }
        // → r6 = r7 + 1
        } while (r6 < 3);
        // LOOP → END
        // ──────────────── Block 5 ──────────────── 
        // CODE → <Inc>: <Reg8: 1, Reg8: 5>
        r1 = r5 + 1
    // → r1 = r5 + 1
    } while (r1 < 3);
    // LOOP → END
    // ──────────────── Block 6 ──────────────── 
    // CODE → <Jmp>: <Addr8: 22>  # Address: 00000063
    goto label_99;
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4608>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer")
    // ──────────────── Block 8 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4610>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}