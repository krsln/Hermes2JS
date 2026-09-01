function makeSound() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 0, UInt8: 0>
    // USED → r0 = this;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 2, string_id: 3933>  # String: '__BC:Classes/ClassTests/Animal/makeSound' (String)
    // USED → r2 = "__BC:Classes/ClassTests/Animal/makeSound";
    // CODE → addr: 20 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Classes/ClassTests/Animal/makeSound")
    // CODE → addr: 25 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 31 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 36 | <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 3, string_id: 176>  # String: 'name' (Identifier)
    // USED → r2 = this.name;
    // CODE → addr: 41 | <GetById>: <Reg8: 1, Reg8: 0, UInt8: 4, string_id: 11864>  # String: 'sound' (Identifier)
    // USED → r1 = this.sound;
    // CODE → addr: 47 | <LoadConstString>: <Reg8: 0, string_id: 2375>  # String: 'says' (String)
    // USED → r0 = "says";
    // CODE → addr: 51 | <Call4>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 0, Reg8: 1>
    console.log(this.name, "says", this.sound)
    // CODE → addr: 58 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 60 | <Ret>: <Reg8: 0>
    return undefined;
}