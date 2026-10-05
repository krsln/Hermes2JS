function* simpleGeneratorTest() {
    // ──────────────── Block 22 ──────────────── 
    // CODE → addr:267 | <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → addr:269 | <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → addr:275 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr:280 | <LoadConstString>: <Reg8: 7, string_id: 4949>  # String: '__BC:Functions/GeneratorTests/simpleGeneratorTest/start' (String)
    // USED → r7 = "__BC:Functions/GeneratorTests/simpleGeneratorTest/start";
    // CODE → addr:284 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    console.log("__BC:Functions/GeneratorTests/simpleGeneratorTest/start")
    // CODE → addr:300 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 48810>  # Object: {'value': 1, 'done': false}
    yield 1
    // ──────────────── Block 17 ──────────────── 
    // CODE → addr:220 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 1525>  # Object: {'value': 2, 'done': false}
    yield 2
    // ──────────────── Block 12 ──────────────── 
    // CODE → addr:165 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 48816>  # Object: {'value': 3, 'done': false}
    yield 3
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr: 81 | <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → addr: 83 | <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → addr: 89 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr: 94 | <LoadConstString>: <Reg8: 7, string_id: 4948>  # String: '__BC:Functions/GeneratorTests/simpleGeneratorTest/end' (String)
    // USED → r7 = "__BC:Functions/GeneratorTests/simpleGeneratorTest/end";
    // CODE → addr: 98 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    console.log("__BC:Functions/GeneratorTests/simpleGeneratorTest/end")
    // CODE → addr:110 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r7 = { "value": undefined, "done": true }
    // CODE → addr:116 | <Ret>: <Reg8: 7>
    return r7;
}