function tryCatchFinallyBranchInFinallyTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4862>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = globalThis.Error;
    // CODE → <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = __uninitialized_this_for_new__r3;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 47>  # String: 'test' (Identifier)
    // USED → r5 = "test";
    // CODE → <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = __uninitialized_this_for_new__r3;
    // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new globalThis.Error("test", __uninitialized_this_for_new__r3);
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = new globalThis.Error("test", __uninitialized_this_for_new__r3);
    // CODE → <Throw>: <Reg8: 0>
    throw new globalThis.Error("test", __uninitialized_this_for_new__r3);
    // CODE → <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 2163>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <JmpTrue>: <Addr8: 14, Reg8: 1>  # Address: 00000065
    if (param1) goto label_101;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4858>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false")
    // CODE → <Jmp>: <Addr8: 11>  # Address: 0000006e
    goto label_110;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4861>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true")
    // ──────────────── Block 3 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
    // CODE → <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <JmpTrue>: <Addr8: 14, Reg8: 1>  # Address: 0000008f
    if (param1) goto label_143;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4858>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false")
    // CODE → <Jmp>: <Addr8: 11>  # Address: 00000098
    goto label_152;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4861>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true")
    // ──────────────── Block 6 ──────────────── 
    // CODE → <Throw>: <Reg8: 0>
    throw caughtException;
}