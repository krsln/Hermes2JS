function optionalChainingTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 5, string_id: 4995>  # String: '__BC:Objects/PropertyTests/optionalChainingTest/start' (String)
    // USED → r5 = "__BC:Objects/PropertyTests/optionalChainingTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/PropertyTests/optionalChainingTest/start")
    // CODE → addr: 22 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1916, UInt16: 20>  # Object: {'b': null}
    r5 = { "b": null }
    // CODE → addr: 28 | <NewObject>: <Reg8: 6>
    r6 = {  }
    // CODE → addr: 30 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 6, UInt8: 0>
    r5.slot_0 = r6
    // CODE → addr: 34 | <LoadConstNull>: <Reg8: 1>
    // USED → r1 = null;
    // CODE → addr: 36 | <Eq>: <Reg8: 3, Reg8: 5, Reg8: 1>
    // USED → r3 = r5 == null;
    // CODE → addr: 40 | <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → addr: 42 | <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // → r5 = { "b": null }
    if (r5 != null) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 47 | <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 2, string_id: 36>  # String: 'b' (Identifier)
        // USED → r5 = r5.b;
        // CODE → addr: 52 | <Eq>: <Reg8: 3, Reg8: 5, Reg8: 1>
        // USED → r3 = r5.b == null;
        // CODE → addr: 56 | <LoadConstUndefined>: <Reg8: 7>
        r7 = undefined
        // → r5 = r5.b
        if (r5.b != null) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 61 | <GetById>: <Reg8: 7, Reg8: 5, UInt8: 3, string_id: 6562>  # String: 'c' (Identifier)
            r7 = r5.c
        }
    }
    if (r7 == null) {
        // ──────────────── Block 4 ──────────────── 
        // CODE → addr: 71 | <LoadConstInt>: <Reg8: 7, Imm32: -1>
        r7 = -1
    }
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 77 | <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 83 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 88 | <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
    console.log(r7)
    // CODE → addr: 93 | <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 99 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr:104 | <LoadConstString>: <Reg8: 4, string_id: 4994>  # String: '__BC:Objects/PropertyTests/optionalChainingTest/end' (String)
    // USED → r4 = "__BC:Objects/PropertyTests/optionalChainingTest/end";
    // CODE → addr:108 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Objects/PropertyTests/optionalChainingTest/end")
    // CODE → addr:113 | <Ret>: <Reg8: 2>
    return undefined;
}