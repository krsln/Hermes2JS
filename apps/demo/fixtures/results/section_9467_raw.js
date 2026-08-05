function tryCatchRethrowDifferentTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4887>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4064>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/try-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/try-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/try-block")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = globalThis.Error;
    // CODE → <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = __uninitialized_this_for_new__;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 2554>  # String: 'original' (String)
    // USED → r5 = "original";
    // CODE → <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = __uninitialized_this_for_new__;
    // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new globalThis.Error("original", __uninitialized_this_for_new__);
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = new globalThis.Error("original", __uninitialized_this_for_new__);
    // CODE → <Throw>: <Reg8: 0>
    throw new globalThis.Error("original", __uninitialized_this_for_new__);
    // CODE → <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4883>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/catch-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/catch-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 0>
    r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/catch-block")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = globalThis.Error;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 6428>  # String: 'wrapped: ' (String)
    // USED → r0 = "wrapped: ";
    // CODE → <Add>: <Reg8: 5, Reg8: 0, Reg8: 2>
    // USED → r5 = "wrapped: " + caughtException;
    // CODE → <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = __uninitialized_this_for_new__;
    // CODE → <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = __uninitialized_this_for_new__;
    // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new globalThis.Error("wrapped: " + caughtException, __uninitialized_this_for_new__);
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = new globalThis.Error("wrapped: " + caughtException, __uninitialized_this_for_new__);
    // CODE → <Throw>: <Reg8: 0>
    throw new globalThis.Error("wrapped: " + caughtException, __uninitialized_this_for_new__);
    // CODE → <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4886>  # String: '__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/finally-block";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/finally-block")
    // CODE → <Throw>: <Reg8: 0>
    throw caughtException;
}