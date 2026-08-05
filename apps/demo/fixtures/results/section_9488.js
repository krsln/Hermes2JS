function parameterDestructureTest(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 3, UInt8: 0, string_id: 28>  # String: 'id' (Identifier)
    // USED → r9 = param1.id;
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 3, UInt8: 1, string_id: 187>  # String: 'name' (Identifier)
    // USED → r8 = param1.name;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    if (param1.name === undefined) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <LoadConstString>: <Reg8: 8, string_id: 514>  # String: 'anon' (String)
        // USED → r8 = "anon";
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 2>
    // USED → r4 = param2;
    // CODE → <IteratorBegin>: <Reg8: 3, Reg8: 4>
    // USED → r3 = GetIterator(r4);
    // CODE → <Mov>: <Reg8: 5, Reg8: 4>
    r5 = param2
    // CODE → <IteratorNext>: <Reg8: 5, Reg8: 3, Reg8: 5>
    // USED → r5 = GetIterator(r4).next();
    // CODE → <Mov>: <Reg8: 6, Reg8: 3>
    // USED → r6 = GetIterator(r4);
    // CODE → <StrictEq>: <Reg8: 0, Reg8: 6, Reg8: 1>
    // USED → r0 = GetIterator(r4) === undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    if (GetIterator(r4) !== undefined) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <Mov>: <Reg8: 7, Reg8: 5>
        // USED → r7 = GetIterator(r4).next();
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 6>
    r6 = undefined
    if (GetIterator(r4) !== undefined && GetIterator(r4) !== undefined) {
        // ──────────────── Block 6 ──────────────── 
        // CODE → <Mov>: <Reg8: 6, Reg8: 4>
        // USED → r6 = GetIterator(r4).next();
        // CODE → <Mov>: <Reg8: 0, Reg8: 2>
        // USED → r0 = GetIterator(r4) === undefined;
    }
    if (GetIterator(r4) !== undefined) {
        // ──────────────── Block 8 ──────────────── 
        // CODE → <IteratorClose>: <Reg8: 3, UInt8: 0>
        GetIterator(r4).return()
    }
    // ──────────────── Block 9 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → <TryGetById>: <Reg8: 10, Reg8: 3, UInt8: 2, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 10, UInt8: 3, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4978>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/start' (String)
    // USED → r4 = "__BC:Objects/DestructuringTests/parameterDestructureTest/start";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 10, Reg8: 4>
    r4 = globalThis.console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/start")
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 2, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 3, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <Mov>: <Reg8: 15, Reg8: 5>
    r15 = globalThis.console
    // CODE → <Mov>: <Reg8: 14, Reg8: 9>
    r14 = param1.id
    // CODE → <Mov>: <Reg8: 13, Reg8: 8>
    r13 = "anon"
    // CODE → <Mov>: <Reg8: 12, Reg8: 7>
    r12 = GetIterator(r4).next()
    // CODE → <Mov>: <Reg8: 11, Reg8: 6>
    r11 = GetIterator(r4).next()
    // CODE → <Call>: <Reg8: 4, Reg8: 4, UInt8: 5>
    r4 = globalThis.console.log(r15, r14, r13, r12, r11)
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 2, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 3, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4975>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/end' (String)
    // USED → r3 = "__BC:Objects/DestructuringTests/parameterDestructureTest/end";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/end")
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}