function nestedObjectDestructureTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 3, string_id: 4969>  # String: '__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start' (String)
    // USED → r3 = "__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start")
    // CODE → addr: 22 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1917, UInt16: 48463>  # Object: {'id': 1, 'name': 'Ada'}
    r3 = { "id": 1, "name": "Ada" }
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    // USED → r6 = r3.name;
    // CODE → addr: 33 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1918, UInt16: 93>  # Object: {'page': 1}
    r3 = { "page": 1 }
    // CODE → addr: 39 | <GetById>: <Reg8: 5, Reg8: 3, UInt8: 3, string_id: 12200>  # String: 'page' (Identifier)
    r5 = (r5 !== undefined) ? r3.page : 1
    // CODE → addr: 45 | <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 54 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 60 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 65 | <LoadConstUInt8>: <Reg8: 0, UInt8: 200>
    // USED → r0 = 200;
    // CODE → addr: 68 | <Call4>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 6, Reg8: 5>
    console.log(200, r3.name, (r5 !== undefined) ? r3.page : 1)
    // CODE → addr: 75 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 81 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 86 | <LoadConstString>: <Reg8: 2, string_id: 4968>  # String: '__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end' (String)
    // USED → r2 = "__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end";
    // CODE → addr: 90 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end")
    // CODE → addr: 95 | <Ret>: <Reg8: 1>
    return undefined;
}