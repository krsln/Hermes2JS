function tryCatchFinallyBranchInFinallyTest(param1) {
    try {
        // ──────────────── Block 0 ──────────────── 
        // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
        // USED → r1 = param1;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 4688>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block' (String)
        // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block";
        // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block")
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
        // USED → r3 = Error;
        // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
        // USED → r0 = Error.prototype;
        // CODE → <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
        // USED → r2 = CreateThis(r0);
        // CODE → <LoadConstString>: <Reg8: 5, string_id: 238>  # String: 'test' (Identifier)
        // USED → r5 = "test";
        // CODE → <Mov>: <Reg8: 6, Reg8: 2>
        // USED → r6 = CreateThis(r0);
        // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
        // USED → r0 = new Error("test");
        // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
        // USED → r0 = new Error("test");
        // CODE → <Throw>: <Reg8: 0>
        throw new Error("test");
    } catch (caughtException) {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 4 ──────────────── 
            // CODE → <LoadConstUndefined>: <Reg8: 0>
            // USED → r0 = undefined;
            // CODE → <Ret>: <Reg8: 0>
            return undefined;
            // LOOP → START (for)
            for (; !param1; r2 = console.log) {
                // ──────────────── Block 2 ──────────────── 
                // CODE → <LoadConstString>: <Reg8: 0, string_id: 4685>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false' (String)
                // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false";
                // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
                console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false")
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
                console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true")
                // ──────────────── Block 1 ──────────────── 
                // CODE → <LoadConstString>: <Reg8: 0, string_id: 2167>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block' (String)
                // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block";
                // CODE → <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 0>
                console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block")
                // CODE → <Mov>: <Reg8: 0, Reg8: 1>
                // USED → r0 = param1;
                // CODE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r3 = console;
            }
            // LOOP → END
        }
        // LOOP → END
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 8 ──────────────── 
            // CODE → <Throw>: <Reg8: 0>
            throw caughtException;
            // LOOP → START (for)
            for (; !param1; r2 = console.log) {
                // ──────────────── Block 6 ──────────────── 
                // CODE → <LoadConstString>: <Reg8: 1, string_id: 4685>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false' (String)
                // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false";
                // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
                console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false")
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
                console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true")
            }
            // LOOP → END
        }
        // LOOP → END
    } finally {
        // ──────────────── Block 5 ──────────────── 
        // CODE → <GetGlobalObject>: <Reg8: 2>
        // USED → r2 = globalThis;
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
    }
}