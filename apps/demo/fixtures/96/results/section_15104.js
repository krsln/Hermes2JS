function renamedDefaultDestructureTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4819>  # String: '__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start' (String)
    // USED → r0 = "__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start")
    // CODE → addr: 22 | <NewObject>: <Reg8: 2>
    r2 = {  }
    // CODE → addr: 24 | <LoadConstInt>: <Reg8: 0, Imm32: 500>
    // USED → r0 = 500;
    // CODE → addr: 30 | <PutNewOwnById>: <Reg8: 2, Reg8: 0, string_id: 13118>  # String: 'timeout' (Identifier)
    r2.timeout = 500
    // CODE → addr: 35 | <GetById>: <Reg8: 3, Reg8: 2, UInt8: 3, string_id: 13118>  # String: 'timeout' (Identifier)
    r3 = r2.timeout
    // CODE → addr: 41 | <LoadConstInt>: <Reg8: 5, Imm32: 1000>
    r5 = 1000
    // CODE → addr: 47 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // → r3 = r2.timeout
    if (r3 !== undefined) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 53 | <Mov>: <Reg8: 5, Reg8: 3>
        r5 = r2.timeout
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 56 | <GetById>: <Reg8: 2, Reg8: 2, UInt8: 4, string_id: 17670>  # String: 'retries' (Identifier)
    r2 = r2.retries
    // CODE → addr: 62 | <LoadConstUInt8>: <Reg8: 4, UInt8: 3>
    r4 = 3
    // → r2 = r2.retries
    if (r2 !== undefined) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → addr: 69 | <Mov>: <Reg8: 4, Reg8: 2>
        r4 = r2.retries
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 72 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 78 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 83 | <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4>
    console.log(r5, r4)
    // CODE → addr: 89 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 95 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:100 | <LoadConstString>: <Reg8: 1, string_id: 4818>  # String: '__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end";
    // CODE → addr:104 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end")
    // CODE → addr:109 | <Ret>: <Reg8: 0>
    return undefined;
}