function tryFinallyLoopBreakTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4895>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/start' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/start")
    // CODE → <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED → r6 = param1;
    // CODE → <LoadConstZero>: <Reg8: 5>
    // USED → r5 = 0;
    // CODE → <LoadConstZero>: <Reg8: 7>
    // USED → r7 = 0;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 6, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
    // USED → r2 = r6.length;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4894>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/item' (String)
    // USED → r4 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/item";
    // CODE → <JNotLess>: <Addr8: 54, Reg8: 5, Reg8: 2>  # Address: 00000060
    // → r2 = r6.length
    if (!(0 < r2)) goto label_96;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 0
    // CODE → <GetByVal>: <Reg8: 2, Reg8: 6, Reg8: 2>
    // USED → r2 = param1[r2];
    // CODE → <JStrictEqual>: <Addr8: 43, Reg8: 2, Reg8: 5>  # Address: 00000060
    // → r2 = param1[r2]
    if (r2 === 0) goto label_96;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 9, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 0
    // CODE → <GetByVal>: <Reg8: 3, Reg8: 6, Reg8: 2>
    // USED → r3 = param1[r2];
    // CODE → <Call3>: <Reg8: 3, Reg8: 8, Reg8: 9, Reg8: 4, Reg8: 3>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/item", r3)
    // CODE → <Inc>: <Reg8: 3, Reg8: 2>
    // USED → r3 = r2 + 1;
    // CODE → <Mov>: <Reg8: 7, Reg8: 3>
    r7 = r2 + 1
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 6, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
    // USED → r2 = r6.length;
    // CODE → <JLess>: <Addr8: -46, Reg8: 3, Reg8: 2>  # Address: 0000002e
    // → r2 = r6.length; r3 = r2 + 1
    if (r3 < r2) goto label_46;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4893>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4892>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/end' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
    // CODE → <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4893>  # String: '__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block")
    // CODE → <Throw>: <Reg8: 0>
    throw caughtException;
}