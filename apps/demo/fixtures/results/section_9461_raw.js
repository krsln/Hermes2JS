function shortCircuitAssignTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4816>  # String: '__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/start' (String)
    // USED → r3 = "__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/start")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 5>
    // USED → r0 = 5;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log(5)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 10>
    // USED → r0 = 10;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log(10)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 20>
    // USED → r0 = 20;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log(20)
    // CODE → <NewObject>: <Reg8: 3>
    r3 = {  }
    // CODE → <GetById>: <Reg8: 4, Reg8: 3, UInt8: 2, string_id: 7613>  # String: 'count' (Identifier)
    // USED → r4 = r3.count;
    // CODE → <LoadConstNull>: <Reg8: 1>
    // USED → r1 = null;
    // CODE → <JNotEqual>: <Addr8: 12, Reg8: 4, Reg8: 1>  # Address: 00000065
    if (r3.count != null) goto label_101;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <PutByIdStrict>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 7613>  # String: 'count' (Identifier)
    r3.count = 0
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetById>: <Reg8: 4, Reg8: 3, UInt8: 2, string_id: 7613>  # String: 'count' (Identifier)
    // USED → r4 = r3.count;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → <Add>: <Reg8: 4, Reg8: 4, Reg8: 0>
    // USED → r4 = r3.count + 1;
    // CODE → <PutByIdStrict>: <Reg8: 3, Reg8: 4, UInt8: 0, string_id: 7613>  # String: 'count' (Identifier)
    r3.count = r3.count + 1
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 2, string_id: 7613>  # String: 'count' (Identifier)
    // USED → r3 = r3.count;
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log(r3.count)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4813>  # String: '__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/end' (String)
    // USED → r2 = "__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}