function tryCatchFinallyImplicitThrowTest(param0, param1) {
    try {
        // ──────────────── Block 0 ──────────────── 
        // CODE → <LoadParam>: <Reg8: 0, UInt8: 1>
        // USED → r0 = param1;
        // CODE → <GetGlobalObject>: <Reg8: 1>
        // USED → r1 = globalThis;
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 4698>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/start' (String)
        // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/start";
        // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        r2 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/start")
        // CODE → <GetEnvironment>: <Reg8: 2, UInt8: 0>
        // USED → r2 = getEnvironment(0);
        // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 0>
        // USED → r3 = getEnvironment(0)[0];
        // CODE → <Mov>: <Reg8: 2, Reg8: 0>
        // USED → r2 = param1;
        // CODE → <LoadConstUndefined>: <Reg8: 0>
        // USED → r0 = undefined;
        // CODE → <Call2>: <Reg8: 0, Reg8: 3, Reg8: 0, Reg8: 2>
        // USED → r0 = getEnvironment(0)[0].call(undefined, param1);
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 4697>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/result' (String)
        // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/result";
        // CODE → <Call3>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 0>
        r2 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/result", getEnvironment(0)[0].call(undefined, param1))
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 4695>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block' (String)
        // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block";
        // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        r2 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block")
        // CODE → <Ret>: <Reg8: 0>
        return getEnvironment(0)[0].call(undefined, param1);
    } catch (caughtException) {
        try {
            // ──────────────── Block 1 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 4694>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/catch-block' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/catch-block";
            // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/catch-block")
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 4695>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block";
            // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block")
            // CODE → <LoadConstInt>: <Reg8: 0, Imm32: -1>
            // USED → r0 = -1;
            // CODE → <Ret>: <Reg8: 0>
            return -1;
        } catch (caughtException) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 1, string_id: 4695>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block' (String)
            // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block";
            // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
            r1 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block")
            // CODE → <Throw>: <Reg8: 0>
            throw caughtException;
        }
    }
}