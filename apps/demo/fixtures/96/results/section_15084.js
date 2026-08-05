function tryFinallyLoopBreakTest(param0, param1) {
    try {
        // ──────────────── Block 0 ──────────────── 
        // CODE → <LoadParam>: <Reg8: 6, UInt8: 1>
        // USED → r6 = param1;
        // CODE → <LoadConstUndefined>: <Reg8: 0>
        // USED → r0 = undefined;
        // CODE → <LoadConstUndefined>: <Reg8: 7>
        r7 = undefined
        // CODE → <GetGlobalObject>: <Reg8: 1>
        // USED → r1 = globalThis;
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 4736>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/start' (String)
        // USED → r2 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/start";
        // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        r2 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/start")
        // CODE → <LoadConstZero>: <Reg8: 5>
        r5 = 0
        // CODE → <LoadConstZero>: <Reg8: 7>
        // USED → r7 = 0;
        // CODE → <Mov>: <Reg8: 2, Reg8: 6>
        // USED → r2 = param1;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
        r2 = param1.length
        // CODE → <LoadConstString>: <Reg8: 4, string_id: 4735>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/item' (String)
        // USED → r4 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/item";
        if (r5 < r2) {
            // LOOP → START (while)
            while (true) {
                // ──────────────── Block 1 ──────────────── 
                // CODE → <Mov>: <Reg8: 3, Reg8: 6>
                // USED → r3 = param1;
                // CODE → <Mov>: <Reg8: 2, Reg8: 7>
                // USED → r2 = 0;
                // CODE → <GetByVal>: <Reg8: 2, Reg8: 3, Reg8: 2>
                r2 = param1[0]
                if (r2 !== r5) {
                    // ──────────────── Block 2 ──────────────── 
                    // CODE → <TryGetById>: <Reg8: 10, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r10 = globalThis.console;
                    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r9 = globalThis.console.log;
                    // CODE → <Mov>: <Reg8: 2, Reg8: 6>
                    // USED → r2 = param1;
                    // CODE → <Mov>: <Reg8: 3, Reg8: 7>
                    // USED → r3 = 0;
                    // CODE → <GetByVal>: <Reg8: 8, Reg8: 2, Reg8: 3>
                    // USED → r8 = param1[0];
                    // CODE → <Call3>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 4, Reg8: 8>
                    r8 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/item", param1[0])
                    // CODE → <Inc>: <Reg8: 3, Reg8: 3>
                    // USED → r3 = r3 + 1;
                    // CODE → <Mov>: <Reg8: 7, Reg8: 3>
                    r7 = r3 + 1
                    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
                    r2 = param1.length
                    // CODE → <JLess>: <Addr8: -52, Reg8: 3, Reg8: 2>  # Address: 00000031
                    if (r3 < r2) goto label_49;
                }
            }
            // LOOP → END
        }
        // ──────────────── Block 3 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 4733>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/end' (String)
        // USED → r2 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/end";
        // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        r2 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/end")
        // CODE → <Ret>: <Reg8: 0>
        return undefined;
    } finally {
        // ──────────────── Block 4 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4734>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        r1 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block")
    }
}