function loopBreakCrossesTryBoundaryTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <Mov>: <Reg8: 8, Reg8: 2>
    // USED → r8 = param1;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4656>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/start' (String)
    // USED → r3 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/start")
    // CODE → <LoadConstZero>: <Reg8: 7>
    // USED → r7 = 0;
    // CODE → <LoadConstZero>: <Reg8: 9>
    // USED → r9 = 0;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
    // USED → r2 = param1.length;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4653>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally' (String)
    // USED → r3 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally";
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 4650>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/continue' (String)
    // USED → r6 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/continue";
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4655>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/item' (String)
    // USED → r5 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/item";
    try {
        if (0 < r2) {
            // LOOP → START (for)
            // → r2 = param1[r2]; r4 = param1
            for (; r4 < r2; r2 = param1.length) {
                // ──────────────── Block 1 ──────────────── 
                // CODE → <Mov>: <Reg8: 4, Reg8: 8>
                // USED → r4 = param1;
                // CODE → <Mov>: <Reg8: 2, Reg8: 9>
                r2 = 0
                // CODE → <GetByVal>: <Reg8: 2, Reg8: 4, Reg8: 2>
                // USED → r2 = param1[r2];
                // → r2 = param1[r2]
                if (r2 >= 0) {
                    // ──────────────── Block 2 ──────────────── 
                    // CODE → <Mov>: <Reg8: 4, Reg8: 8>
                    // USED → r4 = param1;
                    // CODE → <Mov>: <Reg8: 2, Reg8: 9>
                    r2 = 0
                    // CODE → <GetByVal>: <Reg8: 2, Reg8: 4, Reg8: 2>
                    // USED → r2 = param1[r2];
                    // → r2 = param1[r2]
                    if (r2 === 0) {
                        // ──────────────── Block 4 ──────────────── 
                        // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                        // USED → r4 = globalThis.console;
                        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                        // USED → r2 = globalThis.console.log;
                        // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 4, Reg8: 6>
                        console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/continue")
                    } else {
                        // ──────────────── Block 3 ──────────────── 
                        // CODE → <TryGetById>: <Reg8: 10, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                        // USED → r10 = globalThis.console;
                        // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 10, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                        // USED → r4 = globalThis.console.log;
                        // CODE → <Mov>: <Reg8: 11, Reg8: 8>
                        // USED → r11 = param1;
                        // CODE → <Mov>: <Reg8: 2, Reg8: 9>
                        r2 = 0
                        // CODE → <GetByVal>: <Reg8: 2, Reg8: 11, Reg8: 2>
                        // USED → r2 = param1[r2];
                        // CODE → <Call3>: <Reg8: 2, Reg8: 4, Reg8: 10, Reg8: 5, Reg8: 2>
                        console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/item", r2)
                    }
                    // ──────────────── Block 5 ──────────────── 
                    // CODE → <Mov>: <Reg8: 2, Reg8: 9>
                    r2 = 0
                    // CODE → <Inc>: <Reg8: 4, Reg8: 2>
                    // USED → r4 = r2 + 1;
                    // CODE → <Mov>: <Reg8: 9, Reg8: 4>
                    r9 = r2 + 1
                    // CODE → <Mov>: <Reg8: 2, Reg8: 8>
                    // USED → r2 = param1;
                }
            }
            // LOOP → END
            // ──────────────── Block 6 ──────────────── 
            // CODE → <Jmp>: <Addr8: 38>  # Address: 000000e0
            goto label_224;
            // ──────────────── Block 7 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r5 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r4 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 2, string_id: 4648>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/break' (String)
            // USED → r2 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/break";
            // CODE → <Call2>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 2>
            console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/break")
        }
        // ──────────────── Block 8 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r5 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r4 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 4652>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/end' (String)
        // USED → r2 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/end";
        // CODE → <Call2>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 2>
        console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/end")
        // CODE → <Ret>: <Reg8: 0>
        return undefined;
    } finally {
        // ──────────────── Block 9 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r2 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r1 = globalThis.console.log;
        // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
        console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally")
    }
}