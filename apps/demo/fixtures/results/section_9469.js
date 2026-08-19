function nestedTryCatchTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 3674>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/start' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 1, string_id: 4851>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-try' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-try";
    // CODE → addr: 37 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-try")
    // CODE → addr: 42 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 48 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 53 | <LoadConstString>: <Reg8: 1, string_id: 4847>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-try' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-try";
    // CODE → addr: 57 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-try")
    // CODE → addr: 62 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → addr: 68 | <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = CreateThisForNew(r3);
    // CODE → addr: 72 | <LoadConstString>: <Reg8: 5, string_id: 9220>  # String: 'inner' (Identifier)
    // USED → r5 = "inner";
    // CODE → addr: 76 | <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThisForNew(r3);
    // CODE → addr: 79 | <Construct>: <Reg8: 1, Reg8: 3, UInt8: 2>
    // USED → r1 = new Error("inner");
    // CODE → addr: 83 | <SelectObject>: <Reg8: 1, Reg8: 2, Reg8: 1>
    // USED → r1 = new Error("inner");
    // CODE → addr: 87 | <Throw>: <Reg8: 1>
    throw new Error("inner");
    // CODE → addr: 89 | <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → addr: 91 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 97 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:102 | <LoadConstString>: <Reg8: 1, string_id: 516>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-catch' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-catch";
    // CODE → addr:106 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-catch")
    // CODE → addr:111 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → addr:117 | <LoadConstString>: <Reg8: 1, string_id: 3368>  # String: 'rethrown from inner: ' (String)
    // USED → r1 = "rethrown from inner: ";
    // CODE → addr:121 | <Add>: <Reg8: 5, Reg8: 1, Reg8: 2>
    // USED → r5 = "rethrown from inner: " + caughtException;
    // CODE → addr:125 | <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = CreateThisForNew(r3);
    // CODE → addr:129 | <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThisForNew(r3);
    // CODE → addr:132 | <Construct>: <Reg8: 1, Reg8: 3, UInt8: 2>
    // USED → r1 = new Error("rethrown from inner: " + caughtException);
    // CODE → addr:136 | <SelectObject>: <Reg8: 1, Reg8: 2, Reg8: 1>
    // USED → r1 = new Error("rethrown from inner: " + caughtException);
    // CODE → addr:140 | <Throw>: <Reg8: 1>
    throw new Error("rethrown from inner: " + caughtException);
    // CODE → addr:142 | <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → addr:144 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:150 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:155 | <LoadConstString>: <Reg8: 1, string_id: 4848>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-catch' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-catch";
    // CODE → addr:159 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-catch")
    // CODE → addr:164 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:170 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:175 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → addr:180 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:186 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:191 | <LoadConstString>: <Reg8: 0, string_id: 4846>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/end";
    // CODE → addr:195 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/end")
    // CODE → addr:200 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:202 | <Ret>: <Reg8: 0>
    return undefined;
}