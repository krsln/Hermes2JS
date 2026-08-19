function parameterDestructureTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 0, UInt8: 1>
    r0 = param1
    // CODE → addr:  3 | <GetByIdShort>: <Reg8: 7, Reg8: 0, UInt8: 1, string_id: 29>  # String: 'id' (Identifier)
    // USED → r7 = r0.id;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 2, string_id: 176>  # String: 'name' (Identifier)
    r1 = r0.name
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 6, string_id: 518>  # String: 'anon' (String)
    r6 = (r1 === undefined) ? "anon" : r0.name
    // CODE → addr: 17 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 26 | <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // CODE → addr: 29 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 1>
    r1 = r1[1]
    // CODE → addr: 33 | <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r3 = r1.default;
    // CODE → addr: 38 | <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED → r2 = param2;
    // CODE → addr: 41 | <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    // USED → r1 = 2;
    // CODE → addr: 44 | <Call3>: <Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 2, Reg8: 1>
    r2 = r1.default.call(r0, param2, 2)
    // CODE → addr: 50 | <LoadConstZero>: <Reg8: 1>
    r1 = 0
    // CODE → addr: 52 | <GetByVal>: <Reg8: 10, Reg8: 2, Reg8: 1>
    r10 = r2[r1]
    // CODE → addr: 56 | <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    r1 = 1
    // CODE → addr: 59 | <GetByVal>: <Reg8: 9, Reg8: 2, Reg8: 1>
    r9 = r2[r1]
    // CODE → addr: 63 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr: 65 | <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 4, string_id: 99>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr: 71 | <GetByIdShort>: <Reg8: 3, Reg8: 8, UInt8: 5, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 76 | <LoadConstString>: <Reg8: 2, string_id: 4817>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/start' (String)
    // USED → r2 = "__BC:Objects/DestructuringTests/parameterDestructureTest/start";
    // CODE → addr: 80 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 8, Reg8: 2>
    console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/start")
    // CODE → addr: 85 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 4, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 91 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 5, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 96 | <Mov>: <Reg8: 13, Reg8: 3>
    r13 = console
    // CODE → addr: 99 | <Mov>: <Reg8: 12, Reg8: 7>
    r12 = r0.id
    // CODE → addr:102 | <Mov>: <Reg8: 11, Reg8: 6>
    r11 = (r1 === undefined) ? "anon" : r0.name
    // CODE → addr:105 | <Call>: <Reg8: 2, Reg8: 2, UInt8: 5>
    console.log(r13, r12, r11, r10, r9)
    // CODE → addr:109 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 4, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:115 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 5, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:120 | <LoadConstString>: <Reg8: 1, string_id: 4816>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/end' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/parameterDestructureTest/end";
    // CODE → addr:124 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/end")
    // CODE → addr:129 | <Ret>: <Reg8: 0>
    return undefined;
}