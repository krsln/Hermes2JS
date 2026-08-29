function tryCatchTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4890>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 0, string_id: 4891>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/try-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/try-block";
    // CODE → addr: 37 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/try-block")
    // CODE → addr: 42 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → addr: 48 | <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = CreateThisForNew(r3);
    // CODE → addr: 52 | <LoadConstString>: <Reg8: 5, string_id: 47>  # String: 'test' (Identifier)
    // USED → r5 = "test";
    // CODE → addr: 56 | <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThisForNew(r3);
    // CODE → addr: 59 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new Error("test");
    // CODE → addr: 63 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    r0 = new Error("test")
    // CODE → addr: 67 | <Throw>: <Reg8: 0>
    throw r0;
    // CODE → addr: 69 | <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → addr: 71 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 77 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 82 | <LoadConstString>: <Reg8: 0, string_id: 4888>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/catch-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/catch-block";
    // CODE → addr: 86 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/catch-block")
    // CODE → addr: 91 | <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 97 | <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r0 = console.log;
    // CODE → addr:102 | <Call2>: <Reg8: 0, Reg8: 0, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → addr:107 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:113 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:118 | <LoadConstString>: <Reg8: 0, string_id: 4889>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block";
    // CODE → addr:122 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block")
    // CODE → addr:127 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:133 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:138 | <LoadConstString>: <Reg8: 0, string_id: 11290>  # String: 'finally' (Identifier)
    // USED → r0 = "finally";
    // CODE → addr:142 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("finally")
    // CODE → addr:147 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:153 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:158 | <LoadConstString>: <Reg8: 0, string_id: 3600>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/end";
    // CODE → addr:162 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/end")
    // CODE → addr:167 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:169 | <Ret>: <Reg8: 0>
    return r0;
    // CODE → addr:171 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr:173 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:179 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:184 | <LoadConstString>: <Reg8: 2, string_id: 4889>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block";
    // CODE → addr:188 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block")
    // CODE → addr:193 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:199 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:204 | <LoadConstString>: <Reg8: 1, string_id: 11290>  # String: 'finally' (Identifier)
    // USED → r1 = "finally";
    // CODE → addr:208 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("finally")
    // CODE → addr:213 | <Throw>: <Reg8: 0>
    throw r0;
}