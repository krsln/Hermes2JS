function tryCatchFinallyEarlyReturnTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4691>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/try-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/try-block";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/try-block")
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r2 = globalThis.Error;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    r0 = globalThis.Error.prototype
    // CODE → <CreateThis>: <Reg8: 1, Reg8: 0, Reg8: 2>
    // USED → r1 = CreateThis(r0);
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 238>  # String: 'test' (Identifier)
    // USED → r4 = "test";
    // CODE → <Mov>: <Reg8: 5, Reg8: 1>
    // USED → r5 = CreateThis(r0);
    // CODE → <Construct>: <Reg8: 0, Reg8: 2, UInt8: 2>
    // USED → r0 = new globalThis.Error("test");
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = new globalThis.Error("test");
    // CODE → <Throw>: <Reg8: 0>
    throw new globalThis.Error("test");
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4690>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block")
    // CODE → <LoadConstFalse>: <Reg8: 0>
    // USED → r0 = false;
    // CODE → <Ret>: <Reg8: 0>
    return false;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4690>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block")
    // CODE → <Throw>: <Reg8: 0>
    throw caughtException;
}