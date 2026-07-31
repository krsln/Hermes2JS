function tryCatchFinallyBranchInFinallyTest(param0, param1) {
    try {
        // ──────────────── Block 0 ──────────────── 
        // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
        // USED → r1 = param1;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 4688>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block' (String)
        // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block";
        // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        r2 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block")
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
        // USED → r3 = globalThis.Error;
        // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
        // USED → r0 = globalThis.Error.prototype;
        // CODE → <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
        // USED → r2 = createThis(globalThis.Error.prototype, globalThis.Error);
        // CODE → <LoadConstString>: <Reg8: 5, string_id: 238>  # String: 'test' (Identifier)
        r5 = "test"
        // CODE → <Mov>: <Reg8: 6, Reg8: 2>
        r6 = createThis(globalThis.Error.prototype, globalThis.Error)
        // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
        // USED → r0 = new globalThis.Error(param1, createThis(globalThis.Error.prototype, globalThis.Error));
        // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
        // USED → r0 = createThis(globalThis.Error.prototype, globalThis.Error)[new globalThis.Error(param1, createThis(globalThis.Error.prototype, globalThis.Error))];
        // CODE → <Throw>: <Reg8: 0>
        throw createThis(globalThis.Error.prototype, globalThis.Error)[new globalThis.Error(param1, createThis(globalThis.Error.prototype, globalThis.Error))];
    } catch (caughtException) {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 4 ──────────────── 
            // CODE → <LoadConstUndefined>: <Reg8: 0>
            // USED → r0 = undefined;
            // CODE → <Ret>: <Reg8: 0>
            return undefined;
            // LOOP → START (while)
            while (true) {
                // ──────────────── Block 2 ──────────────── 
                // CODE → <LoadConstString>: <Reg8: 0, string_id: 4685>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false' (String)
                // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false";
                // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
                r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false")
                // CODE → <Jmp>: <Addr8: 11>  # Address: 00000076
                goto label_118;
            }
            // LOOP → END
            // LOOP → START (while)
            while (true) {
                // ──────────────── Block 3 ──────────────── 
                // CODE → <LoadConstString>: <Reg8: 0, string_id: 4687>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true' (String)
                // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true";
                // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
                r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true")
                // ──────────────── Block 1 ──────────────── 
                // CODE → <LoadConstString>: <Reg8: 0, string_id: 2167>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block' (String)
                // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block";
                // CODE → <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 0>
                r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block")
                // CODE → <Mov>: <Reg8: 0, Reg8: 1>
                // USED → r0 = param1;
                // CODE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r3 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r2 = globalThis.console.log;
                // CODE → <JmpTrue>: <Addr8: 14, Reg8: 0>  # Address: 0000006d
                if (param1) goto label_109;
            }
            // LOOP → END
        }
        // LOOP → END
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 8 ──────────────── 
            // CODE → <Throw>: <Reg8: 0>
            throw caughtException;
            // LOOP → START (while)
            while (true) {
                // ──────────────── Block 6 ──────────────── 
                // CODE → <LoadConstString>: <Reg8: 1, string_id: 4685>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false' (String)
                // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false";
                // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
                r1 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false")
                // CODE → <Jmp>: <Addr8: 11>  # Address: 000000a0
                goto label_160;
            }
            // LOOP → END
            // LOOP → START (while)
            while (true) {
                // ──────────────── Block 7 ──────────────── 
                // CODE → <LoadConstString>: <Reg8: 1, string_id: 4687>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true' (String)
                // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true";
                // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
                r1 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true")
            }
            // LOOP → END
        }
        // LOOP → END
    } finally {
        // ──────────────── Block 5 ──────────────── 
        // CODE → <GetGlobalObject>: <Reg8: 2>
        // USED → r2 = globalThis;
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <JmpTrue>: <Addr8: 14, Reg8: 1>  # Address: 00000097
        if (param1) goto label_151;
    }
}