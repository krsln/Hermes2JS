function computedPropertyTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4829>  # String: '__BC:Objects/PropertyTests/computedPropertyTest/start' (String)
    // USED → r1 = "__BC:Objects/PropertyTests/computedPropertyTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/PropertyTests/computedPropertyTest/start")
    // CODE → addr: 22 | <NewObject>: <Reg8: 3>
    // USED → r3 = {  };
    // CODE → addr: 24 | <LoadConstUInt8>: <Reg8: 2, UInt8: 42>
    // USED → r2 = 42;
    // CODE → addr: 27 | <LoadConstString>: <Reg8: 1, string_id: 8980>  # String: 'dynamic' (Identifier)
    // USED → r1 = "dynamic";
    // CODE → addr: 31 | <PutOwnByVal>: <Reg8: 3, Reg8: 2, Reg8: 1, UInt8: 1>
    r3["dynamic"] = 42
    // CODE → addr: 36 | <LoadConstString>: <Reg8: 2, string_id: 205>  # String: 'value' (Identifier)
    // USED → r2 = "value";
    // CODE → addr: 40 | <LoadConstString>: <Reg8: 1, string_id: 2363>  # String: 'staticKey' (String)
    // USED → r1 = "staticKey";
    // CODE → addr: 44 | <PutOwnByVal>: <Reg8: 3, Reg8: 2, Reg8: 1, UInt8: 1>
    r3["staticKey"] = "value"
    // CODE → addr: 49 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 55 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 60 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → addr: 65 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 71 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 76 | <LoadConstString>: <Reg8: 0, string_id: 4828>  # String: '__BC:Objects/PropertyTests/computedPropertyTest/end' (String)
    // USED → r0 = "__BC:Objects/PropertyTests/computedPropertyTest/end";
    // CODE → addr: 80 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Objects/PropertyTests/computedPropertyTest/end")
    // CODE → addr: 85 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr: 87 | <Ret>: <Reg8: 0>
    return r0;
}