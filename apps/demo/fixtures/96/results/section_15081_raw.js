function nestedTryCatchTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 1851>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/start' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 1, string_id: 4677>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-try' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-try";
    // CODE → addr: 37 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-try")
    // CODE → addr: 42 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 48 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 53 | <LoadConstString>: <Reg8: 1, string_id: 4672>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-try' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-try";
    // CODE → addr: 57 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-try")
    // CODE → addr: 62 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → addr: 68 | <GetByIdShort>: <Reg8: 1, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r1 = Error.prototype;
    // CODE → addr: 73 | <CreateThis>: <Reg8: 2, Reg8: 1, Reg8: 3>
    // USED → r2 = CreateThis(r1);
    // CODE → addr: 77 | <LoadConstString>: <Reg8: 5, string_id: 7723>  # String: 'inner' (Identifier)
    // USED → r5 = "inner";
    // CODE → addr: 81 | <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThis(r1);
    // CODE → addr: 84 | <Construct>: <Reg8: 1, Reg8: 3, UInt8: 2>
    // USED → r1 = new Error("inner");
    // CODE → addr: 88 | <SelectObject>: <Reg8: 1, Reg8: 2, Reg8: 1>
    r1 = new Error("inner")
    // CODE → addr: 92 | <Throw>: <Reg8: 1>
    throw r1;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 94 | <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → addr: 96 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:102 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:107 | <LoadConstString>: <Reg8: 1, string_id: 4670>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-catch' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-catch";
    // CODE → addr:111 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-catch")
    // CODE → addr:116 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → addr:122 | <LoadConstString>: <Reg8: 1, string_id: 6991>  # String: 'rethrown from inner: ' (String)
    // USED → r1 = "rethrown from inner: ";
    // CODE → addr:126 | <Add>: <Reg8: 5, Reg8: 1, Reg8: 2>
    // USED → r5 = "rethrown from inner: " + caughtException;
    // CODE → addr:130 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r2 = Error.prototype;
    // CODE → addr:135 | <CreateThis>: <Reg8: 2, Reg8: 2, Reg8: 3>
    // USED → r2 = CreateThis(r2);
    // CODE → addr:139 | <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThis(r2);
    // CODE → addr:142 | <Construct>: <Reg8: 1, Reg8: 3, UInt8: 2>
    // USED → r1 = new Error("rethrown from inner: " + caughtException);
    // CODE → addr:146 | <SelectObject>: <Reg8: 1, Reg8: 2, Reg8: 1>
    r1 = new Error("rethrown from inner: " + caughtException)
    // CODE → addr:150 | <Throw>: <Reg8: 1>
    throw r1;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr:152 | <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → addr:154 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:160 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:165 | <LoadConstString>: <Reg8: 1, string_id: 4675>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-catch' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-catch";
    // CODE → addr:169 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-catch")
    // CODE → addr:174 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:180 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:185 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → addr:190 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:196 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:201 | <LoadConstString>: <Reg8: 0, string_id: 4667>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/end";
    // CODE → addr:205 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/end")
    // CODE → addr:210 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:212 | <Ret>: <Reg8: 0>
    return r0;
}