function tryCatchFinallyImplicitThrowTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4873>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/start")
    // CODE → addr: 22 | <GetParentEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getParentEnvironment(0)
    // CODE → addr: 25 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr: 28 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 0>
    // USED → r2 = r0[0];
    // CODE → addr: 32 | <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → addr: 34 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 0, Reg8: 3>
    r0 = r0[0](param1)
    // CODE → addr: 39 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 45 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 50 | <LoadConstString>: <Reg8: 2, string_id: 4872>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/result' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/result";
    // CODE → addr: 54 | <Call3>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/result", r0)
    // CODE → addr: 60 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 66 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 71 | <LoadConstString>: <Reg8: 2, string_id: 4870>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block";
    // CODE → addr: 75 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block")
    // CODE → addr: 80 | <Ret>: <Reg8: 0>
    return r0;
    // CODE → addr: 82 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr: 84 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 90 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 95 | <LoadConstString>: <Reg8: 0, string_id: 4869>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/catch-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/catch-block";
    // CODE → addr: 99 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/catch-block")
    // CODE → addr:104 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:110 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:115 | <LoadConstString>: <Reg8: 0, string_id: 4870>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block";
    // CODE → addr:119 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block")
    // CODE → addr:124 | <LoadConstInt>: <Reg8: 0, Imm32: -1>
    // USED → r0 = -1;
    // CODE → addr:130 | <Ret>: <Reg8: 0>
    return -1;
    // CODE → addr:132 | <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → addr:134 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:140 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:145 | <LoadConstString>: <Reg8: 1, string_id: 4870>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block";
    // CODE → addr:149 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block")
    // CODE → addr:154 | <Throw>: <Reg8: 0>
    throw caughtException;
}