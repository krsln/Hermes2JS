function tryFinallyNoCatchTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4738>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4739>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/try-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/try-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/try-block")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r3 = globalThis.Error;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    r0 = globalThis.Error.prototype
    // CODE → <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
    // USED → r2 = CreateThis(r0);
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 6760>  # String: 'no catch here' (String)
    // USED → r4 = "no catch here";
    // CODE → <Mov>: <Reg8: 5, Reg8: 2>
    // USED → r5 = CreateThis(r0);
    // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new globalThis.Error("no catch here");
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = new globalThis.Error("no catch here");
    // CODE → <Throw>: <Reg8: 0>
    throw new globalThis.Error("no catch here");
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4737>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/finally-block";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/finally-block")
    // CODE → <Throw>: <Reg8: 0>
    throw caughtException;
}