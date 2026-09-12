function Animal(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 2, UInt8: 0>
    // USED → r2 = this;
    // CODE → addr:  3 | <GetEnvironment>: <Reg8: 0, UInt8: 1>
    r0 = getEnvironment(1)
    // CODE → addr:  6 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 3>
    r0 = r0[3]
    // CODE → addr: 10 | <GetByIdShort>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r3 = r0.default;
    // CODE → addr: 15 | <GetEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getEnvironment(0)
    // CODE → addr: 18 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 0>
    r1 = r0[0]
    // CODE → addr: 22 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr: 24 | <Call3>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 2, Reg8: 1>
    r1 = r0.default(this, r1)
    // CODE → addr: 30 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr: 32 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 2, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 38 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 3, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 43 | <LoadConstString>: <Reg8: 1, string_id: 2494>  # String: '__BC:Classes/ClassTests/Animal/constructor' (String)
    // USED → r1 = "__BC:Classes/ClassTests/Animal/constructor";
    // CODE → addr: 47 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:Classes/ClassTests/Animal/constructor")
    // CODE → addr: 52 | <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → addr: 55 | <PutById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 176>  # String: 'name' (Identifier)
    this.name = param1
    // CODE → addr: 61 | <LoadParam>: <Reg8: 1, UInt8: 2>
    // USED → r1 = param2;
    // CODE → addr: 64 | <PutById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 11864>  # String: 'sound' (Identifier)
    this.sound = param2
    // CODE → addr: 70 | <Ret>: <Reg8: 0>
    return r0;
}