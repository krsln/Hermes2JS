function ifTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4734>  # String: '__BC:ControlFlow/IfTests/ifTest/start' (String)
    // USED → r4 = "__BC:ControlFlow/IfTests/ifTest/start";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    r4 = globalThis.console.log("__BC:ControlFlow/IfTests/ifTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 10>
    // USED → r0 = 10;
    if (param1 > 10) {
        // ──────────────── Block 6 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
        // USED → r5 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
        // USED → r4 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 3, string_id: 3380>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-big' (String)
        // USED → r3 = "__BC:ControlFlow/IfTests/ifTest/branch-big";
        // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
        r3 = globalThis.console.log("__BC:ControlFlow/IfTests/ifTest/branch-big")
        // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
        // USED → r5 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
        // USED → r4 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 3, string_id: 3055>  # String: 'big' (String)
        // USED → r3 = "big";
        // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
        r3 = globalThis.console.log("big")
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 5>
        // USED → r0 = 5;
        if (param1 > 5) {
            // ──────────────── Block 5 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
            // USED → r5 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
            // USED → r4 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 3, string_id: 4727>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-medium' (String)
            // USED → r3 = "__BC:ControlFlow/IfTests/ifTest/branch-medium";
            // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
            r3 = globalThis.console.log("__BC:ControlFlow/IfTests/ifTest/branch-medium")
            // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
            // USED → r5 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
            // USED → r4 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 3, string_id: 11037>  # String: 'medium' (Identifier)
            // USED → r3 = "medium";
            // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
            r3 = globalThis.console.log("medium")
            // CODE → <Jmp>: <Addr8: 42>  # Address: 000000d9
            goto label_217;
        } else {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <LoadConstZero>: <Reg8: 0>
            // USED → r0 = 0;
            if (param1 === 0) {
                // ──────────────── Block 4 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
                // USED → r5 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
                // USED → r4 = globalThis.console.log;
                // CODE → <LoadConstString>: <Reg8: 3, string_id: 4729>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-zero' (String)
                // USED → r3 = "__BC:ControlFlow/IfTests/ifTest/branch-zero";
                // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
                r3 = globalThis.console.log("__BC:ControlFlow/IfTests/ifTest/branch-zero")
                // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
                // USED → r5 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
                // USED → r4 = globalThis.console.log;
                // CODE → <LoadConstString>: <Reg8: 3, string_id: 583>  # String: 'zero' (String)
                // USED → r3 = "zero";
                // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
                r3 = globalThis.console.log("zero")
                // CODE → <Jmp>: <Addr8: 84>  # Address: 000000d9
                goto label_217;
            } else {
                // ──────────────── Block 3 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
                // USED → r5 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
                // USED → r4 = globalThis.console.log;
                // CODE → <LoadConstString>: <Reg8: 3, string_id: 4728>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-small' (String)
                // USED → r3 = "__BC:ControlFlow/IfTests/ifTest/branch-small";
                // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
                r3 = globalThis.console.log("__BC:ControlFlow/IfTests/ifTest/branch-small")
                // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
                // USED → r5 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
                // USED → r4 = globalThis.console.log;
                // CODE → <LoadConstString>: <Reg8: 3, string_id: 9413>  # String: 'small' (Identifier)
                // USED → r3 = "small";
                // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
                r3 = globalThis.console.log("small")
                // CODE → <JmpLong>: <Addr32: 129>  # Address: 000000d9
                goto label_217;
            }
        }
    }
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4731>  # String: '__BC:ControlFlow/IfTests/ifTest/end' (String)
    // USED → r2 = "__BC:ControlFlow/IfTests/ifTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:ControlFlow/IfTests/ifTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}