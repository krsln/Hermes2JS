function tryCatchRethrowDifferentTest() {
    try {
        try {
            // ──────────────── Block 0 ──────────────── 
            // CODE → <GetGlobalObject>: <Reg8: 1>
            // USED → r1 = globalThis;
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = console.log;
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 4722>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/start' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/start";
            // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/start")
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = console.log;
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 4723>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/try-block' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/try-block";
            // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/try-block")
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
            // USED → r3 = Error;
            // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
            // USED → r0 = Error.prototype;
            // CODE → <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
            // USED → r2 = CreateThis(r0);
            // CODE → <LoadConstString>: <Reg8: 5, string_id: 2463>  # String: 'original' (String)
            // USED → r5 = "original";
            // CODE → <Mov>: <Reg8: 6, Reg8: 2>
            // USED → r6 = CreateThis(r0);
            // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
            // USED → r0 = new Error("original");
            // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
            // USED → r0 = new Error("original");
            // CODE → <Throw>: <Reg8: 0>
            throw new Error("original");
        } catch (caughtException) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r4 = console;
            // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r3 = console.log;
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 4720>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/catch-block' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/catch-block";
            // CODE → <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 0>
            console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/catch-block")
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
            // USED → r3 = Error;
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 3427>  # String: 'wrapped: ' (String)
            // USED → r0 = "wrapped: ";
            // CODE → <Add>: <Reg8: 5, Reg8: 0, Reg8: 2>
            // USED → r5 = "wrapped: " + caughtException;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
            // USED → r2 = Error.prototype;
            // CODE → <CreateThis>: <Reg8: 2, Reg8: 2, Reg8: 3>
            // USED → r2 = CreateThis(r2);
            // CODE → <Mov>: <Reg8: 6, Reg8: 2>
            // USED → r6 = CreateThis(r2);
            // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
            // USED → r0 = new Error("wrapped: " + caughtException);
            // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
            // USED → r0 = new Error("wrapped: " + caughtException);
            // CODE → <Throw>: <Reg8: 0>
            throw new Error("wrapped: " + caughtException);
        }
    } finally {
        // ──────────────── Block 2 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4721>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/finally-block' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/finally-block";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/finally-block")
    }
}