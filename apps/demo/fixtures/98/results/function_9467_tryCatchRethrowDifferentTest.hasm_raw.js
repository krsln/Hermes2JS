function tryCatchRethrowDifferentTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4887>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 0, string_id: 4064>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/try-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/try-block";
    // CODE → addr: 37 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/try-block")
    // CODE → addr: 42 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → addr: 48 | <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = CreateThisForNew(r3);
    // CODE → addr: 52 | <LoadConstString>: <Reg8: 5, string_id: 2554>  # String: 'original' (String)
    // USED → r5 = "original";
    // CODE → addr: 56 | <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThisForNew(r3);
    // CODE → addr: 59 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new Error("original");
    // CODE → addr: 63 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    r0 = new Error("original")
    // CODE → addr: 67 | <Throw>: <Reg8: 0>
    throw r0;
    // CODE → addr: 69 | <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → addr: 71 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 77 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 82 | <LoadConstString>: <Reg8: 0, string_id: 4883>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/catch-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/catch-block";
    // CODE → addr: 86 | <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/catch-block")
    // CODE → addr: 91 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → addr: 97 | <LoadConstString>: <Reg8: 0, string_id: 6428>  # String: 'wrapped: ' (String)
    // USED → r0 = "wrapped: ";
    // CODE → addr:101 | <Add>: <Reg8: 5, Reg8: 0, Reg8: 2>
    // USED → r5 = "wrapped: " + caughtException;
    // CODE → addr:105 | <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = CreateThisForNew(r3);
    // CODE → addr:109 | <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThisForNew(r3);
    // CODE → addr:112 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new Error("wrapped: " + caughtException);
    // CODE → addr:116 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    r0 = new Error("wrapped: " + caughtException)
    // CODE → addr:120 | <Throw>: <Reg8: 0>
    throw r0;
    // CODE → addr:122 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr:124 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:130 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:135 | <LoadConstString>: <Reg8: 1, string_id: 4886>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/finally-block";
    // CODE → addr:139 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/finally-block")
    // CODE → addr:144 | <Throw>: <Reg8: 0>
    throw r0;
}