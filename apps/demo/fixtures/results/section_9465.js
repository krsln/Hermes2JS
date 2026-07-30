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
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4070>  # String: '__BC:Classes/ClassTests/Animal/makeSound' (String)
    // USED → r3 = "__BC:Classes/ClassTests/Animal/makeSound";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:Classes/ClassTests/Animal/makeSound")
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 186>  # String: 'name' (Identifier)
    // USED → r3 = this.name;
    // CODE → <GetById>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 11493>  # String: 'sound' (Identifier)
    // USED → r2 = this.sound;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 2524>  # String: 'says' (String)
    // USED → r1 = "says";
    // CODE → <Call4>: <Reg8: 1, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 1, Reg8: 2>
    r1 = globalThis.console.log(this.name, "says", this.sound)
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}