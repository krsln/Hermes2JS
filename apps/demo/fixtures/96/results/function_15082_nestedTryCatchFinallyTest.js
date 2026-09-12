function nestedTryCatchFinallyTest() {
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4666>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/start")
    try {
        try {
            // ──────────────── Block 0 ──────────────── 
            // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = console;
            // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = console.log;
            // CODE → addr: 33 | <LoadConstString>: <Reg8: 0, string_id: 1278>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-try' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-try";
            // CODE → addr: 37 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-try")
            // CODE → addr: 42 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
            // USED → r3 = Error;
            // CODE → addr: 48 | <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
            // USED → r0 = Error.prototype;
            // CODE → addr: 53 | <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
            // USED → r2 = CreateThis(r0);
            // CODE → addr: 57 | <LoadConstString>: <Reg8: 5, string_id: 7723>  # String: 'inner' (Identifier)
            // USED → r5 = "inner";
            // CODE → addr: 61 | <Mov>: <Reg8: 6, Reg8: 2>
            // USED → r6 = CreateThis(r0);
            // CODE → addr: 64 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
            // USED → r0 = new Error("inner");
            // CODE → addr: 68 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
            // USED → r0 = new Error("inner");
            // CODE → addr: 72 | <Throw>: <Reg8: 0>
            throw new Error("inner");
        } catch (caughtException) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → addr: 76 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = console;
            // CODE → addr: 82 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = console.log;
            // CODE → addr: 87 | <LoadConstString>: <Reg8: 0, string_id: 4661>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-catch' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-catch";
            // CODE → addr: 91 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-catch")
        } finally {
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr:140 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r4 = console;
            // CODE → addr:146 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r3 = console.log;
            // CODE → addr:151 | <LoadConstString>: <Reg8: 2, string_id: 4664>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-finally' (String)
            // USED → r2 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-finally";
            // CODE → addr:155 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
            console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-finally")
        }
        // ──────────────── Block 7 ──────────────── 
        // CODE → addr:116 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr:122 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr:127 | <LoadConstString>: <Reg8: 0, string_id: 4657>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/after-inner' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/after-inner";
        // CODE → addr:131 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/after-inner")
        // CODE → addr:136 | <Jmp>: <Addr8: 48>  # Address: 000000b8
        goto label_184;
    } catch (caughtException) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → addr:164 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr:170 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr:175 | <LoadConstString>: <Reg8: 0, string_id: 836>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-catch' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-catch";
        // CODE → addr:179 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-catch")
    } finally {
        // ──────────────── Block 5 ──────────────── 
        // CODE → addr:230 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr:236 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr:241 | <LoadConstString>: <Reg8: 1, string_id: 4665>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally";
        // CODE → addr:245 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally")
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:204 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:210 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:215 | <LoadConstString>: <Reg8: 0, string_id: 4659>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/end";
    // CODE → addr:219 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/end")
    // CODE → addr:224 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:226 | <Ret>: <Reg8: 0>
    return undefined;
}