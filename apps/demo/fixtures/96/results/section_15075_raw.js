function tryCatchTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4731>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4732>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/try-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/try-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/try-block")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r3 = globalThis.Error;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    r0 = globalThis.Error.prototype
    // CODE → <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
    // USED → r2 = CreateThis(r0);
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 238>  # String: 'test' (Identifier)
    // USED → r5 = "test";
    // CODE → <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThis(r0);
    // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new globalThis.Error("test");
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = new globalThis.Error("test");
    // CODE → <Throw>: <Reg8: 0>
    throw new globalThis.Error("test");
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4724>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/catch-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/catch-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/catch-block")
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r0 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 0, Reg8: 0, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4730>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 10984>  # String: 'finally' (Identifier)
    // USED → r0 = "finally";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("finally")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4728>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4730>  # String: '__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 10984>  # String: 'finally' (Identifier)
    // USED → r1 = "finally";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("finally")
    // CODE → <Throw>: <Reg8: 0>
    throw caughtException;
}