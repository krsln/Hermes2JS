function makeSound(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this;
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4520>  # String: '__BC:Classes/ClassTests/Dog/makeSound-override' (String)
    // USED → r0 = "__BC:Classes/ClassTests/Dog/makeSound-override";
    // CODE → <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 0>
    r0 = globalThis.console.log("__BC:Classes/ClassTests/Dog/makeSound-override")
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 1>
    // USED → r0 = getEnvironment(1);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 1>
    // USED → r0 = getEnvironment(1)[1];
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 0, UInt8: 3, string_id: 108>  # String: 'default' (Identifier)
    // USED → r6 = getEnvironment(1)[1].default;
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 10, Reg8: 0, UInt8: 0>
    r10 = getEnvironment(0)[0]
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 10199>  # String: 'makeSound' (Identifier)
    r9 = "makeSound"
    // CODE → <LoadConstUInt8>: <Reg8: 7, UInt8: 3>
    r7 = 3
    // CODE → <LoadConstUndefined>: <Reg8: 11>
    r11 = undefined
    // CODE → <Mov>: <Reg8: 8, Reg8: 1>
    r8 = this
    // CODE → <Call>: <Reg8: 4, Reg8: 6, UInt8: 5>
    // USED → r4 = getEnvironment(1)[1].default(r1, r2, r3, r4, r5);
    // CODE → <NewArray>: <Reg8: 3, UInt16: 0>
    // USED → r3 = [];
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    r3 = getEnvironment(1)[1].default(r1, r2, r3, r4, r5).call(undefined, [])
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 4, string_id: 176>  # String: 'name' (Identifier)
    // USED → r3 = this.name;
    // CODE → <GetById>: <Reg8: 2, Reg8: 1, UInt8: 5, string_id: 16498>  # String: 'breed' (Identifier)
    // USED → r2 = this.breed;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 1869>  # String: 'is a' (String)
    // USED → r1 = "is a";
    // CODE → <Call4>: <Reg8: 1, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 1, Reg8: 2>
    r1 = globalThis.console.log(this.name, "is a", this.breed)
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}