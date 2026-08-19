function swapViaDestructureTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4824>  # String: '__BC:Objects/DestructuringTests/swapViaDestructureTest/start' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/swapViaDestructureTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/start")
    // CODE → addr: 22 | <NewArray>: <Reg8: 2, UInt16: 2>
    r2 = []
    // CODE → addr: 26 | <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    // USED → r1 = 2;
    // CODE → addr: 29 | <PutOwnByIndex>: <Reg8: 2, Reg8: 1, UInt8: 0>
    // USED → r2 = r2[0] = 2;
    // CODE → addr: 33 | <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    // USED → r1 = 1;
    // CODE → addr: 36 | <PutOwnByIndex>: <Reg8: 2, Reg8: 1, UInt8: 1>
    // USED → r2 = (r2[0] = 2)[1] = 1;
    // CODE → addr: 40 | <LoadConstZero>: <Reg8: 3>
    r3 = 0
    // CODE → addr: 42 | <GetByVal>: <Reg8: 4, Reg8: 2, Reg8: 3>
    // USED → r4 = ((r2[0] = 2)[1] = 1)[r3];
    // CODE → addr: 46 | <GetByVal>: <Reg8: 3, Reg8: 2, Reg8: 1>
    // USED → r3 = ((r2[0] = 2)[1] = 1)[r1];
    // CODE → addr: 50 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 56 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 61 | <Call3>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 3>
    console.log(r4, r3)
    // CODE → addr: 67 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 73 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 78 | <LoadConstString>: <Reg8: 0, string_id: 4820>  # String: '__BC:Objects/DestructuringTests/swapViaDestructureTest/end' (String)
    // USED → r0 = "__BC:Objects/DestructuringTests/swapViaDestructureTest/end";
    // CODE → addr: 82 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/end")
    // CODE → addr: 87 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 89 | <Ret>: <Reg8: 0>
    return undefined;
}