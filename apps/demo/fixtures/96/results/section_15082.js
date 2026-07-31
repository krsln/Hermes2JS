function nestedTryCatchFinallyTest(param0) {
    try {
        // ──────────────── Block 0 ──────────────── 
        // CODE → <GetGlobalObject>: <Reg8: 1>
        // USED → r1 = globalThis;
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 0, string_id: 4666>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/start' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/start";
        // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
        r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/start")
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 0, string_id: 1278>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-try' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-try";
        // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
        r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-try")
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
        // USED → r3 = globalThis.Error;
        // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
        // USED → r0 = globalThis.Error.prototype;
        // CODE → <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
        // USED → r2 = createThis(globalThis.Error.prototype, globalThis.Error);
        // CODE → <LoadConstString>: <Reg8: 5, string_id: 7723>  # String: 'inner' (Identifier)
        r5 = "inner"
        // CODE → <Mov>: <Reg8: 6, Reg8: 2>
        r6 = createThis(globalThis.Error.prototype, globalThis.Error)
        // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
        // USED → r0 = new globalThis.Error(globalThis, createThis(globalThis.Error.prototype, globalThis.Error));
        // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
        // USED → r0 = createThis(globalThis.Error.prototype, globalThis.Error)[new globalThis.Error(globalThis, createThis(globalThis.Error.prototype, globalThis.Error))];
        // CODE → <Throw>: <Reg8: 0>
        throw createThis(globalThis.Error.prototype, globalThis.Error)[new globalThis.Error(globalThis, createThis(globalThis.Error.prototype, globalThis.Error))];
    } catch (caughtException) {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 4 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 4659>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/end' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/end";
            // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/end")
            // CODE → <LoadConstUndefined>: <Reg8: 0>
            // USED → r0 = undefined;
            // CODE → <Ret>: <Reg8: 0>
            return undefined;
            // ──────────────── Block 1 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 4661>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-catch' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-catch";
            // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-catch")
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 4657>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/after-inner' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/after-inner";
            // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/after-inner")
            // CODE → <Jmp>: <Addr8: 48>  # Address: 000000b8
            goto label_184;
        }
        // LOOP → END
    } finally {
        // ──────────────── Block 5 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4665>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        r1 = globalThis.console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally")
    }
}