function tryLoopMultiReturnTest(param1) {
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr:  3 | <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → addr:  5 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  7 | <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 13 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 18 | <LoadConstString>: <Reg8: 1, string_id: 4748>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start";
    // CODE → addr: 22 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start")
    try {
        // ──────────────── Block 0 ──────────────── 
        // CODE → addr: 27 | <LoadConstZero>: <Reg8: 2>
        // USED → r2 = 0;
        // CODE → addr: 29 | <LoadConstZero>: <Reg8: 4>
        r4 = 0
        // CODE → addr: 31 | <LoadConstString>: <Reg8: 1, string_id: 4747>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive";
        // LOOP → START (while)
        // → r5 = r5.length
        while (!(r6 >= r5)) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → addr: 38 | <Mov>: <Reg8: 5, Reg8: 3>
            r5 = param1
            // CODE → addr: 41 | <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
            r5 = r5.length
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 50 | <Mov>: <Reg8: 6, Reg8: 3>
            // USED → r6 = param1;
            // CODE → addr: 53 | <Mov>: <Reg8: 5, Reg8: 4>
            r5 = r4
            // CODE → addr: 56 | <GetByVal>: <Reg8: 5, Reg8: 6, Reg8: 5>
            r5 = param1[r5]
            // → r5 = param1[r5]
            if (r5 < 0) {
                // ──────────────── Block 6 ──────────────── 
                // CODE → addr:118 | <LoadConstTrue>: <Reg8: 1>
                // USED → r1 = true;
                // CODE → addr:120 | <Ret>: <Reg8: 1>
                return true;
            }
            // ──────────────── Block 3 ──────────────── 
            // CODE → addr: 64 | <Mov>: <Reg8: 6, Reg8: 3>
            // USED → r6 = param1;
            // CODE → addr: 67 | <Mov>: <Reg8: 5, Reg8: 4>
            r5 = r4
            // CODE → addr: 70 | <GetByVal>: <Reg8: 5, Reg8: 6, Reg8: 5>
            r5 = param1[r5]
            // → r5 = param1[r5]
            if (r5 === 0) {
                // ──────────────── Block 5 ──────────────── 
                // CODE → addr:110 | <Mov>: <Reg8: 5, Reg8: 4>
                r5 = r4
                // CODE → addr:113 | <Inc>: <Reg8: 4, Reg8: 5>
                r4 = r5 + 1
            } else {
                // ──────────────── Block 4 ──────────────── 
                // CODE → addr: 78 | <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r8 = console;
                // CODE → addr: 84 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r7 = console.log;
                // CODE → addr: 89 | <Mov>: <Reg8: 6, Reg8: 3>
                // USED → r6 = param1;
                // CODE → addr: 92 | <Mov>: <Reg8: 5, Reg8: 4>
                r5 = r4
                // CODE → addr: 95 | <GetByVal>: <Reg8: 6, Reg8: 6, Reg8: 5>
                r6 = param1[r5]
                // CODE → addr: 99 | <Call3>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 6>
                console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive", r6)
                // CODE → addr:105 | <Inc>: <Reg8: 4, Reg8: 5>
                r4 = r5 + 1
            }
        }
        // LOOP → END
    } catch (caughtException) {
        // ──────────────── Block 8 ──────────────── 
        // CODE → addr:128 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r2 = console;
        // CODE → addr:134 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r1 = console.log;
        // CODE → addr:139 | <LoadConstString>: <Reg8: 0, string_id: 3905>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block";
        // CODE → addr:143 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block")
        // CODE → addr:148 | <LoadConstFalse>: <Reg8: 0>
        // USED → r0 = false;
        // CODE → addr:150 | <Ret>: <Reg8: 0>
        return false;
    }
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:122 | <LoadConstFalse>: <Reg8: 1>
    // USED → r1 = false;
    // CODE → addr:124 | <Ret>: <Reg8: 1>
    return false;
}