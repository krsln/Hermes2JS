function makeSound() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 0>
    // USED → r0 = this;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 3933>  # String: '__BC:Classes/ClassTests/Animal/makeSound' (String)
    // USED → r2 = "__BC:Classes/ClassTests/Animal/makeSound";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Classes/ClassTests/Animal/makeSound")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 3, string_id: 176>  # String: 'name' (Identifier)
    // USED → r2 = this.name;
    // CODE → <GetById>: <Reg8: 1, Reg8: 0, UInt8: 4, string_id: 11864>  # String: 'sound' (Identifier)
    // USED → r1 = this.sound;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 2375>  # String: 'says' (String)
    // USED → r0 = "says";
    // CODE → <Call4>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 0, Reg8: 1>
    console.log(r2, "says", r1)
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}