function* anon_15165() {
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr:  7 | <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → addr:  9 | <TryGetById>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 15 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 20 | <LoadConstString>: <Reg8: 1, string_id: 4789>  # String: '__BC:Functions/GeneratorTests/simpleGeneratorTest/start' (String)
    // USED → r1 = "__BC:Functions/GeneratorTests/simpleGeneratorTest/start";
    // CODE → addr: 24 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/GeneratorTests/simpleGeneratorTest/start")
    // CODE → addr: 32 | <SaveGenerator>: <Addr8: 4>  # Address: 00000024
    yield 1
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 45 | <SaveGenerator>: <Addr8: 4>  # Address: 00000031
    yield 2
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr: 58 | <SaveGenerator>: <Addr8: 4>  # Address: 0000003e
    yield 3
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr: 68 | <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 74 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 79 | <LoadConstString>: <Reg8: 4, string_id: 4197>  # String: '__BC:Functions/GeneratorTests/simpleGeneratorTest/end' (String)
    // USED → r4 = "__BC:Functions/GeneratorTests/simpleGeneratorTest/end";
    // CODE → addr: 83 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Functions/GeneratorTests/simpleGeneratorTest/end")
    // CODE → addr: 88 | <LoadConstUndefined>: <Reg8: 4>
    // USED → r4 = undefined;
    // CODE → addr: 91 | <Ret>: <Reg8: 4>
    return undefined;
}