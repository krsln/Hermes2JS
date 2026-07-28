function makeSound(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this;
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4620>  # String: '__BC:Classes/ClassTests/Dog/makeSound-override' (String)
    // USED → r3 = "__BC:Classes/ClassTests/Dog/makeSound-override";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:Classes/ClassTests/Dog/makeSound-override");
    // CODE → <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
    // USED → r3 = getParentEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 3, UInt8: 3>
    // USED → r3 = getParentEnvironment(0)[3];
    // CODE → <LoadParentNoTraps>: <Reg8: 3, Reg8: 3>
    // USED → r3 = __getPrototypeOfNoTraps__(getParentEnvironment(0)[3]);
    // CODE → <GetByIdWithReceiverLong>: <Reg8: 3, Reg8: 3, UInt8: 2, Reg8: 1, string_id: 9459>  # String: 'makeSound' (Identifier)
    // Error: GetByIdWithReceiverLong at address 35: Expected Reg8, Reg8, UInt8, Reg8, string_id arguments: Reg8: 3, Reg8: 3, UInt8: 2, Reg8: 1, string_id: 9459;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 1>
    r3 = __getPrototypeOfNoTraps__(getParentEnvironment(0)[3]).call(this);
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 186>  # String: 'name' (Identifier)
    // USED → r3 = this.name;
    // CODE → <GetById>: <Reg8: 2, Reg8: 1, UInt8: 4, string_id: 15973>  # String: 'breed' (Identifier)
    // USED → r2 = this.breed;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 1817>  # String: 'is a' (String)
    // USED → r1 = "is a";
    // CODE → <Call4>: <Reg8: 1, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 1, Reg8: 2>
    r1 = globalThis.console.log(this.name, "is a", this.breed);
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}