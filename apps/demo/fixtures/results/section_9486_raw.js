function renamedDefaultDestructureTest(param0) {
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
    r6 = r3.timeout
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <JStrictNotEqual>: <Addr8: 10, Reg8: 6, Reg8: 1>  # Address: 0000002e
    // r6 = r3.timeout
    if (r6 !== undefined) goto label_46;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstInt>: <Reg8: 6, Imm32: 1000>
    // USED → r6 = 1000;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetById>: <Reg8: 5, Reg8: 3, UInt8: 3, string_id: 9071>  # String: 'retries' (Identifier)
    r5 = r3.retries
    // CODE → <JStrictNotEqual>: <Addr8: 7, Reg8: 5, Reg8: 1>  # Address: 0000003b
    // r5 = r3.retries
    if (r5 !== undefined) goto label_59;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 3>
    // USED → r5 = 3;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 6, Reg8: 5>
    console.log(1000, 3)
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