function tryLoopMultiReturnTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 3, UInt8: 1>
    r3 = param1
    // CODE → addr:  3 | <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → addr:  5 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  7 | <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 13 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 18 | <LoadConstString>: <Reg8: 1, string_id: 4906>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start";
    // CODE → addr: 22 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start")
    // CODE → addr: 27 | <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    // CODE → addr: 29 | <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0;
    // CODE → addr: 31 | <LoadConstString>: <Reg8: 1, string_id: 4272>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive";
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 35 | <Mov>: <Reg8: 6, Reg8: 4>
    r6 = 0
    // CODE → addr: 38 | <GetByIdShort>: <Reg8: 5, Reg8: 3, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
    r5 = r3.length
    // CODE → addr: 43 | <JGreaterEqual>: <Addr8: 67, Reg8: 6, Reg8: 5>  # Address: 0000006e
    // → r5 = r3.length; r6 = 0
    if (r6 >= r5) goto label_110;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 47 | <Mov>: <Reg8: 5, Reg8: 4>
    r5 = 0
    // CODE → addr: 50 | <GetByVal>: <Reg8: 5, Reg8: 3, Reg8: 5>
    r5 = param1[r5]
    // CODE → addr: 54 | <JLess>: <Addr8: 52, Reg8: 5, Reg8: 2>  # Address: 0000006a
    // → r5 = param1[r5]
    if (r5 < 0) goto label_106;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 58 | <Mov>: <Reg8: 5, Reg8: 4>
    r5 = 0
    // CODE → addr: 61 | <GetByVal>: <Reg8: 5, Reg8: 3, Reg8: 5>
    r5 = param1[r5]
    // CODE → addr: 65 | <JStrictEqual>: <Addr8: 33, Reg8: 5, Reg8: 2>  # Address: 00000062
    // → r5 = param1[r5]
    if (r5 === 0) goto label_98;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 69 | <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr: 75 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr: 80 | <Mov>: <Reg8: 5, Reg8: 4>
    r5 = 0
    // CODE → addr: 83 | <GetByVal>: <Reg8: 6, Reg8: 3, Reg8: 5>
    // USED → r6 = param1[r5];
    // CODE → addr: 87 | <Call3>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 6>
    console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive", r6)
    // CODE → addr: 93 | <Inc>: <Reg8: 4, Reg8: 5>
    // USED → r4 = r5 + 1;
    // CODE → addr: 96 | <Jmp>: <Addr8: -61>  # Address: 00000023
    goto label_35;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 98 | <Mov>: <Reg8: 5, Reg8: 4>
    r5 = r5 + 1
    // CODE → addr:101 | <Inc>: <Reg8: 4, Reg8: 5>
    r4 = r5 + 1
    // CODE → addr:104 | <Jmp>: <Addr8: -69>  # Address: 00000023
    goto label_35;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:106 | <LoadConstTrue>: <Reg8: 1>
    r1 = true
    // CODE → addr:108 | <Ret>: <Reg8: 1>
    return r1;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:110 | <LoadConstFalse>: <Reg8: 1>
    r1 = false
    // CODE → addr:112 | <Ret>: <Reg8: 1>
    return r1;
    // CODE → addr:114 | <Catch>: <Reg8: 1>
    r1 = caughtException
    // CODE → addr:116 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:122 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:127 | <LoadConstString>: <Reg8: 0, string_id: 4905>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block";
    // CODE → addr:131 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block")
    // CODE → addr:136 | <LoadConstFalse>: <Reg8: 0>
    r0 = false
    // CODE → addr:138 | <Ret>: <Reg8: 0>
    return r0;
}