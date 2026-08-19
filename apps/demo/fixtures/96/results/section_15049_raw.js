function doWhileTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4577>  # String: '__BC:ControlFlow/DoWhileTests/doWhileTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/DoWhileTests/doWhileTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/DoWhileTests/doWhileTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 1, UInt8: 5>
    // USED → r1 = 5;
    // CODE → addr: 25 | <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 27 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 33 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 38 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr: 43 | <Inc>: <Reg8: 2, Reg8: 2>
    r2 = r2 + 1
    // CODE → addr: 46 | <JLess>: <Addr8: -19, Reg8: 2, Reg8: 1>  # Address: 0000001b
    // → r2 = r2 + 1
    if (r2 < 5) goto label_27;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 50 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 56 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 61 | <LoadConstString>: <Reg8: 0, string_id: 4574>  # String: '__BC:ControlFlow/DoWhileTests/doWhileTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/DoWhileTests/doWhileTest/end";
    // CODE → addr: 65 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/DoWhileTests/doWhileTest/end")
    // CODE → addr: 70 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 72 | <Ret>: <Reg8: 0>
    return undefined;
}