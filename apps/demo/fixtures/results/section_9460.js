function ternaryTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4818>  # String: '__BC:ControlFlow/TernaryTests/ternaryTest/start' (String)
    // USED → r2 = "__BC:ControlFlow/TernaryTests/ternaryTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 2>
    console.log("__BC:ControlFlow/TernaryTests/ternaryTest/start")
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    // CODE → <Greater>: <Reg8: 0, Reg8: 3, Reg8: 2>
    // USED → r0 = param1 > 0;
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 2001>  # String: 'positive' (String)
    r6 = (param1 > 0) ? "positive" : (param1 >= 0) ? "zero" : "negative"
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 6>
    console.log(r6)
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 100>
    // USED → r4 = (param1 > 100) ? 100 : (param1 < 0) ? 0 : param1;
    // CODE → <Greater>: <Reg8: 0, Reg8: 3, Reg8: 4>
    // USED → r0 = param1 > 100;
    // ──────────────── Block 8 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4817>  # String: '__BC:ControlFlow/TernaryTests/ternaryTest/end' (String)
    // USED → r1 = "__BC:ControlFlow/TernaryTests/ternaryTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/TernaryTests/ternaryTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}