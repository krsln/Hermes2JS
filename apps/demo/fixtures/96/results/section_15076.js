function tryCatchNoFinallyTest(param0) {
    try {
        // ──────────────── Block 0 ──────────────── 
        // CODE → <GetGlobalObject>: <Reg8: 0>
        // USED → r0 = globalThis;
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4713>  # String: '__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/start' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/start";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/start")
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4718>  # String: '__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/try-block' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/try-block";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/try-block")
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
        // USED → r3 = globalThis.Error;
        // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
        r1 = globalThis.Error.prototype
        // CODE → <CreateThis>: <Reg8: 2, Reg8: 1, Reg8: 3>
        // USED → r2 = CreateThis(r1);
        // CODE → <LoadConstString>: <Reg8: 5, string_id: 6728>  # String: 'no finally here' (String)
        // USED → r5 = "no finally here";
        // CODE → <Mov>: <Reg8: 6, Reg8: 2>
        // USED → r6 = CreateThis(r1);
        // CODE → <Construct>: <Reg8: 1, Reg8: 3, UInt8: 2>
        // USED → r1 = new globalThis.Error("no finally here");
        // CODE → <SelectObject>: <Reg8: 1, Reg8: 2, Reg8: 1>
        // USED → r1 = new globalThis.Error("no finally here");
        // CODE → <Throw>: <Reg8: 1>
        throw new globalThis.Error("no finally here");
    } catch (caughtException) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4709>  # String: '__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/catch-block' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/catch-block";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/catch-block")
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
        // CODE → <LoadConstString>: <Reg8: 0, string_id: 4710>  # String: '__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/end' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/end";
        // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/end")
        // CODE → <LoadConstUndefined>: <Reg8: 0>
        // USED → r0 = undefined;
        // CODE → <Ret>: <Reg8: 0>
        return undefined;
    }
}