function switchTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4740>  # String: '__BC:ControlFlow/SwitchTests/switchTest/start' (String)
    // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:ControlFlow/SwitchTests/switchTest/start")
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    if (0 === param1) {
        // ──────────────── Block 9 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4736>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-0' (String)
        // USED → r1 = "__BC:ControlFlow/SwitchTests/switchTest/case-0";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        r1 = globalThis.console.log("__BC:ControlFlow/SwitchTests/switchTest/case-0")
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 583>  # String: 'zero' (String)
        // USED → r1 = "zero";
        // CODE → <Ret>: <Reg8: 1>
        return "zero";
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
        // USED → r0 = 1;
        if (1 === param1) {
            // ──────────────── Block 8 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
            // USED → r4 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
            // USED → r3 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 2, string_id: 2016>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-1' (String)
            // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/case-1";
            // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
            r2 = globalThis.console.log("__BC:ControlFlow/SwitchTests/switchTest/case-1")
            // CODE → <LoadConstString>: <Reg8: 2, string_id: 6715>  # String: 'one' (Identifier)
            // USED → r2 = "one";
            // CODE → <Ret>: <Reg8: 2>
            return "one";
        } else {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
            // USED → r0 = 2;
            if (2 === param1) {
                // ──────────────── Block 7 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
                // USED → r4 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
                // USED → r3 = globalThis.console.log;
                // CODE → <LoadConstString>: <Reg8: 2, string_id: 892>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-2' (String)
                // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/case-2";
                // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
                r2 = globalThis.console.log("__BC:ControlFlow/SwitchTests/switchTest/case-2")
                // CODE → <LoadConstString>: <Reg8: 2, string_id: 9021>  # String: 'two' (Identifier)
                // USED → r2 = "two";
                // CODE → <Ret>: <Reg8: 2>
                return "two";
            } else {
                // ──────────────── Block 3 ──────────────── 
                // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
                // USED → r0 = 3;
                if (3 === param1) {
                    // ──────────────── Block 6 ──────────────── 
                    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
                    // USED → r4 = globalThis.console;
                    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
                    // USED → r3 = globalThis.console.log;
                    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1730>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-3-4' (String)
                    // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/case-3-4";
                    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
                    r2 = globalThis.console.log("__BC:ControlFlow/SwitchTests/switchTest/case-3-4")
                    // CODE → <LoadConstString>: <Reg8: 2, string_id: 3942>  # String: 'three-four' (String)
                    // USED → r2 = "three-four";
                    // CODE → <Ret>: <Reg8: 2>
                    return "three-four";
                } else {
                    // ──────────────── Block 4 ──────────────── 
                    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 4>
                    // USED → r0 = 4;
                    // CODE → <JStrictEqual>: <Addr8: 30, Reg8: 0, Reg8: 2>  # Address: 00000058
                    if (4 === param1) goto label_88;
                    // ──────────────── Block 5 ──────────────── 
                    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
                    // USED → r4 = globalThis.console;
                    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
                    // USED → r3 = globalThis.console.log;
                    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4737>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-default' (String)
                    // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/case-default";
                    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
                    r2 = globalThis.console.log("__BC:ControlFlow/SwitchTests/switchTest/case-default")
                    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1856>  # String: 'other' (String)
                    // USED → r2 = "other";
                    // CODE → <Ret>: <Reg8: 2>
                    return "other";
                }
            }
        }
    }
}