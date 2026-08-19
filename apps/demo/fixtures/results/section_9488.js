function parameterDestructureTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 3, UInt8: 1>
    r3 = param1
    // CODE → addr:  3 | <GetByIdShort>: <Reg8: 9, Reg8: 3, UInt8: 0, string_id: 28>  # String: 'id' (Identifier)
    // USED → r9 = r3.id;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 8, Reg8: 3, UInt8: 1, string_id: 187>  # String: 'name' (Identifier)
    r8 = (r8 !== undefined) ? r3.name : "anon"
    // CODE → addr: 13 | <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 23 | <LoadParam>: <Reg8: 4, UInt8: 2>
    r4 = param2
    // CODE → addr: 26 | <IteratorBegin>: <Reg8: 3, Reg8: 4>
    r3 = GetIterator(r4)
    // CODE → addr: 29 | <Mov>: <Reg8: 5, Reg8: 4>
    r5 = param2
    // CODE → addr: 32 | <IteratorNext>: <Reg8: 5, Reg8: 3, Reg8: 5>
    r5 = r3.next()
    // CODE → addr: 36 | <Mov>: <Reg8: 6, Reg8: 3>
    // USED → r6 = r3;
    // CODE → addr: 39 | <StrictEq>: <Reg8: 0, Reg8: 6, Reg8: 1>
    // USED → r0 = r3 === undefined;
    // CODE → addr: 43 | <LoadConstUndefined>: <Reg8: 7>
    r7 = (r3 === undefined) ? undefined : r5
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 51 | <LoadConstUndefined>: <Reg8: 6>
    r6 = undefined
    if (r3 !== undefined) {
        // ──────────────── Block 5 ──────────────── 
        // CODE → addr: 56 | <IteratorNext>: <Reg8: 4, Reg8: 3, Reg8: 4>
        r4 = r3.next()
        // CODE → addr: 60 | <Mov>: <Reg8: 5, Reg8: 3>
        // USED → r5 = r3;
        // CODE → addr: 63 | <StrictEq>: <Reg8: 2, Reg8: 5, Reg8: 1>
        // USED → r2 = r3 === undefined;
        // CODE → addr: 67 | <LoadConstUndefined>: <Reg8: 6>
        r6 = undefined
        // CODE → addr: 69 | <Mov>: <Reg8: 0, Reg8: 2>
        r0 = r3 === undefined || r3 === undefined
    }
    if (r3 !== undefined) {
        // ──────────────── Block 8 ──────────────── 
        // CODE → addr: 84 | <IteratorClose>: <Reg8: 3, UInt8: 0>
        r3.return()
    }
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr: 87 | <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → addr: 89 | <TryGetById>: <Reg8: 10, Reg8: 3, UInt8: 2, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr: 95 | <GetByIdShort>: <Reg8: 5, Reg8: 10, UInt8: 3, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr:100 | <LoadConstString>: <Reg8: 4, string_id: 4978>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/start' (String)
    // USED → r4 = "__BC:Objects/DestructuringTests/parameterDestructureTest/start";
    // CODE → addr:104 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 10, Reg8: 4>
    console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/start")
    // CODE → addr:109 | <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 2, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:115 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 3, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:120 | <Mov>: <Reg8: 15, Reg8: 5>
    r15 = console
    // CODE → addr:123 | <Mov>: <Reg8: 14, Reg8: 9>
    r14 = r3.id
    // CODE → addr:126 | <Mov>: <Reg8: 13, Reg8: 8>
    r13 = (r8 !== undefined) ? r3.name : "anon"
    // CODE → addr:129 | <Mov>: <Reg8: 12, Reg8: 7>
    r12 = (r3 === undefined) ? undefined : r5
    // CODE → addr:132 | <Mov>: <Reg8: 11, Reg8: 6>
    r11 = r4
    // CODE → addr:135 | <Call>: <Reg8: 4, Reg8: 4, UInt8: 5>
    console.log(r15, r14, r13, r12, r11)
    // CODE → addr:139 | <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 2, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:145 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 3, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:150 | <LoadConstString>: <Reg8: 3, string_id: 4975>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/end' (String)
    // USED → r3 = "__BC:Objects/DestructuringTests/parameterDestructureTest/end";
    // CODE → addr:154 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/end")
    // CODE → addr:159 | <Ret>: <Reg8: 1>
    return undefined;
}