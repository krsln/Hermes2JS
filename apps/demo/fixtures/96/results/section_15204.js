function create(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 555>  # String: '__BC:Classes/ClassTests/Dog/static-create' (String)
    // USED → r0 = "__BC:Classes/ClassTests/Dog/static-create";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Classes/ClassTests/Dog/static-create")
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getEnvironment(0)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 0, UInt8: 0>
    // USED → r3 = r0[0];
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 3, string_id: 206>  # String: 'prototype' (Identifier)
    r0 = r3.prototype
    // CODE → <CreateThis>: <Reg8: 1, Reg8: 0, Reg8: 3>
    // USED → r1 = CreateThis(r0);
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 1>
    // USED → r5 = param1;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 3527>  # String: 'Mixed' (String)
    // USED → r4 = "Mixed";
    // CODE → <Mov>: <Reg8: 6, Reg8: 1>
    // USED → r6 = CreateThis(r0);
    // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 3>
    // USED → r0 = new r0[0]("Mixed", param1);
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = new r0[0]("Mixed", param1);
    // CODE → <Ret>: <Reg8: 0>
    return new r0[0]("Mixed", param1);
}