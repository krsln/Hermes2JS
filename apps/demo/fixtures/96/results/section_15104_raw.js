function renamedDefaultDestructureTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4819>  # String: '__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start' (String)
    // USED → r0 = "__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start")
    // CODE → <NewObject>: <Reg8: 2>
    r2 = {  }
    // CODE → <LoadConstInt>: <Reg8: 0, Imm32: 500>
    // USED → r0 = 500;
    // CODE → <PutNewOwnById>: <Reg8: 2, Reg8: 0, string_id: 13118>  # String: 'timeout' (Identifier)
    r2.timeout = 500
    // CODE → <GetById>: <Reg8: 3, Reg8: 2, UInt8: 3, string_id: 13118>  # String: 'timeout' (Identifier)
    // USED → r3 = r2.timeout;
    // CODE → <LoadConstInt>: <Reg8: 5, Imm32: 1000>
    r5 = 1000
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <JStrictEqual>: <Addr8: 7, Reg8: 3, Reg8: 0>  # Address: 00000038
    // → r3 = r2.timeout
    if (r3 === undefined) goto label_56;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Mov>: <Reg8: 5, Reg8: 3>
    // USED → r5 = r2.timeout;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 4, string_id: 17670>  # String: 'retries' (Identifier)
    // USED → r2 = r2.retries;
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 3>
    r4 = 3
    // CODE → <JStrictEqual>: <Addr8: 7, Reg8: 2, Reg8: 0>  # Address: 00000048
    // → r2 = r2.retries
    if (r2 === undefined) goto label_72;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <Mov>: <Reg8: 4, Reg8: 2>
    // USED → r4 = r2.retries;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4>
    console.log(r5, r4)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4818>  # String: '__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}