function tryCatchNoFinallyTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4713>  # String: '__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/start' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 1, string_id: 4718>  # String: '__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/try-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/try-block";
    // CODE → addr: 37 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/try-block")
    // CODE → addr: 42 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → addr: 48 | <GetByIdShort>: <Reg8: 1, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r1 = Error.prototype;
    // CODE → addr: 53 | <CreateThis>: <Reg8: 2, Reg8: 1, Reg8: 3>
    // USED → r2 = CreateThis(r1);
    // CODE → addr: 57 | <LoadConstString>: <Reg8: 5, string_id: 6728>  # String: 'no finally here' (String)
    // USED → r5 = "no finally here";
    // CODE → addr: 61 | <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThis(r1);
    // CODE → addr: 64 | <Construct>: <Reg8: 1, Reg8: 3, UInt8: 2>
    // USED → r1 = new Error("no finally here");
    // CODE → addr: 68 | <SelectObject>: <Reg8: 1, Reg8: 2, Reg8: 1>
    // USED → r1 = new Error("no finally here");
    // CODE → addr: 72 | <Throw>: <Reg8: 1>
    throw new Error("no finally here");
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 74 | <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → addr: 76 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 82 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 87 | <LoadConstString>: <Reg8: 1, string_id: 4709>  # String: '__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/catch-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/catch-block";
    // CODE → addr: 91 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/catch-block")
    // CODE → addr: 96 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:102 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:107 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → addr:112 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:118 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:123 | <LoadConstString>: <Reg8: 0, string_id: 4710>  # String: '__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/end";
    // CODE → addr:127 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/end")
    // CODE → addr:132 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:134 | <Ret>: <Reg8: 0>
    return undefined;
}