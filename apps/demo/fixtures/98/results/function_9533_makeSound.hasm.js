function makeSound() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 3, string_id: 4640>  # String: '__BC:Classes/ClassTests/Dog/makeSound-override' (String)
    // USED → r3 = "__BC:Classes/ClassTests/Dog/makeSound-override";
    // CODE → addr: 20 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Classes/ClassTests/Dog/makeSound-override")
    // CODE → addr: 25 | <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
    r3 = getParentEnvironment(0)
    // CODE → addr: 28 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 3, UInt8: 3>
    // USED → r3 = r3[3];
    // CODE → addr: 32 | <LoadParentNoTraps>: <Reg8: 3, Reg8: 3>
    r3 = __getPrototypeOfNoTraps__(r3[3])
    // CODE → addr: 35 | <GetByIdWithReceiverLong>: <Reg8: 3, Reg8: 3, UInt8: 2, Reg8: 1, string_id: 10532>  # String: 'makeSound' (Identifier)
    r3 = Reflect.get(r3, "makeSound", this)
    // CODE → addr: 44 | <Call1>: <Reg8: 3, Reg8: 3, Reg8: 1>
    r3 = r3.call(this)
    // CODE → addr: 48 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 54 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 59 | <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 187>  # String: 'name' (Identifier)
    // USED → r3 = this.name;
    // CODE → addr: 64 | <GetById>: <Reg8: 2, Reg8: 1, UInt8: 4, string_id: 16255>  # String: 'breed' (Identifier)
    // USED → r2 = this.breed;
    // CODE → addr: 70 | <LoadConstString>: <Reg8: 1, string_id: 1820>  # String: 'is a' (String)
    // USED → r1 = "is a";
    // CODE → addr: 74 | <Call4>: <Reg8: 1, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 1, Reg8: 2>
    console.log(this.name, "is a", this.breed)
    // CODE → addr: 81 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 83 | <Ret>: <Reg8: 0>
    return undefined;
}