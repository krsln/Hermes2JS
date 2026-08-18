function parameterDestructureTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 0, UInt8: 1, string_id: 29>  # String: 'id' (Identifier)
    // USED → r7 = param1.id;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 2, string_id: 176>  # String: 'name' (Identifier)
    // USED → r1 = param1.name;
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 518>  # String: 'anon' (String)
    r6 = (r1 === undefined) ? "anon" : param1.name
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 1>
    // USED → r1 = getEnvironment(0)[1];
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r3 = getEnvironment(0)[1].default;
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED → r2 = param2;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    // USED → r1 = 2;
    // CODE → <Call3>: <Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 2, Reg8: 1>
    // USED → r2 = getEnvironment(0)[1].default.call(undefined, param2, r1);
    // CODE → <LoadConstZero>: <Reg8: 1>
    r1 = 0
    // CODE → <GetByVal>: <Reg8: 10, Reg8: 2, Reg8: 1>
    r10 = getEnvironment(0)[1].default.call(undefined, param2, r1)[r1]
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    r1 = 1
    // CODE → <GetByVal>: <Reg8: 9, Reg8: 2, Reg8: 1>
    r9 = getEnvironment(0)[1].default.call(undefined, param2, r1)[r1]
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 4, string_id: 99>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 8, UInt8: 5, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4817>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/start' (String)
    // USED → r2 = "__BC:Objects/DestructuringTests/parameterDestructureTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 8, Reg8: 2>
    console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 4, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 5, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <Mov>: <Reg8: 13, Reg8: 3>
    r13 = console
    // CODE → <Mov>: <Reg8: 12, Reg8: 7>
    r12 = param1.id
    // CODE → <Mov>: <Reg8: 11, Reg8: 6>
    r11 = (r1 === undefined) ? "anon" : param1.name
    // CODE → <Call>: <Reg8: 2, Reg8: 2, UInt8: 5>
    console.log(r13, r12, r11, r10, r9)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 4, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 5, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4816>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/end' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/parameterDestructureTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}