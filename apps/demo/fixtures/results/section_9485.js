function nestedObjectDestructureTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4969>  # String: '__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start' (String)
    // USED → r3 = "__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start")
    // CODE → <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1917, UInt16: 48463>  # Object: {'id': 1, 'name': 'Ada'}
    r3 = { "id": 1, "name": "Ada" }
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    // USED → r6 = r3.name;
    // CODE → <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1918, UInt16: 93>  # Object: {'page': 1}
    r3 = { "page": 1 }
    // CODE → <GetById>: <Reg8: 5, Reg8: 3, UInt8: 3, string_id: 12200>  # String: 'page' (Identifier)
    // USED → r5 = (r3.page !== undefined) ? r3.page : 1;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 200>
    // USED → r0 = 200;
    // CODE → <Call4>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 6, Reg8: 5>
    r3 = globalThis.console.log(200, r3.name, (r3.page !== undefined) ? r3.page : 1)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4968>  # String: '__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end' (String)
    // USED → r2 = "__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end")
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}