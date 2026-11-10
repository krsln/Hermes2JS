function* generatorTryFinallyTest() {
    // ──────────────── Block 31 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0);
    try {
        // ──────────────── Block 18 ──────────────── 
        // CODE → addr:286 | <TryGetById>: <Reg8: 13, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r13 = console;
        // CODE → addr:292 | <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r12 = console.log;
        // CODE → addr:297 | <Call2>: <Reg8: 12, Reg8: 12, Reg8: 13, Reg8: 9>
        console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/start");
        // CODE → addr:302 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 5>
        r1[3] = 1;
        // CODE → addr:317 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 48822>  # Object: {'value': 'a', 'done': false}
        yield "a";
        // ──────────────── Block 12 ──────────────── 
        // CODE → addr:193 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 48826>  # Object: {'value': 'b', 'done': false}
        yield "b";
        // ──────────────── Block 7 ──────────────── 
        // CODE → addr: 91 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 11>
        r1[3] = 0;
        // CODE → addr: 95 | <TryGetById>: <Reg8: 13, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r13 = console;
        // CODE → addr:101 | <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r12 = console.log;
        // CODE → addr:106 | <Call2>: <Reg8: 12, Reg8: 12, Reg8: 13, Reg8: 8>
        console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup");
        // CODE → addr:118 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
        r12 = { "value": undefined, "done": true };
        // CODE → addr:124 | <Ret>: <Reg8: 12>
        return r12;
    } catch (caughtException) {
        // ──────────────── Block 21 ──────────────── 
        // CODE → addr:355 | <Mov>: <Reg8: 6, Reg8: 12>
        // USED → r6 = caughtException;
        // CODE → addr:358 | <StoreToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 12>
        r1[2] = caughtException;
        // CODE → addr:362 | <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 3>
        r12 = r1[3];
        if (0 === r12) {
            // ──────────────── Block 23 ──────────────── 
            // CODE → addr:386 | <Throw>: <Reg8: 6>
            throw caughtException;
        } else {
            // ──────────────── Block 30 ──────────────── 
            // CODE → addr:249 | <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 2>
            // USED → r12 = r1[2];
            // CODE → addr:253 | <Mov>: <Reg8: 6, Reg8: 12>
            r6 = r1[2];
            // CODE → addr:256 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 11>
            r1[3] = 0;
            // CODE → addr:260 | <TryGetById>: <Reg8: 14, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r14 = console;
            // CODE → addr:266 | <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r13 = console.log;
            // CODE → addr:271 | <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 8>
            console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup");
            // CODE → addr:276 | <Throw>: <Reg8: 12>
            throw r1[2];
        }
    }
}