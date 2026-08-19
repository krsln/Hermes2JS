function tryCatchRethrowDifferentTest() {
    try {
        try {
            // ──────────────── Block 0 ──────────────── 
            // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
            // USED → r1 = globalThis;
            // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = console;
            // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = console.log;
            // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4722>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/start' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/start";
            // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/start")
            // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = console;
            // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = console.log;
            // CODE → addr: 33 | <LoadConstString>: <Reg8: 0, string_id: 4723>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/try-block' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/try-block";
            // CODE → addr: 37 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/try-block")
            // CODE → addr: 42 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
            // USED → r3 = Error;
            // CODE → addr: 48 | <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
            // USED → r0 = Error.prototype;
            // CODE → addr: 53 | <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
            // USED → r2 = CreateThis(r0);
            // CODE → addr: 57 | <LoadConstString>: <Reg8: 5, string_id: 2463>  # String: 'original' (String)
            // USED → r5 = "original";
            // CODE → addr: 61 | <Mov>: <Reg8: 6, Reg8: 2>
            // USED → r6 = CreateThis(r0);
            // CODE → addr: 64 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
            // USED → r0 = new Error("original");
            // CODE → addr: 68 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
            // USED → r0 = new Error("original");
            // CODE → addr: 72 | <Throw>: <Reg8: 0>
            throw new Error("original");
        } catch (caughtException) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → addr: 76 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r4 = console;
            // CODE → addr: 82 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r3 = console.log;
            // CODE → addr: 87 | <LoadConstString>: <Reg8: 0, string_id: 4720>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/catch-block' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/catch-block";
            // CODE → addr: 91 | <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 0>
            console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/catch-block")
            // CODE → addr: 96 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
            // USED → r3 = Error;
            // CODE → addr:102 | <LoadConstString>: <Reg8: 0, string_id: 3427>  # String: 'wrapped: ' (String)
            // USED → r0 = "wrapped: ";
            // CODE → addr:106 | <Add>: <Reg8: 5, Reg8: 0, Reg8: 2>
            // USED → r5 = "wrapped: " + caughtException;
            // CODE → addr:110 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
            // USED → r2 = Error.prototype;
            // CODE → addr:115 | <CreateThis>: <Reg8: 2, Reg8: 2, Reg8: 3>
            // USED → r2 = CreateThis(r2);
            // CODE → addr:119 | <Mov>: <Reg8: 6, Reg8: 2>
            // USED → r6 = CreateThis(r2);
            // CODE → addr:122 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
            // USED → r0 = new Error("wrapped: " + caughtException);
            // CODE → addr:126 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
            // USED → r0 = new Error("wrapped: " + caughtException);
            // CODE → addr:130 | <Throw>: <Reg8: 0>
            throw new Error("wrapped: " + caughtException);
        }
    } finally {
        // ──────────────── Block 2 ──────────────── 
        // CODE → addr:134 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr:140 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr:145 | <LoadConstString>: <Reg8: 1, string_id: 4721>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/finally-block' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/finally-block";
        // CODE → addr:149 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/finally-block")
    }
}