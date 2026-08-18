function Animal(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 0>
    // USED → r2 = this;
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 1>
    // USED → r0 = getEnvironment(1);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 3>
    // USED → r0 = getEnvironment(1)[3];
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r3 = getEnvironment(1)[3].default;
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 0>
    // USED → r1 = getEnvironment(0)[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call3>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 2, Reg8: 1>
    r1 = getEnvironment(1)[3].default.call(undefined, this, r1)
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 2, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 3, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 2494>  # String: '__BC:Classes/ClassTests/Animal/constructor' (String)
    // USED → r1 = "__BC:Classes/ClassTests/Animal/constructor";
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:Classes/ClassTests/Animal/constructor")
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → <PutById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 176>  # String: 'name' (Identifier)
    this.name = param1
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 2>
    // USED → r1 = param2;
    // CODE → <PutById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 11864>  # String: 'sound' (Identifier)
    this.sound = param2
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}