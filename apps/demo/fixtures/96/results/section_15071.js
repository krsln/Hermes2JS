function shortCircuitAssignTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4640>  # String: '__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 5>
    // USED → r1 = 5;
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log(5)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 10>
    // USED → r1 = 10;
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log(10)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 20>
    // USED → r1 = 20;
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log(20)
    // CODE → <NewObject>: <Reg8: 1>
    // USED → r1 = {  };
    // CODE → <GetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 7735>  # String: 'count' (Identifier)
    // USED → r3 = {  }.count;
    // CODE → <LoadConstNull>: <Reg8: 2>
    // USED → r2 = null;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 7735>  # String: 'count' (Identifier)
    {  }.count ??= 0
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 7735>  # String: 'count' (Identifier)
    // USED → r3 = {  }.count;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → <Add>: <Reg8: 2, Reg8: 3, Reg8: 2>
    // USED → r2 = {  }.count + 1;
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 7735>  # String: 'count' (Identifier)
    {  }.count = {  }.count + 1
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 3, string_id: 7735>  # String: 'count' (Identifier)
    // USED → r1 = {  }.count;
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log({  }.count)
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4636>  # String: '__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}