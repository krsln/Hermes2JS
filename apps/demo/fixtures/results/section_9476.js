function tryCatchFinallyImplicitThrowTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4873>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/start")
    // CODE → <GetParentEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getParentEnvironment(0);
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 0>
    // USED → r2 = getParentEnvironment(0)[0];
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 0, Reg8: 3>
    // USED → r0 = getParentEnvironment(0)[0].call(0, r3);
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4872>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/result' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/result";
    // CODE → <Call3>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/result", r0)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4870>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block")
    // CODE → <Ret>: <Reg8: 0>
    return getParentEnvironment(0)[0].call(0, r3);
    // CODE → <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4869>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/catch-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/catch-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/catch-block")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4870>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block")
    // CODE → <LoadConstInt>: <Reg8: 0, Imm32: -1>
    // USED → r0 = -1;
    // CODE → <Ret>: <Reg8: 0>
    return -1;
    // CODE → <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4870>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block")
    // CODE → <Throw>: <Reg8: 0>
    throw caughtException;
}