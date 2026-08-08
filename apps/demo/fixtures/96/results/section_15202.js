function Dog(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 0>
    // USED → r4 = this;
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 1>
    // USED → r0 = getEnvironment(1);
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 3>
    // USED → r1 = getEnvironment(1)[3];
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r1 = getEnvironment(1)[3].default;
    // CODE → <GetEnvironment>: <Reg8: 2, UInt8: 0>
    // USED → r2 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 0>
    // USED → r3 = getEnvironment(0)[0];
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 3>
    r1 = getEnvironment(1)[3].default.call(undefined, this, getEnvironment(0)[0])
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(1)[0];
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r1 = getEnvironment(1)[0].default;
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
    // USED → r0 = getEnvironment(1)[0].default.call(undefined, this, getEnvironment(0)[0], (r0[0] = param1)[1] = "Woof");
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 2913>  # String: '__BC:Classes/ClassTests/Dog/constructor' (String)
    // USED → r1 = "__BC:Classes/ClassTests/Dog/constructor";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Classes/ClassTests/Dog/constructor")
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 2>
    // USED → r1 = param2;
    // CODE → <PutById>: <Reg8: 0, Reg8: 1, UInt8: 1, string_id: 16784>  # String: 'breed' (Identifier)
    getEnvironment(1)[0].default.call(undefined, this, getEnvironment(0)[0], (r0[0] = param1)[1] = "Woof").breed = param2
    // CODE → <Ret>: <Reg8: 0>
    return getEnvironment(1)[0].default.call(undefined, this, getEnvironment(0)[0], (r0[0] = param1)[1] = "Woof");
}