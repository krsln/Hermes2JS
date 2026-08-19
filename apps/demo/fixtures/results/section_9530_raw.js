function makeSound() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 0>
    r1 = this
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4093>  # String: '__BC:Classes/ClassTests/Animal/makeSound' (String)
    // USED → r3 = "__BC:Classes/ClassTests/Animal/makeSound";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Classes/ClassTests/Animal/makeSound")
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    // USED → r3 = r1.name;
    // CODE → <GetById>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 11958>  # String: 'sound' (Identifier)
    // USED → r2 = r1.sound;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 2412>  # String: 'says' (String)
    // USED → r1 = "says";
    // CODE → <Call4>: <Reg8: 1, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 1, Reg8: 2>
    console.log(r1.name, "says", r1.sound)
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}