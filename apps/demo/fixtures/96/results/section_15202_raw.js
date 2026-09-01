function Dog(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 4, UInt8: 0>
    // USED → r4 = this;
    // CODE → addr:  3 | <GetEnvironment>: <Reg8: 0, UInt8: 1>
    r0 = getEnvironment(1)
    // CODE → addr:  6 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 3>
    r1 = r0[3]
    // CODE → addr: 10 | <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r1 = r1.default;
    // CODE → addr: 15 | <GetEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getEnvironment(0)
    // CODE → addr: 18 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 0>
    r3 = r2[0]
    // CODE → addr: 22 | <LoadConstUndefined>: <Reg8: 2>
    r2 = undefined
    // CODE → addr: 24 | <Call3>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 3>
    r1 = r1.default.call(r2, this, r3)
    // CODE → addr: 30 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 0>
    r0 = r0[0]
    // CODE → addr: 34 | <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r1 = r0.default;
    // CODE → addr: 39 | <NewArray>: <Reg8: 0, UInt16: 2>
    r0 = []
    // CODE → addr: 43 | <LoadParam>: <Reg8: 5, UInt8: 1>
    // USED → r5 = param1;
    // CODE → addr: 46 | <PutOwnByIndex>: <Reg8: 0, Reg8: 5, UInt8: 0>
    // USED → r0 = r0[0] = param1;
    // CODE → addr: 50 | <LoadConstString>: <Reg8: 5, string_id: 4300>  # String: 'Woof' (String)
    // USED → r5 = "Woof";
    // CODE → addr: 54 | <PutOwnByIndex>: <Reg8: 0, Reg8: 5, UInt8: 1>
    r0 = (r0[0] = param1)[1] = "Woof"
    // CODE → addr: 58 | <Call4>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 3, Reg8: 0>
    r0 = r0.default.call(r2, this, r3, r0)
    // CODE → addr: 65 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr: 67 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 73 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 78 | <LoadConstString>: <Reg8: 1, string_id: 2913>  # String: '__BC:Classes/ClassTests/Dog/constructor' (String)
    // USED → r1 = "__BC:Classes/ClassTests/Dog/constructor";
    // CODE → addr: 82 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/ClassTests/Dog/constructor")
    // CODE → addr: 87 | <LoadParam>: <Reg8: 1, UInt8: 2>
    // USED → r1 = param2;
    // CODE → addr: 90 | <PutById>: <Reg8: 0, Reg8: 1, UInt8: 1, string_id: 16784>  # String: 'breed' (Identifier)
    r0.breed = param2
    // CODE → addr: 96 | <Ret>: <Reg8: 0>
    return r0;
}