function ifElseChainTest(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED → r2 = param2;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4552>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/start' (String)
    // USED → r3 = "__BC:ControlFlow/IfTests/ifElseChainTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:ControlFlow/IfTests/ifElseChainTest/start")
    if (!param1) {
        if (param1 || param2) {
            // ──────────────── Block 5 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
            // USED → r4 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
            // USED → r3 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 2, string_id: 4544>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-either' (String)
            // USED → r2 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-either";
            // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
            r2 = globalThis.console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-either")
            // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
            // USED → r4 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
            // USED → r3 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 2, string_id: 1884>  # String: 'either' (String)
            // USED → r2 = "either";
            // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
            r2 = globalThis.console.log("either")
            // CODE → <Jmp>: <Addr8: 42>  # Address: 000000a4
            goto label_164;
        } else {
            // ──────────────── Block 4 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
            // USED → r4 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
            // USED → r3 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 2, string_id: 4545>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-neither' (String)
            // USED → r2 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-neither";
            // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
            r2 = globalThis.console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-neither")
            // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
            // USED → r4 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
            // USED → r3 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 2, string_id: 1883>  # String: 'neither' (String)
            // USED → r2 = "neither";
            // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
            r2 = globalThis.console.log("neither")
            // CODE → <Jmp>: <Addr8: 84>  # Address: 000000a4
            goto label_164;
        }
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <JmpTrue>: <Addr8: 93, Reg8: 2>  # Address: 0000007c
        if (param2) goto label_124;
        // ──────────────── Block 6 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
        // USED → r3 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 4543>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-both' (String)
        // USED → r2 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-both";
        // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        r2 = globalThis.console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-both")
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
        // USED → r3 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 1173>  # String: 'both' (String)
        // USED → r2 = "both";
        // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        r2 = globalThis.console.log("both")
    }
    if (!param1) {
        // ──────────────── Block 8 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4547>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-not-a' (String)
        // USED → r1 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-not-a";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        r1 = globalThis.console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-not-a")
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 674>  # String: 'not a' (String)
        // USED → r1 = "not a";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        r1 = globalThis.console.log("not a")
    }
    // ──────────────── Block 9 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 308>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/IfTests/ifElseChainTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:ControlFlow/IfTests/ifElseChainTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}