function renamedDefaultDestructureTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4980>  # String: '__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start' (String)
    // USED → r3 = "__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start")
    // CODE → <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1919, UInt16: 19946>  # Object: {'timeout': 500}
    r3 = { "timeout": 500 }
    // CODE → <GetById>: <Reg8: 6, Reg8: 3, UInt8: 2, string_id: 8581>  # String: 'timeout' (Identifier)
    // USED → r6 = (r6 !== undefined) ? r3.timeout : 1000;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetById>: <Reg8: 5, Reg8: 3, UInt8: 3, string_id: 9071>  # String: 'retries' (Identifier)
    // USED → r5 = (r5 !== undefined) ? r3.retries : 3;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 6, Reg8: 5>
    console.log(r6, r5)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4979>  # String: '__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end' (String)
    // USED → r2 = "__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end")
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}