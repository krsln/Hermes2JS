function computedPropertyTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 2, string_id: 4993>  # String: '__BC:Objects/PropertyTests/computedPropertyTest/start' (String)
    // USED → r2 = "__BC:Objects/PropertyTests/computedPropertyTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Objects/PropertyTests/computedPropertyTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 33 | <NewObjectWithBuffer>: <Reg8: 2, UInt16: 1915, UInt16: 46772>  # Object: {'dynamic': 42, 'staticKey': 'value'}
    r2 = { "dynamic": 42, "staticKey": "value" }
    // CODE → addr: 39 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr: 44 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 50 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 55 | <LoadConstString>: <Reg8: 1, string_id: 4992>  # String: '__BC:Objects/PropertyTests/computedPropertyTest/end' (String)
    // USED → r1 = "__BC:Objects/PropertyTests/computedPropertyTest/end";
    // CODE → addr: 59 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/PropertyTests/computedPropertyTest/end")
    // CODE → addr: 64 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 66 | <Ret>: <Reg8: 0>
    return undefined;
}