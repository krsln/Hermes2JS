function tryLoopMultiReturnTest(param0, param1) {
    try {
        // ──────────────── Block 0 ──────────────── 
        // CODE → <LoadParam>: <Reg8: 3, UInt8: 1>
        // USED → r3 = param1;
        // CODE → <LoadConstUndefined>: <Reg8: 4>
        r4 = undefined
        // CODE → <GetGlobalObject>: <Reg8: 0>
        // USED → r0 = globalThis;
        // CODE → <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r5 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4748>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start")
        // CODE → <LoadConstZero>: <Reg8: 2>
        // USED → r2 = 0;
        // CODE → <LoadConstZero>: <Reg8: 4>
        // USED → r4 = 0;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4747>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive";
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → <Mov>: <Reg8: 6, Reg8: 4>
            // USED → r6 = 0;
            // CODE → <Mov>: <Reg8: 5, Reg8: 3>
            // USED → r5 = param1;
            // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
            // USED → r5 = param1.length;
            // → r5 = param1.length; r6 = 0
            if (r6 < r5) {
                // ──────────────── Block 2 ──────────────── 
                // CODE → <Mov>: <Reg8: 6, Reg8: 3>
                // USED → r6 = param1;
                // CODE → <Mov>: <Reg8: 5, Reg8: 4>
                // USED → r5 = 0;
                // CODE → <GetByVal>: <Reg8: 5, Reg8: 6, Reg8: 5>
                // USED → r5 = param1[0];
                // CODE → <JLess>: <Addr8: 58, Reg8: 5, Reg8: 2>  # Address: 00000076
                // → r5 = param1[0]
                if (r5 < 0) goto label_118;
                // ──────────────── Block 3 ──────────────── 
                // CODE → <Mov>: <Reg8: 6, Reg8: 3>
                // USED → r6 = param1;
                // CODE → <Mov>: <Reg8: 5, Reg8: 4>
                // USED → r5 = 0;
                // CODE → <GetByVal>: <Reg8: 5, Reg8: 6, Reg8: 5>
                // USED → r5 = param1[0];
                // → r5 = param1[0]
                if (r5 === 0) {
                    // ──────────────── Block 5 ──────────────── 
                    // CODE → <Mov>: <Reg8: 5, Reg8: 4>
                    r5 = r5++
                    // CODE → <Inc>: <Reg8: 4, Reg8: 5>
                    r4 = r5++
                } else {
                    // ──────────────── Block 4 ──────────────── 
                    // CODE → <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r8 = globalThis.console;
                    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r7 = globalThis.console.log;
                    // CODE → <Mov>: <Reg8: 6, Reg8: 3>
                    // USED → r6 = param1;
                    // CODE → <Mov>: <Reg8: 5, Reg8: 4>
                    // USED → r5 = 0;
                    // CODE → <GetByVal>: <Reg8: 6, Reg8: 6, Reg8: 5>
                    // USED → r6 = param1[0];
                    // CODE → <Call3>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 6>
                    console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive", r6)
                    // CODE → <Inc>: <Reg8: 4, Reg8: 5>
                    // USED → r4 = r5++;
                }
            }
        }
        // LOOP → END
        // ──────────────── Block 6 ──────────────── 
        // CODE → <LoadConstTrue>: <Reg8: 1>
        // USED → r1 = true;
        // CODE → <Ret>: <Reg8: 1>
        return true;
        // ──────────────── Block 7 ──────────────── 
        // CODE → <LoadConstFalse>: <Reg8: 1>
        // USED → r1 = false;
        // CODE → <Ret>: <Reg8: 1>
        return false;
    } catch (caughtException) {
        // ──────────────── Block 8 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r2 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r1 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 0, string_id: 3905>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block";
        // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block")
        // CODE → <LoadConstFalse>: <Reg8: 0>
        // USED → r0 = false;
        // CODE → <Ret>: <Reg8: 0>
        return false;
    }
}