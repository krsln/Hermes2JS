function tryCatchFinallyImplicitThrowTest(param1) {
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 2, string_id: 4698>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/start' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/start")
    try {
        // ──────────────── Block 0 ──────────────── 
        // CODE → addr: 25 | <GetEnvironment>: <Reg8: 2, UInt8: 0>
        r2 = getEnvironment(0)
        // CODE → addr: 28 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 0>
        // USED → r3 = r2[0];
        // CODE → addr: 32 | <Mov>: <Reg8: 2, Reg8: 0>
        // USED → r2 = param1;
        // CODE → addr: 35 | <LoadConstUndefined>: <Reg8: 0>
        r0 = undefined
        // CODE → addr: 37 | <Call2>: <Reg8: 0, Reg8: 3, Reg8: 0, Reg8: 2>
        // USED → r0 = r2[0].call(r0, r2);
        // CODE → addr: 42 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = console;
        // CODE → addr: 48 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = console.log;
        // CODE → addr: 53 | <LoadConstString>: <Reg8: 2, string_id: 4697>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/result' (String)
        // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/result";
        // CODE → addr: 57 | <Call3>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/result", r0)
    } catch (caughtException) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 87 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr: 93 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr: 98 | <LoadConstString>: <Reg8: 0, string_id: 4694>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/catch-block' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/catch-block";
        // CODE → addr:102 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/catch-block")
    } finally {
        // ──────────────── Block 2 ──────────────── 
        // CODE → addr:137 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr:143 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr:148 | <LoadConstString>: <Reg8: 1, string_id: 4695>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block";
        // CODE → addr:152 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block")
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:127 | <LoadConstInt>: <Reg8: 0, Imm32: -1>
    // USED → r0 = -1;
    // CODE → addr:133 | <Ret>: <Reg8: 0>
    return -1;
}