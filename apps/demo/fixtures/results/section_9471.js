function tryCatchFinallyEarlyReturnTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4864>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/try-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/try-block";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/try-block")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r2 = Error;
    // CODE → addr: 28 | <CreateThisForNew>: <Reg8: 1, Reg8: 2, UInt8: 3>
    // USED → r1 = CreateThisForNew(r2);
    // CODE → addr: 32 | <LoadConstString>: <Reg8: 4, string_id: 47>  # String: 'test' (Identifier)
    // USED → r4 = "test";
    // CODE → addr: 36 | <Mov>: <Reg8: 5, Reg8: 1>
    // USED → r5 = CreateThisForNew(r2);
    // CODE → addr: 39 | <Construct>: <Reg8: 0, Reg8: 2, UInt8: 2>
    // USED → r0 = new Error("test");
    // CODE → addr: 43 | <SelectObject>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = new Error("test");
    // CODE → addr: 47 | <Throw>: <Reg8: 0>
    throw new Error("test");
    // CODE → addr: 49 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr: 51 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr: 53 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 59 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 64 | <LoadConstString>: <Reg8: 0, string_id: 4863>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block";
    // CODE → addr: 68 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block")
    // CODE → addr: 73 | <LoadConstFalse>: <Reg8: 0>
    // USED → r0 = false;
    // CODE → addr: 75 | <Ret>: <Reg8: 0>
    return false;
    // CODE → addr: 77 | <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → addr: 79 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr: 81 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 87 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 92 | <LoadConstString>: <Reg8: 1, string_id: 4863>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block";
    // CODE → addr: 96 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block")
    // CODE → addr:101 | <Throw>: <Reg8: 0>
    throw caughtException;
}