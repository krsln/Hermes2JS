function tryCatchNoFinallyTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4881>  # String: '__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/start' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 1, string_id: 4882>  # String: '__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/try-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/try-block";
    // CODE → addr: 37 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/try-block")
    // CODE → addr: 42 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → addr: 48 | <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = CreateThisForNew(r3);
    // CODE → addr: 52 | <LoadConstString>: <Reg8: 5, string_id: 2722>  # String: 'no finally here' (String)
    // USED → r5 = "no finally here";
    // CODE → addr: 56 | <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThisForNew(r3);
    // CODE → addr: 59 | <Construct>: <Reg8: 1, Reg8: 3, UInt8: 2>
    // USED → r1 = new Error("no finally here");
    // CODE → addr: 63 | <SelectObject>: <Reg8: 1, Reg8: 2, Reg8: 1>
    // USED → r1 = new Error("no finally here");
    // CODE → addr: 67 | <Throw>: <Reg8: 1>
    throw new Error("no finally here");
    // CODE → addr: 69 | <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → addr: 71 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 77 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 82 | <LoadConstString>: <Reg8: 1, string_id: 4880>  # String: '__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/catch-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/catch-block";
    // CODE → addr: 86 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/catch-block")
    // CODE → addr: 91 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 97 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:102 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → addr:107 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:113 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:118 | <LoadConstString>: <Reg8: 0, string_id: 734>  # String: '__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/end";
    // CODE → addr:122 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/end")
    // CODE → addr:127 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:129 | <Ret>: <Reg8: 0>
    return undefined;
}