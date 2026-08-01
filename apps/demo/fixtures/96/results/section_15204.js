function create(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 555>  # String: '__BC:Classes/ClassTests/Dog/static-create' (String)
    // USED → r0 = "__BC:Classes/ClassTests/Dog/static-create";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:Classes/ClassTests/Dog/static-create")
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 0, UInt8: 0>
    // USED → r3 = getEnvironment(0)[0];
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 3, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r0 = getEnvironment(0)[0].prototype;
    // CODE → <CreateThis>: <Reg8: 1, Reg8: 0, Reg8: 3>
    // USED → r1 = createThis(getEnvironment(0)[0].prototype, getEnvironment(0)[0]);
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 1>
    // USED → r5 = param1;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 3527>  # String: 'Mixed' (String)
    // USED → r4 = "Mixed";
    // CODE → <Mov>: <Reg8: 6, Reg8: 1>
    r6 = createThis(getEnvironment(0)[0].prototype, getEnvironment(0)[0])
    // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 3>
    // USED → r0 = new getEnvironment(0)[0]("Mixed", param1);
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = new getEnvironment(0)[0]("Mixed", param1);
    // CODE → <Ret>: <Reg8: 0>
    return new getEnvironment(0)[0]("Mixed", param1);
}