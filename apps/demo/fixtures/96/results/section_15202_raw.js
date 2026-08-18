function Dog(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 0>
    // USED → r4 = this;
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 1>
    r0 = getEnvironment(1)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 3>
    // USED → r1 = r0[3];
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r1 = r0[3].default;
    // CODE → <GetEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getEnvironment(0)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 0>
    // USED → r3 = r2[0];
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 3>
    r1 = r0[3].default.call(undefined, this, r3)
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 0>
    // USED → r0 = r0[0];
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r1 = r0[0].default;
    // CODE → <NewArray>: <Reg8: 0, UInt16: 2>
    r0 = []
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 1>
    // USED → r5 = param1;
    // CODE → <PutOwnByIndex>: <Reg8: 0, Reg8: 5, UInt8: 0>
    // USED → r0 = r0[0] = param1;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4300>  # String: 'Woof' (String)
    // USED → r5 = "Woof";
    // CODE → <PutOwnByIndex>: <Reg8: 0, Reg8: 5, UInt8: 1>
    // USED → r0 = (r0[0] = param1)[1] = "Woof";
    // CODE → <Call4>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 3, Reg8: 0>
    r0 = r0[0].default.call(undefined, this, r3, r0)
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 2913>  # String: '__BC:Classes/ClassTests/Dog/constructor' (String)
    // USED → r1 = "__BC:Classes/ClassTests/Dog/constructor";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/ClassTests/Dog/constructor")
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 2>
    // USED → r1 = param2;
    // CODE → <PutById>: <Reg8: 0, Reg8: 1, UInt8: 1, string_id: 16784>  # String: 'breed' (Identifier)
    r0.breed = param2
    // CODE → <Ret>: <Reg8: 0>
    return r0;
}