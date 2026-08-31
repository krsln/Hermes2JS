function logicalShortCircuitTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr:  3 | <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED → r2 = param2;
    // CODE → addr:  6 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  8 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 14 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 19 | <LoadConstString>: <Reg8: 4, string_id: 4812>  # String: '__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/start' (String)
    // USED → r4 = "__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/start";
    // CODE → addr: 23 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/start")
    // CODE → addr: 28 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 34 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 39 | <LoadConstString>: <Reg8: 4, string_id: 5126>  # String: 'and-left' (String)
    // USED → r4 = "and-left";
    // CODE → addr: 43 | <LoadConstString>: <Reg8: 9, string_id: 4811>  # String: '__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect' (String)
    // USED → r9 = "__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect";
    // CODE → addr: 47 | <Call3>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 9, Reg8: 4>
    console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect", "and-left")
    // CODE → addr: 53 | <Mov>: <Reg8: 6, Reg8: 3>
    r6 = param1 && param2
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 83 | <TryGetById>: <Reg8: 7, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr: 89 | <GetByIdShort>: <Reg8: 5, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 94 | <LoadConstString>: <Reg8: 4, string_id: 1150>  # String: 'or-left' (String)
    // USED → r4 = "or-left";
    // CODE → addr: 98 | <Call3>: <Reg8: 4, Reg8: 5, Reg8: 7, Reg8: 9, Reg8: 4>
    console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect", "or-left")
    // CODE → addr:104 | <Mov>: <Reg8: 5, Reg8: 3>
    // USED → r5 = param1 || param2;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:134 | <LoadConstString>: <Reg8: 4, string_id: 76>  # String: 'left' (Identifier)
    r4 = !param1 ? "left" : null
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:143 | <LoadConstNull>: <Reg8: 0>
    // USED → r0 = !param1 ? "left" : null;
    if (null == null) {
        // ──────────────── Block 7 ──────────────── 
        // CODE → addr:149 | <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r8 = console;
        // CODE → addr:155 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r7 = console.log;
        // CODE → addr:160 | <LoadConstString>: <Reg8: 3, string_id: 6243>  # String: 'nullish-right' (String)
        // USED → r3 = "nullish-right";
        // CODE → addr:164 | <Call3>: <Reg8: 3, Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 3>
        console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect", "nullish-right")
        // CODE → addr:170 | <Mov>: <Reg8: 4, Reg8: 2>
        r4 = param2
    }
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:173 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:179 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:184 | <Call4>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6, Reg8: 5, Reg8: 4>
    console.log(r6, r5, r4)
    // CODE → addr:191 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:197 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:202 | <LoadConstString>: <Reg8: 1, string_id: 4809>  # String: '__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/end' (String)
    // USED → r1 = "__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/end";
    // CODE → addr:206 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/end")
    // CODE → addr:211 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:213 | <Ret>: <Reg8: 0>
    return undefined;
}