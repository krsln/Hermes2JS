function nestedTryCatchTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 1851>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/start' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4677>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-try' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-try";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-try")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4672>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-try' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-try";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-try")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r3 = globalThis.Error;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    r1 = globalThis.Error.prototype
    // CODE → <CreateThis>: <Reg8: 2, Reg8: 1, Reg8: 3>
    // USED → r2 = CreateThis(r1);
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 7723>  # String: 'inner' (Identifier)
    // USED → r5 = "inner";
    // CODE → <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThis(r1);
    // CODE → <Construct>: <Reg8: 1, Reg8: 3, UInt8: 2>
    // USED → r1 = new globalThis.Error("inner");
    // CODE → <SelectObject>: <Reg8: 1, Reg8: 2, Reg8: 1>
    // USED → r1 = new globalThis.Error("inner");
    // CODE → <Throw>: <Reg8: 1>
    throw new globalThis.Error("inner");
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4670>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-catch' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-catch";
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-catch")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r3 = globalThis.Error;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 6991>  # String: 'rethrown from inner: ' (String)
    // USED → r1 = "rethrown from inner: ";
    // CODE → <Add>: <Reg8: 5, Reg8: 1, Reg8: 2>
    r5 = "rethrown from inner: " + caughtException
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r2 = globalThis.Error.prototype;
    // CODE → <CreateThis>: <Reg8: 2, Reg8: 2, Reg8: 3>
    // USED → r2 = CreateThis(r2);
    // CODE → <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThis(r2);
    // CODE → <Construct>: <Reg8: 1, Reg8: 3, UInt8: 2>
    // USED → r1 = new globalThis.Error(globalThis.Error.prototype);
    // CODE → <SelectObject>: <Reg8: 1, Reg8: 2, Reg8: 1>
    // USED → r1 = new globalThis.Error(globalThis.Error.prototype);
    // CODE → <Throw>: <Reg8: 1>
    throw new globalThis.Error(globalThis.Error.prototype);
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4675>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-catch' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-catch";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-catch")
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4667>  # String: '__BC:Exceptions/ExceptionTests/nestedTryCatchTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/nestedTryCatchTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}