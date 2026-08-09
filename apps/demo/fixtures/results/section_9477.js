function loopBreakCrossesTryBoundaryTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 8, UInt8: 1>
    // USED → r8 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4831>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/start")
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 8, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
    // USED → r0 = param1.length;
    // CODE → <LoadConstZero>: <Reg8: 7>
    // USED → r7 = 0;
    // CODE → <Less>: <Reg8: 0, Reg8: 7, Reg8: 0>
    // USED → r0 = 0 < param1.length;
    // CODE → <LoadConstUInt8>: <Reg8: 6, UInt8: 1>
    // USED → r6 = 1;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4828>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally' (String)
    // USED → r3 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally";
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4824>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/continue' (String)
    // USED → r5 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/continue";
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4830>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/item' (String)
    // USED → r4 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/item";
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    if (0 < param1.length) {
        // LOOP → START (do_while)
        do {
            // ──────────────── Block 1 ──────────────── 
            // CODE → <Mov>: <Reg8: 0, Reg8: 2>
            // USED → r0 = 0;
            // CODE → <GetByVal>: <Reg8: 9, Reg8: 8, Reg8: 0>
            // USED → r9 = param1[0];
            if (param1[0] >= 0) {
                // ──────────────── Block 2 ──────────────── 
                // CODE → <GetByVal>: <Reg8: 9, Reg8: 8, Reg8: 0>
                // USED → r9 = param1[0];
                if (param1[0] === 0) {
                    // ──────────────── Block 4 ──────────────── 
                    // CODE → <TryGetById>: <Reg8: 10, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r10 = globalThis.console;
                    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r9 = globalThis.console.log;
                    // CODE → <Call2>: <Reg8: 9, Reg8: 9, Reg8: 10, Reg8: 5>
                    r9 = globalThis.console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/continue")
                    // CODE → <TryGetById>: <Reg8: 10, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r10 = globalThis.console;
                    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r9 = globalThis.console.log;
                    // CODE → <Call2>: <Reg8: 9, Reg8: 9, Reg8: 10, Reg8: 3>
                    r9 = globalThis.console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally")
                } else {
                    // ──────────────── Block 3 ──────────────── 
                    // CODE → <TryGetById>: <Reg8: 11, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r11 = globalThis.console;
                    // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r10 = globalThis.console.log;
                    // CODE → <GetByVal>: <Reg8: 9, Reg8: 8, Reg8: 0>
                    // USED → r9 = param1[0];
                    // CODE → <Call3>: <Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 4, Reg8: 9>
                    r9 = globalThis.console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/item", param1[0])
                    // CODE → <TryGetById>: <Reg8: 10, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r10 = globalThis.console;
                    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r9 = globalThis.console.log;
                    // CODE → <Call2>: <Reg8: 9, Reg8: 9, Reg8: 10, Reg8: 3>
                    r9 = globalThis.console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally")
                }
                // ──────────────── Block 5 ──────────────── 
                // CODE → <AddN>: <Reg8: 2, Reg8: 0, Reg8: 6>
                // USED → r2 = 0 + 1;
                // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 8, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
                // USED → r0 = param1.length;
            }
        } while (0 + 1 < param1.length);
        // LOOP → END
        // ──────────────── Block 6 ──────────────── 
        // CODE → <Jmp>: <Addr8: 38>  # Address: 000000c8
        goto label_200;
        // ──────────────── Block 7 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 0, string_id: 4823>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/break' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/break";
        // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
        r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/break")
        // CODE → <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r2 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r0 = globalThis.console.log;
        // CODE → <Call2>: <Reg8: 0, Reg8: 0, Reg8: 2, Reg8: 3>
        r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally")
    }
    // ──────────────── Block 8 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4825>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
    r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
    // CODE → <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    r1 = globalThis.console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally")
    // CODE → <Throw>: <Reg8: 0>
    throw caughtException;
}