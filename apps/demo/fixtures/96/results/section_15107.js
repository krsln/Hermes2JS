function swapViaDestructureTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4824>  # String: '__BC:Objects/DestructuringTests/swapViaDestructureTest/start' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/swapViaDestructureTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/start")
    // CODE → <NewArray>: <Reg8: 2, UInt16: 2>
    // USED → r2 = [];
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    // USED → r1 = 2;
    // CODE → <PutOwnByIndex>: <Reg8: 2, Reg8: 1, UInt8: 0>
    // USED → r2 = [2];
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    // USED → r1 = 1;
    // CODE → <PutOwnByIndex>: <Reg8: 2, Reg8: 1, UInt8: 1>
    // USED → r2 = [2, 1];
    // CODE → <LoadConstZero>: <Reg8: 3>
    // USED → r3 = 0;
    // CODE → <GetByVal>: <Reg8: 4, Reg8: 2, Reg8: 3>
    // USED → r4 = [2, 1][0];
    // CODE → <GetByVal>: <Reg8: 3, Reg8: 2, Reg8: 1>
    // USED → r3 = [2, 1][1];
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 3>
    r1 = globalThis.console.log([2, 1][0], [2, 1][1])
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4820>  # String: '__BC:Objects/DestructuringTests/swapViaDestructureTest/end' (String)
    // USED → r0 = "__BC:Objects/DestructuringTests/swapViaDestructureTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}