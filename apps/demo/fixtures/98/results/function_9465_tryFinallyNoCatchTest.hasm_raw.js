function tryFinallyNoCatchTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4899>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 0, string_id: 4900>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/try-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/try-block";
    // CODE → addr: 37 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/try-block")
    // CODE → addr: 42 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → addr: 48 | <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = CreateThisForNew(r3);
    // CODE → addr: 52 | <LoadConstString>: <Reg8: 4, string_id: 3960>  # String: 'no catch here' (String)
    // USED → r4 = "no catch here";
    // CODE → addr: 56 | <Mov>: <Reg8: 5, Reg8: 2>
    // USED → r5 = CreateThisForNew(r3);
    // CODE → addr: 59 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new Error("no catch here");
    // CODE → addr: 63 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    r0 = new Error("no catch here")
    // CODE → addr: 67 | <Throw>: <Reg8: 0>
    throw r0;
    // CODE → addr: 69 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr: 71 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 77 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 82 | <LoadConstString>: <Reg8: 1, string_id: 4896>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/finally-block";
    // CODE → addr: 86 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/finally-block")
    // CODE → addr: 91 | <Throw>: <Reg8: 0>
    throw r0;
}