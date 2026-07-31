function tryCatchFinallyEarlyReturnTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4864>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/try-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/try-block";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/try-block")
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r2 = globalThis.Error;
    // CODE → <CreateThisForNew>: <Reg8: 1, Reg8: 2, UInt8: 3>
    // USED → r1 = __uninitialized_this_for_new__;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 47>  # String: 'test' (Identifier)
    r4 = "test"
    // CODE → <Mov>: <Reg8: 5, Reg8: 1>
    r5 = __uninitialized_this_for_new__
    // CODE → <Construct>: <Reg8: 0, Reg8: 2, UInt8: 2>
    // USED → r0 = new globalThis.Error(globalThis, __uninitialized_this_for_new__);
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = __uninitialized_this_for_new__[new globalThis.Error(globalThis, __uninitialized_this_for_new__)];
    // CODE → <Throw>: <Reg8: 0>
    throw __uninitialized_this_for_new__[new globalThis.Error(globalThis, __uninitialized_this_for_new__)];
    // CODE → <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4863>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block")
    // CODE → <LoadConstFalse>: <Reg8: 0>
    // USED → r0 = false;
    // CODE → <Ret>: <Reg8: 0>
    return false;
    // CODE → <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4863>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block")
    // CODE → <Throw>: <Reg8: 0>
    throw caughtException;
}