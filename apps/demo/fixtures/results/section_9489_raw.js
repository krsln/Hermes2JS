function swapViaDestructureTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4986>  # String: '__BC:Objects/DestructuringTests/swapViaDestructureTest/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/swapViaDestructureTest/start";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/start")
    // CODE → <NewArray>: <Reg8: 7, UInt16: 2>
    r7 = []
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 0, UInt8: 0>
    r7[0] = 2
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 0, UInt8: 1>
    r7[1] = 1
    // CODE → <Mov>: <Reg8: 6, Reg8: 7>
    // USED → r6 = r7;
    // CODE → <IteratorBegin>: <Reg8: 5, Reg8: 6>
    // USED → r5 = GetIterator(r6);
    // CODE → <Mov>: <Reg8: 7, Reg8: 6>
    r7 = r7
    // CODE → <IteratorNext>: <Reg8: 7, Reg8: 5, Reg8: 7>
    // USED → r7 = GetIterator(r6).next();
    // CODE → <Mov>: <Reg8: 8, Reg8: 5>
    // USED → r8 = GetIterator(r6);
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → <StrictEq>: <Reg8: 1, Reg8: 8, Reg8: 2>
    // USED → r1 = GetIterator(r6) === undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // CODE → <JmpTrue>: <Addr8: 6, Reg8: 1>  # Address: 00000046
    // → r6 = r7
    if (GetIterator(r6) === undefined) goto label_70;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Mov>: <Reg8: 8, Reg8: 7>
    // USED → r8 = GetIterator(r6).next();
    // ──────────────── Block 2 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <JmpTrue>: <Addr8: 28, Reg8: 1>  # Address: 00000064
    if (GetIterator(r6) === undefined) goto label_100;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <IteratorNext>: <Reg8: 6, Reg8: 5, Reg8: 6>
    // USED → r6 = GetIterator(r6).next();
    // CODE → <Mov>: <Reg8: 9, Reg8: 5>
    // USED → r9 = GetIterator(r6);
    // CODE → <StrictEq>: <Reg8: 3, Reg8: 9, Reg8: 2>
    // USED → r3 = GetIterator(r6) === undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <Mov>: <Reg8: 1, Reg8: 3>
    r1 = GetIterator(r6) === undefined
    // CODE → <JmpTrue>: <Addr8: 9, Reg8: 3>  # Address: 00000064
    // → r6 = GetIterator(r6).next()
    if (GetIterator(r6) === undefined) goto label_100;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <Mov>: <Reg8: 7, Reg8: 6>
    // USED → r7 = GetIterator(r6).next();
    // CODE → <Mov>: <Reg8: 1, Reg8: 3>
    // USED → r1 = GetIterator(r6) === undefined;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <JmpTrue>: <Addr8: 6, Reg8: 1>  # Address: 0000006a
    if (GetIterator(r6) === undefined) goto label_106;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <IteratorClose>: <Reg8: 5, UInt8: 0>
    GetIterator(r6).return()
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 8, Reg8: 7>
    console.log(r8, r7)
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4984>  # String: '__BC:Objects/DestructuringTests/swapViaDestructureTest/end' (String)
    // USED → r4 = "__BC:Objects/DestructuringTests/swapViaDestructureTest/end";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/end")
    // CODE → <Ret>: <Reg8: 2>
    return undefined;
}