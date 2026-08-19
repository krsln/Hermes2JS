function makeSound() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 1, UInt8: 0>
    r1 = this
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 3, string_id: 4093>  # String: '__BC:Classes/ClassTests/Animal/makeSound' (String)
    // USED → r3 = "__BC:Classes/ClassTests/Animal/makeSound";
    // CODE → addr: 20 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Classes/ClassTests/Animal/makeSound")
    // CODE → addr: 25 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 31 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 36 | <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    // USED → r3 = r1.name;
    // CODE → addr: 41 | <GetById>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 11958>  # String: 'sound' (Identifier)
    // USED → r2 = r1.sound;
    // CODE → addr: 47 | <LoadConstString>: <Reg8: 1, string_id: 2412>  # String: 'says' (String)
    // USED → r1 = "says";
    // CODE → addr: 51 | <Call4>: <Reg8: 1, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 1, Reg8: 2>
    console.log(r1.name, "says", r1.sound)
    // CODE → addr: 58 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 60 | <Ret>: <Reg8: 0>
    return undefined;
}