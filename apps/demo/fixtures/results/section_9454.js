function optionalChainingTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4779>  # String: '__BC:Objects/PropertyTests/optionalChainingTest/start' (String)
    // USED → r5 = "__BC:Objects/PropertyTests/optionalChainingTest/start";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    // USED → r5 = globalThis.console.log("__BC:Objects/PropertyTests/optionalChainingTest/start");
    // CODE → <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1916, UInt16: 20>  # Object: {'b': null}
    // Error: NewObjectWithBuffer at address 22: Invalid arguments: Reg8: 5, UInt16: 1916, UInt16: 20
    // CODE → <NewObject>: <Reg8: 6>
    // USED → r6 = {  };
    // CODE → <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 6, UInt8: 0>
    globalThis.console.log("__BC:Objects/PropertyTests/optionalChainingTest/start").slot_0 = {  }
    // CODE → <LoadConstNull>: <Reg8: 1>
    // USED → r1 = null;
    // CODE → <Eq>: <Reg8: 3, Reg8: 5, Reg8: 1>
    // USED → r3 = globalThis.console.log("__BC:Objects/PropertyTests/optionalChainingTest/start") == null;
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    if (globalThis.console.log("__BC:Objects/PropertyTests/optionalChainingTest/start") != null) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 2, string_id: 34>  # String: 'b' (Identifier)
        // USED → r5 = globalThis.console.log("__BC:Objects/PropertyTests/optionalChainingTest/start").b;
        // CODE → <Eq>: <Reg8: 3, Reg8: 5, Reg8: 1>
        // USED → r3 = globalThis.console.log("__BC:Objects/PropertyTests/optionalChainingTest/start").b == null;
        // CODE → <LoadConstUndefined>: <Reg8: 7>
        r7 = undefined
        if (globalThis.console.log("__BC:Objects/PropertyTests/optionalChainingTest/start").b != null) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <GetById>: <Reg8: 7, Reg8: 5, UInt8: 3, string_id: 6345>  # String: 'c' (Identifier)
            // USED → r7 = globalThis.console.log("__BC:Objects/PropertyTests/optionalChainingTest/start").b.c;
        }
    }
    if (globalThis.console.log("__BC:Objects/PropertyTests/optionalChainingTest/start").b.c == null) {
        // ──────────────── Block 4 ──────────────── 
        // CODE → <LoadConstInt>: <Reg8: 7, Imm32: -1>
        // USED → r7 = -1;
    }
    // ──────────────── Block 5 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
    r5 = globalThis.console.log(-1)
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4778>  # String: '__BC:Objects/PropertyTests/optionalChainingTest/end' (String)
    // USED → r4 = "__BC:Objects/PropertyTests/optionalChainingTest/end";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    r4 = globalThis.console.log("__BC:Objects/PropertyTests/optionalChainingTest/end")
    // CODE → <Ret>: <Reg8: 2>
    return undefined;
}