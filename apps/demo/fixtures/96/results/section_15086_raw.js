function tryCatchFinallyBranchInFinallyTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 2, string_id: 4688>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block";
    // CODE → addr: 20 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block")
    // CODE → addr: 25 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → addr: 31 | <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r0 = Error.prototype;
    // CODE → addr: 36 | <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
    // USED → r2 = CreateThis(r0);
    // CODE → addr: 40 | <LoadConstString>: <Reg8: 5, string_id: 238>  # String: 'test' (Identifier)
    // USED → r5 = "test";
    // CODE → addr: 44 | <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThis(r0);
    // CODE → addr: 47 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new Error("test");
    // CODE → addr: 51 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    r0 = new Error("test")
    // CODE → addr: 55 | <Throw>: <Reg8: 0>
    throw r0;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 57 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr: 59 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr: 61 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 67 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 72 | <LoadConstString>: <Reg8: 0, string_id: 2167>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block";
    // CODE → addr: 76 | <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block")
    // CODE → addr: 81 | <Mov>: <Reg8: 0, Reg8: 1>
    // USED → r0 = param1;
    // CODE → addr: 84 | <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 90 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 95 | <JmpTrue>: <Addr8: 14, Reg8: 0>  # Address: 0000006d
    if (param1) goto label_109;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 98 | <LoadConstString>: <Reg8: 0, string_id: 4685>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false";
    // CODE → addr:102 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false")
    // CODE → addr:107 | <Jmp>: <Addr8: 11>  # Address: 00000076
    goto label_118;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr:109 | <LoadConstString>: <Reg8: 0, string_id: 4687>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true";
    // CODE → addr:113 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true")
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:118 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:120 | <Ret>: <Reg8: 0>
    return r0;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr:122 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr:124 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:126 | <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:132 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:137 | <JmpTrue>: <Addr8: 14, Reg8: 1>  # Address: 00000097
    if (param1) goto label_151;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:140 | <LoadConstString>: <Reg8: 1, string_id: 4685>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false";
    // CODE → addr:144 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false")
    // CODE → addr:149 | <Jmp>: <Addr8: 11>  # Address: 000000a0
    goto label_160;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:151 | <LoadConstString>: <Reg8: 1, string_id: 4687>  # String: '__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true";
    // CODE → addr:155 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true")
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:160 | <Throw>: <Reg8: 0>
    throw r0;
}