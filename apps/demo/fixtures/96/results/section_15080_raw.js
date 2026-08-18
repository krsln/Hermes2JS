function tryLoopMultiReturnTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4748>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start")
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    // CODE → <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4747>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive";
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Mov>: <Reg8: 6, Reg8: 4>
    r6 = 0
    // CODE → <Mov>: <Reg8: 5, Reg8: 3>
    r5 = param1
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
    r5 = r5.length
    // CODE → <JGreaterEqual>: <Addr8: 76, Reg8: 6, Reg8: 5>  # Address: 0000007a
    // → r5 = r5.length; r6 = 0
    if (r6 >= r5) goto label_122;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Mov>: <Reg8: 6, Reg8: 3>
    // USED → r6 = param1;
    // CODE → <Mov>: <Reg8: 5, Reg8: 4>
    r5 = 0
    // CODE → <GetByVal>: <Reg8: 5, Reg8: 6, Reg8: 5>
    r5 = param1[r5]
    // CODE → <JLess>: <Addr8: 58, Reg8: 5, Reg8: 2>  # Address: 00000076
    // → r5 = param1[r5]
    if (r5 < 0) goto label_118;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <Mov>: <Reg8: 6, Reg8: 3>
    // USED → r6 = param1;
    // CODE → <Mov>: <Reg8: 5, Reg8: 4>
    r5 = 0
    // CODE → <GetByVal>: <Reg8: 5, Reg8: 6, Reg8: 5>
    r5 = param1[r5]
    // CODE → <JStrictEqual>: <Addr8: 36, Reg8: 5, Reg8: 2>  # Address: 0000006e
    // → r5 = param1[r5]
    if (r5 === 0) goto label_110;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → <Mov>: <Reg8: 6, Reg8: 3>
    // USED → r6 = param1;
    // CODE → <Mov>: <Reg8: 5, Reg8: 4>
    r5 = 0
    // CODE → <GetByVal>: <Reg8: 6, Reg8: 6, Reg8: 5>
    // USED → r6 = param1[r5];
    // CODE → <Call3>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 6>
    console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive", r6)
    // CODE → <Inc>: <Reg8: 4, Reg8: 5>
    // USED → r4 = r5 + 1;
    // CODE → <Jmp>: <Addr8: -73>  # Address: 00000023
    goto label_35;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <Mov>: <Reg8: 5, Reg8: 4>
    r5 = r5 + 1
    // CODE → <Inc>: <Reg8: 4, Reg8: 5>
    r4 = r5 + 1
    // CODE → <Jmp>: <Addr8: -81>  # Address: 00000023
    goto label_35;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <LoadConstTrue>: <Reg8: 1>
    // USED → r1 = true;
    // CODE → <Ret>: <Reg8: 1>
    return true;
    // ──────────────── Block 7 ──────────────── 
    // CODE → <LoadConstFalse>: <Reg8: 1>
    // USED → r1 = false;
    // CODE → <Ret>: <Reg8: 1>
    return false;
    // ──────────────── Block 8 ──────────────── 
    // CODE → <Catch>: <Reg8: 1>
    r1 = caughtException
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 3905>  # String: '__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block")
    // CODE → <LoadConstFalse>: <Reg8: 0>
    // USED → r0 = false;
    // CODE → <Ret>: <Reg8: 0>
    return false;
}