function switchInsideTryTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4124>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/start")
    // CODE → addr: 22 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr: 25 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr: 27 | <JStrictEqual>: <Addr8: 60, Reg8: 0, Reg8: 2>  # Address: 00000057
    if (0 === param1) goto label_87;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 31 | <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → addr: 34 | <JStrictEqual>: <Addr8: 26, Reg8: 0, Reg8: 2>  # Address: 0000003c
    if (1 === param1) goto label_60;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 38 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 44 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 49 | <LoadConstString>: <Reg8: 0, string_id: 4853>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-default' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-default";
    // CODE → addr: 53 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-default")
    // CODE → addr: 58 | <Jmp>: <Addr8: 49>  # Address: 0000006b
    goto label_107;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 60 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → addr: 66 | <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = CreateThisForNew(r3);
    // CODE → addr: 70 | <LoadConstString>: <Reg8: 4, string_id: 5232>  # String: 'case 1 throws' (String)
    // USED → r4 = "case 1 throws";
    // CODE → addr: 74 | <Mov>: <Reg8: 5, Reg8: 2>
    // USED → r5 = CreateThisForNew(r3);
    // CODE → addr: 77 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new Error("case 1 throws");
    // CODE → addr: 81 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    r0 = new Error("case 1 throws")
    // CODE → addr: 85 | <Throw>: <Reg8: 0>
    throw r0;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 87 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 93 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 98 | <LoadConstString>: <Reg8: 0, string_id: 4852>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-0' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-0";
    // CODE → addr:102 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-0")
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr:107 | <Jmp>: <Addr8: 24>  # Address: 00000083
    goto label_131;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:109 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr:111 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:117 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:122 | <LoadConstString>: <Reg8: 0, string_id: 3688>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/catch-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/catch-block";
    // CODE → addr:126 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/catch-block")
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:131 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:137 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:142 | <LoadConstString>: <Reg8: 0, string_id: 4857>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block";
    // CODE → addr:146 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block")
    // CODE → addr:151 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:157 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:162 | <LoadConstString>: <Reg8: 0, string_id: 4855>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/end";
    // CODE → addr:166 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/end")
    // CODE → addr:171 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:173 | <Ret>: <Reg8: 0>
    return r0;
    // CODE → addr:175 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr:177 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:183 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:188 | <LoadConstString>: <Reg8: 1, string_id: 4857>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block";
    // CODE → addr:192 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block")
    // CODE → addr:197 | <Throw>: <Reg8: 0>
    throw r0;
}