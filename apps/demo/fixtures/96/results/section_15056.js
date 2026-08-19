function switchTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 1, string_id: 3590>  # String: '__BC:ControlFlow/SwitchTests/switchTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/SwitchTests/switchTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:ControlFlow/SwitchTests/switchTest/start")
    // CODE → addr: 25 | <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // Switch → START
    switch (param1) {
        case 0:
            // ──────────────── Block 9 ──────────────── 
            // CODE → addr:166 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r2 = console;
            // CODE → addr:172 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r1 = console.log;
            // CODE → addr:177 | <LoadConstString>: <Reg8: 0, string_id: 2212>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-0' (String)
            // USED → r0 = "__BC:ControlFlow/SwitchTests/switchTest/case-0";
            // CODE → addr:181 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
            console.log("__BC:ControlFlow/SwitchTests/switchTest/case-0")
            // CODE → addr:186 | <LoadConstString>: <Reg8: 0, string_id: 615>  # String: 'zero' (String)
            // USED → r0 = "zero";
            // CODE → addr:190 | <Ret>: <Reg8: 0>
            return "zero";
        case 1:
            // ──────────────── Block 8 ──────────────── 
            // CODE → addr:140 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = console;
            // CODE → addr:146 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = console.log;
            // CODE → addr:151 | <LoadConstString>: <Reg8: 1, string_id: 352>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-1' (String)
            // USED → r1 = "__BC:ControlFlow/SwitchTests/switchTest/case-1";
            // CODE → addr:155 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
            console.log("__BC:ControlFlow/SwitchTests/switchTest/case-1")
            // CODE → addr:160 | <LoadConstString>: <Reg8: 1, string_id: 7531>  # String: 'one' (Identifier)
            // USED → r1 = "one";
            // CODE → addr:164 | <Ret>: <Reg8: 1>
            return "one";
        case 2:
            // ──────────────── Block 7 ──────────────── 
            // CODE → addr:114 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = console;
            // CODE → addr:120 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = console.log;
            // CODE → addr:125 | <LoadConstString>: <Reg8: 1, string_id: 946>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-2' (String)
            // USED → r1 = "__BC:ControlFlow/SwitchTests/switchTest/case-2";
            // CODE → addr:129 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
            console.log("__BC:ControlFlow/SwitchTests/switchTest/case-2")
            // CODE → addr:134 | <LoadConstString>: <Reg8: 1, string_id: 7725>  # String: 'two' (Identifier)
            // USED → r1 = "two";
            // CODE → addr:138 | <Ret>: <Reg8: 1>
            return "two";
        case 3:
        case 4:
            // ──────────────── Block 6 ──────────────── 
            // CODE → addr: 88 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = console;
            // CODE → addr: 94 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = console.log;
            // CODE → addr: 99 | <LoadConstString>: <Reg8: 1, string_id: 1770>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-3-4' (String)
            // USED → r1 = "__BC:ControlFlow/SwitchTests/switchTest/case-3-4";
            // CODE → addr:103 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
            console.log("__BC:ControlFlow/SwitchTests/switchTest/case-3-4")
            // CODE → addr:108 | <LoadConstString>: <Reg8: 1, string_id: 5307>  # String: 'three-four' (String)
            // USED → r1 = "three-four";
            // CODE → addr:112 | <Ret>: <Reg8: 1>
            return "three-four";
        default:
            // ──────────────── Block 5 ──────────────── 
            // CODE → addr: 62 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = console;
            // CODE → addr: 68 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = console.log;
            // CODE → addr: 73 | <LoadConstString>: <Reg8: 1, string_id: 4629>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-default' (String)
            // USED → r1 = "__BC:ControlFlow/SwitchTests/switchTest/case-default";
            // CODE → addr: 77 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
            console.log("__BC:ControlFlow/SwitchTests/switchTest/case-default")
            // CODE → addr: 82 | <LoadConstString>: <Reg8: 1, string_id: 1881>  # String: 'other' (String)
            // USED → r1 = "other";
            // CODE → addr: 86 | <Ret>: <Reg8: 1>
            return "other";
    }
    // Switch → END
}