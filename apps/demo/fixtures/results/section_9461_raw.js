function shortCircuitAssignTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 3, string_id: 4816>  # String: '__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/start' (String)
    // USED → r3 = "__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 33 | <LoadConstUInt8>: <Reg8: 0, UInt8: 5>
    // USED → r0 = 5;
    // CODE → addr: 36 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log(5)
    // CODE → addr: 41 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 47 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 52 | <LoadConstUInt8>: <Reg8: 0, UInt8: 10>
    // USED → r0 = 10;
    // CODE → addr: 55 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log(10)
    // CODE → addr: 60 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 66 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 71 | <LoadConstUInt8>: <Reg8: 0, UInt8: 20>
    // USED → r0 = 20;
    // CODE → addr: 74 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log(20)
    // CODE → addr: 79 | <NewObject>: <Reg8: 3>
    r3 = {  }
    // CODE → addr: 81 | <GetById>: <Reg8: 4, Reg8: 3, UInt8: 2, string_id: 7613>  # String: 'count' (Identifier)
    r4 = r3.count
    // CODE → addr: 87 | <LoadConstNull>: <Reg8: 1>
    // USED → r1 = null;
    // CODE → addr: 89 | <JNotEqual>: <Addr8: 12, Reg8: 4, Reg8: 1>  # Address: 00000065
    // → r4 = r3.count
    if (r4 != null) goto label_101;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 93 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr: 95 | <PutByIdStrict>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 7613>  # String: 'count' (Identifier)
    r3.count = 0
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr:101 | <GetById>: <Reg8: 4, Reg8: 3, UInt8: 2, string_id: 7613>  # String: 'count' (Identifier)
    // USED → r4 = r3.count;
    // CODE → addr:107 | <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → addr:110 | <Add>: <Reg8: 4, Reg8: 4, Reg8: 0>
    // USED → r4 = r3.count + 1;
    // CODE → addr:114 | <PutByIdStrict>: <Reg8: 3, Reg8: 4, UInt8: 0, string_id: 7613>  # String: 'count' (Identifier)
    r3.count = r3.count + 1
    // CODE → addr:120 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:126 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:131 | <GetById>: <Reg8: 3, Reg8: 3, UInt8: 2, string_id: 7613>  # String: 'count' (Identifier)
    // USED → r3 = r3.count;
    // CODE → addr:137 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log(r3.count)
    // CODE → addr:142 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:148 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:153 | <LoadConstString>: <Reg8: 2, string_id: 4813>  # String: '__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/end' (String)
    // USED → r2 = "__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/end";
    // CODE → addr:157 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/end")
    // CODE → addr:162 | <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → addr:164 | <Ret>: <Reg8: 1>
    return undefined;
}