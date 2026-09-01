function optionalChainingTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4837>  # String: '__BC:Objects/PropertyTests/optionalChainingTest/start' (String)
    // USED → r0 = "__BC:Objects/PropertyTests/optionalChainingTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Objects/PropertyTests/optionalChainingTest/start")
    // CODE → addr: 22 | <NewObject>: <Reg8: 3>
    r3 = {  }
    // CODE → addr: 24 | <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → addr: 26 | <NewObject>: <Reg8: 2>
    r2 = {  }
    // CODE → addr: 28 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 2, string_id: 38>  # String: 'b' (Identifier)
    r0.b = r2
    // CODE → addr: 32 | <PutNewOwnById>: <Reg8: 3, Reg8: 0, string_id: 7189>  # String: 'a' (Identifier)
    r3.a = r0
    // CODE → addr: 37 | <LoadConstNull>: <Reg8: 2>
    // USED → r2 = null;
    // CODE → addr: 39 | <Eq>: <Reg8: 5, Reg8: 3, Reg8: 2>
    // USED → r5 = r3 == null;
    // CODE → addr: 43 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 45 | <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // → r3 = {  }
    if (r3 != null) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 50 | <GetById>: <Reg8: 3, Reg8: 3, UInt8: 3, string_id: 7189>  # String: 'a' (Identifier)
        // USED → r3 = r3.a;
        // CODE → addr: 56 | <Eq>: <Reg8: 5, Reg8: 3, Reg8: 2>
        // USED → r5 = r3.a == null;
        // CODE → addr: 60 | <LoadConstUndefined>: <Reg8: 4>
        r4 = undefined
        // → r3 = r3.a
        if (r3.a != null) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 65 | <GetByIdShort>: <Reg8: 3, Reg8: 3, UInt8: 4, string_id: 38>  # String: 'b' (Identifier)
            // USED → r3 = r3.b;
            // CODE → addr: 70 | <Eq>: <Reg8: 5, Reg8: 3, Reg8: 2>
            // USED → r5 = r3.b == null;
            // CODE → addr: 74 | <LoadConstUndefined>: <Reg8: 4>
            r4 = undefined
            // → r3 = r3.b
            if (r3.b != null) {
                // ──────────────── Block 3 ──────────────── 
                // CODE → addr: 79 | <GetById>: <Reg8: 4, Reg8: 3, UInt8: 5, string_id: 7241>  # String: 'c' (Identifier)
                r4 = r3.c
            }
        }
    }
    if (r4 == null) {
        // ──────────────── Block 5 ──────────────── 
        // CODE → addr: 89 | <LoadConstInt>: <Reg8: 4, Imm32: -1>
        r4 = -1
    }
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 95 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:101 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:106 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → addr:111 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:117 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:122 | <LoadConstString>: <Reg8: 1, string_id: 4830>  # String: '__BC:Objects/PropertyTests/optionalChainingTest/end' (String)
    // USED → r1 = "__BC:Objects/PropertyTests/optionalChainingTest/end";
    // CODE → addr:126 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/PropertyTests/optionalChainingTest/end")
    // CODE → addr:131 | <Ret>: <Reg8: 0>
    return undefined;
}