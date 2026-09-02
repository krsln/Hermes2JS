async function* anon_15169() {
    // ──────────────── Block 12 ──────────────── 
    // CODE → addr: 10 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr: 12 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 18 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 23 | <LoadConstString>: <Reg8: 1, string_id: 4779>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/start' (String)
    // USED → r1 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/start";
    // CODE → addr: 27 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/start")
    try {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 36 | <SaveGenerator>: <Addr8: 4>  # Address: 00000028
        yield "a"
        // ──────────────── Block 4 ──────────────── 
        // CODE → addr: 50 | <SaveGenerator>: <Addr8: 4>  # Address: 00000036
        yield "b"
        // ──────────────── Block 7 ──────────────── 
        // CODE → addr: 80 | <LoadConstUndefined>: <Reg8: 4>
        // USED → r4 = undefined;
        // CODE → addr: 83 | <Ret>: <Reg8: 4>
        return undefined;
    } finally {
        // ──────────────── Block 10 ──────────────── 
        // CODE → addr:133 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = console;
        // CODE → addr:139 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = console.log;
        // CODE → addr:144 | <LoadConstString>: <Reg8: 2, string_id: 4777>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup' (String)
        // USED → r2 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup";
        // CODE → addr:148 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
    }
}