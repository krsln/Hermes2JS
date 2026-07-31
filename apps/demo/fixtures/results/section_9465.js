function tryFinallyNoCatchTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4899>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4900>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/try-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/try-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/try-block")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = globalThis.Error;
    // CODE → <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = __uninitialized_this_for_new__;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 3960>  # String: 'no catch here' (String)
    // USED → r4 = "no catch here";
    // CODE → <Mov>: <Reg8: 5, Reg8: 2>
    // USED → r5 = __uninitialized_this_for_new__;
    // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new globalThis.Error("no catch here", __uninitialized_this_for_new__);
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = new globalThis.Error("no catch here", __uninitialized_this_for_new__);
    // CODE → <Throw>: <Reg8: 0>
    throw new globalThis.Error("no catch here", __uninitialized_this_for_new__);
    // CODE → <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4896>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/finally-block";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/finally-block")
    // CODE → <Throw>: <Reg8: 0>
    throw caughtException;
}