function tryFinallyNormalCompletionTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4903>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 0, string_id: 4904>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/try-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/try-block";
    // CODE → addr: 37 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/try-block")
    // CODE → addr: 42 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 48 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 53 | <LoadConstString>: <Reg8: 0, string_id: 4901>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/finally-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/finally-block";
    // CODE → addr: 57 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/finally-block")
    // CODE → addr: 62 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 68 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 73 | <LoadConstString>: <Reg8: 0, string_id: 3024>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/end";
    // CODE → addr: 77 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/end")
    // CODE → addr: 82 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 84 | <Ret>: <Reg8: 0>
    return undefined;
    // CODE → addr: 86 | <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → addr: 88 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 94 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 99 | <LoadConstString>: <Reg8: 1, string_id: 4901>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/finally-block";
    // CODE → addr:103 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/finally-block")
    // CODE → addr:108 | <Throw>: <Reg8: 0>
    throw caughtException;
}