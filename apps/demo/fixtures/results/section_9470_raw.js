function nestedTryCatchFinallyTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4845>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4840>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-try' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-try";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-try")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = globalThis.Error;
    // CODE → <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = CreateThisForNew(r3);
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 9220>  # String: 'inner' (Identifier)
    // USED → r5 = "inner";
    // CODE → <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThisForNew(r3);
    // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new globalThis.Error("inner");
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = new globalThis.Error("inner");
    // CODE → <Throw>: <Reg8: 0>
    throw new globalThis.Error("inner");
    // CODE → <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 3823>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-catch' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-catch";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-catch")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4837>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-finally' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-finally";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-finally")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4832>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/after-inner' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/after-inner";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/after-inner")
    // CODE → <Jmp>: <Addr8: 48>  # Address: 000000b3
    goto label_179;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4837>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-finally' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-finally";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-finally")
    // CODE → <Throw>: <Reg8: 0>
    throw caughtException;
    // CODE → <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4842>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-catch' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-catch";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-catch")
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4843>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4835>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
    // CODE → <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4843>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally")
    // CODE → <Throw>: <Reg8: 0>
    throw caughtException;
}