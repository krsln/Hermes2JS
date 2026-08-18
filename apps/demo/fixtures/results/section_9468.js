function tryLoopMultiReturnTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4906>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start")
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    // CODE → <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4272>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive";
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 6, Reg8: 4>
        // USED → r6 = 0;
        // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 3, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
        // USED → r5 = r3.length;
        // → r5 = r3.length; r6 = 0
        if (r6 < r5) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <Mov>: <Reg8: 5, Reg8: 4>
            r5 = 0
            // CODE → <GetByVal>: <Reg8: 5, Reg8: 3, Reg8: 5>
            // USED → r5 = param1[r5];
            // CODE → <JLess>: <Addr8: 52, Reg8: 5, Reg8: 2>  # Address: 0000006a
            // → r5 = param1[r5]
            if (r5 < 0) goto label_106;
            // ──────────────── Block 3 ──────────────── 
            // CODE → <Mov>: <Reg8: 5, Reg8: 4>
            r5 = 0
            // CODE → <GetByVal>: <Reg8: 5, Reg8: 3, Reg8: 5>
            // USED → r5 = param1[r5];
            // → r5 = param1[r5]
            if (r5 === 0) {
                // ──────────────── Block 5 ──────────────── 
                // CODE → <Mov>: <Reg8: 5, Reg8: 4>
                r5 = r5 + 1
                // CODE → <Inc>: <Reg8: 4, Reg8: 5>
                r4 = r5 + 1
            } else {
                // ──────────────── Block 4 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r8 = console;
                // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r7 = console.log;
                // CODE → <Mov>: <Reg8: 5, Reg8: 4>
                r5 = 0
                // CODE → <GetByVal>: <Reg8: 6, Reg8: 3, Reg8: 5>
                // USED → r6 = param1[r5];
                // CODE → <Call3>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 6>
                console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive", r6)
                // CODE → <Inc>: <Reg8: 4, Reg8: 5>
                // USED → r4 = r5 + 1;
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
    // CODE → <Catch>: <Reg8: 1>
    r1 = caughtException
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4905>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block")
    // CODE → <LoadConstFalse>: <Reg8: 0>
    // USED → r0 = false;
    // CODE → <Ret>: <Reg8: 0>
    return false;
}