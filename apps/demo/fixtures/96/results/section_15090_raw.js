function switchInsideTryTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4684>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/start' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/start")
    // CODE → <Mov>: <Reg8: 2, Reg8: 0>
    r2 = param1
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <JStrictEqual>: <Addr8: 65, Reg8: 0, Reg8: 2>  # Address: 0000005f
    // → r2 = param1
    if (0 === r2) goto label_95;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → <JStrictEqual>: <Addr8: 26, Reg8: 0, Reg8: 2>  # Address: 0000003f
    if (1 === r2) goto label_63;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4678>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-default' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-default";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-default")
    // CODE → <Jmp>: <Addr8: 54>  # Address: 00000073
    goto label_115;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    r0 = Error.prototype
    // CODE → <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
    // USED → r2 = CreateThis(r0);
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 5270>  # String: 'case 1 throws' (String)
    // USED → r5 = "case 1 throws";
    // CODE → <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = CreateThis(r0);
    // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new Error("case 1 throws");
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = new Error("case 1 throws");
    // CODE → <Throw>: <Reg8: 0>
    throw new Error("case 1 throws");
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 2266>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-0' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-0";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-0")
    // ──────────────── Block 5 ──────────────── 
    // CODE → <Jmp>: <Addr8: 24>  # Address: 0000008b
    goto label_139;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4680>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/catch-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/catch-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/catch-block")
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4683>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4682>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
    // ──────────────── Block 8 ──────────────── 
    // CODE → <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4683>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block")
    // CODE → <Throw>: <Reg8: 0>
    throw caughtException;
}