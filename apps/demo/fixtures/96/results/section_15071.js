function shortCircuitAssignTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4640>  # String: '__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 33 | <LoadConstUInt8>: <Reg8: 1, UInt8: 5>
    // USED → r1 = 5;
    // CODE → addr: 36 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(5)
    // CODE → addr: 41 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 47 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 52 | <LoadConstUInt8>: <Reg8: 1, UInt8: 10>
    // USED → r1 = 10;
    // CODE → addr: 55 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(10)
    // CODE → addr: 60 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 66 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 71 | <LoadConstUInt8>: <Reg8: 1, UInt8: 20>
    // USED → r1 = 20;
    // CODE → addr: 74 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(20)
    // CODE → addr: 79 | <NewObject>: <Reg8: 1>
    r1 = {  }
    // CODE → addr: 81 | <GetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 7735>  # String: 'count' (Identifier)
    // USED → r3 = r1.count;
    // CODE → addr: 87 | <LoadConstNull>: <Reg8: 2>
    // USED → r2 = null;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 93 | <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    // CODE → addr: 95 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 7735>  # String: 'count' (Identifier)
    r1.count ??= 0
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr:101 | <GetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 7735>  # String: 'count' (Identifier)
    // USED → r3 = r1.count;
    // CODE → addr:107 | <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → addr:110 | <Add>: <Reg8: 2, Reg8: 3, Reg8: 2>
    // USED → r2 = r1.count + 1;
    // CODE → addr:114 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 7735>  # String: 'count' (Identifier)
    r1.count = r1.count + 1
    // CODE → addr:120 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:126 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:131 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 3, string_id: 7735>  # String: 'count' (Identifier)
    // USED → r1 = r1.count;
    // CODE → addr:137 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1.count)
    // CODE → addr:142 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:148 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:153 | <LoadConstString>: <Reg8: 0, string_id: 4636>  # String: '__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/end";
    // CODE → addr:157 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/end")
    // CODE → addr:162 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:164 | <Ret>: <Reg8: 0>
    return undefined;
}