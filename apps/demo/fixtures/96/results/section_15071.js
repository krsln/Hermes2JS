function computedPropertyTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4608>  # String: '__BC:Objects/PropertyTests/computedPropertyTest/start' (String)
    // USED → r1 = "__BC:Objects/PropertyTests/computedPropertyTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Objects/PropertyTests/computedPropertyTest/start")
    // CODE → <NewObject>: <Reg8: 3>
    // USED → r3 = {  };
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 42>
    r2 = 42
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 8779>  # String: 'dynamic' (Identifier)
    r1 = "dynamic"
    // CODE → <PutOwnByVal>: <Reg8: 3, Reg8: 2, Reg8: 1, UInt8: 1>
    // Unhandled opcode: PutOwnByVal
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 206>  # String: 'value' (Identifier)
    r2 = "value"
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 3784>  # String: 'staticKey' (String)
    r1 = "staticKey"
    // CODE → <PutOwnByVal>: <Reg8: 3, Reg8: 2, Reg8: 1, UInt8: 1>
    // Unhandled opcode: PutOwnByVal
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    r1 = globalThis.console.log({  })
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4604>  # String: '__BC:Objects/PropertyTests/computedPropertyTest/end' (String)
    // USED → r0 = "__BC:Objects/PropertyTests/computedPropertyTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:Objects/PropertyTests/computedPropertyTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}