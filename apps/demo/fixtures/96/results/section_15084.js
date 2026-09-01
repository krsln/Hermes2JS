function tryFinallyLoopBreakTest(param1) {
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED → r6 = param1;
    // CODE → addr:  3 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:  5 | <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → addr:  7 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  9 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 15 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 20 | <LoadConstString>: <Reg8: 2, string_id: 4736>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/start' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/start";
    // CODE → addr: 24 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/start")
    try {
        // ──────────────── Block 0 ──────────────── 
        // CODE → addr: 29 | <LoadConstZero>: <Reg8: 5>
        // USED → r5 = 0;
        // CODE → addr: 31 | <LoadConstZero>: <Reg8: 7>
        // USED → r7 = 0;
        // CODE → addr: 33 | <Mov>: <Reg8: 2, Reg8: 6>
        r2 = param1
        // CODE → addr: 36 | <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
        r2 = r2.length
        // CODE → addr: 41 | <LoadConstString>: <Reg8: 4, string_id: 4735>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/item' (String)
        // USED → r4 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/item";
        // → r2 = r2.length
        if (0 < r2) {
            // LOOP → START (for)
            // → r2 = param1[r2]; r3 = param1
            for (; r3 < r2; r3 = r3 + 1) {
                // ──────────────── Block 1 ──────────────── 
                // CODE → addr: 49 | <Mov>: <Reg8: 3, Reg8: 6>
                // USED → r3 = param1;
                // CODE → addr: 52 | <Mov>: <Reg8: 2, Reg8: 7>
                r2 = 0
                // CODE → addr: 55 | <GetByVal>: <Reg8: 2, Reg8: 3, Reg8: 2>
                r2 = param1[r2]
                // → r2 = param1[r2]
                if (r2 !== 0) {
                    // ──────────────── Block 2 ──────────────── 
                    // CODE → addr: 63 | <TryGetById>: <Reg8: 10, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r10 = console;
                    // CODE → addr: 69 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r9 = console.log;
                    // CODE → addr: 74 | <Mov>: <Reg8: 2, Reg8: 6>
                    // USED → r2 = param1;
                    // CODE → addr: 77 | <Mov>: <Reg8: 3, Reg8: 7>
                    r3 = 0
                    // CODE → addr: 80 | <GetByVal>: <Reg8: 8, Reg8: 2, Reg8: 3>
                    r8 = param1[r3]
                    // CODE → addr: 84 | <Call3>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 4, Reg8: 8>
                    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/item", r8)
                    // CODE → addr: 93 | <Mov>: <Reg8: 7, Reg8: 3>
                    r7 = r3 + 1
                    // CODE → addr: 96 | <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
                    r2 = r2.length
                }
            }
            // LOOP → END
        }
    } finally {
        // ──────────────── Block 4 ──────────────── 
        // CODE → addr:149 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr:155 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr:160 | <LoadConstString>: <Reg8: 1, string_id: 4734>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block";
        // CODE → addr:164 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block")
    }
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr:105 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:111 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:116 | <LoadConstString>: <Reg8: 2, string_id: 4734>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block";
    // CODE → addr:120 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block")
    // CODE → addr:125 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:131 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:136 | <LoadConstString>: <Reg8: 2, string_id: 4733>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/end' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/end";
    // CODE → addr:140 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/end")
    // CODE → addr:145 | <Ret>: <Reg8: 0>
    return r0;
}