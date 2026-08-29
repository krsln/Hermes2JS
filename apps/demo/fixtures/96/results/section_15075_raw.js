function tryCatchTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4731>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 0, string_id: 4732>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/try-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/try-block";
    // CODE → addr: 37 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/try-block")
    // CODE → addr: 42 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → addr: 48 | <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r0 = Error.prototype;
    // CODE → addr: 53 | <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
    // USED → r2 = CreateThis(r0);
    // CODE → addr: 57 | <LoadConstString>: <Reg8: 5, string_id: 238>  # String: 'test' (Identifier)
    // USED → r5 = "test";
    // CODE → addr: 61 | <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThis(r0);
    // CODE → addr: 64 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new Error("test");
    // CODE → addr: 68 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    r0 = new Error("test")
    // CODE → addr: 72 | <Throw>: <Reg8: 0>
    throw r0;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 74 | <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → addr: 76 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 82 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 87 | <LoadConstString>: <Reg8: 0, string_id: 4724>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/catch-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/catch-block";
    // CODE → addr: 91 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/catch-block")
    // CODE → addr: 96 | <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:102 | <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r0 = console.log;
    // CODE → addr:107 | <Call2>: <Reg8: 0, Reg8: 0, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → addr:112 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:118 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:123 | <LoadConstString>: <Reg8: 0, string_id: 4730>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block";
    // CODE → addr:127 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block")
    // CODE → addr:132 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:138 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:143 | <LoadConstString>: <Reg8: 0, string_id: 10984>  # String: 'finally' (Identifier)
    // USED → r0 = "finally";
    // CODE → addr:147 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("finally")
    // CODE → addr:152 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:158 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:163 | <LoadConstString>: <Reg8: 0, string_id: 4728>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/end";
    // CODE → addr:167 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/end")
    // CODE → addr:172 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:174 | <Ret>: <Reg8: 0>
    return r0;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr:176 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr:178 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:184 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:189 | <LoadConstString>: <Reg8: 2, string_id: 4730>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block";
    // CODE → addr:193 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block")
    // CODE → addr:198 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:204 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:209 | <LoadConstString>: <Reg8: 1, string_id: 10984>  # String: 'finally' (Identifier)
    // USED → r1 = "finally";
    // CODE → addr:213 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("finally")
    // CODE → addr:218 | <Throw>: <Reg8: 0>
    throw r0;
}