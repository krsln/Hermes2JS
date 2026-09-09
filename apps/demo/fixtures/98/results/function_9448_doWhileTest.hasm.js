function doWhileTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 6, string_id: 4755>  # String: '__BC:ControlFlow/DoWhileTests/doWhileTest/start' (String)
    // USED → r6 = "__BC:ControlFlow/DoWhileTests/doWhileTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    console.log("__BC:ControlFlow/DoWhileTests/doWhileTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    // USED → r1 = 1;
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 2, UInt8: 5>
    // USED → r2 = 5;
    // CODE → addr: 28 | <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // LOOP → START (do_while)
    do {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 30 | <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r7 = console;
        // CODE → addr: 36 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r6 = console.log;
        // CODE → addr: 41 | <Call2>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 0>
        console.log(r0)
        // CODE → addr: 46 | <AddN>: <Reg8: 0, Reg8: 0, Reg8: 1>
        r0 = r0 + 1
    // → r0 = r0 + 1
    } while (r0 < 5);
    // LOOP → END
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 54 | <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr: 60 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr: 65 | <LoadConstString>: <Reg8: 5, string_id: 4281>  # String: '__BC:ControlFlow/DoWhileTests/doWhileTest/end' (String)
    // USED → r5 = "__BC:ControlFlow/DoWhileTests/doWhileTest/end";
    // CODE → addr: 69 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:ControlFlow/DoWhileTests/doWhileTest/end")
    // CODE → addr: 74 | <LoadConstUndefined>: <Reg8: 4>
    // USED → r4 = undefined;
    // CODE → addr: 76 | <Ret>: <Reg8: 4>
    return undefined;
}