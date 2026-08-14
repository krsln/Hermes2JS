function optionalChainingTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4995>  # String: '__BC:Objects/PropertyTests/optionalChainingTest/start' (String)
    // USED → r5 = "__BC:Objects/PropertyTests/optionalChainingTest/start";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/PropertyTests/optionalChainingTest/start")
    // CODE → <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1916, UInt16: 20>  # Object: {'b': null}
    r5 = { "b": null }
    // CODE → <NewObject>: <Reg8: 6>
    r6 = {  }
    // CODE → <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 6, UInt8: 0>
    r5.slot_0 = r6
    // CODE → <LoadConstNull>: <Reg8: 1>
    // USED → r1 = null;
    // CODE → <Eq>: <Reg8: 3, Reg8: 5, Reg8: 1>
    // USED → r3 = r5 == null;
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <JmpTrue>: <Addr8: 23, Reg8: 3>  # Address: 00000043
    // → r5 = { "b": null }
    if (r5 == null) goto label_67;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 2, string_id: 36>  # String: 'b' (Identifier)
    // USED → r5 = r5.b;
    // CODE → <Eq>: <Reg8: 3, Reg8: 5, Reg8: 1>
    // USED → r3 = r5.b == null;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <JmpTrue>: <Addr8: 9, Reg8: 3>  # Address: 00000043
    // → r5 = r5.b
    if (r5.b == null) goto label_67;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetById>: <Reg8: 7, Reg8: 5, UInt8: 3, string_id: 6562>  # String: 'c' (Identifier)
    // USED → r7 = r5.b.c;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <JNotEqual>: <Addr8: 10, Reg8: 7, Reg8: 1>  # Address: 0000004d
    if (r7 != null) goto label_77;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadConstInt>: <Reg8: 7, Imm32: -1>
    // USED → r7 = -1;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
    console.log(r7)
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4994>  # String: '__BC:Objects/PropertyTests/optionalChainingTest/end' (String)
    // USED → r4 = "__BC:Objects/PropertyTests/optionalChainingTest/end";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Objects/PropertyTests/optionalChainingTest/end")
    // CODE → <Ret>: <Reg8: 2>
    return undefined;
}