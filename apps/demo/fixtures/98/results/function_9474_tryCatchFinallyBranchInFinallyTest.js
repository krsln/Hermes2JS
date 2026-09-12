function tryCatchFinallyBranchInFinallyTest(param1) {
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    try {
        // ──────────────── Block 0 ──────────────── 
        // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 0>
        // USED → r0 = globalThis;
        // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r4 = console;
        // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r3 = console.log;
        // CODE → addr: 16 | <LoadConstString>: <Reg8: 2, string_id: 4862>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block' (String)
        // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block";
        // CODE → addr: 20 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block")
        // CODE → addr: 25 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
        // USED → r3 = Error;
        // CODE → addr: 31 | <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
        // USED → r2 = CreateThisForNew(r3);
        // CODE → addr: 35 | <LoadConstString>: <Reg8: 5, string_id: 47>  # String: 'test' (Identifier)
        // USED → r5 = "test";
        // CODE → addr: 39 | <Mov>: <Reg8: 6, Reg8: 2>
        // USED → r6 = CreateThisForNew(r3);
        // CODE → addr: 42 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
        // USED → r0 = new Error("test");
        // CODE → addr: 46 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
        // USED → r0 = new Error("test");
        // CODE → addr: 50 | <Throw>: <Reg8: 0>
        throw new Error("test");
    } catch (caughtException) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 67 | <LoadConstString>: <Reg8: 2, string_id: 2163>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block' (String)
        // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block";
        // CODE → addr: 71 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block")
        // CODE → addr: 76 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr: 82 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
    } finally {
        // ──────────────── Block 5 ──────────────── 
        // CODE → addr:116 | <GetGlobalObject>: <Reg8: 2>
        // USED → r2 = globalThis;
        // CODE → addr:118 | <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr:124 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        if (param1) {
            // ──────────────── Block 7 ──────────────── 
            // CODE → addr:143 | <LoadConstString>: <Reg8: 1, string_id: 4861>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true' (String)
            // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true";
            // CODE → addr:147 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
            console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true")
        } else {
            // ──────────────── Block 6 ──────────────── 
            // CODE → addr:132 | <LoadConstString>: <Reg8: 1, string_id: 4858>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false' (String)
            // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false";
            // CODE → addr:136 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
            console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false")
        }
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:110 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:112 | <Ret>: <Reg8: 0>
    return undefined;
}