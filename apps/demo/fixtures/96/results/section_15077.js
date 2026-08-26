function tryFinallyNoCatchTest() {
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4738>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/start")
    try {
        // ──────────────── Block 0 ──────────────── 
        // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr: 33 | <LoadConstString>: <Reg8: 0, string_id: 4739>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/try-block' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/try-block";
        // CODE → addr: 37 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/try-block")
        // CODE → addr: 42 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
        // USED → r3 = Error;
        // CODE → addr: 48 | <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
        // USED → r0 = Error.prototype;
        // CODE → addr: 53 | <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
        // USED → r2 = CreateThis(r0);
        // CODE → addr: 57 | <LoadConstString>: <Reg8: 4, string_id: 6760>  # String: 'no catch here' (String)
        // USED → r4 = "no catch here";
        // CODE → addr: 61 | <Mov>: <Reg8: 5, Reg8: 2>
        // USED → r5 = CreateThis(r0);
        // CODE → addr: 64 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
        // USED → r0 = new Error("no catch here");
        // CODE → addr: 68 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
        // USED → r0 = new Error("no catch here");
        // CODE → addr: 72 | <Throw>: <Reg8: 0>
        throw new Error("no catch here");
    } finally {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 76 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr: 82 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr: 87 | <LoadConstString>: <Reg8: 1, string_id: 4737>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/finally-block' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/finally-block";
        // CODE → addr: 91 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/finally-block")
    }
}