function parameterDestructureTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr:  3 | <GetByIdShort>: <Reg8: 9, Reg8: 3, UInt8: 0, string_id: 28>  # String: 'id' (Identifier)
    // USED → r9 = param1.id;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 8, Reg8: 3, UInt8: 1, string_id: 187>  # String: 'name' (Identifier)
    r8 = (param1.name !== undefined) ? param1.name : "anon";
    // CODE → addr: 13 | <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 23 | <LoadParam>: <Reg8: 4, UInt8: 2>
    r4 = param2;
    // CODE → addr: 26 | <IteratorBegin>: <Reg8: 3, Reg8: 4>
    [r7, r6] = param2;
    // CODE → addr: 48 | <Mov>: <Reg8: 7, Reg8: 5>
    // CODE → addr: 75 | <Mov>: <Reg8: 6, Reg8: 4>
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
    console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/start");
    // CODE → addr:109 | <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 2, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:115 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 3, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:120 | <Mov>: <Reg8: 15, Reg8: 5>
    r15 = console;
    // CODE → addr:123 | <Mov>: <Reg8: 14, Reg8: 9>
    r14 = param1.id;
    // CODE → addr:126 | <Mov>: <Reg8: 13, Reg8: 8>
    r13 = (param1.name !== undefined) ? param1.name : "anon";
    // CODE → addr:129 | <Mov>: <Reg8: 12, Reg8: 7>
    r12 = r7;
    // CODE → addr:132 | <Mov>: <Reg8: 11, Reg8: 6>
    r11 = r6;
    // CODE → addr:135 | <Call>: <Reg8: 4, Reg8: 4, UInt8: 5>
    console.log(r15, r14, r13, r12, r11);
    // CODE → addr:139 | <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 2, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:145 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 3, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:150 | <LoadConstString>: <Reg8: 3, string_id: 4975>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/end' (String)
    // USED → r3 = "__BC:Objects/DestructuringTests/parameterDestructureTest/end";
    // CODE → addr:154 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/end");
    // CODE → addr:159 | <Ret>: <Reg8: 1>
}