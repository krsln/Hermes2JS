function nestedTryCatchFinallyTest() {
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4845>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/start")
    try {
        try {
            // ──────────────── Block 0 ──────────────── 
            // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r3 = console;
            // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r2 = console.log;
            // CODE → addr: 33 | <LoadConstString>: <Reg8: 0, string_id: 4840>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-try' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-try";
            // CODE → addr: 37 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-try")
            // CODE → addr: 42 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
            // USED → r3 = Error;
            // CODE → addr: 48 | <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
            // USED → r2 = CreateThisForNew(r3);
            // CODE → addr: 52 | <LoadConstString>: <Reg8: 5, string_id: 9220>  # String: 'inner' (Identifier)
            // USED → r5 = "inner";
            // CODE → addr: 56 | <Mov>: <Reg8: 6, Reg8: 2>
            // USED → r6 = CreateThisForNew(r3);
            // CODE → addr: 59 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
            // USED → r0 = new Error("inner");
            // CODE → addr: 63 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
            // USED → r0 = new Error("inner");
            // CODE → addr: 67 | <Throw>: <Reg8: 0>
            throw new Error("inner");
        } catch (caughtException) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → addr: 71 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r3 = console;
            // CODE → addr: 77 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r2 = console.log;
            // CODE → addr: 82 | <LoadConstString>: <Reg8: 0, string_id: 3823>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-catch' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-catch";
            // CODE → addr: 86 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-catch")
        } finally {
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr:135 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r4 = console;
            // CODE → addr:141 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r3 = console.log;
            // CODE → addr:146 | <LoadConstString>: <Reg8: 2, string_id: 4837>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-finally' (String)
            // USED → r2 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-finally";
            // CODE → addr:150 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
            console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-finally")
        }
        // ──────────────── Block 7 ──────────────── 
        // CODE → addr:111 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr:117 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr:122 | <LoadConstString>: <Reg8: 0, string_id: 4832>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/after-inner' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/after-inner";
        // CODE → addr:126 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/after-inner")
        // CODE → addr:131 | <Jmp>: <Addr8: 48>  # Address: 000000b3
        goto label_179;
    } catch (caughtException) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → addr:159 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr:165 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr:170 | <LoadConstString>: <Reg8: 0, string_id: 4842>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-catch' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-catch";
        // CODE → addr:174 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-catch")
    } finally {
        // ──────────────── Block 5 ──────────────── 
        // CODE → addr:225 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr:231 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr:236 | <LoadConstString>: <Reg8: 1, string_id: 4843>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally";
        // CODE → addr:240 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally")
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:199 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:205 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:210 | <LoadConstString>: <Reg8: 0, string_id: 4835>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/end";
    // CODE → addr:214 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/end")
    // CODE → addr:219 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:221 | <Ret>: <Reg8: 0>
    return undefined;
}