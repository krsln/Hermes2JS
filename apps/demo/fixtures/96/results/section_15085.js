function tryCatchInsideLoopTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <Mov>: <Reg8: 7, Reg8: 2>
    // USED → r7 = param1;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4708>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start' (String)
    // USED → r3 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start")
    // CODE → <LoadConstZero>: <Reg8: 6>
    // USED → r6 = 0;
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <LoadConstZero>: <Reg8: 8>
    // USED → r8 = 0;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
    // USED → r2 = param1.length;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 2131>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught' (String)
    // USED → r5 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught";
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4701>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok' (String)
    // USED → r4 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok";
    if (!(0 < param1.length)) {
        // ──────────────── Block 6 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4699>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        r1 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end")
        // CODE → <Ret>: <Reg8: 0>
        return 0 + 1;
    } else {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → <Mov>: <Reg8: 3, Reg8: 7>
            // USED → r3 = param1;
            // CODE → <Mov>: <Reg8: 2, Reg8: 8>
            // USED → r2 = 0;
            // CODE → <GetByVal>: <Reg8: 2, Reg8: 3, Reg8: 2>
            // USED → r2 = param1[0];
            if (param1[0] >= 0) {
                // ──────────────── Block 2 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 9, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r9 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r3 = globalThis.console.log;
                // CODE → <Mov>: <Reg8: 10, Reg8: 7>
                // USED → r10 = param1;
                // CODE → <Mov>: <Reg8: 2, Reg8: 8>
                // USED → r2 = 0;
                // CODE → <GetByVal>: <Reg8: 2, Reg8: 10, Reg8: 2>
                // USED → r2 = param1[0];
                // CODE → <Call3>: <Reg8: 2, Reg8: 3, Reg8: 9, Reg8: 4, Reg8: 2>
                r2 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok", param1[0])
                // CODE → <Jmp>: <Addr8: 59>  # Address: 0000009e
                goto label_158;
                // LOOP → START (while)
                while (true) {
                    // ──────────────── Block 5 ──────────────── 
                    // CODE → <Mov>: <Reg8: 2, Reg8: 8>
                    // USED → r2 = 0;
                    // CODE → <Inc>: <Reg8: 3, Reg8: 2>
                    // USED → r3 = 0 + 1;
                    // CODE → <Mov>: <Reg8: 8, Reg8: 3>
                    r8 = 0 + 1
                    // CODE → <Mov>: <Reg8: 2, Reg8: 7>
                    // USED → r2 = param1;
                    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
                    // USED → r2 = param1.length;
                    // CODE → <JLess>: <Addr8: -117, Reg8: 3, Reg8: 2>  # Address: 0000003a
                    if (0 + 1 < param1.length) goto label_58;
                    // ──────────────── Block 4 ──────────────── 
                    // CODE → <Catch>: <Reg8: 9>
                    // USED → r9 = caughtException;
                    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r3 = globalThis.console;
                    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r2 = globalThis.console.log;
                    // CODE → <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 9>
                    r2 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught", caughtException)
                    // CODE → <Mov>: <Reg8: 2, Reg8: 0>
                    // USED → r2 = 0;
                    // CODE → <Inc>: <Reg8: 0, Reg8: 2>
                    // USED → r0 = 0 + 1;
                }
                // LOOP → END
            }
        }
        // LOOP → END
        // ──────────────── Block 3 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 1, UInt8: 4, string_id: 12>  # String: 'Error' (Identifier)
        // USED → r9 = globalThis.Error;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 9, UInt8: 5, string_id: 206>  # String: 'prototype' (Identifier)
        // USED → r2 = globalThis.Error.prototype;
        // CODE → <CreateThis>: <Reg8: 3, Reg8: 2, Reg8: 9>
        // USED → r3 = createThis(globalThis.Error.prototype, globalThis.Error);
        // CODE → <LoadConstString>: <Reg8: 12, string_id: 839>  # String: 'negative value' (String)
        // USED → r12 = "negative value";
        // CODE → <Mov>: <Reg8: 13, Reg8: 3>
        r13 = createThis(globalThis.Error.prototype, globalThis.Error)
        // CODE → <Construct>: <Reg8: 2, Reg8: 9, UInt8: 2>
        // USED → r2 = new globalThis.Error("negative value");
        // CODE → <SelectObject>: <Reg8: 2, Reg8: 3, Reg8: 2>
        // USED → r2 = new globalThis.Error("negative value");
        // CODE → <Throw>: <Reg8: 2>
        throw new globalThis.Error("negative value");
    }
}