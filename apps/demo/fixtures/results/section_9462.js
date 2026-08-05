function logicalShortCircuitTest(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED → r2 = param2;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4812>  # String: '__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/start' (String)
    // USED → r4 = "__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/start";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    r4 = globalThis.console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/start")
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 5126>  # String: 'and-left' (String)
    // USED → r4 = "and-left";
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 4811>  # String: '__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect' (String)
    // USED → r9 = "__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect";
    // CODE → <Call3>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 9, Reg8: 4>
    r4 = globalThis.console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect", "and-left")
    // CODE → <Mov>: <Reg8: 6, Reg8: 3>
    r6 = param1
    if (param1) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 7, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r7 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r5 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 4, string_id: 4971>  # String: 'and-right' (String)
        // USED → r4 = "and-right";
        // CODE → <Call3>: <Reg8: 4, Reg8: 5, Reg8: 7, Reg8: 9, Reg8: 4>
        r4 = globalThis.console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect", "and-right")
        // CODE → <Mov>: <Reg8: 6, Reg8: 2>
        // USED → r6 = param2;
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 1150>  # String: 'or-left' (String)
    // USED → r4 = "or-left";
    // CODE → <Call3>: <Reg8: 4, Reg8: 5, Reg8: 7, Reg8: 9, Reg8: 4>
    r4 = globalThis.console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect", "or-left")
    // CODE → <Mov>: <Reg8: 5, Reg8: 3>
    // USED → r5 = param1;
    if (!param1) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r8 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r7 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 4, string_id: 2476>  # String: 'or-right' (String)
        // USED → r4 = "or-right";
        // CODE → <Call3>: <Reg8: 4, Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 4>
        r4 = globalThis.console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect", "or-right")
        // CODE → <Mov>: <Reg8: 5, Reg8: 2>
        // USED → r5 = param2;
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 76>  # String: 'left' (Identifier)
    r4 = "left"
    if (param1) {
        // ──────────────── Block 5 ──────────────── 
        // CODE → <LoadConstNull>: <Reg8: 4>
        // USED → r4 = null;
    }
    // ──────────────── Block 6 ──────────────── 
    // CODE → <LoadConstNull>: <Reg8: 0>
    // USED → r0 = null;
    if (null == null) {
        // ──────────────── Block 7 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r8 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r7 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 3, string_id: 6243>  # String: 'nullish-right' (String)
        // USED → r3 = "nullish-right";
        // CODE → <Call3>: <Reg8: 3, Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 3>
        r3 = globalThis.console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect", "nullish-right")
        // CODE → <Mov>: <Reg8: 4, Reg8: 2>
        // USED → r4 = param2;
    }
    // ──────────────── Block 8 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call4>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6, Reg8: 5, Reg8: 4>
    r2 = globalThis.console.log(param2, param2, param2)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4809>  # String: '__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/end' (String)
    // USED → r1 = "__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}