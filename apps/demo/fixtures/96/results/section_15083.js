function tryCatchFinallyEarlyReturnTest() {
    try {
        // ──────────────── Block 0 ──────────────── 
        // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
        // USED → r0 = globalThis;
        // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4691>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/try-block' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/try-block";
        // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/try-block")
        // CODE → addr: 22 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
        // USED → r2 = Error;
        // CODE → addr: 28 | <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
        // USED → r0 = Error.prototype;
        // CODE → addr: 33 | <CreateThis>: <Reg8: 1, Reg8: 0, Reg8: 2>
        // USED → r1 = CreateThis(r0);
        // CODE → addr: 37 | <LoadConstString>: <Reg8: 4, string_id: 238>  # String: 'test' (Identifier)
        // USED → r4 = "test";
        // CODE → addr: 41 | <Mov>: <Reg8: 5, Reg8: 1>
        // USED → r5 = CreateThis(r0);
        // CODE → addr: 44 | <Construct>: <Reg8: 0, Reg8: 2, UInt8: 2>
        // USED → r0 = new Error("test");
        // CODE → addr: 48 | <SelectObject>: <Reg8: 0, Reg8: 1, Reg8: 0>
        // USED → r0 = new Error("test");
        // CODE → addr: 52 | <Throw>: <Reg8: 0>
        throw new Error("test");
    } catch (caughtException) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 78 | <LoadConstFalse>: <Reg8: 0>
        // USED → r0 = false;
        // CODE → addr: 80 | <Ret>: <Reg8: 0>
        return false;
    } finally {
        // ──────────────── Block 2 ──────────────── 
        // CODE → addr: 84 | <GetGlobalObject>: <Reg8: 1>
        // USED → r1 = globalThis;
        // CODE → addr: 86 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr: 92 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr: 97 | <LoadConstString>: <Reg8: 1, string_id: 4690>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block";
        // CODE → addr:101 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block")
    }
}