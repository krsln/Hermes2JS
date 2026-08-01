function switchTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 3590>  # String: '__BC:ControlFlow/SwitchTests/switchTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/SwitchTests/switchTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    r1 = globalThis.console.log("__BC:ControlFlow/SwitchTests/switchTest/start")
    // CODE → <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // Switch → START
    switch (param1) {
        case 0:
            // ──────────────── Block 9 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r2 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r1 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 2212>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-0' (String)
            // USED → r0 = "__BC:ControlFlow/SwitchTests/switchTest/case-0";
            // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
            r0 = globalThis.console.log("__BC:ControlFlow/SwitchTests/switchTest/case-0")
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 615>  # String: 'zero' (String)
            // USED → r0 = "zero";
            // CODE → <Ret>: <Reg8: 0>
            return "zero";
        case 1:
            // ──────────────── Block 8 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 1, string_id: 352>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-1' (String)
            // USED → r1 = "__BC:ControlFlow/SwitchTests/switchTest/case-1";
            // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
            r1 = globalThis.console.log("__BC:ControlFlow/SwitchTests/switchTest/case-1")
            // CODE → <LoadConstString>: <Reg8: 1, string_id: 7531>  # String: 'one' (Identifier)
            // USED → r1 = "one";
            // CODE → <Ret>: <Reg8: 1>
            return "one";
        case 2:
            // ──────────────── Block 7 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 1, string_id: 946>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-2' (String)
            // USED → r1 = "__BC:ControlFlow/SwitchTests/switchTest/case-2";
            // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
            r1 = globalThis.console.log("__BC:ControlFlow/SwitchTests/switchTest/case-2")
            // CODE → <LoadConstString>: <Reg8: 1, string_id: 7725>  # String: 'two' (Identifier)
            // USED → r1 = "two";
            // CODE → <Ret>: <Reg8: 1>
            return "two";
        case 3:
            // ──────────────── Block 6 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 1, string_id: 1770>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-3-4' (String)
            // USED → r1 = "__BC:ControlFlow/SwitchTests/switchTest/case-3-4";
            // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
            r1 = globalThis.console.log("__BC:ControlFlow/SwitchTests/switchTest/case-3-4")
            // CODE → <LoadConstString>: <Reg8: 1, string_id: 5307>  # String: 'three-four' (String)
            // USED → r1 = "three-four";
            // CODE → <Ret>: <Reg8: 1>
            return "three-four";
        default:
            // ──────────────── Block 4 ──────────────── 
            // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 4>
            // USED → r1 = 4;
            // CODE → <JStrictEqual>: <Addr8: 30, Reg8: 1, Reg8: 2>  # Address: 00000058
            if (4 === param1) goto label_88;
            // ──────────────── Block 5 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 1, string_id: 4629>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-default' (String)
            // USED → r1 = "__BC:ControlFlow/SwitchTests/switchTest/case-default";
            // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
            r1 = globalThis.console.log("__BC:ControlFlow/SwitchTests/switchTest/case-default")
            // CODE → <LoadConstString>: <Reg8: 1, string_id: 1881>  # String: 'other' (String)
            // USED → r1 = "other";
            // CODE → <Ret>: <Reg8: 1>
            return "other";
    }
    // Switch → END
}