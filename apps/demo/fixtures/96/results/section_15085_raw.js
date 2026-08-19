function tryCatchInsideLoopTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <Mov>: <Reg8: 7, Reg8: 2>
    // USED → r7 = param1;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4708>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start' (String)
    // USED → r3 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start")
    // CODE → <LoadConstZero>: <Reg8: 6>
    // USED → r6 = 0;
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <LoadConstZero>: <Reg8: 8>
    // USED → r8 = 0;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
    r2 = r2.length
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 2131>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught' (String)
    // USED → r5 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught";
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4701>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok' (String)
    // USED → r4 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok";
    // CODE → <JNotLessLong>: <Addr32: 128, Reg8: 6, Reg8: 2>  # Address: 000000b3
    // → r2 = r2.length
    if (!(0 < r2)) goto label_179;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Mov>: <Reg8: 3, Reg8: 7>
    // USED → r3 = param1;
    // CODE → <Mov>: <Reg8: 2, Reg8: 8>
    r2 = 0
    // CODE → <GetByVal>: <Reg8: 2, Reg8: 3, Reg8: 2>
    r2 = param1[r2]
    // CODE → <JLess>: <Addr8: 33, Reg8: 2, Reg8: 6>  # Address: 00000065
    // → r2 = param1[r2]
    if (r2 < 0) goto label_101;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 9, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <Mov>: <Reg8: 10, Reg8: 7>
    // USED → r10 = param1;
    // CODE → <Mov>: <Reg8: 2, Reg8: 8>
    r2 = 0
    // CODE → <GetByVal>: <Reg8: 2, Reg8: 10, Reg8: 2>
    // USED → r2 = param1[r2];
    // CODE → <Call3>: <Reg8: 2, Reg8: 3, Reg8: 9, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok", r2)
    // CODE → <Jmp>: <Addr8: 59>  # Address: 0000009e
    goto label_158;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 9, Reg8: 1, UInt8: 4, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r9 = Error;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 9, UInt8: 5, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r2 = Error.prototype;
    // CODE → <CreateThis>: <Reg8: 3, Reg8: 2, Reg8: 9>
    // USED → r3 = CreateThis(r2);
    // CODE → <LoadConstString>: <Reg8: 12, string_id: 839>  # String: 'negative value' (String)
    // USED → r12 = "negative value";
    // CODE → <Mov>: <Reg8: 13, Reg8: 3>
    // USED → r13 = CreateThis(r2);
    // CODE → <Construct>: <Reg8: 2, Reg8: 9, UInt8: 2>
    // USED → r2 = new Error("negative value");
    // CODE → <SelectObject>: <Reg8: 2, Reg8: 3, Reg8: 2>
    // USED → r2 = new Error("negative value");
    // CODE → <Throw>: <Reg8: 2>
    throw new Error("negative value");
    // ──────────────── Block 4 ──────────────── 
    // CODE → <Catch>: <Reg8: 9>
    // USED → r9 = caughtException;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 9>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught", r9)
    // CODE → <Mov>: <Reg8: 2, Reg8: 0>
    r2 = 0
    // CODE → <Inc>: <Reg8: 0, Reg8: 2>
    // USED → r0 = r2 + 1;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <Mov>: <Reg8: 2, Reg8: 8>
    r2 = 0
    // CODE → <Inc>: <Reg8: 3, Reg8: 2>
    // USED → r3 = r2 + 1;
    // CODE → <Mov>: <Reg8: 8, Reg8: 3>
    r8 = r2 + 1
    // CODE → <Mov>: <Reg8: 2, Reg8: 7>
    r2 = param1
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
    r2 = r2.length
    // CODE → <JLess>: <Addr8: -117, Reg8: 3, Reg8: 2>  # Address: 0000003a
    // → r2 = r2.length; r3 = r2 + 1
    if (r3 < r2) goto label_58;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4699>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return r2 + 1;
}