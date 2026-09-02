function tryFinallyLoopBreakTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:  2 | <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → addr:  4 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  6 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 12 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 17 | <LoadConstString>: <Reg8: 2, string_id: 4895>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/start' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/start";
    // CODE → addr: 21 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/start")
    // CODE → addr: 26 | <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED → r6 = param1;
    // CODE → addr: 29 | <LoadConstZero>: <Reg8: 5>
    // USED → r5 = 0;
    // CODE → addr: 31 | <LoadConstZero>: <Reg8: 7>
    // USED → r7 = 0;
    // CODE → addr: 33 | <GetByIdShort>: <Reg8: 2, Reg8: 6, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
    r2 = param1.length
    // CODE → addr: 38 | <LoadConstString>: <Reg8: 4, string_id: 4894>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/item' (String)
    // USED → r4 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/item";
    // → r2 = param1.length
    if (0 < r2) {
        // LOOP → START (for)
        // → r2 = param1[r2]
        for (; r3 < r2; r3 = r2 + 1) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → addr: 46 | <Mov>: <Reg8: 2, Reg8: 7>
            r2 = 0
            // CODE → addr: 49 | <GetByVal>: <Reg8: 2, Reg8: 6, Reg8: 2>
            r2 = param1[r2]
            // → r2 = param1[r2]
            if (r2 !== 0) {
                // ──────────────── Block 2 ──────────────── 
                // CODE → addr: 57 | <TryGetById>: <Reg8: 9, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r9 = console;
                // CODE → addr: 63 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r8 = console.log;
                // CODE → addr: 68 | <Mov>: <Reg8: 2, Reg8: 7>
                r2 = 0
                // CODE → addr: 71 | <GetByVal>: <Reg8: 3, Reg8: 6, Reg8: 2>
                r3 = param1[r2]
                // CODE → addr: 75 | <Call3>: <Reg8: 3, Reg8: 8, Reg8: 9, Reg8: 4, Reg8: 3>
                console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/item", r3)
                // CODE → addr: 84 | <Mov>: <Reg8: 7, Reg8: 3>
                r7 = r2 + 1
                // CODE → addr: 87 | <GetByIdShort>: <Reg8: 2, Reg8: 6, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
                r2 = param1.length
            }
        }
        // LOOP → END
    }
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 96 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:102 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:107 | <LoadConstString>: <Reg8: 2, string_id: 4893>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block";
    // CODE → addr:111 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block")
    // CODE → addr:116 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:122 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:127 | <LoadConstString>: <Reg8: 2, string_id: 4892>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/end' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/end";
    // CODE → addr:131 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/end")
    // CODE → addr:136 | <Ret>: <Reg8: 0>
    return undefined;
    // CODE → addr:138 | <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → addr:140 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:146 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:151 | <LoadConstString>: <Reg8: 1, string_id: 4893>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block";
    // CODE → addr:155 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block")
    // CODE → addr:160 | <Throw>: <Reg8: 0>
    throw caughtException;
}