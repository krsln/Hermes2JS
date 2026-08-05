function renamedDefaultDestructureTest(param0) {
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
    r0 = globalThis.console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start")
    // CODE → <NewObject>: <Reg8: 2>
    // USED → r2 = {  };
    // CODE → <LoadConstInt>: <Reg8: 0, Imm32: 500>
    // USED → r0 = 500;
    // CODE → <PutNewOwnById>: <Reg8: 2, Reg8: 0, string_id: 13118>  # String: 'timeout' (Identifier)
    // USED → r2 = { timeout: 500 };
    // CODE → <GetById>: <Reg8: 3, Reg8: 2, UInt8: 3, string_id: 13118>  # String: 'timeout' (Identifier)
    // USED → r3 = { timeout: 500 }.timeout;
    // CODE → <LoadConstInt>: <Reg8: 5, Imm32: 1000>
    r5 = 1000
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    if ({ timeout: 500 }.timeout !== undefined) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 5, Reg8: 3>
        // USED → r5 = { timeout: 500 }.timeout;
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 4, string_id: 17670>  # String: 'retries' (Identifier)
    // USED → r2 = { timeout: 500 }.retries;
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 3>
    r4 = 3
    if ({ timeout: 500 }.retries !== undefined) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <Mov>: <Reg8: 4, Reg8: 2>
        // USED → r4 = { timeout: 500 }.retries;
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4>
    r2 = globalThis.console.log({ timeout: 500 }.timeout, { timeout: 500 }.retries)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4818>  # String: '__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}