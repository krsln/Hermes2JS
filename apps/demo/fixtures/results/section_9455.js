function ifElseChainTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 2>
    // USED → r3 = param2;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4773>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/start' (String)
    // USED → r4 = "__BC:ControlFlow/IfTests/ifElseChainTest/start";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/start")
    if (param1 && param2) {
        // ──────────────── Block 6 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r5 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r4 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 3, string_id: 4768>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-both' (String)
        // USED → r3 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-both";
        // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
        console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-both")
        // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r5 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r4 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 3, string_id: 381>  # String: 'both' (String)
        // USED → r3 = "both";
        // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
        console.log("both")
    } else if (param1 || param2) {
        // ──────────────── Block 5 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r5 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r4 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 3, string_id: 4769>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-either' (String)
        // USED → r3 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-either";
        // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
        console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-either")
        // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r5 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r4 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 3, string_id: 1890>  # String: 'either' (String)
        // USED → r3 = "either";
        // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
        console.log("either")
    } else {
        // ──────────────── Block 4 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r5 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r4 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 3, string_id: 4770>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-neither' (String)
        // USED → r3 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-neither";
        // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
        console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-neither")
        // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r5 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r4 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 3, string_id: 1889>  # String: 'neither' (String)
        // USED → r3 = "neither";
        // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
        console.log("neither")
    }
    if (!param1) {
        // ──────────────── Block 8 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r3 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 4771>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-not-a' (String)
        // USED → r2 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-not-a";
        // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-not-a")
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r3 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 669>  # String: 'not a' (String)
        // USED → r2 = "not a";
        // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        console.log("not a")
    }
    // ──────────────── Block 9 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 2026>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/end' (String)
    // USED → r1 = "__BC:ControlFlow/IfTests/ifElseChainTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}